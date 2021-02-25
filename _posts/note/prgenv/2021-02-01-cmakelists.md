---
layout: post
title: "编程配置 -- Android CMake CMakeLists.txt 构建配置文件"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

每次都想走捷径，最后还是得倒回来，认认真真学习这些鸟语法。


## 基本使用

[Android CMake DOC](https://developer.android.com/studio/projects/configure-cmake)
[CMake 命令的官方文档](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html)

```cmake
cmake_minimum_required(VERSION 3.4.1)

# 指定一个本地头文件路径。
include_directories(src/main/cpp/include/)
# 编译构建
add_library( native-lib # 指定 lib 名称。
             SHARED # 设置为 shared lib。
             # 源代码位置。
             src/main/cpp/native-lib.cpp )

# 构建一个 STATIC lib。
add_library( app-glue
             STATIC
             ${ANDROID_NDK}/sources/android/native_app_glue/android_native_app_glue.c )
# 检索一个 lib。
find_library( log-lib # 定义一个 NDK lib 名字。
              # CMake 去查找 CMake lib 的名字。
              log )
# 导入一个 lib。
add_library( imported-lib # 导入一个 lib
             SHARED
             IMPORTED )
set_target_properties( imported-lib # 导入 lib 名字。
                       PROPERTIES IMPORTED_LOCATION # 需要的参数
                       imported-lib/src/${ANDROID_ABI}/libimported-lib.so )

# 连接一个静态 lib。
target_link_libraries( native-lib imported-lib app-glue ${log-lib} )

# 设置路径
set( lib_src_DIR ../gmath )
set( lib_build_DIR ../gmath/outputs )
file(MAKE_DIRECTORY ${lib_build_DIR}) # 创建路径。

# 子构建目录依赖。
add_subdirectory( ${lib_src_DIR} # CMakeLists.txt 文件夹
                  # 指定 build 文件夹。
                  ${lib_build_DIR} )

add_library( lib_gmath STATIC IMPORTED )
set_target_properties( lib_gmath PROPERTIES IMPORTED_LOCATION
                       ${lib_build_DIR}/${ANDROID_ABI}/lib_gmath.a )
include_directories( ${lib_src_DIR}/include )
target_link_libraries( native-lib ... lib_gmath )
```

target_link_libraries 为库或二进制可执行文件添加库链接，要用在 add_executable 之后。
上述指令中的 target 是指通过 add_executable() 和 add_library() 指令生成已经创建的目标文件。


### 区分不同平台

* **ANDROID**：安卓的编译环境；
* **APPLE**：是否是苹果系列的编译环境；
* **IOS**：是否是苹果手机环境；
* **UNIX**：是否是 UNIX 或者 UNIX-like 的环境；
* **WIN32、MSVC**：是否是 Windows。

Android.mk & Application.mk

* **LOCAL_CFLAGS** 可选的编译器选项，在编译 C 代码文件的时候使用。
* **LOCAL_CXXFLAGS** Same as LOCAL_CFLAGS for C++ source files
* **LOCAL_CPPFLAGS** 与 LOCAL_CFLAGS 相同，但是对 C 和 C++ source files 都适用。


## CMake 预定义变量

* **PROJECT\_SOURCE\_DIR** 工程的根目录
* **PROJECT\_BINARY\_DIR** 运行 cmake 命令的目录，通常是 ${PROJECT\_SOURCE\_DIR}/build
* **CMAKE\_INCLUDE\_PATH** 环境变量，非 cmake 变量
* **CMAKE\_LIBRARY\_PATH** 环境变量
* **CMAKE\_CURRENT\_SOURCE\_DIR** 当前处理的 CMakeLists.txt 所在的路径
* **CMAKE\_CURRENT\_BINARY\_DIR** target 编译目录
    * 使用 ADD\_SURDIRECTORY(src bin) 可以更改此变量的值
    * SET(EXECUTABLE\_OUTPUT\_PATH &lt;newPath>) 并不会对此变量有影响，只是改变了最终目标文件的存储路径
* **CMAKE\_CURRENT\_LIST\_FILE** 输出调用这个变量的 CMakeLists.txt 的完整路径
* **CMAKE\_CURRENT\_LIST\_LINE** 输出这个变量所在的行
* **CMAKE\_MODULE\_PATH** 定义自己的 cmake 模块所在的路径
    * SET(CMAKE\_MODULE\_PATH ${PROJECT\_SOURCE\_DIR}/cmake)，然后可以用 INCLUDE 命令来调用自己的模块
* **EXECUTABLE\_OUTPUT\_PATH** 重新定义目标二进制可执行文件的存放位置
* **LIBRARY\_OUTPUT\_PATH** 重新定义目标链接库文件的存放位置
* **PROJECT\_NAME** 返回通过 PROJECT 指令定义的项目名称
* **CMAKE\_ALLOW\_LOOSE\_LOOP\_CONSTRUCTS** 用来控制 IF ELSE 语句的书写方式

```cmake
PROJECT(T1)
SET(SRC_LIST main.cpp)

MESSAGE(STATUS "This is the binary dir: " ${PROJECT_BINARY_DIR})
MESSAGE(STATUS "This is the source dir: " ${PROJECT_SOURCE_DIR})

# 此处的 t1 跟 PROJECT 定义的 T1 没什么关系
ADD_EXECUTABLE(t1 ${SRC_LIST})
```

系统信息
* **CMAKE\_MAJOR\_VERSION** cmake 主版本号，如 2.8.6 中的 2
* **CMAKE\_MINOR\_VERSION** cmake 次版本号，如 2.8.6 中的 8
* **CMAKE\_PATCH\_VERSION** cmake 补丁等级，如 2.8.6 中的 6
* **CMAKE\_SYSTEM** 系统名称，例如 Linux-2.6.22
* **CAMKE\_SYSTEM\_NAME** 不包含版本的系统名，如 Linux
* **CMAKE\_SYSTEM\_VERSION** 系统版本，如 2.6.22
* **CMAKE\_SYSTEM\_PROCESSOR** 处理器名称，如 i686
* **UNIX** 在所有的类 UNIX 平台为 TRUE，包括 OS X 和 cygwin
* **WIN32** 在所有的 win32 平台为 TRUE，包括 cygwin

开关选项
* **BUILD\_SHARED\_LIBS** 控制默认的库编译方式。
    * 如果未进行设置，使用 ADD\_LIBRARY 时又没有指定库类型，默认编译生成的库都是静态库 （可在 t3 中稍加修改进行验证）
* **CMAKE\_C\_FLAGS** 设置 C 编译选项
* **CMAKE\_CXX\_FLAGS** 设置 C++ 编译选项

```cmake
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(T3)
# 若变量 BUILD_SHARED_LIBS 没有设置，并且在 ADD_LIBRARY 时没有指定库类型
# 默认生成的都是静态库
# SET(BUILD_SHARED_LIBS on)
ADD_SUBDIRECTORY(lib_hello)
```

```cmake
AUX_SOURCE_DIRECTORY(. SRC_LIST)
ADD_LIBRARY(hello_shared SHARED ${SRC_LIST}) # lib 的名字不能重复
ADD_LIBRARY(hello_static STATIC ${SRC_LIST})
SET_TARGET_PROPERTIES(hello_static PROPERTIES OUTPUT_NAME "hello")
SET_TARGET_PROPERTIES(hello_shared PROPERTIES OUTPUT_NAME "hello")

# 设置动态库的版本号
SET_TARGET_PROPERTIES(hello_shared PROPERTIES VERSION 1.2 SOVERSION 1)

# 如果发现后来生成的 lib 清除了同名的早先生成的 lib，（只有一个静态库或动态库生成）
# 试下下面两个命令
# 较新版本的 cmake 不再需要下面两个命令就可以同时生成 hello.so hello.a
#SET_TARGET_PROPERTIES(hello_shared PROPERTIES CLEAN_DIRECT_OUTPUT 1)
#SET_TARGET_PROPERTIES(hello_static PROPERTIES CLEAN_DIRECT_OUTPUT 1)
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
```


## CMake 常用命令


### 基本语法规则

* cmake 变量使用 ${} 方式取值，但是在 IF 控制语句中是直接使用变量名
* 环境变量使用 $ENV{} 方式取值，使用 SET(ENV{VAR} VALUE) 赋值
* 指令 (arg1 arg2...) 参数使用括弧括起，参数之间使用空格或分号分开。

  ```cmake
  以 ADD_EXECUTABLE 指令为例：
  ADD_EXECUTABLE(hello main.c func.c) 或者
  ADD_EXECUTABLE(hello main.c;func.c)
  ```

* 指令是大小写无关的，参数和变量是大小写相关的。推荐你全部使用 **大写** 指令。


### PROJECT

* `PROJECT(projectname [CXX] [C] [Java])`
* 指定工程名称，并可指定工程支持的语言。支持语言列表可忽略，默认支持所有语言


### SET

* `SET(VAR [VALUE] [CACHE TYPE DOCSTRING [FORCE]])`
* 定义变量（可以定义多个 VALUE，如 SET(SRC\_LIST main.c util.c reactor.c))


### MESSAGE

* `MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display" ...)`
* 向终端输出用户定义的信息或变量的值
    * SEND\_ERROR，产生错误，生成过程被跳过
    * STATUS，输出前缀为 -- 的信息
    * FATAL\_ERROR，立即终止所有 cmake 过程


### ADD\_EXECUTABLE

* `ADD_EXECUTABLE(bin_file_name ${SRC_LIST})`
* 生成可执行文件


### ADD\_LIBRARY

* `ADD_LIBRARY(libname [SHARED | STATIC | MODULE] [EXCLUDE_FROM_ALL] SRC_LIST)`
* 生成动态库或静态库
    * SHARED 动态库
    * STATIC 静态库
    * MODULE 在使用 dyld 的系统有效，若不支持 dyld，等同于 SHARED
    * EXCLUDE\_FROM\_ALL 表示该库不会被默认构建


### SET\_TARGET\_PROPERTIES

* 设置输出的名称，设置动态库的版本和 API 版本


### CMAKE\_MINIMUM\_REQUIRED

* `CMAKE_MINIMUM_REQUIRED(VERSION version_number [FATAL_ERROR])`
* 声明 CMake 的版本要求


### ADD\_SUBDIRECTORY

* `ADD_SUBDIRECTORY(src_dir [binary_dir] [EXCLUDE_FROM_ALL])`
* 向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制的存放位置
* EXCLUDE\_FROM\_ALL 含义：将这个目录从编译过程中排除


### ~~SUBDIRS~~

* **deprecated**，不再推荐使用
* (hello sample) 相当于分别写 ADD\_SUBDIRECTORY(hello), ADD\_SUBDIRECTORY(sample)


### INCLUDE\_DIRECTORIES

* `INCLUDE_DIRECTORIES([AFTER | BEFORE] [SYSTEM] dir1 dir2 ... )`
* 向工程添加多个特定的头文件搜索路径，路径之间用空格分隔，如果路径包含空格，
    可以使用双引号将它括起来，默认的行为为追加到当前头文件搜索路径的后面。有如下两种方式可以控制搜索路径添加的位置：
    * CMAKE\_INCLUDE\_DIRECTORIES\_BEFORE，通过 SET 这个 cmake 变量为 on，可以将添加的头文件搜索路径放在已有路径的前面
* 通过 AFTER 或 BEFORE 参数，也可以控制是追加还是置前


### LINK\_DIRECTORIES

* `LINK_DIRECTORIES(dir1 dir2 ...)`
* 添加非标准的共享库搜索路径


### TARGET\_LINK\_LIBRARIES

* `TARGET_LINK_LIBRARIES(target lib1 lib2 ...)`
* 为 target 添加需要链接的共享库


### ADD\_DEFINITIONS

* 为 C/C++ 编译器添加 -D 定义
* ADD\_DEFINITIONS(-DENABLE\_DEBUG -DABC)，参数之间用空格分隔


### ADD\_DEPENDENCIES

* `ADD_DEPENDENCIES(target-name depend-target1 depend-target2 ...)`
* 定义 target 依赖的其他 target，确保 target 在构建之前，其依赖的 target 已经构建完毕


### AUX\_SOURCE\_DIRECTORY

* `AUX_SOURCE_DIRECTORY(dir VAR)`
* 发现一个目录下所有的源代码文件并将列表存储在一个变量中
* 把当前目录下的所有源码文件名赋给变量 DIR\_HELLO\_SRCS


### EXEC\_PROGRAM

* `EXEC_PROGRAM(Executable [dir where to run] [ARGS <args>][OUTPUT_VARIABLE <var>] [RETURN_VALUE <value>])`
* 用于在指定目录运行某个程序（默认为当前 CMakeLists.txt 所在目录），通过 ARGS 添加参数，通过 OUTPUT\_VARIABLE 和 RETURN\_VALUE 获取输出和返回值，如下示例

  ```cmake
  # 在 src 中运行 ls 命令，在 src/CMakeLists.txt 添加
  EXEC_PROGRAM(ls ARGS "*.c" OUTPUT_VARIABLE LS_OUTPUT RETURN_VALUE LS_RVALUE)
  IF (not LS_RVALUE)
      MESSAGE(STATUS "ls result: " ${LS_OUTPUT}) # 缩进仅为美观，语法无要求
  ENDIF(not LS_RVALUE)
  ```


### INCLUDE

* INCLUDE(file [OPTIONAL]) 用来载入 CMakeLists.txt 文件
* INCLUDE(module [OPTIONAL]) 用来载入预定义的 cmake 模块
* OPTIONAL 参数的左右是文件不存在也不会产生错误
* 可以载入一个文件，也可以载入预定义模块（模块会在 CMAKE\_MODULE\_PATH 指定的路径进行搜索）
* 载入的内容将在处理到 INCLUDE 语句时直接执行


### FIND\_

* FIND\_FILE(&lt;VAR> name path1 path2 ...)
    * VAR 变量代表找到的文件全路径，包含文件名
* FIND\_LIBRARY(&lt;VAR> name path1 path2 ...)
    * VAR 变量代表找到的库全路径，包含库文件名

  ```cmake
  FIND_LIBRARY(libX X11 /usr/lib)
  IF (NOT libx)
      MESSAGE(FATAL_ERROR "libX not found")
  ENDIF(NOT libX)
  ```

* FIND\_PATH(&lt;VAR> name path1 path2 ...)
    * VAR 变量代表包含这个文件的路径
* FIND\_PROGRAM(&lt;VAR> name path1 path2 ...)
    * VAR 变量代表包含这个程序的全路径
* FIND\_PACKAGE(&lt;name> [major.minor] [QUIET] [NO\_MODULE] [[REQUIRED \| COMPONENTS] [componets ...]])
    * 用来调用预定义在 CMAKE\_MODULE\_PATH 下的 Find&lt;name>.cmake 模块，你也可以自己定义 Find&lt;name>
        模块，通过 SET(CMAKE\_MODULE\_PATH dir) 将其放入工程的某个目录供工程使用


### IF

语法：

```cmake
IF (expression)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
ELSE (expression)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
ENDIF (expression) # 一定要有 ENDIF 与 IF 对应
```

* **IF (expression)**，expression 不为：空, 0, N, NO, OFF, FALSE, NOTFOUND 或 &lt;var>\_NOTFOUND，为真
* **IF (not exp)**，与上面相反
* **IF (var1 AND var2)**
* **IF (var1 OR var2)**
* **IF (COMMAND cmd)** 如果 cmd 确实是命令并可调用，为真
* **IF (EXISTS dir) IF (EXISTS file)** 如果目录或文件存在，为真
* **IF (file1 IS\_NEWER\_THAN file2)**，当 file1 比 file2 新，或 file1/file2 中有一个不存在时为真，文件名需使用全路径
* **IF (IS\_DIRECTORY dir)** 当 dir 是目录时，为真
* **IF (DEFINED var)** 如果变量被定义，为真
* **IF (var MATCHES regex)** 此处 var 可以用 var 名，也可以用 ${var}
* **IF (string MATCHES regex)**

```cmake
# 当给定的变量或者字符串能够匹配正则表达式 regex 时为真。比如：
IF ("hello" MATCHES "ell")
    MESSAGE("true")
ENDIF ("hello" MATCHES "ell")
```

**数字比较表达式**
* **IF (variable LESS number)**
* **IF (string LESS number)**
* **IF (variable GREATER number)**
* **IF (string GREATER number)**
* **IF (variable EQUAL number)**
* **IF (string EQUAL number)**

**按照字母表顺序进行比较**
* **IF (variable STRLESS string)**
* **IF (string STRLESS string)**
* **IF (variable STRGREATER string)**
* **IF (string STRGREATER string)**
* **IF (variable STREQUAL string)**
* **IF (string STREQUAL string)**

```cmake
一个小例子，用来判断平台差异：
IF (WIN32)
    MESSAGE(STATUS “This is windows.”)
ELSE (WIN32)
    MESSAGE(STATUS “This is not windows”)
ENDIF (WIN32)
上述代码用来控制在不同的平台进行不同的控制，但是，阅读起来却并不是那么舒服，
ELSE(WIN32) 之类的语句很容易引起歧义。

可以 SET(CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS ON)
这时候就可以写成:
IF (WIN32)
ELSE ()
ENDIF ()

配合 ELSEIF 使用，可能的写法是这样:
IF (WIN32)
    # do something related to WIN32
ELSEIF (UNIX)
    # do something related to UNIX
ELSEIF (APPLE)
    # do something related to APPLE
ENDIF (WIN32)
```


### WHILE

语法：

```cmake
WHILE(condition)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
ENDWHILE(condition)
```

其真假判断条件可以参考 IF 指令


### FOREACH

FOREACH 指令的使用方法有三种形式：

#### 列表

语法：

```cmake
FOREACH(loop_var arg1 arg2 ...)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
ENDFOREACH(loop_var)
```

示例：

```cmake
AUX_SOURCE_DIRECTORY(. SRC_LIST)
FOREACH(F ${SRC_LIST})
    MESSAGE(${F})
ENDFOREACH(F)
```

#### 范围

```cmake
FOREACH(loop_var RANGE total)
    COMMAND1(ARGS ...)
    COMMAND2(ARGS ...)
    ...
ENDFOREACH(loop_var)
```

```cmake
从 0 到 total 以 １ 为步进
FOREACH(VAR RANGE 10)
    MESSAGE(${VAR})
ENDFOREACH(VAR)
输出：
0
1
2
3
4
5
6
7
8
9
10
```

#### 范围和步进

语法：

```cmake
FOREACH(loop_var RANGE start stop [step])
     COMMAND1(ARGS ...)
     COMMAND2(ARGS ...)
     ...
ENDFOREACH(loop_var)
```

从 start 开始到 stop 结束，以 step 为步进，
**注意：**直到遇到 ENDFOREACH 指令，整个语句块才会得到真正的执行。

```cmake
FOREACH(A RANGE 5 15 3)
     MESSAGE(${A})
ENDFOREACH(A)
输出：
5
8
11
14
```


## cmake 中如何生成动态库和静态库

参考 ADD\_LIBRARY 和 SET\_TARGET\_PROPERTIES 用法
* t3 示例


## cmake 中如何使用动态库和静态库（查找库的路径）

```cmake
# 指定生成目标
add_executable(Demo main.cc)
# 添加链接库
target_link_libraries(Demo MathFunctions)

# 生成链接库
add_library (MathFunctions ${DIR_LIB_SRCS})
```

参考 INCLUDE\_DIRECTORIES, LINK\_DIRECTORIES, TARGET\_LINK\_LIBRARIES 用法
* t4 示例使用动态库或静态库

  ```cmake
  AUX_SOURCE_DIRECTORY(. SRC_LIST)
  LINK_DIRECTORIES(/home/carl/cmake/t3/build/lib) # 这行一定要在 ADD_EXECUTABLE 前面
  ADD_EXECUTABLE(t4 ${SRC_LIST})
  SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

  SET(CMAKE_PROJECT_DIR /home/carl/cmake) # cmake 文件夹的位置
  INCLUDE_DIRECTORIES(${CMAKE_PROJECT_DIR}/t3/lib_hello)
  TARGET_LINK_LIBRARIES(t4 hello) # 链接动态库
  #TARGET_LINK_LIBRARIES(t4 libhello.a) # 链接静态库
  ```

* t5 示例如何使用 cmake 预定义的 cmake 模块（以 FindCURL.cmake 为例演示）

  ```cmake
  AUX_SOURCE_DIRECTORY(. SRC_LIST)
  ADD_EXECUTABLE(curltest ${SRC_LIST})
  SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
  #INCLUDE_DIRECTORIES(/usr/include)
  #TARGET_LINK_LIBRARIES(curltest curl)
  FIND_PACKAGE(CURL)
  IF (CURL_FOUND)
      MESSAGE(STATUS "CURL_INCLUDE_DIR: " ${CURL_INCLUDE_DIR} " CURL_LIBRARY: " ${CURL_LIBRARY})
      INCLUDE_DIRECTORIES(${CURL_INCLUDE_DIR})
      TARGET_LINK_LIBRARIES(curltest ${CURL_LIBRARY})
  ELSE(CURL_FOUND)
      MESSAGE(FATAL_ERROR "CURL library not found")
  ENDIF(CURL_FOUND)

  # 对于系统预定义的 Find<name>.cmake 模块，使用方法一般如上所示：
  # 每一个模块都会定义以下几个变量
  # • <name>_FOUND 通过此变量判断模块是否被找到
  # • <name>_INCLUDE_DIR or <name>_INCLUDES
  # • <name>_LIBRARY or <name>_LIBRARIES
  ```

* t6 示例如何使用自定义的 cmake 模块（编写了自定义的 FindHELLO.cmake）

  ```cmake
  CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
  PROJECT(HELLO)
  MESSAGE(STATUS "此 Project 演示了如何使用自定义的 cmake 模块 (FindHELLO.cmake)")

  SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
  ADD_SUBDIRECTORY(src)
  ```

  ```cmake
  # FindHELLO.cmake
  # 注意此 cmake 文件中的 3 个变量名
  # HELLO_INCLUDE_DIR -- <name>_INCLUDE_DIR
  # HELLO_LIBRARY     -- <name>_LIBRARY
  # HELLO_FOUND       -- <name>_FOUND
  # 惯例需要定义这 3 个变量，命名规则如上，以便与 cmake 预定义的 cmake 模块中的变量名统一

  # FIND_PATH 和 FIND_LIBARY 的 path 部分，一定要是 .h 文件和 lib 文件所在的当前目录，否则找不到
  FIND_PATH(HELLO_INCLUDE_DIR hello.h /home/carl/cmake/t3/lib_hello)
  MESSAGE(STATUS "HELLO_INCLUDE_DIR: " ${HELLO_INCLUDE_DIR})

  FIND_LIBRARY(HELLO_LIBRARY hello /home/carl/cmake/t3/build/lib)
  MESSAGE(STATUS "HELLO_LIBRARY: " ${HELLO_LIBRARY})

  IF (HELLO_INCLUDE_DIR AND HELLO_LIBRARY)
      SET(HELLO_FOUND TRUE)
  ENDIF(HELLO_INCLUDE_DIR AND HELLO_LIBRARY)

  IF (HELLO_FOUND)
      # 若 FIND_PACKAGE 命令没有指定 QUIET 参数，那下面的 IF 语句就为真
      IF (NOT HELLO_FIND_QUIETLY)
          MESSAGE(STATUS "Found Hello: ${HELLO_LIBRARY}")
      ENDIF (NOT HELLO_FIND_QUIETLY)
  ELSE (HELLO FOUND)
      # 如果 FIND_PACKAGE 命令指定了 REQUIRED 参数，说明这个库是此 Project 必须的
      # 对应下面的 HELLO_FIND_REQUIRED 变量
      IF (HELLO_FIND_REQUIRED)
          MESSAGE(FATAL_ERROR "Could not find hello library")
      ENDIF (HELLO_FIND_REQUIRED)
  ENDIF (HELLO_FOUND)
  ```

  ```cmake
  AUX_SOURCE_DIRECTORY(. SRC_LIST)
  ADD_EXECUTABLE(t6 ${SRC_LIST})
  SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

  # 没有指定 QUIET 参数，HELLO_FIND_QUIETLY 为假
  # 指定 REQUIRED 参数，HELLO_FIND_REQUIRED 为真，意味着此 lib 为该 Project 必须
  FIND_PACKAGE(HELLO REQUIRED)
  # 下面的 HELLO_FOUND HELLO_INCLUDE_DIR HELLO_LIBRARY
  # 3 个变量在 FindHELLO.cmake 中定义
  IF (HELLO_FOUND)
      INCLUDE_DIRECTORIES(${HELLO_INCLUDE_DIR})
      TARGET_LINK_LIBRARIES(t6 ${HELLO_LIBRARY})
  ENDIF (HELLO_FOUND)
  ```

**注意** 读 t5 和 t6 的 CMakeLists.txt 和 FindHELLO.cmake 中的注释部分。


## cmake 中如何指定生成文件的输出路径

* 如上 ADD\_SUBDIRECTORY 的时候指定目标二进制文件输出路径（推荐使用下面这种）
* 使用 SET 命令重新定义 EXECUTABLE\_OUTPUT\_PATH 和 LIBRARY\_OUTPUT\_PATH 变量来指定最终的二进制文件的位置

```cmake
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
```

上面的两条命令通常紧跟 ADD\_EXECUTABLE 和 ADD\_LIBRARY，与其写在同一个 CMakeLists.txt 即可

```cmake
AUX_SOURCE_DIRECTORY(. SRC_LIST)
ADD_EXECUTABLE(t2 ${SRC_LIST})
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
```


## cmake 中如何增加编译选项

* 使用变量 CMAKE\_C\_FLAGS 添加 C 编译选项
* 使用变量 CMAKE\_CXX\_FLAGS 添加 C++ 编译选项
* 使用 ADD\_DEFINITION 添加


## cmake 中如何增加头文件路径

* 参考 INCLUDE\_DIRECTORIES 命令用法


## cmake 中如何在屏幕上打印信息

* 参考 MESSAGE 用法


## cmake 中如何给变量赋值

* 参考 SET 和 AUX\_SOURCE\_DIRECTORY 用法

**建议**：*在 Project 根目录先建立 build，然后在 build 文件夹内运行
cmake..，这样就不会污染源代码，如果不想要这些自动生成的文件了，只要简单的删除 build 文件夹就可以。*


## 基本语法

```cmake
cmake_minimum_required(VERSION 3.4.1)
# 等价的变量 PROJECT_BINARY_DIR 和 PROJECT_SOURCE_DIR。
# 它会引入两个变量 demo_BINARY_DIR 和 demo_SOURCE_DIR。
project(demo)

# 设置编译类型
add_executable(demo demo.cpp) # 生成可执行文件
add_library(common STATIC util.cpp) # 生成静态库
add_library(common SHARED util.cpp) # 生成动态库或共享库
# add_library 默认生成是静态库，通过以上命令生成文件名字，
# 在 Linux 下是：demo libcommon.a libcommon.so
# 在 Windows 下是：demo.exe common.lib common.dll

# 指定编译包含的源文件
# 1. 明确指出包含哪些源文件
add_library(demo demo.cpp test.cpp util.cpp)
# 2. 搜索所有的 cpp 文件
aux_source_directory(dir VAR) # 发现一个目录 (dir) 下所有的源代码文件并将列表存储在一个变量 (VAR) 中。
aux_source_directory(. SRC_LIST) # 搜索当前目录下的所有 .cpp 文件
add_library(demo ${SRC_LIST})
# 3. 自定义搜索规则
file(GLOB SRC_LIST "*.cpp" "protocol/*.cpp")
add_library(demo ${SRC_LIST})
# 或者
file(GLOB SRC_LIST "*.cpp")
file(GLOB SRC_PROTOCOL_LIST "protocol/*.cpp")
add_library(demo ${SRC_LIST} ${SRC_PROTOCOL_LIST})
# 或者
aux_source_directory(. SRC_LIST)
aux_source_directory(protocol SRC_PROTOCOL_LIST)
add_library(demo ${SRC_LIST} ${SRC_PROTOCOL_LIST})

# 设置包含的目录
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_BINARY_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
```


### 配置编译参数

```cmake
# 加入一个配置头文件，用于处理 CMake 对源码的设置
configure_file (
    "${PROJECT_SOURCE_DIR}/config.h.in"
    "${PROJECT_BINARY_DIR}/config.h"
)

# 是否使用自己的 MathFunctions 库
option (USE_MYMATH
       "Use provided math implementation" ON) # 设置为 ON，或 OFF

# 是否加入 MathFunctions 库
if (USE_MYMATH)
    include_directories ("${PROJECT_SOURCE_DIR}/math")
    add_subdirectory (math)
    set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 指定生成目标
add_executable(Demo ${DIR_SRCS})
target_link_libraries (Demo ${EXTRA_LIBS})
```

config.h.in：

```cpp
// 这样 CMake 会自动根据 CMakeLists 配置文件中的设置自动生成 config.h 文件。
#cmakedefine USE_MYMATH

// the configured options and settings for Tutorial
#define Demo_VERSION_MAJOR @Demo_VERSION_MAJOR@
#define Demo_VERSION_MINOR @Demo_VERSION_MINOR@
```


### 安装与测试

```cmake
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")

# 指定 MathFunctions 库的安装路径
install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.h DESTINATION include)

# 指定安装路径
install (TARGETS Demo DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/config.h" DESTINATION include)
```


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


## 如何在 gradle 中使用 cmake 的变量

```gradle
android {
    ...
    defaultConfig {
        ...
        externalNativeBuild {
            cmake {
                // 指定一些编译选项
                cppFlags "-std=c++11 -frtti -fexceptions"
                ...

                // 也可以使用下面这种语法向变量传递参数：
                // arguments "-DVARNAME=ARGV".
                arguments "-DANDROID_ARM_NEON=TRUE",
                // 使用下面这种语法向变量传递多个参数（参数之间使用空格隔开）：
                // arguments "-DVARNAME=arg1 arg2"
                    "-DANDROID_CPP_FEATURES=rtti exceptions"

                // 指定 ABI
                abiFilters "armeabi-v7a", "arm64-v8a"
            }
        }
    }
    buildTypes {...}

    externalNativeBuild {
        cmake {
            path "CMakeLists.txt"
        }
    }
}
```


## CMake CMAKE_CXX_FLAGS_DEBUG

[from {% include relref_csdn.html %}](https://blog.csdn.net/Huoon/article/details/108520571)
[stackoverflow](https://stackoverflow.com/questions/8591762/ifdef-debug-with-cmake-independent-from-platform)

* CMAKE_CXX_FLAGS 是 CMake 传给 C++ 编译器的编译选项，通过设置这个值就好比 g++ -std=c++11 -g -Wall
* CMAKE_CXX_FLAGS_DEBUG 是除了 CMAKE_CXX_FLAGS 外，在 Debug 配置下，额外的参数
* CMAKE_CXX_FLAGS_RELEASE 同理，是除了 CMAKE_CXX_FLAGS 外，在 Release 配置下，额外的参数


### 默认值

```cmake
CMAKE_C_FLAGS =
CMAKE_C_FLAGS_DEBUG = -g
CMAKE_C_FLAGS_MINSIZEREL = -Os -DNDEBUG
CMAKE_C_FLAGS_RELEASE = -O3 -DNDEBUG
CMAKE_C_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG

CMAKE_CXX_FLAGS =
CMAKE_CXX_FLAGS_DEBUG = -g
CMAKE_CXX_FLAGS_MINSIZEREL = -Os -DNDEBUG
CMAKE_CXX_FLAGS_RELEASE = -O3 -DNDEBUG
CMAKE_CXX_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG
```


### 解决方案

```cmake
# https://github.com/juj/MathGeoLib/blob/master/CommonOptions.cmake
# Add the global _DEBUG flag from WIN32 platform to all others, which is universally used in MGL to
# perform debug-mode-specific compilation.
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -D_DEBUG")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -D_DEBUG")

IF (WIN32 AND NOT CYGWIN)
    SET(CMAKE_C_FLAGS_DEBUG "-D_DEBUG")
ENDIF ()
```

可以在代码里面检查：

```cpp
// check that exactly one of NDEBUG and _DEBUG is defined
#if !defined(NDEBUG) ^ defined(_DEBUG)
#error Exactly one of NDEBUG and _DEBUG needs to be defined!
#endif

#ifdef CMAKE_INTDIR
#if defined(_MSC_VER) && !defined(NDEBUG)
#define _DEBUG
#endif // defined(_MSC_VER) && !defined(NDEBUG)
#endif // CMAKE_INTDIR

/*! `NDEBUG` or `_DEBUG` mean not build on `DEBUG` mode. */
#ifndef NDEBUG
#ifndef _DEBUG
#define _DEBUG
#endif /* _DEBUG */
#endif /* NDEBUG */

// https://apache.github.io/xalan-c/api/PlatformDefinitions_8hpp_source.html
#if defined(_DEBUG) && defined(NDEBUG)
#error NDEBUG must not be defined when _DEBUG is defined.
#elif !defined(_DEBUG) && !defined(NDEBUG)
#error NDEBUG must be defined when _DEBUG is not defined.
#endif
```


### [实验 {% include relref_csdn.html %}](https://blog.csdn.net/icbm/article/details/52336497)

```cmake
cmake_minimum_required(VERSION 3.4)

message(STATUS "CMAKE_C_FLAGS = " ${CMAKE_C_FLAGS})
message(STATUS "CMAKE_C_FLAGS_DEBUG = " ${CMAKE_C_FLAGS_DEBUG})
message(STATUS "CMAKE_C_FLAGS_MINSIZEREL = " ${CMAKE_C_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_C_FLAGS_RELEASE = " ${CMAKE_C_FLAGS_RELEASE})
message(STATUS "CMAKE_C_FLAGS_RELWITHDEBINFO = " ${CMAKE_C_FLAGS_RELWITHDEBINFO})

message(STATUS "CMAKE_CXX_FLAGS = " ${CMAKE_CXX_FLAGS})
message(STATUS "CMAKE_CXX_FLAGS_DEBUG = " ${CMAKE_CXX_FLAGS_DEBUG})
message(STATUS "CMAKE_CXX_FLAGS_MINSIZEREL = " ${CMAKE_CXX_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_CXX_FLAGS_RELEASE = " ${CMAKE_CXX_FLAGS_RELEASE})
message(STATUS "CMAKE_CXX_FLAGS_RELWITHDEBINFO = " ${CMAKE_CXX_FLAGS_RELWITHDEBINFO})

message(STATUS "CMAKE_EXE_LINKER_FLAGS = " ${CMAKE_EXE_LINKER_FLAGS})
message(STATUS "CMAKE_EXE_LINKER_FLAGS_DEBUG = " ${CMAKE_EXE_LINKER_FLAGS_DEBUG})
message(STATUS "CMAKE_EXE_LINKER_FLAGS_MINSIZEREL = " ${CMAKE_EXE_LINKER_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_EXE_LINKER_FLAGS_RELEASE = " ${CMAKE_EXE_LINKER_FLAGS_RELEASE})
message(STATUS "CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO = " ${CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO})

message(STATUS "CMAKE_MODULE_LINKER_FLAGS = " ${CMAKE_MODULE_LINKER_FLAGS})
message(STATUS "CMAKE_MODULE_LINKER_FLAGS_DEBUG = " ${CMAKE_MODULE_LINKER_FLAGS_DEBUG})
message(STATUS "CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL = " ${CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_MODULE_LINKER_FLAGS_RELEASE = " ${CMAKE_MODULE_LINKER_FLAGS_RELEASE})
message(STATUS "CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO = " ${CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO})

message(STATUS "CMAKE_SHARED_LINKER_FLAGS = " ${CMAKE_SHARED_LINKER_FLAGS})
message(STATUS "CMAKE_SHARED_LINKER_FLAGS_DEBUG = " ${CMAKE_SHARED_LINKER_FLAGS_DEBUG})
message(STATUS "CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL = " ${CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_SHARED_LINKER_FLAGS_RELEASE = " ${CMAKE_SHARED_LINKER_FLAGS_RELEASE})
message(STATUS "CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO = " ${CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO})

message(STATUS "CMAKE_STATIC_LINKER_FLAGS = " ${CMAKE_STATIC_LINKER_FLAGS})
message(STATUS "CMAKE_STATIC_LINKER_FLAGS_DEBUG = " ${CMAKE_STATIC_LINKER_FLAGS_DEBUG})
message(STATUS "CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL = " ${CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL})
message(STATUS "CMAKE_STATIC_LINKER_FLAGS_RELEASE = " ${CMAKE_STATIC_LINKER_FLAGS_RELEASE})
message(STATUS "CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO = " ${CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO})
```

#### Windows 平台 64 位编译输出

```bat
C:\chenchang\VMs\share\test\bld_win32>cmake -G "Visual Studio 14 2015 Win64" ..
-- CMAKE_C_FLAGS =  /DWIN32 /D_WINDOWS /W3
-- CMAKE_C_FLAGS_DEBUG = /D_DEBUG /MDd /Zi /Ob0 /Od /RTC1
-- CMAKE_C_FLAGS_MINSIZEREL = /MD /O1 /Ob1 /D NDEBUG
-- CMAKE_C_FLAGS_RELEASE = /MD /O2 /Ob2 /D NDEBUG
-- CMAKE_C_FLAGS_RELWITHDEBINFO = /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS =  /DWIN32 /D_WINDOWS /W3 /GR /EHsc
-- CMAKE_CXX_FLAGS_DEBUG = /D_DEBUG /MDd /Zi /Ob0 /Od /RTC1
-- CMAKE_CXX_FLAGS_MINSIZEREL = /MD /O1 /Ob1 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELEASE = /MD /O2 /Ob2 /D NDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO = /MD /Zi /O2 /Ob1 /D NDEBUG
-- CMAKE_EXE_LINKER_FLAGS =  /machine:x64
-- CMAKE_EXE_LINKER_FLAGS_DEBUG = /debug /INCREMENTAL
-- CMAKE_EXE_LINKER_FLAGS_MINSIZEREL = /INCREMENTAL:NO
-- CMAKE_EXE_LINKER_FLAGS_RELEASE = /INCREMENTAL:NO
-- CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO = /debug /INCREMENTAL
-- CMAKE_MODULE_LINKER_FLAGS =  /machine:x64
-- CMAKE_MODULE_LINKER_FLAGS_DEBUG = /debug /INCREMENTAL
-- CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL = /INCREMENTAL:NO
-- CMAKE_MODULE_LINKER_FLAGS_RELEASE = /INCREMENTAL:NO
-- CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO = /debug /INCREMENTAL
-- CMAKE_SHARED_LINKER_FLAGS =  /machine:x64
-- CMAKE_SHARED_LINKER_FLAGS_DEBUG = /debug /INCREMENTAL
-- CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL = /INCREMENTAL:NO
-- CMAKE_SHARED_LINKER_FLAGS_RELEASE = /INCREMENTAL:NO
-- CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO = /debug /INCREMENTAL
-- CMAKE_STATIC_LINKER_FLAGS =  /machine:x64
-- CMAKE_STATIC_LINKER_FLAGS_DEBUG =
-- CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL =
-- CMAKE_STATIC_LINKER_FLAGS_RELEASE =
-- CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO =
-- Configuring done
-- Generating done
-- Build files have been written to: C:/chenchang/VMs/share/test/bld_win32
```

#### Ubuntu Linux 16.04 64 位编译输出

```shell
root@chanchen-VirtualBox:/mnt/share/test/bld_lnx# cmake ..
-- CMAKE_C_FLAGS =
-- CMAKE_C_FLAGS_DEBUG = -g
-- CMAKE_C_FLAGS_MINSIZEREL = -Os -DNDEBUG
-- CMAKE_C_FLAGS_RELEASE = -O3 -DNDEBUG
-- CMAKE_C_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG
-- CMAKE_CXX_FLAGS =
-- CMAKE_CXX_FLAGS_DEBUG = -g
-- CMAKE_CXX_FLAGS_MINSIZEREL = -Os -DNDEBUG
-- CMAKE_CXX_FLAGS_RELEASE = -O3 -DNDEBUG
-- CMAKE_CXX_FLAGS_RELWITHDEBINFO = -O2 -g -DNDEBUG
-- CMAKE_EXE_LINKER_FLAGS =
-- CMAKE_EXE_LINKER_FLAGS_DEBUG =
-- CMAKE_EXE_LINKER_FLAGS_MINSIZEREL =
-- CMAKE_EXE_LINKER_FLAGS_RELEASE =
-- CMAKE_EXE_LINKER_FLAGS_RELWITHDEBINFO =
-- CMAKE_MODULE_LINKER_FLAGS =
-- CMAKE_MODULE_LINKER_FLAGS_DEBUG =
-- CMAKE_MODULE_LINKER_FLAGS_MINSIZEREL =
-- CMAKE_MODULE_LINKER_FLAGS_RELEASE =
-- CMAKE_MODULE_LINKER_FLAGS_RELWITHDEBINFO =
-- CMAKE_SHARED_LINKER_FLAGS =
-- CMAKE_SHARED_LINKER_FLAGS_DEBUG =
-- CMAKE_SHARED_LINKER_FLAGS_MINSIZEREL =
-- CMAKE_SHARED_LINKER_FLAGS_RELEASE =
-- CMAKE_SHARED_LINKER_FLAGS_RELWITHDEBINFO =
-- CMAKE_STATIC_LINKER_FLAGS =
-- CMAKE_STATIC_LINKER_FLAGS_DEBUG =
-- CMAKE_STATIC_LINKER_FLAGS_MINSIZEREL =
-- CMAKE_STATIC_LINKER_FLAGS_RELEASE =
-- CMAKE_STATIC_LINKER_FLAGS_RELWITHDEBINFO =
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/share/test/bld_lnx
```


## Refs

- [1] [Cmake 语法与实战入门 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/267803605)
- [2] [cmake demo {% include relref_github.html %}](https://github.com/carl-wang-cn/demo/tree/master/cmake)
- [3] [CMake 入门 / 基本语法](https://zh.m.wikibooks.org/zh-hans/CMake_%E5%85%A5%E9%96%80/%E5%9F%BA%E6%9C%AC%E8%AA%9E%E6%B3%95)
- [4] [CMake 语法 - 详解 CMakeLists.txt（最后包含了 OGRE 的例子） {% include relref_jianshu.html %}](https://www.jianshu.com/p/528eeb266f83)
- [5] [CMakeLists.txt 语法介绍与实例演练（这个颜色好） {% include relref_csdn.html %}](https://blog.csdn.net/afei__/article/details/81201039)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-02-01-cmakelists.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://developer.android.com/studio/projects/configure-cmake]({% include relref.html url="/backup/2021-02-01-cmakelists.md/developer.android.com/e400582b.html" %})
- [https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html]({% include relref.html url="/backup/2021-02-01-cmakelists.md/cmake.org/dae0cbfc.html" %})
- [https://blog.csdn.net/Huoon/article/details/108520571]({% include relref.html url="/backup/2021-02-01-cmakelists.md/blog.csdn.net/43695850.html" %})
- [https://stackoverflow.com/questions/8591762/ifdef-debug-with-cmake-independent-from-platform]({% include relref.html url="/backup/2021-02-01-cmakelists.md/stackoverflow.com/0392352f.html" %})
- [https://github.com/juj/MathGeoLib/blob/master/CommonOptions.cmake]({% include relref.html url="/backup/2021-02-01-cmakelists.md/github.com/24e305e7.html" %})
- [https://apache.github.io/xalan-c/api/PlatformDefinitions_8hpp_source.html]({% include relref.html url="/backup/2021-02-01-cmakelists.md/apache.github.io/eeffe529.html" %})
- [https://blog.csdn.net/icbm/article/details/52336497]({% include relref.html url="/backup/2021-02-01-cmakelists.md/blog.csdn.net/5403caaa.html" %})
- [https://zhuanlan.zhihu.com/p/267803605]({% include relref.html url="/backup/2021-02-01-cmakelists.md/zhuanlan.zhihu.com/d33bbe25.html" %})
- [https://github.com/carl-wang-cn/demo/tree/master/cmake]({% include relref.html url="/backup/2021-02-01-cmakelists.md/github.com/bd0e5b28.html" %})
- [https://zh.m.wikibooks.org/zh-hans/CMake_%E5%85%A5%E9%96%80/%E5%9F%BA%E6%9C%AC%E8%AA%9E%E6%B3%95]({% include relref.html url="/backup/2021-02-01-cmakelists.md/zh.m.wikibooks.org/c46fcb62.html" %})
- [https://www.jianshu.com/p/528eeb266f83]({% include relref.html url="/backup/2021-02-01-cmakelists.md/www.jianshu.com/7e0846cb.html" %})
- [https://blog.csdn.net/afei__/article/details/81201039]({% include relref.html url="/backup/2021-02-01-cmakelists.md/blog.csdn.net/e4e068fd.html" %})
