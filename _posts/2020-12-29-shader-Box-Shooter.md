---
layout: post
title: "特效编程笔记 -- A simple box shooter using Bullet Physics and OpenGL"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

A simple box shooter using Bullet Physics and OpenGL.


## Box Shooter

A simple game that one can throw box to a pile of boxes to drop some of them. The implementation is using using *OpenGL* and *Bullet Physics*.

{% include image.html url="/assets/images/201229-shader-box-shooter/boxshooter.webp" %}


## Installing Box Shooter

To install Box Shooter, follow these steps:

```shell
mkdir build && cd build
cmake .. # Using CMake
make # make all
```
