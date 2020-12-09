#version 400 core
out vec4 FragColor;
in vec3 Normal;
in vec3 FragPos;
in vec2 TexCoords;
uniform sampler2D ourTexture1;
uniform sampler2D ourTexture2;
uniform vec3 lightColor;
uniform vec3 objectColor;
uniform vec4 lightPos;
uniform vec3 viewPos;
uniform vec3 front;
struct Material{
	vec3 ambient;
	vec3 diffuse;
	vec3 specular;
	float shininess;
};

struct SpotLight{
	vec3 position;
	vec3 direction;
	float cutOff;
	float outerCutOff;

	vec3 ambient;
	vec3 diffuse;
	vec3 specular;

	float constant;
	float linear;
	float quadratic;
};
struct Light{
	vec4 lightDir;
	vec3 ambient;
	vec3 diffuse;
	vec3 specular;

	float constant;
	float linear;
	float quadratic;
};

Material material;
Light light;
SpotLight spotLight;
vec3 CalcPointLight(Light light);
vec3 CalcSpotLight(SpotLight light);

void main()
{
	material.ambient=vec3(texture(ourTexture1,TexCoords));
	material.diffuse=vec3(texture(ourTexture1,TexCoords));
	material.specular=vec3(texture(ourTexture2,TexCoords));
	material.shininess=32;

	spotLight.position=viewPos;
	spotLight.direction=front;
	spotLight.outerCutOff=12.5;
	spotLight.cutOff=5.5;

	spotLight.constant=1.0;
	spotLight.linear=0.09;
	spotLight.quadratic=0.032;
	spotLight.ambient=vec3(0.0,0.0,0.0);
	spotLight.diffuse=vec3(1.0,1.0,1.0);
	spotLight.specular=vec3(1.0,1.0,1.0);

	light.constant=1.0;
	light.linear=0.09;
	light.quadratic=0.032;
	light.lightDir=lightPos;
	light.ambient=vec3(0.2,0.2,0.2);
	light.diffuse=vec3(0.6,0.6,0.6);
	light.specular=vec3(1.0,1.0,1.0);
	
	vec3 result=vec3(0.0,0.0,0.0);
	result+=CalcPointLight(light);
	result+=CalcSpotLight(spotLight);
	
	FragColor=vec4(result,1.0);
}
vec3 CalcPointLight(Light light)
{
	vec3 lightDir;
	float distance;
	if(light.lightDir.w==0.0)//direction
		lightDir=normalize(-vec3(light.lightDir));
	else if(light.lightDir.w==1.0)//position
	{
		distance=length(vec3(light.lightDir)-FragPos);
		lightDir=normalize(vec3(light.lightDir)-FragPos);
	}
	float attenuation=1.0/(light.constant+light.linear*distance+light.quadratic*distance*distance);
	float diffuse=max(dot(Normal,lightDir),0.0);

	vec3 viewDir=normalize(viewPos-FragPos);
	vec3 reflectDir=reflect(-lightDir,Normal);
	float specular=pow(max(dot(reflectDir,viewDir),0.0),material.shininess);
	vec3 result=vec3(0.0,0.0,0.0);
	result = (light.ambient*material.ambient+
		diffuse*light.diffuse*material.diffuse+
		specular*light.specular*material.specular)*lightColor*attenuation;

	return result;
}
vec3 CalcSpotLight(SpotLight light)
{
	float theta=dot(normalize(vec3(light.position)-FragPos),-light.direction);
	float spotI=0;
	float epsilon=cos(radians(light.cutOff))-cos(radians(light.outerCutOff));
	spotI=clamp((theta-cos(radians(light.outerCutOff)))/epsilon,0.0,1.0);
	
	vec3 lightDir;
	float distance;
	lightDir=-light.direction;
	distance=length(vec3(light.position)-FragPos);

	float attenuation=1.0/(light.constant+light.linear*distance+light.quadratic*distance*distance);
	float diffuse=max(dot(Normal,lightDir),0.0);

	vec3 viewDir=normalize(viewPos-FragPos);
	vec3 reflectDir=reflect(-lightDir,Normal);
	float specular=pow(max(dot(reflectDir,viewDir),0.0),material.shininess);
	vec3 result=vec3(0.0,0.0,0.0);
	result = (light.ambient*material.ambient+
		diffuse*light.diffuse*material.diffuse+
		specular*light.specular*material.specular)*lightColor*attenuation*spotI;

	return result;
}