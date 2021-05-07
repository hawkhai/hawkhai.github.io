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
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

不依赖任何 3D 引擎，全部采用原生 OpenGL API 实现。程序下载：
<a href="{% include relref.html url="/source/jellyfish.zip" %}" target="_blank">jellyfish.zip</a>


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


## 模型顶点数据

{% include image.html url="/assets/images/210502-shader-opengl-jellyfish/jellyfish1.png" %}

[骨骼动画原理 {% include relref_cnblogs.html %}](https://www.cnblogs.com/tandier/p/10087656.html)
[骨骼动画与蒙皮矩阵](https://www.qiujiawei.com/linear-algebra-19/)
建立 1 个控制点 和 4 个骨骼节点：
{% include image.html url="/assets/images/210502-shader-opengl-jellyfish/jellyfish_skeleton.jpg" %}
[^_^]: https://sunocean.life/jellyfish/Chrysaora/index.html

**aSkinWeight** 可以根据 y 坐标简单算出来：

```cpp
int weightSize = 0;
for (int i = 0; i < vertexPositions.size(); i = i + 3) {
    GLfloat value = vertexPositions[i + 1]; // y
    GLfloat ypos = -value / 3;
    GLfloat w0 = max(min(-ypos + 1, 1), 0);
    GLfloat w1 = max(min(ypos, -ypos + 2), 0);
    GLfloat w2 = max(min(ypos - 1, -ypos + 3), 0);
    GLfloat w3 = max(min(ypos - 2, 1), 0);
    weightData[weightSize++] = w0;
    weightData[weightSize++] = w1;
    weightData[weightSize++] = w2;
    weightData[weightSize++] = w3;
}
```

对应的权重图，权重分布：
{% include image.html url="/assets/images/210502-shader-opengl-jellyfish/weightdata.png" %}

[^_^]: [arodic / WebGL-Fluid-Simulation {% include relref_github.html %}](https://github.com/arodic/WebGL-Fluid-Simulation)
[^_^]: [WebGL Jellyfish Simulation {% include relref_github.html %}](https://github.com/arodic/Chrysaora)
[^_^]: [WebGL jellyfish demo {% include relref_github.html %}](https://github.com/arodic/jellyfish)


## 蒙皮动画

[guillaumeblanc / ozz-animation {% include relref_github.html %}](https://github.com/guillaumeblanc/ozz-animation)

局部姿势是关节相对于父关节来指定的，是一种常见的姿势。局部姿势存储为 $TQS$ 的格式，
表示相对与父关节的位置、朝向、缩放，根关节的父节点可以认为是世界坐标系原点。

关节在三维软件里通常是显示成一个点或者一个球，实际上，每个关节定义了一个坐标空间。
在数学上，关节姿势就是一个仿射变换，用 $P_j$ 表示关节 $j$ 代表的仿射变换，
它是一个 $4\times 4$ 的矩阵，它由平移向量 $T_j$，旋转矩阵 $R_j$ 以及对角缩放矩阵 $S_j$ 组成。

$$
P_j=\left[\begin{matrix}
R_jS_j & T_j \\
0 & 1
\end{matrix}
\right]
$$

局部关节姿势可以表示为：

```cpp
struct JointPose
{
    Quaternion m_rot; // 相对父关节朝向
    Vector3 m_trans;  // 在父关节中的坐标
    Vector3 m_scale;  // 相对父关节的缩放
};
```

局部关节姿势矩阵 $P_j$ 作用到以关节 $j$ 坐标系表示的点或者向量时，其结果是将点或者向量变换到父关节坐标空间表示的点。

这样关节 8 的 **蒙皮矩阵** 就是
$$
F_8=G_8O_8=P_1'P_7'P_8'(P_1P_7P_8)^{-1}
$$

加权平均的计算时，顶点绑定的所有骨架的权重和为 1。通常设每个顶点最多绑定到 4 个骨架，程序存储如下：
```cpp
struct SkinnedVertex
{
    float m_position[3]; // 顶点位置（x, y, z）
    float m_normal[3];   // 顶点法向量（Nx, Ny, Nz）
    float m_u, m_v;      // 纹理坐标
    U8 m_jointIndex[4];  // 关节的索引
    float m_jointWeight[4]; // 关节权重
};
```

上面提到过 **蒙皮矩阵**，但是还没正式定义，蒙皮矩阵就是把顶点从 **绑定姿势** 变换到骨骼的 **当前姿势** 的矩阵。
蒙皮矩阵和前面的 **基变更** 矩阵不同，它只是把顶点变换到新的位置，顶点变换前后都在世界空间中（或模型空间中）。
和上面一样用 $F_j$ 表示关节 $j$ 的蒙皮矩阵，假设某个顶点 $v$ 受到上面关节 14、18、15、25 的影响，
对应点权重分别为 $w_1,w_2,w_3,w_4$，则顶点 $v$ 的最终变换位置为：
$$v'=w_1F_{14}v+w_2F_{18}v+w_3F_{15}v+w_4F_{25}v$$
上面公式就是顶点的蒙皮计算方法。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-05-02-shader-OpenGL-jellyfish.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/tandier/p/10087656.html]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/www.cnblogs.com/9e44e156.html" %})
- [https://www.qiujiawei.com/linear-algebra-19/]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/www.qiujiawei.com/a0255dd8.html" %})
- [https://github.com/arodic/WebGL-Fluid-Simulation]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/c78cb661.html" %})
- [https://github.com/arodic/Chrysaora]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/9c577022.html" %})
- [https://github.com/arodic/jellyfish]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/dbca1ee4.html" %})
- [https://github.com/guillaumeblanc/ozz-animation]({% include relrefx.html url="/backup/2021-05-02-shader-OpenGL-jellyfish.md/github.com/a7d10ab8.html" %})
