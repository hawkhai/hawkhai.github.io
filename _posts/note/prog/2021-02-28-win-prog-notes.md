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

- [https://github.com/lostindark/DriverStoreExplorer/releases]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/a03f4901.html" %})
- [https://jingyan.baidu.com/article/9c69d48fbd146713c9024e04.html]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/jingyan.baidu.com/484816be.html" %})
- [http://www.xitongcheng.com/jiaocheng/win8_article_37723.html]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/www.xitongcheng.com/eec8545c.html" %})
- [https://bbs.pediy.com/thread-195774.htm]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/bbs.pediy.com/10890851.htm" %})
- [https://github.com/xwlan/dprofiler]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/faf10891.html" %})
