---
layout: post
title: "Irrlicht 3D 笔记 -- OpenGL ES 2.x Driver 源码剖析 概览"
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

整个 3D 引擎是构建在 显卡之上，最终 CPU 都需要把数据传给 GPU 完成绘制，这些 Shader 是整个引擎的地基。
OpenGL ES 2.x Driver 底层一共包含 22 个 Shader 文件。逐个文件翻译分析，可以感受到作者的封装思路。

肯定抽象的不错的，因为抽象过后，基本上支持了主流的显卡技术：D3D，OpenGL，OpenGL-ES2 and its own software renderers。
日拱一卒无有尽，功不唐捐终入海。开始觉得很难，拱到最后，发现整个引擎还是挺简陋的。
整个 3D 引擎是构建在 显卡之上，最终 CPU 都需要把数据传给 GPU 完成绘制，这些 Shader 是整个引擎的地基。

* COGLES2DetailMap.fsh
* COGLES2LightmapAdd.fsh
* COGLES2LightmapModulate.fsh
* COGLES2NormalMap.fsh
* COGLES2NormalMap.vsh
* COGLES2OneTextureBlend.fsh
* COGLES2ParallaxMap.fsh
* COGLES2ParallaxMap.vsh
* COGLES2Reflection2Layer.fsh
* COGLES2Reflection2Layer.vsh
* COGLES2Renderer2D.fsh
* COGLES2Renderer2D.vsh
* COGLES2Renderer2D_noTex.fsh
* COGLES2Solid.fsh
* COGLES2Solid.vsh
* COGLES2Solid2.vsh
* COGLES2Solid2Layer.fsh
* COGLES2SphereMap.fsh
* COGLES2SphereMap.vsh
* COGLES2TransparentAlphaChannel.fsh
* COGLES2TransparentAlphaChannelRef.fsh
* COGLES2TransparentVertexAlpha.fsh

后继逐个剖析每个 shader 的具体实现。


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


## Source Code

```cpp
void COGLES2Driver::createMaterialRenderers()
{
    // Create built-in materials.
    core::stringc VertexShader = "COGLES2Solid.vsh";
    core::stringc FragmentShader = "COGLES2Solid.fsh";
    COGLES2MaterialSolidCB* SolidCB = new COGLES2MaterialSolidCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, SolidCB, EMT_SOLID);

    VertexShader = "COGLES2Solid2.vsh";
    FragmentShader = "COGLES2Solid2Layer.fsh";
    COGLES2MaterialSolid2CB* Solid2LayerCB = new COGLES2MaterialSolid2CB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, Solid2LayerCB, EMT_SOLID);

    VertexShader = "COGLES2Solid2.vsh";
    FragmentShader = "COGLES2LightmapModulate.fsh";
    COGLES2MaterialLightmapCB* LightmapCB = new COGLES2MaterialLightmapCB(1.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapCB, EMT_SOLID);

    FragmentShader = "COGLES2LightmapAdd.fsh";
    COGLES2MaterialLightmapCB* LightmapAddCB = new COGLES2MaterialLightmapCB(1.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapAddCB, EMT_SOLID);

    FragmentShader = "COGLES2LightmapModulate.fsh";
    COGLES2MaterialLightmapCB* LightmapM2CB = new COGLES2MaterialLightmapCB(2.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapM2CB, EMT_SOLID);

    COGLES2MaterialLightmapCB* LightmapM4CB = new COGLES2MaterialLightmapCB(4.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapM4CB, EMT_SOLID);

    COGLES2MaterialLightmapCB* LightmapLightingCB = new COGLES2MaterialLightmapCB(1.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapLightingCB, EMT_SOLID);

    COGLES2MaterialLightmapCB* LightmapLightingM2CB = new COGLES2MaterialLightmapCB(2.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapLightingM2CB, EMT_SOLID);

    COGLES2MaterialLightmapCB* LightmapLightingM4CB = new COGLES2MaterialLightmapCB(4.f);
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, LightmapLightingM4CB, EMT_SOLID);

    VertexShader = "COGLES2Solid2.vsh";
    FragmentShader = "COGLES2DetailMap.fsh";
    COGLES2MaterialSolid2CB* DetailMapCB = new COGLES2MaterialSolid2CB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, DetailMapCB, EMT_SOLID);

    VertexShader = "COGLES2SphereMap.vsh";
    FragmentShader = "COGLES2SphereMap.fsh";
    COGLES2MaterialReflectionCB* SphereMapCB = new COGLES2MaterialReflectionCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, SphereMapCB, EMT_SOLID);

    VertexShader = "COGLES2Reflection2Layer.vsh";
    FragmentShader = "COGLES2Reflection2Layer.fsh";
    COGLES2MaterialReflectionCB* Reflection2LayerCB = new COGLES2MaterialReflectionCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, Reflection2LayerCB, EMT_SOLID);

    VertexShader = "COGLES2Solid.vsh";
    FragmentShader = "COGLES2Solid.fsh";
    COGLES2MaterialSolidCB* TransparentAddColorCB = new COGLES2MaterialSolidCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, TransparentAddColorCB, EMT_TRANSPARENT_ADD_COLOR);

    FragmentShader = "COGLES2TransparentAlphaChannel.fsh";
    COGLES2MaterialSolidCB* TransparentAlphaChannelCB = new COGLES2MaterialSolidCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, TransparentAlphaChannelCB, EMT_TRANSPARENT_ALPHA_CHANNEL);

    FragmentShader = "COGLES2TransparentAlphaChannelRef.fsh";
    COGLES2MaterialSolidCB* TransparentAlphaChannelRefCB = new COGLES2MaterialSolidCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, TransparentAlphaChannelRefCB, EMT_SOLID);

    FragmentShader = "COGLES2TransparentVertexAlpha.fsh";
    COGLES2MaterialSolidCB* TransparentVertexAlphaCB = new COGLES2MaterialSolidCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, TransparentVertexAlphaCB, EMT_TRANSPARENT_ALPHA_CHANNEL);

    VertexShader = "COGLES2Reflection2Layer.vsh";
    FragmentShader = "COGLES2Reflection2Layer.fsh";
    COGLES2MaterialReflectionCB* TransparentReflection2LayerCB = new COGLES2MaterialReflectionCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, TransparentReflection2LayerCB, EMT_TRANSPARENT_ALPHA_CHANNEL);

    VertexShader = "COGLES2NormalMap.vsh";
    FragmentShader = "COGLES2NormalMap.fsh";
    COGLES2MaterialNormalMapCB* NormalMapCB = new COGLES2MaterialNormalMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, NormalMapCB, EMT_SOLID);

    COGLES2MaterialNormalMapCB* NormalMapAddColorCB = new COGLES2MaterialNormalMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, NormalMapAddColorCB, EMT_TRANSPARENT_ADD_COLOR);

    COGLES2MaterialNormalMapCB* NormalMapVertexAlphaCB = new COGLES2MaterialNormalMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, NormalMapVertexAlphaCB, EMT_TRANSPARENT_ALPHA_CHANNEL);

    VertexShader = "COGLES2ParallaxMap.vsh";
    FragmentShader = "COGLES2ParallaxMap.fsh";
    COGLES2MaterialParallaxMapCB* ParallaxMapCB = new COGLES2MaterialParallaxMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, ParallaxMapCB, EMT_SOLID);

    COGLES2MaterialParallaxMapCB* ParallaxMapAddColorCB = new COGLES2MaterialParallaxMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, ParallaxMapAddColorCB, EMT_TRANSPARENT_ADD_COLOR);

    COGLES2MaterialParallaxMapCB* ParallaxMapVertexAlphaCB = new COGLES2MaterialParallaxMapCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, ParallaxMapVertexAlphaCB, EMT_TRANSPARENT_ALPHA_CHANNEL);

    VertexShader = "COGLES2Solid.vsh";
    FragmentShader = "COGLES2OneTextureBlend.fsh";
    COGLES2MaterialOneTextureBlendCB* OneTextureBlendCB = new COGLES2MaterialOneTextureBlendCB();
    addHighLevelShaderMaterialFromFiles(VertexShader, FragmentShader, OneTextureBlendCB, EMT_ONETEXTURE_BLEND);

    // Create 2D material renderers
    c8* vs2DData = 0;
    c8* fs2DData = 0;
    loadShaderData(io::path("COGLES2Renderer2D.vsh"), io::path("COGLES2Renderer2D.fsh"), &vs2DData, &fs2DData);
    MaterialRenderer2DTexture = new COGLES2Renderer2D(vs2DData, fs2DData, this, true);
    delete[] vs2DData;
    delete[] fs2DData;
    vs2DData = 0;
    fs2DData = 0;

    loadShaderData(io::path("COGLES2Renderer2D.vsh"), io::path("COGLES2Renderer2D_noTex.fsh"), &vs2DData, &fs2DData);
    MaterialRenderer2DNoTexture = new COGLES2Renderer2D(vs2DData, fs2DData, this, false);
    delete[] vs2DData;
    delete[] fs2DData;
}
```
