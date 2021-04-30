---
layout: post
title: "调试 Memory -- Windows Windbg dump 内存访问错误"
author:
location: "珠海"
categories: ["调试"]
tags: ["调试", "Memory"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "Windbg"
---

多线程中的内存问题，一直被认为是噩梦般的存在，几乎只有高手、大仙才能解决。
少部分情况因为访存地址合法，会对数据造成破坏（悬垂指针或者野指针），一般会在运行一段时间后才因为异常退出。
这时候触发错误导致进程退出的代码位置往往不是“案发的第一现场”，给调试工作带来了更大的难度。


## 一些看法

个人一些看法，当一个工程有大时间又悠久的时候。

1. 尽量 MD/MT 采用 MT，这样一个模块一个堆，谁崩了算谁的，一般情况下，至少能缩小问题定位范围。
    * 也许会说 MD 节省空间，但是节省的几百 K，感觉意义并不大，一张小图片就几百 K 了。
2. 尽量 MD/MT 采用 MT，这样每个模块可以单独升级编译器（比如 vs2005 升级到 vs2019），否则存在多个模块关联，要同时升级，增加了难度。
3. 多线程堆问题是最麻烦的，崩溃的时候第一案发现场已经过了，取到的 dump 并不包含问题代码位置。
    * 第一步是问题重现。只要是可以稳定重现的 bug 都是很好解决的。
    * 工程开发尽量保证 Debug 模式，大部分堆内存问题都会直接报错，“烫烫烫烫”。
    * 开启完全页堆，gflags.exe，争取重现问题。当一个程序的内存大于 1G，这个方法也不行了，一开启，问题代码还没跑到，程序就内存不足崩溃了。
    * 最后的方法就是 git 里面去扒灰源代码，二分法 + code review，最后的倔强。-_-
    * 物归初始 此境初识。关键还是要提高程序员的编码质量。
        * 编写出来的代码可以同时用 cppcheck 等代码静态检测工具检测出一些野指针、无效变量等低级错误。


## 错误分类

常见的内存访问错误有以下几种：

* 写内存越界（MO，Memory Overrun）
* 读写非法内存，本质上也属于内存越界（IMR / IMW， Invalid Memory Read / Invalid Memory Write）
* 栈溢出，也属于内存越界的一种（SO，Stack Overflow）
* 访问未初始化内存（AUM，Access Uninitialized Memory）
* 释放内存的参数为非法值（Wild Free）
* 内存释放两次（DF，Double Free）
* 函数访问指向被调用函数的栈内内存的指针（UaR，Use after Return）
* 内存释放后使用（UaF，Use after Free）
* 内存泄露（ML，Memory Leak）

具体到 C/C++ 语言上面，会有更具体的错误，例如：

* 读取未初始化过的变量
* 野指针 / 悬垂指针读写
    * 野指针
        * 指针所在内存被其他代码非法修改（越界或者其他野指针误伤）
        * 释放内存的参数为非法值（Wild Free），也可能是上一条原因导致
    * 悬垂指针
        * 内存释放后使用（UaF，Use after Free）
        * 内存释放两次（DF，Double Free），第二次释放导致 coredump
* 错误的指针类型转换
* 从已分配内存块的尾部进行读 / 写（数组等类型读写越界）
* 不匹配地使用 malloc/new/new[] 和 free/delete/delete[]


## Refs

- [1] [Linux 定位多线程内存越界问题实践总结 {% include relref_cnblogs.html %}](https://www.cnblogs.com/djinmusic/archive/2013/02/04/2891753.html)
- [2] [Linux Detect c/c++ memory overflow {% include relref_github.html %}](https://matrix207.github.io/2016/01/03/detect-cc-memory-overflow/)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-30-win-memory-dump.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/djinmusic/archive/2013/02/04/2891753.html]({% include relrefx.html url="/backup/2021-04-30-win-memory-dump.md/www.cnblogs.com/59d6c661.html" %})
- [https://matrix207.github.io/2016/01/03/detect-cc-memory-overflow/]({% include relrefx.html url="/backup/2021-04-30-win-memory-dump.md/matrix207.github.io/e0bada66.html" %})
