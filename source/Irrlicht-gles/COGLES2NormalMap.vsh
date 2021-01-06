#define MAX_LIGHTS 2 // 最多两个光源

/* Attributes */

attribute vec3 inVertexPosition; // 顶点坐标
attribute vec3 inVertexNormal; // 顶点法线
attribute vec3 inVertexTangent; // 顶点切线
attribute vec3 inVertexBinormal; // 顶点副法线
attribute vec4 inVertexColor; // 顶点颜色
attribute vec2 inTexCoord0; // 纹理坐标

/* Uniforms */

uniform mat4 uWVPMatrix; // 透视矩阵
uniform mat4 uWVMatrix; // 世界矩阵
uniform vec3 uLightPosition[MAX_LIGHTS]; // 光源位置
uniform vec4 uLightColor[MAX_LIGHTS]; // 光源颜色

/* Varyings */

varying vec2 vTexCoord; // 纹理坐标
varying vec3 vLightVector[MAX_LIGHTS]; // 光源向量
varying vec4 vLightColor[MAX_LIGHTS]; // 光源颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

void main()
{
    gl_Position = uWVPMatrix * vec4(inVertexPosition, 1.0);

    vTexCoord = inTexCoord0;

    for (int i = 0; i < int(MAX_LIGHTS); i++)
    {
        vec3 LightVector = uLightPosition[i] - inVertexPosition;

        vLightVector[i].x = dot(inVertexTangent, LightVector);
        vLightVector[i].y = dot(inVertexBinormal, LightVector);
        vLightVector[i].z = dot(inVertexNormal, LightVector);

        vLightColor[i].x = dot(LightVector, LightVector);
        vLightColor[i].x *= uLightColor[i].a;
        vLightColor[i] = vec4(inversesqrt(vLightColor[i].x));
        vLightColor[i] *= uLightColor[i];
        vLightColor[i].a = inVertexColor.a;

        vLightColor[i].x = clamp(vLightColor[i].x, 0.0, 1.0);
        vLightColor[i].y = clamp(vLightColor[i].y, 0.0, 1.0);
        vLightColor[i].z = clamp(vLightColor[i].z, 0.0, 1.0);
    }

    vFogCoord = length((uWVMatrix * vec4(inVertexPosition, 1.0)).xyz);
}
