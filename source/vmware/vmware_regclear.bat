echo off
cls
echo "flag">>%windir%\system32\test.log
if not exist %windir%\system32\test.log (
cls
echo 请右键使用管理员身份运行！！！
pause
exit
)
cls
echo 确认进行清理？
pause
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\VMware, Inc." /f >nul 2>nul
reg delete "HKEY_CURRENT_USER\SOFTWARE\VMware, Inc." /f >nul 2>nul
reg delete "HKCR\Installer\Products\7A26F0EA2A1AF704F9C48439B99DDAD8" /f >nul 2>nul
reg delete "HKCR\Installer\Products\0C6B325AF07E1AF439D3AD4079F106F7" /f >nul 2>nul
reg delete "HKCR\Installer\Products\A57F49D06AE015943BFA1B54AFE9506C" /f >nul 2>nul
reg delete "HKCR\Installer\Features\7A26F0EA2A1AF704F9C48439B99DDAD8" /f >nul 2>nul
reg delete "HKCR\Installer\Features\7A79579133DA8984D9E8376086814B46" /f >nul 2>nul
reg delete "HKCR\Installer\Features\A116201D664610145AD115603930CA56" /f >nul 2>nul
reg delete "HKCR\Installer\Features\BC78C1BA70810FC44B2CEC1EC481DC4B" /f >nul 2>nul
reg delete "HKCR\Installer\Features\C3839DFF5D1079849A4534FA95A9DE03" /f >nul 2>nul
reg delete "HKCR\Installer\Features\DBBFB30076C6E9142AD4D0ACCFA32594" /f >nul 2>nul
reg delete "HKCR\Installer\Products\7A79579133DA8984D9E8376086814B46" /f >nul 2>nul
reg delete "HKCR\Installer\Products\A116201D664610145AD115603930CA56" /f >nul 2>nul
reg delete "HKCR\Installer\Products\BC78C1BA70810FC44B2CEC1EC481DC4B" /f >nul 2>nul
reg delete "HKCR\Installer\Products\C3839DFF5D1079849A4534FA95A9DE03" /f >nul 2>nul
reg delete "HKCR\Installer\Products\DBBFB30076C6E9142AD4D0ACCFA32594" /f >nul 2>nul
reg delete "HKCR\Installer\Products\7A26F0EA2A1AF704F9C48439B99DDAD8" /f >nul 2>nul
reg delete "HKCR\Installer\Products\7A79579133DA8984D9E8376086814B46" /f >nul 2>nul
reg delete "HKCR\Installer\Products\A116201D664610145AD115603930CA56" /f >nul 2>nul
reg delete "HKCR\Installer\Products\BC78C1BA70810FC44B2CEC1EC481DC4B" /f >nul 2>nul
reg delete "HKCR\Installer\Products\C3839DFF5D1079849A4534FA95A9DE03" /f >nul 2>nul
reg delete "HKCR\Installer\Products\DBBFB30076C6E9142AD4D0ACCFA32594" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\7A26F0EA2A1AF704F9C48439B99DDAD8" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\7A79579133DA8984D9E8376086814B46" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\A116201D664610145AD115603930CA56" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\BC78C1BA70810FC44B2CEC1EC481DC4B" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\C3839DFF5D1079849A4534FA95A9DE03" /f >nul 2>nul
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\DBBFB30076C6E9142AD4D0ACCFA32594" /f >nul 2>nul
echo 清理完成！
pause