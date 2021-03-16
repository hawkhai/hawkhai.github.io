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
