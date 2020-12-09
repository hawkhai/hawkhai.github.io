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
		m_vecPosition = glm::vec3(0.0f, 0.0f, 3.0f);
		m_vecFront = glm::vec3(0.0f, 0.0f, -1.0f);
		m_vecUp = glm::vec3(0.0f, 1.0f, 0.0f);
		m_fFov = 45; // 摄像机 视锥上下面之间的夹角
		m_fPitch = 0;
		m_fYaw = 0;
	}

	glm::mat4 GetViewMatrix()
	{
		return glm::lookAt(m_vecPosition, m_vecPosition + m_vecFront, m_vecUp);
	}

	void ProcessMouseMovement(float xoffset, float yoffset)
	{
		m_fYaw += xoffset * 0.1;
		m_fPitch += yoffset * 0.1;
		glm::vec3 front;

		if (m_fPitch > 89.0f)
			m_fPitch = 89.0f;
		if (m_fPitch < -89.0f)
			m_fPitch = -89.0f;

		front.x = cos(glm::radians(m_fYaw)) * cos(glm::radians(m_fPitch));
		front.y = sin(glm::radians(m_fPitch));
		front.z = sin(glm::radians(m_fYaw)) * cos(glm::radians(m_fPitch));
		m_vecFront = glm::normalize(front);
	}

	void ProcessMouseScroll(float yoffset)
	{
		// 调整 视野角度
		if (m_fFov >= 1.0f && m_fFov <= 85.0f)
			m_fFov -= yoffset;
		if (m_fFov <= 1.0f)
			m_fFov = 1.0f;
		if (m_fFov >= 85.0f)
			m_fFov = 85.0f;
	}

public:
	glm::vec3 m_vecPosition, m_vecFront, m_vecUp;
	float m_fPitch, m_fYaw, m_fFov;
};
#endif
