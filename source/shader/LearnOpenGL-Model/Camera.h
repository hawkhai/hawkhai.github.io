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
        mPosition = glm::vec3(0.0f, 7.0f, 25.0f);
        mFront = glm::vec3(0.0f, 0.0f, -1.0f);
        mUp = glm::vec3(0.0f, 1.0f, 0.0f);
        mFov = 45;
        mPitch = 0;
        mYaw = 0;
    }

    glm::mat4 GetViewMatrix()
    {
        return glm::lookAt(mPosition, mPosition + mFront, mUp);
    }

    void ProcessMouseMovement(float xoffset, float yoffset)
    {
        mYaw += xoffset * 0.1;
        mPitch += yoffset * 0.1;
        glm::vec3 front;

        if (mPitch > 89.0f)
            mPitch = 89.0f;
        if (mPitch < -89.0f)
            mPitch = -89.0f;

        front.x = cos(glm::radians(mYaw)) * cos(glm::radians(mPitch));
        front.y = sin(glm::radians(mPitch));
        front.z = sin(glm::radians(mYaw)) * cos(glm::radians(mPitch));
        mFront = glm::normalize(front);
    }
    void ProcessMouseScroll(float yoffset)
    {
        if (mFov >= 1.0f && mFov <= 85.0f)
            mFov -= yoffset;
        if (mFov <= 1.0f)
            mFov = 1.0f;
        if (mFov >= 85.0f)
            mFov = 85.0f;
    }
public:
    glm::vec3 mPosition, mFront, mUp;
    float mPitch, mYaw, mFov;
};
#endif
