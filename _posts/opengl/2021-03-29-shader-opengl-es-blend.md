---
layout: post
title: "图形学笔记 -- OpenGL ES 混合"
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


## OpenGL ES 2.0

OpenGL ES 2.0 没有 VAO，绘制差异很大。
OpenGL ES 2.0 编程中，用于绘制的顶点数组数据首先保存在 CPU 内存，在调用 glDrawArrays 或者 glDrawElements 等进行绘制时，需要将顶点数组数据从 CPU 内存拷贝到显存。
OpenGL ES 3.0 编程中， VBO 和 EBO 的出现就是为了解决这个问题。[doc](https://developer.aliyun.com/article/782026)

```cpp
// 默认情况下，在 OpenGL 中，沿逆时针方向绘制的面为正面。
const GLfloat TRIANGLE_COORDS[] = {
     0.5f,  0.5f, -1.0f, // 右上角
     0.5f, -0.5f, -1.0f, // 右下角
    -0.5f, -0.5f, -1.0f, // 左下角
    -0.5f,  0.5f, -1.0f, // 左上角
};
glVertexAttribPointer(mPositionId, 3/*每组数据三个 float*/, GL_FLOAT, GL_FALSE, 0, TRIANGLE_COORDS);
// 1. GL_TRIANGLES：每三个顶之间绘制三角形，之间不连接。
// 2. GL_TRIANGLE_FAN：以 V0V1V2, V0V2V3, V0V3V4，……的形式绘制三角形。
// 3. GL_TRIANGLE_STRIP：顺序在每三个顶点之间均绘制三角形。这个方法可以保证从相同的方向上所有三角形均被绘制。
//    以 V0V1V2, V1V2V3, V2V3V4……的形式绘制三角形
glDrawArrays(GL_TRIANGLES, 0, 4/*数组长度 4*/); // 只会绘制 1 个三角形
```

* [NVIDIA -- OpenGL ES 2.0](https://docs.nvidia.com/gameworks/content/technologies/mobile/native_android_opengles.htm)
* [Tutorials: OpenGL ES 2.0](https://tool.oschina.net/uploads/apidocs/android/resources/tutorials/opengl/opengl-es20.html)
* [OpenGL ES SDK for Android -- Simple Triangle {% include relref_github.html %}](https://arm-software.github.io/opengl-es-sdk-for-android/simple_triangle.html)
* [构建 OpenGL ES 环境](https://developer.android.com/training/graphics/opengl/environment)
* [Android 开发者 文档 指南 OpenGL ES](https://developer.android.com/guide/topics/graphics/opengl)


### OpenGL 版本

```cpp
unsigned int uploadData() {

    float vertices[] = {
         0.5f,  0.5f, 0.0f, 0.1f, // top right
         0.5f, -0.5f, 0.0f, 0.1f, // bottom right
        -0.5f, -0.5f, 0.0f, 0.1f, // bottom left
        -0.5f,  0.5f, 0.0f, 0.1f, // top left
    };
    unsigned int indices[] = {
        0, 1, 3,  // first Triangle
        1, 2, 3   // second Triangle
    };

    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    glBindVertexArray(VAO);
    if (TRUE) {
        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
        // GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void* pointer
        // size 每组数据用到的个数
        // stride 一组数据的大小 sizeof(Vertex)
        // pointer 每组数据内部偏移
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
        glEnableVertexAttribArray(0);

        glBindBuffer(GL_ARRAY_BUFFER, 0);
    }
    if (TRUE) {
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
        // remember: do NOT unbind the EBO while a VAO is active as the bound element buffer
        // object IS stored in the VAO; keep the EBO bound.
        // glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    }
    glBindVertexArray(0);
    return VAO;
}

glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
glClear(GL_COLOR_BUFFER_BIT);

glUseProgram(shaderProgram);

glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
glBindVertexArray(0);

glfwSwapBuffers(window);
```


### glVertexAttribPointer in OpenGL and in OpenGLES

非常蛋疼。[doc](https://stackoverflow.com/questions/15380491/glvertexattribpointer-in-opengl-and-in-opengles)

```cpp
// OpenGL
glVertexAttribPointer(vs_position, 2, GL_FLOAT, GL_TRUE, 5 * sizeof(GLfloat), (const GLvoid*) (3*sizeof(GLfloat)) );

// OpenGL ES 2.0
GLFloat vertices[] = {...definition};
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, vertices);
```

They are the same function being used in two different ways.
I'd explain why it works this way, but you won't care, and it's for very stupid and irrelevant reasons.

What matters is what they're doing. And what they're doing depends on something that you didn't show:
what is bound to GL_ARRAY_BUFFER.

See, the behavior of glVertexAttribPointer changes depending on that. If there is no buffer object bound
to GL_ARRAY_BUFFER when you call glVertexAttribPointer, then the function will assume that the final
value is a pointer (like the function's name says: glVertexAttribPointer).
Specifically, it is a pointer into client-owned memory.

When it comes time to render, the vertex attribute data will come from the previously provided pointer.
Thus, the second example is just using an array of client data, declared in standard C style,
as the source data. No buffer objects are involved.

Note: the core profile of OpenGL 3.1+ removed the ability to use client memory;
there, you must use buffer objects, as explained below.

If a buffer object is bound to GL_ARRAY_BUFFER when glVertexAttribPointer is called,
then something special happens. OpenGL will pretend that the pointer (which is what the final
parameter is as far as C/C++ is concerned) is actually a byte offset into the buffer
bound to GL_ARRAY_BUFFER. It will convert the pointer into an integer and then store
that integer offset and the buffer object currently bound to GL_ARRAY_BUFFER.

So the above code takes 3\*sizeof(GLfloat), the byte offset, and converts it into a pointer.
OpenGL will take the pointer and convert it back into an offset, yielding 3\*sizeof(GLfloat) again.

When it comes time to render, OpenGL will then read from the previously given buffer object,
using the previously given offset.

The first example puts the vertex data into a buffer object in GPU memory.
The second example puts the vertex data in a regular C/C++ array, in CPU memory.

[Stride argument in OpenGL ES 2.0](https://community.arm.com/developer/tools-software/graphics/b/blog/posts/stride-argument-in-opengl-es-2-0)

```cpp
GLfloat arr[] = {
  /* 0x20000 */ -1.0f, 1.0f, 1.0f, 0.0f, 1.0f,
  /* 0x20014 */ -1.0f, 0.0f, 1.0f, 0.0f, 0.0f,
  /* 0x20028 */  0.0f, 1.0f, 1.0f, 1.0f, 1.0f
};
glVertexAttribArray(your_glsl_attrib_index, 3, GL_FLOAT, GL_FALSE, 20, arr);
```

And then use glDrawArrays, the OpenGL implementation will do something akin to this :

Copy the address arr (0x20000).
Start reading {-1.0f, 1.0f, 1.0f} from the copied address (referred as copy_arr here) and
pass these values to the GLSL attribute identified by your_glsl_attrib_index.
Do something like copy_arr += stride. At this point, copy_arr == 0x20014.


## OpenGL ES glBlendFunc

[OpenGL ES 绘制贝塞尔曲线 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/111611096)


## OpenGL API 之 glTexEnv

[from {% include relref_csdn.html %}](https://blog.csdn.net/csxiaoshui/article/details/53505933)

通过上面的组合，模拟 glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_ADD); 的效果：

```cpp
glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE);

glTexEnvf(GL_TEXTURE_ENV, GL_COMBINE_RGB, GL_ADD);
glTexEnvf(GL_TEXTURE_ENV, GL_SOURCE0_RGB, GL_PRIMARY_COLOR);
glTexEnvf(GL_TEXTURE_ENV, GL_SOURCE1_RGB, GL_TEXTURE);
glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND0_RGB, GL_SRC_COLOR);
glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND1_RGB, GL_SRC_COLOR);

glTexEnvi(GL_TEXTURE_ENV, GL_COMBINE_ALPHA, GL_MODULATE);
glTexEnvi(GL_TEXTURE_ENV, GL_SOURCE0_ALPHA, GL_PRIMARY_COLOR);
glTexEnvi(GL_TEXTURE_ENV, GL_SOURCE1_ALPHA, GL_TEXTURE);
glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND0_ALPHA, GL_SRC_ALPHA);
glTexEnvi(GL_TEXTURE_ENV, GL_OPERAND1_ALPHA, GL_SRC_ALPHA);

// 这里存在疑问，这两个函数有啥区别？C++ 都能编译过。
void glTexEnvf(GLenum target, GLenum pname, GLfloat param);
void glTexEnvi(GLenum target, GLenum pname, GLint param);
```

{% include image.html url="/assets/images/210329-shader-opengl-es-blend/20161208163641478.png" %}

[Docs » 高级 OpenGL » 混合](https://learnopengl-cn.readthedocs.io/zh/latest/04%20Advanced%20OpenGL/03%20Blending/)


## 独立实验

* [OpenGL 中的混合 (blend) {% include relref_csdn.html %}](https://blog.csdn.net/alicehyxx/article/details/4263058)

* glBlendFunc( GLenum sfactor, GLenum dfactor ); // 混合函数
* glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA ); // 根据贴上去的图片的 alpha 计算，是最常使用的。
* glBlendFunc( GL_ONE , GL_ZERO );  // 源色将覆盖目标色，直接覆盖了。
* glBlendFunc( GL_ZERO , GL_ONE );  // 目标色将覆盖源色，如果底图不透明，什么都没有，贴不上去。

* GL_SRC_ALPHA_SATURATE (f,f,f,1) : f = min(As, 1-Ad)
* 将多边形从远至近排列，并使用以下函数
* glBlendFunc( GL_SRC_ALPHA_SATURATE , GL_ONE );
* glEnable( GL_POLYGON_SMOOTH );
* 可以优化多边形反走样；但必须有 α 位平面，以用来存储累加的覆盖值。

* 当输入颜色值为 RGB 时，混合计算时，A 值默认为 0.0。

* [OpenGL ES -- 混合](https://www.heqiangfly.com/2020/04/30/opengl-es-color-blend/)

```glsl
#version 330 core
in vec2 TexCoords;

out vec4 color;

uniform sampler2D texture1;

void main()
{
    vec4 texColor = texture(texture1, TexCoords);
    if(texColor.a < 0.1)
        discard;
    color = texColor;
}
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-29-shader-opengl-es-blend.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://developer.aliyun.com/article/782026]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/developer.aliyun.com/156f5476.html" %})
- [https://docs.nvidia.com/gameworks/content/technologies/mobile/native_android_opengles.htm]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/docs.nvidia.com/9718b03b.htm" %})
- [https://tool.oschina.net/uploads/apidocs/android/resources/tutorials/opengl/opengl-es20.html]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/tool.oschina.net/c495466f.html" %})
- [https://arm-software.github.io/opengl-es-sdk-for-android/simple_triangle.html]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/arm-software.github.io/09de944d.html" %})
- [https://developer.android.com/training/graphics/opengl/environment]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/developer.android.com/e0fe5c7d.html" %})
- [https://developer.android.com/guide/topics/graphics/opengl]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/developer.android.com/39561e3a.html" %})
- [https://stackoverflow.com/questions/15380491/glvertexattribpointer-in-opengl-and-in-opengles]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/stackoverflow.com/a2d1f30c.html" %})
- [https://community.arm.com/developer/tools-software/graphics/b/blog/posts/stride-argument-in-opengl-es-2-0]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/community.arm.com/714cb84e.html" %})
- [https://zhuanlan.zhihu.com/p/111611096]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/zhuanlan.zhihu.com/7e4d93d1.html" %})
- [https://blog.csdn.net/csxiaoshui/article/details/53505933]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/blog.csdn.net/698b3f27.html" %})
- [https://learnopengl-cn.readthedocs.io/zh/latest/04%20Advanced%20OpenGL/03%20Blending/]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/learnopengl-cn.readthedocs.io/7ca72863.html" %})
- [https://blog.csdn.net/alicehyxx/article/details/4263058]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/blog.csdn.net/aca962c2.html" %})
- [https://www.heqiangfly.com/2020/04/30/opengl-es-color-blend/]({% include relref.html url="/backup/2021-03-29-shader-opengl-es-blend.md/www.heqiangfly.com/721ce01e.html" %})
