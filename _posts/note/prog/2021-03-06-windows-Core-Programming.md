---
layout: post
title: "编程 C++ -- Windows 核心编程，防御基本原理 & 逆向分析"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
archived: true
---


## 防御基本原理

* 内核层
    * 进程防御
        * 进程执行
        * 模块加载
        * 防进程倍结束
        * 内存防御
    * 文件防御
        * 文件操作（创建、读写、删除）
        * 文件自保护
    * 注册表防御
        * 注册表操作（创建、修改、删除）
    * 全局防御
        * 创建、启动、修改 服务
        * 安装全局钩子
    * 网络防御
        * 防黑墙（远程木马）
        * 访问恶意链接
        * 流量监控
* 应用层
    * 下载保护（文件下载完成时对文件的安全检测）
    * 网址安全（通过浏览器访问链接时对网址的安全检测）
    * 自保护


## Windows 关键进程

* system - 驱动的载体，通过 Process Explorer 查看该进程，可查看到系统已加载的驱动
* winlogon.exe - 管理用户的登录和注销
* csrss.exe - Client/Server Runtime Server Subsystem，Win32 子系统的用户模式部分；
    在 Win7 结束该进程，系统直接 BSOD（Blue Screen Of Death）
* lsass.exe - 本地安全和登陆策略
* smss.exe - 会话管理子系统，负责启动用户会话
* services.exe - 系统服务控制管理
* svchost.exe - 从动态链接库（DLL）中运行的服务的通用主机进程名称；以服务的形式将 DLL 加载执行；
* explorer.exe - 资源管理器（桌面）


## 驱动使用的监控技术

* 文件 - minifilter 文件过滤框架；
* 注册表 - Hook 内核或向系统注册回调函数，调用 CmRegisterCallbackEx 注册，需提供自己实现的回调函数；
* 进程 - Hook 内核或向系统注册回调函数，调用 PsSetCreateProcessNotifyRoutine
    注册，需提供自己实现的回调函数；
* 模块 - Hook 内核或向系统注册回调函数，调用 PsSetLoadImageNotifyRoutine 注册，需提供自己实现的回调函数；
* 网络 - tdi、ndis、wfp 网络过滤框架；
* 其它 - 基于 x86 架构上基本可通过 Hook 内核进行大部分的监控，而 x64 只能基于系统回调实现。

文件过滤框架
<https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs>

网络过滤框架
<https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2>


## Hook 技术

Detour
<https://github.com/microsoft/Detours>
* DetourCreateProcessWithDlls - 创建指定进程，并将指定模块注入至目标进程（加载时机早）

{% include image.html url="/assets/images/210306-windows-core-programming/20210418164507.png" %}


## SSDT（System Services Descriptor Table）

```cpp
typedef struct
{
    PVOID *pTable; // Service Table Pointer
    PULONG pulTableCounter; // Table Item Counter. This table is only updated in checked builds.
    ULONG ulServiceCounter; // Number of services contained in this table.
    PUCHAR rguchParamTable; // Table containing the number of bytes of parameters the handler function takes.
} SERVICE_TABLE;
```

SSSDT（System Shadow Services Descriptor Table）

防御基于 x86 架构上的监控实现，基本是以 hook（inline hook） + 注册系统回调实现的；
但在 x64 构架上，微软引入 Driver Signature Enforcement +
Kernel Patch Protection（PatchGuard，简称 PG） 安全机制，
杜绝第三方驱动在系统关键“驱动”中进行的内存修改。因为 PG 的存在，无法继续使用
x86 的 hook 方式实现更多行为的监控，只能使用系统提供的标准回调；
x86 hook 的方式可将 SSDT + SSSDT 里涉及到的各函数调用都进行监控，基本上涵盖了系统上所有的行为，
而系统提供的标准回调，只有进程创建 \ 退出、模块加载、注册表相关、文件、对象回调，
所以，导致了一些在 x86 上可进行防御的行为，在 x64 上无效（或实现方法与 x86 不同）。

[ntfs {% include relref_github.html %}](https://github.com/yuan-xy/pea-search/blob/master/filesearch/ntfs.cpp)

[Through the looking glass: webcam interception and protection in kernel mode](https://www.virusbulletin.com/virusbulletin/2018/09/through-looking-glass-webcam-interception-and-protection-kernel-mode/)
{% include image.html url="/assets/images/210306-windows-core-programming/1ff59f99756da55da2949e76614ff3c6_f2958.jpg" caption="Figure 1: After driver installation." %}
{% include image.html url="/assets/images/210306-windows-core-programming/a01398b94309bb5a669e7312ed28f88f_f2959.jpg" caption="Figure 2: The desirable order." %}

**x64 自保护** 通过 TLS 回调的更早执行时机，Hook 自身 PEB 内 KernelCallbackTable 表的 \_\_ClientLoadLibrary，实现对全局钩子的拦截。

ReactOS
<https://github.com/reactos/reactos>

双机调试 VirtualKD
<https://sysprogs.com/legacy/virtualkd>

Source Insight
<https://www.sourceinsight.com>

CFF Explorer
<https://ntcore.com/?page_id=388>

ProcMon（SysinternalsSuite）
<https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite>

**文件重启删除** 读取注册表 smss.exe 删除的。
**svchost.exe** `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\`
    `%SystemRoot%\system32\svchost.exe -k RPCSS`
    File: `%SystemRoot%\System32\RpcEpMap.dll`
    Registry key: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RpcEptMapper`


## 逆向分析

* IDA
* windbg
* **CFF-Explorer**

反汇编过程即二进制转汇编助记符，参考 intel 指令集手册。
X86 为变长指令（灵活），arm 为定长指令（高效）\[ 4G 寻址问题 \]



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-06-windows-Core-Programming.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/docs.microsoft.com/3f7eeeb1.html" %})
- [https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/docs.microsoft.com/6c6aee69.html" %})
- [https://github.com/microsoft/Detours]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/github.com/f10fd70b.html" %})
- [https://github.com/yuan-xy/pea-search/blob/master/filesearch/ntfs.cpp]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/github.com/cbe71bc2.html" %})
- [https://www.virusbulletin.com/virusbulletin/2018/09/through-looking-glass-webcam-interception-and-protection-kernel-mode/]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/www.virusbulletin.com/00030afb.html" %})
- [https://github.com/reactos/reactos]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/github.com/f366a913.html" %})
- [https://sysprogs.com/legacy/virtualkd]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/sysprogs.com/6caf3e13.html" %})
- [https://www.sourceinsight.com]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/www.sourceinsight.com/8f9f2ff2.html" %})
- [https://ntcore.com/?page_id=388]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/ntcore.com/fdf592d1.html" %})
- [https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite]({% include relrefx.html url="/backup/2021-03-06-windows-Core-Programming.md/docs.microsoft.com/0c438a9b.html" %})
