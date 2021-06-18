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


## MSB8040 Spectre-mitigated libraries are required for this project

原因：这是因为 Visual Studio 默认开启了缓解 Spectre 攻击的机制，所以就有两种解决方案，一种是生成解决方案时禁用 Spectre 缓解机制，另一种就是安装 Spectre 缓解机制。

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/cba0a101a07f41069348b597a794da84.jpg" caption="禁用 Spectre 缓解机制" %}
{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20190912103527364.png" caption="安装 Spectre 缓解机制" %}


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


## Windows 上通过 bat 避免 python 冲突

首先要把 path 里面的所有 python 路径移干净，避免命令行访问到。

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


## Android Studio

AndroidStudio 代码达到指定字符长度时自动换行。
1. 设置每行最大字符个数，超过这个数字 将会自动换行。
2. Line breaks 选中表示隐藏性保持断行。Ensure right margin is not exceeded 选中表示代码超过标准线 就自动换行。

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210211190104.png" %}
{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210211190127.png" %}


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


### ERROR: ABIs [arm64-v8a] are not supported for platform.

ERROR: ABIs [arm64-v8a] are not supported for platform.
Supported ABIs are [armeabi-v7a, x86].
Affected Modules: app

当我使用的 compileSdkVersion 19 时，就会报上面的错，改成 compileSdkVersion 26 就可以了。
说明不同的编译版本，它们所支持的平台不一样。

```
$(call import-add-path, $(LOCAL_PATH)) # 没有这一行，下面这行会报错。
$(call import-module, box2d)
```


### CMake & Gradle

```gradle
allprojects {
    repositories {
        maven { url "http://maven.aliyun.com/nexus/content/groups/public/" }
        maven { url "http://maven.aliyun.com/nexus/content/repositories/jcenter" }
        maven { url "https://dl.bintray.com/umsdk/release" }
        google()
        jcenter()
    }
}
```

```gradle
android {
    defaultConfig {
        externalNativeBuild {
            cmake {
                cppFlags "-std=c++11"
            }
        }
        ndk {
            abiFilters "armeabi-v7a", "arm64-v8a"
        }
    }

    externalNativeBuild {
        cmake {
            path "src/main/cpp/CMakeLists.txt"
            version "3.10.2"
        }
    }
}
```

```cmake
cmake_minimum_required(VERSION 3.4.1)

find_library(log-lib log)

add_library(native-lib SHARED native-lib.cpp)
target_link_libraries(native-lib ${log-lib})
```


### Android.mk & Gradle

[认识 Android.mk 和 Application.mk {% include relref_jianshu.html %}](https://www.jianshu.com/p/f23df3aa342c)
[Android: NDK 中的 Android.mk 和 Application.mk {% include relref_cnblogs.html %}](https://www.cnblogs.com/yongdaimi/p/12061298.html)

```gradle
android {
    defaultConfig {
        ndk {
            moduleName "gamedemo"
            abiFilters "armeabi-v7a", "arm64-v8a"
        }
    }

    externalNativeBuild {
        ndkBuild {
            path 'src/main/jni/Android.mk'
        }
    }
}
```

app/src/main/jni/Application.mk & Android.mk。like hawkhai/IrrGameDemo.git。

#### `Android.mk`

```
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_MODULE := calculator
LOCAL_SRC_FILES := calculator.c
LOCAL_C_INCLUDES := $(LOCAL_PATH)/irrlicht/include $(LOCAL_PATH)/SDL/include

LOCAL_LDLIBS := -llog
include $(BUILD_SHARED_LIBRARY)
```

```
# __android_log_print(ANDROID_LOG_INFO, "log", message);
# error: format string is not a string literal (potentially insecure) [-Werror,-Wformat-security]
# APP_CLAGS：列出编译器标识，在编译任何模块的 C 和 C++ 源文件时这些标志都会被传给编译器
# APP_CPPFLAGS：列出编译器标识，在编译任何模块的 C++ 源文件时这些标志都会被传给编译器
LOCAL_CFLAGS += -Wno-error=format-security -Wreturn-type
LOCAL_CPPFLAGS += -Wno-error=c++11-narrowing -Wno-error=format-security -Wreturn-type
# 增加对 异常 和 rtti 的支持
LOCAL_CPPFLAGS += -fexceptions -frtti
LOCAL_SHORT_COMMANDS := true # ndk 编译报 make (e=87): 参数错误
LOCAL_CFLAGS += -I$(LOCAL_PATH)/../../include/
```

#### `Application.mk`

```
NDK_TOOLCHAIN_VERSION := 4.9
APP_ABI := armeabi-v7a arm64-v8a # 这玩意貌似无效了。
APP_STL := stlport_static # 这个也不行了。c++_static/c++_shared
APP_PLATFORM := android-21
APP_CPPFLAGS += -fexceptions -frtti
```

```
APP_PLATFORM := android-10
APP_STL := c++_static
APP_SHORT_COMMANDS := true # ndk 编译报 make (e=87): 参数错误
APP_ABI := armeabi-v7a arm64-v8a # 感觉没用，尴尬。android/defaultConfig/ndk 里面指定才有用。
APP_CPPFLAGS += -Wno-error=format-security
APP_CFLAGS += -Wno-error=format-security
```


### Android Studio: “Error initializing ADB: Android Debug Bridge not found”

[Android Studio: “Error initializing ADB: Android Debug Bridge not found” 且找不到 Project Structure {% include relref_csdn.html %}](https://blog.csdn.net/dingxianding/article/details/106017010)

**删除了本地的 .idea 文件夹**，然后重启 Android Studio。

发生这种情况，估计是创建项目时，gitignore 中没有忽略 .idea 文件夹，导致 git 拉取项目后用的是别人项目的 .idea 文件夹。


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


## Visual Studio 设置 shader（CG、GLSL）语法提示及高亮和显示行号

[from {% include relref_csdn.html %}](https://blog.csdn.net/weixin_41330389/article/details/89319945)

* 工具，安装“扩展和更新”，“GLSL language integration”。
* 工具 –> “选项”，从左侧选项卡找到“GLSL language integration”，
    此时可以为指定类型文件编辑自定义的扩展名，注意多个扩展名之间用英文分号分隔，
    然后打开相关文件即可完成。
* 都搞完了，要重启一下系统。

{% include image.html url="/assets/images/201215-visual-studio-and-andro~6d/20210310222741.png" %}


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

- [https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/gclxry.com/43348a06.html" %})
- [https://blog.csdn.net/hellokandy/article/details/100931904]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/blog.csdn.net/e2e3de3c.html" %})
- [https://developer.android.com/r/studio-ui/ndk-dir]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/developer.android.com/a3b9e8b2.html" %})
- [http://maven.aliyun.com/nexus/content/groups/public/]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/maven.aliyun.com/f69c0880.html" %})
- [http://maven.aliyun.com/nexus/content/repositories/jcenter]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/maven.aliyun.com/e33967a3.html" %})
- [https://dl.bintray.com/umsdk/release]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/dl.bintray.com/2871e588.html" %})
- [https://www.jianshu.com/p/f23df3aa342c]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/www.jianshu.com/6a23ff97.html" %})
- [https://www.cnblogs.com/yongdaimi/p/12061298.html]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/www.cnblogs.com/a12e7578.html" %})
- [https://blog.csdn.net/dingxianding/article/details/106017010]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/blog.csdn.net/b7b79d7f.html" %})
- [https://zhuanlan.zhihu.com/p/77427951]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/zhuanlan.zhihu.com/bc1d4621.html" %})
- [https://blog.csdn.net/weixin_41330389/article/details/89319945]({% include relrefx.html url="/backup/2020-12-15-Visual-Studio-and-Android-Studio.md/blog.csdn.net/8fdc4aa4.html" %})
