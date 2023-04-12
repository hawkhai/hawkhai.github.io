---
layout: post
title: "编程与调试 -- Tiny Module, Tiny My Life (Windows)"
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
cluster: "Tiny Code & Module"
---

有些模块经常用，很简单，但是反反复复写，最终下决定维护一个通用的模块库。
* **kinjector** 基于 minhook 和 EasyHook 实现的远程注入，少许代码可以实现钩子程序。
* **sharememory** Windows 共享内存，跨进程内存读写，同步机制。
* **kpipe** Windows 远程调用，函数跨进程调用等。
* **remotecall** Windows 远程调用，函数跨进程调用等。


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


### klauncher


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

如果要实现动态长度，用两个 sharememory 实现即可。


## kpipe & remotecall

这个区分服务端和客户端。

m_svrMgr = new KPipeSvrMgr();
m_pPipeSvr = m_svrMgr->CreatePipeSvr();
m_svrMgr->ReleasePipeSvr(m_pPipeSvr);

m_pPipeSvr->SetMsgProcessor(this);
m_pPipeSvr->Start(GetChildSvrPipeName(GetCurrentProcessId()).GetString());

E:\kpdf\pdfreader_master\image\pipe\fastimagePipe.h

验证 收工 remotecall
实现 klauncher。
全部采用 md 源码模式。

崩溃收集。
升级实现。


## remotecall

kpipe 的进一步封装，包含握手过程，从而实现相互调用，简单到 **爆** 。

客户端：
```cpp
#include <iostream>
#include <assert.h>
#include "../remotelib/myremote.h"
#include "../../vld/include/vld.h"

class ClientCallback : public IRmtCallPipeCallback {
    // 线程回调。
    virtual bool OnProcess(int func, const nlohmann::json& argv, nlohmann::json& retv) override {
        printf("ClientCallback");
        return true;
    }
};

int main()
{
    ClientCallback callback;
    MyPipeRemoteServ myServ(callback);

    // 启动子进程。
    std::string gexe = GenerateExeName("remotetarget");
    myServ.StartClient(true, gexe.c_str());

    system("pause");
    nlohmann::json data, result;
    // 调用子进程函数。
    CHECK_RETV_ASSERT(myServ.CallClientFunction(1, data, result));
    return 0;
}
```

服务端：
```cpp
#include <iostream>
#include <assert.h>
#include <string>
#include "../remotelib/myremote.h"
#include "../../vld/include/vld.h"

class ServCallback : public IRmtCallPipeCallback {
    virtual bool OnProcess(int func, const nlohmann::json& argv, nlohmann::json& retv) override {
        printf("ServCallback");
        return true;
    }
};

int _tmain(int argc, _TCHAR* argv[])
{
    setlocale(LC_ALL, "chs");

    ServCallback callback;
    MyPipeRemoteClient myClient(argc, argv, callback);

    nlohmann::json data, result;
    // 调用父进程函数。
    CHECK_RETV_ASSERT(myClient.CallServFunction(1, data, result));

    system("pause");
    return 0;
}
```


## kdll


### kdll.h

```cpp
#pragma once
#include <assert.h>
#include <windows.h>
#include <string>

#ifdef KDLL_EXPORTS
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT __declspec(dllimport)
#endif

#define KDLL_ERSION 1

__interface IDllInterface {
    virtual int Version() = 0;
    virtual int Release() = 0;
    virtual int GetDocumentPageCount() = 0;
};

#ifdef __cplusplus
extern "C" {
#endif
    DLLEXPORT IDllInterface* CreateEntry();
#ifdef __cplusplus
}
#endif

class KDllWrap : public IDllInterface {

    static std::wstring getCurrentDir() {
        wchar_t tpath[MAX_PATH] = { 0 };
        DWORD dwRet = GetModuleFileNameW(NULL, tpath, MAX_PATH);
        if (dwRet == 0) {
            return L".\\";
        }
        std::wstring strexe = tpath;
        int index = strexe.rfind(L'\\');
        if (index <= 0) {
            return L".\\";
        }
        return strexe.substr(0, index + 1);
    }
    static HINSTANCE loadLibrary(const wchar_t* libPath) {
        std::wstring curdir = getCurrentDir();
        if (curdir.empty()) {
            return NULL;
        }

        std::wstring current = curdir;
        current.append(libPath);

        wchar_t lpBuffer[MAX_PATH];
        GetCurrentDirectory(MAX_PATH, lpBuffer);
        SetCurrentDirectory(curdir.c_str());
        HINSTANCE hDLL = LoadLibrary(current.c_str());
        SetCurrentDirectory(lpBuffer);

        if (hDLL == NULL) {
            int err = GetLastError();
            assert(false);
            return NULL;
        }
        return hDLL;
    }

public:
    virtual int Version() override {
        if (!m_interface) {
            return -1;
        }
        return m_interface->Version();
    }

    virtual int Release() override {
        if (!m_interface) {
            return -1;
        }
        auto retv = m_interface->Release();
        m_interface = nullptr;
        return retv;
    }

    virtual int GetDocumentPageCount() override {
        if (!m_interface) {
            return -1;
        }
        return m_interface->GetDocumentPageCount();
    }

    KDllWrap() {
        const wchar_t* libPath = L"kdll.dll";
        m_hDLL = loadLibrary(libPath);
        if (m_hDLL == nullptr) {
            int err = GetLastError();
            assert(false);
            return;
        }

        typedef IDllInterface* (*CreateEntryFunc)();
        CreateEntryFunc fptr = (CreateEntryFunc)GetProcAddress(m_hDLL, "CreateEntry");
        if (fptr == nullptr) {
            int err = GetLastError();
            assert(false);
            return;
        }
        m_interface = fptr();
        if (m_interface->Version() < KDLL_ERSION) {
            m_interface->Release();
            m_interface = nullptr;
            assert(false);
        }
    }
    virtual ~KDllWrap() {
        if (!m_interface) {
            return;
        }
        m_interface->Release();
        m_interface = nullptr;
        // m_hDLL 不释放了。
    }

private:
    IDllInterface* m_interface = nullptr;
    HINSTANCE m_hDLL = nullptr;
};
```


### kdll.cpp

```cpp
#include "pch.h"
#include "kdll.h"

class KDllInstance : public IDllInterface {
public:
    virtual int Version() override {
        return KDLL_ERSION;
    }
    virtual int Release() override {
        delete this;
        return 0;
    }
    virtual int GetDocumentPageCount() override {
        return 7;
    }
};

IDllInterface* CreateEntry() {
    return new KDllInstance();
}
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-04-04-tiny-module.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/www.codeproject.com/5204d1cf.html" %})
- [http://www.cnblogs.com/dongsheng/p/4460944.html]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/www.cnblogs.com/44de51f5.html" %})
- [http://blog.chinaunix.net/uid-26833883-id-3230564.html]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/blog.chinaunix.net/28af4862.html" %})
- [https://blog.csdn.net/shuilan0066/article/details/87979315]({% include relrefx.html url="/backup/2023-04-04-tiny-module.md/blog.csdn.net/750dc08b.html" %})
