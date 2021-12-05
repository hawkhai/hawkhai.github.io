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


## Windows 系统导论

{% include image.html url="/assets/images/211120-windows-program/20211130235154.png" caption="内存管理" %}

{% include image.html url="/assets/images/211120-windows-program/v2-0e31467881f34c15094210a3048babbb_1440w.jpg" caption="虚拟地址转换" %}
{% include image.html url="/assets/images/211120-windows-program/20211201000052.png" %}
* MMU 和 TLB 都是硬件实现（减少操作系统的实现负担）
* TLB 是一个加速用的濶濴濶濻濸，命中时，目标内存都在物理内存中


### 栈空间

* ESP：栈指针寄存器 (extended stack pointer)，该指针永远指向系统栈最上面一个栈帧的栈顶。
* EBP：基址指针寄存器 (extended base pointer)，该指针永远指向系统栈最上面一个栈帧的底部。
* Callee 的第一个指令保存 caller 的 ebp。


### TLS 线程本地存储

* **干啥用** 线程范围内的全局存储
* **静态** 编译器辅助：__declspec(thread) int number;
* **动态** 通过 API 访问：TlsGetValue


### Sleep vs Yield

* 等待其他线程的结果不要用 Sleep+Loop
* 正确的等待是用 WaitForSingleObject，WaitForMultiObjects 的 API
* 正确的让出时间片是：SwitchToThread
* WaitXxx 还有马上检查的功能


### Windows 提供的同步对象

同步对象 | 支持等超时 | 进程锁 | 递归锁
---- | ---- | ---- | ----
CriticalSection 对象 | 否 | 否 | 是
Event 对象 | 是 | 是 | N/A
Mutex 对象 | 是 | 是 | 是
Semaphore 对象 | 是 | 是 | N/A


### Zero Copy

* Linux 上的：sendfile
* Windows 上的：TransmitFile


### x86 架构的包袱

* 复杂指令集 vs 精简指令集
* 思想差异：复杂问题是交给编译器，还是 CPU
* 指令不定长的问题
    * 我们的视角：反编译；
    * CPU 的视角：译码器效率、乱序执行效率


### Windows 注册表

* 本质上是一个有权限管理功能的 key value 存储
* 在文件系统未初始化的时候就可以读取
* 存储系统的配置（驱动项、服务项、COM、文件类型…）
* 注册表是多 hives 的集合

#### 对操作系统

* 相当于 grub3 中 ext3
* Bootmgr 在进系统前不需要文件系统支持
* 相当于给 kernel 使用的 ramfs
* Boot 类型的驱动在文件系统驱动加载前就可以读取到自己需要的配置

#### 对应用程序

* 一个 KV 数据库


### COM 组件

{% include image.html url="/assets/images/211120-windows-program/20211201010653.png" caption="COM 组件" %}


### 编程避坑不完全指引

* 多线程竞争问题（Cache、死锁等）
* 避免长时间高占用 CPU
* 需要频繁分配释放内存时使用内存池
* 注意内存映射的使用
* 避免对象（Handle）泄露，线程用完后揿毁
* 避免栈溢出（递归 vs 循环）
* Windows 上 xxx_s 函数
* 跨平台要考虑什么？（汇编、字节顺序，API 抽象）
* Wow64 的注册表、文件路径、Shell 扩展等
* 同一模块分配的内存、在同一模块内释放
* 尽可能顺序读写，避免大量随机读写
* 避免长时间高吞吐读写磁盘
* 少用黑魔法 (Undocumented API)
* 频繁的小任务可以用线程池管理
* 造轮子前要想清楚
* 不要在界面线程做和界面非相关的操作


## Windows 界面和窗口

1. **WTL: Windows Template Library**
    Windows Template Library，对 ATL 在窗口方面做相关扩展。它封装好多 Windows 控件，也做了很多扩展。
    1. 标准控制（编辑框，列表框，按钮等等）
    2. 公共控制（包括列表视图，树形视图，进度条，微调按钮）
    3. IE 控制（rebar，平面滚动条，日历等等）
    4. 命令条，菜单，和更新 UI 类
    5. 公共对话框
    6. 属性单和页类
    7. 框架窗口，MDI 框架和子框架，分隔条，可滚动的窗口
    8. 设备环境（DC）和 GDI 对象类（笔、刷子、位图等）
    9. 打印机及其信息和设备模式类
    10. 实用工具类：包括 CPoint, CRect, CSize, 和 CString 类

2. **ATL: Active Template Library（活动模板库）**
    ATL 是 ActiveX Template Library 的缩写，它是一套 C++ 模板库。
    ATL 是一个产生 C++/COM 代码的框架，就如同 C 语言是一个产生汇编代码的框架。

3. **STL 即 Standard Template Library（标准模板库）**
    STL 的代码从广义上讲分为三类：algorithm（算法）、container（容器）和 iterator（迭代器）。
    STL 是一些“容器”的集合，这些“容器”有 list, vector, set, map 等，STL 也是算法和其他一些组件的集合。
    就像放在蛋架上的鸡蛋不会滚到桌上，它们很安全，因此，在 STL 容器中的对象也很安全。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-11-20-windows-program.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/zh-cn/visualstudio/profiling/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/bb0194bd.html" %})
- [https://docs.microsoft.com/zh-cn/visualstudio/debugger/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/78bdc34e.html" %})
- [https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/98a18465.html" %})
