#version 400 core
out vec4 FragColor;
in vec2 TexCoord;
uniform sampler2D ourTexture1;
uniform sampler2D ourTexture2;
uniform vec3 lightColor;
void main()
{
	FragColor = vec4(1.0,1.0,1.0,1.0);
}