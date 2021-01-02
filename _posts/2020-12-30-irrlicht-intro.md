---
layout: post
title: "Irrlicht 3D 笔记 -- Irrlicht 初探"
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
---

官网：<http://irrlicht.sourceforge.net/>

把所有官方 Tutorial 跑一遍，可以感受到作者对 OpenGL 底层的封装，一些思路。
截图有点困难，还专门写了一个小程序完成截图，每个 demo 都截了动态图，便于查阅。


## development code

version | svn addr | note
---- | ---- | ----
下一个版本 | svn://svn.code.sf.net/p/irrlicht/code/trunk | 可能不稳定或存在 api 变更
1.8.5 bugfix | svn://svn.code.sf.net/p/irrlicht/code/branches/releases/1.8 | 推荐这个
OpenGL ES | svn://svn.code.sf.net/p/irrlicht/code/branches/ogl-es | 实验性质


## Namespace List

irr | Everything
irr::core | vectors, planes, arrays, lists, and so on
irr::gui | graphical user interface
irr::io | Reading and writing files, accessing zip archives, xml files, ..
irr::scene | Mesh loading, special scene nodes like octrees and billboards, ..
irr::scene::quake3 | Quake3 map (.bsp)
irr::video | video driver

```cpp
#ifdef _IRR_WINDOWS_
#pragma comment(lib, "Irrlicht.lib")
#pragma comment(linker, "/subsystem:windows /ENTRY:mainCRTStartup")
#endif

int main();
```


## Tutorials

<table class="tablestyle" ntablew="3:8:2:3:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | :----: |
| [1.HelloWorld] | VideoDriver, GUIEnvironment and SceneManager. | easy | ![s001shot.jpg] |
| [2.Quake3Map] | 加载 Quake 3 map，创建 SceneNode 并优化渲染速度，创建可控相机位。 | easy | ![s002shot.jpg] |
| [3.Custom SceneNode] | 创建定制的 scene node，shader 写的。 | advanced | ![s003shot.jpg] |
| [4.Movement] | 移动 SceneNode，创建 SceneNode 动画 SceneNodeAnimators，也可以通过键盘控制移动。 | easy | ![s004shot.jpg] |
| [5.User Interface] | 用内建的 User Interface 创建 windows, buttons, scroll bars, static texts and list boxes。 | average | ![s005shot.jpg] |
| [6.2D Graphics] | 2d graphics，draw images, keycolor based sprites, transparent rectangles and different fonts. | easy | ![s006shot.jpg] |
| [7.Collision] | collision 检测，三种方法：stair climbing，拾取三角形，拾取 scene node。 | average | ![s007shot.jpg] |
| [8.SpecialFX] | 特效演示。深度缓冲阴影，粒子系统，广告牌，动态光，水表面。 | average | ![s008shot.jpg] |
| [9.MeshViewer] | mesh viewer。涉及用户接口和场景管理。 | advanced | ![s009.jpg] |
| [10.Shaders] | shaders for D3D8, D3D9 and OpenGL。创建 shader material，关闭 texture mipmaps，使用 text scene nodes。 | advanced | ![s010shot.jpg] |
| [11.Per Pixel Lighting] | 复杂 material。用 normal maps and parallax mapping 计算每个像素的光照。烟雾的使用，和移动粒子系统。 | average | ![s011shot.jpg] |
| [12.Terrain Rendering] | 地形渲染。用地形三角进行物理碰撞检测。 | easy | ![s012shot.jpg] |
| [13.Render To Texture] | 渲染到一个纹理。使用 specular highlights。 | average | ![s013shot.jpg] |
| [14.Win32 window] | win32 窗口中使用引擎。 | easy | ![s014shot.jpg] |
| [15.Load .irr file] | 使用 .irr files。 | easy | ![s015shot.jpg] |
| [16.Quake3Map Shader] | q3 map 特效和加载。 | average | ![s016shot.jpg] |
| [17.Hello World Mobile] | Windows CE 样例。 | advanced | ![s017shot.jpg] |
| [18.SplitScreen] | split screen 演示。 | average | ![s018shot.jpg] |
| [19.Mouse And Joystick] | 手柄和鼠标的使用。 | easy | ![s019shot.jpg] |
| [20.Managed Lights] | 多光源管理。根据场景选择合适的光源。 | advanced | ![s020shot.jpg] |
| [21.Quake3Explorer] | q3 map 浏览器。可以完成管理。 | advanced | ![s021shot.jpg] |
| [22.MaterialViewer] | material 测试，可以手工编辑。 | easy | ![s022shot.jpg] |
| [23.SMeshHandling] | 手工创建 meshes，支持定制处理。 | average | ![s023shot.jpg] |
| [24.CursorControl] | 修改 鼠标 cursors。 | x | ![024shot.jpg] |
| [25.XmlHandling] | XML 的使用，可以用来加载和保存配置。 | x | ![025shot.jpg] |
| [26.OcclusionQuery] | 用 OcclusionQuery 渲染加速。超出视距的节点不绘制。 | x | ![026shot.jpg] |
| [27.PostProcessing] | 创建屏幕双缓冲。颜色反转，用 HLSL and GLSL 写的。 | x | ![] |
| [28.CubeMapping] | cubemap textures 使用，和环境 mapping。 | x | ![] |
| [29.HardwareSkinning] | HardwareSkinning | x | ![] |
| [30.Profiling] | 一些 profiling tools。 | x | ![] |
| [Demo] | 一个完整的游戏 demo。 | x | ![] |

[1.HelloWorld]: http://irrlicht.sourceforge.net/docu/example001.html
[2.Quake3Map]: http://irrlicht.sourceforge.net/docu/example002.html
[3.Custom SceneNode]: http://irrlicht.sourceforge.net/docu/example003.html
[4.Movement]: http://irrlicht.sourceforge.net/docu/example004.html
[5.User Interface]: http://irrlicht.sourceforge.net/docu/example005.html
[6.2D Graphics]: http://irrlicht.sourceforge.net/docu/example006.html
[7.Collision]: http://irrlicht.sourceforge.net/docu/example007.html
[8.SpecialFX]: http://irrlicht.sourceforge.net/docu/example008.html
[9.MeshViewer]: http://irrlicht.sourceforge.net/docu/example009.html
[10.Shaders]: http://irrlicht.sourceforge.net/docu/example010.html
[11.Per Pixel Lighting]: http://irrlicht.sourceforge.net/docu/example011.html
[12.Terrain Rendering]: http://irrlicht.sourceforge.net/docu/example012.html
[13.Render To Texture]: http://irrlicht.sourceforge.net/docu/example013.html
[14.Win32 window]: http://irrlicht.sourceforge.net/docu/example014.html
[15.Load .irr file]: http://irrlicht.sourceforge.net/docu/example015.html
[16.Quake3Map Shader]: http://irrlicht.sourceforge.net/docu/example016.html
[17.Hello World Mobile]: http://irrlicht.sourceforge.net/docu/example017.html
[18.SplitScreen]: http://irrlicht.sourceforge.net/docu/example018.html
[19.Mouse And Joystick]: http://irrlicht.sourceforge.net/docu/example019.html
[20.Managed Lights]: http://irrlicht.sourceforge.net/docu/example020.html
[21.Quake3Explorer]: http://irrlicht.sourceforge.net/docu/example021.html
[22.MaterialViewer]: http://irrlicht.sourceforge.net/docu/example022.html
[23.SMeshHandling]: http://irrlicht.sourceforge.net/docu/example023.html

[24.CursorControl]: http://irrlicht.sourceforge.net/docu/example024.html
[25.XmlHandling]: http://irrlicht.sourceforge.net/docu/example025.html
[26.OcclusionQuery]: http://irrlicht.sourceforge.net/docu/example026.html

[s001shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s001shot.jpg" %}
[s002shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s002shot.jpg" %}
[s003shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s003shot.jpg" %}
[s004shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s004shot.jpg" %}
[s005shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s005shot.jpg" %}
[s006shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s006shot.jpg" %}
[s007shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s007shot.jpg" %}
[s008shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s008shot.jpg" %}
[s009shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s009shot.jpg" %}
[s010shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s010shot.jpg" %}
[s011shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s011shot.jpg" %}
[s012shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s012shot.jpg" %}
[s013shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s013shot.jpg" %}
[s014shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s014shot.jpg" %}
[s015shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s015shot.jpg" %}
[s016shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s016shot.jpg" %}
[s017shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s017shot.jpg" %}
[s018shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s018shot.jpg" %}

[s019shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s019shot.jpg" %}
[s020shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s020shot.jpg" %}
[s021shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s021shot.jpg" %}
[s022shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s022shot.jpg" %}
[s023shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s023shot.jpg" %}

[024shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/024shot.jpg" %}
[025shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/025shot.jpg" %}
[026shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/026shot.jpg" %}


## External Tutorials

<table class="tablestyle" ntablew="3:8:2:3:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | :----: |
| [DevCpp] | Dev C++ 使用。 | easy | ![s001bshot.jpg] |
| [Code::Blocks] | Code::Blocks IDE 使用。 | easy | ![codeblocks.jpg] |
| [Codewarrior] | Metroworks Codewarrior 使用。 | easy | ![s001cshot.jpg] |
| [ODE Integration] | 物理引擎 ODE。 | advanced | ![odelogo.jpg] |
| [Tokamak Integration] | 物理引擎 Tokamak。 | advanced | ![s008bshot.jpg] |
| [PhysX Integration] | 物理引擎 Ageia PhysX （Novodex）。 | advanced | ![physx.jpg] |
| [Newton Integration] | 物理引擎 Newton Game Dynamics。 | advanced | ![newston.jpg] |
| [Newton DevC++ Integration] | Dev-C++，物理引擎 Newton Physics SDK。 | average | ![devcpp_newton.jpg] |

[DevCpp]: http://irrlicht.sourceforge.net/tut_devcpp.html)
[Code::Blocks]: http://irrlicht.sourceforge.net/tut_codeblocks.html)
[Codewarrior]: http://irrlicht.sourceforge.net/tut_codew.html)
[ODE Integration]: http://irrlicht.sourceforge.net/tut_ode.html)
[Tokamak Integration]: http://irrlicht.sourceforge.net/tut_toka.html)
[PhysX Integration]: http://irrlicht.sourceforge.net/tut_physx.html)
[Newton Integration]: http://irrlicht.sourceforge.net/tut_newton.html)
[Newton DevC++ Integration]: http://irrlicht.sourceforge.net/tut_newtondevcpp.html)

[s001bshot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s001bshot.jpg" %}
[codeblocks.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/codeblocks.jpg" %}
[s001cshot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s001cshot.jpg" %}
[odelogo.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/odelogo.jpg" %}
[s008bshot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s008bshot.jpg" %}
[physx.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/physx.jpg" %}
[newston.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/newston.jpg" %}
[devcpp_newton.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/devcpp_newton.jpg" %}


## Hello World $code$

```cpp
#ifdef _MSC_VER
#pragma comment(lib, "Irrlicht.lib")
#pragma comment(linker, "/subsystem:windows /ENTRY:mainCRTStartup")
#endif

#include <irrlicht.h>
#include "exampleHelper.h"

using namespace irr;
using namespace core;
using namespace scene;
using namespace video;
using namespace io;
using namespace gui;

int main() {
    IrrlichtDevice* device = createDevice(video::EDT_OPENGL, dimension2d<u32>(640, 480), 16, false, false, false, 0);
    device->setWindowCaption(L"Hello World! - Irrlicht Engine Demo");

    IVideoDriver* driver = device->getVideoDriver();
    ISceneManager* smgr = device->getSceneManager();
    IGUIEnvironment* guienv = device->getGUIEnvironment();

    guienv->addStaticText(L"Hello World! This is Irrlicht with the burnings software renderer!", rect<s32>(10, 10, 260, 22), true);

    const io::path mediaPath = getExampleMediaPath();
    IAnimatedMesh* mesh = smgr->getMesh(mediaPath + "sydney.md2");
    IAnimatedMeshSceneNode* node = smgr->addAnimatedMeshSceneNode(mesh);
    if (node) {
        node->setMaterialFlag(EMF_LIGHTING, false);
        node->setMD2Animation(scene::EMAT_STAND);
        node->setMaterialTexture(0, driver->getTexture(mediaPath + "sydney.bmp"));
    }

    smgr->addCameraSceneNode(0, vector3df(0, 30, -40), vector3df(0, 5, 0));
    while (device->run()) {
        driver->beginScene(ECBF_COLOR | ECBF_DEPTH, SColor(255, 100, 101, 140));
        smgr->drawAll();
        guienv->drawAll();
        driver->endScene();
    }

    device->drop();
    return 0;
}
```

<p class="counter-reset h2counter"></p>


## Tutorial 1: HelloWorld

{% include image.html url="/assets/images/201230-irrlicht-intro/01.helloworld.webp" %}


## Tutorial 2: Quake3Map

{% include image.html url="/assets/images/201230-irrlicht-intro/02.quake3map_4.webp" %}


## Tutorial 3: Custom SceneNode

{% include image.html url="/assets/images/201230-irrlicht-intro/03.customscenenode.webp" %}


## Tutorial 4: Movement

{% include image.html url="/assets/images/201230-irrlicht-intro/04.movement.webp" %}


## Tutorial 5: User Interface

{% include image.html url="/assets/images/201230-irrlicht-intro/05.userinterface_2.webp" %}


## Tutorial 6: 2D Graphics

{% include image.html url="/assets/images/201230-irrlicht-intro/06.2dgraphics_2.webp" %}


## Tutorial 7: Collision

{% include image.html url="/assets/images/201230-irrlicht-intro/07.collision_4.webp" %}


## Tutorial 8: SpecialFX

{% include image.html url="/assets/images/201230-irrlicht-intro/08.specialfx_3.webp" %}


## Tutorial 9: Mesh Viewer

{% include image.html url="/assets/images/201230-irrlicht-intro/09.meshviewer_2.webp" %}


## Tutorial 10: Shaders

{% include image.html url="/assets/images/201230-irrlicht-intro/10.shaders_2.webp" %}


## Tutorial 11: Per-Pixel Lighting

{% include image.html url="/assets/images/201230-irrlicht-intro/11.perpixellighting_4.webp" %}


## Tutorial 12: Terrain Rendering

{% include image.html url="/assets/images/201230-irrlicht-intro/12.terrainrendering.webp" %}


## Tutorial 13: Render To Texture

{% include image.html url="/assets/images/201230-irrlicht-intro/13.rendertotexture.webp" %}


## Tutorial 14: Win32 Window

{% include image.html url="/assets/images/201230-irrlicht-intro/14.win32window.webp" %}


## Tutorial 15: Loading Scenes from .irr Files

{% include image.html url="/assets/images/201230-irrlicht-intro/15.loadirrfile_2.webp" %}


## Tutorial 16: Quake3 Map Shader Support

{% include image.html url="/assets/images/201230-irrlicht-intro/16.quake3mapshader_3.webp" %}


## Tutorial 17: Helloworld mobile


## Tutorial 18: Splitscreen

{% include image.html url="/assets/images/201230-irrlicht-intro/18.splitscreen_3.webp" %}


## Tutorial 19: Mouse and Joystick

{% include image.html url="/assets/images/201230-irrlicht-intro/19.mouseandjoystick.webp" %}


## Tutorial 20: Managed Lights

{% include image.html url="/assets/images/201230-irrlicht-intro/20.managedlights_2.webp" %}


## Tutorial 21: Quake3 Explorer

{% include image.html url="/assets/images/201230-irrlicht-intro/21.quake3explorer.webp" %}


## Tutorial 22: Material Viewer

{% include image.html url="/assets/images/201230-irrlicht-intro/22.materialviewer.webp" %}


## Tutorial 23: SMeshBufferHandling

{% include image.html url="/assets/images/201230-irrlicht-intro/23.smeshhandling.webp" %}


## Tutorial 24: CursorControl

{% include image.html url="/assets/images/201230-irrlicht-intro/24.cursorcontrol.webp" %}


## Tutorial 25: Xml Handling

{% include image.html url="/assets/images/201230-irrlicht-intro/25.xmlhandling.webp" %}


## Tutorial 26: OcclusionQuery

{% include image.html url="/assets/images/201230-irrlicht-intro/26.occlusionquery.webp" %}


## 27.PostProcessing

{% include image.html url="/assets/images/201230-irrlicht-intro/27.postprocessing.webp" %}


## 28.CubeMapping

{% include image.html url="/assets/images/201230-irrlicht-intro/28.cubemapping_4.webp" %}


## 29.HardwareSkinning


## 30.Profiling

{% include image.html url="/assets/images/201230-irrlicht-intro/30.profiling.webp" %}


## Demo

{% include image.html url="/assets/images/201230-irrlicht-intro/demo_start.webp" %}
{% include image.html url="/assets/images/201230-irrlicht-intro/demo_4.webp" %}


## fonttool & guieditor

{% include image.html url="/assets/images/201230-irrlicht-intro/fonttool.webp" %}

{% include image.html url="/assets/images/201230-irrlicht-intro/guieditor.webp" %}


## MeshConverter.exe

```
Usage: MeshConverter.exe [options] <srcFile> <destFile>
  where options are
 --createTangents: convert to tangents mesh is possible.
 --format=[irrmesh|collada|stl|obj|ply]: Choose target format
```

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [http://irrlicht.sourceforge.net/]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/4ce0a4f4.html" %})
- [2] [http://irrlicht.sourceforge.net/docu/example001.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cf015d5.html" %})
- [3] [http://irrlicht.sourceforge.net/docu/example002.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d470f08f.html" %})
- [4] [http://irrlicht.sourceforge.net/docu/example003.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/016d2c90.html" %})
- [5] [http://irrlicht.sourceforge.net/docu/example004.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/734c770b.html" %})
- [6] [http://irrlicht.sourceforge.net/docu/example005.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/2e6df6d0.html" %})
- [7] [http://irrlicht.sourceforge.net/docu/example006.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cafcd71.html" %})
- [8] [http://irrlicht.sourceforge.net/docu/example007.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d16644d7.html" %})
- [9] [http://irrlicht.sourceforge.net/docu/example008.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f6b6c656.html" %})
- [10] [http://irrlicht.sourceforge.net/docu/example009.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/5d639f5c.html" %})
- [11] [http://irrlicht.sourceforge.net/docu/example010.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/56533bae.html" %})
- [12] [http://irrlicht.sourceforge.net/docu/example011.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/7e014783.html" %})
- [13] [http://irrlicht.sourceforge.net/docu/example012.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/5038a4d2.html" %})
- [14] [http://irrlicht.sourceforge.net/docu/example013.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/908b2729.html" %})
- [15] [http://irrlicht.sourceforge.net/docu/example014.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/70f4ca86.html" %})
- [16] [http://irrlicht.sourceforge.net/docu/example015.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/fc98dca0.html" %})
- [17] [http://irrlicht.sourceforge.net/docu/example016.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/dc3bbbb3.html" %})
- [18] [http://irrlicht.sourceforge.net/docu/example017.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/65d43334.html" %})
- [19] [http://irrlicht.sourceforge.net/docu/example018.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d74639c1.html" %})
- [20] [http://irrlicht.sourceforge.net/docu/example019.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/c270d6b4.html" %})
- [21] [http://irrlicht.sourceforge.net/docu/example020.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d80461a3.html" %})
- [22] [http://irrlicht.sourceforge.net/docu/example021.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cfa7b9f.html" %})
- [23] [http://irrlicht.sourceforge.net/docu/example022.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/6e7ceb41.html" %})
- [24] [http://irrlicht.sourceforge.net/docu/example023.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/e6faf851.html" %})
- [25] [http://irrlicht.sourceforge.net/docu/example024.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/30c4976c.html" %})
- [26] [http://irrlicht.sourceforge.net/docu/example025.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/2872869b.html" %})
- [27] [http://irrlicht.sourceforge.net/docu/example026.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/e17a2c6d.html" %})
- [28] [http://irrlicht.sourceforge.net/tut_devcpp.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f1b6649e.html" %})
- [29] [http://irrlicht.sourceforge.net/tut_codeblocks.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/959cf6e9.html" %})
- [30] [http://irrlicht.sourceforge.net/tut_codew.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a455348c.html" %})
- [31] [http://irrlicht.sourceforge.net/tut_ode.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f195a7b1.html" %})
- [32] [http://irrlicht.sourceforge.net/tut_toka.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/b00f362b.html" %})
- [33] [http://irrlicht.sourceforge.net/tut_physx.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/7270aa13.html" %})
- [34] [http://irrlicht.sourceforge.net/tut_newton.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/ac6f4f9d.html" %})
- [35] [http://irrlicht.sourceforge.net/tut_newtondevcpp.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a2cfe98f.html" %})
