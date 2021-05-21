---
layout: post
title: "PDFium -- 开发环境，PDFium 编译"
author:
location: "珠海"
categories: ["PDFium"]
tags: ["PDFium", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

* [基于开源 PDFium，编译动态库 -- Windows 平台（上） {% include relref_cnblogs.html %}](https://www.cnblogs.com/purehol/p/11734015.html)
* [基于开源 PDFium，编译动态库 -- Windows 平台（下） {% include relref_cnblogs.html %}](https://www.cnblogs.com/purehol/p/11734014.html)
* 编译 pdfium 为 一个 静态库。[Google's pdfium codebase set up as a Visual Studio solution that compiles to a static library on Windows. {% include relref_github.html %}](https://github.com/jwezorek/vs_pdfium)
* 编译好的直接用。[📰 Binary distribution of PDFium {% include relref_github.html %}](https://github.com/bblanchon/pdfium-binaries)


## win10 下 pdfium 编译 VS2019


### 环境准备

* 确保 path 里没有自己安装的 python
    * depot_tools 貌似是：Python 2.7.18
* kernel32.SetConsoleMode to enable ANSI sequences failed
    * [Console Virtual Terminal Sequences](https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)
    * 我本机 win10 不支持 彩色控制台，错误码是 87：
        ```cpp
  ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
  if (mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING) == 0:
          SetConsoleMode(h, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
  return True
```
    * 感觉是一个 `depot_tools\setup_color.py` bug，修改一下它的源代码：
        ```python
  if IS_TTY and is_windows:
          # Wrapping may cause errors on some Windows versions (crbug.com/1114548).
          if platform.release() != '10' or not enable_native_ansi():
              should_wrap = False
```
        <span imgid="20210521155505" />

{% include image.html url="/assets/images/210520-pdfium-devenv/20210521155505.png" relocate="20210521155505" caption="Win10 部分系统 gclient config & sync 会失败 bugfix" %}


### 代码下载

```
mkdir google
cd google
gclient config --unmanaged https://pdfium.googlesource.com/pdfium.git
# In order to use your locally installed version of Visual Studio to build Chrome.
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
gclient sync
```


### 开始编译

生成 gn 构建文件

```
# 进入 pdfium 根目录
cd pdfium
# 使用 VistulStudio 编译必要项
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_MSVS_VERSION=2019
# 利用 GN 来生成构建文件 gn args <directory>
gn args out/Release86
```

将以下内容拷贝进 args.gn 文件后，保存并退出编辑。

```
# Build arguments go here.
# See "gn args <out_dir> --list" for available build arguments.

use_goma = false # Googlers 可以使用它来分布式编译。确保 goma 已安装并首先运行。
is_debug = true # 要生成 release 库，所以关闭调试功能。

# 设置为启用实验性 Skia 后端。
pdf_use_skia = false
# 设置为启用实验性 Skia 后端（仅限路径）。
pdf_use_skia_paths = false

pdf_enable_xfa = true # 设置 false 以删除 XFA 支持（隐含 JS 支持）。
pdf_enable_v8 = true # 设置 false 以删除 Javascript 支持。
pdf_is_standalone = true # 设置非嵌入式构建。
# true 编译为动态库 /MD,/MDd，false 编译为静态库 /MT,/MTd
is_component_build = true # 禁用组件构建（必须为 false）
# pdf_is_complete_lib 为 false 时，编译为多个静态库，true 编译为一个独立的静态库
# pdf_is_complete_lib = true

clang_use_chrome_plugins = false # 当前必须为 false。
target_cpu = "x86" # 默认就是编译 x64 平台，编 x86 平台就需要修改了。
# true 将用 clang 进行编译，false 将用 VS2019 编译
# is_clang = false
```

* KeyError: 'WINDOWSSDKDIR'
    * 如果您的 Visual Studio 安装在非默认目录中， 您需要 设置几个环境变量来将工具链指向您的安装路径。
    * vs2019_install = DRIVE:\path\to\Microsoft Visual Studio\2019\Community, replacing 2019 and Community with your installed versions and replacing DRIVE: with the drive that Visual Studio is on. Often, this will be C:.
    * WINDOWSSDKDIR = DRIVE:\path\to\Windows Kits\10, replacing DRIVE: with the drive that Windows Kits is on. Often, this will be C:.
    * 读取环境变量还有点问题。<span imgid="vs_toolchain_bugfix" />
* You must install Windows 10 SDK version 10.0.19041.0 including the "Debugging Tools for Windows" feature.
    * https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/

{% include image.html url="/assets/images/210520-pdfium-devenv/20210521180749.png" relocate="vs_toolchain_bugfix" caption="vs_toolchain.py def NormalizePath(path):" %}
{% include image.html url="/assets/images/210520-pdfium-devenv/20210521180924.png" relocate="vs_toolchain_bugfix" caption="vs_toolchain.py win_sdk_dir = NormalizePath(win_sdk_dir)" %}

```
# 执行构建示例程序动作
ninja -C <directory> pdfium_test
# 执行构建整个 产品动作
ninja -C <directory> pdfium_all
# 执行构建 pdfium 库动作（本文便是执行构建 pdfium 动态库动作）
ninja -C <directory> pdfium

# 这里，简单使用：
E:\kpdf\pdfium>ninja -C out\Release86 pdfium
```

成功编译出来：
```
E:\kpdf\pdfium>ninja -C out\Release86 pdfium
ninja: Entering directory `out\Release86'
[3261/3261] LINK(DLL) pdfium.dll pdfium.dll.lib pdfium.dll.pdb
```


### 总结

```
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_MSVS_VERSION=2019

E:\kpdf\pdfium>gn args out/Release86
Waiting for editor on "E:\kpdf\pdfium\out\Release86\args.gn"...
Generating files...
Done. Made 355 targets from 139 files in 5690ms

E:\kpdf\pdfium>ninja -C out\Release86 pdfium
ninja: Entering directory `out\Release86'
[3284/3284] LINK(DLL) pdfium.dll pdfium.dll.lib pdfium.dll.pdb
```

gn gen build\Debug --ide=vs


## Crashpad 代码

```
# 获取 Crashpad 代码
fetch crashpad

# 同步第三方库
gclient sync

# 生成 VS 工程文件
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_GENERATORS=msvs-ninja,ninja
set DEPOT_TOOLS_UPDATE=0

python crashpad/build/gyp_crashpad.py

# 编译
ninja -C out/Debug
```

```
gn gen out/test --ide=vs2017 --sln=test --no-deps --args="is_debug=true"
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-20-pdfium-devenv.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/purehol/p/11734015.html]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/www.cnblogs.com/3ef3a595.html" %})
- [https://www.cnblogs.com/purehol/p/11734014.html]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/www.cnblogs.com/4100beaf.html" %})
- [https://github.com/jwezorek/vs_pdfium]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/github.com/dcd83ec9.html" %})
- [https://github.com/bblanchon/pdfium-binaries]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/github.com/e073027d.html" %})
- [https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/docs.microsoft.com/86a6c045.html" %})
- [https://pdfium.googlesource.com/pdfium.git]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/pdfium.googlesource.com/7e24f626.git" %})
- [https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/developer.microsoft.com/633f452d.html" %})
