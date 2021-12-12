---
layout: post
title: "编程与调试 C++ -- 一些 Windows 编程笔记 & Windows 8.1 磁盘 100% 问题"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["开发环境", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## base64

[base62x {% include relref_github.html %}](https://github.com/wadelau/Base62x)
Base64 编码若无特别说明，通常约定非 ASCII 字符按照 UTF-8 字符集进行编码处理。
由于标准的 Base64 编码后可能出现字符 + 和 /，在 URL 中就不能直接作为参数，所以又有一种 "url safe" 的 base64 编码，其实就是把字符 + 和 / 分别变成 - 和 _。

由于 = 字符也可能出现在 Base64 编码中，但 = 用在 URL、Cookie 里面会造成歧义，所以，很多 Base64 编码后会把 = 去掉。

与 Base64 相比，Base32 具有许多优点 [from](https://www.qqxiuzi.cn/bianma/base.php)：
* 适合不区分大小写的文件系统，更利于人类口语交流或记忆。
* 结果可以用作文件名，因为它不包含路径分隔符 “/” 等符号。
* 排除了视觉上容易混淆的字符，因此可以准确的人工录入。（例如，RFC4648 符号集忽略了数字 “1”、“8”和“0”，因为它们可能与字母 “I”，“B”和“O”混淆）。
* 排除填充符号“=”的结果可以包含在 URL 中，而不编码任何字符。
Base32 也比 Base16 有优势：
* Base32 比 Base16 占用的空间更小。（1000 比特数据 Base32 需要 200 个字符，而 Base16 则为 250 个字符）
Base32 的缺点：
* Base32 比 Base64 多占用大约 20％的空间。因为 Base32 使用 8 个 ASCII 字符去编码原数据中的 5 个字节数据，而 Base64 是使用 4 个 ASCII 字符去编码原数据中的 3 个字节数据。


## bkwin 多屏幕支持 bugfix

主窗口在副屏幕，DoModal 弹窗会强制限制到主界面边缘，非常诡异。
后来发现迅雷也有这个 bug，看来迅雷也用了 bkwin 代码。SOUI 等从 bkwin 衍生出来的都存在这个问题（最新版本就不清楚了）。
* \*\*\src\GUI\publish\bkwin\bkdlgview.h
* \*\*\src\GUI\publish\bkwin\CBkDialogViewImplEx.h

```cpp
BOOL ThisCenterWindow(HWND hWndCenter = NULL) throw()
{
    ATLASSERT(::IsWindow(m_hWnd));

    // determine owner window to center against
    DWORD dwStyle = GetStyle();
    if (hWndCenter == NULL)
    {
        if (dwStyle & WS_CHILD)
            hWndCenter = ::GetParent(m_hWnd);
        else
            hWndCenter = ::GetWindow(m_hWnd, GW_OWNER);
    }

    // get coordinates of the window relative to its parent
    RECT rcDlg;
    ::GetWindowRect(m_hWnd, &rcDlg);
    RECT rcArea;
    RECT rcCenter;
    HWND hWndParent;
    if (!(dwStyle & WS_CHILD))
    {
        // don't center against invisible or minimized windows
        if (hWndCenter != NULL)
        {
            DWORD dwStyleCenter = ::GetWindowLong(hWndCenter, GWL_STYLE);
            if (!(dwStyleCenter & WS_VISIBLE) || (dwStyleCenter & WS_MINIMIZE))
                hWndCenter = NULL;
        }

        // center within screen coordinates
        ::SystemParametersInfo(SPI_GETWORKAREA, NULL, &rcArea, NULL);
        if (hWndCenter == NULL)
            rcCenter = rcArea;
        else
            ::GetWindowRect(hWndCenter, &rcCenter);
    }
    else
    {
        // center within parent client coordinates
        hWndParent = ::GetParent(m_hWnd);
        ATLASSERT(::IsWindow(hWndParent));

        ::GetClientRect(hWndParent, &rcArea);
        ATLASSERT(::IsWindow(hWndCenter));
        ::GetClientRect(hWndCenter, &rcCenter);
        ::MapWindowPoints(hWndCenter, hWndParent, (POINT*)&rcCenter, 2);
    }

    int DlgWidth = rcDlg.right - rcDlg.left;
    int DlgHeight = rcDlg.bottom - rcDlg.top;

    // find dialog's upper left based on rcCenter
    int xLeft = (rcCenter.left + rcCenter.right) / 2 - DlgWidth / 2;
    int yTop = (rcCenter.top + rcCenter.bottom) / 2 - DlgHeight / 2;

    // if the dialog is outside the screen, move it inside
    /** 这段代码，多屏幕的时候，就非常尴尬了，注释掉即可。
    if (xLeft < rcArea.left)
        xLeft = rcArea.left;
    else if (xLeft + DlgWidth > rcArea.right)
        xLeft = rcArea.right - DlgWidth;

    if (yTop < rcArea.top)
        yTop = rcArea.top;
    else if (yTop + DlgHeight > rcArea.bottom)
        yTop = rcArea.bottom - DlgHeight;
    */
    // map screen coordinates to child coordinates
    return ::SetWindowPos(m_hWnd, NULL, xLeft, yTop, -1, -1,
        SWP_NOSIZE | SWP_NOZORDER | SWP_NOACTIVATE);
}
```


## C 盘深度清理 —— 清理 FileRepository

DriverStoreExplorer 最新版下载：
<https://github.com/lostindark/DriverStoreExplorer/releases>


## Windows 命令行编码

设置 命令行 utf8，`chcp 65001`。`shutdown -r -t 0`。


## Windows 8.1 磁盘占用 100% 解决办法

<https://jingyan.baidu.com/article/9c69d48fbd146713c9024e04.html>
开机后磁盘占用高，是因为 windows 8.1 默认启用了 superfetch 服务。

[win8 硬盘占用率 100% 怎么办 \| win8 磁盘占用率过高的五种解决方法](http://www.xitongcheng.com/jiaocheng/win8_article_37723.html)


### 关闭家庭组

{% include image.html url="/assets/images/210228-win-prog-notes/15077896870508256831.jpg" %}

进入“计算机管理”后，展开“服务和应用程序”，点击“服务”，然后在右侧的服务列表里分别找到“HomeGroup Listener”与“HomeGroup Provider”服务，将其双击打开；

{% include image.html url="/assets/images/210228-win-prog-notes/150778968833207589663.jpg" %}

之后会弹出属性窗口，将“启动类型”设置为“禁用”，在服务状态下点击“停止”按钮，然后点击“确定”按钮进行保存，两项服务都禁用后就可以关闭家庭组了。

{% include image.html url="/assets/images/210228-win-prog-notes/150778968855082543091.jpg" %}


### 关闭虚拟内存

{% include image.html url="/assets/images/210228-win-prog-notes/1507789688910228795.jpg" %}
{% include image.html url="/assets/images/210228-win-prog-notes/150778968908207565786.jpg" %}

打开性能选项后，切换“高级”选项卡，点击虚拟内存处的“更改”按钮，在性能内存设置中，将“自动管理驱动器的分页文件大小”勾取消，选择“无分页文件”，然后点击“确定”；

{% include image.html url="/assets/images/210228-win-prog-notes/150778968967582538187.jpg" %}


### 关闭快速启动

{% include image.html url="/assets/images/210228-win-prog-notes/15077923003307.jpg" %}
{% include image.html url="/assets/images/210228-win-prog-notes/150778969133207550831.jpg" %}

点击“更改当前不可用的设置”，然后把“启用快速启动（推荐）”前面的勾取消，然后“保存设置”即可。

{% include image.html url="/assets/images/210228-win-prog-notes/15077896916289530141.jpg" %}


### 关闭 superfetch 服务

来到计算机管理后，在左侧展开“服务和应用程序”，点击“服务”，然后在右侧的服务列表里找到“Superfetch”服务，双击打开；

{% include image.html url="/assets/images/210228-win-prog-notes/150778969217582535798.jpg" %}

在弹出属性窗口，将“启动类型”设置为“禁用”，然后在服务状态下方点击“停止”按钮，然后“确定”即可。

{% include image.html url="/assets/images/210228-win-prog-notes/1507789692785266916.jpg" %}


### 关闭占用率过高进程

{% include image.html url="/assets/images/210228-win-prog-notes/15077896934414554890.jpg" %}

切换到“性能”选项卡，然后点击最下面的“打开资源监视器”；
查看“磁盘活动进程”下的名称和读、写的速度，看哪些进程在频繁读写；

{% include image.html url="/assets/images/210228-win-prog-notes/1507789693660286065.jpg" %}


## win10 开机壁纸保存的路径

`C:\Users\qzz\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets`

{% include image.html url="/assets/images/210228-win-prog-notes/20200717102249286.png" %}

将后缀名改为 .jpg 结尾即可查看。


## 系统的 INI 配置读写函数

这里要非常明确，搞不好就乱码了。

`WritePrivateProfileString`，`GetPrivateProfileString`，
If the file was created using Unicode characters,
the function writes Unicode characters to the file.
Otherwise, the function writes ANSI characters.


## D Profile 开源性能分析工具

[from](https://bbs.pediy.com/thread-195774.htm)
D Profile 是一个 win32/64 CPU，memory 性能分析工具：<https://github.com/xwlan/dprofiler>
D Profiler a lightweight, low overhead CPU Memory IO and Lock profiler for Windows x86/x64.
Build in cmd.exe, run command as: msbuild dprofiler.sln


## Windows Performance Toolkit

* WPT（Windows Performance Toolkit）是微软提供的一套用于分析程序性能的工具包，它其中包含两个主要的工具
    * WPR（Windows Performance Recorder）是一个事件记录工具，使用它可以监测系统状态（CPU、磁盘 I/O、堆分配、栈调用…），并生成一个 .etl（Event trace log）日志文件
    * WPA（Windows Performance Analyzer）是一个日志分析工具，使用它可以对 WPR 生成的 .etl 日志文件加以分析得出方便人阅读的数据图表



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-28-win-prog-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/wadelau/Base62x]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/deec4fed.html" %})
- [https://www.qqxiuzi.cn/bianma/base.php]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/www.qqxiuzi.cn/c9a5ff91.php" %})
- [https://github.com/lostindark/DriverStoreExplorer/releases]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/a03f4901.html" %})
- [https://jingyan.baidu.com/article/9c69d48fbd146713c9024e04.html]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/jingyan.baidu.com/484816be.html" %})
- [http://www.xitongcheng.com/jiaocheng/win8_article_37723.html]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/www.xitongcheng.com/eec8545c.html" %})
- [https://bbs.pediy.com/thread-195774.htm]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/bbs.pediy.com/10890851.htm" %})
- [https://github.com/xwlan/dprofiler]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/faf10891.html" %})
