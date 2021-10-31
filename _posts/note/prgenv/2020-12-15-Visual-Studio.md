---
layout: post
title: "开发环境 -- Visual Studio 编程环境搭建"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "Visual Studio"
---


## VS2019 Release 版本调试

1. 链接器 -> 调试 -> 生成调试信息 /Debug -- 生成 pdb 调试信息。
2. C/C++ -> 常规 -> 调试信息格式 /Zi -- 这条容易漏掉，造成还是不能调试。
3. C/C++ -> 优化 -> 最大优化（优选速度） (/O2) -- 大量小函数会被内联，断点位置不准确。


## C2243 “类型强制转换”: 从“const MyMediaPlayer *”到“const QObject *”的转换存在，但无法访问

消息 查看对正在编译的函数 模板 实例化“QMetaObject::Connection QObject::connect<void(__thiscall MyMediaPlayer::\* )(QMediaPlayer::State),MediaPlayerWidget::{ctor}::<lambda_05c4b36ce79266e99b66673c2f7077b4>>(const MyMediaPlayer \*,Func1,Func2)”的引用 fastvcdemo E:\kpdf\fastvc\fastvcdemo\ui\mediaplayerwidget.cpp 56

错误 C2243 “类型强制转换”: 从“const MyMediaPlayer \*”到“const QObject \*”的转换存在，但无法访问 fastvcdemo D:\Qt\QTSetup\5.15.0\msvc2019\include\QtCore\qobject.h 316

**QT 中调用 connect 的时候出现的，解决方式为找到这个 QMyClass 的头文件，打开找到继承关系，看下是不是没有设置 public 继承，如果是的话，将导致链接错误，造成不能访问。**


## error MIDL2025/2026

使用 VC2005 编译出现这个错误
```
Include\unknwn.idl(108) : error MIDL2025 : syntax error : expecting ] or , near "annotation"
Include\unknwn.idl(108) : error MIDL2026 : cannot recover from earlier syntax errors;
aborting compilation
```

如果使用 VC2005 编译出现这个错误，是由于使用了新版本的 VISTA SDK 头文件，而使用旧版本的 MIDL 工具来编译所导致。
解决方法是安装 SDK 时，把它的 SDK 里带的编译工具也需要安装，然后在 VC 里
```
Tools > Options > Projects and Solutions > VC++ Directories > Executable Files
```
里添加这个 SDK 的 BIN 目录，这样就使用新版本的 MIDL 编译工具。


## error LNK2001: 无法解析的外部符号 "public: static struct QMetaObject const QwtPlot::staticMetaObject"

参数宏：`QWT_DLL`。


## MSB8040 Spectre-mitigated libraries are required for this project

原因：这是因为 Visual Studio 默认开启了缓解 Spectre 攻击的机制，所以就有两种解决方案，一种是生成解决方案时禁用 Spectre 缓解机制，另一种就是安装 Spectre 缓解机制。

{% include image.html url="/assets/images/201215-visual-studio/cba0a101a07f41069348b597a794da84.jpg" caption="禁用 Spectre 缓解机制" %}
{% include image.html url="/assets/images/201215-visual-studio/20190912103527364.png" caption="安装 Spectre 缓解机制" %}


## WTL 工程出现的 LINK 错误解决

VS2005 WTL 工程编译 Debug 无问题，编译 Release 时出现 Link 错误

```
1>正在链接 ...
1>LIBCMT.lib(tidtable.obj) : error LNK2005: __encode_pointer 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(tidtable.obj) : error LNK2005: __encoded_null 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(tidtable.obj) : error LNK2005: __decode_pointer 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(crt0dat.obj) : error LNK2005: __get_osplatform 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(crt0dat.obj) : error LNK2005: __osplatform 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(calloc.obj) : error LNK2005: _calloc 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(dosmap.obj) : error LNK2005: __errno 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(dosmap.obj) : error LNK2005: __set_errno 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(dosmap.obj) : error LNK2005: __get_errno 已经在 atlmincrt.lib(atlinit.obj) 中定义
1>LIBCMT.lib(crt0.obj) : error LNK2019: 无法解析的外部符号 _main，该符号在函数 ___tmainCRTStartup 中被引用
1>Release\KugouUIDemo.exe : fatal error LNK1120: 1 个无法解析的外部命令
```

解决方法：

属性页 -> 配置属性 -> 常规 -> 项目默认值 -> 在 ATL 中最小使用 CRT -> 否


## 使用 $err,hr 快速查看当前 GetLastError() 的值

调试时，在 `监视 1` 窗口（`Watch 1`）中输入 `$err,hr` 即可。
在 Visual C++ 中，可以在监视窗口添加 $err,hr 一行来实时显示错误。
调试过程中，该项相当于在每次调用 API 函数之后调用 GetLastError 函数。
其值由两部分组成，一个是错误代码（十六进制），另一个是错误代码所对应的文本提示。该方法支持多语言。

{% include image.html url="/assets/images/201215-visual-studio/78946-20160703182949937-342764345.png" %}

以 $ 和 @ 开头的伪变量（注：$ 和 @ 两个符号是一样的，随便用哪个都可以）：
* `$err` -- 获取 GetLastError() 的返回值
* `$err,hr` -- 获取 GetLastError() 的返回值并解释返回值的含义
* `@eax` -- 查看 eax 的值（64 位为 @rax）
* `@esp+4` -- 函数的第一个参数地址
* `$handles` -- 查看打开的句柄数
* `$tid`  -- 当前线程 id
* `$vframe`  -- 当前栈帧的 ebp
* `$clk`  -- 以时钟周期为单位显示时间
* `$ReturnValue` -- 查看函数的返回值
* `Message,wm` -- 以 windows 消息的宏形式显示 如：Message 为 15 时，显示为 WM_PAINT（注：Message 为 unsigned int 类型）
* `hResult,hr` -- hResult 为 0x80070005 时，显示为 E_ACCESSDENIED（注：hResult 为 void\* 类型）
* `pArray,10` -- 从 pArray 地址起显示后续 10 个 int 类型的数据（注：pArray 为 int\* 类型）
* `(pArray+5),3` -- 从 pArray[5] 地址起显示后续 3 个 int 类型的数据（注：pArray 为 int\* 类型）

[Visual Studio 高级调试技巧 {% include relref_cnblogs.html %}](https://www.cnblogs.com/huhewei/p/6080157.html)


## Windows 上通过 bat 避免 python 冲突

首先要把 path 里面的所有 python 路径移干净，避免命令行访问到。
`D:\kSource\pythonx\winenv.py`

[from](https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/)
python3.bat 的文件，放到 C:\Windows 目录中，python3.bat 的内容如下：
```bat
@echo off
setlocal
set PATH=%PATH%;%~dp0;
C:\Users\john\AppData\Local\Programs\Python\Python37-32\python.exe %*
```

pip.bat
```bat
@echo off
setlocal
set PATH=%PATH%;%~dp0;C:\Users\john\AppData\Local\Programs\Python\Python37-32\Scripts
C:\Users\john\AppData\Local\Programs\Python\Python37-32\Scripts\pip.exe %*
```


## 错误 RC1015 cannot open include file 'afxres.h'.

Or, if you don't want to install MFC, you can replace the line:
```cpp
#include "afxres.h"
```
with:
```cpp
#include <windows.h>
#include <winres.h>
```


## namespace "ATL" 没有成员 AtlGetCommCtrlVersion

vs 工程使用了 wtl-80，提示 namespace "ATL" 没有成员 AtlGetCommCtrlVersion

[namespace "ATL" 没有成员 AtlGetCommCtrlVersion {% include relref_csdn.html %}](https://blog.csdn.net/hellokandy/article/details/100931904)


## VS 没有生成 lib 库

* Lib 生成路径设置不对。
* 宏定义不对。在 debug 里有个预定义，在 release 忘记预定义了，导致 __declspec( dllexport ) 没有生效，没有导出函数，就没有导出库 .lib


## error MSB3073: 命令“... :VCEnd”已退出，代码为 4。

```
1>MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(153,5): error MSB3073: 命令“
1>    if not exist E:\Android\cfwpe\cfwpe\..\..\product mkdir E:\Android\cfwpe\cfwpe\..\..\product
1>    xcopy /v /y /f E:\Android\Debug\cfwpen.* E:\Android\cfwpe\cfwpe\..\..\product
1>    xcopy /v /y /f E:\Android\cfwpe\cfwpe\include\irrKlang\bin\*.* E:\Android\Debug\
1>    xcopy /v /y /f E:\Android\cfwpe\cfwpe\include\irrKlang\bin\*.* E:\Android\cfwpe\cfwpe\..\..\product
1>    :VCEnd”已退出，代码为 4。
```

命令列表中，某个命令返回失败了。比如：xcopy 的 源文件或者文件夹不存在。


## Visual Studio 设置 shader（CG、GLSL）语法提示及高亮和显示行号

[from {% include relref_csdn.html %}](https://blog.csdn.net/weixin_41330389/article/details/89319945)

* 工具，安装“扩展和更新”，“GLSL language integration”。
* 工具 –> “选项”，从左侧选项卡找到“GLSL language integration”，
    此时可以为指定类型文件编辑自定义的扩展名，注意多个扩展名之间用英文分号分隔，
    然后打开相关文件即可完成。
* 都搞完了，要重启一下系统。

{% include image.html url="/assets/images/201215-visual-studio/20210310222741.png" %}


## 字体和空格

工具 > 选项。

{% include image.html url="/assets/images/201215-visual-studio/20201215204249.png" %}

工具 > 选项 > 文本编辑器 > 所有语言 > 制表符。

{% include image.html url="/assets/images/201215-visual-studio/20201215204539.png" %}

而在 vs2019 中这么设置却没有生效。需要修改参数，取消“使用自适应格式”，位置在工具，选项，文本编辑器，高级。

To turn off this behavior, please go to Tools > Options, and then Text Editor > Advanced > Uncheck "Use adaptive formatting".

{% include image.html url="/assets/images/201215-visual-studio/20200403181502106.png" %}

VS Code 设置 tab 缩进无效。
VS Code 找到 文件 > 首选项 > 设置 中搜索 editor.tabSize，在用户设置中设置缩进量，但是有时会出现设置后无效的情况，解决办法：
文件 > 首选项 > 设置 中搜索 detectIndentation，将值设置为 false（即关闭自动检测功能），就可以正常使用用户设置里面的 tab 缩进啦。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-15-Visual-Studio.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/huhewei/p/6080157.html]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio.md/www.cnblogs.com/38d5910a.html" %})
- [https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio.md/gclxry.com/43348a06.html" %})
- [https://blog.csdn.net/hellokandy/article/details/100931904]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio.md/blog.csdn.net/e2e3de3c.html" %})
- [https://blog.csdn.net/weixin_41330389/article/details/89319945]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio.md/blog.csdn.net/8fdc4aa4.html" %})