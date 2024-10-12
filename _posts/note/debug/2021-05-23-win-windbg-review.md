---
layout: post
title: "编程与调试 Memory -- Windows Windbg Review 一些简单使用命令"
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

利用 windbg 分析崩溃、句柄泄漏、死锁、CPU 高、内存泄漏
Windbg 的一些简单使用命令


## 崩溃 自动关联 WinDbg 并调试

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
```
Debugger "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe" -p %ld -e %ld -g
Auto 1
```

* !analyze -v: 获取详细的崩溃分析。
* k: 查看调用堆栈。
* lm: 列出加载的模块。


## 查看地址附近代码

[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/zengkefu/p/6938071.html)
* u 命令（反汇编）
    * 类型 u mymodule.dll!0xaddr 查看汇编程序代码

uf ICSF!SfDirectoryControl | 可以查看整个函数的汇编代码
u ICSF!SfDirectoryControl ICSF!SfDirectoryControl+0x30 | 可以看到 30 个字节的汇编指令
ub ICSF!SfDirectoryControl L30 | 可以查看 SfDirectoryControl 之上的 30 字节的汇编指令

* ln 命令（查找就近的符号）
    * 类型 ln mymodule.dll!0xaddr 查看该地址附近的符号

```
CONTEXT:  (.ecxr)
eax=0041f8fc ebx=013b0000 ecx=0041f924 edx=013b0000 esi=02ea1b04 edi=03004624
eip=013e4a38 esp=0041f6d4 ebp=fffffde0 iopl=0         nv up ei ng nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010282
fastapp!KzPath::GetModuleFolder+0x38:
013e4a38 89bde0fdffff    mov     dword ptr [ebp-220h],edi ss:002b:fffffbc0=????????
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 013e4a38 (fastapp!KzPath::GetModuleFolder+0x00000038)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000001
   Parameter[1]: fffffbc0
Attempt to write to address fffffbc0
```

```
0:000> u 00274a38
fastapp!KzPath::GetModuleFolder+0x38 [D:\PCGMR_BUILD\Cim\CiSrc\zapp\zapp\include\framework\KzPath.cpp @ 52]:
00274a38 89bde0fdffff    mov     dword ptr [ebp-220h],edi
00274a3e c785dcfdffff00000000 mov dword ptr [ebp-224h],0
00274a48 c745fc01000000  mov     dword ptr [ebp-4],1
00274a4f e89cbefeff      call    fastapp!ATL::CAtlStringMgr::GetInstance (002608f0)
00274a54 8bc8            mov     ecx,eax
00274a56 85c9            test    ecx,ecx
00274a58 0f84b9000000    je      fastapp!KzPath::GetModuleFolder+0x117 (00274b17)
00274a5e 8b01            mov     eax,dword ptr [ecx]
0:000> ln 00274a38
D:\PCGMR_BUILD\Cim\CiSrc\zapp\zapp\include\framework\KzPath.cpp(52)+0x38
(00274a00)   fastapp!KzPath::GetModuleFolder+0x38   |  (00274b30)   fastapp!KzPath::LegalizePath
```


## 崩溃

1. 输入 `.ecxr; kbn` 得到崩溃的堆栈
    * 其中源代码如下
2. 查看堆栈和源代码，发现第 0 帧导致崩溃，代码也是本地代码
    * 输入 `.frame 0` ，切到第 0 帧如下
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
3. 输入 `~*kv` ，输出所有线程
4. 输入 `!find stackntdll!RtlEnterCriticalSection` ，查找哪些线程在等待锁
    * 或者看代码某一函数没执行，对比 windbg 中的线程，找到线程 id 分析
    * 图 1 是源代码，图 2 是执行结果, ThreadProc1 函数中的 `ThreadProc1 lock g_mutex2;` 没发生，怀疑是否死锁了
5. windbg 中线程信息如下，发现 ThreadProc1 在等某一把锁
    * 第三帧是本地代码对比源代码发现在等锁 g_mutex2;
    * 第二帧是系统函数在等待锁，锁地址为 00bf7140
6. 输入 `!cs 00bf7140` ，查看这把锁信息
    * 发现锁的占有者是 0x00002cc4
7. 输入 `~~[0x00002cc4]` ，发现对应是 3 号线程
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
4. 输入 `!heap -stat -h00970000` ，查看这个堆状态
    * 发现这个堆的内存主要是被大小为 0x224 的块占用
5. 输入 `!heap -flt s 224` ，查看 224 这些块被谁在使用
6. 输入 `!heap -p -a 00971d20` ，查看堆栈
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
5. 运行一段时间后，再次输入快照， `umdh -pn:memoryleak.exe -f:memory2.log`
6. 分析前后 2 次快照的差异 `umdh -dmemory1.log memory2.log -f:memoryleak.log`
    * 会在当前路径下面生成 memoryleak.log，打开分析
7. 定位到代码，需要具体分析逻辑，查看是否真的泄漏，还是还没来得及释放。

{% include image.html url="/assets/images/210523-win-windbg-review/b3cc5d7ec912facfe1697f6afcdf5719.png" relocate="7" %}


### AppVerifier

WinDbg 的 !heap 命令非常强大，结合 AppVerifier 可以对堆 (heap) 内存进行详细的跟踪和分析

{% include image.html url="/assets/images/210523-win-windbg-review/1ba6703801bca02447eaabe70bc28c33.png" %}


## [windbg.txt {% include relref_github.html %}](https://github.com/mk-z/windbg/blob/master/windbg.txt)

* [WinDbg 入门（用户模式）](https://docs.microsoft.com/zh-cn/windows-hardware/drivers/debugger/getting-started-with-windbg)


### 栈大小

用户态栈默认大小为 1MB，默认内核态栈大小为：
在 x86 系统中，内核栈的初始大小是 12KB，在 X64 CPU（intel 64 和 AMD 64）的系统中，内核态栈的初始大小是 24KB，在安腾（Itanium）处理器的系统中，内核态栈的大小是 32KB。


### windbg 观察栈

* kb：显示栈上的前三个参数（不一定是参数，仅仅是三个固定位置的值）


### 内存信息查看

[Windbg 内存命令 《第四篇》 {% include relref_cnblogs.html %}](https://www.cnblogs.com/kissdodog/p/3730598.html)
```
!address
!address -summary
!address -Stack # 用于线程堆栈的内存。
```


### 并发堆栈

并发堆栈，首先我们需要知道有多少线程。
* `~*` ：查看所有线程
* `~.kp` ：查看当前线程调用堆栈
* `~*kp` ：查看所有线程调用堆栈


## Refs

利用 windbg 分析崩溃、句柄泄漏、死锁、CPU 高、内存泄漏
Windbg 的一些简单使用命令

* <https://www.pianshen.com/article/72521138890/>
* <https://blog.csdn.net/zqw_4181/article/details/79162309>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-23-win-windbg-review.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/zengkefu/p/6938071.html]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/www.cnblogs.com/ea2c61bc.html" %})
- [http://msdl.microsoft.com/download/symbols]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/msdl.microsoft.com/9dd253a8.html" %})
- [https://github.com/mk-z/windbg/blob/master/windbg.txt]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/github.com/dabc29f3.html" %})
- [https://docs.microsoft.com/zh-cn/windows-hardware/drivers/debugger/getting-started-with-windbg]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/docs.microsoft.com/02c5b3b3.html" %})
- [https://www.cnblogs.com/kissdodog/p/3730598.html]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/www.cnblogs.com/41d30370.html" %})
- [https://www.pianshen.com/article/72521138890/]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/www.pianshen.com/00174843.html" %})
- [https://blog.csdn.net/zqw_4181/article/details/79162309]({% include relrefx.html url="/backup/2021-05-23-win-windbg-review.md/blog.csdn.net/b4dbb7b3.html" %})
