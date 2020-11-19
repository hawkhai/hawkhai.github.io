#include "stdafx.h"
#include <math.h>
#include "LearnGL.h"
#include "glad/glad.h"
#include "GLFW/glfw3.h"

#pragma comment(lib, "glfw3.lib") 

#define GLSL(src) "#version 400 core\n" #src "\n\0"

int g_vertexShaderId = 0;
int g_fragShaderId = 0;
int g_shaderProgId = 0;

void setVertexEnv();
void createVertexShader();
void createFragShader();
void createShaderProg();
void drawContent();

int learnOpenGL() {

    // 初始化
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);

    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(400, 300, "OpenGL", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        glfwTerminate();
        return -1;
    }

    setVertexEnv();
    createVertexShader();
    createFragShader();
    createShaderProg();

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); // GL_LINE

    // 渲染引擎
    while (!glfwWindowShouldClose(window)) {

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        drawContent();

        glfwPollEvents();
        glfwSwapBuffers(window);
    }

    // 退出
    glfwTerminate();
    return 0;
}

// 顶点着色器
void createVertexShader() {

    const char* vertexShaderSource = GLSL(
        layout(location = 0) in vec3 aPos;
    layout(location = 1) in vec3 aColor;
    out vec4 ourColor;
    void main() {
        ourColor = vec4(aColor, 1.0f);
        gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0f);
    }
    );

    g_vertexShaderId = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(g_vertexShaderId, 1, &vertexShaderSource, NULL);
    glCompileShader(g_vertexShaderId);
}

// 片段着色器
void createFragShader() {
    // 将着色器源码存入字符串
    const char* fragShaderSource = GLSL(
        out vec4 FragColor;
    in vec4 vertexsColor;
    in vec4 ourColor;
    void main() {
        FragColor = ourColor; // vertexsColor
    }
    );

    // 创建着色器对象
    g_fragShaderId = glCreateShader(GL_FRAGMENT_SHADER);
    // 将源码字符串赋予着色器对象
    glShaderSource(g_fragShaderId, 1, &fragShaderSource, NULL);
    // 编译着色器
    glCompileShader(g_fragShaderId);
}

void setVertexEnv() {
    float vertices[] = {
        -0.5f, -0.5f, 0.0f, 1, 0, 0, // left, down
        0.5f, -0.5f, 0.0f, 0, 1, 0, // right, down
        -0.5f, 0.5f, 0.0f, 0, 0, 1, // left, top
        0.5f, 0.5f, 0.0f, 0, 1, 1, // right, top
    };
    unsigned int indices[] = {
        0, 1, 2,
        1, 2, 3,
    };

    unsigned int VAO; // VAO: vertex array object
    unsigned int VBO; // VBO: vertex buffer object
    unsigned int EBO;

    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    // 绑定当前上下文
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);

    // 往显卡写值，分配显存空间。
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    // 告诉显卡，值的结构。
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);
}

void createShaderProg() {
    // 创建着色器程序对象
    g_shaderProgId = glCreateProgram();
    // 将编译好的着色器附加到程序对象上
    glAttachShader(g_shaderProgId, g_vertexShaderId);
    glAttachShader(g_shaderProgId, g_fragShaderId);
    // 链接生成程序
    glLinkProgram(g_shaderProgId);
}

void drawContent() {

    glUseProgram(g_shaderProgId); // 使用程序

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
    //glDrawArrays(GL_TRIANGLES, 0, 6); // 画三角
}
