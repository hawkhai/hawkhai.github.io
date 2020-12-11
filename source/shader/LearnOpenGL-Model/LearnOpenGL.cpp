#include <glad\glad.h>
#include "Shader.h"
#include <GLFW/glfw3.h>
#include "stb_image.h"
#include "Camera.h"
#include "Model.h"

//顶点数据
#pragma region

glm::vec3 cubePositions[] = {
    glm::vec3(0.0f,0.0f,0.0f),//cube
    glm::vec3(0.0f, 5.0f, 20.0f),//lamp
    glm::vec3(-3.0f,1.0f,-2.0f),//cube2
};

#pragma endregion

GLFWwindow* init();
void processInput(GLFWwindow* window);
void mouseCallback(GLFWwindow* window, double xpose, double ypose);
void scrollCallback(GLFWwindow* window, double xoffset, double yoffset);
float deltaTime = 0.0f;
float lastFrame = 0.0f;
float currentFrame = glfwGetTime();
Camera camera;

int main()
{
    GLFWwindow* window = init();
    Shader cubeShader("cube.vs", "cube.fs");

    glfwSetScrollCallback(window, scrollCallback);
    glEnable(GL_DEPTH_TEST);

    Model ourModel("E:\\kSource\\LearnOpenGL\\resources\\objects\\nanosuit\\nanosuit.obj");

    while (!glfwWindowShouldClose(window))
    {
        currentFrame = glfwGetTime();
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;

        processInput(window);
        float radius = 10.0f;
        float camX = sin(glfwGetTime()) * radius;
        float camZ = cos(glfwGetTime()) * radius;

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glm::mat4 trans = glm::mat4(1.0f);
        glm::mat4 model;
        model = glm::translate(trans, cubePositions[0]);
        model = glm::rotate(model, (float)glfwGetTime(), glm::vec3(0.0f, 3.0f, 0.0f));
        glm::mat4 view;
        view = camera.GetViewMatrix();
        //view=glm::translate(view,glm::vec3(0.0f,0.0f,-3.0f));
        glm::mat4 projection;
        projection = glm::perspective(glm::radians(camera.mFov), 800.0f / 600.0f, 0.1f, 100.0f);
        //trans=projection*view*model;
        cubeShader.useShader();
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "projection"), 1, GL_FALSE, glm::value_ptr(projection));
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "view"), 1, GL_FALSE, glm::value_ptr(view));
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "model"), 1, GL_FALSE, glm::value_ptr(model));
        glUniform4f(glGetUniformLocation(cubeShader.ID, "lightPos"), cubePositions[1].r, cubePositions[1].g, cubePositions[1].b, 1);
        glUniform3f(glGetUniformLocation(cubeShader.ID, "viewPos"), camera.mPosition.r, camera.mPosition.g, camera.mPosition.b);
        glUniform3f(glGetUniformLocation(cubeShader.ID, "front"), camera.mFront.r, camera.mFront.g, camera.mFront.b);

        glUniform3f(glGetUniformLocation(cubeShader.ID, "lightColor"), 1.0f, 1.0f, 1.0f);

        ourModel.Draw(cubeShader);
        glfwPollEvents();
        glfwSwapBuffers(window);
    }
    //退出
    glfwTerminate();
    return 0;
}

GLFWwindow* init()
{
    //初始化
    GLFWwindow* window;
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    window = glfwCreateWindow(600, 450, "OpenGL Model", NULL, NULL);
    if (window == NULL)
    {
        printf("err:windows is NULL");
        glfwTerminate();
    }

    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        printf("err:gladLoadGLLoader is NULL");
    }
    return window;
}

void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);

    if (glfwGetKey(window, GLFW_KEY_Q) == GLFW_PRESS)
    {
        glfwSetCursorPosCallback(window, mouseCallback);
        glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
    }

    float cameraSpeed = 2.5f * deltaTime;
    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        camera.mPosition += cameraSpeed * camera.mFront;
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.mPosition -= cameraSpeed * camera.mFront;;
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.mPosition -= glm::normalize(glm::cross(camera.mFront, camera.mUp)) * cameraSpeed;
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.mPosition += glm::normalize(glm::cross(camera.mFront, camera.mUp)) * cameraSpeed;
}

void mouseCallback(GLFWwindow* window, double xpose, double ypose)
{
    static float yaw = -90.0f, pitch = 0.0f, lastX = 800.0f / 2, lastY = 600.0f / 2, xoffset, yoffset;
    xoffset = xpose - lastX;
    yoffset = lastY - ypose;
    lastX = xpose;
    lastY = ypose;
    camera.ProcessMouseMovement(xoffset, yoffset);
}

void scrollCallback(GLFWwindow* window, double xoffset, double yoffset)
{
    camera.ProcessMouseScroll(yoffset);
}
