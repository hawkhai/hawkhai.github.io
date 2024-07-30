---
layout: post
title: "编程与调试 C++ -- Win10 uwp 使用 WinDbg 调试"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory", "C/C++", "MacOS"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---

> * [Win10 uwp 使用 WinDbg 调试](https://blog.lindexi.com/post/win10-uwp-%E4%BD%BF%E7%94%A8-WinDbg-%E8%B0%83%E8%AF%95.html)
> * [通过命令行启动 uwp 应用 {% include relref_csdn.html %}](https://blog.csdn.net/frozleaf/article/details/121889483)
> * [Win10 uwp 使用 WinDbg 调试](https://cloud.tencent.com/developer/article/2066552)
> * [使用 WinDbg 调试 UWP 应用](https://learn.microsoft.com/zh-cn/windows-hardware/drivers/debugger/debugging-a-uwp-app-using-windbg)

vs2022 自带的 winui3 就是这套
创建个 UI 都是其他进程创建的 UI 管理是有宿主进程的 点按钮响应啥的 都走的 RPC 通讯 跨进程回来的


* https://github.com/StackOverflowExcept1on/uwp-injector
    * This project allows to perform DLL-injection into UWP applications

* https://github.com/kimjongbing/dll_injector_uwp
    * Simple DLL injector coded in Rust and C++, compatible with UWP processes

* https://github.com/fligger/FateInjector
    * The Fate Client Themed UWP app dll Injector


<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-07-30-win10-uwp-windbg.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.lindexi.com/post/win10-uwp-%E4%BD%BF%E7%94%A8-WinDbg-%E8%B0%83%E8%AF%95.html]({% include relrefx.html url="/backup/2024-07-30-win10-uwp-windbg.md/blog.lindexi.com/2d439eea.html" %})
- [https://blog.csdn.net/frozleaf/article/details/121889483]({% include relrefx.html url="/backup/2024-07-30-win10-uwp-windbg.md/blog.csdn.net/bd9202b0.html" %})
- [https://cloud.tencent.com/developer/article/2066552]({% include relrefx.html url="/backup/2024-07-30-win10-uwp-windbg.md/cloud.tencent.com/a08847ce.html" %})
- [https://learn.microsoft.com/zh-cn/windows-hardware/drivers/debugger/debugging-a-uwp-app-using-windbg]({% include relrefx.html url="/backup/2024-07-30-win10-uwp-windbg.md/learn.microsoft.com/50919e15.html" %})
