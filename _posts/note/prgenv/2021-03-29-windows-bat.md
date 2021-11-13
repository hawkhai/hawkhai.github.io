---
layout: post
title: "编程与调试 -- Windows 批处理（bat）语法大全"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "BAT"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
archived: true
---

[Windows 批处理 (bat) 语法大全 {% include relref_csdn.html %}](https://blog.csdn.net/qq_36838191/article/details/83046599)


## 基础语法

1. 批处理文件是一个“.bat”结尾的文本文件，这个文件的每一行都是一条 DOS 命令。可以使用任何文本文件编辑工具创建和修改。
2. 批处理是一种简单的程序，可以用 if 和 goto 来控制流程，也可以使用 for 循环。
3. 批处理的编程能力远不如 C 语言等编程语言，也十分不规范。
4. 每个编写好的批处理文件都相当于一个 DOS 的外部命令，把它所在的目录放到 DOS 搜索路径 (path) 中，即可在任意位置运行。
5. C:\AUTOEXEC.BAT 是每次系统启动时都会自动运行的，可以将每次启动时都要运行的命令放入该文件中。
6. 大小写不敏感（命令符忽略大小写）
7. 批处理的文件扩展名为 .bat 或 .cmd。
8. 在命令提示下键入批处理文件的名称，或者双击该批处理文件，系统就会调用 Cmd.exe 来运行该文件。


### %~dp0[获取当前路径]

* %~dp0 “d”为 Drive 的缩写，即为驱动器、磁盘；“p”为 Path 缩写，即为路径、目录。
* cd %~dp0 ：进入批处理所在目录
* cd %~dp0bin\ ：进入批处理所在目录的 bin 目录


### 传递参数给批处理文件

%[1-9] 表示参数，参数是指在运行批处理文件时在文件名后加的以空格（或者 Tab）分隔的字符串。

变量可以从 %0 到 %9，%0 表示批处理命令本身，其它参数字符串用 %1 到 %9 顺序表示。

Sample：

```
call test2.bat "hello" "haha" （执行同目录下的“test2.bat”文件，并输入两个参数）
```

在“test2.bat”文件里写 :

```
echo %1 ( 打印: "hello")
echo %2 ( 打印: "haha")
echo %0 ( 打印: test2.bat)
echo %19 ( 打印: "hello"9)
```


### Echo 命令

```
Sample： echo off
Sample： echo hello world ( 显示出“hello world”)
Sample： echo Windows Registry Editor Version 5.00 > c:\setupreg.reg （此前还没有 setupreg.reg 这个文件）
Sample： echo "SourcePath"="D:\\Win2003\\" >> c:\setupreg.reg （追加内容进 setupreg.reg 这个文件）
```


### 比较运算符

* EQU - 等于（一般使用“==”）
* NEQ - 不等于（没有 “!=”，改用“ if not 1==1 ”的写法）
* LSS - 小于
* LEQ - 小于或等于
* GTR - 大于
* GEQ - 大于或等于



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-29-windows-bat.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/qq_36838191/article/details/83046599]({% include relrefx.html url="/backup/2021-03-29-windows-bat.md/blog.csdn.net/d1b7bb3a.html" %})
