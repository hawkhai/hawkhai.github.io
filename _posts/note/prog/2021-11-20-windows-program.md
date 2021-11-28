---
layout: post
title: "编程与调试 -- Windows 编程知识点（文档整理）"
author: yqh
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---


## Windows C++ 开发基础


### 头文件引用顺序建议

* 预编译头文件
* 本 cpp 对应的头文件
* C 系统头文件
* C++ 系统头文件
* 项目内部头文件


### 类

* 不要在 C++ 中的构造函数与析构函数中调用虚函数
* 只要用到了继承关系，面向接口编程的情况下，都需要虚析构函数。
* `/we4263` 限制 override 必须写上。
  ```cmake
# Enable and treat as errors the following warnings to easily detect virtual function signature failures:
# 'function' : member function does not override any base class virtual member function
# 'virtual_function' : no override available for virtual member function from base 'class'; function is hidden
target_compile_options(trinity-compile-option-interface
  INTERFACE
    /we4263
    /we4264)
```


### 接口定义

* C++ 没有 interface 关键字，所以我们使用定义纯虚函数的 class 作为
* 接口中不能定义成员变量
* **需要定义一个虚析构函数或者用于释放当前实例对象的纯虚函数，二者必选其一**


## 开发环境和调试入门


### 提升代码质量：性能监控工具

Visual Studio 2019 提供了非常强大的性能分析工具，可以方便对位 CPU、内存问题。
通过按 F5 在 Visual Studio 中开始调试时，默认情况下会出现“诊断工具”窗口。 要手动打开该窗口，
请选择“Debug” > “Windows” > “Show Diagnostic Tools（诊断工具）”。“诊断工具”窗口显示有关事件、进程内存和 CPU 使用情况的信息。


### Visual Studio 编译选项


### Manifest 清单文件

1. 我们在开发应用程序时，一般会引入一些第三方库，通常情况下，我们是把这些第三方依赖文件放到应用程序所处目 录，这样应用程序启动时就能正确找到相关依赖文件。但当依赖文件比较多，我们希望对依赖的文件进行归类，放置 到不同的目录下以便管理，这个时候应用程序的 manifest 就派上用场了。
2. 在介绍应用程序的 manifest 之前，需要了解一下并行程序集（Side-by-Side Assembly）。什么是并行程序集呢 ? 并 行程序集是微软为了解决 DLL Hell 问题而提出的一种解决方案，它采用 manifest 文件扫描组件之间的依赖关系。其 工作原理如下图所求：
3. 什么是 DLL Hell 问题，微软在未提出 Side-by-Side Assembly 之前，应用程序启动时按照一定的规则加载 DLL。通 常情况下，应用程序会采用动态链接方式共享一些操作系统提供的基础库文件，当 Windows 更新共享库且共享库不 能向后兼容时（DLL 自身并不能向后兼容，这种情况通常发生在 DLL 的内存布局发生了改变）, 那些依赖于老版本共享 库的应用程序就不能正常工作了。
4. 为了解决这个问题，微软重写了 DLL 动态加载子系统，提出了并行程序集的解决方案，即允许多个版本的库共同存在， 应用程序通过 manifest 描述自身所依赖的文件，SxS Manager 再通过 manifest 按照一定的规则找到应用程序的依
赖文件，使应用程序正确工作。

以 HelloWorld.exe 为例，假设它依赖 MyMath.dll，而我们又希望 MyMath.dll 放到 math 子目录，目录结构如下：
```
/AppDir
    |--- HelloWorld.exe
    |     |
    |--- math
          |--- math.manifest
          |--- MyMath.dll
```

SxS Manager 加载顺序。Side-by-side searches the WinSxS folder.
1. `\\<appdir>\<assemblyname>.DLL`
2. `\\<appdir>\<assemblyname>.manifest`
3. `\\<appdir>\<assemblyname>\<assemblyname>.DLL`
4. `\\<appdir>\<assemblyname>\<assemblyname>.manifest`
{% include image.html url="/assets/images/211120-windows-program/rumen1.png" width="50%" %}


### Windbg 快速入门：调试 Notepad

1. 打开 windbg，通过 File -> Open Executable 调起 notepad.exe
2. 命令：x notepad!*main* 查找 main 函数入口
3. 命令：bu notepad!WinMain 设置断点
4. 命令：g 运行到 WinMain，触发断点
5. 命令：k 查看当前调用堆栈
6. 命令：bu ntdll!ZwWriteFile 查看保存文件调用堆栈
7. 命令：~ 查看线程
8. 命令：~0s 切换到 0 线程，k 查看调用堆栈

`!analyze` 命令。自动分析崩溃的详细信息，分析异常崩溃的 dump 文件，第一步就是要执行 !analyze -v 异常调用栈。

* [Visual Studio 性能分析教程](https://docs.microsoft.com/zh-cn/visualstudio/profiling/?view=vs-2019)
* [Visual Studio 调试教程](https://docs.microsoft.com/zh-cn/visualstudio/debugger/?view=vs-2019)
* [Windbg 调试 Notepad 的简单入门](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-11-20-windows-program.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/zh-cn/visualstudio/profiling/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/bb0194bd.html" %})
- [https://docs.microsoft.com/zh-cn/visualstudio/debugger/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/78bdc34e.html" %})
- [https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/98a18465.html" %})
