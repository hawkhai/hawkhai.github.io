#include <glad\glad.h>
#include "Shader.h"
#include <GLFW/glfw3.h>
#include "stb_image.h"
#include "Camera.h"

//顶点数据
#pragma region
float vertices[] = {
    -0.5f, -0.5f, -0.5f,  0.0f, 0.0f,
     0.5f, -0.5f, -0.5f,  1.0f, 0.0f,
     0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
     0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
    -0.5f,  0.5f, -0.5f,  0.0f, 1.0f,
    -0.5f, -0.5f, -0.5f,  0.0f, 0.0f,

    -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
     0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 1.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 1.0f,
    -0.5f,  0.5f,  0.5f,  0.0f, 1.0f,
    -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,

    -0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
    -0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
    -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
    -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
    -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
    -0.5f,  0.5f,  0.5f,  1.0f, 0.0f,

     0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
     0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
     0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
     0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
     0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 0.0f,

    -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,
     0.5f, -0.5f, -0.5f,  1.0f, 1.0f,
     0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
     0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
    -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
    -0.5f, -0.5f, -0.5f,  0.0f, 1.0f,

    -0.5f,  0.5f, -0.5f,  0.0f, 1.0f,
     0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 0.0f,
    -0.5f,  0.5f,  0.5f,  0.0f, 0.0f,
    -0.5f,  0.5f, -0.5f,  0.0f, 1.0f
};

glm::vec3 cubePositions[]={
	glm::vec3(0.0f,0.0f,0.0f),
	glm::vec3(2.0f,5.0f,-15.0f),
	glm::vec3(-2.0f,3.0f,-7.5f),
};
//float vertices[]={
//	-0.5f,-0.5f,0.0f,0,0,//left,down
//	 0.5f,-0.5f,0.0f,1,0,//right,down
//	 0.5f, 0.5f,0.0f,1,1,//right,top
//	-0.5f, 0.5f,0.0f,0,1//left,top
//};
unsigned int indices[]={
	0,1,3,
	1,2,3
};
#pragma endregion

GLFWwindow* init();
void VAOSet();
void texture(Shader *myShader);
void processInput(GLFWwindow* window);
void mouse_callback(GLFWwindow* window,double xpose,double ypose);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);

float deltaTime=0.0f;
float lastFrame=0.0f;
float currentFrame=glfwGetTime();
Camera camera;

int main()
{ 
	GLFWwindow* window=init();

	VAOSet();
	Shader myShader;
	texture(&myShader);
	//glPolygonMode(GL_FRONT_AND_BACK,/*GL_FILL*/GL_LINE);
	//渲染引擎
	glfwSetCursorPosCallback(window,mouse_callback);
	glfwSetInputMode(window,GLFW_CURSOR,GLFW_CURSOR_DISABLED);
	glfwSetScrollCallback(window,scroll_callback);
	glEnable(GL_DEPTH_TEST);
	while(!glfwWindowShouldClose(window))
	{
		currentFrame=glfwGetTime();
		deltaTime=currentFrame-lastFrame;
		lastFrame=currentFrame;

		processInput(window);
		float radius=10.0f;
		float camX=sin(glfwGetTime())*radius;
		float camZ=cos(glfwGetTime())*radius;

		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
		
		for(int i=0;i<3;i++)
		{
			glm::mat4 trans=glm::mat4(1.0f);
			glm::mat4 model;
			model=glm::translate(trans,cubePositions[i]);
			model=glm::rotate(model,(float)glfwGetTime(),glm::vec3(1.5f,3.0f,0.0f));

			glm::mat4 view;
			view=camera.GetViewMatrix();
			//view=glm::translate(view,glm::vec3(0.0f,0.0f,-3.0f));
			glm::mat4 projection;
			projection=glm::perspective(glm::radians(camera.fov),800.0f/600.0f,0.1f,100.0f);
			trans=projection*view*model;

			myShader.useShader();
			glUniformMatrix4fv(glGetUniformLocation(myShader.ID,"transform"),1,GL_FALSE,
			glm::value_ptr(trans));
			glDrawArrays(GL_TRIANGLES,0,36);//画三角
		//glDrawElements(GL_TRIANGLES,6,GL_UNSIGNED_INT,0);
		}

		glfwPollEvents();
		glfwSwapBuffers(window);
	}
	//退出
	glfwTerminate();
	return 0;
}

void VAOSet()
{
	unsigned int VBO,VAO,EBO;//ID
	glGenVertexArrays(1,&VAO);
	glGenBuffers(1,&VBO);
	glGenBuffers(1,&EBO);

	glBindVertexArray(VAO);
	glBindBuffer(GL_ARRAY_BUFFER,VBO);
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,EBO);

	//往显卡写值，分配显存空间GL_STATIC_DRAW表示，值不修改
	glBufferData(GL_ARRAY_BUFFER,sizeof(vertices),vertices,GL_STATIC_DRAW);
	glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(indices),indices,GL_STATIC_DRAW);
	//告诉显卡，值的结构 position
	glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,5*sizeof(float),(void*)0);
	glEnableVertexAttribArray(0);
	//告诉显卡，值的结构 position
	glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,5*sizeof(float),(void*)(3*sizeof(float)));
	glEnableVertexAttribArray(1);
}

GLFWwindow* init()
{
		//初始化
	GLFWwindow * window;
	glfwInit();
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR,4);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR,0);
	glfwWindowHint(GLFW_OPENGL_PROFILE,GLFW_OPENGL_CORE_PROFILE);
	window =glfwCreateWindow(800,600,"OPENGL",NULL,NULL);
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

void PrintFullPath(char* partialPath)
{
	char full[_MAX_PATH];
	if (_fullpath(full, partialPath, _MAX_PATH) != NULL)
		printf("Full path is: %s\n", full);
	else
		printf("Invalid path\n");
}

void texture(Shader * myShader)
{
	int width,height,nrChannels;
	unsigned char * data;
	stbi_set_flip_vertically_on_load(true);

	unsigned int texture[2];
	glGenTextures(2,texture);
	//加载第一个纹理
	glBindTexture(GL_TEXTURE_2D,texture[0]);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
	PrintFullPath("Debug\\gitee.png");
	data=stbi_load("Debug\\gitee.png",&width,&height,&nrChannels,0);

	GLint internalformat;
	internalformat = GL_RGB;
	if (nrChannels == 1) internalformat = GL_RED;
	if (nrChannels == 3) internalformat = GL_RGB;
	if (nrChannels == 4) internalformat = GL_RGBA;

	glTexImage2D(GL_TEXTURE_2D,0, internalformat,width,height,0, internalformat,GL_UNSIGNED_BYTE,data);
	glGenerateMipmap(GL_TEXTURE_2D);
	stbi_image_free(data);
	//加载第二个纹理
	glBindTexture(GL_TEXTURE_2D,texture[1]);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
	data=stbi_load("Debug\\opengl.png",&width,&height,&nrChannels,0);

	internalformat = GL_RGB;
	if (nrChannels == 1) internalformat = GL_RED;
	if (nrChannels == 3) internalformat = GL_RGB;
	if (nrChannels == 4) internalformat = GL_RGBA;

	glTexImage2D(GL_TEXTURE_2D,0, internalformat,width,height,0, internalformat,GL_UNSIGNED_BYTE,data);
	glGenerateMipmap(GL_TEXTURE_2D);
	stbi_image_free(data);

	myShader->useShader();
	glUniform1i(glGetUniformLocation(myShader->ID,"ourTexture1"),0);//默认状态，可以省略
	glUniform1i(glGetUniformLocation(myShader->ID,"ourTexture2"),1);

	glActiveTexture(GL_TEXTURE0);//先激活再绑定，纹理单元0,默认状态，可以省略
	glBindTexture(GL_TEXTURE_2D,texture[0]);
	glActiveTexture(GL_TEXTURE1);//先激活再绑定，纹理单元1
	glBindTexture(GL_TEXTURE_2D,texture[1]);
}
void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);

	float cameraSpeed=2.5f*deltaTime;
	if(glfwGetKey(window,GLFW_KEY_W)==GLFW_PRESS)
		camera.Position+=cameraSpeed*camera.Front;
	if(glfwGetKey(window,GLFW_KEY_S)==GLFW_PRESS)
		camera.Position-=cameraSpeed*camera.Front;;
	if(glfwGetKey(window,GLFW_KEY_A)==GLFW_PRESS)
		camera.Position-=glm::normalize(glm::cross(camera.Front,camera.UP))*cameraSpeed;
	if(glfwGetKey(window,GLFW_KEY_D)==GLFW_PRESS)
		camera.Position+=glm::normalize(glm::cross(camera.Front,camera.UP))*cameraSpeed;
}

void mouse_callback(GLFWwindow* window,double xpose,double ypose)
{
	static float yaw=-90.0f,pitch=0.0f,lastX=800.0f/2,lastY=600.0f/2,xoffset,yoffset;
	xoffset=xpose-lastX;
	yoffset=lastY-ypose;
	lastX=xpose;
	lastY=ypose;
	camera.ProcessMouseMovement(xoffset,yoffset);
}

void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
{
	camera.ProcessMouseScroll(yoffset);
}