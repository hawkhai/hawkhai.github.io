---
layout: post
title: "编程与调试 C++ -- MacOS crash dump App 崩溃日志解析方法"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory", "C/C++", "MacOS"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---

[Mac OS App 崩溃日志解析方法 {% include relref_jianshu.html %}](https://www.jianshu.com/p/ebe0c37e5e1c)
Crash 文件大体分为 3 种：Unsymbolicated（未符号化）、Partially Symbolicated（半符号化）和 Fully Symbolicated（符号化）。
{% include image.html url="/assets/images/240625-macos-dump/ccdc59c150863815356569d15f8889ae.webp" %}

一般我们拿到的 .crash 都是 Unsymbolicated。在符号化之前，首先确保 .crash 文件相关崩溃模块的 uuid 和相关崩溃模块的 .dSYM 的 uuid 一致，这样得到的结果才是准确的。
通过 `dwarfdump --uuid <Path to dSYM file>` 得到 .dSYM 的 uuid（ `<>` 不需要）。

dsymutil appName.app/Contents/MacOS/appName

符号存储推荐：
symbols/

```
dsymutil libcpdump_a.dylib
dsymutil libcpdump_ad.dylib
dsymutil libcpdump_i.dylib
dsymutil libcpdump_id.dylib
dsymutil out/arm64/Debug/crashpad_handler
dsymutil out/arm64/Release/crashpad_handler
dsymutil out/x64/Debug/crashpad_handler
dsymutil out/x64/Release/crashpad_handler

cp -R libcpdump_a.*  ../../lib/macos/dump/
cp -R libcpdump_ad.* ../../lib/macos/dump/
cp -R libcpdump_i.*  ../../lib/macos/dump/
cp -R libcpdump_id.* ../../lib/macos/dump/
cp -R out/arm64/Debug/crashpad_handler*   ../../lib/macos/dump/arm64/Debug/
cp -R out/arm64/Release/crashpad_handler* ../../lib/macos/dump/arm64/Release/
cp -R out/x64/Debug/crashpad_handler*     ../../lib/macos/dump/x86_64/Debug/
cp -R out/x64/Release/crashpad_handler*   ../../lib/macos/dump/x86_64/Release/
```

```
# : Mach-O 64-bit executable arm64
/Users/apple/crashpad_handler # 这个不分配 7777 貌似会崩溃？！
```

也有可能是 cpu arch 不同吧，分析 dump 的机器环境上安装的 app 版本必须要与崩溃的版本一致才可以。

**分析崩溃的 机器要和 崩溃的 dump 安装同样的版本，分析程序会读对应的 elf 文件。**
崩溃分析需要准备的文件：
1. 崩溃文件 minidump
2. 对应的符号 .dSYM 文件
3. 安装和崩溃电脑同样的程序版本

**如果代码和构建电脑保持一致，会自动显示代码行。**


## 几个工具

* (star 576) SYM
    一个图形化的崩溃日志符号化工具，最新版本下载地址：<https://github.com/zqqf16/SYM/releases/latest>
* SymbolicatorX
    iOS/Mac 项目崩溃文件自动符号化工具。
* (star 3.4k) [dSYMTools {% include relref_github.html %}](https://github.com/answer-huang/dSYMTools)
    * 友盟统计 可以提交崩溃？？
* (star 1.2k) **MacSymbolicator** Symbolicating macOS/iOS crash reports, easily.
    * 比较喜欢这个的图形化界面。
    * <https://mahdi.jp/apps/macsymbolicator>


### 符号化的准备–UUID

首先判断 DSYM 文件和 app 和 crash 文件（如果存在）的 UUID 相同，确保是同一次编译的产物，
因为每次编译由于 ALSR（地址空间随机化）会生成不同的偏移量，如果三者的 UUID 不同，那么偏移量也会不同，
导致符号化的地址不一样，会定位到错误的方法名上面去，下面就是查看 UUID 的方法。

#### dSYM 文件的 uuid

* 在 DSYM 文件目录内运行。
    xcrun dwarfdump --uuid \*.dSYM

会得到如下 结果：

UUID: 74D0C44D-E902-3A51-B412-2F76EA810AAD (x86_64) DSYMTest.app.dSYM/Contents/Resources/DWARF/DSYMTest

其中 UUID 为 74D0C44D-E902-3A51-B412-2F76EA810AAD。

#### App 的 uuid

* iOS
    xcrun dwarfdump --uuid .app/
* Mac
    xcrun dwarfdump --uuid DSYMTest.app/Contents/MacOS/DSYMTest

需要进入 .app 的包内容里面的 查看同名的可执行文件才行。


## macOS 崩溃日志符号化

<https://blog.msmk.live/2018/08/03/2018-08-03-maccrashreportssymbol/>


### 分析工具

网上一大堆文章都是分析 iOS 的崩溃日志的，针对 Mac 的特别少，其实基本原理都差不多，就不再详细的描述了。就推荐一个崩溃日志符号化的工具。

[下载地址](https://mahdi.jp/apps/macsymbolicator)
[源码地址 {% include relref_github.html %}](https://github.com/inket/MacSymbolicator)

使用方法：
1. 将 .crash 文件和 .dSYM 文件放在同一目录下。
2. 将 .crash 或者 .dSYM 拖入这个工具中，另外一个文件会自动导入。

* 注 1：.dSYM 可以在打包时候生产的 .xcarchive 包中找到。
* 注 2：注意 .crash 和 .dSYM 的 UUID 要一致。
* 查看 dSYM UUID `xcrun dwarfdump --uuid file_path` 。
* .crash 查看 UUID 在 Binary Images 的下一行 包名 后面的那一串字符。
还有一个工具可以参考
[dSYMTools {% include relref_github.html %}](https://github.com/answer-huang/dSYMTools)
这个工具也可以符号化崩溃日志，需要手动操作，具体使用方式链接上面说的很清楚了。

dsymutil YourApp
RelWithDebInfo


## 符号

你看，上面这个是用 dSYM 加载符号看到的信息
下面的就是用二进制加载符号看到的信息。

{% include image.html url="/assets/images/240625-macos-dump/20240626-145720.jpeg" %}
{% include image.html url="/assets/images/240625-macos-dump/20240626-145737.jpeg" %}


## MacOS 平台软件编译的若干问题（自定义 Makefile 调试符号等）

<https://blog.csdn.net/quentin_d/article/details/122879754>

目前，MacOS/iOS 的调试信息使用 dwarf 标准，最终的调试信息一般保存在 .dSYM bundle 文件中，
.dSYM bundle 像 .APP 文件一样，是个文件包，里面的子目录 `.dSYM/Contents/Resources/DWARF/`
保存着 dwarf 调试符号（只包含调试符号信息的 MachO 文件，可以使用 python 工具 dwex 查看）。

**调试时，调试器怎么找到对应的 .dSYM bundle？**
比较简单的方式是，只要将可执行文件和 .dSYM 放到同一个目录下，符合 exename 和 exename.dSYM 的范式，lldb 就可以找到符号，
或者使用 lldb 的 add-dsym 命令加载指定位置的 .dSYM 符号。
可以使用 otool -hlv 或者 dwarfdump --uuid 来查看，这个 UUID 是唯一的。

**编译器怎么生成调试符号？**
可以使用 dsymutil -dump-debug-map main 来查看，或者使用 nm -pa executable 来查看 debug map entries）。
调试信息不存在于最终生成的 Macho 文件中，即使使用 -g 开启调试信息，最终的 MachO 也不会包含太多调试信息，最多会保存着一些函数名（一旦 strip 就会被去掉）。
DWARF Debugging Standard Wiki [link](http://wiki.dwarfstd.org/index.php?title=Apple%27s_%22Lazy%22_DWARF_Scheme)

一般将 object 文件中的调试信息放到 .dSYM 文件包中，这个工作是由 dsymutil 这个工具完成的，它的功能相当于 linux 下的 objcopy 程序。

dsymutil 可以看作是一个 debug info linker，做的事情就是读取 MachO 文件和它对应的 object 文件，获取调试信息，重定位，然后写入到 .dSYM 中（的一个包含 dwarf 的 binary 中）。

调用 dsymutil 工具生成 .dSYM 文件，然后再使用 strip 将可执行文件的中调试信息删除。
```
$(target) : $(objects)
    @mkdir -p $(bin)
    $(CXX) $(objects) -o $(bin)/$@ $(LDFLAGS)

ifeq ($(os), Darwin)
    dsymutil $(bin)/$@
    $(STRIP) -u -r -arch all $(bin)/$@
else
    $(OBJCOPY) --only-keep-debug $(bin)/$(target) $(bin)/$(target).sym
    $(STRIP) --strip-debug --strip-unneeded $(bin)/$(target)
    $(OBJCOPY) --add-gnu-debuglink $(bin)/$(target).sym $(bin)/$(target)
endif
```

需要再用 lipo 打包不同架构的 dwarf MachO，生成一个支持多架构的 .dSYM 文件包。
```
all:

    echo "making arm version ..........."
    sleep 2
    rm -rf build_arm
    make -f makefile clean
    make -f makefile
    mkdir build_arm
    mv build/* build_arm/

    echo "making x86 version ..........."
    sleep 2
    rm -rf build_x86
    make -f makefile clean
    export ARCH=x86
    ARCH=x86
    make -f makefile
    mkdir build_x86
    mv build/* build_x86/

    echo "making universe binary........"
    sleep 2
    rm -rf build
    mkdir build
    @list='$(SUBDIRS)'; for binary in $$list; do \
        echo "making $$binary"; \
        lipo -create -output build/$$binary build_x86/$$binary build_arm/$$binary ; \
        dsymutil build/$$binary ; \
        rm build/$$binary.dSYM/Contents/Resources/DWARF/$$binary ; \
        lipo -create -output build/$$binary.dSYM/Contents/Resources/DWARF/$$binary build_x86/$$binary.dSYM/Contents/Resources/DWARF/$$binary build_arm/$$binary.dSYM/Contents/Resources/DWARF/$$binary ; \
    done;
```

编译时，优化相关的开关 -O0 -O2 等，并不影响调试信息的生成，虽然更高的优化等级生成的代码比-O0 更难以调试。

refer:
<https://stackoverflow.com/questions/10044697/where-how-does-apples-gcc-store-dwarf-inside-an-executable/12827463#12827463>


## 编译 Crashpad 库

<https://www.cnblogs.com/slcode/p/969b1b72b8ab08f3213e4b7364b0c7ac.html>
Crashpad 是一个支持 mac 和 windows 的崩溃报告库，google 还有一个 breakpad，已经不建议使用了。
mac，直接使用官网一步一步走即可。


### 获取工具

[depot_tools 工具链接](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up)
{% include image.html url="/assets/images/240625-macos-dump/1520205-20200109183140862-291019894.png" %}

mac 照着上面安装，然后输出到环境变量中。
windows 下载压缩包，然后放到系统 PATH 中。然后使用 CMD（注意是 cmd，不是 PowerShell）

下载完以后，基本就是靠 depot_tools 这个工具集合了，这个工具机带有 git，ninja，python。


### Crashpad 库编译步骤

[Crashpad 库编译步骤](https://chromium.googlesource.com/crashpad/crashpad/+/master/doc/developing.md)
How to Build Google Crashpad [link](https://docs.bugsplat.com/introduction/getting-started/integrations/cross-platform/crashpad/how-to-build-google-crashpad)

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
sudo echo "export PATH=/Users/apple/Desktop/cfcode/depot_tools:$PATH" >> ~/.zshrc

# Generating Build Configuration
cd ~/crashpad/crashpad
gn gen out/Default
# Building with Ninja
ninja -C out/Default
```

mac 照着上面步骤即可成功编译。
windows 遇到编码问题，在用 ninja 生成项目文件后，有
rule cc
rule cxx
找到 ${cflags_c} 后，添加 `/WX-` ，这是为了忽略编码警告。中途可能还会遇到有换行符的问题，我是用 vscode 把此文件改成 utf-bom 格式存储，这样整个就编译完成了。
{% include image.html url="/assets/images/240625-macos-dump/1520205-20200109183141266-1465950945.png" %}

注：
windows 编译完成，并不是规则的输出到某个目录下，而是分散的，所以需要自己去手动拷贝。
这样未免有点麻烦，可以到 [这里](https://get.backtrace.io/crashpad/builds/) 下载编译好的库。

我选择的 stable 版本，stable 和最新版的头文件组织有点差异，小改一下就好。
[代码指导](https://help.backtrace.io/en/articles/2337714-crashpad-integration-guide)


### 其他

设置 crash exe 工作路径
设置数据存放路径
设置 crash 文件上传路径，上传支持传入多个参数，以方便分析。


## Crashpad 的编译过程及原理

How I Build Google Crashpad with CMake when it's checked into source
<https://gist.github.com/jameskr97/8c40d927db05fe253235e05333fed4f3>

Crashpad 编译

Crashpad 是由 Google 开发的一个开源的跨平台崩溃报告库，主要用于在应用程序崩溃时收集和提交崩溃信息。
通常，我们需要 cmake 来编译项目，但由于 Crashpad 不使用 cmake 编译，因此要实现源码编译 Crashpad，需要编写 cmakelists.txt 来编译。

```
git clone github.com/TheAssemblyArmada/crashpad-cmake.git
```

在 cmakelists.txt 中添加：

```
add_subdirectory(crashpad-cmake)
```


## 崩溃问题

编译方法：从 crashpad/CMakeLists.txt 进行编译，一次性编译出 arm64 和 x86_64 的 debug 和 release，共 4 个版本的文件，存放在 crashpad/build/out 目录下面。
没有采用提交二进制的方案，如果编译机无法顺利完成编译，我再用本地编译的二进制提交。

收集到的 dump 文件属于 mini dump，可以用我们开发环境自带的 lldb 来进行调试。先用 lldb -c 打开 dmp 文件，然后用 bt 查看崩溃栈，其他更复杂的调试方法要靠大家发掘了。举例如下：
```
lldb -c ~/Downloads/20240524/crashpad_database/completed/ec6ca487-3528-4ce5-b800-23d263fee3f2.dmp
(lldb) target create --core "/Users/sumless/Downloads/20240524/crashpad_database/completed/ec6ca487-3528-4ce5-b800-23d263fee3f2.dmp"
warning: (arm64e) /usr/lib/system/libsystem_kernel.dylib address 0x0000000197511000 maps to more than one section: libsystem_kernel.dylib.__DATA_DIRTY and libdyld.dylib.__TEXT
warning: (arm64e) /usr/lib/system/libsystem_platform.dylib address 0x000000019753f000 maps to more than one section: libsystem_platform.dylib.__DATA_CONST and libsystem_info.dylib.__TEXT
Core file '/Users/sumless/Downloads/20240524/crashpad_database/completed/ec6ca487-3528-4ce5-b800-23d263fee3f2.dmp' (aarch64) was loaded.
(lldb) bt
* thread #3, stop reason = EXC_BAD_ACCESS (code=1, address=0x0)
  * frame #0: 0x0000000104a2fad0 Tutorial`threadFunction() at crash_main.cpp:184:14
    frame #1: 0x0000000104a31b64 Tutorial`decltype(std::declval<void (*)()>()()) std::__1::__invoke[abi:ue170006]<void (*)()>(__f=0x000000014f004128) at invoke.h:340:25
    frame #2: 0x0000000104a31afc Tutorial`void std::__1::__thread_execute[abi:ue170006]<std::__1::unique_ptr<std::__1::__thread_struct, std::__1::default_delete<std::__1::__thread_struct>>, void (*)()>(__t=size=2, (null)=__tuple_indices<> @ 0x000000016b4e6f7f) at thread.h:227:5
    frame #3: 0x0000000104a31460 Tutorial`void* std::__1::__thread_proxy[abi:ue170006]<std::__1::tuple<std::__1::unique_ptr<std::__1::__thread_struct, std::__1::default_delete<std::__1::__thread_struct>>, void (*)()>>(__vp=0x000000014f004120) at thread.h:238:5
    frame #4: 0x000000019750af94 libsystem_kernel.dylib
(lldb)q
```

在 LLDB 中查看 dmp 文件（通常指 core dump 文件）时，您可能需要指定调试符号路径以便 LLDB 能够正确地解析符号。您可以使用 target.symbols-path 设置来添加额外的符号路径。打开 LLDB 后，可通过以下命令设置符号路径：

(lldb) settings set target.symbols-path /path/to/symbols
如果您有多个路径需要添加，可以使用冒号（在 Unix-like 系统上）或分号（在 Windows 上）来分隔它们：

(lldb) settings set target.symbols-path /path/to/symbols1:/path/to/symbols2
在 LLDB 中加载 core dump 文件后，它会尝试在这些指定路径中查找符号文件。

请确保替换上述命令中的 /path/to/symbols 为实际的符号文件路径。
关于 lldb，有什么问题都问 AI

lldb --core xxx.dmp
image list


### 自动显示代码行

也有可能是 cpu arch 不同吧，分析 dump 的机器环境上安装的 app 版本必须要与崩溃的版本一致才可以。

**分析崩溃的 机器要和 崩溃的 dump 安装同样的版本，分析程序会读对应的 elf 文件。**
崩溃分析需要准备的文件：
1. 崩溃文件 minidump
2. 对应的符号 .dSYM 文件
3. 安装和崩溃电脑同样的程序版本

如果代码和构建电脑保持一致，会自动显示代码行。
```
(lldb) thread select 46
(lldb) thread backtrace
* thread #46, stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
* frame #0: 0x000000010a0fede0 libkvision.dylib`globalInitNcnnModel(x=<unavailable>) at DeshadowBitmap.cpp:0:13 [opt]
frame #1: 0x000000010a1006eb libkvision.dylib`dcImageClassifyTypev2(a1=0x000070000ce5eb00, a2x=<unavailable>, a3=0x000070000ce5eafc, v33net=0x000000010a4e1690, dirty0=<unavailable>) at DeshadowBitmap.cpp:618:9 [opt]
frame #2: 0x000000010a1011c1 libkvision.dylib`dcImageClassifyType(cv::Mat*, int, DcImageClassifyType*, ncnn::Net&, long long) [inlined] dcImageClassifyTypev2(a1=<unavailable>, a2x=<unavailable>, a3=<unavailable>, v33net=<unavailable>) at KVisionFilterAuto.h:54:12 [opt]
frame #3: 0x000000010a1011b9 libkvision.dylib`dcImageClassifyType(a1=<unavailable>, a2x=<unavailable>, a3=<unavailable>, v33net=<unavailable>, dirty0=123145518704744) at DeshadowBitmap.cpp:656:13 [opt]
frame #4: 0x000000010a102fb9 libkvision.dylib`::kvisionClassifyShadowType(JNIEnv *, int, ImageStruct *) [inlined] dcImageClassifyType(a1=0x000070000ce5eb00, a2x=1, a3=0x000070000ce5eafc, v33net=<unavailable>) at KVisionFilterAuto.h:61:12 [opt]
frame #5: 0x000000010a102f9c libkvision.dylib`kvisionClassifyShadowType(env=<unavailable>, a2k=<unavailable>, jbitmap=<unavailable>) at DeshadowBitmap.cpp:845:9 [opt]
frame #6: 0x000000010a0f81f9 libkvision.dylib`k001(rgba=<unavailable>, width=<unavailable>, height=<unavailable>, stride=<unavailable>, alg=<unavailable>) at convert_mobile.cpp:79:40 [opt]
frame #7: 0x000000010a0ab8c2 libfastimage.dylib`fastimage::KFastImageInterface::fast001(fastimage::FastImage&, fastimage::FastImageAlg) + 130
frame #8: 0x00000001083b1c26 pdfreader`ImageEditor::UpdateThumbnailImage() [inlined] ImageEditor::ChangeFilterImpl(this=<unavailable>, pImage=0x000070000ce5fcb8, nFilterType=FastImageEnhanceDeShadow) at ImageEditor.cpp:278:45 [opt]
frame #9: 0x00000001083b1bb6 pdfreader`ImageEditor::UpdateThumbnailImage(this=0x0000600000ce03b0) at ImageEditor.cpp:691:9 [opt]
frame #10: 0x00000001083aab72 pdfreader`ImageEditor::RepaintImage(this=0x0000600000ce03b0) at ImageEditor.cpp:656:9 [opt]
frame #11: 0x00000001083a06e5 pdfreader`EditorActionThread::run(this=<unavailable>) at EditorActionThread.cpp:90:22 [opt]
frame #12: 0x000000010c10dc0a QtCore`QThreadPrivate::start(arg=0x0000600000ce0418) at qthread_unix.cpp:329:14 [opt]
frame #13: 0x00007fff73c6f109 libsystem_pthread.dylib
frame #14: 0x00007fff73c6ab8b libsystem_pthread.dylib
(lldb) frame variable
* thread #46, stop reason = EXC_BAD_ACCESS (code=EXC_I386_GPFLT)
frame #0: 0x000000010a0fede0 libkvision.dylib`globalInitNcnnModel(x=<unavailable>) at DeshadowBitmap.cpp:0:13 [opt]
483     bool byte_ncnn_inited_aha = false;
484
485     #define sub_B87EC globalInitNcnnModel
-> 486  int globalInitNcnnModel(int x = 1)
^
487     {
488         KLocker locker(g_ncnn_sesion_aha);
489         bool inited = byte_ncnn_inited_aha;
Note: this address is compiler-generated code in function globalInitNcnnModel(int) that has no source code associated with it.
(int) x = <no location, value may have been optimized out>
(KLocker) locker = <variable not available>
(int) result = -1
(bool) inited = <no location, value may have been optimized out>
(int) code = <variable not available>
(lldb) source list
490         byte_ncnn_inited_aha = true;
491
492         int result = 0; // r0
493         result = -1;
494         if (!byte_6B1A2C)
495         {
496             // 初始化 libncnn.so
```


## Termination Reason: DYLD, [0x4] Symbol missing

Application Specific Information:
dyld: launch, loading dependent libraries
```
Dyld Error Message:
  Symbol not found: __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
  Referenced from: /Applications/MyPDF.app/Contents/MacOS/../Frameworks/libopencv_core.3.4.dylib (which was built for Mac OS X 12.0)
  Expected in: /usr/lib/libc++.1.dylib
```

[clang 在编译时指定目标文件所需的最低 macOS 版本 {% include relref_cnblogs.html %}](https://www.cnblogs.com/z16166/p/16861268.html)
这个是因为 Apple 的 SDK 使用 weak linking 来支持不同版本的 macOS。

目标文件所需的最低 macOS 版本有个专有名称“deployment target”。


### 查看库的 deployment target

查看 \*.dylib、\*.a 或者主程序的 deployment target 属性、sdk 版本：
```
otool -l 7z.dylib | grep -E "(minos|sdk)"
find . -name "*.a" | xargs otool -l | grep -E "(minos|sdk)"
```


### 通过命令行参数设置 deployment target

clang/clang++ 在编译时指定 deployment target 的命令行参数是-mmacos-version-min，比如：-mmacos-version-min=10.15，指定最低为 Catalina 的最后一个版本 10.15。
针对 iOS 等有类似的开关如-miphoneos-version-min、-mtvos-version-min、 -mwatchos-version-min。
-mmacos-version-min 有个别名-mmacosx-version-min，别名只是为了兼容，尽量不使用这个别名。
clang 会根据这个命令行参数来定义编译器内置宏 MAC_OS_X_VERSION_MIN_REQUIRED 等，而 SDK 头文件 \<AvailabilityMacros.h>、\<Availability.h>
中有对这些宏的检查，根据宏决定哪些符号采用 weak linking。weak linking 的符号在编译时不会报错，dylib 加载时也不会报错，在用到对应的符号时如果不存在才会报错。


### 通过环境变量设置 deployment target

clang 的这个参数也可通过环境变量来设置。命令行参数优先于环境变量。
```
MACOSX_DEPLOYMENT_TARGET
IPHONEOS_DEPLOYMENT_TARGET
TVOS_DEPLOYMENT_TARGET
WATCHOS_DEPLOYMENT_TARGET
DRIVERKIT_DEPLOYMENT_TARGET
```
我们的工程以及我们的工程所直接 / 间接依赖的所有静态库 / 动态库，都需要在编译时指定相同的 deployment target。
省事的办法是通过环境变量来统一设置，在开始整个打包之前设置一下。
其次是命令行开关。不同工程类型的命令行开关设置方法有差异。以下是命令行开关的设置。


### 通过 vcpkg install 编译的库

需要更改 vcpkg/triplets/x64-osx.cmake 文件的内容，增加下面三行（理论上只要第一行即可，但 vcpkg 目前貌似有 bug，导致 VCPKG_OSX_DEPLOYMENT_TARGET 只对 CMake 工程生效，对其他类型的工程不生效。所以需要第二行、第三行）：
```
set(VCPKG_OSX_DEPLOYMENT_TARGET "10.15")
set(VCPKG_C_FLAGS -mmacosx-version-min=10.15)
set(VCPKG_CXX_FLAGS -mmacosx-version-min=10.15)
```
也可以复制这个文件到某个目录下，在复制出来的文件中增加上面这三行，然后给 vcpkg install 传递--overlay-triplets 参数以使用这个修改过的 triplet 文件。这样通过 vcpkg install 安装的所有库的 deployment target 都是 10.15。


### autoconf 类型的工程

比如 libiconv 库是手动执行 autoconf 编译的，需要在 configure 时增加参数：
```
./configure CFLAGS=-mmacos-version-min=10.15 CPPFLAGS=-mmacos-version-min=10.15
```


### CMake 工程

在 CMakeLists.txt 里的 project() 语句之前增加一句：
```
set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15")
```
或者
```
set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15" CACHE STRING "" FORCE)
set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15" CACHE STRING "Minimum OS X deployment version" FORCE)
```


### Xcode 工程

在界面的工程属性中可以设置 deployment target。


### Makefile 工程

在 makefile 里自行给 clang 传递参数-mmacos-version-min=10.15 即可。


## 其它

* [Mac/iOS crash 或者地址符号解析 —— 工具篇 {% include relref_csdn.html %}](https://blog.csdn.net/goldWave01/article/details/90177708)
    * `xcrun dwarfdump --uuid *.dSYM`
    * `xcrun dwarfdump --uuid DSYMTest.app/Contents/MacOS/DSYMTest`
* [MacOS 如何解析系统库的符号？ {% include relref_csdn.html %}](https://blog.csdn.net/weixin_46168796/article/details/134057199)
* [如何用 Visual Studio 自带工具分析内存泄漏 ? {% include relref_csdn.html %}](https://blog.csdn.net/weixin_46168796/article/details/134057751)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-06-25-macos-dump.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.jianshu.com/p/ebe0c37e5e1c]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/www.jianshu.com/06ce48fe.html" %})
- [https://github.com/zqqf16/SYM/releases/latest]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/github.com/8392334e.html" %})
- [https://github.com/answer-huang/dSYMTools]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/github.com/e93615bd.html" %})
- [https://mahdi.jp/apps/macsymbolicator]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/mahdi.jp/14318311.html" %})
- [https://blog.msmk.live/2018/08/03/2018-08-03-maccrashreportssymbol/]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/blog.msmk.live/27ad49a6.html" %})
- [https://github.com/inket/MacSymbolicator]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/github.com/394cd9a4.html" %})
- [https://blog.csdn.net/quentin_d/article/details/122879754]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/blog.csdn.net/24c85663.html" %})
- [http://wiki.dwarfstd.org/index.php?title=Apple%27s_%22Lazy%22_DWARF_Scheme]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/wiki.dwarfstd.org/185e10b1.php" %})
- [https://stackoverflow.com/questions/10044697/where-how-does-apples-gcc-store-dwarf-inside-an-executable/12827463#12827463]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/stackoverflow.com/0d6c015b.html" %})
- [https://www.cnblogs.com/slcode/p/969b1b72b8ab08f3213e4b7364b0c7ac.html]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/www.cnblogs.com/4e2bbaca.html" %})
- [https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html#_setting_up]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/commondatastorage.googleapis.com/06bc5d57.html" %})
- [https://chromium.googlesource.com/crashpad/crashpad/+/master/doc/developing.md]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/chromium.googlesource.com/21821ca6.html" %})
- [https://docs.bugsplat.com/introduction/getting-started/integrations/cross-platform/crashpad/how-to-build-google-crashpad]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/docs.bugsplat.com/fe1ea0ff.html" %})
- [https://chromium.googlesource.com/chromium/tools/depot_tools.git]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/chromium.googlesource.com/de81edd7.git" %})
- [https://get.backtrace.io/crashpad/builds/]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/get.backtrace.io/d2e2d8a9.html" %})
- [https://help.backtrace.io/en/articles/2337714-crashpad-integration-guide]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/help.backtrace.io/7e8042d4.html" %})
- [https://gist.github.com/jameskr97/8c40d927db05fe253235e05333fed4f3]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/gist.github.com/3b664698.html" %})
- [https://www.cnblogs.com/z16166/p/16861268.html]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/www.cnblogs.com/83362cb1.html" %})
- [https://blog.csdn.net/goldWave01/article/details/90177708]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/blog.csdn.net/5c9c18a0.html" %})
- [https://blog.csdn.net/weixin_46168796/article/details/134057199]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/blog.csdn.net/0a4d0f1c.html" %})
- [https://blog.csdn.net/weixin_46168796/article/details/134057751]({% include relrefx.html url="/backup/2024-06-25-macos-dump.md/blog.csdn.net/e2bc77d1.html" %})
