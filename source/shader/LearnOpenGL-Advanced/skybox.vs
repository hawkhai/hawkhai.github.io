#version 400 core
layout (location=0) in vec3 aPos;
out vec3 TexCoords;
layout (std140) uniform Matrices
{
    mat4 projection;
};
uniform mat4 view;
void main()
{
	TexCoords=aPos;
	gl_Position=view*vec4(aPos,1.0);
	float w=-gl_Position.z;
	gl_Position=projection*view*vec4(aPos,1.0);
	gl_Position.z=w;
}  