#ifndef CAMERA_H
#define CAMERA_H
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

class Camera
{

public:
	Camera()
	{
		Position= glm::vec3(0.0f,0.0f,3.0f);
		Front=glm::vec3(0.0f,0.0f,-1.0f);
		UP=glm::vec3(0.0f,1.0f,0.0f);
		fov=45;
	}
	glm::mat4 GetViewMatrix()
	{
		return glm::lookAt(Position,Position+Front,UP);
	}
	void ProcessMouseMovement(float xoffset,float yoffset)
	{
		Yaw+=xoffset*0.1;
		Pitch+=yoffset*0.1;
		glm::vec3 front;

		if (Pitch > 89.0f)
			Pitch = 89.0f;
		if (Pitch < -89.0f)
			Pitch = -89.0f;

		front.x = cos(glm::radians(Yaw)) * cos(glm::radians(Pitch));
		front.y = sin(glm::radians(Pitch));
		front.z = sin(glm::radians(Yaw)) * cos(glm::radians(Pitch));
		Front = glm::normalize(front);
	}
	void ProcessMouseScroll(float yoffset)
    {
		 if (fov >= 1.0f && fov <= 85.0f)
			fov -= yoffset;
		if (fov <= 1.0f)
			fov = 1.0f;
		if (fov >= 85.0f)
			fov = 85.0f;
    }
public:
	glm::vec3 Position,Front,UP;
	float Pitch,Yaw,fov;
};
#endif