# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate

###########################################################################
## Class About
###########################################################################

class About ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MXCart", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.title_staticText = wx.StaticText( self, wx.ID_ANY, u"About MX Cart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title_staticText.Wrap( -1 )
		self.title_staticText.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12.Add( self.title_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline51 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Chart import utility for MX Mariner", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer12.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"MX Mariner Website", u"http://www.mxmariner.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		bSizer12.Add( self.m_hyperlink1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer1.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../share/mxcart/kattegat.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.m_scrolledWindow1.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_scrolledWindow1.SetMinSize( wx.Size( -1,300 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.aboutTitle_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"About:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aboutTitle_staticText.Wrap( -1 )
		self.aboutTitle_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.aboutTitle_staticText, 0, wx.ALL, 5 )
		
		self.about_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"MXCart will read and convert most BSB version 2 and 3 charts.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.about_staticText.Wrap( -1 )
		bSizer2.Add( self.about_staticText, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Converted charts are exported to a file compatible with MX Mariner.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.creditsTitle_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Credits:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.creditsTitle_staticText.Wrap( -1 )
		self.creditsTitle_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.creditsTitle_staticText, 0, wx.ALL, 5 )
		
		self.credits_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"GDAL - Frank Warmerdam\nGDAL Tiler - Klokan Petr Pridal\nGEMF - Allen Budden\nLibbsb - Suart Cunningham\nMXCart - Will Kamp\npngnq - Stuart Coyle\nPython - Guido Van Rossum\nTilers Tools - Vadim Shlyakhov\nWXPython - Robin Dunn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.credits_staticText.Wrap( -1 )
		bSizer2.Add( self.credits_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.licenseTitle_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"License:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.licenseTitle_staticText.Wrap( -1 )
		self.licenseTitle_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.licenseTitle_staticText, 0, wx.ALL, 5 )
		
		self.license_staticText15 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SIMPLIFIED BSD LICENSE\n\nCopyright (c) 2012, Will Kamp\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met: \n\n1. Redistributions of source code must retain the above copyright notice, this\n   list of conditions and the following disclaimer. \n2. Redistributions in binary form must reproduce the above copyright notice,\n   this list of conditions and the following disclaimer in the documentation\n   and/or other materials provided with the distribution. \n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND\nANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\nWARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR\nANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\nLOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\nON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\nSOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n\nThe views and conclusions contained in the software and documentation are those\nof the authors and should not be interpreted as representing official policies, \neither expressed or implied, of the WILL KAMP.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.license_staticText15.Wrap( -1 )
		bSizer2.Add( self.license_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer2 )
		self.m_scrolledWindow1.Layout()
		bSizer2.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.accept_button = wx.Button( self, wx.ID_ANY, u"Accept", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.accept_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.decline_button = wx.Button( self, wx.ID_ANY, u"Decline", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.decline_button, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtDecline )
		self.accept_button.Bind( wx.EVT_BUTTON, self._evtAccept )
		self.decline_button.Bind( wx.EVT_BUTTON, self._evtDecline )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtDecline( self, event ):
		event.Skip()
	
	def _evtAccept( self, event ):
		event.Skip()
	
	

###########################################################################
## Class InDirDialog
###########################################################################

class InDirDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MX Cart - Input", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.step1_staticText = wx.StaticText( self, wx.ID_ANY, u"Please select a directory containing BSB version 3 (.KAP/.kap files) nautical charts. \n\nAll subdirectories will be included.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.step1_staticText.Wrap( -1 )
		bSizer.Add( self.step1_staticText, 0, wx.ALL, 5 )
		
		self.in_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer.Add( self.in_dirPicker, 0, wx.ALL, 5 )
		
		fgSizer = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.next_button = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.next_button.Enable( False )
		
		fgSizer.Add( self.next_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		
		bSizer.Add( fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.in_dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self._evtDir )
		self.next_button.Bind( wx.EVT_BUTTON, self._evtNext )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtDir( self, event ):
		event.Skip()
	
	def _evtNext( self, event ):
		event.Skip()
	
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class OutDirDialog
###########################################################################

class OutDirDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MX Cart - Output", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.step2_staticText = wx.StaticText( self, wx.ID_ANY, u"Please select a directory where to save the \nMX Mariner region files that will be created.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.step2_staticText.Wrap( -1 )
		bSizer.Add( self.step2_staticText, 0, wx.ALL, 5 )
		
		self.out_dirPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer.Add( self.out_dirPicker, 0, wx.ALL, 5 )
		
		fgSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.back_button = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.back_button, 0, wx.ALL, 5 )
		
		self.next_button = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.next_button.Enable( False )
		
		fgSizer.Add( self.next_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		
		bSizer.Add( fgSizer, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.out_dirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self._evtDir )
		self.back_button.Bind( wx.EVT_BUTTON, self._evtBack )
		self.next_button.Bind( wx.EVT_BUTTON, self._evtNext )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtDir( self, event ):
		event.Skip()
	
	def _evtBack( self, event ):
		event.Skip()
	
	def _evtNext( self, event ):
		event.Skip()
	
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class NameDialog
###########################################################################

class NameDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MX Cart - Name", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.step3_staticText = wx.StaticText( self, wx.ID_ANY, u"Please specify a name and description for the region.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.step3_staticText.Wrap( -1 )
		bSizer1.Add( self.step3_staticText, 0, wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.name_staticText = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_staticText.Wrap( -1 )
		fgSizer1.Add( self.name_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.name_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.name_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.descs_staticText = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.descs_staticText.Wrap( -1 )
		fgSizer1.Add( self.descs_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.descs_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.descs_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer1.Add( fgSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.pngnq_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Compress region", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.pngnq_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Warning: Compression requires much more proccessing time and power.\nHowever, it will reduce region size by approximately 50 percent.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer1.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.back_button = wx.Button( self, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.back_button, 0, wx.ALL, 5 )
		
		self.next_button = wx.Button( self, wx.ID_ANY, u"Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.next_button.Enable( False )
		
		fgSizer2.Add( self.next_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.name_textCtrl.Bind( wx.EVT_TEXT, self._evtEntry )
		self.descs_textCtrl.Bind( wx.EVT_TEXT, self._evtEntry )
		self.pngnq_checkBox.Bind( wx.EVT_CHECKBOX, self._evtCompress )
		self.back_button.Bind( wx.EVT_BUTTON, self._evtBack )
		self.next_button.Bind( wx.EVT_BUTTON, self._evtNext )
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtEntry( self, event ):
		event.Skip()
	
	
	def _evtCompress( self, event ):
		event.Skip()
	
	def _evtBack( self, event ):
		event.Skip()
	
	def _evtNext( self, event ):
		event.Skip()
	
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ProcessDialog
###########################################################################

class ProcessDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MX Cart - Processing", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.step4_staticText = wx.StaticText( self, wx.ID_ANY, u"Please be patient...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.step4_staticText.Wrap( -1 )
		self.bSizer.Add( self.step4_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.spinner_animCtrl = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE )
		self.spinner_animCtrl.LoadFile( u"/usr/local/share/mxcart/spinner.gif" )
		
		self.spinner_animCtrl.Play()
		self.bSizer.Add( self.spinner_animCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.step4Msg_staticText = wx.StaticText( self, wx.ID_ANY, u"Stage 1 of 5 : Creating Tiles\nProcessing chart ? of ?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.step4Msg_staticText.Wrap( -1 )
		self.step4Msg_staticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		self.bSizer.Add( self.step4Msg_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer.Add( self.cancel_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancel_button.Bind( wx.EVT_BUTTON, self._evtCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ResultsDialog
###########################################################################

class ResultsDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MX Cart - Results", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.results_staticText = wx.StaticText( self, wx.ID_ANY, u"x of x charts successfully imported.\nPlease upload ?.gemf and ?.data to the mxmariner\ndirectory on your Android device and re-launch\nMX Mariner.  The new data will be automatically installed.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.results_staticText.Wrap( -1 )
		self.bSizer.Add( self.results_staticText, 0, wx.ALL, 5 )
		
		self.finish_button = wx.Button( self, wx.ID_ANY, u"Finish", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer.Add( self.finish_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.finish_button.Bind( wx.EVT_BUTTON, self._evtFinish )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtFinish( self, event ):
		event.Skip()
	

###########################################################################
## Class Confirm
###########################################################################

class Confirm ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MXCart", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.msg_staticText = wx.StaticText( self, wx.ID_ANY, u"some message here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.msg_staticText.Wrap( -1 )
		self.bSizer.Add( self.msg_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.m_button21, 0, wx.ALL, 5 )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer.Add( self.m_button22, 0, wx.ALL, 5 )
		
		
		self.bSizer.Add( fgSizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtNo )
		self.m_button21.Bind( wx.EVT_BUTTON, self._evtYes )
		self.m_button22.Bind( wx.EVT_BUTTON, self._evtNo )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtNo( self, event ):
		event.Skip()
	
	def _evtYes( self, event ):
		event.Skip()
	
	

###########################################################################
## Class Message
###########################################################################

class Message ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"MXCart", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.msg_staticText = wx.StaticText( self, wx.ID_ANY, u"some message here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.msg_staticText.Wrap( -1 )
		self.bSizer.Add( self.msg_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.ok_button = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSizer.Add( self.ok_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self._evtOk )
		self.ok_button.Bind( wx.EVT_BUTTON, self._evtOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def _evtOk( self, event ):
		event.Skip()
	
	

###########################################################################
## Class Spinner
###########################################################################

class Spinner ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.msg_staticText = wx.StaticText( self, wx.ID_ANY, u"some message goes here!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.msg_staticText.Wrap( -1 )
		self.bSizer.Add( self.msg_staticText, 0, wx.ALL, 5 )
		
		self.spinner_animCtrl = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE ) 
		
		self.spinner_animCtrl.Play()
		self.bSizer.Add( self.spinner_animCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.spinner_animCtrl1 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE )
		self.spinner_animCtrl1.LoadFile( u"/usr/local/share/mxcart/spinner.gif" )
		
		self.spinner_animCtrl1.Play()
		self.bSizer.Add( self.spinner_animCtrl1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Message2
###########################################################################

class Message2 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.msg_staticText = wx.StaticText( self, wx.ID_ANY, u"some message goes here!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.msg_staticText.Wrap( -1 )
		self.bSizer.Add( self.msg_staticText, 0, wx.ALL, 5 )
		
		
		self.SetSizer( self.bSizer )
		self.Layout()
		self.bSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

