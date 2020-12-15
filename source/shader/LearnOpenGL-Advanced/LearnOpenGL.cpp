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
void mouse_callback(GLFWwindow* window, double xpose, double ypose);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);
void mouse_button_callback(GLFWwindow * window, int button, int action, int mods);
float deltaTime = 0.0f;
float lastFrame = 0.0f;
float currentFrame = glfwGetTime();
float near = 10.6f, far = 100.0f, winZ;
bool pickingModelWorldPosition = false;
double winX, winY;
Camera camera;

int main()
{
    GLFWwindow* window = init();
    Shader cubeShader("cube.vs", "cube.fs");
    //glPolygonMode(GL_FRONT_AND_BACK,/*GL_FILL*/GL_LINE);
    glfwSetScrollCallback(window, scroll_callback);
    glEnable(GL_DEPTH_TEST);

    Model ourModel("E:/kSource/LearnOpenGLz/LearnOpenGL-og/resources/objects/nanosuit/nanosuit.obj");
    while (!glfwWindowShouldClose(window))
    {
        currentFrame = glfwGetTime();
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;

        processInput(window);
        float radius = 10.0f;
        float camX = sin(glfwGetTime())*radius;
        float camZ = cos(glfwGetTime())*radius;

        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);


        glm::mat4 trans = glm::mat4(1.0f);
        glm::mat4 model;
        model = glm::translate(trans, cubePositions[0]);
        //model=glm::rotate(model,(float)glfwGetTime(),glm::vec3(0.0f,3.0f,0.0f));
        glm::mat4 view;
        view = camera.GetViewMatrix();
        //view=glm::translate(view,glm::vec3(0.0f,0.0f,-3.0f));
        glm::mat4 projection;
        projection = glm::perspective(glm::radians(camera.mFov), 800.0f / 600.0f, near, far);
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

        if (pickingModelWorldPosition == true)
        {

            glReadPixels((int)winX, 600 - (int)winY, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT, &winZ);
            float x = (2.0f*winX) / 800.0f - 1.0f;
            float y = 1.0f - (2.0f*winY) / 600.0f;
            float z = winZ * 2.0 - 1.0f;
            pickingModelWorldPosition = false;
            if (winZ < 1.0f)
            {

                //float w = (2.0 * near * far) / (far + near - z * (far - near));
                float w = near * far / (near*winZ - far * winZ + far);
                glm::vec4 wolrdPostion = glm::inverse(view)*glm::inverse(projection)*w*glm::vec4(x, y, z, 1);
                cout << " x:" << wolrdPostion.r << " y:" << wolrdPostion.g << " z:" << wolrdPostion.b << " w:" << w << endl;
            }
            else
                cout << "没有点中模型...." << endl;
        }

    }
    //退出
    glfwTerminate();
    return 0;
}

GLFWwindow* init()
{
    //初始化
    GLFWwindow * window;
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    window = glfwCreateWindow(800, 600, "OPENGL", NULL, NULL);
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
    glfwSetMouseButtonCallback(window, mouse_button_callback);
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);

    if (glfwGetKey(window, GLFW_KEY_Q) == GLFW_PRESS)
    {
        glfwSetCursorPosCallback(window, mouse_callback);
        glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
    }

    float cameraSpeed = 2.5f*deltaTime;
    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        camera.mPosition += cameraSpeed * camera.mFront;
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.mPosition -= cameraSpeed * camera.mFront;;
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.mPosition -= glm::normalize(glm::cross(camera.mFront, camera.mUp))*cameraSpeed;
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.mPosition += glm::normalize(glm::cross(camera.mFront, camera.mUp))*cameraSpeed;
}

void mouse_callback(GLFWwindow* window, double xpose, double ypose)
{
    static float yaw = -90.0f, pitch = 0.0f, lastX = 800.0f / 2, lastY = 600.0f / 2, xoffset, yoffset;
    xoffset = xpose - lastX;
    yoffset = lastY - ypose;
    lastX = xpose;
    lastY = ypose;
    camera.ProcessMouseMovement(xoffset, yoffset);
}

void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
{
    camera.ProcessMouseScroll(yoffset);
}

void mouse_button_callback(GLFWwindow * window, int button, int action, int mods)
{
    if (action == GLFW_PRESS) switch (button)
    {
    case GLFW_MOUSE_BUTTON_LEFT:
        glfwGetCursorPos(window, &winX, &winY);
        pickingModelWorldPosition = true;
        break;
    default:
        return;
    }
    return;
}