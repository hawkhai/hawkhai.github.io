---
layout: post
title: "3D 引擎 Irrlicht -- OpenGL ES 2.x Driver 源码剖析 概览"
author:
location: "珠海"
categories: ["3D 引擎"]
tags: ["Irrlicht", "图形学"]
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

整个 3D 引擎是构建在 显卡之上，最终 CPU 都需要把数据传给 GPU 完成绘制，这些 Shader 是整个引擎的地基。
OpenGL ES 2.x Driver 底层一共包含 22 个 Shader 文件。逐个文件翻译分析，可以感受到作者的封装思路。

肯定抽象的不错的，因为抽象过后，基本上支持了主流的显卡技术：D3D、OpenGL、OpenGL-ES2 and its own software renderers。
**日拱一卒无有尽，功不唐捐终入海。**开始觉得很难，拱到最后，发现整个引擎还是挺简陋的。
整个 3D 引擎是构建在 显卡之上，最终 CPU 都需要把数据传给 GPU 完成绘制，这些 Shader 是整个引擎的地基。

后继逐个剖析每个 shader 的具体实现。


## EDriverTypes.h

* **EDT_NULL** NullDriver. 只加载纹理，不渲染。

* **EDT_SOFTWARE** Software Renderer. 支持所有平台，所有硬件。
    只渲染 2D 图形和一些基本的 3D 函数。速度快，但是不准确，不支持剪裁。

* **EDT_BURNINGSVIDEO** Burning's Video.
    模拟了整个 3D 光栅化。能正确的 3D 剪裁、透视矫正、纹理映射 等等。

* **DEPRECATED_EDT_DIRECT3D8_NO_LONGER_EXISTS** Direct3D 8.1. 不再支持。

* **EDT_DIRECT3D9** Direct3D 9.0c.

* **EDT_OPENGL** OpenGL 1.x/2.x/3.x.

* **EDT_OGLES1** OpenGL ES1.

* **EDT_OGLES2** OpenGL ES2.

* **EDT_WEBGL1** WebGL 1. WebGL1 friendly subset of OpenGL-ES 2.x driver for Emscripten.

* **EDT_COUNT** No driver, just for counting the elements.


## addHighLevelShaderMaterialFromFiles

```cpp
// return Number of the material type which can be set in
// SMaterial::MaterialType to use the renderer.
virtual s32 addHighLevelShaderMaterialFromFiles(
    // 顶点着色器参数
    const io::path& vertexShaderProgramFileName,
    const c8* vertexShaderEntryPointName,
    E_VERTEX_SHADER_TYPE vsCompileTarget,
    // 片元着色器参数
    const io::path& pixelShaderProgramFileName,
    const c8* pixelShaderEntryPointName,
    E_PIXEL_SHADER_TYPE psCompileTarget,
    // 几何着色器参数
    const io::path& geometryShaderProgramFileName,
    const c8* geometryShaderEntryPointName = "main",
    E_GEOMETRY_SHADER_TYPE gsCompileTarget = EGST_GS_4_0,
    scene::E_PRIMITIVE_TYPE inType = scene::EPT_TRIANGLES,
    scene::E_PRIMITIVE_TYPE outType = scene::EPT_TRIANGLE_STRIP,
    u32 verticesOut = 0, // Maximal number of vertices created by geometry shader.
    // 其它参数
    IShaderConstantSetCallBack* callback = 0, // 设置 Shelder 常量
    E_MATERIAL_TYPE baseMaterial = video::EMT_SOLID, // renderstates
    s32 userData = 0, // callback 回掉标记参数
    E_GPU_SHADING_LANGUAGE shadingLang = EGSL_DEFAULT // 什么 Shelder 语言
) = 0;
```


### baseMaterial

```cpp
switch (baseMaterial)
{
case EMT_TRANSPARENT_VERTEX_ALPHA:
case EMT_TRANSPARENT_ALPHA_CHANNEL:
case EMT_NORMAL_MAP_TRANSPARENT_VERTEX_ALPHA:
case EMT_PARALLAX_MAP_TRANSPARENT_VERTEX_ALPHA:
    Alpha = true;
    break;
case EMT_TRANSPARENT_ADD_COLOR:
case EMT_NORMAL_MAP_TRANSPARENT_ADD_COLOR:
case EMT_PARALLAX_MAP_TRANSPARENT_ADD_COLOR:
    FixedBlending = true;
    break;
case EMT_ONETEXTURE_BLEND:
    Blending = true;
    break;
default:
    break;
}
```


## material 类型


### EMT_SOLID

$\color{red}{solid}$
标准的固体材料。只使用第一个纹理，只支持漫反射。


### EMT_SOLID_2_LAYER

$\color{red}{solid\\\_2layer}$
固体材质，只支持两个纹理层。第二个根据顶点颜色 alpha 值混合到第一层。
The second is blended onto the first using the alpha value of the vertex colors.


### EMT_LIGHTMAP

$\color{red}{lightmap}$
标准 modulated 光照。两个纹理层。第一个是漫反射 map，第二个是 光照 map。不支持动态光。

**EMT_LIGHTMAP_M2** $\color{red}{lightmap\\\_m2}$
标准光照，两个纹理。第一个是 diffuse map，第二个是 light map，忽略动态光。
The texture colors are effectively multiplied by 2 for brightening. 将两个混合参数相乘后再乘以 2 输出。

**EMT_LIGHTMAP_M4** $\color{red}{lightmap\\\_m4}$
标准光照。同上，将两个混合参数相乘后再乘以 4 输出。D3DTOP_MODULATE4X


### EMT_LIGHTMAP_ADD

$\color{red}{lightmap\\\_add}$
ADD 光照。光照叠加采用加法，而非 modulated。
lightmap and diffuse texture are added instead of modulated.


### EMT_LIGHTMAP_LIGHTING

$\color{red}{lightmap\\\_light}$
同 EMT_LIGHTMAP，支持动态光。

**EMT_LIGHTMAP_LIGHTING_M2** $\color{red}{lightmap\\\_light\\\_m2}$
同 EMT_LIGHTMAP_M2，支持动态光。

**EMT_LIGHTMAP_LIGHTING_M4** $\color{red}{lightmap\\\_light\\\_m4}$
同 EMT_LIGHTMAP_LIGHTING_M4，支持动态光。


### EMT_DETAIL_MAP

$\color{red}{detail\\\_map}$
mapped 细节纹理。
第一个纹理是漫反射 color map，第二个用一个大 scale 加到第一个上，就能保证更多细节。
采用 ADD_SIGNED 加法，所以就可加可减，多用来绘制地形。
(127,127,127) 就表示不对 diffuse map 的值做任何改变。


### EMT_SPHERE_MAP

$\color{red}{sphere\\\_map}$
带环境反射的材质。第一个纹理必须是 'sphere map'。


### EMT_REFLECTION_2_LAYER

$\color{red}{reflection\\\_2layer}$
带反射能力的材质。第一个纹理必须是 reflection map。可以选择不反色。
A reflecting material with an optional non reflecting texture layer.


### EMT_TRANSPARENT_ADD_COLOR

$\color{red}{trans\\\_add}$
透明材质。只用到第一个纹理。
简单的加法，粒子系统经常用到。


### EMT_TRANSPARENT_ALPHA_CHANNEL

$\color{red}{trans\\\_alphach}$
透明材质。根据纹理的 alpha 通道，叠加到目标上。
最好是 32 位模式 `video::IVideoDriver::setTextureCreationFlag()`。
This value controls how sharp the edges become when going from a transparent to a solid spot on the texture.


### EMT_TRANSPARENT_ALPHA_CHANNEL_REF

$\color{red}{trans\\\_alphach\\\_ref}$
透明材质。根据纹理的 alpha 通道。只有当 通道值大于 127，像素值才被写入，否则抛弃。
没有使用 alpha blending，比 EMT_TRANSPARENT_ALPHA_CHANNEL 快一点点。
比如树干的边缘是锋利的，而非模糊的。
It is ideal for drawing stuff like leaves of plants, because the borders are not blurry but sharp.


### EMT_TRANSPARENT_VERTEX_ALPHA

$\color{red}{trans\\\_vertex\\\_alpha}$
透明材质。根据顶点的 alpha 值。


### EMT_TRANSPARENT_REFLECTION_2_LAYER

$\color{red}{trans\\\_reflection\\\_2layer}$
透明反射材质。拥有一个附加可选的非反色纹理。
透明度采用纹理的顶点的 alpha 值。第二个纹理不反射。


### EMT_NORMAL_MAP_SOLID

$\color{red}{normalmap\\\_solid}$
实体法线贴图 renderer。第一个纹理是 color map，第二个是 normal map。
只能绘制 S3DVertexTangents (EVT_TANGENTS) 组成的顶点几何图形。
如果硬件不支持，将退化为 固定光照材质。只支持两个光源，如果太多了，只选择最近的两个。

实体法线图渲染器。第一个图为纹理图，第二个图为法线图。
只有当顶点是 S3DVertexTangents(EVT_TANGENTS) 格式才可以使用这种材质。
可以使用 `IMeshManipulator::createMeshWithTangent()` 将任何网格转换成所需格式。

**EMT_NORMAL_MAP_TRANSPARENT_ADD_COLOR** $\color{red}{normalmap\\\_trans\\\_add}$

透明的法线贴图渲染器。
第一个纹理是 color map，第二纹理是 normal map。
You can convert any mesh into this format using `IMeshManipulator::createMeshWithTangents()` (See SpecialFX2 Tutorial).
如果多个光源，只选择最近的两个。其它同上。

**EMT_NORMAL_MAP_TRANSPARENT_VERTEX_ALPHA** $\color{red}{normalmap\\\_trans\\\_vertexalpha}$

透明的法线贴图渲染器（基于顶点的 alpha 值）。其它同上。


### EMT_PARALLAX_MAP_SOLID

$\color{red}{parallaxmap\\\_solid}$
很像 EMT_NORMAL_MAP_SOLID，但是采用视差 parallax mapping.
第一个纹理采用 color map，第二个纹理采用 normal map（需要包含高度 in the alpha component）。
The `IVideoDriver::makeNormalMapTexture()` method 自动写入这个值当创建 normal maps from a heightmap when using a 32 bit texture.
The height scale of the material (affecting the bumpiness) is being controlled by the SMaterial::MaterialTypeParam member.
If set to zero, the default value (0.02f) will be applied. 过大或者过小，都会绘制出来会非常奇怪。

和 EMT_NORMAL_MAP_SOLID 差不多，只是只有的是 parallax 图，更加真实。
第一个图为纹理图，第二个图为法线图 (32bits)（高度图）。
法线图纹理需要在其透明度通道中包含高度信息，高度信息可以通过函数 IVideoDriver::makeNormalMapTexture 自动设置，
函数参数：第一个纹理图（其 alpha 通道可改变），第二个 amplitude 缩放比例。

**EMT_PARALLAX_MAP_TRANSPARENT_ADD_COLOR** $\color{red}{parallaxmap\\\_trans\\\_add}$

跟 EMT_PARALLAX_MAP_SOLID 一样，但是是透明的。

**EMT_PARALLAX_MAP_TRANSPARENT_VERTEX_ALPHA** $\color{red}{parallaxmap\\\_trans\\\_vertexalpha}$

跟 EMT_PARALLAX_MAP_SOLID 一样，用 EMT_TRANSPARENT_VERTEX_ALPHA 透明。


### EMT_ONETEXTURE_BLEND

$\color{red}{onetexture\\\_blend}$
用纹理生成一个混合方法。

$$BlendFunc = source * sourceFactor + dest * destFactor ( E\_BLEND\_FUNC )$$

The blend function is set to SMaterial::MaterialTypeParam with pack_textureBlendFunc (for 2D) or pack_textureBlendFuncSeparate (for 3D).


### EMT_FORCE_32BIT

$\color{red}{= 0x7fffffff}$
This value is not used. It only forces this enumeration to compile to 32 bit.


## 书上翻译的

{% include image.html url="/assets/images/210105-irrlicht-gles-driver/20210118132805.jpg" %}
{% include image.html url="/assets/images/210105-irrlicht-gles-driver/20210118132823.jpg" %}


## Source Code

```cpp
void COGLES2Driver::createMaterialRenderers()
{
    // Create built-in materials.
    core::stringc vsh = "COGLES2Solid.vsh";
    core::stringc fsh = "COGLES2Solid.fsh";
    // EMT_SOLID SolidCB
    addShaderMaterial(vsh, fsh, SolidCB(), EMT_SOLID);

    vsh = "COGLES2Solid2.vsh";
    fsh = "COGLES2Solid2Layer.fsh";
    // EMT_SOLID_2_LAYER Solid2LayerCB
    addShaderMaterial(vsh, fsh, Solid2CB(), EMT_SOLID);

    vsh = "COGLES2Solid2.vsh";
    fsh = "COGLES2LightmapAdd.fsh";
    // EMT_LIGHTMAP_ADD LightmapAddCB
    addShaderMaterial(vsh, fsh, LightmapCB(1.f), EMT_SOLID);

    fsh = "COGLES2LightmapModulate.fsh";
    // EMT_LIGHTMAP LightmapCB
    addShaderMaterial(vsh, fsh, LightmapCB(1.f), EMT_SOLID);
    // EMT_LIGHTMAP_M2 LightmapM2CB
    addShaderMaterial(vsh, fsh, LightmapCB(2.f), EMT_SOLID);
    // EMT_LIGHTMAP_M4 LightmapM4CB
    addShaderMaterial(vsh, fsh, LightmapCB(4.f), EMT_SOLID);
    // EMT_LIGHTMAP_LIGHTING LightmapLightingCB
    addShaderMaterial(vsh, fsh, LightmapCB(1.f), EMT_SOLID);
    // EMT_LIGHTMAP_LIGHTING_M2 LightmapLightingM2CB
    addShaderMaterial(vsh, fsh, LightmapCB(2.f), EMT_SOLID);
    // EMT_LIGHTMAP_LIGHTING_M4 LightmapLightingM4CB
    addShaderMaterial(vsh, fsh, LightmapCB(4.f), EMT_SOLID);

    vsh = "COGLES2Solid2.vsh";
    fsh = "COGLES2DetailMap.fsh";
    // EMT_DETAIL_MAP DetailMapCB
    addShaderMaterial(vsh, fsh, Solid2CB(), EMT_SOLID);

    vsh = "COGLES2SphereMap.vsh";
    fsh = "COGLES2SphereMap.fsh";
    // EMT_SPHERE_MAP SphereMapCB
    addShaderMaterial(vsh, fsh, ReflectionCB(), EMT_SOLID);

    vsh = "COGLES2Reflection2Layer.vsh";
    fsh = "COGLES2Reflection2Layer.fsh";
    // EMT_REFLECTION_2_LAYER Reflection2LayerCB
    addShaderMaterial(vsh, fsh, ReflectionCB(), EMT_SOLID);

    vsh = "COGLES2Solid.vsh";
    fsh = "COGLES2Solid.fsh";
    // EMT_TRANSPARENT_ADD_COLOR TransparentAddColorCB
    addShaderMaterial(vsh, fsh, SolidCB(), EMT_TRANSPARENT_ADD_COLOR);

    fsh = "COGLES2TransparentAlphaChannel.fsh";
    // EMT_TRANSPARENT_ALPHA_CHANNEL TransparentAlphaChannelCB
    addShaderMaterial(vsh, fsh, SolidCB(), EMT_TRANSPARENT_ALPHA_CHANNEL);

    fsh = "COGLES2TransparentAlphaChannelRef.fsh";
    // EMT_TRANSPARENT_ALPHA_CHANNEL_REF TransparentAlphaChannelRefCB
    addShaderMaterial(vsh, fsh, SolidCB(), EMT_SOLID);

    fsh = "COGLES2TransparentVertexAlpha.fsh";
    // EMT_TRANSPARENT_VERTEX_ALPHA TransparentVertexAlphaCB
    addShaderMaterial(vsh, fsh, SolidCB(), EMT_TRANSPARENT_ALPHA_CHANNEL);

    vsh = "COGLES2Reflection2Layer.vsh";
    fsh = "COGLES2Reflection2Layer.fsh";
    // EMT_TRANSPARENT_REFLECTION_2_LAYER TransparentReflection2LayerCB
    addShaderMaterial(vsh, fsh, ReflectionCB(), EMT_TRANSPARENT_ALPHA_CHANNEL);

    vsh = "COGLES2NormalMap.vsh";
    fsh = "COGLES2NormalMap.fsh";
    // EMT_NORMAL_MAP_SOLID NormalMapCB
    addShaderMaterial(vsh, fsh, NormalMapCB(), EMT_SOLID);
    // EMT_NORMAL_MAP_TRANSPARENT_ADD_COLOR NormalMapAddColorCB
    addShaderMaterial(vsh, fsh, NormalMapCB(), EMT_TRANSPARENT_ADD_COLOR);
    // EMT_NORMAL_MAP_TRANSPARENT_VERTEX_ALPHA NormalMapVertexAlphaCB
    addShaderMaterial(vsh, fsh, NormalMapCB(), EMT_TRANSPARENT_ALPHA_CHANNEL);

    vsh = "COGLES2ParallaxMap.vsh";
    fsh = "COGLES2ParallaxMap.fsh";
    // EMT_PARALLAX_MAP_SOLID ParallaxMapCB
    addShaderMaterial(vsh, fsh, ParallaxMapCB(), EMT_SOLID);
    // EMT_PARALLAX_MAP_TRANSPARENT_ADD_COLOR ParallaxMapAddColorCB
    addShaderMaterial(vsh, fsh, ParallaxMapCB(), EMT_TRANSPARENT_ADD_COLOR);
    // EMT_PARALLAX_MAP_TRANSPARENT_VERTEX_ALPHA ParallaxMapVertexAlphaCB
    addShaderMaterial(vsh, fsh, ParallaxMapCB(), EMT_TRANSPARENT_ALPHA_CHANNEL);

    vsh = "COGLES2Solid.vsh";
    fsh = "COGLES2OneTextureBlend.fsh";
    // EMT_ONETEXTURE_BLEND OneTextureBlendCB
    addShaderMaterial(vsh, fsh, OneTextureBlendCB(), EMT_ONETEXTURE_BLEND);

    // Create 2D material renderers
    loadShaderData("COGLES2Renderer2D.vsh", "COGLES2Renderer2D.fsh", &vs2DData, &fs2DData);
    MaterialRenderer2DTexture = new COGLES2Renderer2D(vs2DData, fs2DData, this, true);

    loadShaderData("COGLES2Renderer2D.vsh", "COGLES2Renderer2D_noTex.fsh", &vs2DData, &fs2DData);
    MaterialRenderer2DNoTexture = new COGLES2Renderer2D(vs2DData, fs2DData, this, false);
}
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-05-irrlicht-gles-driver.md.js" %}'></script></p>
