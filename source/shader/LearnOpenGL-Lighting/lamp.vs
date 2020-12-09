#version 400 core
layout(location=0) in vec3 aPos; // 坐标
layout(location=1) in vec2 aTexCoord; // 纹理坐标
out vec2 TexCoord;
uniform mat4 transform; // 转换矩阵

void main()
{
    gl_Position=transform*vec4(aPos.x,aPos.y,aPos.z,1.0f);
    TexCoord=aTexCoord;
}