#pragma once
#include <glad\glad.h>
//#include <stdio.h>
//#include <string>
//#include <fstream>
//#include <sstream>
#include <glm/glm.hpp>
#include <iostream>
class Shader
{
public:
	int ID;
	void useShader();
	Shader(const char* vertexPath, const char* fragmentPath);
	~Shader(void);
	void setMat4(const std::string &name, const glm::mat4 &mat) const;
    void setBool(const std::string &name, bool value) const;
    void setInt(const std::string &name, int value) const;
    void setFloat(const std::string &name, float value) const;
    void setVec2(const std::string &name, const glm::vec2 &value) const;
    void setVec2(const std::string &name, float x, float y) const;
    void setVec3(const std::string &name, const glm::vec3 &value) const;
    void setVec3(const std::string &name, float x, float y, float z) const;
    void setVec4(const std::string &name, const glm::vec4 &value) const;
    void setVec4(const std::string &name, float x, float y, float z, float w);
    void setMat2(const std::string &name, const glm::mat2 &mat) const;
    void setMat3(const std::string &name, const glm::mat3 &mat) const;
};

