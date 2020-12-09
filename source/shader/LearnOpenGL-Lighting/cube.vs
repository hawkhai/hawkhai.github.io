#version 400 core
layout(location=0) in vec3 aPos; // 坐标
layout(location=1) in vec3 aNormal; // 法线
layout(location=2) in vec2 aTexCoords; // 纹理坐标
out vec3 Normal; // 法线向量
out vec2 TexCoords; // 纹理坐标
out vec3 FragPos; // 模型坐标
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    FragPos=vec3(model*vec4(aPos,1.0f));
    Normal=mat3(transpose(inverse(model)))*aNormal;
    TexCoords=aTexCoords;

    gl_Position=projection*view*vec4(FragPos,1.0f);
}