;-------------------------------------------------------------------------
; Installer script for MXCart
;-------------------------------------------------------------------------

;--------------------------------------------
; General definitions: just some constants that are referred later.
!define PRODUCT_NAME "MX Cart"
!define PRODUCT_VERSION_MAJOR 1
!define PRODUCT_VERSION_MINOR 10
!define PRODUCT_DISPLAY_VERSION "1.10"
!define PRODUCT_PUBLISHER "Will Kamp"
!define PRODUCT_WEB_SITE "http://mxmariner.com/mxcart"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}" ; 
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_INSTALL_DIR "$PROGRAMFILES\MXCart"

;--------------------------------------------
; Maximum compression
SetCompressor /SOLID lzma

;--------------------------------------------
; Modern UI definitions
!include "MUI2.nsh"

;--------------------------------
;Interface Settings
!define MUI_ABORTWARNING
!define MUI_ICON "exe.win32-2.7\icon.ico"
!define MUI_UNICON "exe.win32-2.7\icon.ico"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "exe.win32-2.7\MUI_HEADERIMAGE_BITMAP.bmp"
;MUI_HEADERIMAGE_BITMAP recommended size is 150x57
!define MUI_HEADERIMAGE_RIGHT
!define MUI_HEADER_TRANSPARENT_TEXT
!define MUI_WELCOMEFINISHPAGE_BITMAP "exe.win32-2.7\MUI_WELCOMEFINISHPAGE_BITMAP.bmp"
;MUI_WELCOMEFINISHPAGE_BITMAP recommended size is 164x314 
!define MUI_WELCOMEFINISHPAGE_BITMAP_NOSTRETCH 

;--------------------------------
;Pages

; Welcome page
!insertmacro MUI_PAGE_WELCOME

; License page
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "exe.win32-2.7\license.txt"

; Instfiles page
!insertmacro MUI_PAGE_INSTFILES

; Finish page
!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\license.txt"
!define MUI_FINISHPAGE_NOREBOOTSUPPORT
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"

;--------------------------------------------
; Installer Settings
Name "${PRODUCT_NAME}"
OutFile "${PRODUCT_NAME}_Setup.exe"
InstallDir "${PRODUCT_INSTALL_DIR}"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "${PRODUCT_PUBLISHER}"
RequestExecutionLevel admin ;Request application privileges for Windows Vista/7

;--------------------------------
;Installer Sections

Section "MainSection" MainSection

  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  
  ;Copy files
  File /r "exe.win32-2.7\*"

  SetShellVarcontext all
  CreateDirectory "$APPDATA\MXCart"
  CopyFiles "$INSTDIR\icon.ico" "$APPDATA\MXCart"
  CreateShortCut "$INSTDIR\MXCart.lnk" "$INSTDIR\MXCart.exe" "" \
  "$APPDATA\MXCart\icon.ico" "" SW_SHOWNORMAL "" "Chart Import Utility"

  CreateDirectory "$SMPROGRAMS\MXCart"
  CopyFiles "$INSTDIR\MXCart.lnk" "$SMPROGRAMS\MXCart"

  WriteUninstaller "$INSTDIR\Uninstall.exe"
  CreateShortCut "$INSTDIR\Uninstall.lnk" "$INSTDIR\Uninstall.exe" "" \
  "$INSTDIR\Uninstall.exe" "" SW_SHOWNORMAL "" "Uninstall MXCart"
  CopyFiles "$INSTDIR\Uninstall.lnk" "$SMPROGRAMS\MXCart"

  SetShellVarContext current
  CopyFiles "$INSTDIR\MXCart.lnk" "$DESKTOP"

  ;Add/Remove registry settings: This registry entry will list the product in 'installed programs list'
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "${PRODUCT_NAME}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\Uninstall.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\\icon.ico"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_DISPLAY_VERSION}"
  WriteRegDWORD ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "VersionMajor" "${PRODUCT_VERSION_MAJOR}"
  WriteRegDWORD ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "VersionMinor" "${PRODUCT_VERSION_MINOR}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

;--------------------------------
;Uninstaller Section

;When the uninstaller is launched, this function provides a confirmation message box.
Function un.onInit
	MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove ${PRODUCT_NAME} and all of its components?" IDYES +2
	Abort
FunctionEnd

;When the uninstallation is complete, this function displays a success message box.
Function un.onUninstSuccess
	HideWindow
	MessageBox MB_ICONINFORMATION|MB_OK "${PRODUCT_NAME} was successfully removed from your computer."
FunctionEnd

;This function gets executed when uninstaller is launched. It basically removes all installed files.
Section "Uninstall"

RMDir /r "$INSTDIR"
SetShellVarContext all
RMDir /r "$SMPROGRAMS\MXCart"
RMDir /r "$APPDATA\MXCart"
SetShellVarContext current
Delete "$DESKTOP\MXCart.lnk"
  
  ;Remove the entry from 'installed programs list'
  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"

  ;SetAutoClose True ;This will close the uinstall window that shows the details of files deleted.
SectionEnd