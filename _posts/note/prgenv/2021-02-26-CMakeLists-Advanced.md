---
layout: post
title: "编程配置 -- CMake CMakeLists.txt 高级特性"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "Android"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---


## 其它

* add_subdirectory 最好在 include_directories 前面，否则 incdir 会形成递归重复。


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

- [https://blog.csdn.net/iceboy314159/article/details/104696565]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/blog.csdn.net/28e181b5.html" %})
- [https://www.cnblogs.com/likemao/p/11061951.html]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/97ec105a.html" %})
- [https://www.cnblogs.com/zjutzz/p/7284114.html]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.cnblogs.com/57bb48f4.html" %})
- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.4-chinese.md]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/04ed1da9.html" %})
- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.5-chinese.md]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/9a399d1f.html" %})
