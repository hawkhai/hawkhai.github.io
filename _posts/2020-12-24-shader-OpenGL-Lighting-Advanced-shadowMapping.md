---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 高级光照 阴影 shadowMapping"
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
cluster: "LearnOpenGL"
---


## shadowMapping

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_theory_spaces.png" %}

通过移动视口到光源位置，可以观察到这个位置每个东西都是明亮的，因为从光的角度来看是没有阴影的。
从光源的角度将场景的深度渲染到一张深度缓冲区中，我们可以在场景中获得一张阴影或者无阴影的贴图，一张阴影贴图。

高级光照阴影 ShadowMapping，实在没看透彻，源码抄了一遍，才透彻了。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_theory.gif" %}


## 详解

从光源处得到的深度图片，越近越黑，越远越白。最下面纯白，是没有任何绘制的边界了。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/20201224121704.png" %}


## Refs

- [1] [Shadow Mapping](https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping)
- [2] [阴影映射 {% include relref_github.html %}](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping]({% include relref.html url="/backup/2020-12-24-shader-OpenGL-Lighting-Advanced-shadowMapping.md/learnopengl.com/296bb720.html" %})
- [2] [https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/]({% include relref.html url="/backup/2020-12-24-shader-OpenGL-Lighting-Advanced-shadowMapping.md/learnopengl-cn.github.io/43cc6489.html" %})
