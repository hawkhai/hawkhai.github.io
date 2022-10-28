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
* Dan-Moulding <http://www.codeproject.com/Articles/9815/Visual-Leak-Detector-Enhanced-Memory-Leak-Detectio>

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

* <https://kinddragon.github.io/vld/>
    * **我使用的这个。** Latest release v2.5.1 - 2017-10-17 forked from dmoulding/vld
* <https://github.com/dmoulding/vld>
    * 这个应该是正版，和最初的同一个作者。非常古老了。
* <https://github.com/oneiric/vld>
    * vld-2.7.0-setup.exe - 13 Sep 2021
* <https://github.com/derickr/vld>
    * 这个点赞挺多的。


## LeakSanitizer

lsan_suppressions.txt

LeakSanitizer 是一个运行时期的内存泄漏检测器。可以跟 AddressSanitizer 结合起来，用于检测内存错误及内存泄漏，也可以单独使用。LSan 几乎不会带来性能上的影响，直到程序终止。即一旦检测到内存问题，程序即会终止，这一点与 ASan 一致。


## drmemory

DrMemory-Windows-sfx.exe

**Dr. Memory** (www.drmemory.org) is an open-source dynamic memory
monitoring tool for Windows, Linux, and Mac.


## Leakdiag

**内存泄露** from 大神同事 `zōu mǐn`。
这个最好用，比那个 UMDH 好用多了。
分析工具：
[Leakdiag](http://ftpmirror.your.org/pub/misc/ftp.microsoft.com/PSS/Tools/Developer%20Support%20Tools/LDGrapher/)

{% include image.html url="/assets/images/220506-memory-leak-vld/1.png" %}

步骤：
1. Toos 选项中配置符号路径以及堆栈级数
2. 选中 target.exe 进程
3. 选中 Windows Heap Alloctor
4. 点击 Start 开始监控
5. 出现内存异常时，点击 Log 记录内存分配信息
6. 打开日志文件，如：lo@kscan_2660_LDlog_6278bc35_sess_1.xml
    * 通常泄露的数据的堆栈信息都会有记录，但是有时候会无法记录堆栈，但是会有分配的堆栈的大小信息。
7. 查看大内存的分配数据
8. 因为没有记录下堆栈数据，使用 windbg 条件断点（当分配 16384 字节内存大小时断下）
   ```
   bp ntdll!RtlAllocateHeap "j(poi(@esp+c) = 16384) 'k';'gc'"
   ```
9. 8 步骤对应的代码为
10. 9 图中连续分配内存，但是没有地方释放
11. 9 图中的 Cahe 内存属于 ToyMemCache 对象，ToyMemCache 是 ToyEFileObj 的成员，
    IToyEFileObj 被 IToyEGenericScanStatus 持有，追溯到 IToyEGenericScanStatus 存在引用计数不平衡的问题。
12. 异常代码如下
    * Unpack 传入了 NULL 指针变量
    * 变指针为空时，它直接使用了临时堆栈中的**不可见栈变量地址**来接收指针，并且是个祼指针，导致了引用计数不平衡，泄露了内存。
13. 改法如下

{% include image.html url="/assets/images/220506-memory-leak-vld/2.png" relocate="6" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/3.png" relocate="7" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/4.png" relocate="9" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/5.png" relocate="12.1" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/6.png" relocate="12.1" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/7.png" relocate="12.2" %}
{% include image.html url="/assets/images/220506-memory-leak-vld/8.png" relocate="13" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-06-memory-leak-vld.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://kinddragon.github.io/vld/]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/kinddragon.github.io/56acbbc3.html" %})
- [http://www.codeproject.com/Articles/9815/Visual-Leak-Detector-Enhanced-Memory-Leak-Detectio]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/www.codeproject.com/234cf836.html" %})
- [https://github.com/dmoulding/vld]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/github.com/a11363fc.html" %})
- [https://github.com/oneiric/vld]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/github.com/8d5aee04.html" %})
- [https://github.com/derickr/vld]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/github.com/ab07174a.html" %})
- [http://ftpmirror.your.org/pub/misc/ftp.microsoft.com/PSS/Tools/Developer%20Support%20Tools/LDGrapher/]({% include relrefx.html url="/backup/2022-05-06-memory-leak-vld.md/ftpmirror.your.org/070ecfdd.html" %})
