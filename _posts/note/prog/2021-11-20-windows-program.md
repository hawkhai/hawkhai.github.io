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
visibility:
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

反调试手段 IsDebuggerPresent

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

{% include image.html url="/assets/images/211120-windows-program/20211206130243.png" %}


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


## GDI 绘制系统与动画

{% include image.html url="/assets/images/211120-windows-program/20211205230522.png" caption="WINDOWS GRAPHICS ARCHITECTURE" %}


### GDI 对象的上限

There is a theoretical limit of 65,536 GDI handles per session.
However, the maximum number of GDI handles that can be opened per session is usually lower, since it is affected by available memory.
There is also a default per-process limit of GDI handles.
To change this limit, set the following registry value: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows\GDIProc` `essHandleQuota` This value can be set to a number between 256 and 65,536.


### 句柄泄露

所有的 GDI 对象，在使用完成后，都需要调用删除，否则就会出现泄露问题 DeleteObject、ReleaseDC


### GDI 的继任者：GDI+

GDI+ is an API that is exposed through a set of C++ classes. programmers of new applications should use
GDI+ for all their graphics needs because GDI+ optimizes many of the capabilities of GDI and also provides
additional features.


### GETTING STARTED

```cpp
#include <gdiplus.h>
using namespace Gdiplus;
#pragma comment(lib, "Gdiplus.lib")
INT WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, PSTR, INT iCmdShow)
{
    // Initialize GDI+.
    GdiplusStartupInput gdiplusStartupInput;
    ULONG_PTR gdiplusToken;
    GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);
    // working with GDI+.
    // Shutdown GDI+
    GdiplusShutdown(gdiplusToken);
}
```


### WHAT’S NEWS

* Gradient Brushes（渐变笔刷）
* Cardinal Splines（曲线拟合）
* Independent Path Objects（Path 对象的生命周期延长）
* Transformations and the Matrix Object（矩阵变换，旋转、缩放、平移）
* Scalable Regions（区域也可以进行缩放变换了）
* Alpha Blending（颜色混合）
* Support for Multiple Image Formats（图片格式支持：BMP\PNG\JPEG\ICON\GIF...）


## 模块和 COM 组件


### DllMain

函数调用过程中有 ldr 锁，建议尽量不要做逻辑。
下面逻辑会触发 ldr 锁，确认不能在 dllmain 里面做以下事情：
* 调用 LoadLibrary(Ex)
* 使用 CoInitializeEx
* 使用 CreateProcess
* 使用 User32 或 Gdi32 中的函数
* 与其他线程同步执行
* 注意以上行为，间接调用也会引起，所以谨慎起见，尽量不用任何封装好的代码，除非你非常确认代码不会触发任何 ldr 锁。


### 原生 com 四个导出函数

* DllCanUnloadNow // 判断 dll 是否可以释放（引用计数是否为 0）
* DllGetClassObject // 获取接口类指针
* DllRegisterServer // 写注册表，注册为 com 组件，供任何人使用
* DllUnregisterServer // 删注册表，反注册


## 字符串编码和操作


### ASCII /ˈæskiː/

（American Standard Code for Information Interchange）
编码起源于电报码，1960 年 10 月 6 日，美国标准协会（ANSI）的 X3.2 小组委员
会举行第一次会议，开始了关于 ASCII 标准制定。第一版 ASCII 标准于 1963 年发
布，在 1967 年经历了重大修改，在 1986 年期间经历了最近一次更新。ASCII 开始
基于英语字母表，将指定的 128 个字符编码成 7 位的二进制整数。其中 95 个编码
字符是可以打印的，包括数字 0-9，小写字母 a-z，大写字母 A-Z，还有一些标点
符号。


### ISO-8859-1

ISO-8859-1 编码是单字节编码（8bit），向下兼容 ASCII，其编码范围是
0x00-0xFF，0x00-0x7F 之间完全和 ASCII 一致，0x80-0x9F 之间未定义，
0xA0-0xFF 之间主要是拉丁字母和符号。
此字符集广泛应用于欧洲地区国家，支持英语、丹麦、德语、西班牙语、
法语、冰岛语等。Windows 补全该编码中的未使用字符，形成自己的编码
Windows-1252（code page 1252）


### Unicode

Unicode 是一种计算机行业统一编码标准，其起源是为了解决各国编码之
间的不兼容问题，创始人之一 Joe Becker 说为其取名‘Unicode’是为了表
明这是一种唯一的 (unique)，统一的 (unified)，通用的 (universal ) 编码。
Unicode 最初设计使用 16 位二进制来表示所有语言中的字符，因为当时所
有报纸和杂志的现代文字总和小于 2^14 = 16,384 。1991 年 3 月，Unicode 联
盟在加利福尼亚成立，10 月，发布 Unicode 1.0。

Unicode 的发展
* 1996 年发布 Unicode 2.0，加入了代理
字符机制 (Surrogate Characters
Mechanism)，将码域增加到了 100 多万，
Unicode 不在局限于 16 位。
* 2000 年以后，Unicode 基本保持一年一
更的节奏，截止到 2020 年最新发布的
Unicode 10.0，已经拥有 143,859 个字
符。

{% include image.html url="/assets/images/211120-windows-program/page16_1.jpg" caption="码域划分（Unicode 平面）" %}

{% include image.html url="/assets/images/211120-windows-program/20211210235106.png" caption="代理字符机制" width="75%" %}


### 编码方法

Unicode 定义了两种类型的编码方法：Unicode Transformation Format (UTF)
和 Universal Coded Character Set (UCS)
1. UTF 编码有 UTF-8、UTF-16、UTF-32
2. UCS 编码有 UCS-2，UCS-4
3. Windows 上的 ANSI 编码


### UTF-16

UTF-16(16-bit Unicode Transformation Format)，是一种可变长编码，用
1 或 2 个 16 位（2 字节）代码单元进行编码。UTF-16 是从早期的 16 位定长编
码 UCS-2 发展而来，由于 16 位最多只能编码 65,536 个字符，随着需要使用的
字符越来越多，这明显不够用。于是 IEEE（Institute of Electrical and
Electronics Engineers，电气与电子工程师协会）提出了 UCS-4 方案，用 4 字
节编码一个字符。Unicode 联盟觉得这个方案扯淡，因为这会浪费很多磁
盘空间，而且很多厂商已经投入大量资源基于 2 字节进行技术开发。最终
UTF-16 作为一个折中方案在 Unicode 2.0 标准中发布。

BMP:
* U+0000~U+D7FF 和 U+E000~U+FFFF（中间刚好缺少了 U+D800~U+DFFF，用于“代理字符机制”）
* 2 字节编码一个码点，直接前面补 0 即可。

SP:
* U+10000~U+10FFFF
* 码点个数：0x100000

假设 Unicode 码点 U，范围是（U+10000 ~ U+10FFFF）
* U 减去 0x10000 得到 range：0x00000 ~ 0xFFFFF
* 0xFFFFF 拆成两半 0x3ff & 0x3ff
* 分别加上“代理字符机制”，就是 高位：0xD800 ~ 0xDBFF，低位：0xDC00 ~ 0xDFFF

{% include image.html url="/assets/images/211120-windows-program/page22_1.jpg" width="50%" %}

```
Unicode 字符：U+10437
先减去 0x10000，结果为 0x0437，转成 20 位二进制：0000000001 0000110111
高位：0x0001 + 0xD800 = 0xD801
低位：0x0037 + 0xDC00 = 0xDC37
所以 UTF-16 编码为：0xD801DC37
```

UTF-16 的一个代码单元是 2 字节，由于大多数通信协议和存储协议都是以字
节单位，于是在存储 UTF-16 序列的时候就需要选择字节序。为了便于识别
字节序，UTF-16 引入了 BOM(Byte Order Mark)，插入在第一个实际代码
值之前。U+FEFF（零宽度不间断空格，啥也不是）表示大端，U+FFFE（非
字符）表示小端。UTF-16 规定如果缺少 BOM 头，应假设字节序为大端。

但事实上，因为 windows 默认使用小端，所以很多软件也默认使用小端，
平台的力量还是大。

特点：
* 可变长编码
* 不兼容 ASCII 编码
* 不可编码代理位


### UTF-8

UTF-8 是一种可变长编码，使用 1-4 字节（8 位）编码所有 Unidcode 字符。与
ASCII 兼容，Unicode 前 128 个字符与 ASCII 是一一对应的，UTF-8 使用一字
节对其进行编码，并且在二进制值上与 ASCII 一样。UTF-8 已经成为了万维
网上的主导编码，截止到 2020 年，95% 网页使用 UTF-8 编码。IMC 推荐所有
的 e-mail 程序使用 UTF-8 展示和创建邮件，W3C 推荐将 UTF-8 作为 XML 和
HTML 的默认编码。

{% include image.html url="/assets/images/211120-windows-program/page30_1.jpg" width="75%" %}

{% include image.html url="/assets/images/211120-windows-program/20211211001552.png" caption="编码方式" %}

UTF-8 编码的最小代码值单元是 1 字节，所以不存在字节序问题。但是很多
Windows 程序（Windows 记事本）会在以 UTF-8 保存的文件最前加上 0xEF, 0xBB, 0xBF，这个通常称为 BOM 头。

优势：
* 兼容 ASCII
* **字符边界容易识别**
* 小于 U+0080 的编码只需一个字节
* 不用考虑字节序问题
* **相比 UTF-16 容错性更强**

劣势：
* 编码 U+0800-U+FFFF 需要 3 字节


### ANSI

ANSI 编码没有明确定义，但通常被用来指代 Windows 代码页（Windows code page），在英文系统上通常指 Windows-1252 代码页，在简体中文系统通常
指 Windows-936（在不同的 windows 系统上，可能指代不同的代码页）。事实上，
“ANSI编码”这个名字是个错误用法，应为 ANSI 从来没有发表过这样的标准。

**Windows-1252**：
别名 CP-1252，用一个字节，总共编码 256 个字符，在英文和一些西方的
Windows 系统上作为默认编码。

**Windows-936**：
别名 CP-936，是 Windows 系统为简体中文设计的编码，最初只覆盖 GB2312 中
的字符，但是随着 Window95 的发布，被扩展到覆盖大部分的 GBK。

{% include image.html url="/assets/images/211120-windows-program/page36_2.jpg" caption="更改默认 Code Page" width="50%" %}


### Windows-936

第一部分：使用 1 个字节编码，0x00-0x80 和 0xff。总共编码 130 个字符，
前 128 个字符和 ASCII 兼容。

第二部分：使用 2 个字节编码，一个 lead byte（首字节），一个 trail
byte（尾字节），lead byte 范围：0x81-0xfe（125），trail byte 范围：
0x40-0xfe（190），总共编码字符：23750


### 编码转换

```cpp
MultiByteToWideChar // UTF-16 转 UTF-8 或者 ANSI
WideCharToMultiByte // UTF-16 转 UTF-8 或者 ANSI
CA2W // MultiByteToWideChar
CW2A // WideCharToMultiByte
CStringA sa;
CString s = sa; // 危险（ANSI）
```

#### WritePrivateProfileString

INI 文件读写 API：WritePrivateProfileString
1. MSDN：文件不存在就创建，使用 ANSI 编码；如果存在 Unicode 编码文件，则
写入 Unicode 字符。
2. 这里的 Unicode 编码实际指：UTF-16 编码（小端）

#### Windows 记事本“另存为”中的编码

* ANSI，不同版本系统不一样，同一系统不同设置也不一样。
* Unicode，实际指代的是 UTF-16（小端）。
* Unicode big endian，实际是 UTF-16（大端）
* UTF-8，实际是带 BOM 头的 UTF-8 编码

Windows 记事本中输入“连”，ctrl+s 保存后再打开。
文件内容 16 进制为：0xC1AC，转成二进制：1100 0001 1010 1100，命中
UTF-8 的两字节编码规则 (110xxxxx 10xxxxxx)，被识别成 UTF-8 编码。
当做 UTF-8 解码，得到 U+6C，但是不在 U+0080-U+07FF 之间，被当做错误
编码。
> ANSI 编码，但是二进制能命中 UTF8 规则，但是又找不到 UTF8 对应的字符。


## 注册表与权限


### 注册表介绍

Windows 目录中 system.dat、user.dat 和 config.pol 文件 (regedit.exe)

除了 HKEY_CURRENT_USER 之外的所有支持文件都保存在 C:\Windows\System32\config。
HKEY_CURRENT_USER 的支持文件存储在您的个人资料文件夹中，%UserProfile%\Ntuser.dat

* HKEY_CLASSES_ROOT
* HKEY_CURRENT_USER
* HKEY_LOCAL_MACHINE
* HKEY_USERS
* HKEY_CURRENT_CONFIG
* HKEY_DYN_DATA

显示类型（在编辑器中） | 数据类型 | 说明
---- | ---- | ----
REG_SZ | 字符串 | 文本字符串
REG_MULTI_SZ | 多字符串 | 含有多个文本值的字符串
REG_BINARY | 二进制数 | 二进制值，以十六进制显示
REG_DWORD | 双字 | 一个 32 位的二进制值
REG_QWORD | 四字 | 一个 64 位的二进制值


### 注册表操作


### 权限管理

* **普通用户** 可以操作 HKEY_CURRENT_USER，无法操作 HKEY_LOCAL_MACHINE
* **管理员** 可以操作 HKEY_CURRENT_USER、HKEY_LOCAL_MACHINE
* **服务** 可以操作 HKEY_LOCAL_MACHINE，操作 HKEY_CURRENT_USER 需要获取模拟当前用户，或者获取当前用户的 id，读取 HKEY_USER 下面的值


### 什么是 UAC

#### 概念

UAC 是 User Account Control 的缩写，其中文翻译为用户帐户控制，是微软在 Windows Vista 和 Win7 中引用的新技术，主要功能是进行一些会影响系统安全的操作时，会自动触发 UAC，用户确认后才能执行，从而保证系统安全。

触发 UAC 提示的操作：
* 修改 Windows Update 配置
* 增加或删除用户帐户
* 改变用户的帐户类型
* 改变 UAC 设置
* 安装 ActiveX
* 安装或卸载程序
* 安装设备驱动程序
* 修改和设置家长控制
* 增加或修改注册表
* 将文件移动或复制到 Program Files 或是 Windows 目录

#### UAC 的级别

最低的级别（0 级）：关闭 UAC 功能（必须重新启动后才能生效）。在该级别下，如果是以管理员登录，则所有操作都将直接运行而不会有任何通知，包括病毒或木马对系统进行的修改。在此级别下，病毒或木马可以任意连接访问网络中的其他电脑、甚至与互联网上的电脑进行通信或数据传输。可见如果完全关闭 UAC 并以管理员身份登录，将严重降低系统安全性。此外，如果是以标准用户登录，那么安装、升级软件或对系统进行修改和设置，将直接被拒绝而不弹出任何提示，用户只有获得管理员权限才能进行。可见完全关闭 UAC 并以标准用户登录，各种操作和设置也非常不方便，因此建议不要选择该级别。

比默认级别稍低的级别（1 级）：该级别不启用安全桌面，也就是说有可能产生绕过 UAC 更改系统设置的情况。不过一般情况下，如果是用户启动某些程序而需要对系统进行修改，可以直接运行，不会产生安全问题。但如果用户没有运行任何程序却弹出提示窗口，则有可能是恶意程序在试图修改系统设置，此时应果断选择阻止。该级别适用于有一定系统经验的用户。

默认级别（2 级）：在默认级别下，只有在应用程序试图改变计算机设置时才会提示用户，而用户主动对 Windows 进行更改设置则不会提示。同时，在该模式下将启用安全桌面，以防绕过 UAC 更改系统设置。可以看出，默认级别可以既不干扰用户的正常操作，又可以有效防范恶意程序在用户不知情的情况下修改系统设置。一般的用户都可以采用该级别设置。

最高级别（3 级）：在高级级别下，“始终通知”（即完全开启），在该级别下，用户安装应用程序、对软件进行升级、应用程序在任何情况下对操作系统进行更改、更改 Windows 设置等情况，都会弹出提示窗口（并启用安全桌面），请求用户确认。由此可见该级别是最安全的级别，但同时也是最“麻烦”的级别，适用于多人共用一台电脑的情况下，限制其他标准用户，禁止其随意更改系统设置。

#### 为什么需要 UAC

这里需要说到一个概念：Host-based Intrusion Prevention System HIPS，基于主机的入侵防御系统。HIPS 是一种系统控制软件，它能监控电脑中文件的运行，对文件的调用，以及对注册表的修改。HIPS 可以分为 3D，AD(Application Defend)--应用程序防御体系、RD(Registry Defend) 注册表防御体系、FD(File Defend）文件防御体系。UAC 可以理解为一个基础的 HIPS 防御系统。杀毒软件的更新永远要追着病毒来，这种滞后性使得病毒有机会利用时间差攻击系统；而对杀毒软件而言，亡羊补牢就意味着重大的失败。这种情况下，要谋求更高的安全性，HIPS 成为了当然之选。

#### UAC 与兼容性

经常有人抱怨 NT6.x 系统的兼容性多么多么差，身边也有人因为“不兼容”而将系统换回 XP。但从我个人的使用看，几乎所有的软件都能很好的工作于 NT6.x 上。区别在哪？排除掉确实因为软件开发导致的兼容性问题的话，普通用户只会双击运行程序，而我在一次尝试失败后会根据程序行为对其进行手动提权。刚从 XP 过来的用户，估计不会有那么一套权限划分的意识，UAC 在某种程度上而言也就削弱了系统对普通用户的兼容性。但我们如果能够根据程序行为对需要的程序进行手动提权，所谓“兼容性问题”也就迎刃而解了。对用户水平更高的需求？也许吧。但计算机从来都是与永无休止的学习联系在一起的。而如果程序的开发能进一步的规范化，内置提权申请的程序就不存在被 UAC 影响兼容性的问题了。

#### UAC bypass

[ref](https://twiki.cmcm.com/display/DUBA/UAC+bypass)
[ref {% include relref_github.html %}](https://0x00-0x00.github.io/research/2018/10/31/How-to-bypass-UAC-in-newer-Windows-versions.html)
目前公开的方法中，有以下几种方法绕过 UAC：
* 白名单提权机制
* DLL 劫持
* Windows 自身漏洞提权
* 远程注入
* COM 接口技术

针对新版 win10 有效的绕过 UAC 的几种方案 [UAC-bypass.md]

#### 高低权限通信问题

服务和管理员、普通用户无法进行消息通信，需要做特殊过滤
ChangeWindowMessageFilter
* 普通用户无法操作 C:\Program Files (x86)，会访问 `C:\Users\当前登录计算机用户名\AppData\Local\VirtualStore\Program Files\下目录的的文本文件`，需要加特殊过滤。


### 注册表优化


### 个性化设置

用作开机标识的注册表
{% include image.html url="/assets/images/211120-windows-program/page46_1.jpg" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-11-20-windows-program.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/zh-cn/visualstudio/profiling/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/bb0194bd.html" %})
- [https://docs.microsoft.com/zh-cn/visualstudio/debugger/?view=vs-2019]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/78bdc34e.html" %})
- [https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/getting-started-with-windbg]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/docs.microsoft.com/98a18465.html" %})
- [https://0x00-0x00.github.io/research/2018/10/31/How-to-bypass-UAC-in-newer-Windows-versions.html]({% include relrefx.html url="/backup/2021-11-20-windows-program.md/0x00-0x00.github.io/33c60558.html" %})
