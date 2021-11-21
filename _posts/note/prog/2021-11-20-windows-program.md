---
layout: post
title: "编程与调试 -- Windows 编程知识点（文档整理）"
author: yqh
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---


## Windows C++ 开发基础


### 头文件引用顺序建议

* 预编译头文件
* 本 cpp 对应的头文件
* C 系统头文件
* C++ 系统头文件
* 项目内部头文件


### 类

* 不要在 C++ 中的构造函数与析构函数中调用虚函数
* 只要用到了继承关系，面向接口编程的情况下，都需要虚析构函数。
* `/we4263` 限制 override 必须写上。
  ```cmake
# Enable and treat as errors the following warnings to easily detect virtual function signature failures:
# 'function' : member function does not override any base class virtual member function
# 'virtual_function' : no override available for virtual member function from base 'class'; function is hidden
target_compile_options(trinity-compile-option-interface
  INTERFACE
    /we4263
    /we4264)
```


### 接口定义

* C++ 没有 interface 关键字，所以我们使用定义纯虚函数的 class 作为
* 接口中不能定义成员变量
* **需要定义一个虚析构函数或者用于释放当前实例对象的纯虚函数，二者必选其一**


## 开发环境和调试入门



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-11-20-windows-program.md.js" %}'></script></p>
