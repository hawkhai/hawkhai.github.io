---
layout: post
title: "“特效编程”笔记 -- 计算机图形学 OPENGL / 冯氏光照模型"
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
---

<https://ke.qq.com/course/package/25480?flowToken=1019441>


## OpenGL 光照

冯氏光照模型的主要结构由 3 个分量组成：环境 (Ambient)、漫反射 (Diffuse) 和镜面 (Specular) 光照。

**环境光照 (Ambient Lighting)**：物体几乎永远不会是完全黑暗的。所以环境光照一般是个常量。

**漫反射光照 (Diffuse Lighting)**：模拟光源对物体的方向性影响，物体的某一部分越是正对着光源，它就会越亮。

**镜面光照 (Specular Lighting)**：模拟有光泽物体上面出现的亮点。镜面光照的颜色相比于物体的颜色会更倾向于光的颜色。

{% include image.html url="/images/OpenGL-GLSL/v2-7d9cb4f3c58bce1dd41c43902284f7d4_720w.jpg" %}

{% include image.html url="/images/OpenGL-GLSL/20201209104409.png" %}

- 基础光照原理讲解

- 创建一个光照场景

- 冯氏光照基础效果实现

- 材质 & 光属性

- 光照贴图

- 平行光与点光源

- 聚光手电筒效果

- 多光源 shader 函数封装

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://ke.qq.com/course/package/25480?flowToken=1019441]({% include relref.html url="/backup/2020-12-09-shader-OpenGL-Lighting.md/ke.qq.com/3fd1c97a.html" %})
