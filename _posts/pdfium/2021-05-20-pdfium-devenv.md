---
layout: post
title: "工作笔记 PDFium -- 开发环境，PDFium 编译"
author:
location: "珠海"
categories: ["工作笔记"]
tags: ["PDFium", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "PDFium 编译"
---

* [基于开源 PDFium，编译动态库 -- Windows 平台（上） {% include relref_cnblogs.html %}](https://www.cnblogs.com/purehol/p/11734015.html)
* [基于开源 PDFium，编译动态库 -- Windows 平台（下） {% include relref_cnblogs.html %}](https://www.cnblogs.com/purehol/p/11734014.html)
* 编译 pdfium 为 一个 静态库。[Google's pdfium codebase set up as a Visual Studio solution that compiles to a static library on Windows. {% include relref_github.html %}](https://github.com/jwezorek/vs_pdfium)
* 编译好的直接用。[📰 Binary distribution of PDFium {% include relref_github.html %}](https://github.com/bblanchon/pdfium-binaries)


## ninja 编译 pdfium


### 环境准备

* 确保 path 里没有自己安装的 python.exe
    * depot_tools 貌似是：Python 2.7.18
    * 一个环境安装多个 python 的方法：[Windows 上通过 bat 避免 python 冲突]({% include relref.html url="/blog/2020/12/15/Visual-Studio#windows-%E4%B8%8A%E9%80%9A%E8%BF%87-bat-%E9%81%BF%E5%85%8D-python-%E5%86%B2%E7%AA%81" %})
* 下载 安装 depot_tools：
    * from [depot_tools_tutorial(7) Manual Page](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html) Download the [depot_tools](https://storage.googleapis.com/chrome-infra/depot_tools.zip) bundle and extract it somewhere.
    * 加入环境变量：`C:\kSource\kpdf\depot_tools`
* kernel32.SetConsoleMode to enable ANSI sequences failed
    * [Console Virtual Terminal Sequences](https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)
    * 我本机 win10 不支持 彩色控制台，错误码是 87：
        ```cpp
  ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
  if (mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING) == 0:
          SetConsoleMode(h, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
  return True
```
    * 感觉是一个 `depot_tools\setup_color.py` bug，修改一下它的源代码：<span imgid="20210521155505" />

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
For details search for DEPOT_TOOLS_WIN_TOOLCHAIN in the instructions at <https://chromium.googlesource.com/chromium/src/+/HEAD/docs/windows_build_instructions.md>


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
is_debug = false # 生成 release 库时关闭调试配置。

# 设置为启用实验性 Skia 后端。
pdf_use_skia = false
# 设置为启用实验性 Skia 后端（仅限路径）。
pdf_use_skia_paths = false

pdf_enable_xfa = false # 设置 false 以删除 XFA 支持（隐含 JS 支持）。
pdf_enable_v8 = false # 设置 false 以删除 Javascript 支持。
pdf_is_standalone = true # 设置非嵌入式构建。
# true 启用组件构建，可生成 pdfium.dll；false 更适合静态库场景。
is_component_build = true # 本文编译动态库，所以启用组件构建。
# pdf_is_complete_lib 为 false 时，编译为多个静态库，true 编译为一个独立的静态库
# 编译为一个独立的静态库（is_component_build 必须为 false）
# pdf_is_complete_lib = true

clang_use_chrome_plugins = false # 当前必须为 false。
# cpu 架构；x86、x64 可选
target_cpu = "x86" # 默认就是编译 x64 平台，编 x86 平台就需要修改了。
# true 将用 clang 进行编译，false 将用 VS2019 编译
# is_clang = false
```

vs_toolchain.py 构建配置脚本会读取：`path = os.environ.get('vs%s_install' % version)`
* KeyError: 'WINDOWSSDKDIR'
    * 如果您的 Visual Studio 安装在非默认目录中， 您需要 设置几个环境变量来将工具链指向您的安装路径。
    * **vs2019_install** = DRIVE:\path\to\Microsoft Visual Studio\2019\Community, replacing 2019 and Community with your installed versions and replacing DRIVE: with the drive that Visual Studio is on. Often, this will be C:.
        * `C:\Program Files (x86)\Microsoft Visual Studio\2019\Community`
    * **WINDOWSSDKDIR** = DRIVE:\path\to\Windows Kits\10, replacing DRIVE: with the drive that Windows Kits is on. Often, this will be C:.
        * `C:\Program Files (x86)\Windows Kits\10`
    * 读取环境变量还有点问题。<span imgid="vs_toolchain_bugfix" />
      ```python
if path and path[0] in ("\"", "'"): path = path[1:]
if path and path[-1] in ("\"", "'"): path = path[:-1]
path = path.replace("\\\\", "\\")
#print("NormalizePath", path) # 一定不能打印东西，打印了就相当于报错了。
```
* You must install Windows 10 SDK version 10.0.19041.0 including the "Debugging Tools for Windows" feature.
    * <https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/>

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


## VS2019

要安装带缓解的 mfc。很多第三方库用到了 mfc，能装的都装一下吧。
* 适用于最新 v142 生成工具的 C++ MFC (x86 和 x64)
    * 包含用于开发 MFC 应用程序的标头和库，包含多字节字符集（MBCS）。
* 也不要动不动就 git clean up，这玩意会删除 `pdfium\third_party\llvm-build\Release+Asserts\bin\clang-cl.exe`

```
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_MSVS_VERSION=2019

gn help gen
gn gen build/Debug
gn gen --ide=vs2019 --sln=pdfium build/Debug --args="use_goma=false is_debug=true pdf_use_skia=false pdf_use_skia_paths=false pdf_enable_xfa=false pdf_enable_v8=false pdf_is_standalone=true is_component_build=true clang_use_chrome_plugins=false target_cpu=\"x86\""
gn gen --ide=xcode --workspace=pdfium build/Debug --args="is_debug=true"

gn args build/Debug
gn args build/Debug --list --short
gn args build/Debug --list=target_cpu
gn help host_os
```

```
set DEPOT_TOOLS_WIN_TOOLCHAIN=0
set GYP_MSVS_VERSION=2019

C:\kSource\kpdf\google\pdfium>gn gen --ide=vs2019 --sln=pdfium build/Debug --args="use_goma=false is_debug=true pdf_use_skia=false pdf_use_skia_paths=false pdf_enable_xfa=false pdf_enable_v8=false pdf_is_standalone=true is_component_build=true clang_use_chrome_plugins=false target_cpu=\"x86\""
Generating Visual Studio projects took 133ms
Done. Made 154 targets from 94 files in 25889ms
```

{% include image.html url="/assets/images/210520-pdfium-devenv/20210524232030.png" %}

**要多编译几次，感觉 146 个工程，没有做项目依赖。**


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



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-20-pdfium-devenv.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/purehol/p/11734015.html]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/www.cnblogs.com/3ef3a595.html" %})
- [https://www.cnblogs.com/purehol/p/11734014.html]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/www.cnblogs.com/4100beaf.html" %})
- [https://github.com/jwezorek/vs_pdfium]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/github.com/dcd83ec9.html" %})
- [https://github.com/bblanchon/pdfium-binaries]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/github.com/e073027d.html" %})
- [https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/commondatastorage.googleapis.com/7437eefa.html" %})
- [https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/docs.microsoft.com/86a6c045.html" %})
- [https://pdfium.googlesource.com/pdfium.git]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/pdfium.googlesource.com/7e24f626.git" %})
- [https://chromium.googlesource.com/chromium/src/+/HEAD/docs/windows_build_instructions.md]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/chromium.googlesource.com/4e232b39.html" %})
- [https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/]({% include relrefx.html url="/backup/2021-05-20-pdfium-devenv.md/developer.microsoft.com/633f452d.html" %})
