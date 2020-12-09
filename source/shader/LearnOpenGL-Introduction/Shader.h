#pragma once
#include <glad\glad.h>
//#include <stdio.h>
//#include <string>
//#include <fstream>
//#include <sstream>
#include <iostream>

class Shader
{
public:
	int ID;
	void useShader();
	Shader(void);
	~Shader(void);
};
