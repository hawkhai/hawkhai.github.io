---
layout: post
title: "编程与调试 C++ -- interview"
author: 杨全海
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 成员初始化列表

* 更高效：少了一次调用默认构造函数的过程。
* 有些场合必须要用初始化列表：
    * 常量成员，因为常量只能初始化不能赋值，所以必须放在初始化列表里面
    * 引用类型，引用必须在定义的时候初始化，并且不能重新赋值，所以也要写在初始化列表里面
    * 没有默认构造函数的类类型，因为使用初始化列表可以不必调用默认构造函数来初始化

[from](https://interview.huihut.com/)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-03-30-interview.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://interview.huihut.com/]({% include relrefx.html url="/backup/2022-03-30-interview.md/interview.huihut.com/40dfb5bd.html" %})
