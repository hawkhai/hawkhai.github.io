---
layout: post
title: "“特效编程”笔记 -- OPENGL 入门（几何着色器）"
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

通过顶点着色器和片段着色器，可以将输入的顶点经过着色器的处理显示到屏幕上。
OpenGL 3.2 及更新的版本支持几何着色器，介于顶点着色器和片段着色器之间，几何着色器接收顶点着色器的输出作为输入，通过高效的几何运算，将数据输出到片段着色器。

{% include image.html url="/images/OpenGL-GLSL/20201112210938.png" %}

本文源码 <a href="{% include relref.html url="/source/shader/geometry.cpp" %}" target="_blank">geometry.cpp</a>


## 几何着色器入门

顶点着色器处理顶点，片段着色器处理每个小的片段，而几何着色器处理整个原语。第一行描述几何着色器处理的原语类型。

```glsl
layout(points) in;
````

支持的原语类型如下，对应绘制命令类型：

* **points** - GL_POINTS (1 vertex)
* **lines** - GL_LINES, GL_LINE_STRIP, GL_LINE_LIST (2 vertices)
* **lines_adjacency** - GL_LINES_ADJACENCY, GL_LINE_STRIP_ADJACENCY (4 vertices)
* **triangles** - GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN (3 vertices)
* **triangles_adjacency** - GL_TRIANGLES_ADJACENCY, GL_TRIANGLE_STRIP_ADJACENCY (6 vertices)

实例中绘制类型为 GL_POINTS，此处使用 points。


### 输出类型

第二行描述着色的输出。通过处理，几何着色器能输出完全不同的几何体类型，生成的原语数也可以变化。

```glsl
layout(line_strip, max_vertices = 2) out;
````

此行定义输出类型和最大输出顶点数。

支持的输出类型如下：

* **points**
* **line_strip**
* **triangle_strip**

类型虽然很少，但可以充分覆盖所有的原语类型。例如，三个顶点的 `triangle_strip` 相当于一个普通的三角形。


### 顶点输入

几何着色器中可通过 gl_in 数组访问顶点着色器中的变量 gl_Position，gl_in 为结构化的数组，具体如下：

```glsl
in gl_PerVertex
{
    vec4 gl_Position;
    float gl_PointSize;
    float gl_ClipDistance[];
} gl_in[];
````


### 顶点输出

几何着色器程序通过两个指定的函数产生原语：EmitVertex、EndPrimitive。每次调用 EmitVertex，顶点加入到当前原语中。
当添加完所有的顶点，几何着色器调用 EndPrimitive 产生原语。

```glsl
void main() {
    gl_Position = gl_in[0].gl_Position + vec4(-0.1, 0.0, 0.0, 0.0);
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(0.1, 0.0, 0.0, 0.0);
    EmitVertex();

    EndPrimitive();
}
```

调用 EmitVertex 前，顶点属性应该赋值给变量 gl_Position，类似于顶点着色器中的赋值。


## 动态生成几何图形

```cpp
void createGeometryShader() {
    const char* geometryShaderSrc = GLSL(
        layout(points) in;
    layout(line_strip, max_vertices = 64) out;

    in vec3 vColor[]; // Output from vertex shader for each vertex
    in float vSides[];

    out vec3 fColor; // Output to fragment shader

    const float PI = 3.1415926;

    void main() {
        fColor = vColor[0]; // Point has only one vertex

        //gl_Position = gl_in[0].gl_Position + vec4(-0.1, 0.0, 0.0, 0.0);
        //EmitVertex();

        //gl_Position = gl_in[0].gl_Position + vec4(0.1, 0.0, 0.0, 0.0);
        //EmitVertex();

        for (int i = 0; i <= vSides[0]; i++) {
            // Angle between each side in radians
            float ang = PI * 2.0 / vSides[0] * i;

            // Offset from center of point (0.3 to accomodate for aspect ratio)
            vec4 offset = vec4(cos(ang) * 0.3, -sin(ang) * 0.4, 0.0, 0.0);
            gl_Position = gl_in[0].gl_Position + offset;

            EmitVertex();
        }

        EndPrimitive();
    }
    );
    g_geometryShaderId = glCreateShader(GL_GEOMETRY_SHADER);
    glShaderSource(g_geometryShaderId, 1, &geometryShaderSrc, NULL);
    glCompileShader(g_geometryShaderId);
}
```


## 几何着色器

如果需要重复绘制一个网格，像三维游戏中的立方体，则可以通过几何着色器使用相似的方式产生立方体，只是每一个产生的实例都是相同的。

最新的 WebGL 和 OpenGL ES 标准不在支持几何着色器，开发移动应用和 web 应用请不要使用几何着色器。


## References

- [1] [几何着色器](https://blog.csdn.net/iron_lzn/article/details/48729849)
- [2] [LearnOpenGL CN 几何着色器](https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/09%20Geometry%20Shader/)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://blog.csdn.net/iron_lzn/article/details/48729849]({% include relref.html url="/backup/2020-11-12-shader-OpenGL-geometry.md/blog.csdn.net/b3b65693.html" %})
- [2] [https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/09%20Geometry%20Shader/]({% include relref.html url="/backup/2020-11-12-shader-OpenGL-geometry.md/learnopengl-cn.github.io/09c8e082.html" %})
