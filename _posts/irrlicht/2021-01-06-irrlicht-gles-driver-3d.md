---
layout: post
title: "Irrlicht 3D 笔记 -- OpenGL ES 2.x Driver 源码剖析 3D 部分"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
cluster: "Irrlicht OpenGL-ES2 Driver"
---

Irrlicht 采用了标准的 Blinn-Phong 光照模型。但是它是在 顶点着色器 里面计算的光照，这样更解决 GPU，相比放在片段着色器里面计算，光照效果更生硬。

Irrlicht 总体说来还是比较简陋。主要包含 Blinn-Phong 光照模型，反射、天空盒、法线纹理、视差纹理等等。


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
            if ( i >= uLightCount )    // can't use uniform as loop-counter directly in glsl
                break;
            if (uLightType[i] == 0)
                pointLight(i, Position, Normal, Ambient, Diffuse, vSpecularColor);
        }

        for (int i = 0; i < int(MAX_LIGHTS); i++)
        {
            if ( i >= uLightCount )
                break;
            if (uLightType[i] == 1)
                spotLight(i, Position, Normal, Ambient, Diffuse, vSpecularColor);
        }

        for (int i = 0; i < int(MAX_LIGHTS); i++)
        {
            if ( i >= uLightCount )
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


## COGLES2LightmapAdd.fsh

跟 COGLES2Solid2Layer.fsh 一样，只是颜色混合方式不太一样。

```glsl
void main()
{
    vec4 FinalColor = (Color0 + Color1) * vVertexColor + vSpecularColor;
}
```


## COGLES2LightmapModulate.fsh

跟 COGLES2Solid2Layer.fsh 一样，只是颜色混合方式不太一样。

```glsl
void main()
{
    vec4 FinalColor = (Color0 * Color1 * uModulate) * vVertexColor + vSpecularColor;
}
```


## COGLES2DetailMap.fsh

跟 COGLES2Solid2Layer.fsh 一样，只是颜色混合方式不太一样。

```glsl
void main()
{
    vec4 FinalColor = vec4(Color0 + (Color1 - 0.5)) * vVertexColor + vSpecularColor;
}
```


## COGLES2SphereMap.vsh

主要用于天空盒贴图。和 COGLES2Solid.vsh 得主要不同是：

```glsl
void main()
{
    vec3 Position = (uWVMatrix * vec4(inVertexPosition, 1.0)).xyz;

    vec3 P = normalize(Position);
    vec3 N = normalize(vec4(uNMatrix * vec4(inVertexNormal, 0.0)).xyz);
    vec3 R = reflect(P, N);

    float V = 2.0 * sqrt(R.x*R.x + R.y*R.y + (R.z+1.0)*(R.z+1.0));
    vTextureCoord0 = vec2(R.x/V + 0.5, R.y/V + 0.5);
}
```


## COGLES2SphereMap.fsh

代码和 COGLES2Solid.fsh 完全一样。


## COGLES2Reflection2Layer.fsh

代码在 COGLES2Solid2.vsh 的基础上，纹理 2 采用反射得到：

```glsl
void main()
{
    vec3 Position = (uWVMatrix * vec4(inVertexPosition, 1.0)).xyz;
    vec3 P = normalize(Position);
    vec3 N = normalize(vec4(uNMatrix * vec4(inVertexNormal, 0.0)).xyz);
    vec3 R = reflect(P, N);

    float V = 2.0 * sqrt(R.x*R.x + R.y*R.y + (R.z+1.0)*(R.z+1.0));
    vTextureCoord1 = vec2(R.x/V + 0.5, R.y/V + 0.5);
}
```


## COGLES2Reflection2Layer.vsh

```glsl
void main()
{
    vec4 FinalColor = (Color0 * Color1) * vVertexColor + vSpecularColor;
}
```


## COGLES2TransparentVertexAlpha.fsh

乘上纹理的值。

```glsl
void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage0))
        Color *= texture2D(uTextureUnit0, vTextureCoord0);
    Color += vSpecularColor;
}
```


## COGLES2TransparentAlphaChannelRef.fsh

乘上纹理的值，小于 uAlphaRef 就抛弃。

```glsl
void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage0))
        Color *= texture2D(uTextureUnit0, vTextureCoord0);

    if (Color.a < uAlphaRef)
        discard;

    Color += vSpecularColor;
}
```


## COGLES2TransparentAlphaChannel.fsh

和上面一个区别是，乘上纹理的值，uTextureUsage0 并且小于 uAlphaRef 就抛弃。

```glsl
void main()
{
    vec4 Color = vVertexColor;

    if (bool(uTextureUsage0))
    {
        Color *= texture2D(uTextureUnit0, vTextureCoord0);

        // TODO: uAlphaRef should rather control sharpness of alpha, don't know how to do that right now and this works in most cases.
        if (Color.a < uAlphaRef)
            discard;
    }
    Color += vSpecularColor;
}
```


## COGLES2NormalMap.vsh

```glsl
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
```


## COGLES2NormalMap.fsh

实体法线图渲染器。第一个图为纹理图，第二个图为法线图。
只有当顶点是 S3DVertexTangents(EVT_TANGENTS) 格式才可以使用这种材质。
可以使用 `IMeshManipulator::createMeshWithTangent()` 将任何网格转换成所需格式。
[Irrlicht 学习笔记 (10)--PerPixelLighting](http://www.voidcn.com/article/p-ncwwekol-bad.html)

```glsl
#define MAX_LIGHTS 2 // 最多两个光源

precision mediump float;

/* Uniforms */

uniform sampler2D uTextureUnit0; // 纹理单元
uniform sampler2D uTextureUnit1; // 纹理单元 2
uniform int uFogEnable; // 是否雾
uniform int uFogType; // 雾的类型
uniform vec4 uFogColor; // 雾的颜色
uniform float uFogStart; // 雾的开始 Linear FogType
uniform float uFogEnd; // 雾的结束 Linear FogType
uniform float uFogDensity; // 雾的密度

/* Varyings */

varying vec2 vTexCoord; // 纹理坐标
varying vec3 vLightVector[MAX_LIGHTS]; // 光源向量
varying vec4 vLightColor[MAX_LIGHTS]; // 光源颜色
varying float vFogCoord; // 雾的厚度，可以理解为深度。

void main()
{
    vec4 Color  = texture2D(uTextureUnit0, vTexCoord);
    vec3 Normal = texture2D(uTextureUnit1, vTexCoord).xyz *  2.0 - 1.0;

    vec4 FinalColor = vec4(0.0, 0.0, 0.0, 0.0);

    for (int i = 0; i < int(MAX_LIGHTS); i++)
    {
        vec3 LightVector = normalize(vLightVector[i]);

        float Lambert = max(dot(LightVector, Normal), 0.0);
        FinalColor += vec4(Lambert) * vLightColor[i];
    }

    FinalColor *= Color;
    FinalColor.w = vLightColor[0].w;

    if (bool(uFogEnable)) ...

    gl_FragColor = FinalColor;
}
```


## COGLES2ParallaxMap.vsh

视差贴图。法线贴图可以在低面片数的模型上表现出高面片数模型的很多细节。
法线贴图并不是把模型的面数提高了，而是使用法线贴图中的法线来计算光照，通过明暗效果作假，让观察者误以为模型有凹凸。
法线贴图只能在明暗效果上作假（模拟凹凸），无法控制表面的凹凸程度。
即使我们使用图像软件强制调出一个凹凸相对明显的法线贴图，但正如为什么要引入视差贴图？中的两个图，法线贴图下的凹凸效果明显真实感不高！

相比法线贴图，多点相机位置。

```glsl
uniform vec3 uEyePosition; // 相机坐标
varying vec3 vEyeVector; // 相机向量

void main()
{
    vec3 EyeVector = uEyePosition - inVertexPosition;

    vEyeVector.x = dot(inVertexTangent, EyeVector);
    vEyeVector.y = dot(inVertexBinormal, EyeVector);
    vEyeVector.z = dot(inVertexNormal, EyeVector);
    vEyeVector *= vec3(1.0, -1.0, -1.0);
}
```


## COGLES2ParallaxMap.fsh

和 EMT_NORMAL_MAP_SOLID 差不多，只是只有的是 parallax 图，更加真实。
第一个图为纹理图，第二个图为法线图 (32bits)（高度图）。
法线图纹理需要在其透明度通道中包含高度信息，高度信息可以通过函数 IVideoDriver::makeNormalMapTexture 自动设置，
函数参数：第一个纹理图（其 alpha 通道可改变），第二个 amplitude 缩放比例。

关键代码只有两行，主要是微调一下纹理采样的坐标，偏移 `EyeVector.xy * TempFetch.w` 模拟：

```glsl
vec3 EyeVector = normalize(vEyeVector);
vec2 TexCoord = EyeVector.xy * TempFetch.w + vTexCoord;
```

在 COGLES2NormalMap.fsh 的基础上，多点点代码。

```glsl
uniform float uFactor; // 纹理颜色的乘积参数
varying vec3 vEyeVector; // 相机向量

void main()
{
    vec4 TempFetch = texture2D(uTextureUnit1, vTexCoord) *  2.0 - 1.0;
    TempFetch *= uFactor;

    vec3 EyeVector = normalize(vEyeVector);
    vec2 TexCoord = EyeVector.xy * TempFetch.w + vTexCoord;

    // vec4 Color  = texture2D(uTextureUnit0, vTexCoord);
    vec4 Color  = texture2D(uTextureUnit0, TexCoord);
    // vec3 Normal = texture2D(uTextureUnit1, vTexCoord).xyz *  2.0 - 1.0;
    vec3 Normal = texture2D(uTextureUnit1, TexCoord).xyz *  2.0 - 1.0;
}
```


## COGLES2OneTextureBlend.fsh

主要是根据纹理参数，决定混合参数。
$$BlendFunc = source * sourceFactor + dest * destFactor ( E\_BLEND\_FUNC )$$

The blend function is set to SMaterial::MaterialTypeParam with pack_textureBlendFunc (for 2D) or pack_textureBlendFuncSeparate (for 3D).

```glsl
uniform int uBlendType; // 混合类型，采用 Color0/Color1

void main()
{
    vec4 Color0 = vVertexColor;
    vec4 Color1 = vec4(1.0, 1.0, 1.0, 1.0);

    if (bool(uTextureUsage0))
        Color1 = texture2D(uTextureUnit0, vTextureCoord0);

    vec4 FinalColor = Color0 * Color1;
    FinalColor += vSpecularColor;

    if (uBlendType == 1)
    {
        FinalColor.w = Color0.w;
    }
    else if (uBlendType == 2)
    {
        FinalColor.w = Color1.w;
    }

    if (bool(uFogEnable)) ...

    gl_FragColor = FinalColor;
}
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-06-irrlicht-gles-driver-3d.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.voidcn.com/article/p-ncwwekol-bad.html]({% include relrefx.html url="/backup/2021-01-06-irrlicht-gles-driver-3d.md/www.voidcn.com/b445f1f6.html" %})
