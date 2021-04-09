---
layout: post
title: "开发环境 -- Windows VMware 升级安装的问题"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "VMware"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

我本机是 Windows 10 64，安装的老版本的 VMware，在覆盖升级安装新版本的时候，老遇到问题。


## 问题 1：卸载 VMware 时提示 “The MSI '' failed”

[Cleaning up after an incomplete uninstallation on a Windows host (1308)](https://kb.vmware.com/s/article/1308)

造成问题的原因是：前任服务停不掉。
运行 VMware_Install_Cleaner，重启系统，就能完成卸载了。

Download <a href="{% include relref.html url="/source/vmware/VMware_Install_Cleaner.zip" %}" target="_blank">VMware_Install_Cleaner.zip</a>


## 问题 2：找不到 C:\Users\ADMIN\AppData\Local\Temp\vmware_1265030095

["The feature you are trying to use is on a network resource that is unavailable" error when upgrading VMware Workstation (2145285)](https://kb.vmware.com/s/article/2145285)

I have solved this problem by deleting all "tools-linux.msi" and "tools-windows.msi" from the registry.

```
id='tools-freebsd'  -'DBBFB30076C6E9142AD4D0ACCFA32594'
id='tools-linux'    -'A116201D664610145AD115603930CA56'
id='tools-netware'  -'7A79579133DA8984D9E8376086814B46'
id='tools-solaris'  -'BC78C1BA70810FC44B2CEC1EC481DC4B'
id='tools-winPre2k' -'7A26F0EA2A1AF704F9C48439B99DDAD8'
id='tools-windows'  -'C3839DFF5D1079849A4534FA95A9DE03'
```

Download <a href="{% include relref.html url="/source/vmware/vmware_regclear.bat" %}" target="_blank">vmware_regclear.bat</a>

```bat
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
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-18-windows-vmware-upgrade.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://kb.vmware.com/s/article/1308]({% include relrefx.html url="/backup/2020-12-18-windows-vmware-upgrade.md/kb.vmware.com/8dbdee8d.html" %})
- [https://kb.vmware.com/s/article/2145285]({% include relrefx.html url="/backup/2020-12-18-windows-vmware-upgrade.md/kb.vmware.com/1f45748c.html" %})
