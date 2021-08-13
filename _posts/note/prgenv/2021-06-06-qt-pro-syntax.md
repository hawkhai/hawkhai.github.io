---
layout: post
title: "编程配置 -- QT .Pro & .Pri 语法"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "QT"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

$$PWD 表示该工程的当前目录


## QtCreator


### Qt Widgets Application

使用 QtDesigner 窗体设计基于桌面和 c++ 实现应用程序逻辑的用户界面的 Qt 小部件。


### Qt Console Application

使用一个 main.cpp 文件


### Qt Quick Application

创建一个 Qt 快速应用程序包含 QML 和 c++ 代码。该项目包括一个 QQuickView。您可以构建应用程序并将其部署到桌面，嵌入式和移动目标平台。


### Qt Quick Controls Application

创建一个使用 Qt 快速控制 2（需要 Qt 5.7 或更高版本）或 Qt 快速控制的 Qt 快速应用程序。


### Qt Canvas 3D Application

创建一个引入 Qt3D 画布，可选择包括 three.js，的 Qt 快速应用程序模块。


### C++ Library

共享或静态基于 qmake 的 c++ 库


### Qt Quick 1 Extension Plugin

c++ 插件可以提供扩展，可以动态加载到 Qt 快速 1 应用程序通过使用 QDeclarativeEngine 类


### Qt Quick 2 Extension Plugin

c++ 插件可以提供扩展，可以动态加载到 Qt 快速 2 应用程序通过使用 QQmlEngine 类


### Qt Creator Plugin

创建一个自定义 QtCreator 的插件


## 模板

模板变量告诉 qmake 生成文件的类型等
```
TEMPLATE = app
```
具体参数如下：
* app：生成应用程序，即可执行文件
* lib：生成库文件
PS：只添加 TEMPLATE = lib 则生成动态库，若想生成静态库，则需要再添加多一条语句，详情如下：
```
TEMPLATE = lib
CONFIG += staticlib
```

* VPATH - 寻找补充文件的搜索路径。
* DEF_FILE - 只有 Windows 需要：应用程序所要连接的 .def 文件。
* RC_FILE - 只有 Windows 需要：应用程序的资源文件。
* RES_FILE - 只有 Windows 需要：应用程序所要连接的资源文件。


## 引入 lib 文件

```
LIBS += -L folderPath
```
-L 表示引入路径
eg.
```
Release:LIBS += -L folderPath // release 版引入的 lib 文件路径
Debug:LIBS += -L folderPath // Debug 版引入的 lib 文件路径
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-06-06-qt-pro-syntax.md.js" %}'></script></p>
