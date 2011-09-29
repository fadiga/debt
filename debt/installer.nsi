Name "Suivi des dettes"

;SetCompress off 

; installer file name
OutFile "Install-DEBET.exe"

; default destination dir
InstallDir "C:\DEBET"

; request application privilege
; user should be ok. one can still right-click to install as admin
RequestExecutionLevel user

Page directory
Page instfiles

Section ""

  ; destination folder
  SetOutPath $INSTDIR
  
  ; List of files/folders to copy
  File /r dist\*.*
  File /r *.dll
  File /r *.manifest
  File /r images
  File /r locale

  ; start menu entry
  CreateDirectory "$SMPROGRAMS\DEBT"
  CreateShortCut "$SMPROGRAMS\DEBT\Suivi des dettes.lnk" "$INSTDIR\debt.exe" "" "$INSTDIR\debt.exe" 0
  createShortCut "$SMPROGRAMS\DEBT\Uninstall Suivi des dettes.lnk" "$INSTDIR\uninstaller.exe"


  ; uninstaller
  writeUninstaller $INSTDIR\uninstaller.exe

SectionEnd

section "Uninstall"
 
# Always delete uninstaller first
delete $INSTDIR\uninstaller.exe

RMDir /r $SMPROGRAMS\DEBT
 
# now delete installed file
delete $INSTDIR\*.exe
delete $INSTDIR\*.dll
delete $INSTDIR\*.manifest
delete $INSTDIR\*.exe
delete $INSTDIR\*.lib
delete $INSTDIR\*.zip
RMDir /r $INSTDIR\icons
RMDir /r $INSTDIR\locale
 
sectionEnd

