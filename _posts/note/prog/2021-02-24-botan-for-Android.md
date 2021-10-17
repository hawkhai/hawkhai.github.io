---
layout: post
title: "编程与调试 C++ -- Botan for Android: Crypto and TLS for Modern C++"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

Cryptography Toolkit
botan.randombit.net
[Botan: Crypto and TLS for Modern C++ {% include relref_github.html %}](https://github.com/randombit/botan)
这个库有点特（sāo）别（qì），需要针对每个平台运行 configure.py 生成对应平台的代码，Star 1.6k，非常流（niú）行（bī）。

有文档 [Building Botan](https://botan.randombit.net/handbook/building.html)，用 botan-2.13.0 版本搞事情。


## Windows

```bat
python configure.py --os=windows --cc=msvc --cpu=x86_32 \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib
```

顺利生成三个文件：botan_all_internal.h，botan_all.h，botan_all.cpp。


## --amalgamation

Use amalgamation to build


### --disable-shared-library

Disable building a shared library


### --enable-modules=MODS

Enable some specific modules


### --minimized-build

Start with the bare minimum. This is mostly useful in conjuction with
--enable-modules to get a build that has just the features
a particular application requires.


## Android

Android 难搞哦。


### --cc-bin=BINARY

Set path to compiler binary
If not provided, the value of the `CXX` environment variable is used if set.

Modern versions of Android NDK use Clang and support C++11.
Simply configure using the appropriate NDK compiler:

```shell
$ export CXX=/opt/android-ndk/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android28-clang++
$ ./configure.py --os=android --cc=clang --cpu=arm64
```

```bat
set path=D:\Android\Sdk\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin;%path% # 直接找到 clang++
python configure.py --os=android --cc=clang --cpu=x86_64 \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib --without-os-feature=getauxval
```

```bat
set CXX=D:\Android\Sdk\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin\aarch64-linux-android28-clang++.cmd
python configure.py --os=android --cc=clang --cpu=arm64 \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib --without-os-feature=getauxval
```

```bat
set CXX=D:\Android\Sdk\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin\armv7a-linux-androideabi28-clang++.cmd
python configure.py --os=android --cc=clang --cpu=arm \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib --without-os-feature=getauxval
```

```bat
set CXX=D:\Android\Sdk\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin\i686-linux-android28-clang++.cmd
python configure.py --os=android --cc=clang --cpu=x86 \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib --without-os-feature=getauxval
```

```bat
set CXX=D:\Android\Sdk\ndk\22.0.7026061\toolchains\llvm\prebuilt\windows-x86_64\bin\x86_64-linux-android28-clang++.cmd
python configure.py --os=android --cc=clang --cpu=x86_64 \
    --minimized-build --amalgamation --disable-shared-library \
    --enable-modules=aes,sha2_32,md5,cbc,filters,zlib --without-os-feature=getauxval
```


## 整合

五份代码只有 botan_all.h 的部分头文件定义不一样，**拣出来** 整合。

```cpp
#ifdef _MSC_VER
    #include "botan_all_windows_msvc_x86_32.h"
#endif

// https://developer.android.com/ndk/guides/cpu-features
#ifdef __ANDROID__
    #ifdef __arm__
        #include "botan_all_android_clang_arm32.h"
    #endif
    #ifdef __aarch64__
        #include "botan_all_android_clang_arm64.h"
    #endif
    #ifdef __i386__
        #include "botan_all_android_clang_x86_32.h"
    #endif
    #ifdef __x86_64__
        #include "botan_all_android_clang_x86_64.h"
    #endif
#endif
```

botan_all_android_clang_arm32 vs botan_all_android_clang_x86_64 主要差异；

{% include image.html url="/assets/images/210224-botan-for-android/20210224150930.png" url2="/assets/images/210224-botan-for-android/20210224150920.png" %}


## 最终代码

<a href="{% include relref.html url="/source/botan_src.zip" %}" target="_blank">Download</a>

还需要从 <https://www.zlib.net/> 下载：zlib-1.2.11.tar.gz 配合食用。^_^



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-24-botan-for-Android.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/randombit/botan]({% include relrefx.html url="/backup/2021-02-24-botan-for-Android.md/github.com/85f12777.html" %})
- [https://botan.randombit.net/handbook/building.html]({% include relrefx.html url="/backup/2021-02-24-botan-for-Android.md/botan.randombit.net/bde2930d.html" %})
- [https://developer.android.com/ndk/guides/cpu-features]({% include relrefx.html url="/backup/2021-02-24-botan-for-Android.md/developer.android.com/11aa3d2a.html" %})
- [https://www.zlib.net/]({% include relrefx.html url="/backup/2021-02-24-botan-for-Android.md/www.zlib.net/1215b7e1.html" %})
