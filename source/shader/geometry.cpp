#include "stdafx.h"
#include <math.h>
#include "LearnOpenGL.h"
#include "glad/glad.h"
#include "GLFW/glfw3.h"

#pragma comment(lib, "glfw3.lib") 

#define GLSL(src) "#version 150 core\n" #src

// https://blog.csdn.net/iron_lzn/article/details/48729849
namespace geometry {

    int g_vertexShaderId = 0;
    int g_geometryShaderId = 0;
    int g_fragShaderId = 0;
    int g_shaderProgId = 0;

    // 顶点着色器
    void createVertexShader() {

        const char* vertexShaderSource = GLSL(
            in vec2 pos;
            in vec3 color;
            in float sides;

            out vec3 vColor; // Output to geometry (or fragment) shader
            out float vSides;

            void main() {
                gl_Position = vec4(pos, 0.0, 1.0);
                vColor = color;
                vSides = sides;
            }
        );

        g_vertexShaderId = glCreateShader(GL_VERTEX_SHADER);
        glShaderSource(g_vertexShaderId, 1, &vertexShaderSource, NULL);
        glCompileShader(g_vertexShaderId);
    }

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

    // 片段着色器
    void createFragShader() {
        // 将着色器源码存入字符串
        const char* fragmentShaderSource = GLSL(
            out vec4 outColor;
            in vec3 fColor;

            void main() {
                outColor = vec4(fColor, 1.0);
            }
        );
        // 创建着色器对象
        g_fragShaderId = glCreateShader(GL_FRAGMENT_SHADER);
        // 将源码字符串赋予着色器对象
        glShaderSource(g_fragShaderId, 1, &fragmentShaderSource, NULL);
        // 编译着色器
        glCompileShader(g_fragShaderId);
    }

    void setVertexEnv() {

        // VBO: vertex buffer object
        unsigned int VBO;
        float points[] = {
            //  Color Coordinates Sides
            -0.45f,  0.45f, 1.0f, 0.0f, 0.0f,  4.0f,
             0.45f,  0.45f, 0.0f, 1.0f, 0.0f,  8.0f,
             0.45f, -0.45f, 0.0f, 0.0f, 1.0f, 16.0f,
            -0.45f, -0.45f, 1.0f, 1.0f, 0.0f, 32.0f
        };
        glGenBuffers(1, &VBO);
        glBindBuffer(GL_ARRAY_BUFFER, VBO);
        glBufferData(GL_ARRAY_BUFFER, sizeof(points), points, GL_STATIC_DRAW);

        // VAO: vertex array object
        unsigned int VAO;
        glGenVertexArrays(1, &VAO);
        glBindVertexArray(VAO);
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


        // Specify layout of point data
        GLint posAttrib = glGetAttribLocation(g_shaderProgId, "pos");
        glEnableVertexAttribArray(posAttrib);
        glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE, 6 * sizeof(float), 0);

        GLint colAttrib = glGetAttribLocation(g_shaderProgId, "color");
        glEnableVertexAttribArray(colAttrib);
        glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(2 * sizeof(float)));

        GLint sidesAttrib = glGetAttribLocation(g_shaderProgId, "sides");
        glEnableVertexAttribArray(sidesAttrib);
        glVertexAttribPointer(sidesAttrib, 1, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(5 * sizeof(float)));
    }

    void drawContent() {

        glUseProgram(g_shaderProgId); // 使用程序

        glDrawArrays(GL_POINTS, 0, 4);
    }
}

int geometryShader() {

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

    geometry::setVertexEnv();
    geometry::createVertexShader();
    geometry::createGeometryShader();
    geometry::createFragShader();
    geometry::createShaderProg();

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE); // GL_FILL

    // 渲染引擎
    while (!glfwWindowShouldClose(window)) {

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        geometry::drawContent();

        glfwPollEvents();
        glfwSwapBuffers(window);
    }

    // 退出
    glfwTerminate();
    return 0;
}