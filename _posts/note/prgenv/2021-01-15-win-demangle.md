---
layout: post
title: "编程笔记 -- 调用约定 (Calling Conventions) C++ 函数名修饰 (Name Mangling)"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

调用约定 (Calling Conventions) (__cdecl、__stdcall、__fastcall) C++ 函数名修饰 (Name Mangling)。


## 调用约定


### __cdecl

格式为 function。


### __stdcall

格式为 _function@number。


### __fastcall

格式为 @function@number。


## C++ 函数名修饰（Decorated Names，Name Mangling）

* \_\_cdecl，@@YA
* \_\_stdcall，@@YG
* \_\_fastcall，@@YI


## dll 导出函数方式比较


### C++ 编译

对于 C++ 编译器的函数名修饰规则：不管 _\_cdecl, _\_fastcall 还是 _\_stdcall 调用方式，函数修饰名都是以 "?" 开始，后面是函数在名字，再后面是函数返回类型和参数类型按照代号拼出的参数表。
对于 _\_stdcall 方式，参数表的开始标示是 "@@YG”, 对于 _\_cdecl 方式则是 "@@YA”, 对于 _\_fastcall 方式则是 "@@YI”。
参数表后以 "@Z” 标示整个名字的结束，如果该函数无参数，则以 "Z” 标识结束。

* `__declspec(dllexport) int add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904162755028-1519997000.png" %}

* `__declspec(dllexport) int __cdecl add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904162812590-44820080.png" %}

* `__declspec(dllexport) int __stdcall add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904162822390-722876879.png" %}

* `__declspec(dllexport) int __fastcall add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904162845970-1658299139.png" %}


### C 编译

_\_stdcall 和 _\_fastcall 编译出来的函数名还是和原始的函数名不同。
就拿 _\_stdcall 来说，它以 C 编译导出的时候，会在函数前面加入下划线，并在函数后面加入 @ 和参数总大小的字节数。

* `extern "C" __declspec(dllexport) int add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904162900687-483646682.png" %}

* `extern "C" __declspec(dllexport) int __cdecl add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904164216907-1400578503.png" %}

* `extern "C" __declspec(dllexport) int __stdcall add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904164223433-1206003218.png" %}

* `extern "C" __declspec(dllexport) int __fastcall add(int, int);`

{% include image.html url="/assets/images/210115-win-demangle/632353-20180904164229061-354285467.png" %}


## Source

[Tool to demangle C++ symbols {% include relref_github.html %}](https://github.com/eklitzke/demangle).

```cpp
#include <stdio.h>
#include <getopt.h>
#include <stdlib.h>
#include <cxxabi.h>

static void demangle(const char* mangled_name, bool quiet) {
    int status = 0;
    const char* realname = abi::__cxa_demangle(mangled_name, 0, 0, &status);
    switch (status) {
    case 0:
        if (quiet) {
            puts(realname);
        }
        else {
            printf("%s  %s\n", realname, mangled_name);
        }
        break;
    case -1:
        printf("FAIL: failed to allocate memory while demangling %s\n",
            mangled_name);
        break;
    case -2:
        printf("FAIL: %s is not a valid name under the C++ ABI mangling rules\n",
            mangled_name);
        break;
    default:
        printf("FAIL: some other unexpected error: %d\n", status);
        break;
    }
    free((void*)realname);
}
```

内部源码实现：[Demangler for MSVC symbols {% include relref_github.html %}](https://github.com/rui314/msvc-demangler)


## 附件下载

{% include image.html url="/assets/images/210115-win-demangle/f_53837a9a2b32da06c4da07476dee9613.png" %}

一般本机上都有，用 Everything 检索本地：undname.exe。

* Name Mangling 解析工具，界面如上截图：<a href="{% include relref.html url="/source/demangle/dem.rar" %}" target="_blank">dem.rar</a>
* Name Mangling 解析工具，命令行版本：<a href="{% include relref.html url="/source/demangle/undname.rar" %}" target="_blank">undname.rar</a>
* 可执行文件 (exe、dll、lib) 解析工具：<a href="{% include relref.html url="/source/demangle/dumpbin.rar" %}" target="_blank">dumpbin.rar</a> - dumpbin /EXPORTS /IMPORTS filename
* 在线版本 [GCC and MSVC C++ Demangler](http://demangler.com/)


## Refs

- [1] [调用约定 C++ 函数名修饰](http://www.3scard.com/index.php?m=blog&f=view&id=10)
- [2] [编译器的函数名修饰的机制 extern C 的作用 {% include relref_jianshu.html %}](https://www.jianshu.com/p/c0f3a3ac88b2)
- [3] [dll 导出函数的两种方式的比较 {% include relref_cnblogs.html %}](https://www.cnblogs.com/talenth/p/9585208.html)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-15-win-demangle.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/eklitzke/demangle]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/github.com/ae250947.html" %})
- [https://github.com/rui314/msvc-demangler]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/github.com/f170810d.html" %})
- [http://demangler.com/]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/demangler.com/1d1c5662.html" %})
- [http://www.3scard.com/index.php?m=blog&f=view&id=10]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/www.3scard.com/4598f332.php" %})
- [https://www.jianshu.com/p/c0f3a3ac88b2]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/www.jianshu.com/462a0ca3.html" %})
- [https://www.cnblogs.com/talenth/p/9585208.html]({% include relrefx.html url="/backup/2021-01-15-win-demangle.md/www.cnblogs.com/3aaa0090.html" %})
