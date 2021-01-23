---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 高级光照 阴影 shadowMapping"
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
codeprint:
cluster: "LearnOpenGL"
---

又花了一天时间，终于把这玩意彻底弄通透了。阴影计算过程，先切换到光源视角，此时应该是看不到任何阴影的，保存此时的深度值，然后再切换到相机视角，每个坐标都可以换算到刚才的光源视角空间，用刚才保存的深度值辅助判断当前坐标是否在阴影内。能发明这个算法的人肯定是个小天才。[哇][哇]


## shadowMapping

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_theory_spaces.png" %}

阴影是怎么算出来的？
通过移动视口到光源位置，可以观察到这个位置每个东西都是明亮的，因为从光的角度来看是没有阴影的。
从光源的角度将场景的深度渲染到一张深度缓冲区中，我们可以在场景中获得一张阴影贴图，真正绘制的时候根据其深度值判断是否在阴影中。

高级光照阴影 ShadowMapping，实在没看透彻，源码抄了一遍，才透彻了。**这一章节应该是到目前为止最难的了。**[原文 {% include relref_github.html %}](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/) 写的非常好，就是有点难懂。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_theory.webp" %}


## 详解

从光源处得到的深度图片，越近越黑，越远越白。最下面纯白，是没有任何绘制的边界了。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/20201224121704.png" %}

**正常绘制阴影的时候，要换算到阴影的空间坐标，取数值。**最开始没看懂的关键，也是这个地方。

```cpp
glViewport(0, 0, SCR_WIDTH, SCR_HEIGHT); // 要重新调整视口
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
shader.use();
glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
glm::mat4 view = camera.GetViewMatrix();
shader.setMat4("projection", projection);
shader.setMat4("view", view);
// set light uniforms
shader.setVec3("viewPos", camera.Position);
shader.setVec3("lightPos", lightPos);
shader.setMat4("lightSpaceMatrix", lightSpaceMatrix);
glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, woodTexture);
glActiveTexture(GL_TEXTURE1);
glBindTexture(GL_TEXTURE_2D, depthMap);
renderScene(shader);
```

这儿的新的地方是 FragPosLightSpace 这个输出向量。我们用同一个 lightSpaceMatrix，把世界空间顶点位置转换为光空间。顶点着色器传递一个普通的经变换的世界空间顶点位置 vs_out.FragPos 和一个光空间的 vs_out.FragPosLightSpace 给片段着色器。

```glsl
vs_out.FragPos = vec3(model * vec4(aPos, 1.0));
vs_out.FragPosLightSpace = lightSpaceMatrix * vec4(vs_out.FragPos, 1.0);

float shadow = ShadowCalculation(fs_in.FragPosLightSpace);
float ShadowCalculation(vec4 fragPosLightSpace)
{
    // perform perspective divide
    vec3 projCoords = fragPosLightSpace.xyz / fragPosLightSpace.w;
    // transform to [0,1] range
    projCoords = projCoords * 0.5 + 0.5;
    // get closest depth value from light's perspective (using [0,1] range fragPosLight as coords)
    float closestDepth = texture(shadowMap, projCoords.xy).r;
    // get depth of current fragment from light's perspective
    float currentDepth = projCoords.z;
    // check whether current frag pos is in shadow
    float shadow = currentDepth > closestDepth  ? 1.0 : 0.0;

    return shadow;
}
```

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_base.webp" %}

这个效果存在很大的问题。**阴影失真 (Shadow Acne)** 造成这个问题的原因是浮点数计算误差，黑色条纹是被误认为阴影的。
里面的大量锯齿，差不多也是 浮点精度不够，倾斜，深度缓冲尺寸不够大 三个组合原因。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/shadow_mapping_acne_diagram.png" %}

```glsl
// 相当于根据倾斜程度，把阴影深度变浅了。
// calculate bias (based on depth map resolution and slope)
vec3 normal = normalize(fs_in.Normal);
vec3 lightDir = normalize(lightPos - fs_in.FragPos);
float bias = max(0.05 * (1.0 - dot(normal, lightDir)), 0.005);
// check whether current frag pos is in shadow
float shadow = currentDepth - bias > closestDepth  ? 1.0 : 0.0;
```

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/20201224155520.png" %}

远处还有黑色的阴影，那是因为超出了 深度缓冲的尺寸边界。

```cpp
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER);
GLfloat borderColor[] = { 1.0, 1.0, 1.0, 1.0 };
glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, borderColor);
```

```glsl
float ShadowCalculation(vec4 fragPosLightSpace)
{
    [...]
    if(projCoords.z > 1.0)
        shadow = 0.0;

    return shadow;
}
```


## 更高级形式

点光源阴影，生成深度立方体贴图。

{% include image.html url="/assets/images/201224-shader-opengl-lighting-~55/point_shadows.png" %}


## Refs

- [1] [Shadow Mapping](https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping)
- [2] [阴影映射 {% include relref_github.html %}](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/)

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-23: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://learnopengl-cn.github.io/05%20Advanced%20Lighting/03%20Shadows/01%20Shadow%20Mapping/]({% include relref.html url="/backup/2020-12-24-shader-OpenGL-Lighting-Advanced-shadowMapping.md/learnopengl-cn.github.io/43cc6489.html" %})
- [https://learnopengl.com/Advanced-Lighting/Shadows/Shadow-Mapping]({% include relref.html url="/backup/2020-12-24-shader-OpenGL-Lighting-Advanced-shadowMapping.md/learnopengl.com/296bb720.html" %})
