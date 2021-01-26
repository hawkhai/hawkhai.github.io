---
layout: post
title: "调试 -- VS 程序员使用 windbg 实例"
author:
location: "珠海"
categories: ["调试"]
tags: ["编程笔记", "调试"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

如果使用 32 位的 windbg，windbg 加载完 dump 文件后，窗口会显示 wow64cpu，表示是 64 位进程，需要切换到 64 位环境：

```
.load wow64exts
!sw
```


## 设置符号表（crtl + s）

```
srv*D:\DumpAnalysis\ms_symbols*https://msdl.microsoft.com/download/symbols;
srv*D:\DumpAnalysis\toy_symbols*\\10.1.32.208\symbols;
```

如果堆栈显示 `toyhelper!0x3838`，表示 `toyhelper` 模块加载符号表失败，可以显示符号表全路径寻址，手动把符号表文件放到加载的路径，完成手动加载指定模块：

```
!lmi toyhelper      // 查找名为 toyhelper 模块的 pdb 文件是否已经被正确加载了
!sym noisy          // 当 Windbg 加载 Symbol 文件的时候，显示 Symbol 的路径，默认情况下是不显示的。
.reload /f xxx.dll  // 重新加载指定模块的符号表文件。
.reload /i xxx.dll  // 如果确定代码是完全一样的，只是编译时间引起加载符号表加载错误，可以使用此命令行忽略符号表的检查。
lmvm xxx            // 这个命令不能带文件后缀。可以查看模块的版本号，文件大小。
CheckSum            // 这两项信息可以校验文件是否损坏、篡改
```

建议本地有一份和编译服务器同样目录的源码，这样的话操作符号表文件也方便点，如果符号表不匹配，可以直接从编译产出目录把符号表文件拷贝到同路径构建目录。


## VS 操作习惯的 Windbg

如果符号表齐全并且代码目录和编译服务器的代码目录一致，`alt+3`（局部变量窗口）、`alt+6`（当前线程堆栈窗口）、`alt+9`（线程列表窗口），可以很方便的，和使用 vs 差不多一样的查看代码、线程、线程堆栈，点击切换栈帧，查看当前栈帧的局部变量。右键这些窗口选择 dock（停靠），使用习惯可以更接近 vs 了。想同时观察多个命令，可以用 ctrl+n 打开多个命令窗口。如果没有符号表，或者符号表不齐全，或者代码目录和编译服务器的代码目录不一致，很多东西还是得用命令行。

```
!analyze -v         // 最为强大的命令，自动分析 dump，并输出错误信息，输出建议命令行
```

命令执行后，自动分析并显示有问题的堆栈，有错误提示，并且有推荐的命令行的。一般推荐的命令行很给力，可以直接看到出问题的堆栈。例如 `~41s; .ecxr; kvn`。意思切换到 41 号线程，修复堆栈，显示堆栈。错误提示也蛮给力的，可以留意一下。

```
~72s                // 切换到 72 号线程（最后记得带 s）
```

k 命令显示当前线程调用堆栈、帧数、简单参数值，n 表示帧号：

```
0:037> kvn
# ChildEBP RetAddr Args to Child
00 06abfb7c 7c92df3c 7c93b22b 000008dc 00000000 ntdll!KiFastSystemCallRet (FPO: [0,0,0])
01 06abfb80 7c93b22b 000008dc 00000000 00000000 ntdll!NtWaitForSingleObject+0xc (FPO: [3,0,0])
02 06abfc08 7c921046 00ab61c8 769ad222 76ab61c8 ntdll!RtlpWaitForCriticalSection+0x132 (FPO: [Non-Fpo])
03 06abfc10 769ad222 76ab61c8 0b2cbd98 76ab61c0 ntdll!RtlEnterCriticalSection+0x46 (FPO: [1,0,0])
04 06abfc20 769afb04 0b2cbd98 00000080 00000001 ole32!COleStaticMutexSem::Request+0x59 (FPO: [0,0,0])
05 06abfdcc 769afd56 0b2cbd98 00000080 00000001 ole32!COIDTable::ThreadCleanup+0x32 (FPO: [Non-Fpo])
06 06abfdf8 769afca9 00000000 06abfe44 76ab67e8 ole32!FinishShutdown+0x69 (FPO: [Non-Fpo])
07 06abfe14 769af231 00000000 00000000 0b2cbd98 ole32!ApartmentUninitialize+0x7e (FPO: [Non-Fpo])
08 06abfe2c 769aee98 06abfe44 00000000 00000001 ole32!wCoUninitialize+0x41 (FPO: [Non-Fpo])
09 06abfe48 769dc269 00000001 76990000 769ad1ba ole32!CoUninitialize+0x5b (FPO: [Non-Fpo])
0a 06abfe54 769ad1ba 06abfe7c 769ad159 76990000 ole32!DoThreadSpecificCleanup+0x4f (FPO: [0,0,0])
0b 06abfe5c 769ad159 76990000 00000003 00000000 ole32!ThreadNotification+0x37 (FPO: [Non-Fpo])
0c 06abfe7c 769ad101 76990000 00000003 00000000 ole32!DllMain+0x147 (FPO: [Non-Fpo])
0d 06abfe9c 7c92118a 76990000 00000003 00000000 ole32!_DllMainCRTStartup+0x52 (FPO: [Non-Fpo])
0e 06abfebc 7c933a23 769ad0b9 76990000 00000003 ntdll!LdrpCallInitRoutine+0x140f 06abff34 7c80c126 0012f144 7c92e900 0190cd00 ntdll!LdrShutdownThread+0xd7 (FPO: [Non-Fpo])
10 06abff6c 7813299f 00000000 781329c1 00000000 kernel32!ExitThread+0x3e (FPO: [Non-Fpo])
11 06abff74 781329c0 00000000 371c30cd 0012f144 msvcr80!_endthreadex+0x1f (FPO: [1,0,0]) (CONV: cdecl) [f:\sp\vctools\crt_bld\self_x86\crt\src\threadex.c @ 412]
12 06abffac 78132a47 7c92e900 7c80b713 0190cd00 msvcr80!_callthreadstartex+0x20 (FPO: [Non-Fpo]) (CONV: cdecl) [f:\sp\vctools\crt_bld\self_x86\crt\src\threadex.c @ 348]
13 06abffb4 7c80b713 0190cd00 0012f144 7c92e900 msvcr80!_threadstartex+0x66 (FPO: [1,0,4]) (CONV: stdcall) [f:\sp\vctools\crt_bld\self_x86\crt\src\threadex.c @ 326]
14 06abffec 00000000 781329e1 0190cd00 00000000 kernel32!BaseThreadStart+0x37 (FPO: [Non-Fpo])
```

切换调用帧：

```
.frame 13
```

来到上面堆栈的 13 帧：

```
13 06abffb4 7c80b713 0190cd00 0012f144 7c92e900 msvcr80!_threadstartex+0x66 (FPO: [1,0,4]) (CONV: stdcall) [f:\sp\vctools\crt_bld\self_x86\crt\src\threadex.c @ 326])
```

此命令挺好用的，如果源码在本地（建议本地有一份和编译服务器同样目录的源码），会直接跳转到相关代码。然后可以用 x 命令，显示当前帧的局部变量、参数（this 指针可以重点关注：dt this 地址，局部变量查看窗口有时候查看不了具体内容，dt 命令还是很好用的）。


## x 命令

运行 x 命令后，可以用 dt 命令行，显示各种代码级别的内容。例如 dt CStringW 082efefc 指定地址转成 CStringW 来查看值。直接用 du 命令行查看此地址是不行的。以上命令行方法，和 vs 点击堆栈，查看变量效果接近了。

将地址转为指定结构体：`dt KHealthProxyImpl 0xfffffffc`

切换到源码：

```
.open C:\Program Files (x86)\Microsoft Visual Studio 8\VC\crt\src\threadex.c
```

鼠标移到代码上，可以看到当前代码的局部变量、参数等。前提是当前线程当前帧，所以 `~s、.frame` 命令很重要。

dd wort、da ansic 编码、du unicode 编码、dds 根据地址还原堆栈（注意 winapi 中的 context 结构，可以用此命令行还原堆栈）


## 异常捕获的崩溃

__CxxUnhandledExceptionFilter 崩溃点（c、c++ 抛出异常，堆栈被运行库接管，需要还原堆栈）：.cxr dwo(__CxxUnhandledExceptionFilter 的第一个参数地址（左边开始第三个参数）+ 4)

然后 kb（或 kv、kvn）即可还原异常堆栈。

也可以用跟底层的命令还原堆栈：dt _CONTEXT __CxxUnhandledExceptionFilter 的第一个参数地址，上面命令行可以获得 ESP 的地址，然后再用 dds 命令行还原 ESP 堆栈，命令为：dds ESP 的地址 l100。

有些命令行是无限行数的，例如 dW 显示宽字节字符串、dds 显示堆栈，记得这种命令行一定要带上 l100，表示只显示 100 行，否则 windbg 会 busy，不容易中断。


## windbg 断点调试

可以做一些简单的技术逆向。

```
bu kernel32!CreateFileW
```

断点在 kernel32.dll 的 CreateFileW 函数，这个是 dll 的真正导出函数、不能用 CreateFile 这样的函数名，一定要指定 W 或 A 版本 api。

触发断点后，kb 查看堆栈。api 参数顺序从左到右，第三个开始才是真实函数参数。如果像上面断点 CreateFileW 的例子，需要先 f10 单步一下，函数参数才入栈，才能看到正确的前三个参数，如果不想单步就查看函数参数，或者要看第 3 个后面的参数，需要用下面的方法：

poi 是解引用，类似 C/C++ 的 \* 解引用指针，windbg 里面看到的参数数值都是地址，需要解引用。如果不想单步就查看函数参数，或者查看超过的 3 个函数参数，可以这样打印当前函数的堆栈，du poi(esp+4)。esp+4 是第一个参数、esp+8 是第二个参数，依次类推。du 是 unicode 字符串数据格式，如果整数换 dd，其他格式类推。查看 CreateFileW 的 7 个参数，可以用以下方法一次性查看。类型需要根据参数变化而变化，例如 %mu 表示 Unicode 字符串，%ma 表示 ANSI 字符串，%p 表示整数。

```
// 以下命令行可以打印前 7 个函数参数，如果参数数量不一样，可以自行减少、增加
.printf"%mu,%p,%p,%p,%p,%p,%p",poi(esp+4),poi(esp+8),poi(esp+c),poi(esp+10),poi(esp+14),poi(esp+18),poi(esp+1c)
.cls // 清除屏幕
!gle // getlasterror
```


## 死锁

定位卡死、通常是定位主线程卡死，因为其他线程卡死估计也暴露不了。
所以第一关注对象肯定是 0 号线程。

```
!locks 查看所有的线程占用的锁
~*k
0 号线程 wait -> x 号线程
x 号线程 wait -> y 号线程
……
y 号线程 wait -> 0 或 x 即会造成死锁
```

<https://blog.csdn.net/xxin_w/article/details/8449855>

```shell
!cs -l # 获取更为全面的关键区信息
!handle 000000c4 f # 查看该句柄的信息
!locks # 查看进程中哪些锁处于锁定状态
```


## 内存

```
查看分配的的内存：`!heap -a`
查看内存泄漏方法：`!heap –s`
查看程序内存状况
过一段时间再次通过 `!heap –s` 查看程序内存状况。找出增长较快的内存块，如 00b70000。
!!heap -stat -h 00b70000 查看 00b70000 内存详细情况
!heap -flt s 查进程中 size=ea60 的所有内存
0:000> !heap -flt s ea60
3.4 !heap -p –a 查看内存堆栈，定位泄露根源。
0:000> !heap -p -a 71614e38
0:000> !heap -p -a 721acf68
```

<https://blog.csdn.net/cuglifangzheng/article/details/50725890>
<https://blog.csdn.net/worldy/article/details/17888253>


## 进程信息

```
!runaway    // 显示当前进程中线程运行情况
vertarget   // 查看系统信息、系统运行时长 System Uptime、进程启动时间 Process Uptime
!peb        // 查看进程信息（进程的 ImageBaseAddress，进程的堆（Heap）起始地址， 装载了那些 DLL，命令行参数，系统的环境变量，mimidump 通常无效，可以查看 0 号线程堆栈，查看 main 函数参数）
!teb：      // 查看进程信息（栈（stack）的起始地址，Tls Storage 的地址，异常处理的地址，LastError 的值。
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-10-18-win-vs-windbg.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://msdl.microsoft.com/download/symbols]({% include relref.html url="/backup/2020-10-18-win-vs-windbg.md/msdl.microsoft.com/105143dc.html" %})
- [https://blog.csdn.net/xxin_w/article/details/8449855]({% include relref.html url="/backup/2020-10-18-win-vs-windbg.md/blog.csdn.net/8df66dff.html" %})
- [https://blog.csdn.net/cuglifangzheng/article/details/50725890]({% include relref.html url="/backup/2020-10-18-win-vs-windbg.md/blog.csdn.net/c4bc0b31.html" %})
- [https://blog.csdn.net/worldy/article/details/17888253]({% include relref.html url="/backup/2020-10-18-win-vs-windbg.md/blog.csdn.net/a11c9486.html" %})
