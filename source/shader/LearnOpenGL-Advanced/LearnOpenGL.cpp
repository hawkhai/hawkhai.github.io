#include <glad\glad.h>
#include "Shader.h"
#include <GLFW/glfw3.h>
#include "stb_image.h"
#include "Camera.h"
#include "Model.h"
#include <map>

//声明
#pragma region

glm::vec3 cubePositions[] = {
    glm::vec3(0.0f,0.0f,0.0f),//cube
    glm::vec3(0.0f, 5.0f, 20.0f),//lamp
    glm::vec3(-10.0f,1.0f,-10.0f),//cube2
};
GLFWwindow* init();
void processInput(GLFWwindow* window);
void mouse_callback(GLFWwindow* window, double xpose, double ypose);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);
void mouse_button_callback(GLFWwindow * window, int button, int action, int mods);
void modelPicking();
float deltaTime = 0.0f;
float lastFrame = 0.0f;
float currentFrame = glfwGetTime();
float near = 0.1f, far = 100.0f, winZ;
bool pickingModelWorldPosition = false;
double winX, winY;
Camera camera;
string modelSelected = "NULL";
glm::vec3 modelPos;
struct modelStruct
{
    Model * model;
    glm::mat4 modelMatrix;
    glm::vec3 worldPosition;
};
modelStruct modelObject;
map<string, modelStruct> _models;
map<string, modelStruct>::iterator _modelsIter;
glm::mat4 model;
glm::mat4 view;
glm::mat4 projection;
#pragma endregion

Mesh getMesh(unsigned int textureColorbuffer)
{
    vector<Vertex> vertices;
    vector<unsigned int> indices;
    vector<Texture> textures;
    float transparentVertices[] = {
        // positions      // texture Coords (swapped y coordinates because texture is flipped upside down)
        0.0f,  0.5f,  0.0f,  0.0f,  1.0 - 0.0f,
        0.0f, -0.5f,  0.0f,  0.0f,  1.0 - 1.0f,
        1.0f, -0.5f,  0.0f,  1.0f,  1.0 - 1.0f,

        0.0f,  0.5f,  0.0f,  0.0f,  1.0 - 0.0f,
        1.0f, -0.5f,  0.0f,  1.0f,  1.0 - 1.0f,
        1.0f,  0.5f,  0.0f,  1.0f,  1.0 - 0.0f
    };

    for (int i = 0; i < 6; i++)
    {
        Vertex _vertex;
        _vertex.Position = glm::vec3(transparentVertices[i * 5 + 0], transparentVertices[i * 5 + 1], transparentVertices[i * 5 + 2]);
        _vertex.Normal = glm::vec3(0, 0, 1);
        _vertex.TexCoords = glm::vec2(transparentVertices[i * 5 + 3], transparentVertices[i * 5 + 4]);
        vertices.push_back(_vertex);
    }
    for (int i = 0; i < 6; i++)
    {
        indices.push_back(i);
    }
    Texture _tex;
    _tex.id = textureColorbuffer;
    _tex.type = "texture_diffuse";
    _tex.path = "cao.png";
    textures.push_back(_tex);
    return Mesh(vertices, indices, textures);
}
void setShader(Shader * shader)
{
    shader->useShader();
    shader->setMat4("projection", projection);
    shader->setMat4("view", view);
    shader->setVec4("lightPos", cubePositions[1].r, cubePositions[1].g, cubePositions[1].b, 1);
    shader->setVec3("viewPos", camera.Position.r, camera.Position.g, camera.Position.b);
    shader->setVec3("front", camera.Front.r, camera.Front.g, camera.Front.b);
    shader->setVec3("lightColor", 1.0f, 1.0f, 1.0f);
}
int main()
{
    GLFWwindow* window = init();
    Shader modelShader("cube.vs", "cube.fs");
    Shader stencilShader("cube.vs", "stencil.fs");
    Shader caoShader("cube.vs", "cao.fs");

    glfwSetScrollCallback(window, scroll_callback);

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    Model ourModel("D:/WK/opengl/bin/nanosuit/nanosuit.obj");
    modelObject.model = &ourModel;
    _models["Zhang3"] = modelObject;
    modelObject.worldPosition = cubePositions[2];
    _models["Li4"] = modelObject;

    vector<glm::vec3> windowsPos;
    windowsPos.push_back(glm::vec3(-0.5f, 7.5f, 18.48f));
    map<float, glm::vec3> sortedWindowsPos;
    for (int i = 0; i < windowsPos.size(); i++)
    {
        float distance = glm::length(camera.Position - windowsPos[i]);
        sortedWindowsPos[distance] = windowsPos[i];
    }

    unsigned int FBO; // 创建一个帧缓冲对象
    glGenFramebuffers(1, &FBO);
    glBindFramebuffer(GL_FRAMEBUFFER, FBO);

    unsigned int texColorBuffer = 0;
    glGenTextures(1, &texColorBuffer); // 纹理附件
    glBindTexture(GL_TEXTURE_2D, texColorBuffer);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 600, 450, 0, GL_RGB, GL_UNSIGNED_BYTE, NULL);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // 它附加到帧缓冲上
    glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texColorBuffer, 0);

    unsigned int RBO; // 缓冲对象附件
    glGenRenderbuffers(1, &RBO);
    glBindRenderbuffer(GL_RENDERBUFFER, RBO);
    glRenderbufferStorage(GL_RENDERBUFFER, GL_DEPTH24_STENCIL8, 600, 450);

    // 把帧缓冲对象附加上
    glFramebufferRenderbuffer(GL_FRAMEBUFFER, GL_DEPTH_STENCIL_ATTACHMENT, GL_RENDERBUFFER, RBO);

    if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE)
        std::cout << "ERROR::FRAMEBUFFER:: Framebuffer is not complete!" << std::endl;

    glBindFramebuffer(GL_FRAMEBUFFER, 0);

    Mesh mesh = getMesh(texColorBuffer);

    while (!glfwWindowShouldClose(window))
    {
        currentFrame = glfwGetTime();
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;

        processInput(window);
        float radius = 10.0f;
        float camX = sin(glfwGetTime())*radius;
        float camZ = cos(glfwGetTime())*radius;

        glm::mat4 trans = glm::mat4(1.0f);
        model = glm::mat4(1.0f);
        view = glm::mat4(1.0f);
        view = camera.GetViewMatrix();
        projection = glm::mat4(1.0f);;
        projection = glm::perspective(glm::radians(camera.fov), 600.0f / 450.0f, near, far);
        setShader(&modelShader);
        setShader(&caoShader);
        setShader(&stencilShader);

        //将内容绘制到自定义帧缓冲的纹理附件
        glBindFramebuffer(GL_FRAMEBUFFER, FBO);

        glEnable(GL_DEPTH_TEST);
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);
        for (_modelsIter = _models.begin(); _modelsIter != _models.end(); _modelsIter++)
        {
            glStencilFunc(GL_ALWAYS, 1, 0xFF);
            model = glm::translate(trans, _modelsIter->second.worldPosition);
            //_modelsIter->second.modelMatrix=model=glm::rotate(model,(float)glfwGetTime(),glm::vec3(0.0f,1.0f,0.0f));
            if (_modelsIter->first == modelSelected)
            {
                modelShader.useShader();
                modelShader.setMat4("model", model);
                _modelsIter->second.model->Draw(modelShader);
                glStencilFunc(GL_NOTEQUAL, 1, 0xFF);
                glStencilMask(0x00);
                float scale = 1.02;
                model = glm::translate(model, glm::vec3(0.0f, 7.5f, 0.0f));
                model = glm::scale(model, scale*glm::vec3(1, 1, 1));
                _modelsIter->second.modelMatrix = model = glm::translate(model, glm::vec3(0.0f, -7.5f, 0.0f));
                stencilShader.useShader();
                stencilShader.setMat4("model", model);
                _modelsIter->second.model->Draw(stencilShader);
                glStencilMask(0xFF);
            }
            else {

                modelShader.useShader();
                modelShader.setMat4("model", model);
                _modelsIter->second.model->Draw(modelShader);
            }
        }
        //使用纹理绘制窗户
        glBindFramebuffer(GL_FRAMEBUFFER, 0);
        glDisable(GL_DEPTH_TEST);
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        map<float, glm::vec3>::reverse_iterator iter;
        for (iter = sortedWindowsPos.rbegin(); iter != sortedWindowsPos.rend(); ++iter)
        {
            model = glm::translate(trans, iter->second);
            caoShader.useShader();
            caoShader.setMat4("model", model);
            mesh.Draw(caoShader);
        }

        glfwPollEvents();
        glfwSwapBuffers(window);
        modelPicking();

        static int ticks = -1;
        ticks++;
        static double _lastTime = glfwGetTime();

        if (ticks == 60)
        {
            double deltaTime = glfwGetTime() - _lastTime;
            cout << "帧数：" << ticks / deltaTime << endl;
            ticks = 0;
            _lastTime = glfwGetTime();

        }
    }

    glDeleteFramebuffers(1, &FBO);

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
    window = glfwCreateWindow(600, 450, "OPENGL", NULL, NULL);
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
        camera.Position += cameraSpeed * camera.Front;
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.Position -= cameraSpeed * camera.Front;;
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.Position -= glm::normalize(glm::cross(camera.Front, camera.UP))*cameraSpeed;
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.Position += glm::normalize(glm::cross(camera.Front, camera.UP))*cameraSpeed;
}

void mouse_callback(GLFWwindow* window, double xpose, double ypose)
{
    static float yaw = -90.0f, pitch = 0.0f, lastX = 600.0f / 2, lastY = 450.0f / 2, xoffset, yoffset;
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

void modelPicking()
{
    if (pickingModelWorldPosition == true)
    {
        glReadPixels((int)winX, 450 - (int)winY, 1, 1, GL_DEPTH_COMPONENT, GL_FLOAT, &winZ);
        float x = (2.0f*winX) / 600.0f - 1.0f;
        float y = 1.0f - (2.0f*winY) / 450.0f;
        float z = winZ * 2.0 - 1.0f;
        pickingModelWorldPosition = false;
        //有像素被点中
        if (winZ < 1.0f)
        {
            //float w = (2.0 * near * far) / (far + near - z * (far - near));
            float w = near * far / (near*winZ - far * winZ + far);
            glm::vec4 wolrdPostion = glm::inverse(view)*glm::inverse(projection)*w*glm::vec4(x, y, z, 1);
            //cout<<" x:"<<wolrdPostion.r<<" y:"<<wolrdPostion.g<<" z:"<<wolrdPostion.b<<" w:"<<w<<endl;
            for (_modelsIter = _models.begin(); _modelsIter != _models.end(); _modelsIter++)
            {
                float _distance = glm::distance(_modelsIter->second.worldPosition + glm::vec3(0, 7.5, 0), glm::vec3(wolrdPostion));
                if (_distance < 7.5)
                {
                    modelPos = glm::inverse(_modelsIter->second.modelMatrix)*wolrdPostion;
                    modelSelected = _modelsIter->first;
                    cout << _modelsIter->first << "模型被选中..." << endl;
                }

            }
        }
        else
        {
            modelSelected = "NULL";
            //cout<<"没有点中模型...."<<endl;
        }

    }
}