---
layout: post
title: "开发环境 -- Visual Studio 与 Android Studio 编程环境搭建"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "Android"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## Android Studio


### CreateProcess error = 2，系统找不到指定的文件

local.properties 不完整，造成的问题。

```
sdk.dir=D\:\\Android\\Sdk
ndk.dir=D\:\\Android\\Sdk\\ndk-bundle
```


### NDK 调试问题

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20180902012723348.jpg" %}

<https://developer.android.com/studio/projects/install-ndk>


## Windows 命令行编码

设置 命令行 utf8，`chcp 65001`。


## 字体和空格

工具 > 选项。

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20201215204249.png" %}

工具 > 选项 > 文本编辑器 > 所有语言 > 制表符。

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20201215204539.png" %}

而在 vs2019 中这么设置却没有生效。需要修改参数，取消“使用自适应格式”，位置在工具，选项，文本编辑器，高级。

To turn off this behavior, please go to Tools > Options, and then Text Editor > Advanced > Uncheck "Use adaptive formatting".

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20200403181502106.png" %}

VS Code 设置 tab 缩进无效。
VS Code 找到 文件 > 首选项 > 设置 中搜索 editor.tabSize，在用户设置中设置缩进量，但是有时会出现设置后无效的情况，解决办法：
文件 > 首选项 > 设置 中搜索 detectIndentation，将值设置为 false（即关闭自动检测功能），就可以正常使用用户设置里面的 tab 缩进啦。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-15-Visual-Studio-and-Android-Studio.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://developer.android.com/studio/projects/install-ndk]({% include relref.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/developer.android.com/6fc38ff6.html" %})
