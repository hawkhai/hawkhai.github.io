---
layout: post
title: "调试 Memory -- Windows Windbg Review 一些简单使用命令"
author:
location: "珠海"
categories: ["调试"]
tags: ["调试", "Memory"]
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

利用 windbg 分析崩溃、句柄泄漏、死锁、CPU 高、内存泄漏
Windbg 的一些简单使用命令


## 崩溃

1. 输入 `.ecxr; kbn` 得到崩溃的堆栈
    * 其中源代码如下
2. 查看堆栈和源代码，发现第 0 帧导致崩溃，代码也是本地代码
    * 输入 `.frame 0`, 切到第 0 帧如下
3. 输入 `dv` 查看当前帧的一些变量信息
    * 发现变量 p=0x00000000

{% include image.html url="/assets/images/210523-win-windbg-review/e2f4d76605a000c8ad1ba979af2e3371.png" relocate="1.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/2c4d087da38cbdc40af1bd34ca7cdec4.png" relocate="3.1" %}


## 句柄泄漏

1. 启动进程
2. 用 windbg 附加到进程
3. `!htrace -enable` 命令开启句柄检测
4. `!htrace –snapshot`
5. 运行一段时间后
6. `!htrace –diff`
    * 得到如下信息，标红函数创建了 event
7. 输入 `lsa handleLeak!ThreadProc1+0x00000037`
    * 这样就可以看出代码中在不停 CreateEvent。

{% include image.html url="/assets/images/210523-win-windbg-review/8bd67a36208ba6df2a1aaad62de8ccac.png" relocate="6.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/91acedf8b730c3c07ab8eea0f025eeaf.png" relocate="7.1" %}

*补充：*
可以在 windbg 调式中，输入 `!handle` 可以得到当前堆栈的一些句柄信息，可以看出这个堆栈 event 非常多。

{% include image.html url="/assets/images/210523-win-windbg-review/6c0d22d7a8aa92e42b4fe3e4590621b2.png" %}


## 死锁

1. 启动进程
2. Windbg 附加进程
3. 输入 `~*kv`，输出所有线程
4. 输入 `!find stackntdll!RtlEnterCriticalSection`，查找哪些线程在等待锁
    * 或者看代码某一函数没执行，对比 windbg 中的线程，找到线程 id 分析
    * 图 1 是源代码，图 2 是执行结果, ThreadProc1 函数中的 `ThreadProc1 lock g_mutex2;` 没发生，怀疑是否死锁了
5. windbg 中线程信息如下，发现 ThreadProc1 在等某一把锁
    * 第三帧是本地代码对比源代码发现在等锁 g_mutex2;
    * 第二帧是系统函数在等待锁，锁地址为 00bf7140
6. 输入 `!cs 00bf7140`，查看这把锁信息
    * 发现锁的占有者是 0x00002cc4
7. 输入 `~~[0x00002cc4]`，发现对应是 3 号线程
8. 切到 3 号线程，并输出堆栈
    * 发现代码 27 号，也在等一把锁，锁地址 00bf7158
9. 同理输出锁信息
10. 发现锁占有者 0x00004c80，切到线程 0x00004c80，并输出堆栈
    * 发现是刚才的 2 号线程

{% include image.html url="/assets/images/210523-win-windbg-review/95066ec6534b8aed6f2b5b26ff2bf7d5.png" relocate="4.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/0ce1de20e20ef1a7228fca7f2be0c620.png" relocate="4.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/ccdedd80fb7d1c5719dfdc277ec8bae9.png" relocate="5.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/0c33c4e9cbc81354721b64916c680aef.png" relocate="6.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/15a8932417aad29cc70c5a7e591d5f9e.png" relocate="7.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/28088bd5b4dc48fe5f8fa8ab8affc244.png" relocate="8.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/f74675b67078d79f0f5cbb5102fff19e.png" relocate="9.1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/05b045f4a4107904ec53b5c34fcac67d.png" relocate="10.1" %}

至此分析完成 2 号线程和 3 号线程发生死锁。


## CPU 高

1. 启动进程
2. Windbg 附加进程
3. 输入 `!runaway`
4. 发现 2 号线程 cpu 最高，切到 2 号线程，并输出堆栈
5. 可以得到是 `cpuhigh!ThreadProc1+0x35`

{% include image.html url="/assets/images/210523-win-windbg-review/fe452b8a25808655635ad74b9b64705a.png" relocate="4" %}
{% include image.html url="/assets/images/210523-win-windbg-review/4cbd234c01d9a195e7c4c6fb26150521.png" relocate="5" %}


## 内存泄漏


### windbg 手动分析

1. 设置 gflags.exe, 这工具和 windbg 在同一目录
2. windbg 附加到进程，输入 `!heap –s`
3. 程序运行一段时间之后，再次输入 `!heap–s`
    * 发现 00970000 这个堆有增加，其他无变化
4. 输入 `!heap -stat -h00970000`，查看这个堆状态
    * 发现这个堆的内存主要是被大小为 0x224 的块占用
5. 输入 `!heap -flt s 224`，查看 224 这些块被谁在使用
6. 输入 `!heap -p -a 00971d20`，查看堆栈
7. 已经得到堆栈，本地有源代码，还可以查看代码，
    * 输入 `lsa memoryleak!ThreadProc1+0x00000048`

{% include image.html url="/assets/images/210523-win-windbg-review/811218329c0e37de0583e9c24cd290e2.png" relocate="1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/54a54b7166a037fe28ec642849e509f4.png" relocate="1" %}
{% include image.html url="/assets/images/210523-win-windbg-review/c8f19f0bae8eb708e7ab0f188b4ab0ff.png" relocate="2" %}
{% include image.html url="/assets/images/210523-win-windbg-review/9d5a6257a9ffd484d8f145e6079f913b.png" relocate="3" %}
{% include image.html url="/assets/images/210523-win-windbg-review/c664203f9367716bdf221aee5efdb907.png" relocate="4" %}
{% include image.html url="/assets/images/210523-win-windbg-review/8aa966a96bd46b5c7cfa20f94e6ffb27.png" relocate="5" %}
{% include image.html url="/assets/images/210523-win-windbg-review/3dcf3505287e97de2634edd115903ba1.png" relocate="6" %}
{% include image.html url="/assets/images/210523-win-windbg-review/f39b852524278a8b6a2d72f30a75852c.png" relocate="7" %}


### 利用 umdh 分析

1. 同 5.1 设置 gflags 配置
2. 开启命令窗口 cmd, 输入要定位内存泄露的程序 `gflags.exe /i memoryleak.exe +ust`
3. 设置程序的符号表路径
  ```
SET _NT_SYMBOL_PATH=SRV*C:\Symbols*http://msdl.microsoft.com/download/symbols;F:\windbgtest\Debug
```
4. 启动 memoryleak.exe, 利用 umdh 创建第一次 heap 快照
    * 输入 `umdh-pn:memoryleak.exe -f:memory1.log`
5. 运行一段时间后，再次输入快照，`umdh -pn:memoryleak.exe -f:memory2.log`
6. 分析前后 2 次快照的差异 `umdh -dmemory1.log memory2.log -f:memoryleak.log`
    * 会在当前路径下面生成 memoryleak.log，打开分析
7. 定位到代码，需要具体分析逻辑，查看是否真的泄漏，还是还没来得及释放。

{% include image.html url="/assets/images/210523-win-windbg-review/b3cc5d7ec912facfe1697f6afcdf5719.png" relocate="7" %}


### AppVerifier

WinDbg 的 !heap 命令非常强大，结合 AppVerifier 可以对堆 (heap) 内存进行详细的跟踪和分析

{% include image.html url="/assets/images/210523-win-windbg-review/1ba6703801bca02447eaabe70bc28c33.png" %}


## Refs

利用 windbg 分析崩溃、句柄泄漏、死锁、CPU 高、内存泄漏
Windbg 的一些简单使用命令

* https://www.pianshen.com/article/72521138890/
* https://blog.csdn.net/zqw_4181/article/details/79162309

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-23-win-windbg-review.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://msdl.microsoft.com/download/symbols]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/msdl.microsoft.com/9dd253a8.html" %})
- [https://www.pianshen.com/article/72521138890/]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/www.pianshen.com/00174843.html" %})
- [https://blog.csdn.net/zqw_4181/article/details/79162309]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/blog.csdn.net/b4dbb7b3.html" %})
