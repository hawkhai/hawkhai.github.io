---
layout: post
title: "图形学笔记 -- OpenGL 毕业报告 / 3D 水母程序 jellyfish"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

不依赖任何 3D 引擎，全部采用原生 OpenGL API 实现。


## 先上效果

{% include image.html url="/assets/images/210502-shader-opengl-jellyfish/jellyfish_3.webp" %}


## 数学基础函数

M4x4 采用行优先的内存结构，glm::mat4 是 列优先记法。
```cpp
// 计算投影视锥体
GLfloat* M4x4_makeFrustum(GLfloat left, GLfloat right,
    GLfloat bottom, GLfloat top,
    GLfloat znear, GLfloat zfar, GLfloat* r);
// 转置矩阵
GLfloat* M4x4_transpose(GLfloat* m, GLfloat* r);
// 计算标准正交矩阵的逆矩阵 4x4
GLfloat* M4x4_inverseOrthonormal(GLfloat* m, GLfloat* r);
// 矩阵相乘
GLfloat* M4x4_mul(GLfloat* a, GLfloat* b, GLfloat* r);
// 计算 透视投影
GLfloat* M4x4_makePerspective(GLfloat fovy, GLfloat aspect, GLfloat znear, GLfloat zfar, GLfloat* r);
// 平移矩阵
GLfloat* M4x4_makeTranslate3(GLfloat x, GLfloat y, GLfloat z, GLfloat* r);
// 矩阵平移
GLfloat* M4x4_translate3(GLfloat x, GLfloat y, GLfloat z, GLfloat* m, GLfloat* r);
// 矩阵旋转
GLfloat* M4x4_rotate(GLfloat angle, glm::vec3 axis, GLfloat* m, GLfloat* r);
// 定义一个视图矩阵
GLfloat* M4x4_makeLookAt(glm::vec3 eye, glm::vec3 center, glm::vec3 up, GLfloat* r);
// 平移矩阵
GLfloat* M4x4_makeTranslate(glm::vec3 v, GLfloat* r);
// 矩阵缩放
GLfloat* M4x4_scale1(GLfloat k, GLfloat* m, GLfloat* r);

// 向量点乘
GLfloat V3_dot(glm::vec3 a, glm::vec3 b);
// 向量叉乘
glm::vec3 V3_cross(glm::vec3 a, glm::vec3 b);
// 向量加法
glm::vec3 V3_add(glm::vec3 a, glm::vec3 b, glm::vec3& r);
// 向量缩放
glm::vec3 V3_scale(glm::vec3 a, GLfloat k);
// 向量方向：向量 A 到向量 B 的方向（标准化）
glm::vec3 V3_direction(glm::vec3 a, glm::vec3 b);
// 向量减法
glm::vec3 V3_sub(glm::vec3 a, glm::vec3 b);
// 向量长度
GLfloat V3_length(glm::vec3 a);
// 向量标准化
glm::vec3 V3_normalize(glm::vec3 a);
// 向量取反
glm::vec3 V3_neg(glm::vec3 a);
```

[arodic / WebGL-Fluid-Simulation {% include relref_github.html %}](https://github.com/arodic/WebGL-Fluid-Simulation)
[WebGL Jellyfish Simulation {% include relref_github.html %}](https://github.com/arodic/Chrysaora)
[WebGL jellyfish demo {% include relref_github.html %}](https://github.com/arodic/jellyfish)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-02-shader-OpenGL-jellyfish.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/arodic/WebGL-Fluid-Simulation]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/c78cb661.html" %})
- [https://github.com/arodic/Chrysaora]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/9c577022.html" %})
- [https://github.com/arodic/jellyfish]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/dbca1ee4.html" %})
