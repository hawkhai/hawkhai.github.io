---
layout: post
title: "编程 C++ -- CMake CMakeLists.txt 构建配置文件"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## CMake 编译一个简单 C++ 项目

```
ROOT -- CMakeLists.txt addlib build main.cpp
                         +-- CMakeLists.txt library.cpp library.h
```


### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10)
project(cppproject)

set(CMAKE_CXX_STANDARD 11)

add_subdirectory(acclib)

add_executable(cppproject main.cpp) # 生成一个可执行的文件
target_link_libraries(cppproject accliblibrary)
```


### addlib/CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10)
project(accliblibrary)

set(CMAKE_CXX_STANDARD 11)

add_library(accliblibrary SHARED library.cpp library.h) # 诉生成一个库文件。
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-01-cmakelists.md.js" %}'></script></p>
