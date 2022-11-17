---
layout: post
title: "开发环境 -- Android Studio 编程环境搭建"
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


## 反编译

apktool+dex2jar+jd-gui 一直是一个比较流行的 Android 反编译组合。
在使用过 jadx 之后觉得 jadx 相比上面的组合具有如下两个优点：
* 可以直接反编译出 .java 文件
* 查看源码时直接显示资源名称，而不是像 jd-gui 里显示的资源 ID

* [Apktool {% include relref_github.html %}](https://ibotpeaches.github.io/Apktool/) apktool_2.6.1.jar
    * 通过该工具能完整的从 apk 中提取出 resource、dex、manifest、xml 等文件，也可以修改资源文件之后 rebuild 一个 apk。
* [JD-GUI {% include relref_github.html %}](http://java-decompiler.github.io/) jd-gui-windows-1.6.6.zip
    * 通过该工具，可以通过可视化的界面操作查看第二步生成的 jar 文件，即查看反编译后的源码情况。
* [dex2jar {% include relref_github.html %}](https://github.com/pxb1988/dex2jar) dex-tools-2.2-SNAPSHOT-2021-10-31.zip
    * 通过该工具将 dex 文件变成一个（包含 class 文件的）jar 文件。
* [jadx {% include relref_github.html %}](https://github.com/skylot/jadx) jadx-gui-1.4.4-no-jre-win.exe
    * export JVM_ARGS="-Xmx4096m -XX:MaxPermSize=1024m"
* [Bytecode-Viewer.jar {% include relref_github.html %}](https://github.com/Konloch/bytecode-viewer) Bytecode-Viewer-2.11.2.jar
    * A Java 8+ Jar & Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger & More)
* [baksmali-2.5.2.jar & smali-2.5.2.jar](https://bitbucket.org/JesusFreke/smali/downloads/)

E:\kSource\pythonx\orange\dexapk.py

E:\kSource\pythonx\orange\dex-tools\apktool_2.6.1.jar
E:\kSource\pythonx\orange\apktool.bat
E:\kSource\pythonx\orange\jd-gui-windows-1.6.6\jd-gui.exe
E:\kSource\pythonx\orange\dex-tools-2.2-SNAPSHOT\d2j-dex2jar.bat
E:\kSource\pythonx\orange\dex-tools\baksmali-2.5.2.jar
E:\kSource\pythonx\orange\dex-tools\smali-2.5.2.jar
E:\kSource\dist\Bytecode-Viewer-2.11.2.jar
C:\Users\ADMIN\Downloads\jadx-gui-1.4.4-with-jre-win\jadx-gui-1.4.4.exe

E:\kSource\pythonx\orange\dex-tools-2.2-SNAPSHOT\d2j-dex2jar.bat classes.dex --output classes.jar
E:\kSource\pythonx\orange\dex-tools-2.2-SNAPSHOT\d2j-dex2jar.bat classes2.dex --output classes2.jar
E:\kSource\pythonx\orange\dex-tools-2.2-SNAPSHOT\d2j-dex2jar.bat classes3.dex --output classes3.jar
E:\kSource\pythonx\orange\dex-tools-2.2-SNAPSHOT\d2j-dex2jar.bat classes4.dex --output classes4.jar

反编译命令：
```
apktool.bat d 2020_12_12_5.31.0.20201211_dbg.apk -f
apktool.bat d 2020_12_12_5.31.0.20201211_official.apk -f
```

W: Cant find 9patch chunk in file: "drawable-xxhdpi-v4/umcsdk_exception_bg.9.png". Renaming it to \*.png.

打包命令：
```
apktool.bat b 2020_12_12_5.31.0.20201211_dbg
```

dex2jar.bat
反编译命令：
```
d2j-dex2jar.bat [classes.dex 文件]
d2j-dex2jar.bat xyz.apk
```

jadx?


### 签名

<https://www.cnblogs.com/yyq-quan/archive/2011/07/08/2101434.html>
<https://blog.csdn.net/weixin_34726945/article/details/113044682>

E:\android-studio-ide-181.5014246-windows\android-studio\jre\bin\keytool.exe
chcp 65001
chcp 936
E:\android-studio-ide-181.5014246-windows\android-studio\jre\bin\keytool.exe -genkey -v -keystore androidguy-test.keystore -alias androidguy -keyalg RSA -validity 30000
testguy
```
正在为以下对象生成 2,048 位 RSA 密钥对和自签名证书 (SHA256withRSA) ( 有效期为 30,000 天 ):
         CN=hai, OU=cf, O=cf, L=zh, ST=zh, C=cn
输入 <androidguy> 的密钥口令（如果和密钥库口令相同，按回车）：
[正在存储 androidguy-test.keystore]

Warning:
JKS 密钥库使用专用格式。建议使用 "keytool -importkeystore -srckeystore androidguy-test.keystore -destkeystore androidguy-test.keystore -deststoretype pkcs12" 迁移到行业标准格式 PKCS12。
```

E:\android-studio-ide-181.5014246-windows\android-studio\jre\bin\jarsigner.exe
chcp 936
E:\android-studio-ide-181.5014246-windows\android-studio\jre\bin\jarsigner.exe -verbose -keystore androidguy-test.keystore 2020_12_12_5.31.0.20201211_dbg2.apk androidguy


## WINDOWS 的 Android Studio 无法启动 ARM 的模拟器

* mumu 夜神也是 x86 模拟器，只是有 intel 搞得一个 arm 兼容层 **houdini**
* 现在 windows 下跑 arm apk 最好的方案就是微软搞的那个 **wsa**，win11 可以直接商店安装，win10 其实也能用，但需要一些特殊步骤安装


## Android Studio

AndroidStudio 代码达到指定字符长度时自动换行。
1. 设置每行最大字符个数，超过这个数字 将会自动换行。
2. Line breaks 选中表示隐藏性保持断行。Ensure right margin is not exceeded 选中表示代码超过标准线 就自动换行。

{% include image.html url="/assets/images/201215-android-studio/20210211190104.png" %}
{% include image.html url="/assets/images/201215-android-studio/20210211190127.png" %}


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

{% include image.html url="/assets/images/201215-android-studio/20210205105349.png" %}

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

{% include image.html url="/assets/images/201215-android-studio/20210205110750.png" %}
{% include image.html url="/assets/images/201215-android-studio/20210205110931.png" %}

{% include image.html url="/assets/images/201215-android-studio/20210205155832.png" %}

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



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-15-Android-Studio.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://ibotpeaches.github.io/Apktool/]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/ibotpeaches.github.io/cf838194.html" %})
- [http://java-decompiler.github.io/]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/java-decompiler.github.io/8cff06fd.html" %})
- [https://github.com/pxb1988/dex2jar]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/github.com/db14066b.html" %})
- [https://github.com/skylot/jadx]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/github.com/c57ce690.html" %})
- [https://github.com/Konloch/bytecode-viewer]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/github.com/3abeab5a.html" %})
- [https://bitbucket.org/JesusFreke/smali/downloads/]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/bitbucket.org/1c13ac70.html" %})
- [https://www.cnblogs.com/yyq-quan/archive/2011/07/08/2101434.html]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/www.cnblogs.com/e163fdc3.html" %})
- [https://blog.csdn.net/weixin_34726945/article/details/113044682]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/blog.csdn.net/4c983743.html" %})
- [https://developer.android.com/r/studio-ui/ndk-dir]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/developer.android.com/a3b9e8b2.html" %})
- [http://maven.aliyun.com/nexus/content/groups/public/]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/maven.aliyun.com/f69c0880.html" %})
- [http://maven.aliyun.com/nexus/content/repositories/jcenter]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/maven.aliyun.com/e33967a3.html" %})
- [https://dl.bintray.com/umsdk/release]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/dl.bintray.com/2871e588.html" %})
- [https://www.jianshu.com/p/f23df3aa342c]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/www.jianshu.com/6a23ff97.html" %})
- [https://www.cnblogs.com/yongdaimi/p/12061298.html]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/www.cnblogs.com/a12e7578.html" %})
- [https://blog.csdn.net/dingxianding/article/details/106017010]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/blog.csdn.net/b7b79d7f.html" %})
- [https://zhuanlan.zhihu.com/p/77427951]({% include relrefx.html url="/backup/2020-12-15-Android-Studio.md/zhuanlan.zhihu.com/bc1d4621.html" %})
