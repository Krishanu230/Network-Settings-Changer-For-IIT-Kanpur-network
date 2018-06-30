


@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------
pause
echo Got admin permission
echo:
echo setting ip
echo:

for /F "tokens=*" %%A in (temp.txt) do  netsh interface ip set address name="Ethernet" static %%A
echo setting dns1
echo:
for /F "tokens=*" %%A in (DNS1.txt) do netsh interface ipv4 add dnsserver "Ethernet" address=%%A index=1
echo setting dns2
echo:
for /F "tokens=*" %%A in (DNS2.txt) do netsh interface ipv4 add dnsserver "Ethernet" address=%%A index=2

echo Contact Krishanu Singh 170347 in case of any error
pause