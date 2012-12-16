import tempfile

versionNum = "1.10"
version = "MX Cart %sbeta" %(versionNum)

name = ""
nameNotAllowedMsg = "Names cannot begin with REGION_ or region_."
description = ""

indir = ""
outdir = ""
__tempdir = "/__MXCART"

def getTempDir():
    return (tempfile.gettempdir() + __tempdir).replace("\\","/")

quantize = False

lstBsbFiles = []
lstBsbErrorFiles = []
numBsbFiles = 0
numBsbMB = 0.0
numChartsMerge = 0

CleanupMessage = "Cleaning up MX Cart temp directory... \n " + \
                 "Please wait."
CancelConfirmMsg = "Are you sure you'd like to quit?"
BSBSearchMsg = "Searching for BSB/.KAP files.\n" + \
               "Please wait..."


Step4ComfirmMsg = "We are about to create a new MX Mariner region using:\n" + \
                  "%s BSBv3 files totaling %s megabytes\n\n" + \
                  "BSBv3 directory:\n" + \
                  "%s \n\n" + \
                  "The MX Mariner region data will be created in directory:\n" +\
                  "%s \n\n" + \
                  "Name: %s\n" + \
                  "Description: %s\n\n" + \
                  "This is your last chance to go back as this process can take some time.\n" + \
                  "Would you like to continue ?"

__Stage1Msg = "Stage 1 of 5 : Creating Tiles\n\n" + \
               "Tiling BSB chart %s of %s"
__Stage2Msg = "Stage 2 of 5 : Merging Tiles"
__Stage3Msg = "Stage 3 of 5 : Quantizing Tiles"
__Stage4Msg = "Stage 4 of 5 : Concatenating Tiles"
__Stage5Msg = "Stage 5 of 5 : Generating Data"
def getStageMsg(stage=1):
    if stage>5:
        return __Stage1Msg
    return (__Stage1Msg, __Stage2Msg, __Stage3Msg, __Stage4Msg, __Stage5Msg)[stage-1]

ResultsMsg = "%s of %s charts successfully imported.\n" + \
             "Please upload %s and %s to the \"mxmariner\"\n" + \
             "directory on your Android device and re-launch\n" + \
             "MX Mariner.  The new data will be automatically installed."
             
if __name__ == "__main__":
     print getTempDir()