---
layout: post
title: "编程与调试 C++ -- 跨 Android、Linux 和 Windows 的 C 编程杂记"
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


## Refs

[1] [from](https://www.linuxidc.com/Linux/2012-02/52963.htm)
[2] [from](https://www.linuxidc.com/Linux/2012-02/52963p2.htm)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-24-cross-platform-windows-linux-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.linuxidc.com/Linux/2012-02/52963.htm]({% include relrefx.html url="/backup/2021-03-24-cross-platform-windows-linux-notes.md/www.linuxidc.com/c0293f28.htm" %})
- [https://www.linuxidc.com/Linux/2012-02/52963p2.htm]({% include relrefx.html url="/backup/2021-03-24-cross-platform-windows-linux-notes.md/www.linuxidc.com/9efb56a2.htm" %})
