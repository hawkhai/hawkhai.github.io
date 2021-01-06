---
layout: post
title: "Irrlicht 3D 笔记 -- OpenGL ES 2.x Driver 源码剖析 3D 基础部分"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle: none
comments:
visibility:
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
cluster: "Irrlicht OpenGL-ES2 Driver"
---

Irrlicht 采用了标准的 Blinn-Phong 光照模型。但是它是在 顶点着色器 里面计算的光照，这样更解决 GPU，相比放在片段着色器里面计算，光照效果更生硬。


## COGLES2Solid.vsh

```glsl
#define MAX_LIGHTS 8 // 最多的光源数

/* Attributes */

attribute vec3 inVertexPosition; // 顶点坐标
attribute vec3 inVertexNormal; // 顶点法线
attribute vec4 inVertexColor; // 顶点颜色
attribute vec2 inTexCoord0; // 纹理坐标

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
varying vec4 vVertexColor; // 顶点颜色
varying vec4 vSpecularColor; // 镜面反射颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

// 平行光，也就是 方向光。Blinn-Phong 光照模型。
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

// 点光源。
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

// 聚光源，即手电筒光，没有实现。
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

    vVertexColor = inVertexColor.bgra;
    vSpecularColor = vec4(0.0, 0.0, 0.0, 0.0);

    vec3 Position = (uWVMatrix * vec4(inVertexPosition, 1.0)).xyz;

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
```


## COGLES2Solid.fsh

```glsl
precision mediump float;

/* Uniforms */

uniform int uTextureUsage0; // 是否采用纹理
uniform sampler2D uTextureUnit0; // 纹理单元
uniform int uFogEnable; // 是否雾
uniform int uFogType; // 雾的类型
uniform vec4 uFogColor; // 雾的颜色
uniform float uFogStart; // 雾的开始 Linear FogType
uniform float uFogEnd; // 雾的结束 Linear FogType
uniform float uFogDensity; // 雾的密度

/* Varyings */

varying vec2 vTextureCoord0; // 纹理坐标
varying vec4 vVertexColor; // 顶点颜色
varying vec4 vSpecularColor; // 镜面反射颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

float computeFog()
{
    const float LOG2 = 1.442695;
    float FogFactor = 0.0;

    if (uFogType == 0) // Exp
    {
        FogFactor = exp2(-uFogDensity * vFogCoord * LOG2);
    }
    else if (uFogType == 1) // Linear
    {
        float Scale = 1.0 / (uFogEnd - uFogStart);
        FogFactor = (uFogEnd - vFogCoord) * Scale;
    }
    else if (uFogType == 2) // Exp2
    {
        FogFactor = exp2(-uFogDensity * uFogDensity * vFogCoord * vFogCoord * LOG2);
    }

    FogFactor = clamp(FogFactor, 0.0, 1.0);

    return FogFactor;
}

void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage0))
        Color *= texture2D(uTextureUnit0, vTextureCoord0);
    Color += vSpecularColor;

    if (bool(uFogEnable))
    {
        float FogFactor = computeFog();
        vec4 FogColor = uFogColor;
        FogColor.a = 1.0;
        Color = mix(FogColor, Color, FogFactor);
    }

    gl_FragColor = Color;
}
```


## COGLES2Solid2.vsh

在 COGLES2Solid.vsh 的基础上，增加了一个纹理。

```glsl
attribute vec2 inTexCoord1; // 纹理坐标 2
uniform mat4 uTMatrix1; // 纹理矩阵 2
varying vec2 vTextureCoord1; // 纹理坐标 2

void main()
{
    vec4 TextureCoord1 = vec4(inTexCoord1.x, inTexCoord1.y, 1.0, 1.0);
    vTextureCoord1 = vec4(uTMatrix1 * TextureCoord1).xy;
}
```


## COGLES2Solid2Layer.fsh

在 COGLES2Solid.fsh 的基础上，增加了一个纹理。根据顶点的颜色 alpha 通道混合。

```glsl
void main()
{
    vec4 Color0 = vec4(1.0, 1.0, 1.0, 1.0);
    vec4 Color1 = vec4(1.0, 1.0, 1.0, 1.0);

    if (bool(uTextureUsage0))
        Color0 = texture2D(uTextureUnit0, vTextureCoord0);

    if (bool(uTextureUsage1))
        Color1 = texture2D(uTextureUnit1, vTextureCoord1);

    vec4 FinalColor = (Color0 * vVertexColor.a + Color1 * (1.0 - vVertexColor.a)) * vVertexColor;
    FinalColor += vSpecularColor;
}
```
