---
layout: post
title: "编程与调试 C++ -- VC++ 程序捕获所有异常"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
archived: true
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


## 使用 Windows 错误报告 (WER)

打开注册表编辑器：
* 按 Win + R 打开运行对话框，输入 regedit 并按回车键。

导航到注册表项：
* 导航到 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps。

创建子项：
* 如果 LocalDumps 子项不存在，右键点击 Windows Error Reporting，选择 新建 -> 项，命名为 LocalDumps。

配置应用程序的转储设置：
* 在 LocalDumps 下，右键点击右侧窗格，选择 新建 -> 项，命名为您的应用程序的可执行文件名（例如 onnxruntime.exe）。
* 在新创建的项下，右键点击右侧窗格，选择 新建 -> 字符串值，命名为 DumpFolder。
* 双击 DumpFolder，输入您希望保存转储文件的路径（例如 C:\Dumps）。
* 再次右键点击右侧窗格，选择 新建 -> DWORD (32-bit) 值，命名为 DumpType。
* 双击 DumpType，设置其值为 2（表示完整内存转储）或 1（表示小型内存转储）。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-07-windows-dump-Exception-capture.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://gclxry.com/article/catch-all-exceptions-in-visual-cpp/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/788b277a.html" %})
- [https://gclxry.com/article/use-windbg-to-locate-handle-leaks/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/1fa2a3b5.html" %})
- [https://gclxry.com/article/implement-a-right-cpp-singleton/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/a115665e.html" %})
- [https://gclxry.com/article/windows-memory-introduction/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/8aaf20da.html" %})
- [https://gclxry.com/article/implement-a-cpp-lock-on-windows/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/f4a7bda8.html" %})
- [https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/gclxry.com/43348a06.html" %})
- [https://www.codeproject.com/Articles/207464/Exception-Handling-in-Visual-Cplusplus]({% include relrefx.html url="/backup/2021-03-07-windows-dump-Exception-capture.md/www.codeproject.com/2468bc01.html" %})
