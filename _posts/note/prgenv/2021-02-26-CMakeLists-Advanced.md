---
layout: post
title: "编程与调试 -- CMake CMakeLists.txt 高级特性"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "Android", "CMake"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "CMake"
---

**前面一篇文章。[编程配置 -- Android CMake CMakeLists.txt 构建配置文件]({% include relref.html url="/blog/2021/02/01/cmakelists" %})**

[^_^]: <http://jekyllcn.com/docs/templates/>


## $<$<CONFIG:Debug>:Release> $<$<CONFIG:Release>:Debug>

這是一個 CMake generator expression。
像 $<...>這樣的表達式是在 CMake 2.8 中引入的 generator exressions。這些表達式的主要特徵是它們在構建時進行評估，而不是在配置時進行評估，就像正常的 CMake 變量一樣。
<https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html>

```cmake
if current_configuration == "Debug"
    output "Release"
if current_configureation == "Release"
    output "Debug"

set(RCFILE app.rc)
source_group("rcfile" FILES ${RCFILE})
set_source_files_properties(${RCFILE} PROPERTIES LANGUAGE RC)
```


## 编译期函数返回值检查

```cmake
# MacOS     -Winconsistent-missing-override
# GCC 5.1   -Werror=suggest-override
# -pthread for g++
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x -pthread -Werror=return-type")
```


### 通过编译选项将特定警告视为错误

* [编写合格的 C 代码（1）：通过编译选项将特定警告视为错误 {% include relref_cnblogs.html %}](https://www.cnblogs.com/zjutzz/p/10802138.html)
    * A simple logging library implemented in C99 [rxi / log.c {% include relref_github.html %}](https://github.com/rxi/log.c)
    * Getting colored output working on Windows [github {% include relref_github.html %}](https://github.com/rspec/rspec/wiki/Getting-colored-output-working-on-Windows)
* [编写合格的 C 代码（2）：实现简易日志库 {% include relref_cnblogs.html %}](https://www.cnblogs.com/zjutzz/p/11333334.html)

* 开启 安全开发生命周期（SDL）检查
* CMakeLists.txt 中的设定
  ```cmake
if (CMAKE_SYSTEM_NAME MATCHES "Windows")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} /we4715 /we4013 /we4431 /we4133 /we4716 /we6244 /we6246 /we4457 /we4456 /we4172 /we4700 /we4477 /we4018 /we4047")
    set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} /we4715 /we4013 /we4431 /we4133 /we4716 /we6244 /we6246 /we4457 /we4456 /we4172 /we4700 /we4477 /we4018 /we4047")
elseif (CMAKE_SYSTEM_NAME MATCHES "Linux" OR CMAKE_SYSTEM_NAME MATCHES "Darwin")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Werror=implicit-function-declaration -Werror=implicit-int -Werror=incompatible-pointer-types -Werror=return-type -Werror=shadow -Werror=return-local-addr -Werror=uninitialized -Werror=format -Werror=sign-compare -Werror=int-conversion")
    set(CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS} -Werror=implicit-function-declaration -Werror=implicit-int -Werror=incompatible-pointer-types -Werror=return-type -Werror=shadow -Werror=return-local-addr -Werror=uninitialized -Werror=format -Werror=sign-compare -Werror=int-conversion")
endif()
```
* Visual Studio 中的设定
    * 项目属性->配置属性->C/C++->高级->将特定的警告视为错误，填入相应的警告、错误代号：
        * 4715;4013;4431;4133;4716;6244;6246;4457;4456;4172;4700;4477;4018;4047
* 基于 Makefile
    * CFLAGS += -Werror=implicit-function-declaration -Werror=implicit-int -Werror=incompatible-pointer-types -Werror=return-type -Werror=shadow -Werror=return-local-addr -Werror=uninitialized -Werror=format -Werror=sign-compare -Werror=int-conversion
* 直接调用 gcc/clang
    * gcc xxx.c -Werror=implicit-function-declaration -Werror=implicit-int -Werror=incompatible-pointer-types -Werror=return-type -Werror=shadow -Werror=return-local-addr -Werror=uninitialized -Werror=format -Werror=sign-compare -Werror=int-conversion


### How to convert warning C4715 to error

C4715：不是所有的控件路径都返回值。Two ways of doing this
`#pragma warning (error : 4715)`
Compiling with `/we4715` option passed to cl.exe

[PlatformWindowsMSVC.cmake {% include relref_github.html %}](https://github.com/kateyy/geohazardvis/blob/master/cmake/PlatformWindowsMSVC.cmake)

```cmake
# MacOS     -Winconsistent-missing-override
# GCC 5.1   -Werror=suggest-override
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread") # -pthread for g++
if (MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /we4715") # makes missing return as error
endif()

# version specific compile flags
# 1800: Visual Studio 12 2013
# 1900: Visual Studio 14 2015
if (MSVC_VERSION VERSION_LESS 1900)

    list(APPEND DEFAULT_COMPILE_FLAGS
        <<CONFIG:Debug>: /Zi>     # this is set in RelWithDebInfo builds for all MSVC versions
        <<CONFIG:RelNoOptimization>: /Zi>
    )

else() # Visual Studio 14 2015 as minimum

    list(APPEND DEFAULT_COMPILE_FLAGS
        /Zc:referenceBinding /Zc:strictStrings /Zc:throwingNew
        # allow native edit and continue
        <<CONFIG:Debug>:             /ZI>
        <<CONFIG:RelNoOptimization>: /ZI>
        # Enable compiler generation of Control Flow Guard security checks. (incompatible with /ZI)
        <<CONFIG:Release>:           /guard:cf>
        <<CONFIG:RelWithDebInfo>:    /guard:cf>
    )
endif()
```


## Notes

* add_subdirectory 最好在 include_directories 前面，否则 incdir 会形成递归重复。
* [cmake 函数参数解析 {% include relref_csdn.html %}](https://blog.csdn.net/sakaue/article/details/38377661)
    * ${SRC} 在 function 外是完整的 4 个元素，而在 function 却只剩下了头一个元素。
    * [cmake_parse_arguments(MY_INSTALL "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN} ) from](https://cmake.org/cmake/help/v3.0/module/CMakeParseArguments.html?highlight=cmake_parse_arguments)


## CMake 设置 VS 工程筛选器

[from {% include relref_csdn.html %}](https://blog.csdn.net/iceboy314159/article/details/104696565)
[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/likemao/p/11061951.html)

```cmake
source_group(main FILES ${SOURCES})
source_group(math FILES ${MATHSRC})
source_group(math\\matrix FILES ${MATSRC})
source_group(uav FILES ${UAVSRC})

# Create the source groups for source tree with root at CMAKE_CURRENT_SOURCE_DIR.
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${SOURCE_LIST})

# https://github.com/juj/MathGeoLib/blob/master/CommonOptions.cmake
# Add the global _DEBUG flag from WIN32 platform to all others, which is universally used in MGL to
# perform debug-mode-specific compilation.
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -D_DEBUG")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -D_DEBUG")
```


## 参数定义

```cmake
if (CMAKE_CL_64)
    add_definitions(-D_WIN64)
endif()

set(JSON_BuildTests OFF CACHE INTERNAL "") # 外面
# 里面：
option(JSON_BuildTests "Build the unit tests when BUILD_TESTING is enabled." ON)
    if (BUILD_TESTING AND JSON_BuildTests) ...
```

[from {% include relref_cnblogs.html %}](https://www.cnblogs.com/zjutzz/p/7284114.html)

```cmake
cmake_minimum_required(VERSION 3.1)

project(hello)

function(assign_source_group)
    foreach(_source IN ITEMS ${ARGN})
        if (IS_ABSOLUTE "${_source}")
            file(RELATIVE_PATH _source_rel "${CMAKE_CURRENT_SOURCE_DIR}" "${_source}")
        else()
            set(_source_rel "${_source}")
        endif()
        get_filename_component(_source_path "${_source_rel}" PATH)
        string(REPLACE "/" "\\" _source_path_msvc "${_source_path}")
        source_group("${_source_path_msvc}" FILES "${_source}")
    endforeach()
endfunction(assign_source_group)

function(my_add_executable)
    foreach(_source IN ITEMS ${ARGN})
        assign_source_group(${_source})
    endforeach()
    add_executable(${ARGV})
endfunction(my_add_executable)

my_add_executable(hello include/hello.hpp src/hello.cpp)
```


## skylicht-engine vsSourceGroup.cmake

```cmake
# group source on visual project
# setup_project_group(PROJ_SRCS ${PROJ_SRCS} CUR_DIR ${CUR_DIR})
function(setup_project_group)

    CMAKE_PARSE_ARGUMENTS(
        ARGV "" "CUR_DIR" "PROJ_SRCS"
        ${ARGN}
    )

    foreach(source IN LISTS ARGV_PROJ_SRCS)
        # get source path
        get_filename_component(source_path ${source} PATH)

        # get source relative path
        string(REPLACE "${ARGV_CUR_DIR}/./" "" source_relative ${source_path})

        if (MSVC OR XCODE)
            # get group name
            string(REPLACE "/" "\\" group_name ${source_relative})
        else()
            set(group_name ${source_relative})
        endif()

        if ("${source_relative}" STREQUAL "${source_path}")
            source_group("${group_name}" FILES "${source}")
            # no need group because source is in $ARGV_CUR_DIR
        else()
            # setup project group
            source_group("${group_name}" FILES "${source}")
        endif()
    endforeach()
endfunction()

function(add_source_group)

    CMAKE_PARSE_ARGUMENTS(
        ARGV "" "GROUP_NAME" "PROJ_SRCS"
        ${ARGN}
    )

    foreach(source IN LISTS ARGV_PROJ_SRCS)
        # setup project group
        source_group("${ARGV_GROUP_NAME}" FILES "${source}")
    endforeach()
endfunction()
```


## skylicht-engine vsPCH.cmake

```cmake
function(target_precompiled_header project_target pch_source)
if (MSVC)
    get_filename_component(pch_basename ${pch_source} NAME_WE)
    set(pch_header "${pch_basename}.h")

    set_target_properties(${project_target} PROPERTIES COMPILE_FLAGS "/Yu${pch_header}")
    set_source_files_properties(${pch_source} PROPERTIES COMPILE_FLAGS "/Yc${pch_header}")
endif(MSVC)
endfunction()
```


## function vs macro

可以看到，Moo 这个宏的表现与 C 语言中的宏类似，仅仅是做字符串的替换；
Foo 函数里 arg 则是被赋值为 var 的值，在 Foo 内部可以修改这个 arg 变量的值。

```cmake
set(var "ABC")

macro(Moo arg)
  message("arg = ${arg}")
  set(arg "abc")
  message("# After change the value of arg.")
  message("arg = ${arg}")
endmacro()
message("=== Call macro ===")
Moo(${var})

function(Foo arg)
  message("arg = ${arg}")
  set(arg "abc")
  message("# After change the value of arg.")
  message("arg = ${arg}")
endfunction()
message("=== Call function ===")
Foo(${var})
```

```
➜ /Users/userk/codes/local_codes/cmake_test/build cmake ..
=== Call macro ===
arg = ABC
# After change the value of arg.
arg = ABC
=== Call function ===
arg = ABC
# After change the value of arg.
arg = abc
```


## 重新定义函数和宏

[7.4 用指定参数定义函数或宏](https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.4-chinese.md)
[7.5 重新定义函数和宏](https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.5-chinese.md)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-26-CMakeLists-Advanced.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://jekyllcn.com/docs/templates/]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/jekyllcn.com/a06345ca.html" %})
- [https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/cmake.org/1e5863d8.html" %})
- [https://www.cnblogs.com/zjutzz/p/10802138.html]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/66780ceb.html" %})
- [https://github.com/rxi/log.c]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/github.com/e00aa14a.html" %})
- [https://github.com/rspec/rspec/wiki/Getting-colored-output-working-on-Windows]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/github.com/7a35e51b.html" %})
- [https://www.cnblogs.com/zjutzz/p/11333334.html]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/5687afa3.html" %})
- [https://github.com/kateyy/geohazardvis/blob/master/cmake/PlatformWindowsMSVC.cmake]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/github.com/95b75574.html" %})
- [https://blog.csdn.net/sakaue/article/details/38377661]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/blog.csdn.net/0f86d44d.html" %})
- [https://cmake.org/cmake/help/v3.0/module/CMakeParseArguments.html?highlight=cmake_parse_arguments]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/cmake.org/0fae8de9.html" %})
- [https://blog.csdn.net/iceboy314159/article/details/104696565]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/blog.csdn.net/28e181b5.html" %})
- [https://www.cnblogs.com/likemao/p/11061951.html]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/97ec105a.html" %})
- [https://github.com/juj/MathGeoLib/blob/master/CommonOptions.cmake]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/github.com/24e305e7.html" %})
- [https://www.cnblogs.com/zjutzz/p/7284114.html]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/57bb48f4.html" %})
- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.4-chinese.md]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/04ed1da9.html" %})
- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.5-chinese.md]({% include relrefx.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/9a399d1f.html" %})
