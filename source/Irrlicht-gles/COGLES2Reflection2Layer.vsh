#define MAX_LIGHTS 8 // 最多的光源数

/* Attributes */

attribute vec3 inVertexPosition; // 顶点坐标
attribute vec3 inVertexNormal; // 顶点法线
attribute vec4 inVertexColor; // 顶点颜色
attribute vec2 inTexCoord0; // 纹理坐标
attribute vec2 inTexCoord1; // 纹理坐标 2

/* Uniforms */

uniform mat4 uWVPMatrix; // 透视矩阵
uniform mat4 uWVMatrix; // 世界矩阵
uniform mat4 uNMatrix; // 法线矩阵
uniform mat4 uTMatrix0; // 纹理矩阵

uniform vec4 uGlobalAmbient; // 全局环境光
uniform vec4 uMaterialAmbient; // 材质环境光
uniform vec4 uMaterialDiffuse; // 材质漫反射
uniform vec4 uMaterialEmissive; // 材质自发光
uniform vec4 uMaterialSpecular; // 材质镜面反射
uniform float uMaterialShininess; // 材质镜面反射光泽度

uniform int uLightCount; // 光源个数
uniform int uLightType[MAX_LIGHTS]; // 光源类型
uniform vec3 uLightPosition[MAX_LIGHTS]; // 光源位置
uniform vec3 uLightDirection[MAX_LIGHTS]; // 光源方向
uniform vec3 uLightAttenuation[MAX_LIGHTS]; // 光源衰减
uniform vec4 uLightAmbient[MAX_LIGHTS]; // 光源环境光
uniform vec4 uLightDiffuse[MAX_LIGHTS]; // 光源漫反射
uniform vec4 uLightSpecular[MAX_LIGHTS]; // 光源镜面反射

uniform float uThickness; // 绘制的粗细。

/* Varyings */

varying vec2 vTextureCoord0; // 纹理坐标
varying vec2 vTextureCoord1; // 纹理坐标 2
varying vec4 vVertexColor; // 顶点颜色
varying vec4 vSpecularColor; // 镜面反射颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

void dirLight(in int index, in vec3 position, in vec3 normal, inout vec4 ambient, inout vec4 diffuse, inout vec4 specular)
{
    vec3 L = normalize(-(uNMatrix * vec4(uLightDirection[index], 0.0)).xyz);

    ambient += uLightAmbient[index];

    float NdotL = dot(normal, L);

    if (NdotL > 0.0)
    {
        diffuse += uLightDiffuse[index] * NdotL;

        vec3 E = normalize(-position);
        vec3 HalfVector = normalize(L + E);
        float NdotH = max(0.0, dot(normal, HalfVector));

        float SpecularFactor = pow(NdotH, uMaterialShininess);
        specular += uLightSpecular[index] * SpecularFactor;
    }
}

void pointLight(in int index, in vec3 position, in vec3 normal, inout vec4 ambient, inout vec4 diffuse, inout vec4 specular)
{
    vec3 L = uLightPosition[index] - position;
    float D = length(L);
    L = normalize(L);

    float Attenuation = 1.0 / (uLightAttenuation[index].x + uLightAttenuation[index].y * D +
        uLightAttenuation[index].z * D * D);

    ambient += uLightAmbient[index] * Attenuation;

    float NdotL = dot(normal, L);

    if (NdotL > 0.0)
    {
        diffuse += uLightDiffuse[index] * NdotL * Attenuation;

        vec3 E = normalize(-position);
        vec3 HalfVector = normalize(L + E);
        float NdotH = max(0.0, dot(normal, HalfVector));

        float SpecularFactor = pow(NdotH, uMaterialShininess);
        specular += uLightSpecular[index] * SpecularFactor * Attenuation;
    }
}

void spotLight(in int index, in vec3 position, in vec3 normal, inout vec4 ambient, inout vec4 diffuse, inout vec4 specular)
{
    // TO-DO
}

void main()
{
    gl_Position = uWVPMatrix * vec4(inVertexPosition, 1.0);
    gl_PointSize = uThickness;

    vec4 TextureCoord0 = vec4(inTexCoord0.x, inTexCoord0.y, 1.0, 1.0);
    vTextureCoord0 = vec4(uTMatrix0 * TextureCoord0).xy;

    vec3 Position = (uWVMatrix * vec4(inVertexPosition, 1.0)).xyz;
    vec3 P = normalize(Position);
    vec3 N = normalize(vec4(uNMatrix * vec4(inVertexNormal, 0.0)).xyz);
    vec3 R = reflect(P, N);

    float V = 2.0 * sqrt(R.x*R.x + R.y*R.y + (R.z+1.0)*(R.z+1.0));
    vTextureCoord1 = vec2(R.x/V + 0.5, R.y/V + 0.5);

    vVertexColor = inVertexColor.bgra;
    vSpecularColor = vec4(0.0, 0.0, 0.0, 0.0);

    if (uLightCount > 0)
    {
        vec3 Normal = normalize((uNMatrix * vec4(inVertexNormal, 0.0)).xyz);

        vec4 Ambient = vec4(0.0, 0.0, 0.0, 0.0);
        vec4 Diffuse = vec4(0.0, 0.0, 0.0, 0.0);

        for (int i = 0; i < int(MAX_LIGHTS); i++)
        {
            if( i >= uLightCount )    // can't use uniform as loop-counter directly in glsl
                break;
            if (uLightType[i] == 0)
                pointLight(i, Position, Normal, Ambient, Diffuse, vSpecularColor);
        }

        for (int i = 0; i < int(MAX_LIGHTS); i++)
        {
            if( i >= uLightCount )
                break;
            if (uLightType[i] == 1)
                spotLight(i, Position, Normal, Ambient, Diffuse, vSpecularColor);
        }

        for (int i = 0; i < int(MAX_LIGHTS); i++)
        {
            if( i >= uLightCount )
                break;
            if (uLightType[i] == 2)
                dirLight(i, Position, Normal, Ambient, Diffuse, vSpecularColor);
        }

        vec4 LightColor = Ambient * uMaterialAmbient + Diffuse * uMaterialDiffuse;
        LightColor = clamp(LightColor, 0.0, 1.0);
        LightColor.w = 1.0;

        vVertexColor *= LightColor;
        vVertexColor += uMaterialEmissive;
        vVertexColor += uGlobalAmbient * uMaterialAmbient;
        vVertexColor = clamp(vVertexColor, 0.0, 1.0);

        vSpecularColor *= uMaterialSpecular;
    }

    vFogCoord = length(Position);
}
