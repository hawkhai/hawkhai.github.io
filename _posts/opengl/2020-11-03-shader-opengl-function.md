---
layout: post
title: "图形学笔记 -- OpenGL Shader 函数 Waveform 波形"
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

偶然看到这篇文章。
[Unity Shader：Waveform 波形 (2) - 基本波形：正弦，三角，锯齿，直角以及其变种的实现方式 {% include relref_csdn.html %}](https://blog.csdn.net/liu_if_else/article/details/77712935)
非常生动，自己也用纯 OpenGL 实现了一个。

画离散点，然后在几何着色器里面连接成面条。


## Gallary

{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-sin.webp" caption="sin $y = (sin(x) + 1.0) / 2.0$" %}
{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-square.webp" caption="Square $y = (round(sin(x)) + 1.0) / 2.0$" %}
{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-sawtooth.webp" caption="SawTooth $y = clamp(mod(x / 5.0, 1.0f), 0.0, 1.0)$" %}
{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-inverse-sawtooth.webp" caption="Inverse SawTooth $y = 1.0f - clamp(mod(x / 5.0, 1.0f), 0.0, 1.0)$" %}
{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-hill.webp" caption="hill $y = abs(sin(x))$" %}
{% include image.html url="/assets/images/201103-shader-opengl-function/learngl-inverse-hill.webp" caption="inverse hill $y = 1.0f - abs(sin(x))$" %}


## Code

```cpp
#include "stdafx.h"
#include <math.h>
#include "LearnGL.h"
#include "glad/glad.h"
#include "GLFW/glfw3.h"

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/string_cast.hpp>

#include "camera.h"
#include <iostream>
#include <sstream>

#pragma comment(lib, "glfw3.lib")

#define INFO_LOG_SIZE 512
#define SNAP_SHOT     TRUE

// settings
const unsigned int SCR_WIDTH = 720;
const unsigned int SCR_HEIGHT = 370;

#define GLSL(src) "#version 150 core\n" #src

namespace geometry {

    int g_vertexShaderId = 0;
    int g_geometryShaderId = 0;
    int g_fragShaderId = 0;
    int g_shaderProgId = 0;

    unsigned int VAO = 0;
    unsigned int VBO = 0;

    float* points = nullptr;
    int pointsize = 0;

    GLint success = 0;
    GLchar infoLog[INFO_LOG_SIZE] = { 0 };
    // camera
    Camera camera(glm::vec3(2.0f, 1.0f, 2.0f));

    float lastX = SCR_WIDTH / 2.0f;
    float lastY = SCR_HEIGHT / 2.0f;
    bool firstMouse = true;

    // timing
    float deltaTime = 0.0f; // time between current frame and last frame
    float lastFrame = 0.0f;

    // 顶点着色器
    void createVertexShader() {

        const char* vertexShaderSource = GLSL(

            in vec3 pos;
        in float ktype;
        in float kstep;
        in float kparam;

        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        out float vtype;
        out float vstep;
        out float vparam;

        void main() {
            gl_Position = vec4(pos, 1.0);
            vtype = ktype;
            vstep = kstep;
            vparam = kparam;
        }
        );

        g_vertexShaderId = glCreateShader(GL_VERTEX_SHADER);
        glShaderSource(g_vertexShaderId, 1, &vertexShaderSource, NULL);
        glCompileShader(g_vertexShaderId);

        glGetShaderiv(g_vertexShaderId, GL_COMPILE_STATUS, &success);
        if (!success)
        {
            glGetShaderInfoLog(g_vertexShaderId, INFO_LOG_SIZE, NULL, infoLog);
        }
    }

    void createGeometryShader() {
        const char* geometryShaderSource = GLSL(

            layout(points) in;
        layout(triangle_strip, max_vertices = 32) out;

        in float vtype[];
        in float vstep[];
        in float vparam[];

        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        out vec3 fColor; // Output to fragment shader

        void emitVertex(in vec4 offset) {
            vec4 temp = gl_in[0].gl_Position + offset;
            gl_Position = projection * view * model * temp;
            EmitVertex();
        }

        /**
         * 1 2
         * 3 4
         */
        void drawPlane(in vec4 p1, in vec4 p2, in vec4 p3, in vec4 p4, in float color, in float colorNext) {
            fColor = vec3(colorNext);
            emitVertex(p1);
            emitVertex(p2);
            fColor = vec3(color);
            emitVertex(p4);
            emitVertex(p3);
            fColor = vec3(colorNext);
            emitVertex(p1);
        }

        void calc(in float x, out float y) {

            // perfect sin
            y = (sin(x) + 1.0) / 2.0;
            // hill
            //y = abs(sin(x));
            // inverse hill
            //y = 1.0f - abs(sin(x));
            // SawTooth
            //y = clamp(mod(x / 5.0, 1.0f), 0.0, 1.0);
            // Inverse SawTooth
            //y = 1.0f - clamp(mod(x / 5.0, 1.0f), 0.0, 1.0);
            // Square
            y = (round(sin(x)) + 1.0) / 2.0;
        }

        void main() {

            float color;
            calc(vparam[0] * 2, color);

            float colorNext = 0;
            calc((vparam[0] - vstep[0] * 10) * 2, colorNext);

            /**
             * 1 2
             * 3 4
             */
            vec4 p1 = vec4(-0.02, 0.0, -vstep[0], 0.0);
            vec4 p2 = vec4(+0.02, 0.0, -vstep[0], 0.0);
            vec4 p3 = vec4(-0.02, 0.0, 0.0, 0.0);
            vec4 p4 = vec4(+0.02, 0.0, 0.0, 0.0);

            if (vtype[0] <= 1.0) { // White wave
                float tmph;
                float scale = 7;
                calc(vparam[0] * 2, tmph);
                p3.y = tmph / scale;
                p4.y = tmph / scale;
                calc((vparam[0] - vstep[0] * 10) * 2, tmph);
                calc((vparam[0] - vstep[0] * 10) * 2, tmph);
                p1.y = tmph / scale;
                p2.y = tmph / scale;
                color = 1.0;
                drawPlane(p1, p2, p3, p4, color, color);

            }
            else {
                drawPlane(p1, p2, p3, p4, color, colorNext);
            }

            EndPrimitive();
        }
        );
        g_geometryShaderId = glCreateShader(GL_GEOMETRY_SHADER);
        glShaderSource(g_geometryShaderId, 1, &geometryShaderSource, NULL);
        glCompileShader(g_geometryShaderId);

        glGetShaderiv(g_geometryShaderId, GL_COMPILE_STATUS, &success);
        if (!success)
        {
            glGetShaderInfoLog(g_geometryShaderId, INFO_LOG_SIZE, NULL, infoLog);
        }
    }

    // 片段着色器
    void createFragShader() {
        // 将着色器源码存入字符串
        const char* fragmentShaderSource = GLSL(

            out vec4 outColor;

        in vec3 fColor;

        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        void main() {
            outColor = vec4(fColor, 1.0);
        }
        );

        g_fragShaderId = glCreateShader(GL_FRAGMENT_SHADER);
        glShaderSource(g_fragShaderId, 1, &fragmentShaderSource, NULL);
        glCompileShader(g_fragShaderId);

        glGetShaderiv(g_fragShaderId, GL_COMPILE_STATUS, &success);
        if (!success)
        {
            glGetShaderInfoLog(g_fragShaderId, INFO_LOG_SIZE, NULL, infoLog);
        }
    }

#define TSIZE 1000
#define SECSIZE 6

    void setVertexEnv() {

        glGenVertexArrays(1, &VAO);
        glBindVertexArray(VAO);

        points = new float[TSIZE * SECSIZE];

        glGenBuffers(1, &VBO);
        glBindBuffer(GL_ARRAY_BUFFER, VBO);
    }

    void releaseShader() {
        glDeleteVertexArrays(1, &VAO);
        glDeleteBuffers(1, &VBO);

        glDeleteProgram(g_shaderProgId);
        glDeleteShader(g_vertexShaderId);
        glDeleteShader(g_geometryShaderId);
        glDeleteShader(g_fragShaderId);

        delete[] points;
        points = nullptr;
    }

    void createShaderProg() {
        // 创建着色器程序对象
        g_shaderProgId = glCreateProgram();
        // 将编译好的着色器附加到程序对象上
        glAttachShader(g_shaderProgId, g_vertexShaderId);
        glAttachShader(g_shaderProgId, g_geometryShaderId);
        glAttachShader(g_shaderProgId, g_fragShaderId);
        // 链接生成程序
        glLinkProgram(g_shaderProgId);

        glGetProgramiv(g_shaderProgId, GL_LINK_STATUS, &success);
        if (!success)
        {
            glGetProgramInfoLog(g_shaderProgId, INFO_LOG_SIZE, NULL, infoLog);
        }

        /**
        in vec3 pos;
        in float ktype;
        in float kstep;
        in float kparam;
        */
        // Specify layout of point data
        GLint attrib = 0;

        attrib = glGetAttribLocation(g_shaderProgId, "pos");
        glEnableVertexAttribArray(attrib);
        glVertexAttribPointer(attrib, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), 0);

        attrib = glGetAttribLocation(g_shaderProgId, "ktype");
        glEnableVertexAttribArray(attrib);
        glVertexAttribPointer(attrib, 1, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));

        attrib = glGetAttribLocation(g_shaderProgId, "kstep");
        glEnableVertexAttribArray(attrib);
        glVertexAttribPointer(attrib, 1, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(4 * sizeof(float)));

        attrib = glGetAttribLocation(g_shaderProgId, "kparam");
        glEnableVertexAttribArray(attrib);
        glVertexAttribPointer(attrib, 1, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(5 * sizeof(float)));
    }

    void setMat4(const char* name, const glm::mat4& mat)
    {
        glUniformMatrix4fv(glGetUniformLocation(g_shaderProgId, name), 1, GL_FALSE, &mat[0][0]);
    }

    void drawContent() {

        glUseProgram(g_shaderProgId); // 使用程序

        glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 10.0f);
        if (SNAP_SHOT) {
            projection[0] = glm::vec4(1.240637, 0.000000, 0.000000, 0.000000);
            projection[1] = glm::vec4(0.000000, 2.414213, 0.000000, 0.000000);
            projection[2] = glm::vec4(0.000000, 0.000000, -1.020202, -1.000000);
            projection[3] = glm::vec4(0.000000, 0.000000, -0.202020, 0.000000);
        }
        setMat4("projection", projection);

        glm::mat4 view = camera.GetViewMatrix();
        if (SNAP_SHOT) {
            view[0] = glm::vec4(0.886206, -0.246878, 0.392034, 0.000000);
            view[1] = glm::vec4(-0.000000, 0.846193, 0.532877, 0.000000);
            view[2] = glm::vec4(-0.463292, -0.472239, 0.749901, 0.000000);
            view[3] = glm::vec4(0.671812, 0.702021, -1.839670, 1.000000);
        }
        setMat4("view", view);

        glm::mat4 model = glm::mat4(1.0f);
        setMat4("model", model);

        std::ostringstream streamz;
        streamz << "projection" << glm::to_string(projection).c_str() << "view"
            << glm::to_string(view).c_str() << std::endl;
        OutputDebugStringA(streamz.str().c_str());

        float ktime = -glfwGetTime();
        float kstep = 0.01;
        for (int i = 0; i < TSIZE; i++)
        {
            points[i * SECSIZE + 0] = 0.25;
            points[i * SECSIZE + 1] = 0;
            points[i * SECSIZE + 2] = 2.0 - kstep * i;
            points[i * SECSIZE + 3] = 2; // ktype
            points[i * SECSIZE + 4] = kstep; // kstep
            points[i * SECSIZE + 5] = -(kstep)*i * 10 + ktime; // kparam
        }

        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glBufferData(GL_ARRAY_BUFFER, TSIZE * SECSIZE, points, GL_STATIC_DRAW);
        glDrawArrays(GL_POINTS, 0, TSIZE);

        for (int i = 0; i < TSIZE; i++)
        {
            points[i * SECSIZE + 0] = -0.25;
            points[i * SECSIZE + 1] = 0;
            points[i * SECSIZE + 2] = 2.0 - kstep * i;
            points[i * SECSIZE + 3] = 0; // ktype
            points[i * SECSIZE + 4] = kstep; // kstep
            points[i * SECSIZE + 5] = -(kstep)*i * 10 + ktime; // kparam
        }

        glBufferData(GL_ARRAY_BUFFER, TSIZE * SECSIZE, points, GL_STATIC_DRAW);
        glDrawArrays(GL_POINTS, 0, TSIZE);
    }

    void processInput(GLFWwindow* window)
    {
        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
            glfwSetWindowShouldClose(window, true);

        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)
            camera.ProcessKeyboard(FORWARD, deltaTime);
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS)
            camera.ProcessKeyboard(BACKWARD, deltaTime);
        if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS)
            camera.ProcessKeyboard(LEFT, deltaTime);
        if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS)
            camera.ProcessKeyboard(RIGHT, deltaTime);
    }

    void framebuffer_size_callback(GLFWwindow* window, int width, int height)
    {
        glViewport(0, 0, width, height);
    }

    void mouse_callback(GLFWwindow* window, double xpos, double ypos)
    {
        if (firstMouse)
        {
            lastX = xpos;
            lastY = ypos;
            firstMouse = false;
        }

        float xoffset = xpos - lastX;
        float yoffset = lastY - ypos; // reversed since y-coordinates go from bottom to top

        lastX = xpos;
        lastY = ypos;

        camera.ProcessMouseMovement(xoffset, yoffset);
    }

    void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
    {
        camera.ProcessMouseScroll(yoffset);
    }
}

int geometryShader() {

    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);

    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "OpenGL", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        glfwTerminate();
        return -1;
    }

    glfwSetFramebufferSizeCallback(window, geometry::framebuffer_size_callback);
    glfwSetCursorPosCallback(window, geometry::mouse_callback);
    glfwSetScrollCallback(window, geometry::scroll_callback);
    // tell GLFW to capture our mouse
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

    geometry::setVertexEnv();
    geometry::createVertexShader();
    geometry::createGeometryShader();
    geometry::createFragShader();
    geometry::createShaderProg();

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    glEnable(GL_DEPTH_TEST);

    // 渲染引擎
    while (!glfwWindowShouldClose(window)) {

        float currentFrame = glfwGetTime();
        geometry::deltaTime = currentFrame - geometry::lastFrame;
        geometry::lastFrame = currentFrame;

        geometry::processInput(window);

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        geometry::drawContent();

        glfwPollEvents();
        glfwSwapBuffers(window);
    }

    geometry::releaseShader();
    // 退出
    glfwTerminate();
    return 0;
}
```


## Refs

- [1] [Unity Shader：Waveform 波形 (1) - 用正弦函数做闪烁效果并分析波形公式中的参数 {% include relref_csdn.html %}](https://blog.csdn.net/liu_if_else/article/details/77144264)
- [2] [Unity Shader：Waveform 波形 (2) - 基本波形：正弦，三角，锯齿，直角以及其变种的实现方式 {% include relref_csdn.html %}](https://blog.csdn.net/liu_if_else/article/details/77712935)
- [3] [Unity Shader：Waveform 波形 (3) - 复合波 {% include relref_csdn.html %}](https://blog.csdn.net/liu_if_else/article/details/78086749)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-03-shader-opengl-function.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/liu_if_else/article/details/77712935]({% include relrefx.html url="/backup/2020-11-03-shader-opengl-function.md/blog.csdn.net/e82c31b3.html" %})
- [https://blog.csdn.net/liu_if_else/article/details/77144264]({% include relrefx.html url="/backup/2020-11-03-shader-opengl-function.md/blog.csdn.net/bb01545a.html" %})
- [https://blog.csdn.net/liu_if_else/article/details/78086749]({% include relrefx.html url="/backup/2020-11-03-shader-opengl-function.md/blog.csdn.net/061f0782.html" %})
