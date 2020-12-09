---
layout: post
title: "“特效编程”笔记 -- 计算机图形学 OPENGL / 冯氏光照模型"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
---

<https://ke.qq.com/course/package/25480?flowToken=1019441>

本文源码 <a href="{% include gitsrc.html url="/source/shader/LearnOpenGL-Lighting" %}" target="_blank">LearnOpenGL-Lighting</a>

{% include image.html url="/images/OpenGL-GLSL/glLightingGrab.gif" %}


## OpenGL 光照

冯氏光照模型的主要结构由 3 个分量组成：环境 (Ambient)、漫反射 (Diffuse) 和镜面 (Specular) 光照。

**环境光照 (Ambient Lighting)**：物体几乎永远不会是完全黑暗的。所以环境光照一般是个常量。

**漫反射光照 (Diffuse Lighting)**：模拟光源对物体的方向性影响，物体的某一部分越是正对着光源，它就会越亮。

**镜面光照 (Specular Lighting)**：模拟有光泽物体上面出现的亮点。镜面光照的颜色相比于物体的颜色会更倾向于光的颜色。

$$
I_p=k_ai_a+\sum_{m{\in}\mathrm{lights}}{(k_d(\hat{L}_m\cdot\hat{N})i_{m,d})+k_s(\hat{R}_m\cdot\hat{V})^{\alpha}i_{m,s})}
$$

{% include image.html url="/images/OpenGL-GLSL/v2-7d9cb4f3c58bce1dd41c43902284f7d4_720w.jpg" %}

{% include image.html url="/images/OpenGL-GLSL/20201209104409.png" %}

- 基础光照原理讲解

- 创建一个光照场景

- 冯氏光照基础效果实现

- 材质 & 光属性

- 光照贴图

- 平行光与点光源

- 聚光手电筒效果

- 多光源 shader 函数封装


## 坐标关系

模型、视图、投影矩阵 model view projection

```glsl
gl_Position = projection * view * model * vec4(position, 1.0);
```

多个光源，采用合并结果。

```glsl
void main()
{
    // 属性
    vec3 norm = normalize(Normal);
    vec3 viewDir = normalize(viewPos - FragPos);

    // 第一阶段：定向光照
    vec3 result = CalcDirLight(dirLight, norm, viewDir);
    // 第二阶段：点光源
    for(int i = 0; i < NR_POINT_LIGHTS; i++)
        result += CalcPointLight(pointLights[i], norm, FragPos, viewDir);
    // 第三阶段：聚光
    //result += CalcSpotLight(spotLight, norm, FragPos, viewDir);

    FragColor = vec4(result, 1.0);
}
```


### 光源

顶点着色器。

```glsl
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
```

片段着色器。

```glsl
#version 400 core
out vec4 FragColor;
in vec2 TexCoord;
uniform vec3 lightColor;

void main()
{
    FragColor = vec4(1.0,1.0,1.0,1.0);
}
```


### 模型物体

顶点着色器。

```glsl
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
```

片段着色器。

先定义几个数据结构。

```glsl
// 材质
struct Material {
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
    float shininess;
};

// 聚光灯
struct SpotLight {
    vec3 position;
    vec3 direction;
    float cutOff; // 内圈
    float outerCutOff; // 外圈

    vec3 ambient;
    vec3 diffuse;
    vec3 specular;

    float constant;
    float linear;
    float quadratic;
};

struct Light {

    vec4 lightDir; // 光方向

    vec3 ambient;
    vec3 diffuse;
    vec3 specular;

    float constant;
    float linear;
    float quadratic;
};
```

```glsl
#version 400 core
out vec4 FragColor;
in vec3 Normal; // 法线向量
in vec3 FragPos; // 模型坐标
in vec2 TexCoords; // 纹理坐标
uniform sampler2D ourTexture1; // 纹理 1
uniform sampler2D ourTexture2; // 纹理 2
uniform vec3 lightColor;
uniform vec3 objectColor;
uniform vec4 lightPos;
uniform vec3 viewPos; // camera
uniform vec3 front; // camera

Material material;
Light light;
SpotLight spotLight;
vec3 CalcPointLight(Light light);
vec3 CalcSpotLight(SpotLight light);

void main()
{
    // 材质参数
    material.ambient=vec3(texture(ourTexture1,TexCoords));
    material.diffuse=vec3(texture(ourTexture1,TexCoords));
    material.specular=vec3(texture(ourTexture2,TexCoords));
    material.shininess=32;

    // 聚光灯参数
    spotLight.position=viewPos;
    spotLight.direction=front;
    spotLight.outerCutOff=3.5;
    spotLight.cutOff=2.5;

    spotLight.constant=0;
    spotLight.linear=0.09;
    spotLight.quadratic=0.032;
    spotLight.ambient=vec3(0.0,0.0,0.0);
    spotLight.diffuse=vec3(1.0,1.0,1.0);
    spotLight.specular=vec3(1.0,1.0,1.0);

    // 点光源参数
    light.lightDir=lightPos;

    light.constant=1.0;
    light.linear=0.09;
    light.quadratic=0.032;
    light.ambient=vec3(0.2,0.2,0.2);
    light.diffuse=vec3(0.6,0.6,0.6);
    light.specular=vec3(1.0,1.0,1.0);

    // 最终颜色叠加
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
    // 光线衰减
    float attenuation=1.0/(light.constant+light.linear*distance+light.quadratic*distance*distance);
    // 计算 漫反射光照
    float diffuse=max(dot(Normal,lightDir),0.0);

    vec3 viewDir=normalize(viewPos-FragPos);
    vec3 reflectDir=reflect(-lightDir,Normal);
    // 计算 镜面光照
    float specular=pow(max(dot(reflectDir,viewDir),0.0),material.shininess);

    vec3 result=vec3(0.0,0.0,0.0);
    // 冯氏光照模型
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
    spotI=clamp((theta-cos(radians(light.outerCutOff)))/epsilon,0.0,1.0); // 聚光灯亮度

    vec3 lightDir;
    float distance;
    lightDir=-light.direction;
    distance=length(vec3(light.position)-FragPos);

    // 光线衰减
    float attenuation=1.0/(light.constant+light.linear*distance+light.quadratic*distance*distance);
    // 计算 漫反射光照
    float diffuse=max(dot(Normal,lightDir),0.0);

    vec3 viewDir=normalize(viewPos-FragPos);
    vec3 reflectDir=reflect(-lightDir,Normal);
    // 计算 镜面光照
    float specular=pow(max(dot(reflectDir,viewDir),0.0),material.shininess);

    vec3 result=vec3(0.0,0.0,0.0);
    // 冯氏光照模型
    result = (light.ambient*material.ambient+
        diffuse*light.diffuse*material.diffuse+
        specular*light.specular*material.specular)*lightColor*attenuation*spotI;

    return result;
}
```


## 参考资料

- [1] [冯氏光照模型](https://blog.csdn.net/zhaoyin214/article/details/81625964)
- [2] [冯氏光照模型 简书](https://www.jianshu.com/p/bc384e81d590)
- [3] [其它源码](https://learnopengl.com/code_viewer_gh.php?code=src/2.lighting/6.multiple_lights/multiple_lights.cpp)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://ke.qq.com/course/package/25480?flowToken=1019441]({% include relref.html url="/backup/2020-12-09-shader-OpenGL-Lighting.md/ke.qq.com/3fd1c97a.html" %})
- [2] [https://blog.csdn.net/zhaoyin214/article/details/81625964]({% include relref.html url="/backup/2020-12-09-shader-OpenGL-Lighting.md/blog.csdn.net/f8bddaa8.html" %})
- [3] [https://www.jianshu.com/p/bc384e81d590]({% include relref.html url="/backup/2020-12-09-shader-OpenGL-Lighting.md/www.jianshu.com/5a656440.html" %})
- [4] [https://learnopengl.com/code_viewer_gh.php?code=src/2.lighting/6.multiple_lights/multiple_lights.cpp]({% include relref.html url="/backup/2020-12-09-shader-OpenGL-Lighting.md/learnopengl.com/f55884a3.php" %})
