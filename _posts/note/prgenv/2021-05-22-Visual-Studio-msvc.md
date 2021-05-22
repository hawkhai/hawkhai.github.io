---
layout: post
title: "开发环境 -- Visual Studio & WinDBG 平台高级调试与优化"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "Visual Studio"
---

Windows 平台高级调试与优化 —— VC 开发工具
张银奎 (Raymond Zhang)

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522151547.jpg" caption="知识盲区永远存在，下午茶大饼好吃。" %}


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


## 异常处理和崩溃


### JIT 调试

{% include image.html url="/assets/images/210522-visual-studio-msvc/20210522170340.png" caption="应用程序崩溃和 JIT 调试" %}

* 没有包含所有细节
* 因版本不同会略有不同
* 在使用 WinDBG 的内核调试中，不能对这个函数设置断点 —— 死循环
* 可以使用 ITP 来跟踪

{% include image.html url="/assets/images/210522-visual-studio-msvc/winadt_raymond_all2021_118.png" caption="KiExceptionDispatch" %}

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-22-Visual-Studio-msvc.md.js" %}'></script></p>
