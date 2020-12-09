#include <glad\glad.h>
#include "Shader.h"
#include <GLFW/glfw3.h>
#include "stb_image.h"
#include "Camera.h"

//顶点数据
#pragma region
float vertices[] = {
    // positions          // normals           // texture coords
    -0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  0.0f,  0.0f,
     0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  1.0f,  0.0f,
     0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  1.0f,  1.0f,
     0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  1.0f,  1.0f,
    -0.5f,  0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  0.0f,  1.0f,
    -0.5f, -0.5f, -0.5f,  0.0f,  0.0f, -1.0f,  0.0f,  0.0f,

    -0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  0.0f,  0.0f,
     0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  1.0f,  0.0f,
     0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  1.0f,  1.0f,
     0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  1.0f,  1.0f,
    -0.5f,  0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  0.0f,  1.0f,
    -0.5f, -0.5f,  0.5f,  0.0f,  0.0f,  1.0f,  0.0f,  0.0f,

    -0.5f,  0.5f,  0.5f, -1.0f,  0.0f,  0.0f,  1.0f,  0.0f,
    -0.5f,  0.5f, -0.5f, -1.0f,  0.0f,  0.0f,  1.0f,  1.0f,
    -0.5f, -0.5f, -0.5f, -1.0f,  0.0f,  0.0f,  0.0f,  1.0f,
    -0.5f, -0.5f, -0.5f, -1.0f,  0.0f,  0.0f,  0.0f,  1.0f,
    -0.5f, -0.5f,  0.5f, -1.0f,  0.0f,  0.0f,  0.0f,  0.0f,
    -0.5f,  0.5f,  0.5f, -1.0f,  0.0f,  0.0f,  1.0f,  0.0f,

     0.5f,  0.5f,  0.5f,  1.0f,  0.0f,  0.0f,  1.0f,  0.0f,
     0.5f,  0.5f, -0.5f,  1.0f,  0.0f,  0.0f,  1.0f,  1.0f,
     0.5f, -0.5f, -0.5f,  1.0f,  0.0f,  0.0f,  0.0f,  1.0f,
     0.5f, -0.5f, -0.5f,  1.0f,  0.0f,  0.0f,  0.0f,  1.0f,
     0.5f, -0.5f,  0.5f,  1.0f,  0.0f,  0.0f,  0.0f,  0.0f,
     0.5f,  0.5f,  0.5f,  1.0f,  0.0f,  0.0f,  1.0f,  0.0f,

    -0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,  0.0f,  1.0f,
     0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,  1.0f,  1.0f,
     0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,  1.0f,  0.0f,
     0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,  1.0f,  0.0f,
    -0.5f, -0.5f,  0.5f,  0.0f, -1.0f,  0.0f,  0.0f,  0.0f,
    -0.5f, -0.5f, -0.5f,  0.0f, -1.0f,  0.0f,  0.0f,  1.0f,

    -0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f,  0.0f,  1.0f,
     0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f,  1.0f,  1.0f,
     0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,  1.0f,  0.0f,
     0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,  1.0f,  0.0f,
    -0.5f,  0.5f,  0.5f,  0.0f,  1.0f,  0.0f,  0.0f,  0.0f,
    -0.5f,  0.5f, -0.5f,  0.0f,  1.0f,  0.0f,  0.0f,  1.0f
};
glm::vec3 cubePositions[] = {
    glm::vec3(0.0f,0.0f,0.0f),//cube
    glm::vec3(2.0f, 0.0f, 2.0f),//lamp
    glm::vec3(-3.0f,1.0f,-2.0f),//cube2
};
//float vertices[]={
//    -0.5f,-0.5f,0.0f,0,0,//left,down
//     0.5f,-0.5f,0.0f,1,0,//right,down
//     0.5f, 0.5f,0.0f,1,1,//right,top
//    -0.5f, 0.5f,0.0f,0,1//left,top
//};
unsigned int indices[] = {
    0,1,3,
    1,2,3
};
#pragma endregion

GLFWwindow* init();
void VAOSet();
void loadTexture(Shader* myShader);
void processInput(GLFWwindow* window);
void mouseCallback(GLFWwindow* window, double xpose, double ypose);
void scrollCallback(GLFWwindow* window, double xoffset, double yoffset);

float deltaTime = 0.0f;
float lastFrame = 0.0f;
float currentFrame = glfwGetTime();
Camera camera;
unsigned int lightVAO;
unsigned int VBO, cubeVAO, EBO;//ID
int main()
{
    GLFWwindow* window = init();

    VAOSet();
    Shader lightShader("lamp.vs", "lamp.fs");
    Shader cubeShader("cube.vs", "cube.fs");
    loadTexture(&cubeShader);
    //glPolygonMode(GL_FRONT_AND_BACK,/*GL_FILL*/GL_LINE);
    //渲染引擎
    //glfwSetCursorPosCallback(window,mouseCallback);
    //glfwSetInputMode(window,GLFW_CURSOR,GLFW_CURSOR_DISABLED);

    glfwSetScrollCallback(window, scrollCallback);
    glEnable(GL_DEPTH_TEST);
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
        model = glm::rotate(model, (float)glfwGetTime(), glm::vec3(1.5f, 3.0f, 0.0f));
        glm::mat4 view;
        view = camera.GetViewMatrix();
        //view=glm::translate(view,glm::vec3(0.0f,0.0f,-3.0f));
        glm::mat4 projection;
        projection = glm::perspective(glm::radians(camera.m_fZoom), 800.0f / 600.0f, 0.1f, 100.0f);
        //trans=projection*view*model;
        cubeShader.useShader();
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "projection"), 1, GL_FALSE, glm::value_ptr(projection));
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "view"), 1, GL_FALSE, glm::value_ptr(view));
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "model"), 1, GL_FALSE, glm::value_ptr(model));
        glUniform4f(glGetUniformLocation(cubeShader.ID, "lightPos"), cubePositions[1].r, cubePositions[1].g, cubePositions[1].b, 1);
        glUniform3f(glGetUniformLocation(cubeShader.ID, "viewPos"), camera.m_vecPosition.r, camera.m_vecPosition.g, camera.m_vecPosition.b);
        glUniform3f(glGetUniformLocation(cubeShader.ID, "front"), camera.m_vecFront.r, camera.m_vecFront.g, camera.m_vecFront.b);
        glUniform3f(glGetUniformLocation(cubeShader.ID, "objectColor"), 1.0f, 0.5f, 0.31f);

        glUniform3f(glGetUniformLocation(cubeShader.ID, "lightColor"), 1.0f, 1.0f, 1.0f);
        glBindVertexArray(cubeVAO);
        glDrawArrays(GL_TRIANGLES, 0, 36);//画三角
        model = glm::translate(trans, cubePositions[2]);
        glUniformMatrix4fv(glGetUniformLocation(cubeShader.ID, "model"), 1, GL_FALSE, glm::value_ptr(model));
        glDrawArrays(GL_TRIANGLES, 0, 36);//画三角
    //glDrawElements(GL_TRIANGLES,6,GL_UNSIGNED_INT,0);
    /*}*/

        trans = glm::mat4(1.0f);
        model = glm::translate(trans, cubePositions[1]);
        model = glm::scale(model, glm::vec3(0.2f, 0.2f, 0.2f));
        trans = projection * view * model;
        lightShader.useShader();
        glUniformMatrix4fv(glGetUniformLocation(lightShader.ID, "transform"), 1, GL_FALSE, glm::value_ptr(trans));
        glUniform3f(glGetUniformLocation(lightShader.ID, "lightColor"), 1.0f, 1.0f, 1.0f);
        glBindVertexArray(lightVAO);
        glDrawArrays(GL_TRIANGLES, 0, 36);//画三角

        glfwPollEvents();
        glfwSwapBuffers(window);
    }
    //退出
    glfwTerminate();
    return 0;
}

void VAOSet()
{

    glGenVertexArrays(1, &cubeVAO);
    glGenBuffers(1, &VBO);
    //glGenBuffers(1,&EBO);

    glBindVertexArray(cubeVAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    //glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,EBO);

    //往显卡写值，分配显存空间GL_STATIC_DRAW表示，值不修改
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    //glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(indices),indices,GL_STATIC_DRAW);
    //告诉显卡，值的结构 position
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);
    //告诉显卡，值的结构 法线
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);
    //告诉显卡，值的结构 纹理坐标
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6 * sizeof(float)));
    glEnableVertexAttribArray(2);

    glGenVertexArrays(1, &lightVAO);
    glBindVertexArray(lightVAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

}

GLFWwindow* init()
{
    //初始化
    GLFWwindow* window;
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    window = glfwCreateWindow(600, 450, "LearnOpenGL Lighting", NULL, NULL);
    if (window == NULL)
    {
        printf("err:windows is NULL");
        glfwTerminate();
        return NULL;
    }

    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        printf("err:gladLoadGLLoader is NULL");
    }
    return window;
}

void loadTexture(Shader* myShader)
{
    int width, height, nrChannels;
    unsigned char* data;
    stbi_set_flip_vertically_on_load(true);

    unsigned int texture[2];
    glGenTextures(2, texture);
    //加载第一个纹理
    glBindTexture(GL_TEXTURE_2D, texture[0]);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    data = stbi_load("container2.png", &width, &height, &nrChannels, 0);
    GLenum format = GL_RGB;
    if (nrChannels == 1)
        format = GL_RED;
    else if (nrChannels == 3)
        format = GL_RGB;
    else if (nrChannels == 4)
        format = GL_RGBA;
    glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, data);
    glGenerateMipmap(GL_TEXTURE_2D);
    stbi_image_free(data);
    //加载第二个纹理
    glBindTexture(GL_TEXTURE_2D, texture[1]);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    data = stbi_load("container2_specular.png", &width, &height, &nrChannels, 0);
    glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, data);
    glGenerateMipmap(GL_TEXTURE_2D);
    stbi_image_free(data);

    myShader->useShader();
    glUniform1i(glGetUniformLocation(myShader->ID, "ourTexture1"), 0);//默认状态，可以省略
    glUniform1i(glGetUniformLocation(myShader->ID, "ourTexture2"), 1);

    glActiveTexture(GL_TEXTURE0);//先激活再绑定，纹理单元0,默认状态，可以省略
    glBindTexture(GL_TEXTURE_2D, texture[0]);
    glActiveTexture(GL_TEXTURE1);//先激活再绑定，纹理单元1
    glBindTexture(GL_TEXTURE_2D, texture[1]);
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
        camera.m_vecPosition += cameraSpeed * camera.m_vecFront;
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.m_vecPosition -= cameraSpeed * camera.m_vecFront;;
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.m_vecPosition -= glm::normalize(glm::cross(camera.m_vecFront, camera.m_vecUp)) * cameraSpeed;
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.m_vecPosition += glm::normalize(glm::cross(camera.m_vecFront, camera.m_vecUp)) * cameraSpeed;
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