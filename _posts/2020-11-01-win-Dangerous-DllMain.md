---
layout: post
title: "调试 -- 危险的 Windows DllMain 死锁问题"
author:
location: "珠海"
categories: ["调试"]
tags: ["编程笔记", "调试", "死锁"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

[^_^]: IPC 卡死 twiki 78250087
[^_^]: 不要在 DllMain 中做的事情 twiki 19302552


## 不要在 DllMain 中做的事情

不要再 DllMain 做太多事情，容易导致线程卡死，特别的注入或者 hook 系统进程的千万要注意，导致严重后果：
1. 系统进程卡死，无法操作桌面或者桌面黑屏。
2. 导致用户进程起不来。
3. ...


### 直接或者间接调用 LoadLibrary(Ex)

假如我们在 A.dll 中的 DllMain 收到 DLL_PROCESS_ATTACH 时，加载了 B.dll；
而 B.dll 中的 DllMain 在收到 DLL_PROCESS_ATTACH 时又去加载 A.dll。则产生了循环依赖。
但是注意不要想当然认为这个过程是 A.dll 的 DllMain 调用了 B.dll 的 DllMain，
B.dll 的 DllMain 再调用了 A.dll 的 DllMain 这样的死循环。即使不出现循环依赖，也会死锁的。


### 使用 CoInitializeEx

在 CoInitializeEx 底层会调用 LoadLibraryEx，原因同上。


### 使用 CreateProcess

CreateProcess 在底层执行了加载 DLL 的操作。我用 IDA 查看 Kernel32 中的 CreateProcess 可以发现其底层调用的 CreateProcessInternalW。


### 使用 User32 或 Gdi32 中的函数

User32 和 Gdi32 中部分函数在调用的底层会加载其他 DLL。


### 使用托管代码

运行托管代码需要加载其他 DLL。


### 与其他线程同步执行

进程创建和销毁以及 DLL 的加载都要进入 PEB 的 LoadLock 临界区。
如果占用了 LoaderLock 临界区的线程在等待一个需要经过临界区才能结束的线程时，就发生了死锁。


### 同步对象

如果该同步对象的释放需要获得 PEB 中的 LoaderLock，而占用该临界区的线程又要去等待这个同步对象，则会死锁。
其实 F 中的线程也算是个同步对象。


### 使用 CreateThread

主线程进入临界区去调用 DllMain 时进入了临界区，而工作线程也要进入临界区去执行 DllMain。
但是此时临界区被主线程占用，工作线程便进入等待状态。而主线程却等待工作线程退出才退出临界区。
于是这就是死锁产生的原因。


### 使用 ExitThread

理由同上。


## DllMain 的相关特性

1. Dll 的加载不会导致之前创建的线程调用其 DllMain 函数。

2. 线程创建后会调用已经加载了的 DLL 的 DllMain，且调用原因是 DLL_THREAD_ATTACH。（DisableThreadLibraryCalls 会导致该过程不被调用）

3. TerminateThread 方式终止线程是不会让该线程去调用该进程中加载的 Dll 的 DllMain。

4. 线程正常退出时，会调用进程中还没卸载的 DLL 的 DllMain，且调用原因是 DLL_THREAD_DETACH。

5. 进程正常退出时，会调用（不一定是主线程）该进程中还没卸载的 DLL 的 DllMain，且调用原因是 DLL_PROCESS_DETACH。

6. 加载 DLL 进入进程空间时（和哪个线程 LoadLibrary 无关），加载它的线程会调用 DllMain，且调用原因是 DLL_PROCESS_ATTACH。

7. DLL 从进程空间中卸载出去前，会被卸载其的线程调用其 DllMain，且调用原因是 DLL_PROCESS_DETACH。

8. TerminateProcess 将导致线程和进程在退出时不对未卸载的 DLL 进行 DllMain 调用。

9. ExitProcess 将导致主线程意外退出，子线程对未卸载的 DLL 进行了 DllMain 调用，且调用原因是 DLL_PROCESS_DETACH。

10. ExitThread 是最和平的退出方式，它会让线程退出前对未卸载的 DLL 调用 DllMain。

11. 线程的创建和退出不会对调用了 DisableThreadLibraryCalls 的 DLL 调用 DllMain。

{% include image.html url="/assets/images/201101-win-dangerous-dllmain/image2017-11-10_15-24-53.png" %}


### References

- [1] [《DllMain 中不当操作导致死锁问题的分析--加载卸载 DLL 与 DllMain 死锁的关系》 {% include relref_csdn.html %}](http://blog.csdn.net/breaksoftware/article/details/8163362)
- [2] [《DllMain 中不当操作导致死锁问题的分析--导致 DllMain 中死锁的关键隐藏因子》 {% include relref_csdn.html %}](http://blog.csdn.net/breaksoftware/article/details/8150476)
- [3] [《DllMain 中不当操作导致死锁问题的分析--线程退出时产生了死锁》 {% include relref_csdn.html %}](http://blog.csdn.net/breaksoftware/article/details/8163663)
- [4] <https://docs.microsoft.com/zh-cn/windows/win32/api/objbase/nf-objbase-coinitialize?redirectedfrom=MSDN>
- [5] <https://docs.microsoft.com/zh-cn/windows/win32/dlls/dynamic-link-library-best-practices?redirectedfrom=MSDN>
- [6] <https://docs.microsoft.com/zh-cn/windows/win32/dlls/dllmain?redirectedfrom=MSDN>
- [7] <https://bbs.pediy.com/thread-208999.htm>


## IPC 卡死

1. FreeLibrary -> LdrUnloadDll
    1. 锁住 LdrpLoadCompleteEvent 事件对象
    2. 发送 DLL_PROCESS_DETACH 消息给 dll
    3. 释放 LdrpLoadCompleteEvent 事件对象

2. Dll 接收到 DLL_PROCESS_DETACH 事件后，做清理操作，清理全局对象等。

3. 新线程起来：LdrInitializeThunk -> LdrpDrainWorkQueue 中的 LdrpLoadCompleteEvent 锁

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-22: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://blog.csdn.net/breaksoftware/article/details/8163362]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/blog.csdn.net/87294419.html" %})
- [http://blog.csdn.net/breaksoftware/article/details/8150476]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/blog.csdn.net/44e57bef.html" %})
- [http://blog.csdn.net/breaksoftware/article/details/8163663]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/blog.csdn.net/79314094.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/api/objbase/nf-objbase-coinitialize?redirectedfrom=MSDN]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/docs.microsoft.com/488b94b8.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/dlls/dynamic-link-library-best-practices?redirectedfrom=MSDN]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/docs.microsoft.com/67dab8c2.html" %})
- [https://docs.microsoft.com/zh-cn/windows/win32/dlls/dllmain?redirectedfrom=MSDN]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/docs.microsoft.com/2170abf7.html" %})
- [https://bbs.pediy.com/thread-208999.htm]({% include relref.html url="/backup/2020-11-01-win-Dangerous-DllMain.md/bbs.pediy.com/60516d54.htm" %})
