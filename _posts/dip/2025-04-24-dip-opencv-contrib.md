---
layout: post
title: "图像处理 -- Windows cv::freetype::FreeType2"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

mkdir build && cd build
cmake -G "Visual Studio 16 2019" -T v142 ..
cmake --build . --config Release

cmake -S . -G "Visual Studio 16 2019" -T v142 -B build
cmake --build build --config Release
cmake .. -G "Visual Studio 16 2019" -T v142

cmake -G "Visual Studio 16 2019" -T v142 -DCMAKE_INSTALL_PREFIX="install_x86" -A "Win32" ..


## 安装 freetype 和 harfbuzz（通过 vcpkg）

```
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg
bootstrap-vcpkg.bat
vcpkg install freetype:x64-windows harfbuzz:x64-windows
vcpkg install pkgconf:x64-windows
```

vcpkg install freetype:x86-windows harfbuzz:x86-windows
vcpkg install pkgconf:x86-windows


## 克隆 OpenCV 和 opencv_contrib

```
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

cmake -S . -G "Visual Studio 16 2019" -T v142 -B build

mkdir opencv_build
cd opencv_build

同目录：
* /opencv_build
* /opencv
* /opencv_contrib
* /vcpkg
* /install

set PKG_CONFIG_EXECUTABLE=I:\opencv_work\vcpkg\packages\pkgconf_x64-windows\tools\pkgconf\pkgconf.exe
set PKG_CONFIG_PATH=I:\opencv_work\vcpkg\installed\x64-windows\lib\pkgconfig

"I:\opencv_work\vcpkg\packages\pkgconf_x64-windows\tools\pkgconf\pkgconf.exe" --modversion freetype2

set PKG_CONFIG_EXECUTABLE=I:\opencv_work\vcpkg\packages\pkgconf_x86-windows\tools\pkgconf\pkgconf.exe
set PKG_CONFIG_PATH=I:\opencv_work\vcpkg\installed\x86-windows\lib\pkgconfig
"I:\opencv_work\vcpkg\packages\pkgconf_x86-windows\tools\pkgconf\pkgconf.exe" --modversion freetype2

```
cmake ^
 -G "Visual Studio 16 2019" -T v142 ^
 -A x64 ^
 -DCMAKE_INSTALL_PREFIX=I:/opencv_work/install ^
 -DOPENCV_EXTRA_MODULES_PATH=I:/opencv_work/opencv_contrib/modules ^
 -DWITH_FREETYPE=ON ^
 -DWITH_HARFBUZZ=ON ^
 -DWITH_TEXT=ON ^
 -DWITH_AVX2=ON ^
 -DENABLE_AVX=ON ^
 -DENABLE_SSE=ON ^
 -DENABLE_SSE2=ON ^
 -DENABLE_SSE3=ON ^
 -DENABLE_SSSE3=ON ^
 -DENABLE_SSE41=ON ^
 -DENABLE_SSE42=ON ^
 -DCMAKE_TOOLCHAIN_FILE=I:/opencv_work/vcpkg/scripts/buildsystems/vcpkg.cmake ^
 -DCMAKE_BUILD_TYPE=Release ^
 -DPKG_CONFIG_EXECUTABLE=I:/opencv_work/vcpkg/packages/pkgconf_x64-windows/tools/pkgconf/pkgconf.exe ^
 -DPKG_CONFIG_PATH=I:/opencv_work/vcpkg/installed/x64-windows/lib/pkgconfig ^
 -DFREETYPE_INCLUDE_DIR_ft2build=I:/opencv_work/vcpkg/packages/freetype_x64-windows/include ^
 -DFREETYPE_INCLUDE_DIR_freetype2=I:/opencv_work/vcpkg/packages/freetype_x64-windows/include/freetype ^
 -DHARFBUZZ_INCLUDE_DIRS=I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/include/harfbuzz ^
 I:/opencv_work/opencv

cmake ^
 -G "Visual Studio 16 2019" -T v142 ^
 -A x64 ^
 -DCMAKE_INSTALL_PREFIX=I:/opencv_work/install ^
 -DOPENCV_EXTRA_MODULES_PATH=I:/opencv_work/opencv_contrib/modules ^
 -DWITH_FREETYPE=ON ^
 -DWITH_HARFBUZZ=ON ^
 -DWITH_TEXT=ON ^
 -DCMAKE_TOOLCHAIN_FILE=I:/opencv_work/vcpkg/scripts/buildsystems/vcpkg.cmake ^
 -DCMAKE_BUILD_TYPE=Debug ^
 -DPKG_CONFIG_EXECUTABLE=I:/opencv_work/vcpkg/packages/pkgconf_x64-windows/tools/pkgconf/pkgconf.exe ^
 -DPKG_CONFIG_PATH=I:/opencv_work/vcpkg/installed/x64-windows/lib/pkgconfig ^
 -DFREETYPE_INCLUDE_DIR_ft2build=I:/opencv_work/vcpkg/packages/freetype_x64-windows/include ^
 -DFREETYPE_INCLUDE_DIR_freetype2=I:/opencv_work/vcpkg/packages/freetype_x64-windows/include/freetype ^
 -DHARFBUZZ_INCLUDE_DIRS=I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/include/harfbuzz ^
 I:/opencv_work/opencv
```

Win32 / x86 版本：
```
cmake ^
 -G "Visual Studio 16 2019" -T v142 ^
 -A Win32 ^
 -DCMAKE_INSTALL_PREFIX=I:/opencv_work/install ^
 -DOPENCV_EXTRA_MODULES_PATH=I:/opencv_work/opencv_contrib/modules ^
 -DWITH_FREETYPE=ON ^
 -DWITH_HARFBUZZ=ON ^
 -DWITH_TEXT=ON ^
 -DCMAKE_TOOLCHAIN_FILE=I:/opencv_work/vcpkg/scripts/buildsystems/vcpkg.cmake ^
 -DCMAKE_BUILD_TYPE=Release ^
 -DPKG_CONFIG_EXECUTABLE=I:/opencv_work/vcpkg/packages/pkgconf_x86-windows/tools/pkgconf/pkgconf.exe ^
 -DPKG_CONFIG_PATH=I:/opencv_work/vcpkg/installed/x86-windows/lib/pkgconfig ^
 -DFREETYPE_INCLUDE_DIR_ft2build=I:/opencv_work/vcpkg/packages/freetype_x86-windows/include ^
 -DFREETYPE_INCLUDE_DIR_freetype2=I:/opencv_work/vcpkg/packages/freetype_x86-windows/include/freetype ^
 -DHARFBUZZ_INCLUDE_DIRS=I:/opencv_work/vcpkg/packages/harfbuzz_x86-windows/include/harfbuzz ^
 I:/opencv_work/opencv

cmake ^
 -G "Visual Studio 16 2019" -T v142 ^
 -A Win32 ^
 -DCMAKE_INSTALL_PREFIX=I:/opencv_work/install ^
 -DOPENCV_EXTRA_MODULES_PATH=I:/opencv_work/opencv_contrib/modules ^
 -DWITH_FREETYPE=ON ^
 -DWITH_HARFBUZZ=ON ^
 -DWITH_TEXT=ON ^
 -DCMAKE_TOOLCHAIN_FILE=I:/opencv_work/vcpkg/scripts/buildsystems/vcpkg.cmake ^
 -DCMAKE_BUILD_TYPE=Debug ^
 -DPKG_CONFIG_EXECUTABLE=I:/opencv_work/vcpkg/packages/pkgconf_x86-windows/tools/pkgconf/pkgconf.exe ^
 -DPKG_CONFIG_PATH=I:/opencv_work/vcpkg/installed/x86-windows/lib/pkgconfig ^
 -DFREETYPE_INCLUDE_DIR_ft2build=I:/opencv_work/vcpkg/packages/freetype_x86-windows/include ^
 -DFREETYPE_INCLUDE_DIR_freetype2=I:/opencv_work/vcpkg/packages/freetype_x86-windows/include/freetype ^
 -DHARFBUZZ_INCLUDE_DIRS=I:/opencv_work/vcpkg/packages/harfbuzz_x86-windows/include/harfbuzz ^
 I:/opencv_work/opencv
```

```
cmake --build . --config Release --target INSTALL
cmake --build . --config Debug --target INSTALL
```

```
vcpkg/installed/x64-windows/include/
vcpkg/installed/x64-windows/lib/
vcpkg/installed/x64-windows/bin/
```

rmdir /s /q opencv_build
mkdir opencv_build
cd opencv_build

检查是否生效
配置完后，查看终端输出中是否有：
```
--   freetype:                 YES (ver ...)
--     harfbuzz:               YES (ver ...)
--     Module opencv_freetype will be built

-- FREETYPE_INCLUDE_DIRS:
-- FREETYPE_LIBRARIES:
-- HARFBUZZ_INCLUDE_DIRS: I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/include/harfbuzz
-- HARFBUZZ_LIBRARIES:
-- freetype2:   YES (ver )
-- harfbuzz:    YES (ver )
```


## 直接修改

freetype\CMakeLists.txt
I:\opencv_work\vcpkg\packages\pkgconf_x64-windows\tools\pkgconf\pkgconf.exe

```
# Manually specify the include and library directories for FreeType and HarfBuzz
set(FREETYPE_INCLUDE_DIR_ft2build "I:/opencv_work/vcpkg/packages/freetype_x64-windows/include")
set(FREETYPE_INCLUDE_DIR_freetype2 "I:/opencv_work/vcpkg/packages/freetype_x64-windows/include/freetype")
set(HARFBUZZ_INCLUDE_DIRS "I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/include/harfbuzz")

set(FREETYPE_FOUND 1)
set(HARFBUZZ_FOUND 1)

if (NOT FREETYPE_FOUND)
  message(FATAL_ERROR "FREETYPE not found. Make sure freetype2.pc is available via pkg-config or set manually.")
endif()

if (NOT HARFBUZZ_FOUND)
  message(FATAL_ERROR "HARFBUZZ not found. Make sure harfbuzz.pc is available via pkg-config or set manually.")
endif()

message(STATUS "FREETYPE_INCLUDE_DIRS: ${FREETYPE_INCLUDE_DIRS}")
message(STATUS "FREETYPE_LIBRARIES: ${FREETYPE_LIBRARIES}")
message(STATUS "HARFBUZZ_INCLUDE_DIRS: ${HARFBUZZ_INCLUDE_DIRS}")
message(STATUS "HARFBUZZ_LIBRARIES: ${HARFBUZZ_LIBRARIES}")
```

```
# 根据 CMAKE_BUILD_TYPE 变量设置库路径
if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    # Debug 构建时使用 debug 库
    set(FREETYPE_LIBRARY_RELEASE "I:/opencv_work/vcpkg/packages/freetype_x64-windows/debug/lib/freetyped.lib")
    set(HARFBUZZ_LIBRARY "I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/debug/lib/harfbuzz.lib")
else()
    # Release 构建时使用 release 库
    set(FREETYPE_LIBRARY_RELEASE "I:/opencv_work/vcpkg/packages/freetype_x64-windows/lib/freetype.lib")
    set(HARFBUZZ_LIBRARY "I:/opencv_work/vcpkg/packages/harfbuzz_x64-windows/lib/harfbuzz.lib")
endif()

if (FREETYPE_FOUND AND HARFBUZZ_FOUND)
  ocv_define_module(freetype opencv_core opencv_imgproc WRAP python)
  ocv_target_link_libraries(${the_module} ${FREETYPE_LIBRARIES} ${HARFBUZZ_LIBRARIES}
    ${FREETYPE_LIBRARY_RELEASE} ${HARFBUZZ_LIBRARY}
  )
  ocv_include_directories( ${FREETYPE_INCLUDE_DIRS} ${HARFBUZZ_INCLUDE_DIRS}
    "I:/opencv_work/vcpkg/packages/freetype_x64-windows/include"
    "I:/opencv_work/vcpkg/packages/freetype_x64-windows/include/freetype"
  )
else()
  ocv_module_disable(freetype)
endif()
```

编译时确保链接了 opencv_freetype470.lib 以及 opencv_world470.lib 或其他相关模块。

* /vcpkg/packages/freetype_x64-windows/debug/lib/freetyped.lib
* /vcpkg/packages/freetype_x64-windows/lib/freetype.lib
* /vcpkg/packages/freetype_x64-windows/include
* /vcpkg/packages/freetype_x64-windows/include/freetype

* /vcpkg/packages/harfbuzz_x64-windows/debug/lib/harfbuzz.lib
* /vcpkg/packages/harfbuzz_x64-windows/lib/harfbuzz.lib
* /vcpkg/packages/harfbuzz_x64-windows/include/harfbuzz



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-04-24-dip-opencv-contrib.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/microsoft/vcpkg.git]({% include relrefx.html url="/backup/2025-04-24-dip-opencv-contrib.md/github.com/9cce1220.html" %})
- [https://github.com/opencv/opencv.git]({% include relrefx.html url="/backup/2025-04-24-dip-opencv-contrib.md/github.com/59192dea.html" %})
- [https://github.com/opencv/opencv_contrib.git]({% include relrefx.html url="/backup/2025-04-24-dip-opencv-contrib.md/github.com/d443124b.html" %})
