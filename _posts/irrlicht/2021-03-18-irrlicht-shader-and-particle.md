---
layout: post
title: "Irrlicht 笔记 -- Irrlicht Shader 和 粒子系统的使用"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

Irrlicht 纹理 和 粒子系统的使用


## Tutorial 3: Custom SceneNode

创建定制的 scene node，没有用到 shader。

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/03.customscenenode.webp" urlx="/assets/images/210318-irrlicht-shader-and-par~f5/003shot.jpg" %}

```cpp
class CSampleSceneNode : public scene::ISceneNode
{
    core::aabbox3d<f32> Box;
    video::S3DVertex Vertices[4];
    video::SMaterial Material;

public:
    CSampleSceneNode(scene::ISceneNode* parent, scene::ISceneManager* mgr, s32 id)
        : scene::ISceneNode(parent, mgr, id)
    {
        Material.Wireframe = false;
        Material.Lighting = false;
        Material.Thickness = 0.f;
        // Pos(pos), Normal(normal), Color(color), TCoords(tcoords)
        Vertices[0] = video::S3DVertex(0,0,10,    5,1,0,  video::SColor(255,0,255,255), 0,1);
        Vertices[1] = video::S3DVertex(10,0,-10,  10,0,0, video::SColor(255,255,0,255), 1,1);
        Vertices[2] = video::S3DVertex(0,20,0,    20,1,1, video::SColor(255,255,255,0), 1,0);
        Vertices[3] = video::S3DVertex(-10,0,-10, 40,0,1, video::SColor(255,0,255,0),   0,0);

        Box.reset(Vertices[0].Pos);
        for (s32 i=1; i<4; ++i)
            Box.addInternalPoint(Vertices[i].Pos);
    }

    virtual void OnRegisterSceneNode()
    {
        if (IsVisible)
            SceneManager->registerNodeForRendering(this);
        ISceneNode::OnRegisterSceneNode();
    }

    virtual void render()
    {
        u16 indices[] = {    0,2,3, 2,1,3, 1,0,3, 2,0,1    };
        video::IVideoDriver* driver = SceneManager->getVideoDriver();
        driver->setMaterial(Material);
        driver->setTransform(video::ETS_WORLD, AbsoluteTransformation);
        driver->drawVertexPrimitiveList(&Vertices[0], 4, &indices[0], 4,
            video::EVT_STANDARD, scene::EPT_TRIANGLES, video::EIT_16BIT);
    }
};

int main()
{
    CSampleSceneNode *myNode =
        new CSampleSceneNode(smgr->getRootSceneNode(), smgr, 666);

    scene::ISceneNodeAnimator* anim =
        smgr->createRotationAnimator(core::vector3df(0.8f, 0, 0.8f));
    if (anim)
    {
        myNode->addAnimator(anim);
        anim->drop();
        anim = 0;
    }

    myNode->drop();
    myNode = 0; // As I shouldn't refer to it again, ensure that I can't

    u32 frames=0;
    while (device->run())
    {
        driver->beginScene(video::ECBF_COLOR | video::ECBF_DEPTH, video::SColor(0,100,100,100));
        smgr->drawAll();
        driver->endScene();

        if (++frames == 100) // don't update more often, setWindowCaption can be expensive
        {
            core::stringw str = L"Irrlicht Engine [";
            str += driver->getName();
            str += L"] FPS: ";
            str += (s32) driver->getFPS();
            device->setWindowCaption(str.c_str());
            frames = 0;
        }
    }

    device->drop();
    return 0;
}
```


## Tutorial 8: SpecialFX

特效演示。深度缓冲阴影，粒子系统，广告牌，动态光，水表面。

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/08.specialfx_3.webp" urlx="/assets/images/210318-irrlicht-shader-and-par~f5/008shot.jpg" %}

```cpp
int main()
{
    mesh = smgr->addHillPlaneMesh( "myHill",
        core::dimension2d<f32>(20,20),
        core::dimension2d<u32>(40,40), 0, 0,
        core::dimension2d<f32>(0,0),
        core::dimension2d<f32>(10,10));

    node = smgr->addWaterSurfaceSceneNode(mesh->getMesh(0), 3.0f, 300.0f, 30.0f);
    node->setPosition(core::vector3df(0,7,0));

    node->setMaterialTexture(0, driver->getTexture(mediaPath + "stones.jpg"));
    node->setMaterialTexture(1, driver->getTexture(mediaPath + "water.jpg"));

    node->setMaterialType(video::EMT_REFLECTION_2_LAYER);

    // create a particle system
    scene::IParticleSystemSceneNode* ps =
        smgr->addParticleSystemSceneNode(false);

    if (ps)
    {
        scene::IParticleEmitter* em = ps->createBoxEmitter(
            core::aabbox3d<f32>(-7,0,-7,7,1,7), // emitter size
            core::vector3df(0.0f,0.06f,0.0f),   // initial direction
            80,100,                             // emit rate
            video::SColor(0,255,255,255),       // darkest color
            video::SColor(0,255,255,255),       // brightest color
            800,2000,0,                         // min and max age, angle
            core::dimension2df(10.f,10.f),         // min size
            core::dimension2df(20.f,20.f));        // max size

        ps->setEmitter(em); // this grabs the emitter
        em->drop(); // so we can drop it here without deleting it

        scene::IParticleAffector* paf = ps->createFadeOutParticleAffector();

        ps->addAffector(paf); // same goes for the affector
        paf->drop();

        ps->setPosition(core::vector3df(-70,60,40));
        ps->setScale(core::vector3df(2,2,2));
        ps->setMaterialFlag(video::EMF_LIGHTING, false);
        ps->setMaterialFlag(video::EMF_ZWRITE_ENABLE, false);
        ps->setMaterialTexture(0, driver->getTexture(mediaPath + "fire.bmp"));
        ps->setMaterialType(video::EMT_TRANSPARENT_ADD_COLOR);
    }

    // add animated character
    mesh = smgr->getMesh(mediaPath + "dwarf.x");
    scene::IAnimatedMeshSceneNode* anode = 0;

    anode = smgr->addAnimatedMeshSceneNode(mesh);
    anode->setPosition(core::vector3df(-50,20,-60));
    anode->setAnimationSpeed(15);

    while (device->run())
    if (device->isWindowActive())
    {
        driver->beginScene(video::ECBF_COLOR | video::ECBF_DEPTH, video::SColor(0));
        smgr->drawAll();
        driver->endScene();

        const s32 fps = driver->getFPS();
        if (lastFPS != fps)
        {
            core::stringw str = L"Irrlicht Engine - SpecialFX example [";
            str += driver->getName();
            str += "] FPS:";
            str += fps;

            device->setWindowCaption(str.c_str());
            lastFPS = fps;
        }
    }

    device->drop();
    return 0;
}
```


## Tutorial 10: Shaders

shaders for D3D8, D3D9 and OpenGL。创建 shader material，关闭 texture mipmaps，使用 text scene nodes。

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/10.shaders_2.webp" urlx="/assets/images/210318-irrlicht-shader-and-par~f5/010shot.jpg" %}

```glsl
attribute vec3 inVertexPosition;
attribute vec3 inVertexNormal;
attribute vec4 inVertexColor;
attribute vec2 inTexCoord0;

uniform mat4 mWorldViewProj;
uniform mat4 mInvWorld;
uniform mat4 mTransWorld;
uniform vec3 mLightPos;
uniform vec4 mLightColor;

varying mediump vec4 v_color;
varying mediump vec2 v_texCoord;

void main(void)
{
    gl_Position = mWorldViewProj * vec4(inVertexPosition,1.0);

    vec4 normal = vec4(inVertexNormal, 0.0);
    normal = mInvWorld * normal;
    normal = normalize(normal);

    vec4 worldpos = vec4(inVertexPosition,1.0) * mTransWorld;

    vec4 lightVector = worldpos - vec4(mLightPos,1.0);
    lightVector = normalize(lightVector);

    float tmp2 = dot(-lightVector, normal);

    vec4 tmp = mLightColor * tmp2;
    v_color = vec4(tmp.x, tmp.y, tmp.z, 0.0);

    v_texCoord = inTexCoord0;
}

precision mediump float;

varying vec2 v_texCoord;
varying vec4 v_color;

uniform sampler2D myTexture;

void main (void)
{
    vec4 col = texture2D(myTexture, v_texCoord);
    col *= v_color;
    gl_FragColor = col * 4.0;
}
```

```cpp
class MyShaderCallBack : public video::IShaderConstantSetCallBack
{
public:
    MyShaderCallBack() : WorldViewProjID(-1), TransWorldID(-1), InvWorldID(-1), PositionID(-1),
                        ColorID(-1), TextureID(-1), FirstUpdate(true)
    {
    }

    virtual void OnSetConstants(video::IMaterialRendererServices* services, s32 userData)
    {
        video::IVideoDriver* driver = services->getVideoDriver();

        // 获取 Shader 常量。
        if (UseHighLevelShaders && FirstUpdate)
        {
            WorldViewProjID = services->getVertexShaderConstantID("mWorldViewProj");
            TransWorldID = services->getVertexShaderConstantID("mTransWorld");
            InvWorldID = services->getVertexShaderConstantID("mInvWorld");
            PositionID = services->getVertexShaderConstantID("mLightPos");
            ColorID = services->getVertexShaderConstantID("mLightColor");

            if (driver->getDriverType() == video::EDT_OPENGL)
                TextureID = services->getVertexShaderConstantID("myTexture");
            FirstUpdate = false;
        }

        core::matrix4 invWorld = driver->getTransform(video::ETS_WORLD);
        invWorld.makeInverse();
        if (UseHighLevelShaders)
            services->setVertexShaderConstant(InvWorldID, invWorld.pointer(), 16);
        else
            services->setVertexShaderConstant(invWorld.pointer(), 0, 4);

        // 设置剪裁矩阵
        core::matrix4 worldViewProj;
        worldViewProj = driver->getTransform(video::ETS_PROJECTION);
        worldViewProj *= driver->getTransform(video::ETS_VIEW);
        worldViewProj *= driver->getTransform(video::ETS_WORLD);

        if (UseHighLevelShaders)
            services->setVertexShaderConstant(WorldViewProjID, worldViewProj.pointer(), 16);
        else
            services->setVertexShaderConstant(worldViewProj.pointer(), 4, 4);

        // 设置相机位置
        core::vector3df pos = device->getSceneManager()-> getActiveCamera()->getAbsolutePosition();
        if (UseHighLevelShaders)
            services->setVertexShaderConstant(PositionID, reinterpret_cast<f32*>(&pos), 3);
        else
            services->setVertexShaderConstant(reinterpret_cast<f32*>(&pos), 8, 1);

        // 设置光照颜色
        video::SColorf col(0.0f,1.0f,1.0f,0.0f);
        if (UseHighLevelShaders)
            services->setVertexShaderConstant(ColorID, reinterpret_cast<f32*>(&col), 4);
        else
            services->setVertexShaderConstant(reinterpret_cast<f32*>(&col), 9, 1);

        // 设置世界变换矩阵
        core::matrix4 world = driver->getTransform(video::ETS_WORLD);
        world = world.getTransposed();
        if (UseHighLevelShaders)
        {
            services->setVertexShaderConstant(TransWorldID, world.pointer(), 16);
            s32 TextureLayerID = 0;
            services->setPixelShaderConstant(TextureID, &TextureLayerID, 1);
        }
        else
            services->setVertexShaderConstant(world.pointer(), 10, 4);
    }

private:
    s32 WorldViewProjID;
    s32 TransWorldID;
    s32 InvWorldID;
    s32 PositionID;
    s32 ColorID;
    s32 TextureID;
    bool FirstUpdate;
};

int main()
{
    io::path vsFileName; // filename for the vertex shader
    io::path psFileName; // filename for the pixel shader

    if (!driver->queryFeature(video::EVDF_PIXEL_SHADER_1_1) &&
        !driver->queryFeature(video::EVDF_ARB_FRAGMENT_PROGRAM_1))
    {
        device->getLogger()->log("WARNING: Pixel shaders disabled "\
            "because of missing driver/hardware support.");
        psFileName = "";
    }

    if (!driver->queryFeature(video::EVDF_VERTEX_SHADER_1_1) &&
        !driver->queryFeature(video::EVDF_ARB_VERTEX_PROGRAM_1))
    {
        device->getLogger()->log("WARNING: Vertex shaders disabled "\
            "because of missing driver/hardware support.");
        vsFileName = "";
    }

    if (gpu)
    {
        MyShaderCallBack* mcSolid = new MyShaderCallBack();
        MyShaderCallBack* mcTransparentAdd = new MyShaderCallBack();

        if (UseHighLevelShaders)
        {
            newMaterialType1 = gpu->addHighLevelShaderMaterialFromFiles(
                vsFileName, "vertexMain", video::EVST_VS_1_1,
                psFileName, "pixelMain", video::EPST_PS_1_1,
                mcSolid, video::EMT_SOLID, 0);

            newMaterialType2 = gpu->addHighLevelShaderMaterialFromFiles(
                vsFileName, "vertexMain", video::EVST_VS_1_1,
                psFileName, "pixelMain", video::EPST_PS_1_1,
                mcTransparentAdd, video::EMT_TRANSPARENT_ADD_COLOR, 0);
        }

        mcSolid->drop();
        mcTransparentAdd->drop();
    }

    // create test scene node 1, with the new created material type 1
    scene::ISceneNode* node = smgr->addCubeSceneNode(50);
    node->setPosition(core::vector3df(0,0,0));
    node->setMaterialTexture(0, driver->getTexture(mediaPath + "wall.bmp"));
    node->setMaterialFlag(video::EMF_LIGHTING, false);
    node->setMaterialType((video::E_MATERIAL_TYPE)newMaterialType1);

    smgr->addTextSceneNode(gui->getBuiltInFont(),
            L"PS & VS & EMT_SOLID",
            video::SColor(255,255,255,255),    node);
    scene::ISceneNodeAnimator* anim = smgr->createRotationAnimator(
            core::vector3df(0,0.3f,0));
    node->addAnimator(anim);
    anim->drop();

    node = smgr->addCubeSceneNode(50);
    node->setPosition(core::vector3df(0,-10,50));
    node->setMaterialTexture(0, driver->getTexture(mediaPath + "wall.bmp"));
    node->setMaterialFlag(video::EMF_LIGHTING, false);
    node->setMaterialFlag(video::EMF_BLEND_OPERATION, true);
    node->setMaterialType((video::E_MATERIAL_TYPE)newMaterialType2);
    smgr->addTextSceneNode(gui->getBuiltInFont(),
            L"PS & VS & EMT_TRANSPARENT",
            video::SColor(255,255,255,255),    node);

    anim = smgr->createRotationAnimator(core::vector3df(0,0.3f,0));
    node->addAnimator(anim);
    anim->drop();
```


## Tutorial 11: Per-Pixel Lighting

逐像素光照、雾、移动光、粒子。复杂 material。用 normal maps and parallax mapping 计算每个像素的光照。烟雾的使用，和移动粒子系统。
[Irrlicht 学习笔记 (10)--PerPixelLighting {% include relref_csdn.html %}](https://blog.csdn.net/gqkly/article/details/51870182)

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/11.perpixellighting_4.webp" urlx="/assets/images/210318-irrlicht-shader-and-par~f5/011shot.jpg" %}


## Tutorial 13: Render To Texture

渲染到一个纹理。使用 specular highlights。

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/13.rendertotexture.webp" urlx="/assets/images/210318-irrlicht-shader-and-par~f5/013shot.jpg" %}


## 27.PostProcessing

创建屏幕双缓冲。颜色反转，用 HLSL and GLSL 写的。

{% include image.html url="/assets/images/210318-irrlicht-shader-and-par~f5/27.postprocessing.webp" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-18-irrlicht-shader-and-particle.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/gqkly/article/details/51870182]({% include relrefx.html url="/backup/2021-03-18-irrlicht-shader-and-particle.md/blog.csdn.net/055cce4d.html" %})
