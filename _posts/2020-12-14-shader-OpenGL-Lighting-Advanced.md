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


## 冯氏光照模型的不足

* 在镜面光分量上，当视线与反射光向量夹角大于 90° 时，镜面光值将会变为 0，在反光度非常小的情况下，会产生较明显的边界情况。

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_over_90.png" caption=" 镜面光临界情况 "%}


## Blinn-Phong 光照

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_halfway_vector.png" caption=" 镜面光临界情况 "%}

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

{% include image.html url="/assets/images/201214-shader-opengl-lighting-~d1/advanced_lighting_comparrison.png" caption=" 模型效果比较 "%}


## 参考资料

- [Blinn-Phong 光照](http://morimiya.me/2019/02/24/Blinn-Phong%E5%85%89%E7%85%A7/)
- [高级光照 learnopengl-cn {% include relref_github.html %}](https://learnopengl-cn.github.io/05%20Advanced%20Lighting/01%20Advanced%20Lighting/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [http://morimiya.me/2019/02/24/Blinn-Phong%E5%85%89%E7%85%A7/]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/morimiya.me/7ce24540.html" %})
- [2] [https://learnopengl-cn.github.io/05%20Advanced%20Lighting/01%20Advanced%20Lighting/]({% include relref.html url="/backup/2020-12-14-shader-OpenGL-Lighting-Advanced.md/learnopengl-cn.github.io/6e82a48b.html" %})
