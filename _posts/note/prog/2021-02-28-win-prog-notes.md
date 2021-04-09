---
layout: post
title: "编程 C++ -- 一些 Windows Program Notes"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## Windows 命令行编码

设置 命令行 utf8，`chcp 65001`。`shutdown -r -t 0`。


## Windows 8.1 磁盘占用 100% 解决办法

<https://jingyan.baidu.com/article/9c69d48fbd146713c9024e04.html>
开机后磁盘占用高，是因为 windows 8.1 默认启用了 superfetch 服务。


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

- [https://jingyan.baidu.com/article/9c69d48fbd146713c9024e04.html]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/jingyan.baidu.com/484816be.html" %})
- [https://bbs.pediy.com/thread-195774.htm]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/bbs.pediy.com/10890851.htm" %})
- [https://github.com/xwlan/dprofiler]({% include relrefx.html url="/backup/2021-02-28-win-prog-notes.md/github.com/faf10891.html" %})
