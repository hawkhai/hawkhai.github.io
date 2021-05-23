---
layout: post
title: "调试 -- Visual Studio & WinDBG 平台高级调试与优化"
author:
location: "珠海"
categories: ["调试"]
tags: ["调试", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---

Windows 平台高级调试与优化 —— VC 开发工具
张银奎 (Raymond Zhang)

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522151547.jpg" caption="知识盲区永远存在，下午茶大饼好吃。" %}

**为了更好的处理内存问题，我们要尽力保证 Debug 版本（更多的运行检查）和 x64 版本（页堆才能顺利开启）都能顺利编译出来，另外编译器也要及时升级。**


## MS Visual C++ 简史

版本 发布时间 新增主要功能

* MSC 7.0 1992 C++、MFC 1.0
* MSVC 1.0 1992 32 位支持，MFC 2.0
* MSVC 2.0 1994 MFC 3.0
* MSVC 4.0 1995 MFC 4.0，Developer Studio IDE（MSDEV.exe），ClassView
* MSVC 4.2 1996 MFC 4.2
* MSVC 5.0 1997 MFC 4.21，COM
* MSVC 6.0 1998 运行时错误检查，Edit and Continue，MFC 6.0
* MSVC 7.0 2002 Visual Studio .NET 2002（又称 VS7.0）的一部分，.NET 支持，link time code generation，MFC 7.0
* MSVC 7.1 2003 Visual Studio .NET 2003（又称 VS7.1）的一部分，Visual J#，MFC 7.1
* MSVC 8.0 2005 Visual Studio 2005（又称 VS8.0）的一部分，C++/CLI，OpenMP，MFC 8.0
* MSVC 9.0 2007 Visual Studio 2008（又称 VS9.0）的一部分
* MSVC 10.0 2010 Visual Studio 2010，partial support for C++11
* MSVC 11.0 2012 Visual Studio 2012， improved C++11 support
* MSVC 12.0 2013 Visual Studio 2013，C++11 and C99 support
* MSVC14.0 2015 Visual Studio 2015，improved C++11/14 support
* MSVC 14.1 2017 Visual Studio 2017
* MSVC 14.2 2019 Visual Studio 2019


## 软件的编译和构建过程

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522134245.png" caption="软件的编译和构建过程" %}

Parallel Stack（并行调用栈）
* 调试 >> 窗口 >> 并行堆栈（调试状态暂停可以看到）

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522142723.png" %}

```cpp
extern "C" int WINAPI
_tWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    _In_ LPTSTR lpCmdLine, int nCmdShow)
#pragma warning(suppress: 4985)
{
    // call shared/exported WinMain
    return AfxWinMain(hInstance, hPrevInstance, lpCmdLine, nCmdShow);
}

    static int __cdecl invoke_main()
    {
        return wWinMain(
            reinterpret_cast<HINSTANCE>(&__ImageBase),
            nullptr,
            _get_wide_winmain_command_line(),
            __scrt_get_show_window_mode());
    }

static __declspec(noinline) int __cdecl __scrt_common_main_seh()
{
    if (!__scrt_initialize_crt(__scrt_module_type::exe))
        __scrt_fastfail(FAST_FAIL_FATAL_APP_EXIT);

    bool has_cctor = false;
    __try
    {
        bool const is_nested = __scrt_acquire_startup_lock();

        if (__scrt_current_native_startup_state == __scrt_native_startup_state::initializing)
        {
            __scrt_fastfail(FAST_FAIL_FATAL_APP_EXIT);
        }
        else if (__scrt_current_native_startup_state == __scrt_native_startup_state::uninitialized)
        {
            __scrt_current_native_startup_state = __scrt_native_startup_state::initializing;

            if (_initterm_e(__xi_a, __xi_z) != 0)
                return 255;

            _initterm(__xc_a, __xc_z);

            __scrt_current_native_startup_state = __scrt_native_startup_state::initialized;
        }
        else
        {
            has_cctor = true;
        }

        __scrt_release_startup_lock(is_nested);

        // If this module has any dynamically initialized __declspec(thread)
        // variables, then we invoke their initialization for the primary thread
        // used to start the process:
        _tls_callback_type const* const tls_init_callback = __scrt_get_dyn_tls_init_callback();
        if (*tls_init_callback != nullptr && __scrt_is_nonwritable_in_current_image(tls_init_callback))
        {
            (*tls_init_callback)(nullptr, DLL_THREAD_ATTACH, nullptr);
        }

        // If this module has any thread-local destructors, register the
        // callback function with the Unified CRT to run on exit.
        _tls_callback_type const * const tls_dtor_callback = __scrt_get_dyn_tls_dtor_callback();
        if (*tls_dtor_callback != nullptr && __scrt_is_nonwritable_in_current_image(tls_dtor_callback))
        {
            _register_thread_local_exe_atexit_callback(*tls_dtor_callback);
        }

        //
        // Initialization is complete; invoke main...
        //

        int const main_result = invoke_main();

        //
        // main has returned; exit somehow...
        //

        if (!__scrt_is_managed_app())
            exit(main_result);

        if (!has_cctor)
            _cexit();

        // Finally, we terminate the CRT:
        __scrt_uninitialize_crt(true, false);
        return main_result;
    }
    __except (_seh_filter_exe(GetExceptionCode(), GetExceptionInformation()))
    {
        // Note:  We should never reach this except clause.
        int const main_result = GetExceptionCode();

        if (!__scrt_is_managed_app())
            _exit(main_result);

        if (!has_cctor)
            _c_exit();

        return main_result;
    }
}

// This is the common main implementation to which all of the CRT main functions
// delegate (for executables; DLLs are handled separately).
static __forceinline int __cdecl __scrt_common_main()
{
    // The /GS security cookie must be initialized before any exception handling
    // targeting the current image is registered.  No function using exception
    // handling can be called in the current image until after this call:
    __security_init_cookie();

    return __scrt_common_main_seh();
}

extern "C" int wWinMainCRTStartup()
{
    return __scrt_common_main();
}
```


## Data Breakpoint

* Monitor variables
* WinDBG’ba command, rely on CPU’s debug register
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522150040.png" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522150126.png" caption="Hit of Data Breakpoint" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522150417.png" caption="WPF Tracing" %}


## PDB 的文件布局

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522134535.png" caption="PDB 的文件布局" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522134634.png" %}


## 编译器的运行期检查

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522144017.png" %}


## 细看一个函数

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522145653.png" caption="P95" %}


## WinDBG 概览

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522165140.png" caption="WinDBG Internals" %}


### WinDBG 的发展历史

* 前身 KD 和 NTSD
    * 在开始开发 NT 内核的时候开始开发，1989 年
* C 阶段的 WinDBG
    * 大约在 1992 年 4 月开始开发
    * 版本号与 NT 内核的版本号一致
    * 到 Win2K 时结束
* P 阶段的 WinDBG
    * 在 C 阶段代码基础上重构
    * 第一个版本与 2000 年 4 月 WinHec 会议上露面
    * 2000/09/21 重构后的 1.0 版本正式发行
    * 目前（2009 年 3 月）版本是 6.11

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522152155.png" caption="绿色软件 很多宝贝" %}

* dbgeng.dll


### 命令表达式

* 支持两种表达式
    * C++ 表达式
    * MASM 表达式
* 默认使用 MASM 表达式
* 使用 @@masm(…) 或者 @@c++(…) 可以显式指定括号中的表达式所使用的语法类型
* 使用 ?(MASM) 或者 ??(C++) 评估表达式的取值
* `.expr`

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522153707.png" %}


### 硬件断点示例

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522161038.png" %}

* 陷阱类异常 —— 命中时，访问指令已经执行完毕
* EIP 指向下一条指令，串指令例外


### 8 个通用寄存器

* EAX 函数返回值
* ECX 循环次数
* ESI，EDI 串操作的源和目标
* ESP 栈顶
* EBP 栈帧基地址
* 长模式下都为 64 位，RAX…

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522162644.png" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522162812.png" caption="所有模式下都为 16 位长" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522162917.png" caption="1 个标志寄存器 + 1 个 IP" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522163036.png" caption="EFlags" %}
{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522163139.png" caption="Control Registers" %}


### 调试事件

* EXCEPTION_DEBUG_EVENT
* CREATE_THREAD_DEBUG_EVENT
* CREATE_PROCESS_DEBUG_EVENT
* EXIT_THREAD_DEBUG_EVENT
* EXIT_PROCESS_DEBUG_EVENT
* LOAD_DLL_DEBUG_EVENT
* UNLOAD_DLL_DEBUG_EVENT
* OUTPUT_DEBUG_STRING_EVENT


## 异常处理和崩溃


### JIT 调试

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522170340.png" caption="应用程序崩溃和 JIT 调试" %}

* 没有包含所有细节
* 因版本不同会略有不同
* 在使用 WinDBG 的内核调试中，不能对这个函数设置断点 —— 死循环
* 可以使用 ITP 来跟踪

{% include image.html url="/assets/images/210522-visual-studio-msvc/winadt_raymond_all2021_118.png" caption="KiExceptionDispatch" %}


### 分发用户态异常

```cpp
if (FirstChance) {
    if (PsGetCurrentProcess()->DebugPort == 0 // 没有用户调试器
        || KdIsThisAKdTrap(Tf, &Context)) { // 内核调试器
        // 分发给内核调试器
        if (KiDebugRoutine &&
            KiDebugRoutine(Tf, Reserved, Er, &Context,
            PreviousMode, FirstChance) != 0) break;
    }

    if (DbgkForwardException(TrapFrame,
        DebugEvent, FirstChance) != 0) return;
    if (valid_user_mode_stack_with_enough_space) {
        copy_context_and_exception_record_2_user_stack; // 上下文拷贝到用户空间
        TrapFrame->Eip = KeUserExceptionDispatcher; // 飞程序指针
        return;
    }
}
if (DbgkForwardException(Tf, TRUE, LastChance) != 0) return;
if (DbgkForwardException(Tf, FALSE, LastChance) != 0) return;
ZwTerminateProcess(NtCurrentThread(), Er->ExceptionCode);
```


### JIT 调试器的设置

* Hive: HKEY_LOCAL_MACHINE
Key: SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
* To set alternative JIT debuggers, just change the debuggers key
```
windbg -I
```

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210523094139.png" %}


## 深入理解栈


## 调试堆

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210523114638.png" caption="Windows 内存管理" %}

```
D:\dbglabs\bin\release>"D:\Windows Kits\10\Debuggers\x86\gflags.exe" -i heapmfc.exe +ust
Current Registry Settings for heapmfc.exe executable are: 00001000
    ust - Create user mode stack trace database
D:\dbglabs\bin\release>"D:\Windows Kits\10\Debuggers\x86\umdh.exe" -pn:heapmfc.exe
```


## 多线程调试


### D Profile 开源性能分析工具

[from](https://bbs.pediy.com/thread-195774.htm)
D Profile 是一个 win32/64 CPU，memory 性能分析工具：<https://github.com/xwlan/dprofiler>
D Profiler a lightweight, low overhead CPU Memory IO and Lock profiler for Windows x86/x64.
Build in cmd.exe, run command as: msbuild dprofiler.sln


## 转储和转储分析


## 事件追踪和调优

* Windows Software Trace Preprocessor


## 使用硬件调试器调试 Windows 内核的启动过程

[from](http://advdbg.org/blogs/advdbg_system/archive/2012/10/05/5427.aspx)
最近公司刚买了一台 CEDT 硬件仿真器,  能调试从系统复位到关机重启的所有过程。我拿来跟了一下 windows 的内核启动过程，看了看完全真实的 Windows 初始化过程 :

* CEDT 开机后会请求用户选择目标系统的处理器类型。选择后，机器会在 BIOS 自动连接目标计算机。连接成功后，亲切的 Windbg 界面出现了。
* 停止系统运行后，发现系统停在 BIOS 里。在 Windbg 的命令行敲“！runto nt”，目标机继续运行，直到 Windbg 停止。
* EDT 提供命令直接执行到 nt!KiSystemStartup 然后停下来。然后打开 CEDT 的代码追踪功能，“！trclbr on”。从 BOOTLOADER 会传给 KiSystemStartup 一个结构的地址，结构中包含了 BOOT 的一些基本的信息，例如，引导分区，文件系统类型等等。KiSystemStartup 首先将该结构指针赋值变量 KeLoaderBlock。紧接着，KiSystemStartup 会将 P0BootStack 和 KiIdleThread0 的地址存入 LOADER_BLOCK 中。FS 寄存器会被赋值 0x30 并将 FS:[0x130] 清零。
* 调用 KiInitializeMachineType（）。KiInitializeMachineType（）从 KeLoaderBlock 中读取设备类型并赋值 KeI386MachineType。
* 调用 GetMachineBootPointers（）获取当前的 GDTR 和 IDTR 信息。然后为中断程序和 NMI 等初始化 TSS。
* 调用 KiInitializePcr（）. 初始化 KiIdleThread0 的 ApcState，将 KiIdleProcess 的指针赋给 KiIdleThread0->ApcState.Process.
* 调用 KiSwapIDT() 然后用 IDT 中的中断处理函数表初始化中断向量表。
* 调用 KiProcessorStart(). 这个函数只是判断了一下 KiProcessorStartControl 的值，看起来它像是个简单状态机的键。在这时，什么也没做就退出了。
* 调用 HalInitializeProcessor（），HalInitializeProcessor（）读取 CPUID 获得当前系统中的实际处理核个数，并初始化 HalPrivateDispatchTable 中的重要服务，其中 HalpSetupPciDeviceForDebugging，HalpReleasePciDeviceForDebugging，HalpGetAcpiTablePhase0，HalpCheckPowerButton，HalpMapPhysicalMemory64，HalpUnmapVirtualAddress。 初始化 8259 和 APIC 的中断处理程序。
* 调用 KdInitSystem（），KdInitSystem 首先检查是否是 DEBUG 模式，如果是，他会把 KdpStub 赋给 KiDebugRoutine，并且初始化 KdpDebuggerDataListHead 和 KdVersionBlock。 原来我们经常用来调试的 STUB 是在这初始化的。
* 调用 KdPollBreakIn（）来收取调试的报文，如果有 BREAKIN 报文收到，赋值 KdpControlCPressed 并返回非零。并在退出后进入 DbgBreakPointWithStatus（）。
* 在接下来程序中，KiBootFeatureBits 的 Bit7 将会设为 1。
* 调用 KiInitializeKernel（）。在 KiInitializeKernel 中，首先
    * 调用 _SEH_prolog（）；
    * 调 KiSetProcessorType（）通过检查处理器 STEPPING 和从 CPUID 中读取信息获得处理器种类并设置 _KPRCB. CpuType.  KiSetCR0Bits（）根据处理器类型设置 CR0 的 BIT16。 调用 KiIsNpxPresent（）判断是否支持浮点运算器。
    * 初始化 KPRCB. MaximumDpcQueueDepth, KPRCB. MinimumDpcRate, KPRCB.AdjustDpcThreshold
    * 调用 PoInitializePrcb（）初始化 KPRCB.PROCESSOR_POWER_STATE，
    * 调用 KeInitializeDpc（）填充 KDPC。调用 KeInitializeTimerEx（）初始化一个内核同步定时器。
    * 检查了 BOOTOPTION 的设置。设置 EFER 寄存器的 LME， 启动 IA-32e 模式。
    * 中间省略了一些代码的分析，包括初始化 Ki486CompatibilityLock，KiFreezeExecutionLock 等。
    * 调用 KeInitializeProcess（）填充第一个进程的 KPROCESS。
    * 根据 FeatureBits 初始化线程的参数。调用 KeInitializeThread() 初始化线程 KiIdleThread0， 堆栈 P0BootStack，进程为前面初始化的进程。
    * 调用 KeStartThread（）设置 KiIdleThread0 为 READY 状态。
    * 调用 ExpInitializeExecutive（），初始化 OBJECT 管理器，初始化安全， 进程管理器以及 PNP 管理器。在进程管理器的初始化过程中，创建 PsInitialSystemProcess 以及线程 Phase1Initialization（）。PNP 管理器的初始化过程将读取注册表中的设备资源用于初始化。
* 调用 MmCreateKernelStack（）创建内核的堆栈。
* 进入 KiIdleLoop（）。

{% include image.html url="/assets/images/210522-visual-studio-msvc/2021523-15549.jpeg" %}

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-22-Visual-Studio-msvc.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://bbs.pediy.com/thread-195774.htm]({% include relrefx.html url="/backup/2021-05-22-Visual-Studio-msvc.md/bbs.pediy.com/10890851.htm" %})
- [https://github.com/xwlan/dprofiler]({% include relrefx.html url="/backup/2021-05-22-Visual-Studio-msvc.md/github.com/faf10891.html" %})
- [http://advdbg.org/blogs/advdbg_system/archive/2012/10/05/5427.aspx]({% include relrefx.html url="/backup/2021-05-22-Visual-Studio-msvc.md/advdbg.org/9d96ab00.aspx" %})
