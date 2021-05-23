---
layout: post
title: "调试 C++ -- GFlags 检查内存越界、野指针等作用的工具使用"
author:
location: "珠海"
categories: ["调试"]
tags: ["调试", "Memory", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "Windbg"
---

打开检查功能：

```shell
gflags /p /enable **.exe /full
```

关闭检查功能：

```shell
gflags /p /disable **.exe
```

列出当前启动了页堆的进程列表：

```shell
gflags /p
```


## 案例

调试运行，程序退出时崩溃在 ntdll 中的一个函数中，output 窗口中输出：

```shell
HEAP: Free Heap block xxxxxx modified at xxxxxx after it was freed
```

此时，无法快速找出程序哪里出现了内存非法访问。


## 解决方法

a. 安装 Debugging Tools for Windows（也就是 WinDbg），安装后将安装目录添加到 Path 环境变量中。

b. 执行：`gflags -p /enable ***.exe /full "***.exe"`，为需要调试的程序名称，不需要完整路径。该命令行会在注册表里设置一些调试参数，使内存在使用的时候加入了保护机制，
一旦内存写越界，或者发生野指针的问题，都会导致一个中断。由此，就可以确定问题到底出在哪里了。

配置正常页堆：

```shell
"C:/Program Files/Debugging Tools for Windows (x86)/gflags.exe" /p /enable qq.exe
```

配置完全页堆：

```shell
"C:/Program Files/Debugging Tools for Windows (x86)/gflags.exe" /p /enable qq.exe /full
```

列出当前启动了页堆的进程列表：

```shell
"C:/Program Files/Debugging Tools for Windows (x86)/gflags.exe" /p
```

取消页堆设置：

```shell
"C:/Program Files/Debugging Tools for Windows (x86)/gflags.exe" /p /disable qq.exe
```

c. 调试运行自己的程序，此时 Visual C++ 会直接定位在有问题的代码处。

d. 删除注册表中的调试设置：`gflags -p /disable ***.exe`


## 页堆 Page Heap

从 Windows 2000 开始操作系统开始在堆管理器引入“校验层”，即 Page Heap 管理器。这个校验层处于 Ntdll.dll 模块内。
可以验证应用程序所有的动态内存操作（读写、分配、释放及其它操作）。

页堆有两种类型：正常页堆和完全页堆（Full Page Heap）。


### **完全页堆**

当分配一块内存时，通过调整内存块的分配位置，使其结尾恰好与系统分页边界对齐，然后在边界处再多分配一个不可访问的页作为保护区域。这样，一旦出现内存读 / 写越界时，进程就会 Crash，从而帮助及时检查内存越界。

因为每次分配的内存都要以这种形式布局，尤其对于小片的内存分配，即使分配一个字节，也要分配一个内存页，和一个保留的虚拟内存页（注意在目前的实现中，这个用作边界保护区域的页从来不会被提交）。
这就需要大量的内存，到底一个进程需要多少内存，很难估算，因此在使用 Page Heap 前，至少保证你的机器至少设置了 1G 虚拟内存以上。


### **正常页堆**

正常页堆原理与 CRT 调试内存分配函数类似，通过分配少量的填充信息，在释放内存块时检查填充区域。来检测内存是否被损坏，此方法的优点是极大的减少了内存耗用量。
缺点是只能在释放块时检测，不太好跟踪出错的代码位置。


### **GFlags、AppVerifier、Pageheap.exe**

GFlags、AppVerifier、Pageheap.exe 是三种外壳工具，都是用来方便用户配置 Page heap 选项的。Page Heap 选项位于注册表目录：

```shell
HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows NT/CurrentVersion/Image File Execution Options/**你的可执行程序名**/
```

当 Windows 开始启动一个进程时，Window 通过检查这个注册表目录的设置，对该进程应用相应的 PageHeap 选项。

**Pageheap.exe**

PageHeap 配置工具，在 Windows 2000 Professional SP2 以上可用。已经被 GFlags 取代。

**GFlags**

老牌的 PageHeap 配置工具，有命令行和 GUI 两种操作方式，功能比较全，包含在 Windbg 调试器安装包内。同样在 Windows 2000 Professional SP2 以上可用。

**AppVerifier**

新的 PageHeap 配置工具，需要 XP 系统才支持。VS2005 内置了 AppVerifier 支持，用“Debug”菜单—>“Start With Application Verifier”启动程序，会自动启动 Page Heap。

一定需要这些工具吗？

正如前面提到的，PageHeap 属于操作系统提供的功能，这几个工具只是方便修改注册表中的选项，在实际应用中可以通过直接修改注册表来启用 PageHeap。
这在客户的机器上很有用，不再要求客户去安装这些软件。


## 一些特殊选项解释

/unaligned

这个选项只能用于完全页堆。当我们从普通堆管理器分配一块内存时，内存总是 8 字节对齐的，页堆默认情况下也会使用这个对齐规则，
但是这会导致分配的内存块的结尾不能跟页边界精确对齐，可能存在 0-7 个字节的间隙，显然，对位于间隙范围内的访问是不会被立即发现。
更准确的说，读操作将永远不能被发现，写操作则要等到内存块释放时校验间隙空间内的填充信息时才发现。
/unaligned 用于修正这个缺陷，它指定页堆管理器不必遵守 8 字节对齐规则，保证内存块尾部精确对齐页边界。
需要注意的是，一些程序启用这个选项可能出现异常，例如 IE 和 QQ 就不支持。

/backwards

这个选项只能用于完全页堆。这个选项使得分配的内存块头部与页边界对齐（而不是尾部与边界对齐），通过这个选项来检查头部的访问越界。

/debug

指定一启动进程即 Attach 到调试器，对于那些不能自动生成 dump 的程序，是比较有用的选项。


## 页堆能校验的有效范围

所有内存分配函数，只要最终调用到 ntdll.Dll 堆管理函数（即 RtlAllocateHeap，RtlFreeHeap），页堆都是有效的。具体包括：
诸如 HeapAlloc、HeapFree、HeapReAlloc、LocalAlloc、LocalFree、LocalReAlloc 等等。
Kernel32 提供的堆管理函数。CRT 内存分配如：malloc、free、realloc、msize、expand、运算符 new、delete、new[]、delete[] 等等。
但页堆不能用于验证虚拟内存分配函数如：VirtualAlloc、VirtualFree 等分配的内存块。


## 页堆能处理的错误类型

错误类型 | 正常页堆 | 整页堆
---- | ---- | ----
堆句柄无效 | 立即发现 | 立即发现
堆内存块指针无效 | 立即发现 | 立即发现
多线程访问堆不同步 | 立即发现 | 立即发现
假设重新分配返回相同地址 (realloc) | 90% 内存释放后发现 | 90% 立即发现
内存块重复释放 | 90% 立即发现 | 90% 立即发现
访问已释放的内存块 | 90% 在实际释放后发现 | 90% 立即发现
访问块结尾之后的内容 | 在释放后发现 | 立即发现
访问块开始之前的内容 | 在释放后发现 | 立即发现


## Others

1. 注册内存分配 / 释放钩子函数 (hook)。在 Linux 下可以 malloc_hook, free_hook 等 5 个钩子函数，
    在 Windows 下可以注册 _CrtSetAllocHook 钩子函数，这样在分配内存的时候就可以捕获这一请求并加以处理。
    Visual Leak Detecter 和 mtrace 使用此方式。
2. 使用宏定义替换。将用户代码中的 malloc, free 替换为宏定义的 mwMalloc(sz, \__FILE__, \__LINE__) 等自定义函数，
    从而跟踪内存请求，memwatch 即使用此方式。
3. 操作符重载。此方法仅用于 C++ 语言中，通过重载 new、delete 操作符来实现跟踪内存请求，
    重载后的操作符类似于钩子函数意义。debug_new 采用此方式。

* [Using UMDH to Find a User-Mode Memory Leak](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/using-umdh-to-find-a-user-mode-memory-leak)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-26-memory-leak-gflags.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/using-umdh-to-find-a-user-mode-memory-leak]({% include relrefx.html url="/backup/2020-12-26-memory-leak-gflags.md/docs.microsoft.com/2856424b.html" %})
