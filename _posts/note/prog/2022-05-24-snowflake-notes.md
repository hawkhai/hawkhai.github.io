---
layout: post
title: "编程与调试 C++ -- 一些奇奇怪怪的编程知识"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## ssdeep、tlsh、vhash、mmdthash

* 准确率 ACC
* 召回率 REC
* 精确率 PRE

mmdthash
ssdeep
vhash
tlsh


## quic 协议

Quic 全称 quick udp internet connection，“快速 UDP 互联网连接”，（和英文 quick 谐音，简称“快”）是由 google 提出的使用 udp 进行多路并发传输的协议。
一种基于 UDP 的传输协议，用于提升网络加载速度，在弱网环境下表现较好。
Quic 相比现在广泛应用的 http2+tcp+tls 协议有如下优势：

* 减少了 TCP 三次握手及 TLS 握手时间。
* 改进的拥塞控制。
* 避免队头阻塞的多路复用。
* 连接迁移。
* 前向冗余纠错。


## 进程注入

进程注入的方法非常之多，很多与 DLL 注入有关，比如注册表（Image File Execution Options）、DLL 劫持、输入法、COM、LSP 劫持（LayerService Provider，与 winsock 有关）

除了 DLL 注入，还有 shellcode 注入，因为 shellcode 更小，所以 shellcode 的使用也更加多样。

2017 年，在黑客大会上 Eugene Kogan 和 Tal Liberman 又分享了更加隐蔽和特别的方法，比如 Process Doppelganging。


## 基于 LSTM 的二进制代码相似性检测


## 逆向某平台分析过程指导

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458434317&idx=1&sn=0a0f3bcee1cdd99c2f2db1a2fd899619&chksm=b18f8b8786f802919884f0682fe9fb38c0971e3e7de732ec11f35cbd994b87fc12c3e758b344&scene=178&cur_album_id=2293635948628279298)
扔到 ida 看导出函数发现是 jni 动态注册没找到 getServerApi() 这个方法，接下来使用 unidbg 进行分析 call_jni_onload 后找到偏移地址 0x12795。

在 ida 中 G 跳转到偏移地址。

查看 sub_4DF0 函数 F5 生成伪代码。


## 逆向角度看 C++ 部分特性

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436558&idx=1&sn=770b20ad3eb60dbb20c83a59f83c8b48&chksm=b18ff34486f87a52514c67a59d4702e7f2ffc59b9a13f8cd4718b7ec28b79c38ae304eb4167c&scene=178&cur_album_id=2293635948628279298)


## 多项式 MBA 原理及其在代码混淆中的应用


## Windows API 调用详解

[note {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436731&idx=1&sn=4859b3f1fb19001e9e81622fa233fbcf&chksm=b18ff4f186f87de7c12b38a3a1febc82f9faa2ad578ee61e80d3fe64bc12b5bd65c92735587f&scene=178&cur_album_id=2293635948628279298)
sysenter
中断门和调用门比较类似，也是一种用来提权的东西。其核心理念在于 Windows 对 intel CPU 的一种利用。

整个调用方式最关键的就是通过 sysenter 从 User 层到达 Kernel 层，可以说前面的都是在给这一步做铺垫。

sysenter 叫做快速系统调用，叫快速是因为之前的系统调用不快，在 Pentium II（奔腾 2 代 CPU）之后才有的 sysenter，在其之前是采用的 KiIntSystemCall 函数来处理的。

```
// 1：设置寄存器
CS = IA32_SYSENTER_CS
SS = IA32_SYSENTER_CS+8
eip = IA32_SYSENTER_EIP
esp = IA32_SYSENTER_ESP

// 2：切换特权级
切换到 0 环特权级，（其实设置了寄存器就是切换了）

// 3：切换 CPU 模式
清楚 eflags 寄存器中的虚拟 8086 模式（VM 标志）

// 4：执行
执行系统例程调用
```

查壳工具
ExeinfoPE

反调试相关：
IsDebuggerPresent
IsProcessorFeaturePresent // 判断处理器相关信息


## Windows 内核-句柄


## 用 Python 去除图片背景：​Rembg 库

Rembg is a tool to remove images background.
<https://github.com/danielgatis/rembg>


## 智能电表安全之通讯分析

{% include image.html url="/assets/images/220524-snowflake-notes/640.png" %}


## 实现 DebugPort 清零

<https://bbs.pediy.com/thread-271460.htm>
DebugPort 是用于调试的一个端口，如果把这个端口清零，常规手段则无法调试我们的进程。


## 模拟 windwos 系统调用例子，重写 writeprocessmemory 和 readprocessmemory

分别以 int21 和 syscall 两种调用方式实现 代码如下
<https://bbs.pediy.com/thread-271471.htm>
```cpp
#include "stdafx.h"
#include <Windows.h>

// 读进程内存（中断门调用）
BOOL WINAPI HbgReadProcessMemory_INT(
                                HANDLE hProcess,
                                LPCVOID lpBaseAddress,
                                LPVOID lpBuffer,
                                DWORD nSize,
                                LPDWORD lpNumberOfBytesRead)
{
    LONG NtStatus;
    __asm
    {
        // 直接模拟 KiIntSystemCall
        lea edx,hProcess; // 要求 edx 存储最后入栈的参数
        mov eax, 0xBA;
        int 0x2E;
        mov NtStatus, eax;
    }
    if (lpNumberOfBytesRead != NULL)
    {
        *lpNumberOfBytesRead = nSize;
    }
    // 错误检查
    if (NtStatus < 0)
    {
        return FALSE;
    }
    return TRUE;
}

// 读进程内存（快速调用）
BOOL WINAPI HbgReadProcessMemory_FAST(
                                HANDLE hProcess,
                                LPCVOID lpBaseAddress,
                                LPVOID lpBuffer,
                                DWORD nSize,
                                LPDWORD lpNumberOfBytesRead)
{

    LONG NtStatus;
    /*
    __asm
    {
        // 模拟 ReadProcessMemory
        lea eax,nSize;
        push eax;
        push nSize;
        push lpBuffer;
        push lpBaseAddress;
        push hProcess;
        sub esp, 0x04; // 模拟 ReadProcessMemory 里的 CALL NtReadVirtualMemory
        // 模拟 NtReadVirtualMemory
        mov eax, 0xBA;
        push NtReadVirtualMemoryReturn; // 模拟 NtReadVirtualMemory 函数里的 CALL [0x7FFE0300]
        // 模拟 KiFastSystemCall
        mov edx, esp;
        _emit 0x0F; // sysenter
        _emit 0x34;
NtReadVirtualMemoryReturn:
        add esp, 0x18; // 模拟 NtReadVirtualMemory 返回到 ReadProcessMemory 时的 RETN 0x14
        mov NtStatus, eax;
    }
    if (lpNumberOfBytesRead != NULL)
    {
        *lpNumberOfBytesRead = nSize;
    }
    */
    __asm
    {
        lea eax,nSize;
        push eax;
        push nSize;
        push lpBuffer;
        push lpBaseAddress;
        push hProcess;
        sub esp, 0x04; // 模拟 ReadProcessMemory 里的 CALL NtReadVirtualMemory
        // 模拟 NtReadVirtualMemory
        mov eax, 0xBA;
        mov edx, 0X7FFE0300 // 不能直接调用内核，间接 call 函数地址来实现
        CALL DWORD PTR[EDX]
        add esp, 0x18;
        mov NtStatus, eax;
    }
    // 错误检查
    if (NtStatus < 0)
    {
        return FALSE;
    }
    return TRUE;
}

// 写进程内存（中断门调用）
BOOL WINAPI HbgWriteProcessMemory_INT(
                                HANDLE hProcess,
                                LPCVOID lpBaseAddress,
                                LPVOID lpBuffer,
                                DWORD nSize,
                                LPDWORD lpNumberOfBytesWritten)
{
    LONG NtStatus;
    __asm
    {
        lea edx, hProcess;
        mov eax, 0x115;
        int 0x2E;
        mov NtStatus, eax;
    }
    if (lpNumberOfBytesWritten != NULL)
    {
        *lpNumberOfBytesWritten = nSize;
    }
    // 错误检查
    if (NtStatus < 0)
    {
        return FALSE;
    }
    return TRUE;
}

// 写进程内存（快速调用）
BOOL WINAPI HbgWriteProcessMemory_FAST(
                                HANDLE hProcess,
                                LPCVOID lpBaseAddress,
                                LPVOID lpBuffer,
                                DWORD nSize,
                                LPDWORD lpNumberOfBytesWritten)
{
    LONG NtStatus;
    __asm
    {
        // 模拟 WriteProcessMemory
        lea eax,nSize;
        push eax;
        push nSize;
        push lpBuffer;
        push lpBaseAddress;
        push hProcess;
        sub esp, 0x04; // 模拟 WriteProcessMemory 里的 CALL NtWriteVirtualMemory
        // 模拟 NtWriteVirtualMemory
        mov eax, 0x115;
/*
push NtWriteVirtualMemoryReturn; // 模拟 NtWriteVirtualMemory 函数里的 CALL [0x7FFE0300]
        // 模拟 KiFastSystemCall
        mov edx, esp;
        _emit 0x0F; // sysenter
        _emit 0x34;
NtWriteVirtualMemoryReturn:
*/
        mov edx, 0X7FFE0300 // 不能直接调用内核，间接 call 函数地址来实现
            CALL DWORD PTR[EDX]
        add esp, 0x18; // 模拟 NtWriteVirtualMemory 返回到 WriteProcessMemory 时的 RETN 0x14
        mov NtStatus, eax;
    }
    if (lpNumberOfBytesWritten != NULL)
    {
        *lpNumberOfBytesWritten = nSize;
    }
    // 错误检查
    if (NtStatus < 0)
    {
        return FALSE;
    }
    return TRUE;
}

void __declspec(naked) MyReadMem(HANDLE hProcess,
                                LPVOID addr,
                                LPVOID buffer,
                                DWORD len,
                                LPDWORD lpNumberOfBytesWritten)
{
    _asm
    {
        mov   eax, 0BAh
        mov   edx, 7FFE0300h
        call  dword ptr[edx]

        ret 0x14
    }
}

BOOL WINAPI HbgReadProcessMemory_FAST2(
                                HANDLE hProcess,
                                LPCVOID lpBaseAddress,
                                LPVOID lpBuffer,
                                DWORD nSize,
                                LPDWORD lpNumberOfBytesRead)
{

    LONG NtStatus;

    __asm
    {
        lea eax, nSize;
        push eax;
        push nSize;
        push lpBuffer;
        push lpBaseAddress;
        push hProcess;
        call MyReadMem
    }
    // 错误检查
    if (NtStatus < 0)
    {
        return FALSE;
    }
    return TRUE;
}
```


## 反射式 DLL 注入实现

反射式 DLL 注入实现（ManualMap，手动解析 PE 并映射到目标进程再运行）

一般而言要注入 DLL 到一个目标进程最简单的方法 就是先获取 DLL 文件路径，然后在目标进程分配内存空间将路径写入到目标进程，写入到目标进程后再调用 CreateRemoteThread()/NtCreateThread()/RtlCreateUserThread() 函数来运行 LoadLibraryA/W 函数调用自己的 DLL，这种方法的缺陷也很明显那就是容易被游戏检测到，很容易被游戏拦截，比如 CSGO 最新版就已经有这个限制了。

想要突破 CSGO 的限制注入 DLL 进去，我们可以采用反射式注入的方法（也可以先恢复 CSGOhook 的 api 进行远程线程注入），那么什么是反射式注入呢？又有什么有点呢？
反射式 dll 注入与常规 dll 注入类似，而不同的地方在于反射式 dll 注入技术自己实现了一个 reflective loader() 函数来代替 LoadLibaryA() 函数去加载 dll，示意图如下图所示。蓝色的线表示与用常规 dll 注入相同的步骤，红框中的是 reflective loader() 函数行为，也是下面重点描述的地方。

Reflective loader 实现思路如下：

1. 获得被注入进程未解析的 dll 的基地址。
2. 获得必要的 dll 句柄和函数为修复导入表做准备。
3. 分配一块新内存去取解析 dll，并把 pe 头复制到新内存中和将各节复制到新内存中。
4. 修复导入表和重定向表。
5. 执行 DllMain() 函数。

{% include image.html url="/assets/images/220524-snowflake-notes/640injet.png" %}

<https://bbs.pediy.com/thread-272569.htm>
<https://github.com/MrXiao7/DllInjector>
<https://github.com/Kerrbty/RemoteLoadDll>


### API Hook 的几种实现

[API Hook 的几种实现 {% include relref_cnblogs.html %}](https://www.cnblogs.com/rogeryu/archive/2009/06/04/1496538.html)
1. 改写函数的首地址。
2. 改写导入表
3. 改写虚函数表。


## Typora 解密之跳动的二进制

Typora 是一款由 Abner Lee 开发的轻量级 Markdown 编辑器，与其他 Markdown 编辑器不同的是，Typora 没有采用源代码和预览双栏显示的方式，而是采用所见即所得的编辑方式，实现了即时预览的功能，但也可切换至源代码编辑模式。

* 使用 FindCrypt3 插件 ，搜索一下算法常量吧。

**内存破解**
简单说几种思路，由于 main.node 是后加载的模块，所以内存破解有些难度。

* 调试器加载 ：参照上述手段，在模块加载通知中断下，定位到解密函数下断，修改内存中的 JS 代码
* 导出表 HOOK：参考病毒木马使用的进程替换（傀儡进程）技术，创建进程后挂起，由于 main.node 中的 node api 是使用框架中的导出 api，所以可以替换导出函数为自己的函数，在调用时进行参数判断，如果为 JS 代码，则修改
* DLL 劫持：替换 main.node，由自己加载真正的 main.node 并调用，调用时，定位到解密函数并 hook，等待 JS 代码并修改
* PE 代码注入 ：修改框架的 PE 文件，并加载自己的 DLL，加载后进行导出表 hook

可能遇到的问题：对 main.node 或者框架进行完整性校验，更加强大的反调试手段。

[note](https://bbs.pediy.com/thread-272618.htm)

[start66. {% include relref_weixin.html %}](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5NTc2MDYxMw==&action=getalbum&album_id=2293635948628279298&scene=173&from_msgid=2458436731&from_itemidx=1&count=3&nolastread=1)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-24-snowflake-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458434317&idx=1&sn=0a0f3bcee1cdd99c2f2db1a2fd899619&chksm=b18f8b8786f802919884f0682fe9fb38c0971e3e7de732ec11f35cbd994b87fc12c3e758b344&scene=178&cur_album_id=2293635948628279298]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/6eb26110.html" %})
- [https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436558&idx=1&sn=770b20ad3eb60dbb20c83a59f83c8b48&chksm=b18ff34486f87a52514c67a59d4702e7f2ffc59b9a13f8cd4718b7ec28b79c38ae304eb4167c&scene=178&cur_album_id=2293635948628279298]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/0075049f.html" %})
- [https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458436731&idx=1&sn=4859b3f1fb19001e9e81622fa233fbcf&chksm=b18ff4f186f87de7c12b38a3a1febc82f9faa2ad578ee61e80d3fe64bc12b5bd65c92735587f&scene=178&cur_album_id=2293635948628279298]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/5a67a6fe.html" %})
- [https://github.com/danielgatis/rembg]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/github.com/156be90b.html" %})
- [https://bbs.pediy.com/thread-271460.htm]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/bbs.pediy.com/f725448d.htm" %})
- [https://bbs.pediy.com/thread-271471.htm]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/bbs.pediy.com/7c8cfe91.htm" %})
- [https://bbs.pediy.com/thread-272569.htm]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/bbs.pediy.com/09b64a65.htm" %})
- [https://github.com/MrXiao7/DllInjector]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/github.com/8c750d26.html" %})
- [https://github.com/Kerrbty/RemoteLoadDll]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/github.com/ca0eeb9f.html" %})
- [https://www.cnblogs.com/rogeryu/archive/2009/06/04/1496538.html]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/www.cnblogs.com/316f18af.html" %})
- [https://bbs.pediy.com/thread-272618.htm]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/bbs.pediy.com/03692cc5.htm" %})
- [https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5NTc2MDYxMw==&action=getalbum&album_id=2293635948628279298&scene=173&from_msgid=2458436731&from_itemidx=1&count=3&nolastread=1]({% include relrefx.html url="/backup/2022-05-24-snowflake-notes.md/mp.weixin.qq.com/78332679.html" %})
