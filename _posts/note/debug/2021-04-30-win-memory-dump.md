---
layout: post
title: "编程与调试 Memory -- Windows Windbg dump 内存崩溃泄漏问题（debug 意义）"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory"]
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

多线程中的内存问题，一直被认为是噩梦般的存在，几乎只有世外高手、大罗神仙才能解决。
少部分情况因为访存地址合法，会对数据造成破坏（悬垂指针或者野指针），一般会在运行一段时间后才因为异常退出。
这时候触发错误导致进程退出的代码位置往往不是“案发的第一现场”，给调试工作带来了更大的难度。

**为了更好的处理内存问题，我们要尽力保证 Debug 版本（更多的运行检查）和 x64 版本（页堆才能顺利开启）都能顺利编译出来，另外编译器也要及时升级。**

debug 版本 和 Relase 版本。debug 本质上插入了 代码。
gflags 在没有修改代码的 条件下，只能做有限的 内存边界检查，插桩之类。
所以保住 debug 版本，对一个工程来说，很重要。

**Win32 堆和 CRT 堆的常用字节模式和它们的含义** @156@liebao

字节模式 | 堆管理器 | 用途 | 长度
---- | ---- | ---- | ----
0xFEEEFEEE  | Win32 堆 | 填充空闲块的数据区        | 块数据区大小
0xBAADF00D  | Win32 堆 | 填充新分配块的数据区      | 块数据区大小
0xAB        | Win32 堆 | 填充在堆块的用户数据之后，用于检测堆溢出 | 不确定
0xFD        | CRT 调试堆 | 填充用户数据区前后的隔离区（no-man’s land） | 各 4 个字节
0xDD        | CRT 调试堆 | 填充释放的堆块（dead land） | 整个堆块大小
0xCD        | CRT 调试堆 | 填充新分配的堆块（clean land） | 用户数据区大小


## 内存管理

1. 内存泄漏
    * 简单的潜在堆内存丢失和缓冲区覆盖
    * 来自资源错误管理的潜在堆内存丢失
2. 错误分配，包括大量增加 free() 释放的内存和未初始化的引用
    * 未初始化的指针
    * 两个错误的内存释放
3. 悬空指针
    * 悬空指针
4. 数组边界违规
    * 数组边界违规


## 栈的调试支持


### 基于 Cookie 的安全检查

* 在栈帧的起始处存放一个整数 —— Cookie
* 函数返回时检查 Cookie 的完好性，如果损坏则报告
* Visual Studio .Net 2002 开始支持，Windows Server 2003 首先采用
* 编译时，指定 /GS 选项，默认启用
* 发布版本和调试版本都可以使用
* 编译时会判断是否有必要针对当前函数使用 Cookie


### 编译器的运行期检查

* Run-Time Error Check (RTC)
* 栈指针被破坏（Stack pointer corruption）
* 局部缓冲区（数组）越界（Overruns）
* 栈被破坏（Stack corruption）
* 依赖未初始化过的局部变量
* 因为赋值给较短的变量导致数据丢失
* 观察栈桢，布局，Cookie


## 堆的调试支持

* 堆尾检查（Heap Tail Checking），简称 HTC
* 释放检查（Heap Free Checking），简称 HFC
* 参数检查，对传递给堆管理器的参数进行更多的检查
* 调用时验证（Heap Validation on Call），简称 HVC
* 堆块标记（Heap Tagging）
* 用户态栈回溯（User mode Stack Trace），简称 UST


### 页堆

* 专门用于调试，简称 DPH，Windows 2000 引入
* 大量使用内存页 —— 为了调试，不惜代价
* 对调试堆溢出特别有效，实时中断到调试器

#### 页堆的堆块

《软件调试》图 23-6 P680
* 每个堆块至少占用两个内存页
* 有专门的管理信息区，堆块指针不容易被破坏
    * Linux 下可以使用 valgrind

#### 验证器

* 下载安装
* 包含在 SDK 中
* 针对可执行文件名 .exe
* 不关心路径

{% include image.html url="/assets/images/210430-win-memory-dump/20210523141256.png" %}


## 一些看法

个人一些看法，当一个工程又大、时间又悠久的时候。

1. 尽量 MD/MT 采用 MT，这样一个模块一个堆，谁崩了算谁的，一般情况下，至少能缩小问题定位范围。
    * 也许会说 MD 节省空间，但是节省的几百 K，感觉意义并不大，一张小图片就几百 K 了。
2. 尽量 MD/MT 采用 MT，这样每个模块可以单独升级编译器（比如 vs2005 升级到 vs2019），否则存在多个模块关联，要同时升级，增加了难度。
3. 多线程堆问题是最麻烦的，崩溃的时候第一案发现场已经过了，取到的 dump 并不包含问题代码位置。
    * 第一步是问题重现。只要是可以稳定重现的 bug 都是很好解决的。
    * 工程开发尽量保证 Debug 模式（这里体现了 CMake 的优越性），大部分堆内存问题都会直接报错，“屯屯屯屯屯”，“烫烫烫烫烫”。
        * VisualStudio Debug 版本 /GZ 可以帮助捕获内存错误。<span imgid="DebugGZ" />
        * Debug 版本加入断言，检查非法的函数参数，未定义行为的意外使用，其他程序员的错误的假设以及不可能发生的情况仍然不知何故出现了所造成的 bugs。
    * 开启完全页堆，**gflags.exe**，争取重现问题。当一个程序的内存大于 1G，这个方法也不行了，一开启，问题代码还没跑到，程序就内存不足崩溃了。
    * 最后的方法就是 git 里面去扒灰源代码，二分法 + code review，最后的倔强。-_-
    * 物归初始 此境初识。关键还是要提高程序员的编码质量。
        * 编写出来的代码可以同时用 cppcheck 等代码静态检测工具检测出一些野指针、无效变量等低级错误。

{% include image.html url="/assets/images/210430-win-memory-dump/20210502140538.png" relocate="DebugGZ" caption="Debug 版本，使用了未初始化指针，报错，Release 版本不报错。" %}
{% include image.html url="/assets/images/210430-win-memory-dump/20210502140610.png" relocate="DebugGZ" caption="Debug 版本，堆越界写入，回收的时候直接报错。" %}
{% include image.html url="/assets/images/210430-win-memory-dump/20210502140622.png" relocate="DebugGZ" caption="Release 版本，堆越界写入，最后报错。" %}

{% include image.html url="/assets/images/210430-win-memory-dump/20210511121604.png" relocate="DebugGZ" caption="Debug 版本，vector 越界断言。" %}
{% include image.html url="/assets/images/210430-win-memory-dump/20210511121624.png" relocate="DebugGZ" caption="Debug 版本，vector 越界断言，直接定位到代码行。" %}


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


## 内核崩溃定位

```
!chksym xxx
.reload
!irql
```

{% include image.html url="/assets/images/210430-win-memory-dump/2342141.png" %}

{% include image.html url="/assets/images/210430-win-memory-dump/kzzz1.png" caption="verifier" %}
{% include image.html url="/assets/images/210430-win-memory-dump/kzzz2.png" %}


## 句柄泄漏定位

```
!htrace -enable
!htrace -diff
!handle
```

{% include image.html url="/assets/images/210430-win-memory-dump/kzzz3.png" %}


## 堆泄漏定位

`gflags.exe /i xxx.exe +ust` ，**开启用户层栈记录**：

{% include image.html url="/assets/images/210430-win-memory-dump/a1.png" %}

```
KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\testcmd.exe
GlobalFlag=0x00001000
```

`!heap -s` 列举当前栈信息：

{% include image.html url="/assets/images/210430-win-memory-dump/a2.png" %}

`!heap -s` 再列举一次做对比，看 Commit 变化的就是泄漏的：

{% include image.html url="/assets/images/210430-win-memory-dump/a3.png" %}

`!heap -stat -h` 堆地址，看堆增长占比：

{% include image.html url="/assets/images/210430-win-memory-dump/a4.png" %}

`!heap -flt s` 看指定大小的堆：

{% include image.html url="/assets/images/210430-win-memory-dump/a5.png" %}

`db` 看堆结构数据：

{% include image.html url="/assets/images/210430-win-memory-dump/a6.png" %}

`!heap -p -a` 看泄漏堆所处的线程栈：

{% include image.html url="/assets/images/210430-win-memory-dump/a7.png" %}


## 利用 umdh 快速定位堆泄漏

UMDH 是 Windows debug tools 下的一款命令行工具，它的全名是 User-Mode Dump Heap 这个工具会分析当前进程再堆上分配的内存，并有两种模式：
1. 进程分析模式，这个模式会对进程分配的每一块内存做记录，其中包含分配的内存大小，内存分配地址，内存分配时的函数调用堆栈等。
2. 日子分析模式，该模式会比较几个不同的日志，找出内存增长的地方。

```
gflags.exe /i xxx.exe +ust，开启用户层栈记录
泄漏前：umdh -pn:xxx.exe -f:C:\a.txt
泄漏后：umdh -pn:xxx.exe -f:C:\b.txt
分析增加栈：umdh -d C:\a.txt C:\b.txt >> C:\c.txt
```

{% include image.html url="/assets/images/210430-win-memory-dump/b1.png" %}


## Refs

- [1] [Linux 定位多线程内存越界问题实践总结 {% include relref_cnblogs.html %}](https://www.cnblogs.com/djinmusic/archive/2013/02/04/2891753.html)
- [2] [Linux Detect c/c++ memory overflow {% include relref_github.html %}](https://matrix207.github.io/2016/01/03/detect-cc-memory-overflow/)

- 20200319 [经验分享：taoge & lwj - Windbg 应用与案例分析](http://blog.rdev.kingsoft.net/?p=3359)
  - Windbg 调试技巧 - taoge
  - Windbg 调试与案例分析 - lwj



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-30-win-memory-dump.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/djinmusic/archive/2013/02/04/2891753.html]({% include relrefx.html url="/backup/2021-04-30-win-memory-dump.md/www.cnblogs.com/59d6c661.html" %})
- [https://matrix207.github.io/2016/01/03/detect-cc-memory-overflow/]({% include relrefx.html url="/backup/2021-04-30-win-memory-dump.md/matrix207.github.io/e0bada66.html" %})
