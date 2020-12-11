---
layout: post
title: "“特效编程”笔记 -- OpenGL 图形学 / 模型加载"
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

不同 3D 引擎实现千差万别，但模型都是由非常多的三角形拼接组成。解析模型数据，然后得到所有三角形并完成绘制。

{% include image.html url="/assets/images/201211-shader-opengl-model-loa~a7/glmodelgrab.gif" %}

OpenGL 模型加载。解析模型文件，得到一堆三角形数据，把这些三角形绘制出来，就是这个样子了。

本文源码 <a href="{% include gitsrc.html url="/source/shader/LearnOpenGL-Model" %}" target="_blank">LearnOpenGL-Model</a>


## Assimp

一个非常流行的模型导入库是 Assimp，它是 Open Asset Import Library（开放的资产导入库）的缩写。
Assimp 能够导入很多种不同的模型文件格式（并也能够导出部分的格式），它会将所有的模型数据加载至 Assimp 的通用数据结构中。

{% include image.html url="/assets/images/201211-shader-opengl-model-loa~a7/assimp_structure.png" %}

一个 Mesh 对象本身包含了渲染所需要的所有相关数据，像是顶点位置、法向量、纹理坐标、面 (Face) 和物体的材质。

一个网格包含了多个面。Face 代表的是物体的渲染图元 (Primitive)（三角形、方形、点）。一个面包含了组成图元的顶点的索引。由于顶点和索引是分开的，使用一个索引缓冲来渲染是非常简单的。


## 网格 Mesh

我们定义 Vertex：

```cpp
struct Vertex {
    glm::vec3 Position; // 顶点位置
    glm::vec3 Normal; // 法线
    glm::vec2 TexCoords; // 纹理坐标
};
```

定义一个纹理：

```cpp
struct Texture {
    unsigned int id; // 对应的 glGenTextures ID。
    string type; // 和 glsl shader 对应，根据这个名字完成参数传递。
    string path; // 图片文件路径。
};

#define TEXTURE_TYPE_DIFFUSE  "texture_diffuse"
#define TEXTURE_TYPE_SPECULAR "texture_specular"
```

相应的 glsl 就是：

```glsl
uniform sampler2D texture_diffuse1;
```

那么一个网格（Mesh）可以定义为：

```cpp
class Mesh {
    vector<Vertex> vertices;
    vector<unsigned int> indices;
    vector<Texture> textures;
    unsigned int VAO, VBO, EBO;
};

// 绘制就是：
void Draw(Shader& shader)
{
    glBindVertexArray(VAO);
    glDrawElements(GL_TRIANGLES, indices.size(), GL_UNSIGNED_INT, 0);
}
```


## 模型 Model

一个模型由非常多的 Mesh 组成，可以定义为：

```cpp
class Model {
    vector<Mesh> meshes;
};

// 绘制就是：
void Draw(Shader& shader)
{
    for (unsigned int i = 0; i < meshes.size(); i++)
        meshes[i].Draw(shader);
}
```


## 最终效果

{% include image.html url="/assets/images/201211-shader-opengl-model-loa~a7/model_diffuse.png" %}

{% include image.html url="/assets/images/201211-shader-opengl-model-loa~a7/model_lighting.png" %}

[LearnOpenGL 模型加载](https://learnopengl-cn.github.io/03%20Model%20Loading/01%20Assimp/)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://learnopengl-cn.github.io/03%20Model%20Loading/01%20Assimp/]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Model-loading.md/learnopengl-cn.github.io/a7063ebf.html" %})
