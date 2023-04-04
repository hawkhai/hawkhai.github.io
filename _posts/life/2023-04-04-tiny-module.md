---
layout: post
title: "编程与调试 -- Tiny Module, Tiny My Life"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["C/C++", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

有些模块经常用，很简单，但是反复写反复写，最终下决定维护一个通用的模块库。
* **kinjector** 基于 minhook 和 EasyHook 实现的远程注入，少许代码可以实现钩子程序。
* **sharememory** Windows 远程调用，内存共享，函数跨进程调用等。


## kinjector

基于 minhook 和 EasyHook 实现的远程注入，少许代码可以实现钩子程序。

* EasyHook32.dll & EasyHook64.dll
* MinHook.x64.dll & MinHook.x86.dll

* kinjector.exe & kinjector64.exe 负责注入。
  ```
  E:\kSource\pythonx\note\bin>kinjector.exe --help
  -i, -I, --pid=PID         Target process Id
  -n, -N, --pname=PNAME     Target process Name
  -k, -K, --hook=DLL        Hook DLL
  -p, -P, --pause           Exit pause
  -h, -H, --help            Shows the command help
  ```
* kloader.dll & kloader64.dll 被注入后加载的模块，会根据参数调用第三方模块。
  ```cpp
  typedef int (__stdcall *LPFN_ToyEntryPoint)(void*);
  assert(GetModuleHandleW(libPath) == hDLL);
  std::string fname = "ToyEntryPoint";
  LPFN_ToyEntryPoint fptr = (LPFN_ToyEntryPoint)GetProcAddress(hDLL, fname.c_str());
  if (!fptr) {
      fname = "_ToyEntryPoint@4";
      fptr = (LPFN_ToyEntryPoint)GetProcAddress(hDLL, fname.c_str());
  }
  ```
* kzcount.dll & kzcount64.dll 第三方模块。
  ```cpp
  #define DLL_API extern "C" __declspec(dllexport)
  DLL_API int __stdcall ToyEntryPoint(void* inRemoteInfo);
  int __stdcall ToyEntryPoint(void*) {
      mainfunc();
      return 7;
  }
  ```

* toytarget.exe & toytarget64.exe 测试目标。
* mycount.exe & mycount64.exe 模拟调用。


## sharememory

Windows 远程调用，内存共享，函数跨进程调用等。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-04-04-tiny-module.md.js" %}'></script></p>
