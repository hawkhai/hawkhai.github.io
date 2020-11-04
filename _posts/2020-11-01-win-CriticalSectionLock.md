---
layout: post
title: "调试 -- Windbg 调试关键区（CriticalSection）死锁"
location: "珠海"
categories: ["调试"]
tags: [Prog Note, 调试]
toc: true
---

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

等了一下，线程无法正常退出，然后 TerminateThread，临界区被占用造成死锁，进程还是无法正常退出。悲剧。

卡死死锁问题。一般出现在主线程，否则也很难被发现。

1. 不要在 DllMain 中做的事情。
2. 不要轻易用 TerminateThread / ExitThread / SuspendThread。
    子线程和主线程都使用了一个临界区变量，TerminateThread 结束线程时，不会回收线程的栈！
3. 使用了 \_\_try \_\_except 捕获了异常，导致锁未释放。

在 Windows 中使用互斥锁可以有效的避免死锁。
当持有 Mutex 的线程在调用 ReleaseMutex 前意外退出，如 ExitThread 和 TerminateThread。
系统会把 Mutex 分给等待 Mutex 的线程中的一个并返回 Wait_Abandoned，从而避免了死锁。


## Dynamic-Link Library Best Practices

DllMain 在收到 DLL_PROCESS_ATTACH 和 DLL_PROCESS_DETACH 时会进入临界区。
它是使其他线程不能进入临界区从而导致死锁的关键。

<https://docs.microsoft.com/zh-cn/windows/win32/dlls/dynamic-link-library-best-practices>

{% include image.html url="/images/win-CriticalSectionLock/fig2.png" %}


## 定位到卡死位置

关键命令：

```shell
!cs -l # 获取更为全面的关键区信息
!handle 000000c4 f # 查看该句柄的信息
!locks # 查看进程中哪些锁处于锁定状态
```

```
ntdll_77b20000!ZwWaitForSingleObject+0x15:
00000000`77b3f8e1 83c404          add     esp,4
Minidump doesn't have an exception context
Unable to get exception context, HRESULT 0x80004002
ChildEBP          RetAddr           Args to Child
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
