from BsbScales import BsbScales
from FilePathSearch import RecursiveSearch
from Helper_Gdal import KapToVrt
from Helper_Tiler import VrtToTiles
from Helper_Merge import Merge
from MyGemfBuilder import main as GemfBuilder
from threading import Thread, enumerate
from time import sleep
from subprocess import Popen
import GUI
import Resources
import re
import os.path
import shutil
import FindZoom
import GenerateData
import wx.lib.newevent
import platform
from multiprocessing import Process

if platform.system() == "Windows":
    from multiprocessing import freeze_support

ConfirmEvent, EVT_CONFIRMATION = wx.lib.newevent.NewEvent()
InThreadEvent, EVT_IN_THREAD = wx.lib.newevent.NewEvent()

class BlankParent(GUI.BlankParent):
    pass

class Spinner(GUI.Spinner):
    def setMessage(self, message):
        self.msg_staticText.SetLabel(message)
        self.SetSizer(self.bSizer)
        self.Layout()
        self.bSizer.Fit(self)
        
    def Play(self):
        self.spinner_animCtrl.Play()

class Message(GUI.Message):
    def setMessage(self, message):
        self.msg_staticText.SetLabel(message)
        self.SetSizer(self.bSizer)
        self.Layout()
        self.bSizer.Fit(self)
    
    def _evtOk(self, event):
        event.Skip()
        self.Destroy()
        
class Confirm(GUI.Confirm):
    def setMessage(self, message):
        self.msg_staticText.SetLabel(message)
        self.SetSizer(self.bSizer)
        self.Layout()
        self.bSizer.Fit(self)
    
    def _evtYes(self, event):
        newEvent = ConfirmEvent(attr1=True)
        wx.PostEvent(self.GetParent(), newEvent)
        self.Destroy()
        
    def _evtNo(self, event):
        newEvent = ConfirmEvent(attr1=False)
        wx.PostEvent(self.GetParent(), newEvent)
        self.Destroy()
        
class InDirDialog(GUI.InDirDialog):
    #Pick the BSB input directory
    def _evtNext(self, event):
        dialog = OutDirDialog(None)
        dialog.out_dirPicker.SetPath(Resources.outdir)
        
        self.spinner = Spinner(self)
        self.Bind(EVT_IN_THREAD, self.searchFinishHandler)
        EVT_IN_THREAD(app, self.searchFinishHandler)
        bsbSearchThread = Thread(target=BSBSearch)
        bsbSearchThread.start()
        self.spinner.setMessage(Resources.BSBSearchMsg)
        self.spinner.Play()
        self.spinner.ShowModal()
        
        if (Resources.outdir != ""):
            dialog.next_button.Enable()
        dialog.Show()
        self.Destroy()
        
    def _evtCancel(self, event):
        confirm = Confirm(self)
        confirm.setMessage(Resources.CancelConfirmMsg)
        self.Bind(EVT_CONFIRMATION, self.cancelHandler)
        EVT_CONFIRMATION(self, self.cancelHandler)
        confirm.ShowModal()
        
    def cancelHandler(self, event):
        if (event.attr1):
            self.Destroy()
            blankParent.Destroy()
            
    def searchFinishHandler(self, event):
        self.spinner.Destroy()
        
    def _evtDir(self, event):
        Resources.indir = self.in_dirPicker.GetPath().replace("\\", "/")
        self.next_button.Enable()
        
class OutDirDialog(GUI.OutDirDialog):
    #Pick the BSB output directory
    def _evtBack(self, event):
        dialog = InDirDialog(None);
        dialog.in_dirPicker.SetPath(Resources.indir)
        dialog.next_button.Enable()
        dialog.Show()
        self.Destroy()
    
    def _evtNext(self, event):
        dialog = NameDialog(None)
        dialog.name_textCtrl.SetValue(Resources.name)
        dialog.descs_textCtrl.SetValue(Resources.description)
        dialog.Show()
        self.Destroy()
        
    def _evtCancel(self, event):
        confirm = Confirm(self)
        confirm.setMessage(Resources.CancelConfirmMsg)
        self.Bind(EVT_CONFIRMATION, self.cancelHandler)
        EVT_CONFIRMATION(self, self.cancelHandler)
        confirm.ShowModal()
        
    def cancelHandler(self, event):
        if (event.attr1):
            self.Destroy()
            blankParent.Destroy()
        
    def _evtDir(self, event):
        Resources.outdir = self.out_dirPicker.GetPath()
        self.next_button.Enable()

class NameDialog(GUI.NameDialog):
    #Set the name and description
    def _evtBack(self, event):
        dialog = OutDirDialog(None)
        dialog.out_dirPicker.SetPath(Resources.outdir)
        dialog.next_button.Enable()
        dialog.Show()
        self.Destroy()
    
    def _evtNext(self, event):
        confirm = Confirm(self)
        confirm.setMessage(Resources.Step4ComfirmMsg % (Resources.numBsbFiles, Resources.numBsbMB, Resources.indir, Resources.outdir, Resources.name, Resources.description))
        self.Bind(EVT_CONFIRMATION, self.nextHandler)
        EVT_CONFIRMATION(self, self.nextHandler)
        confirm.ShowModal()
        
    def _evtCancel(self, event):
        confirm = Confirm(self)
        confirm.setMessage(Resources.CancelConfirmMsg)
        self.Bind(EVT_CONFIRMATION, self.cancelHandler)
        EVT_CONFIRMATION(self, self.cancelHandler)
        confirm.ShowModal()
        
    def cancelHandler(self, event):
        if (event.attr1):
            self.Destroy()
            blankParent.Destroy()
            
    def nextHandler(self, event):
        if (event.attr1):
            dialog = ProcessDialog(None)
            dialog.Initialize()
            dialog.Show()
            self.Destroy()
        
    def _evtCompress(self, event):
        Resources.quantize = self.pngnq_checkBox.GetValue()
    
    def _evtEntry(self, event):
        
        if event.GetEventObject() == self.name_textCtrl:
            replaceChar = "_"
            useUpper = True
        else:
            replaceChar = " "
            useUpper = False
        
        val = str(event.GetEventObject().GetValue())
        if useUpper:
            newval = re.sub(r'\W+', replaceChar, val).lstrip().upper() #remove any non words and force uppercase
        else:
            newval = re.sub(r'\W+', replaceChar, val).lstrip() #remove any non words
        if newval != val:
            event.GetEventObject().SetValue(newval)
            event.GetEventObject().SetInsertionPointEnd()
        Resources.name = self.name_textCtrl.GetValue()
        Resources.description = self.descs_textCtrl.GetValue()
        if len(Resources.name) > 0 and len(Resources.description) > 0:
            self.next_button.Enable()
        else:
            self.next_button.Disable()
        if Resources.name.upper().startswith("REGION_"):
            message = Message(self)
            message.setMessage(Resources.nameNotAllowedMsg)
            self.name_textCtrl.SetValue("")
            message.ShowModal()

class ProcessDialog(GUI.ProcessDialog):
    def Initialize(self):
        self.currentChart = 1
        self.stage = 1
        self.Bind(EVT_IN_THREAD, self.nextStage)
        EVT_IN_THREAD(app, self.nextStage)
        self.SetStage()
        
    def SetStage(self):        
        if (self.stage == 1):
            makeTiles = Thread(target=MakeTiles)
            makeTiles.setName("makeTiles")
            #makeTiles.setDaemon(False) #python won't wait for thread to terminate if daemon
            makeTiles.start()
            msg = Resources.getStageMsg(self.stage) % (self.currentChart, Resources.numBsbFiles)
            
        if (self.stage == 2):
            mergeTiles = Thread(target=MergeTiles)
            mergeTiles.setName("mergeTiles")
            #mergeTiles.setDaemon(False) #python won't wait for thread to terminate if daemon
            mergeTiles.start()
            msg = Resources.getStageMsg(self.stage)
            
        if (self.stage == 3):
            quanTiles = Thread(target=QuantTiles)
            quanTiles.setName("quanTiles")
            #quanTiles.setDaemon(False) #python won't wait for thread to terminate if daemon
            quanTiles.start()
            msg = Resources.getStageMsg(self.stage)
            
        if (self.stage == 4):
            concatTiles = Thread(target=ConcatTiles)
            concatTiles.setName("concatTiles")
            #concatTiles.setDaemon(False) #python won't wait for thread to terminate if daemon
            concatTiles.start()
            msg = Resources.getStageMsg(self.stage)
            
        if (self.stage == 5):
            genData = Thread(target=GenData)
            genData.setName("genData")
            #genData.setDaemon(False) #python won't wait for thread to terminate if daemon
            genData.start()
            msg = Resources.getStageMsg(self.stage)
            
        self.step4Msg_staticText.SetLabel(msg)
        self.SetSizer(self.bSizer)
        self.Layout()
        self.bSizer.Fit(self)
    
    def _evtCancel(self, event):
        confirm = Confirm(self)
        confirm.setMessage(Resources.CancelConfirmMsg)
        self.Bind(EVT_CONFIRMATION, self.cancelHandler)
        EVT_CONFIRMATION(self, self.cancelHandler)
        confirm.ShowModal()
        
    def cancelHandler(self, event):
        if (event.attr1):
            print "Cancelling tasks and cleaning up... please wait."
            global pleaseContinue
            pleaseContinue = False
            if platform.system() == "Windows":
                self.Hide()
#            if platform.system() == "Linux":
#                msgDialog = GUI.Message2(None)
#                msgDialog.msg_staticText.SetLabel("Cleaning up... please wait.")
#                msgDialog.Show()
            
            for thread in enumerate():
                if thread.getName() != "MainThread":
                    if thread.isAlive():
                        #print "Joining thread: " + thread.getName()
                        thread.join()
            
            if os.path.isdir(Resources.getTempDir()):
                #print "Removing temporary directory", os.path.abspath(Resources.getTempDir())
                shutil.rmtree(os.path.abspath(Resources.getTempDir()))
                    
#            if platform.system() == "Linux":
#                msgDialog.Destroy()
                
            self.Destroy()
            blankParent.Destroy()
            
    def nextStage(self, event):
        #print "nextStage", event.advance
        if event.advance:
            if self.stage == 5:
                dialog = ResultsDialog(None)
                dialog.setResultMessage()
                dialog.Show()
                self.Destroy()
            else:
                self.stage += 1
                self.SetStage()
        if not event.advance:
            self.currentChart += 1
            self.step4Msg_staticText.SetLabel(Resources.getStageMsg(1) % (self.currentChart, Resources.numBsbFiles))

class ResultsDialog(GUI.ResultsDialog):
    def setResultMessage(self):
        numImported = Resources.numBsbFiles - len(Resources.lstBsbErrorFiles)
        gemfName = Resources.name + ".gemf"
        dataName = Resources.name + ".zdat"
        if len(Resources.lstBsbErrorFiles) > 0:
            print "the following BSB charts could not be read and were skipped:"
            for bsbFile in Resources.lstBsbErrorFiles:
                print bsbFile
        self.results_staticText.SetLabel(Resources.ResultsMsg % (numImported, Resources.numBsbFiles, gemfName, dataName))
        self.SetSizer(self.bSizer)
        self.Layout()
        self.bSizer.Fit(self)
        
    def _evtFinish(self, event):
        self.Hide()
        
        if os.path.isdir( os.path.abspath(Resources.getTempDir()) ):
            print "Cleaning up temporary directory: ", os.path.abspath(Resources.getTempDir())
            print "Please wait..."
            shutil.rmtree(os.path.abspath(Resources.getTempDir()))
        print "complete, bye now :)"
        self.Destroy()
        blankParent.Destroy()

#class Dialog(GUI.Dialog):
#    def setStep(self, panel, child=None):
#        self.bSizer.Add(panel)
#        self.SetSizer(self.bSizer)
#        self.Layout()
#        self.bSizer.Fit(self)
#        if child != None:
#            child.Destroy()
#    
#    def _evtCancel(self, event):
#        self.Destroy()
#        
#    def _evtDir(self, event):
#        self.next_button.Enable()
#        print self.in_dirPicker.GetPath(), " selected as BSB directory"
#            
#    def _evtNext(self, event):
#        pass
    
class About(GUI.About):
    def _evtAccept(self, event):
        dialog = InDirDialog(blankParent);
        dialog.Show()
        self.Hide()
        self.Destroy()
        
    def _evtDecline(self, event):
        self.Destroy()
        blankParent.Destroy()

def BSBSearch():
    mSearch = RecursiveSearch(Resources.indir)
    Resources.lstBsbFiles = mSearch.getFilePaths()
    Resources.numBsbFiles = mSearch.getNumFiles()
    Resources.numBsbMB = mSearch.getMegaBytes()
    
    wx.PostEvent(app, InThreadEvent())

def MakeTiles():
    ### STAGE 1 ###
    
    for kapPath in Resources.lstBsbFiles:
        if pleaseContinue:
            
            #we need to wait for this process to finish before moving on
            kapToVrtProc = Process(target=KapToVrt, args=(kapPath,))
            kapToVrtProc.start()
            while kapToVrtProc.is_alive():
                sleep(.1)
            
            vrtPath = kapPath[0:-4] + ".vrt"
            #print vrtPath
            if os.path.isfile(vrtPath):
                
                zxyFullPath = Resources.getTempDir() + "/" + kapPath.split("/")[-1][0:-4] + ".zxy/"
                tileError = True
                
                try:
                    vrtToTilesProc = Process(target=VrtToTiles, args=(Resources.getTempDir(), vrtPath, FindZoom.getKapZoom(kapPath),))
                    vrtToTilesProc.start()
                    while vrtToTilesProc.is_alive():
                        sleep(.1)
                    if os.path.isdir(zxyFullPath):
        #                    if len(os.listdir(zxyFullPath)) > 0:
        #                        tileError = False
                        for subDir in os.listdir(zxyFullPath):
                            if os.path.isdir(zxyFullPath + subDir):
                                tileError = False
                except:
                    pass
                    print "VrtToTiles failed!"
                    
                if tileError:
                        print "ERROR gdal_tiler failed processing chart: ", kapPath.split("/")[-1]
                        Resources.lstBsbErrorFiles.append(kapPath.split("/")[-1][0:-4]) 
                ###
                
                os.remove(vrtPath) #clean up vrt files
            else:
                ###map2gdal failed because there is no vrt file...
                print vrtPath
                print "ERROR map2gdal failed processing chart: ", kapPath.split("/")[-1]
                Resources.lstBsbErrorFiles.append(kapPath.split("/")[-1][0:-4])
            
            
#            mp = Process(target=TileMap, args=(kapPath, parent.currentChart, resourcePipeB, signalPipeA))
#            mp.start()
            
            #Event is bound to Step4.nextStage(self, event)
            wx.PostEvent(app, InThreadEvent(advance=False))
    
    #posting this event signals to parent window that the task is finished
    if pleaseContinue:
        #Event is bound to Step4.nextStage(self, event)
        wx.PostEvent(app, InThreadEvent(advance=True))
    
def MergeTiles():
    ### STAGE 2 ###
    bsbScales = BsbScales(Resources.indir)
    sortList = bsbScales.getKapsSortedByScale(".zxy")
    for errorBsbFile in Resources.lstBsbErrorFiles:
        if sortList.__contains__(errorBsbFile + ".zxy"):
            sortList.remove(errorBsbFile + ".zxy")
    sortList.reverse()
    Resources.numChartsMerge = len(sortList)
    if Resources.numChartsMerge > 0:
        moPath = Resources.getTempDir() + "/mergeorder.txt"
        if os.path.isfile(moPath):
            os.remove(moPath)
        moFile = open(moPath, "w")
        for line in sortList:
            if os.path.isdir(Resources.getTempDir() + "/" + line):
                moFile.write(Resources.getTempDir() + "/" + line + "\n")
            else:
                pass
                #print "missing tileset: " + line
        moFile.close()
        
        Merge(Resources.getTempDir() + "/merge", moPath)
    
    if pleaseContinue:
        wx.PostEvent(app, InThreadEvent(advance=True))

def QuantTiles():
    ### STAGE 3 ###
    
    if Resources.quantize:
        print "Quantizing generated tiles with pngnq..."
        pngList = RecursiveSearch(Resources.getTempDir() + "/merge", ".png")
        for pngPath in pngList.getFilePaths():
            pngPath = pngPath.replace("\\","/")
            #print pngPath
            if platform.system() == "Windows":
                thisone = Popen([os.getcwd().replace("\\","/")+'/pngnqi.exe','-s1','-g2.2','-n','256','-e','.nq8',pngPath])
                #thisone = Popen([os.path.abspath(os.curdir).replace("\\","/")+'/pngnqi.exe','-s1','-g2.2','-n','256','-e','.nq8',pngPath])
            if platform.system() == "Linux":
                thisone = Popen(['pngnq','-s1','-g2.2','-n','256','-e','.nq8', pngPath])
            thisone.wait()
            os.remove(pngPath)
            os.rename(pngPath.replace(".png", ".nq8"), pngPath)
            if not pleaseContinue:
                break
                wx.PostEvent(app, InThreadEvent(advance=False))
    if pleaseContinue:
        print "Quantization finished"
        wx.PostEvent(app, InThreadEvent(advance=True))

def ConcatTiles():
    ### STAGE 4 ###
    if Resources.numChartsMerge > 0:
        directory = Resources.getTempDir() + "/gemf"
        if not os.path.isdir(directory):
            os.mkdir(directory)
        shutil.move(Resources.getTempDir() + "/merge", directory)
        
        GemfBuilder( (directory,) )
        shutil.move(directory + "/map_data.gemf", Resources.outdir + "/" + Resources.name + ".gemf")
    
    if pleaseContinue:
        wx.PostEvent(app, InThreadEvent(advance=True))

def GenData():
    ### STAGE 5 ###
    if Resources.numChartsMerge > 0:
        myFilter = []
        for ea in Resources.lstBsbFiles:
            if Resources.lstBsbErrorFiles.__contains__(ea.split("/")[-1][0:-4]):
                Resources.lstBsbFiles.remove(ea)
            else:
                myFilter.append(ea.split("/")[-1])
        
        GenerateData.generateRegion(Resources.name, Resources.description, Resources.indir, Resources.outdir, myFilter)
    
    if pleaseContinue:
        wx.PostEvent(app, InThreadEvent(advance=True))

if __name__ == "__main__":
    if platform.system() == "Windows":
        freeze_support()
    else:
        import sys
        sys.path.append(os.path.dirname(os.path.abspath(__file__)) +"/my_tilers_tools")
       
    global pleaseContinue
    global app   
    app = wx.App(redirect=False)
    
    print "MXCart Initialized ..."
    print "If you experience problems, please email the contents of this window to manimaul@gmail.com"
    
     
    pleaseContinue = True    
    
    blankParent = BlankParent(None)
    
    about = About(blankParent)
    about.title_staticText.SetLabel(Resources.version)
    about.Show()
    
    if not os.path.isdir(Resources.getTempDir()):
        #print "Making temporary directory", os.path.abspath(Resources.getTempDir())
        os.makedirs(Resources.getTempDir())
    else:
        #print "Cleaning out temp directory"
        shutil.rmtree(Resources.getTempDir(), ignore_errors=True)
    
    app.MainLoop()
