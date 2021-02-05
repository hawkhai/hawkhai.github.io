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
visibility:
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

# NDK was located by using ndk.dir property.
# This method is deprecated and will be removed in a future release.
# Please delete ndk.dir from local.properties and set android.ndkVersion
# to [21.1.6352462] in all native modules in the project.
# https://developer.android.com/r/studio-ui/ndk-dir
# Affected Modules: app
ndk.dir=D\:\\Android\\Sdk\\ndk-bundle # 最新版已经不需要了。
```


### Android Studio: “Error initializing ADB: Android Debug Bridge not found”

[Android Studio: “Error initializing ADB: Android Debug Bridge not found” 且找不到 Project Structure {% include relref_csdn.html %}](https://blog.csdn.net/dingxianding/article/details/106017010)

**删除了本地的.idea文件夹**，然后重启 Android Studio。

发生这种情况，估计是创建项目时，gitignore 中没有忽略 .idea 文件夹，导致 git 拉取项目后用的是别人项目的 .idea 文件夹，这时候就会发生这种诡异的事。所以用 idea 开发的时候，一定要把 .idea 文件夹加到 gitignore 中哦！


### NDK 调试问题

#### The application could not be installed: INSTALL_FAILED_TEST_ONLY

在项目中的 gradle.properties 全局配置中设置：
`android.injected.testOnly=false`

#### Waiting For Debugger

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210205105349.png" %}

```gradle
buildTypes {
    debug {
        minifyEnabled false
        debuggable true
        jniDebuggable true
    }
}
```

* 勾上这两个，重启 IDE，就可以调试 Java 代码了，但是还是调试不了 C++ 代码。[android studio JNI 调试 （debug） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/77427951)

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210205110750.png" %}
{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210205110931.png" %}

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210205155832.png" %}

**巨坑。NDK 里面带了 python.exe，和本机的 python 冲突，`LLDB server` 成功起来后就好了。**

```
02/05 16:41:05: Launching 'app' on Galaxy Nexus API 30.
Install successfully finished in 680 ms.
$ adb shell am start -n "com.cfgame.myapp/com.cfgame.myapp.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -D
Waiting for application to come online: com.cfgame.myapp.test | com.cfgame.myapp
Waiting for application to come online: com.cfgame.myapp.test | com.cfgame.myapp
Waiting for application to come online: com.cfgame.myapp.test | com.cfgame.myapp
Connecting to com.cfgame.myapp
Now Launching Native Debug Session
$ adb shell cat /data/local/tmp/lldb-server | run-as com.cfgame.myapp sh -c 'cat > /data/data/com.cfgame.myapp/lldb/bin/lldb-server && chmod 700 /data/data/com.cfgame.myapp/lldb/bin/lldb-server'
$ adb shell cat /data/local/tmp/start_lldb_server.sh | run-as com.cfgame.myapp sh -c 'cat > /data/data/com.cfgame.myapp/lldb/bin/start_lldb_server.sh && chmod 700 /data/data/com.cfgame.myapp/lldb/bin/start_lldb_server.sh'
Starting LLDB server: /data/data/com.cfgame.myapp/lldb/bin/start_lldb_server.sh /data/data/com.cfgame.myapp/lldb unix-abstract /com.cfgame.myapp-0 platform-1612514467397.sock "lldb process:gdb-remote packets"

Executing commands in 'E:\android-studio-ide-181.5014246-windows\android-studio\bin\lldb\shared\stl_printers\load_script'.
(lldb) script import sys
(lldb) script import os
(lldb) script ...
```


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

- [https://developer.android.com/r/studio-ui/ndk-dir]({% include relref.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/developer.android.com/a3b9e8b2.html" %})
- [https://blog.csdn.net/dingxianding/article/details/106017010]({% include relref.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/blog.csdn.net/b7b79d7f.html" %})
- [https://zhuanlan.zhihu.com/p/77427951]({% include relref.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/zhuanlan.zhihu.com/bc1d4621.html" %})
