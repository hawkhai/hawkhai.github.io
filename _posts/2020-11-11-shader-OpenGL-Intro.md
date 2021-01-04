---
layout: post
title: "特效编程笔记 -- 计算机图形学 OPENGL 入门"
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

以前随便找点代码，改吧改吧就能跑，今天算是入门学习了一下。
顶点着色器、几何着色器、片段着色器。又酷又通透 ——

本文源码 <a href="{% include gitsrc.html url="/source/shader/LearnOpenGL-Introduction" %}" target="_blank">LearnOpenGL-Introduction</a>

* 相关代码

    * 课程完整源码：<https://github.com/hawkhai/LearnOpenGL.git>
    * 用到第三方库：<https://gitee.com/hawkhai/opengl-3rd.git>


## uni-marburg.de 课程

<https://www.uni-marburg.de/en/fb12/research-groups/grafikmultimedia/lectures/graphics>

<https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/graphics_9_1_eng_web.html>

[OpenGL Step by Step - OpenGL Development](http://ogldev.atspace.co.uk/index.html)


## 历史

1988 年 5 月，Pixar 公布了第三版 RenderMan 规范，将「着色器」的使用推广到了我们目前所知的各大应用领域。

随着图形处理器的进步，OpenGL 和 Direct3D 等主要的图形软件库都开始支持着色器。
第一批支持着色器的 GPU 仅支持像素着色器，但随着开发者逐渐认识到着色器的强大，很快便出现了顶点着色器。
2000 年，第一款支持可编程像素着色器的显卡 Nvidia GeForce 3（NV20）问世。Direct3D 10 和 OpenGL 3.2 则引入了几何着色器。

{% include image.html url="/assets/images/201111-shader-opengl-intro/faa27c0e4a3a4b7eb3436c016ce606f1.jpeg"
caption="利用 gpu 渲染一个巨人的图像" %}

[计算机图形学 OPENGL 入门 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1px41197A5)

<https://ke.qq.com/course/package/25480?flowToken=1019441>

<https://learnopengl-cn.github.io/>


## Others

- 包含部分第三方库：<https://github.com/Groovounet/ogl-samples>

- 几个完整得范例：<https://github.com/hawkhai/openglcpp.git>

    * computeShaderParticleSystem.vcxproj / computeShader.sln
        * OpenGL Compute Shader Particle System：Attraction based compute shader particle system using SSBOs.
        * \#define GL_COMPUTE_SHADER 0x91B9
        * \#define GL_VERTEX_SHADER 0x8B31
        * \#define GL_FRAGMENT_SHADER 0x8B30
        * This compute shader implements a very basic attraction based particle system that changes velocities to move the particles towards the target position.
        * 40 帧，2048 个粒子，CPU & GPU 都能大概控制在 5%。
        * 平常我们使用的 Shader 有顶点着色器、几何着色器、片段着色器，这几个都是为光栅化图形渲染服务的，**OpenGL 4.3（发布日期：2012 年 8 月 6 日）**之后新出了一个 Compute Shader，用于通用计算并行加速。[link {% include relref_cnblogs.html %}](https://www.cnblogs.com/chen9510/p/12000320.html)
        * OpenGL ES 3.1 使用计算着色器（Compute Shader）[link {% include relref_csdn.html %}](https://blog.csdn.net/qq_39561000/article/details/103112147)

    * eglExample.vcxproj / eglExample.sln [没运行成功] -- \eglapp\app.vcxproj 完成了。[Debug x64]
        * Shows how to use EGL for setting up OpenGL ES 2.0 on a windows desktop. Only works for vendors that support EGL on desktop.
        * [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
        * [SimpleGL Example](https://wiki.maemo.org/SimpleGL_example)
        * [OpenGL ES EGL 简介 -- 完整的一个文档用例 {% include relref_csdn.html %}](https://blog.csdn.net/iEearth/article/details/71180457)
        * [EGL 1.5 implementation for Windows and X11 supporting OpenGL. {% include relref_github.html %}](https://github.com/McNopper/EGL)

    * geometryShaderSimple.vcxproj / geometryShader.sln
        * Very simple geometry shader demo.
        * This geometry shader takes a single GL_POINT as input and generates triangles for a complete circle.

    * instancing.vcxproj [没运行成功]
        * 多实例的 demo，LearnOpenGL 里面有类似的例子：`glDrawElementsInstanced`。
        * Mesh instancing (OpenGL 3.3+) demo. Made to compare against the same Vulkan example.

    * raypicking.vcxproj / raypicking.sln [没运行成功]
        * CPU based ray picking for object selection.

    * SPIRVShader.vcxproj / SPIRVShader.sln [没运行成功]
        * Shows how to load binary SPIR-V Shaders with OpenGL. SPIR-V has initially been introduced as the binary shader format for Vulkan, but is also available on OpenGL via the GL_ARB_gl_spirv extension.
        * This example loads two basic binary SPIR-V shaders instead of GLSL shaders from text. SPIR-V shaders for OpenGL can be generated using the glslang reference compiler. If you're using Visual Studio, you can use my SPIRV-VSExtension to generate SPIR-V from GLSL directly out of the IDE.

    * triangle.vcxproj / triangle.sln
        * OpenGL example - Indexed triangle rendering
        * <https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/08%20Advanced%20GLSL/#uniform>
        * [Unform Buffer Objecct(UBO) {% include relref_cnblogs.html %}](https://www.cnblogs.com/chen9510/p/11447292.html)
        * [Uniform Buffer Object {% include relref_khronos.html %}](https://www.khronos.org/opengl/wiki/Uniform_Buffer_Object)
        * error LNK2019: 无法解析的外部符号 _stbi_load -> 需要在 #include <stb_image.h> 前增加一句 #define STB_IMAGE_IMPLEMENTATION。

{% include image.html url="/assets/images/201111-shader-opengl-intro/computeshaderparticlesystem.gif" %}
{% include image.html url="/assets/images/201111-shader-opengl-intro/20201203151447.png" %}

- __imp__vsnprintf

错误 LNK2019 无法解析的外部符号 \_\_imp\_\_vsnprintf，该符号在函数 \_\_glfwInputError 中被引用 LearnOpenGL E:\kSource\LearnOpenGLk\LearnOpenGL\glfw3.lib(init.obj) 1

原因：问题是 glfw 静态 libs 是用与您正在使用的版本不同的 visual studio 版本构建的。
> 你也可以添加一个额外的库到你的链接器输入，即 legacy_stdio_definitions.lib。进入“属性”>“链接器”>“输入”。在其他依赖项中添加上面提到的库。<https://zgserver.com/parsing-6.html>


### vulkan 与 SPIR-V

* 小科普 -- 图形接口 vulkan 与 SPIR-V

Khronos 组织在 GDC 2015 大会上发布了 Vulkan API。关于 Vulkan 的细节，类似于 AMD Mantle 和微软 DirectX 12，Vulkan 是一个底层 3D 图形 API，允许开发者获得硬件底层控制能力，同时减少性能开销，Vulkan 为开发人员提供通常留给驱动程序的控制能力，如线程管理，内存管理和错误检查等等功能。

Standard, Portable Intermediate Representation - V (SPIR-V)
OpenGL 4.6 的最大变化就是 支持 SPIR-V，一种用于 GPU 通用计算和图形学的中间语言，Khronos 开发设计，最初是为 OpenCL 规范准备的，和下一代图形标准 Vulkan 差不多同时提出，也在不断发展完善。

{% include image.html url="/assets/images/201111-shader-opengl-intro/microsoft-shader-conductor-architecture.jpg" %}


### instancing.vcxproj

* 每个 Instance 不一样的数据

```cpp
struct UboInstanceData {
    // Model matrix for each instance
    glm::mat4 model;
    // Color for each instance
    // vec4 is used due to memory alignment
    // GPU aligns at 16 bytes
    glm::vec4 color;
};

glGenBuffers(1, &UBOInst);
glBindBuffer(GL_UNIFORM_BUFFER, UBOInst);
glBufferData(GL_UNIFORM_BUFFER, uboInstance.size() * sizeof(UboInstanceData), uboInstance.data(), GL_DYNAMIC_DRAW);
glBindBuffer(GL_UNIFORM_BUFFER, 0);

glBindBuffer(GL_UNIFORM_BUFFER, UBO);
GLvoid* p = glMapBuffer(GL_UNIFORM_BUFFER, GL_WRITE_ONLY);
memcpy(p, &uboVS, sizeof(uboVS));
glUnmapBuffer(GL_UNIFORM_BUFFER);
```

* 所有模型都一样的数据

```cpp
struct GlobalMatricesData {
    // Global matrices
    struct MatricesData {
        glm::mat4 projection;
        glm::mat4 view;
    } matrices;
    // Seperate data for each instance
} uboVS;

// Uniform buffer object
glGenBuffers(1, &UBO);
glBindBuffer(GL_UNIFORM_BUFFER, UBO);
glBufferData(GL_UNIFORM_BUFFER, sizeof(uboVS), &uboVS, GL_DYNAMIC_DRAW);
glBindBuffer(GL_UNIFORM_BUFFER, 0);

glBindBuffer(GL_UNIFORM_BUFFER, UBOInst);
GLvoid* p = glMapBuffer(GL_UNIFORM_BUFFER, GL_WRITE_ONLY);
memcpy(p, uboInstance.data(), uboSize);
glUnmapBuffer(GL_UNIFORM_BUFFER);
```

```glsl
#version 450

#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

layout (location = 0) in vec3 inPos;
layout (location = 1) in vec3 inNormal;
layout (location = 3) in vec3 inColor;

struct Instance
{
    mat4 model;
    vec4 color;
};

layout (binding = 0) uniform UBO
{
    mat4 projection;
    mat4 view;
} ubo;

layout (binding = 1) uniform UBOInst
{
    Instance instance[343];
} uboinstance;

layout (location = 0) out vec3 outNormal;
layout (location = 1) out vec3 outColor;
layout (location = 2) out vec3 outEyePos;
layout (location = 3) out vec3 outLightVec;

void main()
{
    outNormal = inNormal;
    outColor = inColor;
    outColor = uboinstance.instance[gl_InstanceID].color.rgb;
    mat4 modelView = ubo.view * uboinstance.instance[gl_InstanceID].model;
    gl_Position = ubo.projection * modelView * vec4(inPos.xyz, 1.0);
    outEyePos = (gl_Position).xyz;
    vec4 lightPos = vec4(0.0, 0.0, 0.0, 1.0) * modelView;
    outLightVec = normalize(lightPos.xyz - outEyePos);
}
```

```glsl
#version 450

#extension GL_ARB_separate_shader_objects : enable
#extension GL_ARB_shading_language_420pack : enable

layout (location = 0) in vec3 inNormal;
layout (location = 1) in vec3 inColor;
layout (location = 2) in vec3 inEyePos;
layout (location = 3) in vec3 inLightVec;

layout (location = 0) out vec4 outFragColor;

void main()
{
    vec3 N = normalize(inNormal);
    vec3 L = normalize(vec3(1.0));

    vec3 Eye = normalize(-inEyePos);
    vec3 Reflected = normalize(reflect(-inLightVec, inNormal));

    vec4 IAmbient = vec4(vec3(0.1), 1.0);
    vec4 IDiffuse = vec4(1.0) * max(dot(inNormal, inLightVec), 0.0);

    float specular = 0.75;
    vec4 ISpecular = vec4(0.5, 0.5, 0.5, 1.0) * pow(max(dot(Reflected, Eye), 0.0), 4.0) * specular;

    outFragColor = vec4((IAmbient + IDiffuse) * vec4(inColor, 1.0) + ISpecular);
}
```


## 第一课

- 状态机上下文软件环境

    状态机：当前绘制状态、光照设置、纹理设置、材质设置。

- GLFW 窗口

    生成窗口，支持 OpenGL 上下文。

- GLAD

    用户画图。

- 顶点数组对象 VAO 顶点缓冲对象 VBO

    * 顶点数组对象：Vertex Array Object，VAO
    * 顶点缓冲对象：Vertex Buffer Object，VBO
    * 索引缓冲对象：Element Buffer Object，EBO 或 Index Buffer Object，IBO

    输入：3D 坐标；输出：2D 像素。

{% include image.html url="/assets/images/201111-shader-opengl-intro/20201112141055.png" %}

- FragmentShader 片段着色器

    1. 将着色器源码存入字符串
    2. 创建着色器对象
    3. 将源码字符串赋予着色器对象
    4. 编译着色器
    5. 创建着色器程序对象
    6. 将编译好的着色器附加到程序对象上
    7. 链接生成程序

- VertexShader 顶点着色器

- 索引缓冲对象 EBO

    其中在渲染的时候有多重的组合方式：

    VBO / VAO / EBO

    建议使用顶点缓冲区，但是是否索引可以参考他们的优劣：

    * `glDrawArrays` 传输或指定的数据是最终的真实数据，在绘制时效能更好
    * `glDrawElements` 指定的是真实数据的调用索引，在内存 / 显存占用上更节省

- GLSL 数据传输

- VBO 中存放多种属性

- 一个 VAO 对应多个 VBO

[OpenGL ES in iOS - 2. 画一个三角形](https://www.uiimage.com/post/blog/opengl-es/opengl-es-2-draw-a-triangle/)

```cpp
// Default VAO needed for OpenGL 3.3+ core profiles
void setVertexEnv() {
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, // left, down
        0.5f, -0.5f, 0.0f,  // right, down
        -0.5f, 0.5f, 0.0f,  // left, top
    };
    float colors[] = {
        1, 0, 0, // left, down
        0, 1, 0, // right, down
        0, 0, 1, // left, top
    };

    unsigned int VAO; // VAO: vertex array object
    unsigned int VBO[2]; // VBO: vertex buffer object

    glGenVertexArrays(1, &VAO);
    glGenBuffers(2, VBO);

    // 绑定当前上下文
    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO[0]);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, VBO[1]);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colors), colors, GL_STATIC_DRAW);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(1);
}
```

- 图元连接方式

{% include image.html url="/assets/images/201111-shader-opengl-intro/23e3ac4c617.jpg" %}

1. GL_POINTS 每个顶点在屏幕上都是单独的点。
2. GL_LINES 每一对顶点定义一个线段。
3. GL_LINE_STRIP 一个从第一个顶点依次经过每一个后续顶点而绘制的线条。
4. GL_LINE_LOOP 和 GL_LINE_STRIP 相同，但是最后一个顶点和第一个顶点连接起来了。
5. GL_TRIANGLES 每三个顶点构成一个三角形。
6. GL_TRIANGLE_STRIP 三角形带，新增一个顶点，就复用前面的两个顶点，构成一个新的三角形。
7. GL_TRIANGLE_FAN 以一个原点为中心，呈扇形排列，公用相邻顶点的一组三角形。


## 第二课

- shader 类封装

- 加载显示纹理

- 纹理过滤

- 纹理单元

- 齐次坐标

- 线性代数基础：三维里沿着 x 轴旋转

- 线性代数基础：变换

- glm

- 缩放旋转位移顺序问题

- 坐标系统


## 第三课

- 坐标系实例

- 立方体

- 摄像机

- LookAt

- 摄像机 WASD 空指

- 摄像机旋转缩放

- 代码整理 Camera 封装

```cpp
// i 表示 32 位整形
// f 表示 32 位浮点型
// ub 表示 8 位无符号 byte
// ui 表示 32 位无符号整形
// v 表示接受相应的指针类型

void setInt(int value)          glUniform1i(value);
void setBool(bool value)        glUniform1i((int)value);
void setFloat(float value)      glUniform1f(value);

void setVec2(glm::vec2 &value)  glUniform2fv(1, &value[0]);
void setVec3(glm::vec3 &value)  glUniform3fv(1, &value[0]);
void setVec4(glm::vec4 &value)  glUniform4fv(1, &value[0]);

void setVec2(float x, float y)  glUniform2f(x, y);
void setVec3(float x, float y, float z) glUniform3f(x, y, z);
void setVec4(float x, float y, float z, float w) glUniform4f(x, y, z, w);

void setMat2(glm::mat2 &mat)    glUniformMatrix2fv(1, &mat[0][0]);
void setMat3(glm::mat3 &mat)    glUniformMatrix3fv(1, &mat[0][0]);
void setMat4(glm::mat4 &mat)    glUniformMatrix4fv(1, &mat[0][0]);
```


## 运行结果

相机源码：<https://github.com/JoeyDeVries/LearnOpenGL/blob/master/src/1.getting_started/7.4.camera_class/camera_class.cpp>

{% include image.html url="/assets/images/201111-shader-opengl-intro/boxtest.gif" %}

{% include image.html url="/assets/images/201111-shader-opengl-intro/glintrograb.gif" %}

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/hawkhai/LearnOpenGL.git]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/github.com/1371fb1d.git" %})
- [https://gitee.com/hawkhai/opengl-3rd.git]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/gitee.com/3cdcc6e8.git" %})
- [https://www.uni-marburg.de/en/fb12/research-groups/grafikmultimedia/lectures/graphics]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.uni-marburg.de/2b3b5349.html" %})
- [https://www.mathematik.uni-marburg.de/~thormae/lectures/graphics1/graphics_9_1_eng_web.html]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.mathematik.uni-marburg.de/cda8cdff.html" %})
- [http://ogldev.atspace.co.uk/index.html]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/ogldev.atspace.co.uk/dc93b5ea.html" %})
- [https://www.bilibili.com/video/BV1px41197A5]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.bilibili.com/e1622428.html" %})
- [https://ke.qq.com/course/package/25480?flowToken=1019441]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/ke.qq.com/3fd1c97a.html" %})
- [https://learnopengl-cn.github.io/]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/learnopengl-cn.github.io/e0710dd2.html" %})
- [https://github.com/Groovounet/ogl-samples]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/github.com/da66ecca.html" %})
- [https://github.com/hawkhai/openglcpp.git]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/github.com/24544c96.git" %})
- [https://www.cnblogs.com/chen9510/p/12000320.html]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.cnblogs.com/717083ae.html" %})
- [https://blog.csdn.net/qq_39561000/article/details/103112147]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/blog.csdn.net/b11e47b9.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.saschawillems.de/5efcfffd.html" %})
- [https://wiki.maemo.org/SimpleGL_example]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/wiki.maemo.org/ceafcc8b.html" %})
- [https://blog.csdn.net/iEearth/article/details/71180457]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/blog.csdn.net/6ff86f67.html" %})
- [https://github.com/McNopper/EGL]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/github.com/84bf5cd8.html" %})
- [https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/08%20Advanced%20GLSL/#uniform]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/learnopengl-cn.github.io/f1d48aaa.html" %})
- [https://www.cnblogs.com/chen9510/p/11447292.html]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.cnblogs.com/cfd7fec8.html" %})
- [https://www.khronos.org/opengl/wiki/Uniform_Buffer_Object]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.khronos.org/04bc8242.html" %})
- [https://zgserver.com/parsing-6.html]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/zgserver.com/060e6561.html" %})
- [https://www.uiimage.com/post/blog/opengl-es/opengl-es-2-draw-a-triangle/]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/www.uiimage.com/9d22c628.html" %})
- [https://github.com/JoeyDeVries/LearnOpenGL/blob/master/src/1.getting_started/7.4.camera_class/camera_class.cpp]({% include relref.html url="/backup/2020-11-11-shader-OpenGL-Intro.md/github.com/5c619a05.cpp" %})
