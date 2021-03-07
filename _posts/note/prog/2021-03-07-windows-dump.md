---
layout: post
title: "编程 C++ -- VC++ 程序捕获所有异常"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---

Breakpad
* 在 windows 平台上，使用微软提供的 SetUnhandledExceptionFilter() 方法来实现。
* 在 OS X 平台上，通过创建一个线程来监听 Mach Exception port 来实现。
* 在 Linux 平台上，通过设置一个信号处理器来监听 SIGILL SIGSEGV 等异常信号。

```cpp
EXTERN_C IMAGE_DOS_HEADER __ImageBase;
#define HINST_THISCOMPONENT ((HINSTANCE)&__ImageBase)
```

一些不错的文章：
* [VC++ 程序捕获所有异常](https://gclxry.com/article/catch-all-exceptions-in-visual-cpp/)
* [使用 windbg 定位句柄泄漏](https://gclxry.com/article/use-windbg-to-locate-handle-leaks/)
* [实现一个标准的单例](https://gclxry.com/article/implement-a-right-cpp-singleton/)
* [Windows 内存类型介绍](https://gclxry.com/article/windows-memory-introduction/)
* [Windows 上锁的实现](https://gclxry.com/article/implement-a-cpp-lock-on-windows/)
* [Windows 上通过 bat 避免 python 冲突](https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/)
* [Effective Exception Handling in Visual C++](https://www.codeproject.com/Articles/207464/Exception-Handling-in-Visual-Cplusplus)

C++11 之后，保证了静态变量的初始化是线程安全的。这样创建一个单例非常简单，代码如下：
```cpp
class Singleton {
public:
    static Singleton *GetInstance() {
        static Singleton intance;
        return &intance;
    }

private:
    // 禁止在类外创建实例
    Singleton() = default;

    // 禁止在类外销毁
    ~Singleton() = default;

    // 禁止拷贝和赋值
    Singleton(const Singleton &) = delete;
    Singleton &operator=(const Singleton &) = delete;
};
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-07-windows-dump.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://gclxry.com/article/catch-all-exceptions-in-visual-cpp/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/788b277a.html" %})
- [https://gclxry.com/article/use-windbg-to-locate-handle-leaks/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/1fa2a3b5.html" %})
- [https://gclxry.com/article/implement-a-right-cpp-singleton/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/a115665e.html" %})
- [https://gclxry.com/article/windows-memory-introduction/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/8aaf20da.html" %})
- [https://gclxry.com/article/implement-a-cpp-lock-on-windows/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/f4a7bda8.html" %})
- [https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/]({% include relref.html url="/backup/2021-03-07-windows-dump.md/gclxry.com/43348a06.html" %})
- [https://www.codeproject.com/Articles/207464/Exception-Handling-in-Visual-Cplusplus]({% include relref.html url="/backup/2021-03-07-windows-dump.md/www.codeproject.com/2468bc01.html" %})
