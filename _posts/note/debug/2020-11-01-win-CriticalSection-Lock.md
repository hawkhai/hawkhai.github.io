---
layout: post
title: "调试 -- Windbg 调试临界区（CriticalSection）死锁"
author:
location: "珠海"
categories: ["调试"]
tags: ["编程", "调试", "死锁"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 悲剧的发生

一种非常糟糕的写法：

```cpp
if (m_hThread != NULL) {
    DWORD dwExit = WaitForSingleObject(m_hThread, 100);
    if (dwExit != WAIT_OBJECT_0) {
        TerminateThread(m_hThread, EXIT_SUCCESS);
    }
    CloseHandle(m_hThread);
    m_hThread  = NULL;
    m_dwThread = 0;
}
```

等了一下，线程无法正常退出，然后 TerminateThread，临界区被占用造成死锁，进程还是无法正常退出。
分析 dump，发现一个不存在的线程占用了临界区，悲剧。

卡死死锁问题。一般出现在主线程，否则也很难被发现。

1. 不要在 DllMain 中做的事情。
2. 不要轻易用 TerminateThread / ExitThread / SuspendThread。
    子线程和主线程都使用了一个临界区变量，TerminateThread 结束线程时，不会回收线程的栈！
3. 使用 \_\_try \_\_except 捕获了异常，导致锁未释放。

在 Windows 中使用互斥锁可以有效的避免死锁。
当持有 Mutex 的线程在调用 ReleaseMutex 前意外退出，如 ExitThread 和 TerminateThread。
系统会把 Mutex 分给等待 Mutex 的线程中的一个并返回 Wait_Abandoned，从而避免了死锁。


## Dynamic-Link Library Best Practices

DllMain 在收到 DLL_PROCESS_ATTACH 和 DLL_PROCESS_DETACH 时会进入临界区。
它是使其他线程不能进入临界区从而导致死锁的关键。

<https://docs.microsoft.com/zh-cn/windows/win32/dlls/dynamic-link-library-best-practices>

{% include image.html url="/assets/images/201101-win-criticalsection-lock/fig2.png" %}


## 定位到卡死位置

关键命令：

```shell
!cs -l # 获取更为全面的临界区信息
!handle 000000c4 f # 查看该句柄的信息
!locks # 查看进程中哪些锁处于锁定状态
~*kvn; # 查看所有线程调用堆栈
!cs -o -l
```

```
ntdll_77b20000!ZwWaitForSingleObject+0x15:
00000000`77b3f8e1 83c404          add     esp,4
Minidump doesn't have an exception context
Unable to get exception context, HRESULT 0x80004002
ChildEBP RetAddr  Args to Child
0018b9d8 77b6ebae 0000011c 00000000 00000000 ntdll_77b20000!ZwWaitForSingleObject+0x15
0018ba3c 77b6ea92 00000000 00000000 00000001 ntdll_77b20000!RtlpWaitOnCriticalSection+0x13e
0018ba64 77b56f76 77c220c0 77cec451 00000000 ntdll_77b20000!RtlEnterCriticalSection+0x150
0018ba9c 775c1a32 00000001 00000000 0018bac4 ntdll_77b20000!LdrLockLoaderLock+0xe4
0018bae8 0040ada8 00400000 0018bb30 00000104 KERNELBASE!GetModuleFileNameW+0x75
```

ZwWaitForSingleObject Syntax：

```cpp
NTSYSAPI NTSTATUS ZwWaitForSingleObject(
  HANDLE         Handle,
  BOOLEAN        Alertable,
  PLARGE_INTEGER Timeout
);
```

句柄为：0000011c。查看句柄：`!handle 0x0000011c f`。


## windbg 死锁分析

[link {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/tetpft089bWAV9VxfjCzqA)
资源管理器的等待链分析功能。


### !locks 命令

可以直观的看出 cs 锁的占用情况，拥有者线程。

{% include image.html url="/assets/images/201101-win-criticalsection-lock/20201108194937.jpg" %}


### !cs 命令

除了可以看出被占用的 cs 锁，也能看到未被占用锁的情况。

{% include image.html url="/assets/images/201101-win-criticalsection-lock/20201108195012.jpg" %}


### !handle 命令

可以查看句柄的类型，用于排查非 cs 锁的情况。

{% include image.html url="/assets/images/201101-win-criticalsection-lock/20201108195044.jpg" %}


## Mutex 实战


### C++ 源码

```cpp
#include "stdafx.h"
#include <windows.h>
#include <tchar.h>
#include <process.h>

HANDLE hMutexA = NULL;
HANDLE hMutexB = NULL;

unsigned __stdcall ThreadProc1(void * pArg) {
    WaitForSingleObject(hMutexA, INFINITE);
    Sleep(500);
    WaitForSingleObject(hMutexB, INFINITE);

    printf("+++\n");

    ReleaseMutex(hMutexB);
    ReleaseMutex(hMutexA);

    return 0;
}

unsigned __stdcall ThreadProc2(void * pArg) {
    WaitForSingleObject(hMutexB, INFINITE);
    Sleep(500);
    WaitForSingleObject(hMutexA, INFINITE);

    printf("...\n");

    ReleaseMutex(hMutexA);
    ReleaseMutex(hMutexB);

    return 0;
}

int mainlock()
{
    hMutexA = CreateMutex(NULL, FALSE, TEXT("MutexA"));
    hMutexB = CreateMutex(NULL, FALSE, TEXT("MutexB"));

    // 启动线程
    HANDLE hThread1 = (HANDLE)_beginthreadex(NULL, 0, ThreadProc1, NULL, 0, NULL);
    HANDLE hThread2 = (HANDLE)_beginthreadex(NULL, 0, ThreadProc2, NULL, 0, NULL);

    getchar();

    // 等待线程退出并关闭句柄
    if (hThread1) {
        WaitForSingleObject(hThread1, INFINITE);
        CloseHandle(hThread1);
    }

    if (hThread2) {
        WaitForSingleObject(hThread2, INFINITE);
        CloseHandle(hThread2);
    }

    // 关闭句柄
    if (hMutexA)
        CloseHandle(hMutexA);
    if (hMutexB)
        CloseHandle(hMutexB);

    return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
    mainlock();
    return 0;
}

```


### 等待链

{% include image.html url="/assets/images/201101-win-criticalsection-lock/wtchain.png" %}
{% include image.html url="/assets/images/201101-win-criticalsection-lock/20201109211915.png" %}


### 崩溃分析

```
0:000> .load wow64exts; !sw; ~*kvn;
Switched to Guest (WoW) mode

.  0  Id: 572c.4c78 Suspend: 0 Teb: 00377000 Unfrozen
 # ChildEBP RetAddr  Args to Child
00 0019fcc8 772d88f9 0000010c 00000000 00000000 ntdll_77b80000!NtWaitForSingleObject+0xc (FPO: [3,0,0])
01 0019fd3c 772d8852 0000010c ffffffff 00000000 KERNELBASE!WaitForSingleObjectEx+0x99 (FPO: [SEH])
*** WARNING: Unable to verify checksum for locktest.exe
02 0019fd50 004116a3 0000010c ffffffff 0019ff18 KERNELBASE!WaitForSingleObject+0x12 (FPO: [Non-Fpo])
03 0019fe44 004117c3 00411082 00411082 00376000 locktest!mainlock+0xc3 (FPO: [Non-Fpo]) (CONV: cdecl) [e:\ksource\pythonx\note\locktest\locktest.cpp @ 49]
04 0019ff18 00411d76 00000001 005c1048 005c5a20 locktest!wmain+0x23 (FPO: [Non-Fpo]) (CONV: cdecl) [e:\ksource\pythonx\note\locktest\locktest.cpp @ 70]
05 0019ff68 00411bbd 0019ff80 76e60419 00376000 locktest!__tmainCRTStartup+0x1a6 (FPO: [Non-Fpo]) (CONV: cdecl) [f:\dd\vctools\crt_bld\self_x86\crt\src\crtexe.c @ 594]
06 0019ff70 76e60419 00376000 76e60400 0019ffdc locktest!wmainCRTStartup+0xd (FPO: [Non-Fpo]) (CONV: cdecl) [f:\dd\vctools\crt_bld\self_x86\crt\src\crtexe.c @ 414]
07 0019ff80 77be66ed 00376000 b788a4ad 00000000 kernel32!BaseThreadInitThunk+0x19 (FPO: [Non-Fpo])
08 0019ffdc 77be66bd ffffffff 77c053e8 00000000 ntdll_77b80000!__RtlUserThreadStart+0x2f (FPO: [SEH])
09 0019ffec 00000000 00411082 00376000 00000000 ntdll_77b80000!_RtlUserThreadStart+0x1b (FPO: [Non-Fpo])

   1  Id: 572c.72e4 Suspend: 0 Teb: 00380000 Unfrozen
 # ChildEBP RetAddr  Args to Child
00 00a0fdc4 772d88f9 00000108 00000000 00000000 ntdll_77b80000!NtWaitForSingleObject+0xc (FPO: [3,0,0])
01 00a0fe38 772d8852 00000108 ffffffff 00000000 KERNELBASE!WaitForSingleObjectEx+0x99 (FPO: [SEH])
02 00a0fe4c 00411459 00000108 ffffffff 0f7e47f0 KERNELBASE!WaitForSingleObject+0x12 (FPO: [Non-Fpo])
03 00a0ff28 0f7e48d1 00000000 083591b5 0f7e47f0 locktest!ThreadProc1+0x59 (FPO: [Non-Fpo]) (CONV: stdcall) [e:\ksource\pythonx\note\locktest\locktest.cpp @ 12]
04 00a0ff64 0f7e4877 005c7650 00a0ff80 76e60419 msvcr80d!_callthreadstartex+0x51 (FPO: [Non-Fpo]) (CONV: cdecl) [f:\dd\vctools\crt_bld\self_x86\crt\src\threadex.c @ 348]
05 00a0ff70 76e60419 005c7650 76e60400 00a0ffdc msvcr80d!_threadstartex+0x87 (FPO: [Non-Fpo]) (CONV: stdcall) [f:\dd\vctools\crt_bld\self_x86\crt\src\threadex.c @ 331]
06 00a0ff80 77be66ed 005c71d0 b731a4ad 00000000 kernel32!BaseThreadInitThunk+0x19 (FPO: [Non-Fpo])
07 00a0ffdc 77be66bd ffffffff 77c053e8 00000000 ntdll_77b80000!__RtlUserThreadStart+0x2f (FPO: [SEH])
08 00a0ffec 00000000 0f7e47f0 005c71d0 00000000 ntdll_77b80000!_RtlUserThreadStart+0x1b (FPO: [Non-Fpo])

   2  Id: 572c.78e4 Suspend: 0 Teb: 00383000 Unfrozen
 # ChildEBP RetAddr  Args to Child
00 00befdc4 772d88f9 00000104 00000000 00000000 ntdll_77b80000!NtWaitForSingleObject+0xc (FPO: [3,0,0])
01 00befe38 772d8852 00000104 ffffffff 00000000 KERNELBASE!WaitForSingleObjectEx+0x99 (FPO: [SEH])
02 00befe4c 00411549 00000104 ffffffff 0f7e47f0 KERNELBASE!WaitForSingleObject+0x12 (FPO: [Non-Fpo])
03 00beff28 0f7e48d1 00000000 082b91b5 0f7e47f0 locktest!ThreadProc2+0x59 (FPO: [Non-Fpo]) (CONV: stdcall) [e:\ksource\pythonx\note\locktest\locktest.cpp @ 25]
04 00beff64 0f7e4877 005c71d0 00beff80 76e60419 msvcr80d!_callthreadstartex+0x51 (FPO: [Non-Fpo]) (CONV: cdecl) [f:\dd\vctools\crt_bld\self_x86\crt\src\threadex.c @ 348]
05 00beff70 76e60419 005c71d0 76e60400 00beffdc msvcr80d!_threadstartex+0x87 (FPO: [Non-Fpo]) (CONV: stdcall) [f:\dd\vctools\crt_bld\self_x86\crt\src\threadex.c @ 331]
06 00beff80 77be66ed 005c7410 b72fa4ad 00000000 kernel32!BaseThreadInitThunk+0x19 (FPO: [Non-Fpo])
07 00beffdc 77be66bd ffffffff 77c053e8 00000000 ntdll_77b80000!__RtlUserThreadStart+0x2f (FPO: [SEH])
08 00beffec 00000000 0f7e47f0 005c7410 00000000 ntdll_77b80000!_RtlUserThreadStart+0x1b (FPO: [Non-Fpo])

```


### 句柄查看

```
0:000:x86> !handle 0x00000108 f;
Handle 00000108
  Type         	Mutant
  Attributes   	0
  GrantedAccess	0x1f0001:
         Delete,ReadControl,WriteDac,WriteOwner,Synch
         QueryState
  HandleCount  	2
  PointerCount 	65538
  Name         	\Sessions\1\BaseNamedObjects\MutexB
  Object specific information
    Mutex is Owned
    Mutant Owner 572c.78e4
0:000:x86> !handle 0x00000104 f;
Handle 00000104
  Type         	Mutant
  Attributes   	0
  GrantedAccess	0x1f0001:
         Delete,ReadControl,WriteDac,WriteOwner,Synch
         QueryState
  HandleCount  	2
  PointerCount 	65538
  Name         	\Sessions\1\BaseNamedObjects\MutexA
  Object specific information
    Mutex is Owned
    Mutant Owner 572c.72e4

```


## References

- [1] [WinDbg -- 调试互斥体 (Mutex) 死锁 {% include relref_csdn.html %}](https://blog.csdn.net/china_jeffery/article/details/78927524)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-01-win-CriticalSection-Lock.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/zh-cn/windows/win32/dlls/dynamic-link-library-best-practices]({% include relrefx.html url="/backup/2020-11-01-win-CriticalSection-Lock.md/docs.microsoft.com/a6f1b753.html" %})
- [https://mp.weixin.qq.com/s/tetpft089bWAV9VxfjCzqA]({% include relrefx.html url="/backup/2020-11-01-win-CriticalSection-Lock.md/mp.weixin.qq.com/f94113cf.html" %})
- [https://blog.csdn.net/china_jeffery/article/details/78927524]({% include relrefx.html url="/backup/2020-11-01-win-CriticalSection-Lock.md/blog.csdn.net/06aee774.html" %})
