---
layout: post
title: "开发环境 -- CompatTelRunner：微软如何用几百 KB/s 把机械硬盘干到 100%"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["Windows", "CompatTelRunner", "磁盘", "性能优化", "故障排查"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
date: 2026-08-31 23:30:00 +0800
l2dwidget: true
---

先说结论：如果 Windows 任务管理器显示机械硬盘长期 100%，吞吐量却只有几十 KB/s 到几百 KB/s，先别急着怪硬盘坏了，也别只盯着“读写速度”看。微软自带的 `CompatTelRunner.exe` 可能正在后台把整块盘的目录树翻个底朝天。

这玩意名义上叫“兼容性评估”，实际效果却像一个拿着微软通行证的全盘爬虫：不征求意见，不解释自己在干什么，用最低优先级 I/O 当遮羞布，然后让机械硬盘的磁头在海量小文件之间疯狂横跳。任务管理器只告诉你“磁盘 100%”，却不肯把目录枚举造成的灾难讲清楚。

一个操作系统后台任务能做到这么不透明、这么扰民，也算是某种工程奇迹。


## 现场：几百 KB/s，硬盘却被打成 100%

问题盘是希捷 `ST2000DM008-2FR102` ，一块 7200 RPM 的机械硬盘。故障发作时的表现非常典型：

* 磁盘活动时间持续 100%；
* 请求队列长期约 5～22；
* 单次 I/O 延迟约 0.05～1.8 秒；
* 吞吐量经常只有几十 KB/s 到约 1 MB/s；
* D 盘卡得像硬盘快死了，G 盘却基本没有访问；
* SMART、NTFS 和系统存储日志均没有给出坏盘证据。

如果只看吞吐量，这点数据甚至有些可笑。但机械硬盘怕的不是字节数，而是随机寻道。连续读取 100 MB 可能很轻松，跨几万个目录各摸一下 4 KB，却足以把磁头折腾得半死。

更坑的是，普通进程 I/O 统计主要展示读写字节，目录枚举、文件属性查询、打开关闭句柄等元数据操作并不显眼。因此你会看到“没什么进程大量读写”，同时磁盘活动时间仍然钉死在 100%。


## Procmon 抓现行：就是 CompatTelRunner

最后使用微软自己的 Process Monitor 抓取 15 秒文件活动，元凶终于现形：

* `CompatTelRunner.exe` 对 D 盘产生 10,641 个文件事件；
* 其中 4,753 次目录枚举；
* 1,529 次文件读取；
* 正在遍历 `D:\Qt\...` 等包含海量源码和小文件的目录。

它实际执行的命令类似：

```text
%windir%\system32\CompatTelRunner.exe
    -m:appraiser.dll
    -f:DoScheduledTelemetryRun express
```

对应的计划任务位于：

```text
\Microsoft\Windows\Application Experience\
    Microsoft Compatibility Appraiser Exp
```

停止进程并禁用任务后，20 秒复测结果是：

* 活动时间：持续 100% → 约 0～1.7%；
* 请求队列：5～22 → 基本为 0；
* 延迟：最高约 1.8 秒 → 约 0～23 毫秒；
* 最终稳定后延迟约 0～3 毫秒。

硬盘没有突然自愈。只是那个在后台翻箱倒柜的混账进程终于停了。


## 它到底在干什么

公允地说，Compatibility Appraiser 不是一个完全没有业务目的的随机病毒。它会收集和刷新应用程序、驱动、设备以及系统组件的兼容性清单，供 Windows Setup、Windows Update 和企业升级工具判断当前机器能否升级到目标版本。

微软自己的文档明确写着：Appraiser 会生成应用文件、驱动包和设备的兼容性决策数据；兼容性扫描还会写入并刷新 `AppCompatFlags` 下的 compatibility intelligence，供 Windows Update 判断设备是否适合目标版本。

参考资料：

* [Required diagnostic events and fields for Windows 10](https://learn.microsoft.com/en-us/windows/privacy/required-windows-diagnostic-data-events-and-fields-2004)
* [Use the Windows Setup Compatibility Scan Logs to Identify Blocking Issues](https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/use-windows-setup-compatibility-scan-logs-to-identify-blocking-issues)
* [Optional diagnostic data for Windows](https://learn.microsoft.com/en-us/windows/privacy/optional-diagnostic-data)

问题不在于“系统升级前做兼容性检查”这个目标，而在于它的工程实现和产品态度：

1. 扫描范围巨大，碰到源码、SDK、模型和依赖库目录就会制造海量随机 I/O；
2. 所谓低优先级 I/O 解决不了机械硬盘寻道瓶颈；
3. 用户界面没有清晰说明哪个任务正在枚举哪些目录；
4. Windows 更新、兼容性规则变化和内部状态变化可能让它重新运行；
5. 对一块已经用了多年的机械盘，它能只用几百 KB/s 就长期霸占 100% 活动时间；
6. 出问题时，任务管理器提供的信息还不足以让普通用户定位根因。

这就是典型的“业务理由没错，所以实现再粗暴也没人负责”。微软需要一份升级兼容性清单，于是用户的整块机械盘就成了免费扫描场。至于电脑卡不卡、磁头累不累、用户能不能知道发生了什么，显然都排在遥测和升级流程后面。


## 为什么它能反复折腾一年

兼容性清单不是生成一次就永久有效。软件、驱动、文件版本、Windows 目标版本和兼容性规则都会变化，Appraiser 会认为旧结果需要刷新。

本机任务使用的也不是简单、直观的“每天运行一次”触发器，而是 Windows 内部状态触发。它运行的是 `DoScheduledTelemetryRun express` ，Windows Update 或系统维护状态变化后可能再次评估。

所以仅仅在任务管理器里结束一次 `CompatTelRunner.exe` 没什么用。今天杀掉，下一次更新或维护周期又能回来。更恶心的是，每次回来都可以重新走一遍那些几乎没变化的大型源码树。


## 本机的处理方案

本机保留了一份可恢复脚本：

```text
D:\kSource\pythonx\disable-compattelrunner.ps1
```

它会：

* 终止当前 `CompatTelRunner.exe` ；
* 禁用两个常见的 Compatibility Appraiser 任务名；
* 在 `C:\ProgramData\CodexMaintenance` 部署 SYSTEM 守护脚本；
* 注册开机、登录和每 5 分钟复核触发器；
* 如果 Windows 更新偷偷重新启用任务，再次将其禁用。

管理员 PowerShell 中执行：

```powershell
powershell.exe -ExecutionPolicy Bypass `
    -File "D:\kSource\pythonx\disable-compattelrunner.ps1"
```

需要安装 Windows 大版本功能更新时，可以恢复：

```powershell
powershell.exe -ExecutionPolicy Bypass `
    -File "D:\kSource\pythonx\disable-compattelrunner.ps1" `
    -Restore
```

代价也要说清楚：禁用 Appraiser 后，Windows 大版本升级使用的兼容性资格和保护信息可能不会及时刷新。准备升级大版本时，应先恢复；升级完成后再决定是否重新禁用。普通用户不应该在不知道代价的情况下照抄任何“万能优化脚本”。


## 别看到 100% 就只会杀 Windows 服务

这次问题后来再次出现，但复查发现 `CompatTelRunner.exe` 并没有运行，Appraiser 任务也仍然处于 Disabled。新的元凶是两组同样愚蠢的递归扫描：

* 一个 Codex 任务从错误的上级目录执行递归 `Get-ChildItem` 和 `git status` ；
* `TGitCache.exe` 在 4.8 秒内对 D 盘制造了 63,301 个文件事件，递归扫描巨大的 Git 工作区。

结束 `TGitCache.exe` 后，D 盘立即从接近 100% 变成：

```text
活动时间：0%
请求队列：0
读取速度：0
写入速度：0
```

这说明诊断不能靠背答案。上次是 `CompatTelRunner` ，这次可能是 TortoiseGit，下次也可能是杀毒软件、索引器、IDE、Agent 或某条写得像屎一样的递归脚本。正确做法是抓取“进程 + 操作 + 文件路径”，而不是把所有 Windows 服务轮流关闭一遍然后祈祷。


## 最终教训

* “磁盘 100%”描述的是忙碌时间，不等于吞吐量很大；
* 机械硬盘会被目录枚举和小随机 I/O 轻易打满；
* 普通 I/O 字节统计可能隐藏真正的元数据访问洪水；
* 不要在包含海量仓库和依赖树的上级目录执行无边界递归搜索；
* 不要对巨型工作区使用常驻、全递归的 Git 图标缓存；
* 修复必须可恢复，并记录副作用；
* 任务被禁用不代表永远不会被 Windows 更新改回来，必须复核实际进程和任务状态；
* 最可靠的证据不是“我感觉是某个服务”，而是 Procmon 日志里精确到文件路径的事件。

`CompatTelRunner` 最令人火大的地方，不是它完全没用，而是它把微软自己的升级便利建立在用户看不见、说不清、停不稳的后台扫描上。一个负责兼容性的组件，最后把正常使用电脑这件事搞得如此不兼容，确实非常 Windows。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-08-31-compattelrunner.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://learn.microsoft.com/en-us/windows/privacy/required-windows-diagnostic-data-events-and-fields-2004]({% include relrefx.html url="/backup/2026-08-31-compattelrunner.md/learn.microsoft.com/f04c874a.html" %})
- [https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/use-windows-setup-compatibility-scan-logs-to-identify-blocking-issues]({% include relrefx.html url="/backup/2026-08-31-compattelrunner.md/learn.microsoft.com/f14f508e.html" %})
- [https://learn.microsoft.com/en-us/windows/privacy/optional-diagnostic-data]({% include relrefx.html url="/backup/2026-08-31-compattelrunner.md/learn.microsoft.com/b1b326d2.html" %})
