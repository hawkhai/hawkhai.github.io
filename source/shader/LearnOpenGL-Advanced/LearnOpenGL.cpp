#include <glad\glad.h>
#include "Shader.h"
#include <GLFW/glfw3.h>
#include "stb_image.h"
#include "Camera.h"
#include "Model.h"
#include <map>
//声明
#pragma region

glm::vec3 cubePositions[]={
	glm::vec3(0.0f,0.0f,0.0f),//cube
	glm::vec3(0.0f, 5.0f, 20.0f),//lamp
	glm::vec3(-10.0f,1.0f,-10.0f),//cube2
};
GLFWwindow* init();
void processInput(GLFWwindow* window);
void mouse_callback(GLFWwindow* window,double xpose,double ypose);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);
void mouse_button_callback(GLFWwindow * window, int button,int action ,int mods);
void modelPicking();
float deltaTime=0.0f;
float lastFrame=0.0f;
float currentFrame=glfwGetTime();
float near=10.6f, far=100.0f, winZ;
bool pickingModelWorldPosition=false;
double winX,winY;
Camera camera;
string modelSelected="NULL";
map<string,pair<glm::vec3,Model>> _models;
map<string,pair<glm::vec3,Model>>::iterator _modelsIter;
glm::mat4 model;
glm::mat4 view;
glm::mat4 projection;
#pragma endregion


int main()
{ 
	GLFWwindow* window=init();
	Shader modelShader("cube.vs","cube.fs");
	Shader stencilShader("cube.vs","stencil.fs");
	//glPolygonMode(GL_FRONT_AND_BACK,/*GL_FILL*/GL_LINE);
	glfwSetScrollCallback(window,scroll_callback);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_STENCIL_TEST);
	glStencilOp(GL_KEEP,GL_KEEP,GL_REPLACE);

    Model ourModel("E:/kSource/LearnOpenGLz/LearnOpenGL-og/resources/objects/nanosuit/nanosuit.obj");
	
	_models.insert(pair<string,pair<glm::vec3,Model>>("Zhang3",pair<glm::vec3,Model>(cubePositions[0],ourModel)));
	_models["Li4"]=pair<glm::vec3,Model>(cubePositions[2],ourModel);

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
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT);


		glm::mat4 trans=glm::mat4(1.0f);
		model=glm::mat4(1.0f);
		view=glm::mat4(1.0f);
		view=camera.GetViewMatrix();
		projection=glm::mat4(1.0f);;
		projection=glm::perspective(glm::radians(camera.fov),800.0f/600.0f,near,far);
		modelShader.useShader();
		modelShader.setMat4("projection",projection);
		modelShader.setMat4("view",view);
		modelShader.setVec4("lightPos",cubePositions[1].r,cubePositions[1].g,cubePositions[1].b,1);
		modelShader.setVec3("viewPos",camera.Position.r,camera.Position.g,camera.Position.b);
		modelShader.setVec3("front",camera.Front.r,camera.Front.g,camera.Front.b);
		modelShader.setVec3("lightColor",1.0f,1.0f,1.0f);
		stencilShader.useShader();
		stencilShader.setMat4("projection",projection);
		stencilShader.setMat4("view",view);
		//ourModel.Draw(cubeShader);
		for(_modelsIter=_models.begin();_modelsIter!=_models.end();_modelsIter++)
		{
			if(_modelsIter->first==modelSelected)
			{
				glStencilFunc(GL_ALWAYS,1,0xFF);
				model=glm::translate(trans,_modelsIter->second.first);
				model=glm::rotate(model,(float)glfwGetTime(),glm::vec3(0.0f,1.0f,0.0f));
				modelShader.useShader();
				modelShader.setMat4("model",model);
				_modelsIter->second.second.Draw(modelShader);
				glStencilFunc(GL_NOTEQUAL,1,0xFF);
				glStencilMask(0x00);
				float scale=1.02;
				model=glm::translate(model,glm::vec3(0.0f,7.5f,0.0f));
				model=glm::scale(model,scale*glm::vec3(1,1,1));
				model=glm::translate(model,glm::vec3(0.0f,-7.5f,0.0f));
				stencilShader.useShader();
				stencilShader.setMat4("model",model);
				_modelsIter->second.second.Draw(stencilShader);
				glStencilMask(0xFF);
			}else{
				glStencilFunc(GL_ALWAYS,1,0xFF);
				model=glm::translate(trans,_modelsIter->second.first);
				model=glm::rotate(model,(float)glfwGetTime(),glm::vec3(0.0f,1.0f,0.0f));
				modelShader.useShader();
				modelShader.setMat4("model",model);
				_modelsIter->second.second.Draw(modelShader);
			}
		}

		glfwPollEvents();
		glfwSwapBuffers(window);
		modelPicking();
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
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR,3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR,2);
	glfwWindowHint(GLFW_OPENGL_PROFILE,GLFW_OPENGL_CORE_PROFILE);
	window =glfwCreateWindow(600,450,"OPENGL",NULL,NULL);
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
	glfwSetMouseButtonCallback(window,mouse_button_callback);
	if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
		glfwSetWindowShouldClose(window, true);

	if(glfwGetKey(window,GLFW_KEY_Q)==GLFW_PRESS)
	{
		glfwSetCursorPosCallback(window,mouse_callback);
		glfwSetInputMode(window,GLFW_CURSOR,GLFW_CURSOR_DISABLED);
	}

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

void mouse_button_callback(GLFWwindow * window, int button,int action ,int mods)
{
	if(action== GLFW_PRESS) switch(button)
	{
	case GLFW_MOUSE_BUTTON_LEFT:
		glfwGetCursorPos(window,&winX,&winY);
		pickingModelWorldPosition=true;
		break;
	default:
		return;
	}
	return;
}

void modelPicking()
{
	if(pickingModelWorldPosition==true)
	{

		glReadPixels((int)winX,600-(int)winY,1,1,GL_DEPTH_COMPONENT,GL_FLOAT,&winZ);
		float x=(2.0f*winX)/800.0f-1.0f;
		float y=1.0f-(2.0f*winY)/600.0f;
		float z=winZ*2.0-1.0f;
		pickingModelWorldPosition=false;
		//有像素被点中
		if(winZ<1.0f)
		{
			//float w = (2.0 * near * far) / (far + near - z * (far - near));
			float w=near*far/(near*winZ-far*winZ+far);
			glm::vec4 wolrdPostion=glm::inverse(view)*glm::inverse(projection)*w*glm::vec4(x,y,z,1);
			//cout<<" x:"<<wolrdPostion.r<<" y:"<<wolrdPostion.g<<" z:"<<wolrdPostion.b<<" w:"<<w<<endl;
			for(_modelsIter=_models.begin();_modelsIter!=_models.end();_modelsIter++)
			{
				float _distance=glm::distance(_modelsIter->second.first+glm::vec3(0,7.5,0),glm::vec3(wolrdPostion));
				if(_distance<7.5)
				{
					modelSelected=_modelsIter->first;
					cout<<_modelsIter->first<<"模型被选中..."<<endl;
				}
				
			}
		}else
		{
			modelSelected="NULL";
			//cout<<"没有点中模型...."<<endl;
		}

	}
}