---
layout: post
title: "编程与调试 -- Windows 编程知识点（文档整理）2/2 逆向 & 驱动"
author: yqh
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
cluster: "Windows 编程知识点"
---


## 浅析逆向分析


### ELF(linux) 和 PE(windows)

{% include image.html url="/assets/images/220109-windows-program2/img_0d335cb525dc4ed2bece08855aa251e1.png" %}

{% include image.html url="/assets/images/220109-windows-program2/img_cba9aa9667b44125934478368847a72f.png" caption="PE 格式总览" %}


### PE 头

* PE 结构相关头文件
    * Windows-sdk 下 \include\winnt.h
* 关键结构
    * DosHeader
    * NtHeader
        * FileHeader
        * OptionalHeader
            * DataDirectory
    * SectionTable


### DOS 头

* 作用
    * 文件头，兼容 DOS 模式
    * DOS 下默认显示 This program must be run under win32
* 重要字段
    * e_magic 标记 MZ(4D5A)，MS-DOS 创建者 Mark Zbikowski
    * e_lfanew 指向真正的 PEHeader

{% include image.html url="/assets/images/220109-windows-program2/img_dcbba4e657d14ddb89907b51285f162a.png" caption="DOS 头" %}


### FileHeader

* 作用
    * 描述 PE 基础信息
* 重要字段
    * Machine
    * NumberOfSections，节数量
    * SizeOfOptionalHeader，可选头大小
    * Characteristics，PE 属性


### OptionalHeader

* 作用
    * 描述 PE 详细信息
* 重要字段
    * Magic
        * PE32/64
    * Subsystem
        * Console/win
    * DataDirectory
    * AddressOfEntryPoint(OEP)
        * 入口点，编译器特征
        * 劫持修改（感染型）
        * Main 和 OEP

{% include image.html url="/assets/images/220109-windows-program2/img_ac2054f4819042acaa386ec63e141433.png" caption="main 和 OEP" %}

* main 是不是第一行执行的代码？
    * OEP(crt/src/cr0.c)
        * mainCRTStartup/WinMainCRTStartup
    * main
        * main/WinMain
* 编译运行过程
    * 编译链接过程 ENTRY 选项指定入口函数，默认为 main
    * OEP 指定为 libc.lib 中的 mainCRTStartup(console)
    * mainCRTStartup 完成初始化后调用 main
* 备注
    * 文件特征注意


### DataDirectory

* 作用
    * 导入、导出、资源等关键结构的总索引
* 介绍
    * DataDirectory 位于 OptionalHeader 末尾
    * 共 16 组，每组指定一个重要数据结构
* 重要字段
    * 导出表，导出函数
    * 导入表，引用外部 DLL 信息
    * 调试表，PDB 等调试信息
    * 资源表，图标，对话框，版本信息等
    * 安全表，数字签名


### SectionTable

* 作用
    * 除文件头外的代码、数据、资源分段存储索引
    * 便于系统安全性设置
* 重要字段
    * VirtualAddress，节区在内存中的偏移
    * PointerToRawData，节区在文件偏移
    * Characteristics，描述该节的 rwx 属性

{% include image.html url="/assets/images/220109-windows-program2/img_49bc33aaa7dd48cea48bb76232346316.png" caption="源码与 PE" %}


### PE 文件映射

{% include image.html url="/assets/images/220109-windows-program2/img_27b4d651d500450fad5e4943189d4289.png" %}

* PE-Section
    * .text，二进制代码，x 属性
    * .data，全局变量、字符串、预定义数据，rw 属性
    * .rsrc，资源图标、对话框资源、版本信息等，r 属性
* TIPS
    * 对齐粒度
        * 0x200->0x1000
    * 节名无实质意义，不同的编译器喜好不同
        * .text(vc)
        * .CODE(delphi)
* 节空隙
    * 恶意代码寄生

{% include image.html url="/assets/images/220109-windows-program2/img_6f9d487018ff4e17a28fa22b2be5c3b3.png" caption="感染型病毒" %}

ntcore CFF-Explorer


### x86 指令编码

反汇编过程即二进制转汇编助记符，参考 intel 指令集手册 X86 为变长指令（灵活），arm 为定长指令（高效）[4G 寻址问题]

{% include image.html url="/assets/images/220109-windows-program2/img_0a12e635211a4c2686b7909f1665f1a8.png" caption="x86 指令编码" %}


### 指令编码

* 作用
    * 实现虚拟机（bochs) / 沙箱
        * 精准控制每个指令执行，OS 开发
    * 恶意代码仿真执行
        * 对抗混淆、加密
    * 反汇编，机读指令转人读指令
        * 安全必备
    * vulnerability/shellcode/inline-hook
        * 核心安全分析、防御

{% include image.html url="/assets/images/220109-windows-program2/img_0930cb7fa94b43ea813ba24a5eb36059.png" %}


### 汇编简介

{% include image.html url="/assets/images/220109-windows-program2/img_3301cf6f12aa4c26b69156794495c25f.png" %}

* 指令分类
    * 计算
        * Add/adc/inc/sub/mul/…
    * 读写
        * Mov/lea/push/pop/xchg/…
    * 控制
        * Jmp/jcc/loop/call/ret/…
    * 其他
        * clc/stc/cld/cupid/…
* 备注
    * 仅寄存器可参与计算
    * 地址间不能直接操作


### 反汇编 — call stack

{% include image.html url="/assets/images/220109-windows-program2/img_1a01faaae0ea411a8a3e09f42dbecc1a.png" %}
{% include image.html url="/assets/images/220109-windows-program2/img_72d1459ae6b94c52b26c98ba8ab1551d.png" %}

* 寄存器
    * Ebp 指向当前函数栈基址
        * [ebp+xx] 参数 / [ebp-xx] 变量
    * Esp 指向当前函数栈顶
* 进入 / 退出函数时构建和释放栈帧
    * 仅改变 ebp/esp 即可
    * 返回地址
* 如何平衡堆栈
    * 根据调用类型


### 反汇编案例

{% include image.html url="/assets/images/220109-windows-program2/img_c7ea0bdfdc0e4fa493f314960985b3a2.png" %}
{% include image.html url="/assets/images/220109-windows-program2/img_5a7df3420fe04996abe2773d7fde2bdb.png" %}


### 动态调试 & 静态分析

TIPS
* 资源 DLLFindResourceA/W
    * LoadStringA/W(user32.dll)
* 调用栈结构
* Ctrl+F9 执行到返回
* 关注前置跳转
* 分析建立在开发 / 系统的理解之上

多层封装
异步调用
动态加载
加密解密
自定义接口
壳
反调试


### 代码防护

* 关键函数 / 文件采用无意义名字
* 避免明文存储，配置文件 hash 化
* 尽量减少无用提示
* 无关代码注释删除


## 防御基本原理


### 防御 & 系统简述

防御（内核）同步 & 异步 拦截的区别及应用场景
* 同步：触发（命中）关键行为时，发起行为的线程被阻塞，内核将行为的相关信息传递至应用层；
* 异步：触发（命中）关键行为时，获取行为的相关信息后，不影响行为的继续执行，内核将行为的相关信息传递至应用层；
* 行为的相关信息：
    * 行为发起者（进程文件路径）
    * 行为标识（防御标记的行为种类）
    * 行为目标（根据标识有所不同，如：进程创建类的，这里的目标会是被调用的进程文件路径）
    * ………………
* 场景：
    * 同步拦截用于威胁性较高的行为，如：进程创建、创建服务、启动服务、修改注册表项启动项……
    * 异步拦截用于信息通知、文件写完成……，如：进程退出

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

#### Windows 关键进程

* system - 驱动的载体，通过 Process Explorer 查看该进程，可查看到系统已加载的驱动
* winlogon.exe - 管理用户的登录和注销
* csrss.exe - Client/Server Runtime Server Subsystem，Win32 子系统的用户模式部分；在 Win7 结束该进程，系统直接 BSOD（Blue Screen Of Death）
* lsass.exe - 本地安全和登陆策略 smss.exe - 会话管理子系统，负责启动用户会话
* services.exe - 系统服务控制管理
* svchost.exe - 从动态链接库（DLL）中运行的服务的通用主机进程名称；以服务的形式将 DLL 加载执行；
* explorer.exe - 资源管理器（桌面）

{% include image.html url="/assets/images/220109-windows-program2/img_15fc1b088df245f09e188dd00326f3e8.png" %}

* `mov eax,42h` 对应内核里 SSDT 表所在的 index
* `mov edx,7FFE0300h` 0x7ffe0000 存储 \_KUSER\_SHARED\_DATA 结构体，用于应用层和内核层共享数据


### 防御原理

#### 驱动使用的监控技术

* 文件 - minifilter 文件过滤框架
* 注册表 - Hook 内核或向系统注册回调函数，调用 CmRegisterCallbackEx 注册，需提供自己实现的回调函数（）
* 进程 - Hook 内核或向系统注册回调函数，调用 PsSetCreateProcessNotifyRoutine 注册，需提供自己实现的回调函数
* 模块 - Hook 内核或向系统注册回调函数，调用 PsSetLoadImageNotifyRoutine 注册，需提供自己实现的回调函数
* 网络 - tdi、ndis、wfp 网络过滤框架（）
* 其它 - 基于 x86 架构上基本可通过 Hook 内核进行大部分的监控，而 x64 只能基于系统回调实现
* 文件过滤框架 <https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs>
* 网络过滤框架 <https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2>

#### Hook 技术

* “注入”，通过修改目标进程，将代码指令写入至目标进程的内存并执行；
* “钩子”，可对程序内关键函数或任意有效内存地址进行“安装”；大部分的“安装”对指定程序内的内存进行修改，与注入组合使用；

{% include image.html url="/assets/images/220109-windows-program2/img_f78ebdace97f4670a6e8bb2ea02aa798.png" %}

**Detour**
微软提供的可用于多平台的“hook”库，提供：进程创建时的注入（模块）、指定函数 hook……

**DetourCreateProcessWithDlls** - 创建指定进程，并将指定模块注入至目标进程（加载时机早）

在修改导入表完成后，目前进程还处于“挂起”状态，后续调用“ResumeThread”后，系统按照标准的进程创建流程，遍历导入表将对应的模块进行加载（将模块映射至当前进程内存，并获取 AddressOfEntryPoint 调用入口点 DllEntry）；

进程的首个线程（进程初始化）ntdll!_LdrpInitialize --> ntdll!LdrpInitializeProcess --> ntdll!LdrpRunInitializeRoutines --> ntdll!LdrpCallInitRoutine
TLS 回调比模块的 dllmain 执行时机更早

{% include image.html url="/assets/images/220109-windows-program2/img_900f2685bc0640e7bdc5accf5c0fe3ba.png" caption="LdrpRunInitializeRoutines 代码片段" %}

{% include image.html url="/assets/images/220109-windows-program2/20220116223329.png" %}

#### SSDT（System Services Descriptor Table）

```cpp
typedef struct {
    PVOID *pTable; // Service Table Pointer
    PULONG pulTableCounter; // Table Item Counter. This table is only updated in checked builds.
    ULONG ulServiceCounter; // Number of services contained in this table.
    PUCHAR rguchParamTable; // Table containing the number of bytes of parameters the handler function takes.
} SERVICE_TABLE;
```

#### SSSDT（System Shadow Services Descriptor Table）

```cpp
typedef struct {
    PVOID *pTable; // Service Table Pointer
    PULONG pulTableCounter; // Table Item Counter. This table is only updated in checked builds.
    ULONG ulServiceCounter; // Number of services contained in this table.
    PUCHAR rguchParamTable; // Table containing the number of bytes of parameters the handler function takes.
} SERVICE_TABLE;
```

#### x86 \ x64 系统的区别

防御基于 x86 架构上的监控实现，基本是以 hook（inline hook） + 注册系统回调实现的；但在 x64 构架上，微软引入 Driver Signature Enforcement + Kernel Patch Protection（PatchGuard，简称 PG） 安全机制，杜绝第三方驱动在系统关键“驱动”中进行的内存修改。因为 PG 的存在，无法继续使用 x86 的 hook 方式实现更多行为的监控，只能使用系统提供的标准回调；x86 hook 的方式可将 SSDT + SSSDT 里涉及到的各函数调用都进行监控，基本上涵盖了系统上所有的行为，而系统提供的标准回调，只有进程创建 / 退出、模块加载、注册表相关、文件、对象回调，所以，导致了一些在 x86 上可进行防御的行为，在 x64 上无效（或实现方法与 x86 不同）；


### 监控点的实现

#### 监控点实现（应用层）

* 文件监控 ReadDirectoryChangesW
    * 应用层实现文件监控效果的函数（非回调），可对文件夹里的文件名变动、目录名变动、文件属性变动……进行监控
    * 缺点：
        * 1、有针对性的（传入的目录句柄），不是全局监控
        * 2、无法获取操作者，即无法知道是哪个进程发起对文件的修改行为
* 注册表监控 RegNotifyChangeKeyValue
    * 应用层实现注册表监控效果的函数（非回调），完成调用后指定位置如发生变化会返回
    * 缺点：
        * 1、有针对性的（传入的指定项），不是全局监控
        * 2、无法获取操作者，即无法知道哪个进程发起的修改行为
        * 3、无法获取更多的信息，即无法知道哪个键、哪些键值发生变化
* x64 自保护
    * 通过 TLS 回调的更早执行时机，Hook 自身 PEB 内 KernelCallbackTable 表的 __ClientLoadLibrary，实现对全局钩子的拦截


### 例子 / 参考资料

#### Code

* Detour <https://github.com/microsoft/Detours>
* ReactOS <https://github.com/reactos/reactos>
* 双机调试 VirtualKD <https://sysprogs.com/legacy/virtualkd>
* Nt 源码

[ntfs {% include relref_github.html %}](https://github.com/yuan-xy/pea-search/blob/master/filesearch/ntfs.cpp)

[Through the looking glass: webcam interception and protection in kernel mode](https://www.virusbulletin.com/virusbulletin/2018/09/through-looking-glass-webcam-interception-and-protection-kernel-mode/)
{% include image.html url="/assets/images/220109-windows-program2/1ff59f99756da55da2949e76614ff3c6_f2958.jpg" caption="Figure 1: After driver installation." %}
{% include image.html url="/assets/images/220109-windows-program2/a01398b94309bb5a669e7312ed28f88f_f2959.jpg" caption="Figure 2: The desirable order." %}

#### Tool

* Source Insight <https://www.sourceinsight.com> 或 看雪 \ 百度 破解版
* CFF Explorer <https://ntcore.com/?page_id=388> 或 百度
* ProcMon（SysinternalsSuite） <https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite>

#### 文件重启删除

**文件重启删除** 读取注册表 smss.exe 删除的。
* **svchost.exe** `HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Svchost\`
    * `%SystemRoot%\system32\svchost.exe -k RPCSS`
    * File: `%SystemRoot%\System32\RpcEpMap.dll`
    * Registry key: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RpcEptMapper`

#### 逆向分析

* IDA
* windbg
* **CFF-Explorer**

反汇编过程即二进制转汇编助记符，参考 intel 指令集手册。
X86 为变长指令（灵活），arm 为定长指令（高效）\[ 4G 寻址问题 \]



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-01-09-windows-program2.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/docs.microsoft.com/3f7eeeb1.html" %})
- [https://docs.microsoft.com/en-us/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/docs.microsoft.com/6c6aee69.html" %})
- [https://github.com/microsoft/Detours]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/github.com/f10fd70b.html" %})
- [https://github.com/reactos/reactos]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/github.com/f366a913.html" %})
- [https://sysprogs.com/legacy/virtualkd]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/sysprogs.com/6caf3e13.html" %})
- [https://github.com/yuan-xy/pea-search/blob/master/filesearch/ntfs.cpp]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/github.com/cbe71bc2.html" %})
- [https://www.virusbulletin.com/virusbulletin/2018/09/through-looking-glass-webcam-interception-and-protection-kernel-mode/]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/www.virusbulletin.com/00030afb.html" %})
- [https://www.sourceinsight.com]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/www.sourceinsight.com/8f9f2ff2.html" %})
- [https://ntcore.com/?page_id=388]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/ntcore.com/fdf592d1.html" %})
- [https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite]({% include relrefx.html url="/backup/2022-01-09-windows-program2.md/docs.microsoft.com/0c438a9b.html" %})
