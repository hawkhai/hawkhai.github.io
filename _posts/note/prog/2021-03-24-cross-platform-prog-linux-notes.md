---
layout: post
title: "编程与调试 C++ -- 跨 Android、Linux 和 Windows 的 C 编程杂记"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["Android", "C/C++", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## CMake & OpenCV

```
mkdir buildx64
cd buildx64
cmake ..
cd ..

mkdir build
cd build
cmake .. -A Win32
cd ..
```


## 宏定义

```cpp
#include "kminwindef.h"

#include "kIrrCompileConfig.h"
#ifdef _KIRR_WINDOWS_
#ifdef _KIRR_ANDROID_PLATFORM_
#ifdef _KIRR_WINDOWS_API_

// 常用的几个。
#ifdef _MSC_VER /* Visual Studio */
#ifdef __ANDROID__
// 不常用不建议采用的。
#ifdef _WIN32 // _WINDOWS
```


## String

Linux 为 srandom 和 random 函数，Windows 为 srand 和 rand 函数。

Linux 为 snprintf，Windows 为 \_snprintf。

同理，Linux 中的 strcasecmp，Windows 为 \_stricmp。


## Time

Linux 中，time_t 结构是长整形。而 windows 中，time_t 结构是 64 位的整形。如果要在 windows 始 time_t 为 32 位无符号整形，可以加宏定义，_USE_32BIT_TIME_T。

Linux 中，sleep 的单位为秒。Windows 中，Sleep 的单位为毫秒。即，Linux 下 sleep (1)，在 Windows 环境下则需要 Sleep (1000)。

Windows 中的 timecmp 宏，不支持大于等于或者小于等于。

Windows 中没有 struct timeval 结构的加减宏可以使用，需要手动定义：

```cpp
#define MICROSECONDS (1000 * 1000)

#define timeradd(t1, t2, t3) do {                                                          \
  (t3)->tv_sec = (t1)->tv_sec + (t2)->tv_sec;                                              \
  (t3)->tv_usec = (t1)->tv_usec + (t2)->tv_usec % MICROSECONDS;                            \
  if ((t1)->tv_usec + (t2)->tv_usec > MICROSECONDS) (t3)->tv_sec ++;                       \
} while (0)

#define timersub(t1, t2, t3) do {                                                          \
  (t3)->tv_sec = (t1)->tv_sec - (t2)->tv_sec;                                              \
  (t3)->tv_usec = (t1)->tv_usec - (t2)->tv_usec;                                           \
  if ((t1)->tv_usec - (t2)->tv_usec < 0) (t3)->tv_usec --, (t3)->tv_usec += MICROSECONDS;  \
} while (0)
```

Android、Linux 实现 Windows API：

```cpp
DWORD WINAPI GetTickCount(VOID) {
    struct timespec ts{};
    if (clock_gettime(CLOCK_MONOTONIC, &ts) != 0) {
        return 0;
    }
    DWORD theTick;
    theTick = ts.tv_nsec / 1000000;
    theTick += ts.tv_sec * 1000;
    return theTick;
}

ULONGLONG WINAPI GetTickCount64(VOID) {
    struct timespec ts{};
    if (clock_gettime(CLOCK_MONOTONIC, &ts) != 0) {
        return 0;
    }
    ULONGLONG theTick;
    theTick = ts.tv_nsec / 1000000;
    theTick += ts.tv_sec * 1000;
    return theTick;
}
```


## File

Linux 与 Windows 下面，均可以使用 stat 调用来查询文件信息。但是，Linux 只支持 2G 大小，而 Windows 只支持 4G 大小。
为了支持更大的文件查询，可以在 Linux 环境下加 \_FILE\_OFFSET\_BITS=64 定义，在 Windows 下面使用 \_stat64 调用，入参为 struct \_\_stat64。

Linux 中可根据 stat 的 st_mode 判断文件类型，有 S_ISREG、S_ISDIR 等宏。Windows 中没有，需要自己定义相应的宏，如

```cpp
#define S_ISLNK(m) (((m) & 00170000) == 0120000)
#define S_ISREG(m) (((m) & 00170000) == 0100000)
#define S_ISDIR(m) (((m) & 00170000) == 0040000)
#define S_ISCHR(m) (((m) & 00170000) == 0020000)
#define S_ISBLK(m) (((m) & 00170000) == 0060000)
#define S_ISFIFO(m) (((m) & 00170000) == 0010000)
#define S_ISSOCK(m) (((m) & 00170000) == 0140000)
```

Linux 中删除文件是 unlink，Windows 中为 DeleteFile。

```cpp
// exdir 表示进行文件夹检查，不能是 文件夹
bool IsFilePathExists(const char* path, bool exdir)
{
    int code = ::access(path, 0);
    if (0 == code) {
        if (exdir && IsDirectory(path)) {
            return false;
        }
        return true;
    }
    return false;
}

bool IsFileRegular(const std::string &path) {
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISREG(st.st_mode);
}

bool IsDirectory(const std::string &path)
{
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISDIR(st.st_mode);
}
```


## LoadLibrary

```cpp
#include "pch.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <iostream>
#include <assert.h>

#include <kIrrCompileConfig.h>
#ifdef _MSC_VER
#include <EGL/egl.h>
#include <EGL/eglplatform.h>
#include <GLES2/gl2.h>
#include <GLES2/gl2platform.h>
#else
#include <EGL/egl.h>
#include <GLES/gl.h> // for glPointParameterf
#include <GLES2/gl2.h>
#include <GLES2/gl2ext.h>
//#include <GLES3/gl3.h> // for glReadBuffer
#define MAX_PATH 256
#include <dlfcn.h>
#endif

#include "fkdriver.h"
#include "fakedriverAdapter.h"
#include "fakehook.h"
#include "kminwindef.h"

#ifdef _KIRR_WINDOWS_
std::wstring getCurrentPath() {
    wchar_t tPath[MAX_PATH];
    DWORD dwRet = GetModuleFileName(NULL, tPath, MAX_PATH);
    std::wstring strexe = tPath;
    int index = strexe.rfind('\\');
    return strexe.substr(0, index);
}

HINSTANCE getLibrary(const TCHAR* libPath) {
    std::wstring current = getCurrentPath();
    current.append(libPath);

    int index = current.rfind('\\');
    std::wstring curdir = current.substr(0, index);

    WCHAR lpBuffer[MAX_PATH];
    GetCurrentDirectory(MAX_PATH, lpBuffer);
    SetCurrentDirectory(curdir.c_str());
    HINSTANCE hDLL = LoadLibrary(current.c_str());
    SetCurrentDirectory(lpBuffer);

    if (hDLL == nullptr) {
        int err = GetLastError();
        return nullptr;
    }
    return hDLL;
}

// Mali Adreno PowerVR
void* getEGLFunction(EnumFakeDriverHookFunction fid, const char* fname) {
    const wchar_t* libPath = getFakeDriverAdapterPath();
    static HINSTANCE hDLL = getLibrary(libPath);
    if (hDLL == nullptr) {
        int err = GetLastError();
        return nullptr;
    }
    fname = getFunctionName(fid);
    FARPROC fptr = GetProcAddress(hDLL, fname);
    if (fptr == nullptr) {
        int err = GetLastError();
        return nullptr;
    }
    return fptr;
}

extern "C" IMAGE_DOS_HEADER __ImageBase;
void* getCurrentEGLFunction(EnumFakeDriverHookFunction fid) {
    static HMODULE module = reinterpret_cast<HMODULE>(&__ImageBase);
    PROC result = GetProcAddress(module, getFunctionName(fid));
    return result;
}

PROC getCurrentProcAddress(EnumFakeDriverHookFunction fid) {
    static HMODULE module = reinterpret_cast<HMODULE>(&__ImageBase);
    PROC result = GetProcAddress(module, getFunctionName(fid));
    return result;
}

#else
void* getProcAddress(void* handle, EnumFakeDriverHookFunction fid) {

    if (handle == nullptr) {
        char* err = dlerror();
        return nullptr;
    }
    const char* fname = getFunctionName(fid);
    char buffer[MAX_PATH] = { 0 };
    for (int i = 0; i < strlen(fname); i++) {
        buffer[i] = fname[i];
        if (buffer[i] == '@') {
            buffer[i] = 0;
            break;
        }
    }
    void* fptr = dlsym(handle, &buffer[1]);
    if (fptr == nullptr) {
        char* err = dlerror();
        return nullptr;
    }
    return fptr;
}

void* getCurrentEGLFunction(EnumFakeDriverHookFunction fid) {
    static void* handle = dlopen("libfakedriver.so", RTLD_LAZY); // dlclose(handle);
    return getProcAddress(handle, fid);
}
void* getEGLFunction(EnumFakeDriverHookFunction fid, const char* fname) {
    static void* handle = dlopen("libfakedriverAdapter.so", RTLD_LAZY); // dlclose(handle);
    return getProcAddress(handle, fid);
}

#endif
```

Android:
```cpp
#include <jni.h>
#include <string>
#include <dlfcn.h> // 关键头文件。

void* getProcAddress(void* handle, const char* fname) {
    if (handle == nullptr) {
        char* err = dlerror();
        return nullptr;
    }
    void* fptr = dlsym(handle, fname);
    if (fptr == nullptr) {
        char* err = dlerror();
        return nullptr;
    }
    return fptr;
}

void* getFunctionPtr(const char* fname) {
    static void* handle = dlopen("libtest.so", RTLD_LAZY); // dlclose(handle);
    return getProcAddress(handle, fname);
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_test_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject thiz) {
    void* func = getFunctionPtr("Java_com_testEngine_platform",
                                "libtestEngine.so");
    typedef jstring JNICALL (*FUNC)(JNIEnv* env, jobject /* this */);
    FUNC myfunc = (FUNC) func;
    jstring retv = myfunc(env, thiz);
    return retv;
    //std::string hello = "Hello from C++";
    //return env->NewStringUTF(hello.c_str());
}
```


## windows 程序移植到 linux & mac 总结


### 标准 c++ 实现 CString 类和 TCHAR

<https://blog.csdn.net/qq_36810544/article/details/84329132>

<https://codeproject.freetls.fastly.net/Articles/1146/CString-clone-Using-Standard-C>


### std::string 跨平台格式化函数实现代码

<https://blog.csdn.net/jzkdl/article/details/80196309>


## Refs

[1] [from](https://www.linuxidc.com/Linux/2012-02/52963.htm)
[2] [from](https://www.linuxidc.com/Linux/2012-02/52963p2.htm)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-24-cross-platform-prog-linux-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/qq_36810544/article/details/84329132]({% include relrefx.html url="/backup/2021-03-24-cross-platform-prog-linux-notes.md/blog.csdn.net/211e02f4.html" %})
- [https://codeproject.freetls.fastly.net/Articles/1146/CString-clone-Using-Standard-C]({% include relrefx.html url="/backup/2021-03-24-cross-platform-prog-linux-notes.md/codeproject.freetls.fastly.net/ca031c29.html" %})
- [https://blog.csdn.net/jzkdl/article/details/80196309]({% include relrefx.html url="/backup/2021-03-24-cross-platform-prog-linux-notes.md/blog.csdn.net/b0f43536.html" %})
- [https://www.linuxidc.com/Linux/2012-02/52963.htm]({% include relrefx.html url="/backup/2021-03-24-cross-platform-prog-linux-notes.md/www.linuxidc.com/c0293f28.htm" %})
- [https://www.linuxidc.com/Linux/2012-02/52963p2.htm]({% include relrefx.html url="/backup/2021-03-24-cross-platform-prog-linux-notes.md/www.linuxidc.com/9efb56a2.htm" %})
