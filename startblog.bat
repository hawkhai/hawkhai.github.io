@echo off
setlocal

rem Keep the launcher working in command prompts opened before Ruby was installed.
if exist "C:\Ruby27-x64\bin\ruby.exe" set "PATH=C:\Ruby27-x64\bin;%PATH%"
if not exist "C:\Ruby27-x64\bin\ruby.exe" if exist "C:\Ruby25-x64\bin\ruby.exe" set "PATH=C:\Ruby25-x64\bin;%PATH%"

where ruby >nul 2>&1 || (
    echo Ruby was not found. Add Ruby to PATH or install it in C:\Ruby27-x64 or C:\Ruby25-x64.
    exit /b 1
)
where bundle >nul 2>&1 || (
    echo Bundler was not found. Run: gem install bundler -v 1.16.1
    exit /b 1
)

if /i "%~1"=="check" (
    ruby -v || exit /b 1
    call bundle _1.16.1_ --version || exit /b 1
    exit /b 0
)

start "Jekyll Blog" python3 jekyllserv.py
cd ..
cd pythonx
start "Git Sync" python3 mygit.py all

endlocal
