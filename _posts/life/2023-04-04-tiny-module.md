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
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---

有些模块经常用，很简单，但是反复写反复写，最终下决定维护一个通用的模块库。
* **kinjector** 基于 minhook 和 EasyHook 实现的远程注入，少许代码可以实现钩子程序。
* **sharememory** Windows 共享内存，跨进程内存读写，同步机制。
* **kpipe** Windows 远程调用，函数跨进程调用等。


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

Windows 共享内存，跨进程内存读写，同步机制。

[TestFileLock.zip](https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock)
[共享内存，同步机制](https://sunocean.life/blog/blog/2022/05/31/Share-Momery)
<http://www.cnblogs.com/dongsheng/p/4460944.html>
<http://blog.chinaunix.net/uid-26833883-id-3230564.html>
<https://blog.csdn.net/shuilan0066/article/details/87979315>

Windows 下进程的地址空间在逻辑上是相互隔离的，但在物理上却是重叠的。所谓的重叠是指同一块内存区域可能被多个进程同时使用。
共享内存，各个进程可以共享同一块物理内存，进程可以直接读写内存，不需要数据拷贝。
由于多个进程共享一块内存，所以也需要同步机制。

1. 本进程创建
    1. 创建内存映射文件对象 CreateFileMapping，
        Windows 即在物理内存申请一块指定大小的内存区域，返回文件映射对象的句柄 hMap。
    2. 将内存对象映射在进程地址空间 MapViewOfFile。
2. 其它进程访问，其它进程访问这个内存对象时，
    1. OpenFileMapping 获取对象句柄。
    2. 调用 MapViewOfFile 映射在自己的进程空间。

完整代码：github.com/hawkhai/ShareMemory.git
共享内存，写入只要不释放，就可以实现跨进程读取，避免文件内容落地。
写入的函数负责共享内存块的创建。
这样，同一块内存块被映射到了不同的进程空间，从而达到多个进程共享同一个内存块的目的。

```cpp
#include <windows.h>
#include <iostream>
#include <string>
#include <vector>
#include <assert.h>
#include "../ShareMemoryDll/ShareMemoryDll.h"

using namespace ShareMemoryDll;

#define SHARE_MEMORY_NAME L"SHARE_MEMORY_TEST"
#define SHARE_MEMORY_SIZE (1024*1024) // 1MB

void testread() {
    ShareMemoryRead sharememory(SHARE_MEMORY_NAME);
    if (!sharememory.check()) {
        return;
    }

    CShareMemoryCallback callback;
    ShareMemoryData* data = nullptr;
    int datasize = 0;
    if ((datasize = sharememory.read(data, &callback)) >= 1) {
        TestData* testData = (TestData*)&data[0];
    }
    if (data) {
        callback.free(data);
    }
}

void testwrite() {
    ShareMemoryWrite sharememory(SHARE_MEMORY_NAME, SHARE_MEMORY_SIZE);
    if (!sharememory.check()) {
        return;
    }

    TestData testData(true);
    sharememory.write((ShareMemoryData*)&testData, sizeof(testData));
}
```


## kpipe

这个区分服务端和客户端。

m_svrMgr = new KPipeSvrMgr();
m_pPipeSvr = m_svrMgr->CreatePipeSvr();
m_svrMgr->ReleasePipeSvr(m_pPipeSvr);

m_pPipeSvr->SetMsgProcessor(this);
m_pPipeSvr->Start(GetChildSvrPipeName(GetCurrentProcessId()).GetString());

E:\kpdf\pdfreader_master\image\pipe\fastimagePipe.h



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-04-04-tiny-module.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/www.codeproject.com/5204d1cf.html" %})
- [http://www.cnblogs.com/dongsheng/p/4460944.html]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/www.cnblogs.com/44de51f5.html" %})
- [http://blog.chinaunix.net/uid-26833883-id-3230564.html]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/blog.chinaunix.net/28af4862.html" %})
- [https://blog.csdn.net/shuilan0066/article/details/87979315]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/blog.csdn.net/750dc08b.html" %})
