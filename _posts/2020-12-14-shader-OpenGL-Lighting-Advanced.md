---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 高级光照 Blinn-Phong & 阴影"
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

无意中看到一篇文章 “Real Shading in Unreal Engine 4”，还是 13 年的。要实现一个好的光照模型究竟有多难。
<a href="{% include relref.html url="/source/2013SiggraphPresentationsNotes-26915738.pdf" %}" target="_blank">2013SiggraphPresentationsNotes-26915738.pdf</a>
[from](https://de45xmedrsdbp.cloudfront.net/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf)


## 冯氏光照模型的不足

* 在镜面光分量上，当视线与反射光向量夹角大于 90° 时，镜面光值将会变为 0，在反光度非常小的情况下，会产生较明显的边界情况。

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_over_90.png" caption="镜面光临界情况" %}


## Blinn-Phong 光照

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_halfway_vector.png" caption="镜面光临界情况" %}

* Blinn-Phong 光照模型是建立在冯氏光照模型的基础上对镜面光计算进行修改的算法，Blinn-Phong 模型不再依赖于反射向量，而是采用了半程向量 (Halfway Vector)，
即光线与视线夹角一半方向上的一个单位向量。当半程向量与法线向量越接近时，镜面光分量就越大。
* 当视线正好与反射向量对齐时，半程向量就会与法线完美契合。所以当观察者视线越接近于原本反射光线的方向时，镜面高光就会越强。
* 现在，不论观察者向哪个方向看，半程向量与表面法线之间的夹角都不会超过 90 度（除非光源在表面以下）。它产生的效果会与冯氏光照有些许不同，但是大部分情况下看起来会更自然一点，特别是低高光的区域。Blinn-Phong 着色模型正是早期固定渲染管线时代时 OpenGL 所采用的光照模型。
* 获取半程向量的方法很简单，只需要将光线的方向向量和观察向量加到一起，并将结果正规化 (Normalize) 就可以了：
    $$\vec H = \frac{\vec L + \vec V}{||\vec L + \vec V||}$$
* 除此之外，冯氏模型与 Blinn-Phong 模型也有一些细微的差别：半程向量与表面法线的夹角通常会小于观察与反射向量的夹角。所以，如果你想获得和冯氏着色类似的效果，就必须在使用 Blinn-Phong 模型时将镜面反光度设置更高一点。通常我们会选择冯氏着色时反光度分量的 2 到 4 倍。

```glsl
vec3 lightDir   = normalize(lightPos - FragPos);
vec3 viewDir    = normalize(viewPos - FragPos);
vec3 halfwayDir = normalize(lightDir + viewDir);

float spec = pow(max(dot(normal, halfwayDir), 0.0), shininess);
vec3 specular = lightColor * spec;
```

```glsl
void main()
{
    [...]
    float spec = 0.0;
    if(blinn)
    {
        vec3 halfwayDir = normalize(lightDir + viewDir);
        spec = pow(max(dot(normal, halfwayDir), 0.0), 16.0);
    }
    else
    {
        vec3 reflectDir = reflect(-lightDir, normal);
        spec = pow(max(dot(viewDir, reflectDir), 0.0), 8.0);
    }
}
```

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_comparrison.png" caption="模型效果比较" %}


## gamma 校正原理

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/gamma_correction_gamma_curves.png" %}

Gamma 校正是一个**上拱**的过程。

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/gamma_correction_example.png" %}


## shadowMapping

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/shadow_mapping_theory_spaces.png" %}

通过移动视口到光源位置，可以观察到这个位置每个东西都是明亮的，因为从光的角度来看是没有阴影的。
从光源的角度将场景的深度渲染到一张深度缓冲区中，我们可以在场景中获得一张阴影或者无阴影的贴图，一张阴影贴图。

高级光照阴影 ShadowMapping，实在没看透彻，源码抄了一遍，才透彻了。能感受到暴力美学。
***[<font color="red">高级光照阴影 ShadowMapping /blog/2020/12/24/shader-OpenGL-Lighting-Advanced-shadowMapping</font>]({% include relref.html url="/blog/2020/12/24/shader-OpenGL-Lighting-Advanced-shadowMapping" %})***

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/shadow_mapping_theory.webp" %}


## Point Shadows 帧缓冲深度附件


## Point Shadows 渲染阴影


## 法线图贴

伴随矩阵 (Adjugate Matrix)：

$$
\begin{bmatrix} T_x & T_y & T_z \\ B_x & B_y & B_z \end{bmatrix}  = \frac{1}{\Delta U_1 \Delta V_2 - \Delta U_2 \Delta V_1} \begin{bmatrix} \Delta V_2 & -\Delta V_1 \\ -\Delta U_2 & \Delta U_1 \end{bmatrix} \begin{bmatrix} E_{1x} & E_{1y} & E_{1z} \\ E_{2x} & E_{2y} & E_{2z} \end{bmatrix}
$$


## Parallax Mapping 视差贴图


## Steep Parallax Mapping


## HDR


## Bloom

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/bloom.png" %}


## deferred shading 延迟渲染

目前我们看到最终画面都是 2D 的，只能看到有限的像素数，理论上我们只要处理（指光照，阴影处理）最终我们可以看到的点的效果就够了，
多余的处理是浪费的。而正常的前向渲染 (Forward Shading) 流程是把空间的点进行各种剪裁后，进行处理，所处理量远远大于我们最终看到的。
所以延迟渲染出现了。它先将摄像机空间的点光栅化转化成屏幕坐标后再进行处理。这样就能减少处理的次数，从而提高效率。

> 我一直认为，延迟渲染跟阴影，是图形学的一个分水岭。能深刻的理解了延迟渲染、阴影，那么至少图形学算是入门了，至少对渲染架构，渲染的一些基本算法，入门了，不再是门外汉了。[延迟渲染 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/102134614)

延时其实指的是在渲染场景之后，再来进行光照计算，也就是延时光照计算在后期进行，
正向渲染的着色器采取物体 + 光照同时进行计算，也就是在渲染物体的时候，直接利用物体的物质，法线和颜色进行光照计算；
而延时渲染，是先渲染场景，在 G-buffer 中存储光照计算所需要的数据。[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_41286360/article/details/102794290)

```cpp
/**
延迟渲染主要步骤：
1. 几何处理阶段；
2. 光照处理阶段；
*/
int main() {
    // G-buffer 的创建
    unsigned int gBuffer;
    glGenFramebuffers(1, &gBuffer);
    glBindFramebuffer(GL_FRAMEBUFFER, gBuffer);

    unsigned int gPosition, gNormal, gAlbedoSpec;
    // position - 位置信息
    // normal - 法线信息
    // albedospec - 颜色信息

    // 深度附件

    // MRT-Multiple Render Targets 多渲染目标技术
    unsigned int attachments[3] = { GL_COLOR_ATTACHMENT0,GL_COLOR_ATTACHMENT1,GL_COLOR_ATTACHMENT2 };
    glDrawBuffers(3, attachments);

    // 多光源
    // 渲染步骤
    while (!glfwWindowShouldClose(window)) {
        // 几何处理阶段

        // 光照处理阶段

        renderQuad();
        if (LightBox)
        {
            // 绘制光源
        }

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}

// 绘制铺满整个屏幕的矩形
unsigned int quadVAO = 0;
unsigned int quadVBO;
void renderQuad() {
}
```


### g-buffer.fs

```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec2 aTexCoords;

out vec3 FragPos;
out vec2 TexCoords;
out vec3 Normal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    vec4 worldPos = model * vec4(aPos, 1.0);
    FragPos = worldPos.xyz;
    TexCoords = aTexCoords;

    mat3 normalMatrix = transpose(inverse(mat3(model)));
    Normal = normalMatrix * aNormal;

    gl_Position = projection * view * worldPos;
}
```


### g-buffer.vs

```glsl
#version 330 core
layout (location = 0) out vec3 gPosition;
layout (location = 1) out vec3 gNormal;
layout (location = 2) out vec4 gAlbedoSpec;

in vec2 TexCoords;
in vec3 FragPos;
in vec3 Normal;

uniform sampler2D texture_diffuse1;

void main()
{
    gPosition = FragPos;
    gNormal = normalize(Normal);
    gAlbedoSpec.rgb = texture(texture_diffuse1, TexCoords).rgb;
}
```


### deferred_shading.vs

```glsl
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoords;

out vec2 TexCoords;

void main()
{
    TexCoords = aTexCoords;
    gl_Position = vec4(aPos, 1.0);
}
```


### deferred_shading.fs

```glsl
#version 330 core
out vec4 FragColor;

in vec2 TexCoords;

uniform sampler2D gPosition;
uniform sampler2D gNormal;
uniform sampler2D gAlbedoSpec;
uniform float num;

struct Light {
    vec3 Position;
    vec3 Color;
};
const int NR_LIGHTS = 50;
uniform Light lights[NR_LIGHTS];
uniform vec3 viewPos;

void main()
{
    // 从 G-buffer 中提取数据
    vec3 FragPos = texture(gPosition, TexCoords).rgb;
    vec3 Normal = texture(gNormal, TexCoords).rgb;
    vec3 Diffuse = texture(gAlbedoSpec, TexCoords).rgb;
    float Specular = 1.0f;

    // 光照计算
    vec3 lighting = Diffuse * 0.9;
    vec3 viewDir = normalize(viewPos - FragPos);
    for(int i = 0; i < NR_LIGHTS; ++i)
    {
        // 环境光
        vec3 ambient = Diffuse * 0.01;
        // 漫反射
        vec3 lightDir = normalize(lights[i].Position - FragPos);
        vec3 diffuse = max(dot(Normal, lightDir), 0.0) * Diffuse * lights[i].Color;
        // 镜面高光
        vec3 halfwayDir = normalize(lightDir + viewDir);
        float spec = pow(max(dot(Normal, halfwayDir), 0.0), 16.0);
        vec3 specular = lights[i].Color * spec * Specular;

        lighting += ambient + diffuse + specular;
    }
    FragColor = vec4(lighting/num, 1.0);
}
```

[Deferred Shading（延迟渲染） {% include relref_cnblogs.html %}](https://www.cnblogs.com/wangchengfeng/p/3440097.html)


### 延时渲染的缺点

* 不可以用混合技术，因此透明对象无法渲染。
* 没法实现基于硬件实现的多重采样抗锯齿功能；因为渲染过程发生在上面的第二步，第二步只有一个样本，
    但是基于硬件实现的多重采样抗锯齿需要多个样本。
* 需要高带宽的显卡。
* 显卡不支持 mrt（multi render target）技术，还可以实现延时渲染吗？可以做，可以通过建立三个帧缓冲，分别存储位置，法线和延时信息，
    渲染三次场景提取信息并存储在三个附件中，但是不建议，这样显卡的负担会很大。


## 屏幕空间环境光屏蔽 SSAO

屏幕空间环境光遮蔽 (Screen-Space Ambient Occlusion, SSAO)。
在 2007 年，Crytek 公司发布了一款叫做屏幕空间环境光遮蔽 (Screen-Space Ambient Occlusion, SSAO) 的技术，并用在了他们的看家作孤岛危机上。

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/ssao_overview.png" %}


## X-ray 图像模拟

* <https://www.ndt.net/article/wcndt00/papers/idn256/idn256.htm>
* [X-ray 图像模拟（Simulation of X-Ray NDT Imaging Techniques） {% include relref_cnblogs.html %}](https://www.cnblogs.com/kalluwa/p/7092532.html)

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/20210104160558.png" %}


## Metaballs - Quintic

Metaball。纯 Shader 实现，代码只有 200 多行，满满的数学知识。

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/preview0.webp" %}
{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/preview1.webp" %}
{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/preview2.webp" %}

* https://www.shadertoy.com/view/XssXDl
* https://www.shadertoy.com/view/ld2GRz
* https://github.com/millsvonmilski/Unity3D_RayMarching_MetaBall

Bounded metaballs with quintic falloff.
Literature often recommends cubic (smoothstep) falloffs (rather than exponential or 1/dÂ²) for they are bounded.
However they produce discontinuities in normals/lighting.
Quintic falloffs solves the problem.


## FurEffect

[SoftPixel Engine](http://softpixelengine.sourceforge.net/screenshots_gallery.html)

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/galleryfureffect.jpg" %}


## RTR (Real Time Rendering)

更多高级光照知识：[RTR4 拾遗（一）-- 图形学的 B 面 {% include relref_csdn.html %}](https://blog.csdn.net/leonwei/article/details/84821309)
[PBR--RTR4 笔记 -- 第八章 光与颜色 {% include relref_csdn.html %}](https://blog.csdn.net/gqkly/article/details/88086791)


## 参考资料

- [1] [Blinn-Phong 光照](http://morimiya.me/2019/02/24/Blinn-Phong%E5%85%89%E7%85%A7/)
- [2] [高级光照 learnopengl-cn {% include relref_github.html %}](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/01%20Advanced%20Lighting/)

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-23: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://de45xmedrsdbp.cloudfront.net/Resources/files/2013SiggraphPresentationsNotes-26915738.pdf]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/de45xmedrsdbp.cloudfront.net/5e127a5d.pdf" %})
- [https://zhuanlan.zhihu.com/p/102134614]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/zhuanlan.zhihu.com/4b44882b.html" %})
- [https://blog.csdn.net/qq_41286360/article/details/102794290]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/blog.csdn.net/cf63d6f4.html" %})
- [https://www.cnblogs.com/wangchengfeng/p/3440097.html]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/www.cnblogs.com/fec295b6.html" %})
- [https://www.ndt.net/article/wcndt00/papers/idn256/idn256.htm]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/www.ndt.net/368552c1.htm" %})
- [https://www.cnblogs.com/kalluwa/p/7092532.html]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/www.cnblogs.com/7b29365d.html" %})
- [https://www.shadertoy.com/view/XssXDl]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/www.shadertoy.com/2ed3e251.html" %})
- [https://www.shadertoy.com/view/ld2GRz]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/www.shadertoy.com/9f397b54.html" %})
- [https://github.com/millsvonmilski/Unity3D_RayMarching_MetaBall]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/github.com/e5fcf488.html" %})
- [http://softpixelengine.sourceforge.net/screenshots_gallery.html]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/softpixelengine.sourceforge.net/5dda551b.html" %})
- [https://blog.csdn.net/leonwei/article/details/84821309]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/blog.csdn.net/5d77c232.html" %})
- [https://blog.csdn.net/gqkly/article/details/88086791]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/blog.csdn.net/275cbb7d.html" %})
- [http://morimiya.me/2019/02/24/Blinn-Phong%E5%85%89%E7%85%A7/]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/morimiya.me/7ce24540.html" %})
- [https://learnopengl-cn.github.io/05%20Advanced%20Lighting/01%20Advanced%20Lighting/]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/learnopengl-cn.github.io/6e82a48b.html" %})
