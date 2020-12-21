#version 330 core
layout (location = 0) in vec3 aPos;
layout(location  = 1) in vec3 aNormal;
layout (location = 2) in vec2 aTexCoords;

out VS_OUT {
//    vec2 texCoords;
	vec3 normal;
} vs_out;
//uniform ª∫≥Â∂‘œÛ
layout (std140) uniform Matrices
{
    mat4 projection;
};
uniform mat4 view;
uniform mat4 model;

void main()
{
	vs_out.normal = mat3(transpose(inverse(model)))*aNormal;
//    vs_out.texCoords = aTexCoords;
    gl_Position = projection * view * model * vec4(aPos, 1.0); 
}