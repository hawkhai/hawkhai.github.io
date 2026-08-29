@echo off
setlocal

rem Keep the launcher working in command prompts opened before Ruby was installed.
if exist "C:\Ruby27-x64\bin\ruby.exe" set "PATH=C:\Ruby27-x64\bin;%PATH%"

where ruby >nul 2>&1 || (
    echo Ruby was not found. Expected C:\Ruby27-x64\bin\ruby.exe
    exit /b 1
)
where bundle >nul 2>&1 || (
    echo Bundler was not found. Run: gem install bundler -v 1.16.1
    exit /b 1
)

if /i "%~1"=="check" (
    ruby -v
    call bundle _1.16.1_ --version
    exit /b 0
)

start "Jekyll Blog" python3 jekyllserv.py
cd ..
cd pythonx
start "Git Sync" python3 mygit.py all

endlocal
