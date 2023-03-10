---
layout: post
title: "3D 引擎 Irrlicht -- Irrlicht 3D 学习笔记"
author:
location: "珠海"
categories: ["3D 引擎"]
tags: ["Irrlicht", "图形学"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 雾效


### 雾的类型 E_FOG_TYPE

* **EFT_FOG_EXP** ：简单渲染在屏幕上显示的雾的模式。它无法给予我们非常漂亮的雾的效果，但是却可以在古老的电脑上工作的很好。
* **EFT_FOG_EXP22** ：比 1 提高了一点，将渲染全屏幕的雾，然而她会给予场景更深的效果。
* **EFT_FOG_LINEAR** ：这是最好的雾的渲染模式，对象在雾中消隐的很好。


### 创建雾

```cpp
driver->setFog(video::SColor(0,138,125,81), // color
               video::EFT_FOG_LINEAR, // fog type
               0, // start
               500, // end
               0.005f, // density
               true, // pixel fog
               false // range fog
);
```

The object must has the fog flag enabled in its material.


## 水效

注意，按下面的方式创建水的特效，必须要设置光照，同时创建 device 时，device 的 type 最好不要用 EDT_SOFTWARE，用这种 type，会影响水效。

{% include image.html url="/assets/images/210106-irrlicht-notes/20210106174623.png" %}


### 创建水面的 mesh

```cpp
mesh = smgr->addHillPlaneMesh("myHill", // name
            core::dimension2d<f32>(20,20), // tile Size
            core::dimension2d<u32>(40,40), // tile Count
            0, // material
            0, // hill Height
            core::dimension2d<f32>(0,0), // There will be countHills.X hills along the X axis and countHills.Y
                                         // along the Y axis. So in total there will be countHills.X * countHills.Y hills.
            core::dimension2d<f32>(10,10) // texture Repeat Count
);
```


### mesh 纹理

利用上面的 mesh，创建一个水面的 node，并为 node 设置两层纹理，一层做为水表，一层做为水底物体透明纹理。

```cpp
node = smgr->addWaterSurfaceSceneNode(mesh->getMesh(0), // mesh
                    3.0f, // waveHeight
                    300.0f, // waveSpeed
                    30.0f // waveLength
);
node->setPosition(core::vector3df(0,7,0));
node->setMaterialTexture(0, driver->getTexture("../../media/stones.jpg"));
node->setMaterialTexture(1, driver->getTexture("../../media/water.jpg"));
node->setMaterialType(video::EMT_REFLECTION_2_LAYER);
```


## 制作环绕的灯光

用公告板与一个动态光结合实现一个动态灯光。

公告板是什么？
A billboard is like a 3d sprite: A 2d element, which always looks to the camera.


### 制作一个动态灯

```cpp
scene::ISceneNode* node = smgr->addLightSceneNode(0, // parent
                                core::vector3df(0,0,0), // position
                                video::SColorf(1.0f, 0.6f, 0.7f, 1.0f), // color
                                800.0f); // radius
scene::ISceneNodeAnimator* anim = 0;
anim = smgr->createFlyCircleAnimator(core::vector3df(0,150,0), 250.0f);
node->addAnimator(anim);
anim->drop();
```


### 制作公告板

制作公告板，并将公告板的 parent 设为动态灯，这样公告板便可以有灯光一起动。

```cpp
node = smgr->addBillboardSceneNode(node, // parent
                                   core::dimension2d<f32>(50, 50) // size
); // position relative to its parent is (0, 0, 0)
node->setMaterialFlag(video::EMF_LIGHTING, false);
node->setMaterialType(video::EMT_TRANSPARENT_ADD_COLOR);
node->setMaterialTexture(0, driver->getTexture("../../media/particlewhite.bmp"));
```

{% include image.html url="/assets/images/210106-irrlicht-notes/20210106174952.png" %}


### 进一步为动态灯增加例子系统

* 创建粒子节点，并将其 parent 设为公告板，以便粒子系统更随公告板一起动。

```cpp
scene::IParticleSystemSceneNode * ps =smgr->addParticleSystemSceneNode (false, node);
```

* 创建粒子发射器，粒子发射器有多种，这里使用的是 box 发射器。

```cpp
scene::IParticleEmitter * em = ps->createBoxEmitter(
            core::aabbox3d<f32>(-3,0,-3,3,1,3), // emitter size the box
            core::vector3df(0.0f,0.06f,0.0f), // initial direction and speed
            80, // Minimal amount of particles emitted per second
            100, // Maximal amount of particles emitted per second
            video::SColor(0,255,255,255), // Minimal initial start color of a particle
            video::SColor(0,255,255,255), // Maximal initial start color of a particle
            800, 2000, // min and max age,
            0, //angle
            core::dimension2df(10.f,10.f), // min size
            core::dimension2df(20.f,20.f) // max size
);
ps->setEmitter(em); // this grabs the emitter
em->drop(); // so we can drop it here without deleting it
```

* 创建粒子淡出效果，粒子系统有很多效果，如 GravityAffector，利用这种效果可实现下雨，下雪的效果，这里使用的是淡出的效果。

```cpp
scene::IParticleAffector* paf = ps->createFadeOutParticleAffector();
ps->addAffector(paf); // same goes for the affector
paf->drop();
```

* 为粒子系统设置其他参数。

```cpp
ps->setPosition(core::vector3df(-70,60,40));
ps->setScale(core::vector3df(2,2,2));
ps->setMaterialFlag(video::EMF_LIGHTING, false);
ps->setMaterialFlag(video::EMF_ZWRITE_ENABLE, false);
ps->setMaterialTexture(0, driver->getTexture("../../media/fire.bmp"));
ps->setMaterialType(video::EMT_TRANSPARENT_VERTEX_ALPHA);
```

{% include image.html url="/assets/images/210106-irrlicht-notes/20210106175809.png" %}


## Render To Texture

Render to Texture 渲染到纹理：普通的图形渲染流程中，最终结果是渲染到帧缓存中，
最后显示到屏幕上，现在可以利用 FBO 等技术，把图像渲染到纹理中，然后可以把纹理
继续应用到场景绘制中，比如渲染一个场景 A 到纹理中，在另一个场景 B 的一个电视屏
幕上把刚才的纹理贴上去，就像是在播放 A 一样，再比如各种镜子中的景象也是一样道
理，阴影图（ shadow mapping ）也算是运用了 RTT。随着 GPU 的发展，RTT 还可以有更
多的应用，让用户更深入的参与到渲染流程中。（摘自石头的笔记）

* 创建一个纹理对象，作为 render target。

```cpp
rt = driver->addRenderTargetTexture(core::dimension2d<u32>(256,256), "RTT1");
```

* 将其设置为一个 node 的 texture。

```cpp
test->setMaterialTexture(0, rt);
```

* 在绘制之前设置 render target。

```cpp
driver->setRenderTarget(rt, true, true, video::SColor(0,0,0,255));
```

* 进行 render，此次 render 是将照相机看到的场景 render 到目标纹理上，即 `rtsmgr->drawAll();`
    一般情况下，需要设置两个照相机，一个是用于用户空间，一个用于纹理映射。同时在
    render 时，进行两次 render，第一次将用于纹理映射的相机设为活动摄像机，把场景 render
    到 texture 上，第二次将用户空间摄像机设为活动摄像机，将整个场景 render 到帧缓冲区，
    并显示到屏幕上。

{% include image.html url="/assets/images/210106-irrlicht-notes/20210106180333.png" %}


## 设置动态阴影

* 创建 device 时，打开缓冲区

```cpp
IrrlichtDevice *device =
createDevice( video::EDT_OPENGL, dimension2d<u32>(640, 480), 16, false, TRUE, false, 0);
```

* 创建物体

```cpp
mesh = smgr->getMesh("../../media/dwarf.x");
scene::IAnimatedMeshSceneNode* anode = 0;
anode = smgr->addAnimatedMeshSceneNode(mesh);
anode->setPosition(core::vector3df(-50,20,-60));
anode->setAnimationSpeed(15);
```

* 为物体设置阴影

```cpp
// add shadow
anode->addShadowVolumeSceneNode();
smgr->setShadowColor(video::SColor(150,0,0,0));
anode->setScale(core::vector3df(2,2,2));
anode->setMaterialFlag(video::EMF_NORMALIZE_NORMALS, true);
```

{% include image.html url="/assets/images/210106-irrlicht-notes/20210106180732.png" %}


## 利用灰度图创建地形


### 创建地形

创建地形：

```cpp
scene::ITerrainSceneNode* terrain = smgr->addTerrainSceneNode(
        "../../media/terrain-heightmap.bmp", // 高度图的文件名称
        0, // parent node
        -1, // node id
        core::vector3df(0.f, 0.f, 0.f), // position
        core::vector3df(0.f, 0.f, 0.f), // rotation
        core::vector3df(40.f, 4.4f, 40.f), // scale // 对地形进行放大
        video::SColor ( 255, 255, 255, 255 ), // vertexColor
        5, // maxLOD LOD (levels of detail)
        scene::ETPS_17, // patchSize 地形块大小
        4 // smoothFactor
);
terrain->setMaterialFlag(video::EMF_LIGHTING, false);
terrain->setMaterialTexture(0,
    driver->getTexture("../../media/terrain-texture.jpg"));
terrain->setMaterialTexture(1,
    driver->getTexture("../../media/detailmap3.jpg"));
terrain->setMaterialType(video::EMT_DETAIL_MAP);
terrain->scaleTexture(1.0f, 20.0f); // 第一层纹理保持不变，第二层纹理放大 20 倍
```


## LOD 技术

LOD 技术在不影响画面视觉效果的条件下，通过逐次简化景物的表面细节来减少场景的
几何复杂性，从而提高绘制算法的效率。该技术通常对每一原始多面体模型建立几个不同逼
近精度的几何模型。与原模型相比，每个模型均保留了一定层次细节。在绘制时，根据不同
的标准选择适当的层次模型来表示物体。


## 灰度图

灰度是指黑白图像中点的颜色深度，范围一般从 0 到 255，白色为 255，黑色为 0，故
黑白图片也称灰度图像，在医学、图像识别领域有很广泛的用途。
"灰度" 代表 DPI 的值，DPI 的意思是每平方英寸有多少象素点，象素点越大，图象的精确度越大，同时文件的尺寸
也越大，当然也不是 DPI 越大就越好，具体情况具体分析。

任何颜色都有红、绿、蓝三原色组成，假如原来某点的颜色为 RGB(R, G, B)，那么，
我们可以通过下面几种方法，将其转换为灰度：

1. 浮点算法：`Gray=R*0.3+G*0.59+B*0.11`
2. 整数方法：`Gray=(R*30+G*59+B*11)/100`
3. 移位方法：`Gray=(R*28+G*151+B*77)>>8`
4. 平均值法：`Gray=(R+G+B)/3`
5. 仅取绿色：`Gray=G`

通过上述任一种方法求得 Gray 后，将原来的 RGB(R,G,B) 中的 R,G,B 统一用 Gray 替换，
形成新的颜色 RGB(Gray,Gray,Gray)，用它替换原来的 RGB(R,G,B) 就是灰度图了。


## 几种贴图映射


### 法线贴图

Material type：EMT_NORMAL_MAP_SOLID

[法线贴图](http://blog.sina.com.cn/s/blog_5497d613010006qu.html)
根据这个参数作为 光照模型 亮度计算时候的参数。

{% include image.html url="/assets/images/210106-irrlicht-notes/u62p2t1d361616f14dt20040514101725.jpg" caption="采用色彩通道存储法线向量" %}

{% include image.html url="/assets/images/210106-irrlicht-notes/u62p2t1d361616f15dt20040514101725.jpg" caption="法线贴图的生成过程" %}


### 视差映射

Material type：EMT_PARALLAX_MAP_SOLID

[Parallax Mapping {% include relref_csdn.html %}](http://blog.csdn.net/soilwork/archive/2006/12/22/1452437.aspx)

作为实现 bump map 的技术之一，Parallax Mapping（视差映射）的目的同样也是让平坦表面实现凹凸效果。和 Normal Mapping 相比，Parallax Mapping 能实现更加真实和强烈的凹凸感。

* [视差贴图（Parallax Mapping） {% include relref_csdn.html %}](https://blog.csdn.net/happykocola/article/details/72812081)
* [视差贴图（Parallax Mapping） {% include relref_cnblogs.html %}](https://www.cnblogs.com/jim-game-dev/p/5410529.html) [blog {% include relref_github.html %}](https://chengkehan.github.io/ParallaxMapping.html)
* [视差贴图（Parallax Mapping） {% include relref_csdn.html %}](https://blog.csdn.net/weixin_30920091/article/details/96251306)


### 凹凸映射

凹凸映射和纹理映射非常相似。然而，纹理映射是把颜色加到多边形上，而凹凸映射
是把粗糙信息加到多边形上。
[凹凸映射 Bump Mapping {% include relref_csdn.html %}](http://blog.csdn.net/weili_2007/archive/2008/01/07/2028804.aspx)


### 纹理映射


## 经典的 Shading 技术

经典的 Shading 方式有三种，Lambert Shading（D3D 中称为 Flat Shading）、Gouraud Shading 和 Phong Shading。

* **Lambert Shading** ：最简单的一种方式， 在面片所依赖的顶点中选择其中一个作为整个面
    片的颜色，这种方式计算最快，但显示出的效果也最为粗糙，在视觉上面片与面片之间的边
    界过渡很突兀。
* **Gouraud Shading** ：首先计算出面片所依赖的顶点的颜色，然后根据面片上的位置对几个
    顶点的颜色进行插值计算所得，这种方法很好的提升了现实的效果，面片之间过渡相对自然。
* **Phong Shading** ：并不首先计算出各个顶点的颜色，而是直接根据面片上像素的位置对顶
    点的法线进行插值，然后根据插值所得的法线，依次计算面片上每个点的颜色，这样的计算
    更加精确，即使在面片很少的模型上颜色的表现和过渡也更平稳，当然所需的计算时间也相
    对要多些。

其实后两种 Shading 方式就是我们常说的逐顶点光照和逐像素光照，只不过那个是从
Shader 流程上区分并命名的而已，原理则是分别来自这两种不同的
Shading 方式的。


## Refs

- [1] [irrlicht 学习笔记 (6.21-6.24) -- zj](https://wenku.baidu.com/view/f3e3532bcfc789eb172dc8e0.html)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-06-irrlicht-notes.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://blog.sina.com.cn/s/blog_5497d613010006qu.html]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/blog.sina.com.cn/bc80254b.html" %})
- [http://blog.csdn.net/soilwork/archive/2006/12/22/1452437.aspx]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/blog.csdn.net/df7043bb.aspx" %})
- [https://blog.csdn.net/happykocola/article/details/72812081]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/blog.csdn.net/541773f9.html" %})
- [https://www.cnblogs.com/jim-game-dev/p/5410529.html]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/www.cnblogs.com/1bd51954.html" %})
- [https://chengkehan.github.io/ParallaxMapping.html]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/chengkehan.github.io/ca717f6a.html" %})
- [https://blog.csdn.net/weixin_30920091/article/details/96251306]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/blog.csdn.net/3bf38417.html" %})
- [http://blog.csdn.net/weili_2007/archive/2008/01/07/2028804.aspx]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/blog.csdn.net/733ae918.aspx" %})
- [https://wenku.baidu.com/view/f3e3532bcfc789eb172dc8e0.html]({% include relrefx.html url="/backup/2021-01-06-irrlicht-notes.md/wenku.baidu.com/53d6a8ae.html" %})
