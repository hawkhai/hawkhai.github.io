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

- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.4-chinese.md]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/04ed1da9.html" %})
- [https://www.bookstack.cn/read/CMake-Cookbook/content-chapter7-7.5-chinese.md]({% include relref.html url="/backup/2021-02-26-CMakeLists-Advanced.md/www.bookstack.cn/9a399d1f.html" %})
