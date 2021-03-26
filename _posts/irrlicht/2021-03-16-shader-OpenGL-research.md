---
layout: post
title: "图形学笔记 -- OpenGL Research 基本函数调用整理"
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

Irrlicht GLES 分析。


## Draw

* glEnableVertexAttribArray
    * index=2;
* glVertexAttribPointer
    * index=0; size=3; type=5126; normalized=; stride=68; pointer=<ADDRESS>;
    * 在内存中采用交叉模式存储，向 gpu 传入顶点数据的方法。
    * 注意，这里的 offset 是内存中大小的偏移，必须准确计算出内存大小偏移量 sizeof。
    * glVertexAttribPointer(naPosition, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (GLvoid*)0);
    * glVertexAttribPointer(naTexcoord, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (const GLvoid*)(2*sizeof(float)));
* glDrawElements
    * mode=4; count=6; type=5123; indices=<ADDRESS>;
* glDisableVertexAttribArray
    * index=0;


## Uniform & Program

* glUseProgram
    * program=73;
* glUniform1iv
    * location=2; count=1; value=<ADDRESS>;
* glUniformMatrix4fv
    * location=0; count=1; transpose=; value=<ADDRESS>;
* glUniform1fv
    * location=67; count=1; value=<ADDRESS>;


## 全局设置

* glEnable
    * ap=2884;
* glDisable
    * cap=3042;
* glColorMask
    * red=; green=; blue=; alpha=;
* glCullFace
    * mode=1029;
* glFrontFace
    * mode=2304;
* glViewport
    * x=0; y=0; width=1920; height=1080;

* glBlendFunc
    * sfactor=1; dfactor=0;
    * glEnable(GL_BLEND); // 启动混合并设置混合因子
    * glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA); // 表示源颜色乘以自身的 alpha 值，目标颜色乘以 1.0 减去源颜色的 alpha 值，然后相加，得到新的颜色。
* glDepthFunc
    * efunc=513;
    * glDisable(GL_DEPTH_TEST);
    * 指通过目标像素与当前像素在 z 方向上值大小的比较是否满足参数指定的条件，来决定在深度（Z 方向）上是否绘制目标像素，该函数只有启用“深度测试”时才有效。
* glDepthMask
    * flag=;
    * 1) 开启深度写入，glDepthMask( GL_TRUE )
    * 2) 渲染所有的不透明物体，以任何顺序
    * 3) 关闭深度写入，glDepthMask( GL_FALSE )
    * 4) 开启混合 glEnable( GL_BLEND )
    * 5) 从远到近渲染透明物体
* glLineWidth
    * width=1;


## 绘制前 Clear

* glClearColor
    * red=0; green=0; blue=0; alpha=0;
* glClearDepthf
    * d=1;
* glClear
    * mask=16640;
* glFlush


## 纹理生成

* glGenTextures
    * n=1; textures=<ADDRESS>;
* glBindTexture
    * target=3553; texture=1;
* glTexParameteri
    * target=3553; pname=10241; param=9728;
* glHint
    * target=33170; mode=4352;
    * glHint(GL_GENERATE_MIPMAP_HINT, GL_DONT_CARE);
* glTexImage2D **上传图片数据。**
    * target=3553; level=0; internalformat=32993; width=64; height=64; border=0; format=32993; type=5121; pixels=<ADDRESS>;
    * glTexImage2D(GL_TEXTURE_2D, 0, InternalFormat, Size.Width, Size.Height, 0, PixelFormat, PixelType, 0);
    * internalformat 指定纹理中的颜色组件。可选的值有 GL_ALPHA, GL_RGB, GL_RGBA, GL_LUMINANCE, GL_LUMINANCE_ALPHA 等几种。
    * format 像素数据的颜色格式，不需要和 internalformatt 取值必须相同。可选的值参考 internalformat。
    * type 指定像素数据的数据类型。可以使用的值有 GL_UNSIGNED_BYTE, GL_UNSIGNED_SHORT_5_6_5, GL_UNSIGNED_SHORT_4_4_4_4, GL_UNSIGNED_SHORT_5_5_5_1。
* glGenerateMipmap
    * target=3553;
* glActiveTexture
    * texture=33985;
* glPixelStorei 对齐像素字节函数：[glPixelStorei {% include relref_csdn.html %}](https://blog.csdn.net/keneyr/article/details/102727363)
    * pname=3333; param=1;
    * glPixelStorei(GL_UNPACK_ALIGNMENT,1) 控制的是所读取数据的对齐方式，默认 4 字节对齐，
        即一行的图像数据字节数必须是 4 的整数倍，即读取数据时，读取 4 个字节用来渲染一行，
        之后读取 4 字节数据用来渲染第二行。对 RGB 3 字节像素而言，若一行 10 个像素，即 30 个字节，在 4 字节对齐模式下，
        OpenGL 会读取 32 个字节的数据，若不加注意，会导致 glTextImage 中致函数的读取越界，从而全面崩溃。
    * 1) glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    * 2) glTexImage2D(,,,, &pixelData);
    * 3) glPixelStorei(GL_UNPACK_ALIGNMENT, 4);

```cpp
glGenTextures(1, &texture);
glBindTexture(GL_TEXTURE_2D, texture);
... // 上传图片等操作
glBindTexture(GL_TEXTURE_2D, 0); // Unbind texture

// Bind Textures using texture units
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, texture);
glUniform1i(glGetUniformLocation(Program, "ourTexture"), 0);
```

纹理与 sampler2D 变量的关联是通过索引来关联的。
状态机，A 关联 B，B 关联 C，从而实现了 A 关联 C。开始不理解为什么设计成这样，慢慢的居然感受到了一种暴力美学。
这边绑定状态机，那边绑定 Shader，中间再关联一下，这样任何一边都可以自由修改和接入。

从本地内存向 GPU 的传输（UNPACK），包括各种 glTexImage、glDrawPixel；
从 GPU 到本地内存的传输（PACK），包括 glGetTexImage、glReadPixel 等。
也正因如此，PBO 也有 PACK 和 UNPACK 模式的区别。

```cpp
// 我们可以给 sampler2D 变量赋 int 值。
GLuint tex_loc = glGetUniformLocation(program, "tex");
// GL_TEXTURE1 又与值为 1 的 sampler2D 变量关联
glUniform1i(tex_loc, 1); // 这个 1 其实代表 GL_TEXTURE1

glActiveTexture(GL_TEXTURE1); // 将纹理与 GL_TEXTURE1 关联起来。
glBindTexture(GL_TEXTURE_2D, tex_id); // tex_id 与 GL_TEXTUR1 关联
```

平时使用单张纹理怎么不需要 glActiveTexture？<br/>
**sampler2D 默认值为 0，纹理也默认与 GL_TEXTURE0 关联。**

```cpp
GLuint GetDebugTextureId() {
    static GLuint texture = 0;
    if (texture != 0) {
        return texture;
    }
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);
    if (true) {
        GLubyte data[] = {
            255, 0, 0, 155,
            0, 255, 0, 155,
            0, 0, 255, 155,
            255, 255, 255, 155 };
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

        GLsizei width = 2;
        GLsizei height = 2;
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);
    }
    glBindTexture(GL_TEXTURE_2D, 0);
    return texture;
}

GLint SetProgramUniformTexture(GLuint program, const GLchar* name, GLuint texture) {
    glActiveTexture(GL_TEXTURE0);
    // texture 和 GL_TEXTURE0 绑定
    glBindTexture(GL_TEXTURE_2D, texture);
    int location = glGetUniformLocation(program, name);
    // Shader 和 GL_TEXTURE0 绑定。
    glUniform1i(location, 0);
}
```


## 获取当前 gles 环境参数

* glGetString
    * name=7938; --> RESULT=OpenGL ES 2.0 (ANGLE 2.1.0.57ea533f79a7);
* glGetIntegerv
    * pname=34930; data=<ADDRESS>;
* glGetFloatv
    * pname=33902; data=<ADDRESS>;
* glGetError
    * --> RESULT=0;


## egl 部分

* eglBindAPI Set the current rendering API.
    * api=12448; --> RESULT=1;
* eglCreateWindowSurface 创建一个 EGL 窗口 surface。
    * dpy=<ADDRESS>; config=<ADDRESS>; win=<ADDRESS>; attrib_list=<ADDRESS>; --> RESULT=<ADDRESS>;
* eglGetError 获取 错误信息。
    * --> RESULT=12288;
* eglMakeCurrent 绑定 ctx 到当前渲染线程，并且画和读 surfaces。
    * dpy=<ADDRESS>; draw=<ADDRESS>; read=<ADDRESS>; ctx=<ADDRESS>; --> RESULT=1;
* eglCreateContext 创建一个 EGL 渲染上下文。
    * dpy=<ADDRESS>; config=<ADDRESS>; share_context=<ADDRESS>; attrib_list=<ADDRESS>; --> RESULT=<ADDRESS>;
* eglGetDisplay 获取当前的 EGL display。
    * display_id=<ADDRESS>; --> RESULT=<ADDRESS>;
* eglSwapBuffers post egl surface。
    * dpy=<ADDRESS>; surface=<ADDRESS>; --> RESULT=1;
* eglInitialize 初始化。
    * dpy=<ADDRESS>; major=<ADDRESS>; minor=<ADDRESS>; --> RESULT=1;
* eglChooseConfig 根据指定的 attributes，返回合适的 配置列表。
    * dpy=<ADDRESS>; attrib_list=<ADDRESS>; configs=<ADDRESS>; config_size=1; num_config=<ADDRESS>; --> RESULT=1;


## Shader 部分

* glCreateProgram
    * --> RESULT=1;
* glCreateShader
    * type=35633; --> RESULT=2;
* glCompileShader
    * shader=2;
* glAttachShader
    * program=1; shader=2;
* glBindAttribLocation
    * program=1; index=0; name=inVertexPosition;
* glShaderSource
    * shader=2; count=1; string=<ADDRESS>; length=<ADDRESS>;
* glLinkProgram
    * program=1;
* glGetShaderiv return a parameter from a shader object
    * shader=2; pname=35713; params=<ADDRESS>;
* glGetProgramiv return a parameter from a program object
    * program=1; pname=35714; params=<ADDRESS>;
* glGetUniformLocation
    * program=1; name=uWVPMatrix; --> RESULT=0;
* glGetActiveUniform return information about an active uniform variable
    * program=1; index=0; bufSize=25; length=<ADDRESS>; size=<ADDRESS>; type=<ADDRESS>; name=uWVPMatrix;
    * 通过索引号取得 GLSL 中声明的 Uniform 变量的名称、类型、是否是数组等信息。


### OpenGL 的 glGetActiveUniform 和 glGetUniformLocation

OpenGL 的 GLSL 中声明的 Uniform 变量用于应用程序向 GLSL 程序传递参数。
glGetActiveUniform 函数通过索引号取得 GLSL 中声明的 Uniform 变量的名称、类型、是否是数组等信息，
而 glGetUniformLocation 函数则是通过变量名称取得 Location 值，Location 可以视为 GLSL 程序编译后，各个 Uniform 变量在 GPU 内存中的布局的顺序号。

Uniform 变量可以使用单个变量、数组、结构体变量、结构体数组等。令人比较疑惑的是数组元素和结构体成员与 Location 值的关系，因此我通过实验，得出结果如下：

1. GLSL 内置类型的变量，如 int、float、vec2 等等所有类型，如果声明为变量，则取得的名称就是直接是变量名字符串。
    如果声明为数组，则取得的名称是包含数组名和零号元素下标的字符串。
    但如果变量未在 GLSL 代码中使用，则视为不存在，数组无论声明为多少个元素，只会从 0 开始至 GLSL 使用到的最大下标有效。
2. 如果是自定义结构体，则名称是包含结构体和成员名在内的字符串，但结构体成员如果是数组，则无论是否使用到，都会在布局中存在。

```glsl
// 这是 GLSL 的，没有什么实际功能，只是把声明的变量用上，防止编译优化时被忽略掉。
uniform sampler2D qt_Texture0; // 这个采样器没在代码中使用，编译后就不存在了。
varying vec4 qt_TexCoord0;
uniform int _intVar;
uniform int _intArr[5];
uniform float _floatVar;
uniform float _floatArr[6];
uniform vec2 _vec2ver;
uniform vec2 _vec2Arr[7];
uniform ivec2 _ivec2ver;
uniform ivec2 _ivec2Arr[8];
uniform vec3 _vec3Arr[1];
struct StrUct
{
    float fa;
    float fArr[3];
    int   ia;
    int   iArr[4];
    vec2  va;
    vec2  vArr[5];
    mat4  mArr[6];
};
uniform StrUct _sVar;
uniform StrUct _sArr[6];
void main(void)
{
    float a = float(_intVar) + float(_intArr[0]) + float(_intArr[1]) + float(_intArr[2]);
    float b = _floatVar + _floatArr[0] + _floatArr[1] + _floatArr[2] + _vec3Arr[0].x;
    a += _vec2ver.x;
    b += _vec2Arr[6].y;
    int c = _ivec2ver.r + _ivec2Arr[5].r + _ivec2Arr[6].r + _ivec2Arr[7].r;
    float d = float(c) * a * b;
    float e = _sVar.fa + _sVar.fArr[1];
    float f = float(_sVar.ia + _sVar.iArr[1]) * _sArr[1].va.x + _sArr[0].vArr[3].g;
    gl_FragColor.x = float(c);
    gl_FragColor.y = d;
    gl_FragColor.z = e;
    gl_FragColor.a = f;
}
```

```cpp
// 这是一段取得 Uniform 变量数量和最大名称字符串长度之后，枚举每个变量信息的 C++ 代码。
GLintcount = 0;
GLintbufSize = 0;
GLintlength = 0;
std::stringname;
glGetProgramiv(programId, GL_ACTIVE_UNIFORMS, &count);
glGetProgramiv(programId, GL_ACTIVE_UNIFORM_MAX_LENGTH, &bufSize);
if (count && bufSize)
{
    for (int32_t i = 0; i < count; ++i)
    {
        GLenum symbolicConstant;
        name.resize(static_cast<size_t>(bufSize));
        glGetActiveUniform(programId, i, bufSize, &length, &elementCount, &symbolicConstant, &name.front());
        name.resize(static_cast<size_t>(length));
        location = glGetUniformLocation(programId, name.c_str());
        if (location < 0) continue;
        fprintf(stderr, "%d,  Location:%d\tsize:%d,  type:%04X\tname:%s\n", i, location, elementCount, symbolicConstant, name.c_str());
    }
}
```

代码输出的内容：

```
0,  Location:0    size:1,  type:8B5C    name:qt_ModelViewProjectionMatrix
1,  Location:1    size:1,  type:1404    name:_intVar
2,  Location:2    size:3,  type:1404    name:_intArr[0]
3,  Location:5    size:1,  type:1406    name:_floatVar
4,  Location:6    size:3,  type:1406    name:_floatArr[0]
5,  Location:9    size:1,  type:8B50    name:_vec2ver
6,  Location:10    size:7,  type:8B50    name:_vec2Arr[0]
7,  Location:17    size:1,  type:8B53    name:_ivec2ver
8,  Location:18    size:8,  type:8B53    name:_ivec2Arr[0]
9,  Location:26    size:1,  type:8B51    name:_vec3Arr[0]
10,  Location:27    size:1,  type:1406    name:_sVar.fa
11,  Location:28    size:3,  type:1406    name:_sVar.fArr[0]
12,  Location:31    size:1,  type:1404    name:_sVar.ia
13,  Location:32    size:4,  type:1404    name:_sVar.iArr[0]
14,  Location:36    size:1,  type:8B50    name:_sVar.va
15,  Location:37    size:5,  type:8B50    name:_sVar.vArr[0]
16,  Location:42    size:6,  type:8B5C    name:_sVar.mArr[0]
17,  Location:48    size:1,  type:1406    name:_sArr[0].fa
18,  Location:49    size:3,  type:1406    name:_sArr[0].fArr[0]
19,  Location:52    size:1,  type:1404    name:_sArr[0].ia
20,  Location:53    size:4,  type:1404    name:_sArr[0].iArr[0]
21,  Location:57    size:1,  type:8B50    name:_sArr[0].va
22,  Location:58    size:5,  type:8B50    name:_sArr[0].vArr[0]
23,  Location:63    size:6,  type:8B5C    name:_sArr[0].mArr[0]
24,  Location:69    size:1,  type:1406    name:_sArr[1].fa
25,  Location:70    size:3,  type:1406    name:_sArr[1].fArr[0]
26,  Location:73    size:1,  type:1404    name:_sArr[1].ia
27,  Location:74    size:4,  type:1404    name:_sArr[1].iArr[0]
28,  Location:78    size:1,  type:8B50    name:_sArr[1].va
29,  Location:79    size:5,  type:8B50    name:_sArr[1].vArr[0]
30,  Location:84    size:6,  type:8B5C    name:_sArr[1].mArr[0]
```

* 凡是数组，取得的名称中都有 "[0]"，表示是数组的第一个元素。
* 在使用 glGetUniformLocation 去获取 Location 值时，可以包含下标，也可以不包含下标。
* 如 "_intArr" 和 "_intArr[0]" 都返回相同的 Location 值，"_intArr[1]”、"_intArr[2]”分别表示下标为 1 和 2 的元素。
* 注意输出信息中 _intArr 的 size 只有 3，也就是说数组只有 3 个元素，尽管 GLSL 中是声明的 _intArr[5]，但由于在代码中最大只用到了 [2]，
    因此没有使用到的就被 GLSL 编译器优化掉了。
    _vec2Arr 最大用到了 7，尽管没有使用到 0、1、2……等，但明显 GLSL 编译器是认为它们存在的。
* 但是也不应该使用 size 值是否大于 1 来判断是否是数组，比如 _vec3Arr 这个数组，size 就为 1。
* 也不应该假设数组的各个下标对应的 Location 值就是 0 号元素的 Location 值加下标值，因为一些资料上说不同的 GPU 实现可能不一样，
    数组各个下标的 Location 值不一定和下标的顺序一致，那么正确的方式还是要通过完整的 "数组名 [下标]" 来取得对应的 Location 值。
* 对于结构体，又有所不同，名字并不只是结构体的名字，还包含了所有成员的名字。结构体的数组也和普通的数组一样，虽然 _sArr 这个数组声明了 6 个元素，
    但由于在代码中只用到了 0 和 1 号元素，因此有效的就只有 0 和 1。至于结构体中的数组成员，又和普通的数组有一些区别，无论数组成员是否被使用到，
    它都是存在的，并且长度和声明的一致。

----

OpenGL 状态机 和 面向过程的 C 语言接口，令人眼花缭乱。几处早莺争暖树，谁家新燕啄春泥。
为了实现一个功能，需要一组 API 配合食用。整理了一些入门级常用的，加强理解。


## GLFW 窗口管理

```cpp
#include <GLFW/glfw3.h>

glfwInit();
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);

GLFWwindow* window = glfwCreateWindow(WIDTH, HEIGHT, "LearnOpenGL", nullptr, nullptr);
glfwMakeContextCurrent(window);
glfwSetKeyCallback(window, key_callback);

while (!glfwWindowShouldClose(window))
    glfwPollEvents();
    glfwSwapBuffers(window);
glfwTerminate();

// key_callback
glfwSetWindowShouldClose(window, GL_TRUE);
```


## Shader 程序

```cpp
vertex = glCreateShader(GL_VERTEX_SHADER);
glShaderSource(vertex, 1, &vShaderCode, NULL);
glCompileShader(vertex);

fragment = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragment, 1, &fShaderCode, NULL);
glCompileShader(fragment);

geometry = glCreateShader(GL_GEOMETRY_SHADER);
glShaderSource(geometry, 1, &gShaderCode, NULL);
glCompileShader(geometry);

Program = glCreateProgram();
glAttachShader(Program, vertex);
glAttachShader(Program, fragment);
glAttachShader(Program, geometry);
glLinkProgram(Program);

// 连接完成，就可以删除了。
glDeleteShader(vertex);
glDeleteShader(fragment);
glDeleteShader(geometry);
```


## 纹理指定

```cpp
glGenTextures(1, &texture);
glBindTexture(GL_TEXTURE_2D, texture);
    // 当前纹理的相关参数设定
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    int width, height;
    unsigned char* image = SOIL_load_image("..\\resources\\textures\\container.jpg", &width, &height, 0, SOIL_LOAD_RGB);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, image);
    glGenerateMipmap(GL_TEXTURE_2D);
    SOIL_free_image_data(image);
glBindTexture(GL_TEXTURE_2D, 0); // Unbind texture when done, so we won't accidentily mess up our texture.
```


## VBO VAO EBO

```cpp
// Set up vertex data (and buffer(s)) and attribute pointers
GLfloat vertices[] = {
    // Positions        // Texture Coords
     0.5f,  0.5f, 0.0f, 1.0f, 1.0f, // Top Right
     0.5f, -0.5f, 0.0f, 1.0f, 0.0f, // Bottom Right
    -0.5f, -0.5f, 0.0f, 0.0f, 0.0f, // Bottom Left
    -0.5f,  0.5f, 0.0f, 0.0f, 1.0f  // Top Left
};
GLuint indices[] = { // Note that we start from 0!
    0, 1, 3, // First Triangle
    1, 2, 3  // Second Triangle
};

// 这玩意是针对 VBO 的。
void glVertexAttribPointer(
    GLuint          index, // 指定要修改的顶点属性的索引值
    GLint           size,  // 指定每个顶点属性的组件数量。
    GLenum          type,  // 指定数组中每个组件的数据类型。
    GLboolean       normalized, // 指定当被访问时，固定点数据值是否应该被归一化（GL_TRUE）
                                // 或者直接转换为固定点值（GL_FALSE）。
    GLsizei         stride, // 指定连续顶点属性之间的偏移量。
    const GLvoid*   pointer // 指定第一个组件在数组的第一个顶点属性中的偏移量。
);
```

```cpp
GLuint VBO, VAO, EBO;
glGenVertexArrays(1, &VAO);
glGenBuffers(1, &VBO); // array buffer
glGenBuffers(1, &EBO); // element array buffer

glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    // Position attribute
    // layout (location = 0) in vec3 position;
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid*)0);
    glEnableVertexAttribArray(0);
    // TexCoord attribute
    // layout (location = 2) in vec2 texCoord;
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));
    glEnableVertexAttribArray(2);

glBindVertexArray(0); // Unbind VAO

// 绘制 Draw container
glBindVertexArray(VAO);
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
glBindVertexArray(0);

// 释放
// Properly de-allocate all resources once they've outlived their purpose
glDeleteVertexArrays(1, &VAO);
glDeleteBuffers(1, &VBO);
glDeleteBuffers(1, &EBO);
```


## 绘制与 Shader 使用

```cpp
// Define the viewport dimensions
glViewport(0, 0, WIDTH, HEIGHT);
```

```cpp
// Render
// Clear the color buffer
glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
glClear(GL_COLOR_BUFFER_BIT);

// Bind Textures using texture units
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, texture);
glUniform1i(glGetUniformLocation(Program, "ourTexture"), 0);

// Activate shader
glUseProgram(Program);

// Get their uniform location
GLint modelLoc = glGetUniformLocation(Program, "model");
GLint viewLoc = glGetUniformLocation(Program, "view");
GLint projLoc = glGetUniformLocation(Program, "projection");
// Pass them to the shaders
glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm::value_ptr(model));
glUniformMatrix4fv(viewLoc, 1, GL_FALSE, glm::value_ptr(view));
glUniformMatrix4fv(projLoc, 1, GL_FALSE, glm::value_ptr(projection));

// 绘制 !! glDrawElements
```


## 帧缓冲配置与使用

```cpp
// framebuffer configuration
// -------------------------
unsigned int framebuffer;
glGenFramebuffers(1, &framebuffer);
glBindFramebuffer(GL_FRAMEBUFFER, framebuffer);

    // create a color attachment texture
    unsigned int textureColorbuffer;
    glGenTextures(1, &textureColorbuffer);
    glBindTexture(GL_TEXTURE_2D, textureColorbuffer);

    /* 创建 */
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, SCR_WIDTH, SCR_HEIGHT, 0, GL_RGB, GL_UNSIGNED_BYTE, NULL);
        /* 参数 */
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    /* 挂载 */
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureColorbuffer, 0);

    // create a renderbuffer object for depth and stencil attachment (we won't be sampling these)
    unsigned int rbo;
    glGenRenderbuffers(1, &rbo);
    glBindRenderbuffer(GL_RENDERBUFFER, rbo);

    // use a single renderbuffer object for both a depth AND stencil buffer.
    /* 创建 */
    glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, SCR_WIDTH, SCR_HEIGHT);
    // now that we actually created the framebuffer and added all attachments we want to check if it is actually complete now
    /* 挂载 */
    glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, rbo);

    /* 检查 */
    if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
        cout << "ERROR::FRAMEBUFFER:: Framebuffer is not complete!" << endl;
glBindFramebuffer(GL_FRAMEBUFFER, 0);
```

```cpp
glBindFramebuffer(GL_FRAMEBUFFER, framebuffer);
glEnable(GL_DEPTH_TEST); // enable depth testing (is disabled for rendering screen-space quad)

    // 绘制各种东东 -- 绘制到缓冲里面了
    glBindVertexArray(cubeVAO);
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, cubeTexture);
        glDrawArrays(GL_TRIANGLES, 0, 6);
    glBindVertexArray(0);
glBindFramebuffer(GL_FRAMEBUFFER, 0);

// 再次绘制
glBindVertexArray(planeVAO);
    glBindTexture(GL_TEXTURE_2D, floorTexture);
    glDrawArrays(GL_TRIANGLES, 0, 6);
glBindVertexArray(0);

glBindVertexArray(quadVAO);
    // use the color attachment texture as the texture of the quad plane
    glBindTexture(GL_TEXTURE_2D, textureColorbuffer); // 前面创建的纹理缓冲附件
    glDrawArrays(GL_TRIANGLES, 0, 6);
glBindVertexArray(0);
```


## 着色器

```glsl
// 纹理送入
uniform sampler2D screenTexture;
// 最终颜色生成
out vec4 FragColor;
// 纹理取值
FragColor = texture(screenTexture, TexCoords);
// 顶点着色器传参到片段着色器
out vec2 TexCoords;
in vec2 TexCoords;
// CPU 到 GPU 参数传递
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoords;
// 顶点着色器输出
gl_Position = vec4(aPos, 1.0);
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-16-shader-OpenGL-research.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/keneyr/article/details/102727363]({% include relref.html url="/backup/2021-03-16-shader-OpenGL-research.md/blog.csdn.net/c07f06d3.html" %})
