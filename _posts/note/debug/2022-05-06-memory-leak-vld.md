---
layout: post
title: "编程与调试 C++ -- VLD (Visual LeakDetector) 内存泄露库的使用"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory", "C/C++"]
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


## vld.exe

VLD (Visual LeakDetector) 内存泄露库的使用，VLD 是一款用于 Visual C++ 的免费内存泄漏检查工具。
1. 可以得到内存泄漏点的调用堆栈，如果可以的话，还可以得到其所在的文件及行号；
2. 可以得到泄漏内存的完整数据；
3. 恶意设置内存泄漏报告的级别；
4. 它以动态库的形式提供，无需编译源代码，只需要很小的改动程序；
5. 源代码使用 GNU 许可发布，并有详细的文档及其注释。

VLD 网址：[vld.codeplex.com {% include relref_github.html %}](https://kinddragon.github.io/vld/)
<http://www.codeproject.com/Articles/9815/Visual-Leak-Detector-Enhanced-Memory-Leak-Detectio>

1. VLD 只能在 Windows 下使用，在包含 vld.h 头文件时增加预编译选项。
2. 在 Release 模式下，不会链接 VisualLeak Detector。
3. Windows 提供了一个 StackWalk64 函数可以获得堆栈的内容。

VLD 工具原理。在初始化是 VLD 使用 \_CrtSetAllocation 注册这个钩子函数。
```cpp
int AllocHook(int allocType,
        void* userData, size_t size,
        int blockType, long requestNumber,
        const unsigned char* filename, int lineNumber);
```


## LeakSanitizer

lsan_suppressions.txt

LeakSanitizer 是一个运行时期的内存泄漏检测器。可以跟 AddressSanitizer 结合起来，用于检测内存错误及内存泄漏，也可以单独使用。LSan 几乎不会带来性能上的影响，直到程序终止。即一旦检测到内存问题，程序即会终止，这一点与 ASan 一致。


## drmemory

DrMemory-Windows-sfx.exe

**Dr. Memory** (www.drmemory.org) is an open-source dynamic memory
monitoring tool for Windows, Linux, and Mac.



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-06-memory-leak-vld.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://kinddragon.github.io/vld/]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/kinddragon.github.io/56acbbc3.html" %})
- [http://www.codeproject.com/Articles/9815/Visual-Leak-Detector-Enhanced-Memory-Leak-Detectio]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/www.codeproject.com/234cf836.html" %})
