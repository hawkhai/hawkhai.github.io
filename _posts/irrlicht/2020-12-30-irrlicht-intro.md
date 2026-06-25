---
layout: post
title: "3D 引擎 Irrlicht -- Irrlicht 3D 所有 Tutorial 动态图概览"
author:
location: "珠海"
categories: ["3D 引擎"]
tags: ["Irrlicht", "图形学"]
toc: true
toclistyle: none
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

官网：<http://irrlicht.sourceforge.net/>

把所有官方 Tutorial 跑一遍，可以感受到作者对 OpenGL 底层的封装，一些思路。对 Irrlicht 的能力，也能有一个整体感知。
截图有点困难，还专门写了一个小程序完成截图，每个 demo 都截了动态图，便于查阅。

花了两天完成，Irrlicht 3D 所有 Tutorial 动态图概览。🐬


## development code

<table class="tablestyle" ntablew="2:8:3"></table>

version | svn addr | note
---- | ---- | ----
下一个版本 | svn://svn.code.sf.net/p/irrlicht/code/trunk | 可能不稳定或存在 api 变更
1.8.5 bugfix | svn://svn.code.sf.net/p/irrlicht/code/branches/releases/1.8 | 推荐这个
OpenGL ES | svn://svn.code.sf.net/p/irrlicht/code/branches/ogl-es | 实验性质


## Namespace List

<table class="tablestyle" ntablew="2:8"></table>

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

<table class="tablestyle" ntablew="3:8:2:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | :----: |
| [1.HelloWorld] | VideoDriver, GUIEnvironment and SceneManager. | 简单 | ![s001shot.jpg] |
| [2.Quake3Map] | 加载 Quake 3 map，创建 SceneNode 并优化渲染速度，创建可控相机位。 | 简单 | ![s002shot.jpg] |
| [3.Custom SceneNode] | 创建定制的 scene node，shader 写的。 | 高级的 | ![s003shot.jpg] |
| [4.Movement] | 移动 SceneNode，创建 SceneNode 动画 SceneNodeAnimators，也可以通过键盘控制移动。 | 简单 | ![s004shot.jpg] |
| [5.User Interface] | 用内建的 User Interface 创建 windows, buttons, scroll bars, static texts and list boxes。 | 平均的 | ![s005shot.jpg] |
| [6.2D Graphics] | 2d graphics, draw images, keycolor based sprites, transparent rectangles and different fonts. | 简单 | ![s006shot.jpg] |
| [7.Collision] | collision 检测，三种方法：stair climbing，拾取三角形，拾取 scene node。 | 平均的 | ![s007shot.jpg] |
| [8.SpecialFX] | 特效演示。深度缓冲阴影，粒子系统，广告牌，动态光，水表面。 | 平均的 | ![s008shot.jpg] |
| [9.MeshViewer] | mesh viewer。涉及用户接口和场景管理。 | 高级的 | ![s009shot.jpg] |
| [10.Shaders] | shaders for D3D8, D3D9 and OpenGL。创建 shader material，关闭 texture mipmaps，使用 text scene nodes。 | 高级的 | ![s010shot.jpg] |
| [11.Per Pixel Lighting] | 复杂 material。用 normal maps and parallax mapping 计算每个像素的光照。烟雾的使用，和移动粒子系统。 | 平均的 | ![s011shot.jpg] |
| [12.Terrain Rendering] | 地形渲染。用地形三角进行物理碰撞检测。 | 简单 | ![s012shot.jpg] |
| [13.Render To Texture] | 渲染到一个纹理。使用 specular highlights。 | 平均的 | ![s013shot.jpg] |
| [14.Win32 window] | win32 窗口中使用引擎。 | 简单 | ![s014shot.jpg] |
| [15.Load .irr file] | 使用 .irr files。 | 简单 | ![s015shot.jpg] |
| [16.Quake3Map Shader] | q3 map 特效和加载。 | 平均的 | ![s016shot.jpg] |
| [17.Hello World Mobile] | Windows CE 样例。 | 高级的 | ![s017shot.jpg] |
| [18.SplitScreen] | split screen 演示。 | 平均的 | ![s018shot.jpg] |
| [19.Mouse And Joystick] | 手柄和鼠标的使用。 | 简单 | ![s019shot.jpg] |
| [20.Managed Lights] | 多光源管理。根据场景选择合适的光源。 | 高级的 | ![s020shot.jpg] |
| [21.Quake3Explorer] | q3 map 浏览器。可以完成管理。 | 高级的 | ![s021shot.jpg] |
| [22.MaterialViewer] | material 测试，可以手工编辑。 | 简单 | ![s022shot.jpg] |
| [23.SMeshHandling] | 手工创建 meshes，支持定制处理。 | 平均的 | ![s023shot.jpg] |
| [24.CursorControl] | 修改 鼠标 cursors。 |  | ![024shot.jpg] |
| [25.XmlHandling] | XML 的使用，可以用来加载和保存配置。 |  | ![025shot.jpg] |
| [26.OcclusionQuery] | 用 OcclusionQuery 渲染加速。超出视距的节点不绘制。 |  | ![026shot.jpg] |
| [27.PostProcessing] | 创建屏幕双缓冲。颜色反转，用 HLSL and GLSL 写的。 |  | ![027shot.jpg] |
| [28.CubeMapping] | cubemap textures 使用，和环境 mapping。 |  | ![028shot.jpg] |
| [29.HardwareSkinning] | HardwareSkinning |  | ![029shot.jpg] |
| [30.Profiling] | 一些 profiling tools。 |  | ![030shot.jpg] |
| [Demo] | 一个完整的游戏 demo。 |  | ![demoshot.jpg] |

[1.HelloWorld]: <http://irrlicht.sourceforge.net/docu/example001.html>
[2.Quake3Map]: <http://irrlicht.sourceforge.net/docu/example002.html>
[3.Custom SceneNode]: <http://irrlicht.sourceforge.net/docu/example003.html>
[4.Movement]: <http://irrlicht.sourceforge.net/docu/example004.html>
[5.User Interface]: <http://irrlicht.sourceforge.net/docu/example005.html>
[6.2D Graphics]: <http://irrlicht.sourceforge.net/docu/example006.html>
[7.Collision]: <http://irrlicht.sourceforge.net/docu/example007.html>
[8.SpecialFX]: <http://irrlicht.sourceforge.net/docu/example008.html>
[9.MeshViewer]: <http://irrlicht.sourceforge.net/docu/example009.html>
[10.Shaders]: <http://irrlicht.sourceforge.net/docu/example010.html>
[11.Per Pixel Lighting]: <http://irrlicht.sourceforge.net/docu/example011.html>
[12.Terrain Rendering]: <http://irrlicht.sourceforge.net/docu/example012.html>
[13.Render To Texture]: <http://irrlicht.sourceforge.net/docu/example013.html>
[14.Win32 window]: <http://irrlicht.sourceforge.net/docu/example014.html>
[15.Load .irr file]: <http://irrlicht.sourceforge.net/docu/example015.html>
[16.Quake3Map Shader]: <http://irrlicht.sourceforge.net/docu/example016.html>
[17.Hello World Mobile]: <http://irrlicht.sourceforge.net/docu/example017.html>
[18.SplitScreen]: <http://irrlicht.sourceforge.net/docu/example018.html>
[19.Mouse And Joystick]: <http://irrlicht.sourceforge.net/docu/example019.html>
[20.Managed Lights]: <http://irrlicht.sourceforge.net/docu/example020.html>
[21.Quake3Explorer]: <http://irrlicht.sourceforge.net/docu/example021.html>
[22.MaterialViewer]: <http://irrlicht.sourceforge.net/docu/example022.html>
[23.SMeshHandling]: <http://irrlicht.sourceforge.net/docu/example023.html>

[24.CursorControl]: <http://irrlicht.sourceforge.net/docu/example024.html>
[25.XmlHandling]: <http://irrlicht.sourceforge.net/docu/example025.html>
[26.OcclusionQuery]: <http://irrlicht.sourceforge.net/docu/example026.html>

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

[s019shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/019shot.jpg" %}
[s020shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/020shot.jpg" %}
[s021shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/021shot.jpg" %}
[s022shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/022shot.jpg" %}
[s023shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/023shot.jpg" %}

[024shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/024shot.jpg" %}
[025shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/025shot.jpg" %}
[026shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/026shot.jpg" %}

[027shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/027shot.jpg" %}
[028shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/028shot.jpg" %}
[029shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s023shot.jpg" %}
[030shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/030shot.png" %}
[demoshot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/demoshot.png" %}


## External Tutorials

<table class="tablestyle" ntablew="3:8:2:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | :----: |
| [DevCpp] | Dev C++ 使用。 | 简单 | ![s001bshot.jpg] |
| [Code::Blocks] | Code::Blocks IDE 使用。 | 简单 | ![codeblocks.jpg] |
| [Codewarrior] | Metroworks Codewarrior 使用。 | 简单 | ![s001cshot.jpg] |
| [ODE Integration] | 物理引擎 ODE。 | 高级的 | ![odelogo.jpg] |
| [Tokamak Integration] | 物理引擎 Tokamak。 | 高级的 | ![s008bshot.jpg] |
| [PhysX Integration] | 物理引擎 Ageia PhysX （Novodex）。 | 高级的 | ![physx.jpg] |
| [Newton Integration] | 物理引擎 Newton Game Dynamics。 | 高级的 | ![newston.jpg] |
| [Newton DevC++ Integration] | Dev-C++，物理引擎 Newton Physics SDK。 | 平均的 | ![devcpp_newton.jpg] |

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

VideoDriver, GUIEnvironment and SceneManager.

{% include image.html url="/assets/images/201230-irrlicht-intro/01.helloworld.webp" urlx="/assets/images/201230-irrlicht-intro/001shot.jpg" %}


## Tutorial 2: Quake3Map

加载 Quake 3 map，创建 SceneNode 并优化渲染速度，创建可控相机位。

{% include image.html url="/assets/images/201230-irrlicht-intro/02.quake3map_4.webp" urlx="/assets/images/201230-irrlicht-intro/002shot.jpg" %}


## Tutorial 3: Custom SceneNode

创建定制的 scene node，没有用到 shader。

{% include image.html url="/assets/images/201230-irrlicht-intro/03.customscenenode.webp" urlx="/assets/images/201230-irrlicht-intro/003shot.jpg" %}


## Tutorial 4: Movement

移动 SceneNode，创建 SceneNode 动画 SceneNodeAnimators，也可以通过键盘控制移动。

{% include image.html url="/assets/images/201230-irrlicht-intro/04.movement.webp" urlx="/assets/images/201230-irrlicht-intro/004shot.jpg" %}


## Tutorial 5: User Interface

用内建的 User Interface 创建 windows, buttons, scroll bars, static texts and list boxes。

{% include image.html url="/assets/images/201230-irrlicht-intro/05.userinterface_2.webp" urlx="/assets/images/201230-irrlicht-intro/005shot.jpg" %}


## Tutorial 6: 2D Graphics

2d graphics, draw images, keycolor based sprites, transparent rectangles and different fonts.

{% include image.html url="/assets/images/201230-irrlicht-intro/06.2dgraphics_2.webp" urlx="/assets/images/201230-irrlicht-intro/006shot.jpg" %}


## Tutorial 7: Collision

collision 检测，三种方法：stair climbing，拾取三角形，拾取 scene node。

{% include image.html url="/assets/images/201230-irrlicht-intro/07.collision_4.webp" urlx="/assets/images/201230-irrlicht-intro/007shot.jpg" %}


## Tutorial 8: SpecialFX

特效演示。深度缓冲阴影，粒子系统，广告牌，动态光，水表面。

{% include image.html url="/assets/images/201230-irrlicht-intro/08.specialfx_3.webp" urlx="/assets/images/201230-irrlicht-intro/008shot.jpg" %}


## Tutorial 9: Mesh Viewer

mesh viewer。涉及用户接口和场景管理。

{% include image.html url="/assets/images/201230-irrlicht-intro/09.meshviewer_2.webp" urlx="/assets/images/201230-irrlicht-intro/009shot.jpg" %}


## Tutorial 10: Shaders

shaders for D3D8, D3D9 and OpenGL。创建 shader material，关闭 texture mipmaps，使用 text scene nodes。

{% include image.html url="/assets/images/201230-irrlicht-intro/10.shaders_2.webp" urlx="/assets/images/201230-irrlicht-intro/010shot.jpg" %}


## Tutorial 11: Per-Pixel Lighting

逐像素光照、雾、移动光、粒子。复杂 material。用 normal maps and parallax mapping 计算每个像素的光照。烟雾的使用，和移动粒子系统。
[Irrlicht 学习笔记 (10)--PerPixelLighting {% include relref_csdn.html %}](https://blog.csdn.net/gqkly/article/details/51870182)

{% include image.html url="/assets/images/201230-irrlicht-intro/11.perpixellighting_4.webp" urlx="/assets/images/201230-irrlicht-intro/011shot.jpg" %}


## Tutorial 12: Terrain Rendering

地形渲染。用地形三角进行物理碰撞检测。

{% include image.html url="/assets/images/201230-irrlicht-intro/12.terrainrendering.webp" urlx="/assets/images/201230-irrlicht-intro/012shot.jpg" %}


## Tutorial 13: Render To Texture

渲染到一个纹理。使用 specular highlights。

{% include image.html url="/assets/images/201230-irrlicht-intro/13.rendertotexture.webp" urlx="/assets/images/201230-irrlicht-intro/013shot.jpg" %}


## Tutorial 14: Win32 Window

win32 窗口中使用引擎。

{% include image.html url="/assets/images/201230-irrlicht-intro/14.win32window.webp" urlx="/assets/images/201230-irrlicht-intro/014shot.jpg" %}


## Tutorial 15: Loading Scenes from .irr Files

使用 .irr files。

{% include image.html url="/assets/images/201230-irrlicht-intro/15.loadirrfile_2.webp" urlx="/assets/images/201230-irrlicht-intro/015shot.jpg" %}


## Tutorial 16: Quake3 Map Shader Support

q3 map 特效和加载。

{% include image.html url="/assets/images/201230-irrlicht-intro/16.quake3mapshader_3.webp" urlx="/assets/images/201230-irrlicht-intro/016shot.jpg" %}


## Tutorial 17: Helloworld mobile

Windows CE 样例。

{% include image.html url="/assets/images/201230-irrlicht-intro/017shot.jpg" %}


## Tutorial 18: Splitscreen

split screen 演示。分屏技术。将视口分为 4 部分，三个显示 fixed camera 和一个用户控制 camera。
[Irrlicht 引擎学习笔记 (14)--Splitscreen {% include relref_csdn.html %}](https://blog.csdn.net/gqkly/article/details/51870581)

{% include image.html url="/assets/images/201230-irrlicht-intro/18.splitscreen_3.webp" urlx="/assets/images/201230-irrlicht-intro/018shot.jpg" %}


## Tutorial 19: Mouse and Joystick

手柄和鼠标的使用。

{% include image.html url="/assets/images/201230-irrlicht-intro/19.mouseandjoystick.webp" urlx="/assets/images/201230-irrlicht-intro/019shot.jpg" %}


## Tutorial 20: Managed Lights

多光源管理。根据场景选择合适的光源。

光源管理器。为了使用超过 8 个的灯光，注册一个可选光源管理器，允许可以在渲染的时候开关特定灯光。
如果没有注册光源管理器，默认的基于距离（距离照相机）的流程将被激活。

* NO_MANAGEMENT: 关闭光源管理器，展示引擎默认的光源行为。将依据照相机与灯光距离，选择最近的 8 个光源。
* LIGHTS_NEAREST_NODE: 展示为每个场景节点启用有限数量的光源。如果为正在渲染的节点找到了三个光源，启用它们而关闭其他的光源，这里可行。
    但是应用到整个场景，就处理不好了。会看到闪烁现象，这是由于光源在切换其所关联的节点造成的。
* LIGHTS_IN_ZONE: 展示依据 "zone" 来开关光源的技术。每个空的场景节点作为一个 zone 的父节点。
    当节点被渲染的时候，关闭所有光源，找到父 "zone" 节点并打开在其内的光源。
    这能为每个节点实现，实现本地光源的效果。这可以用于单个房间内绑定本地光源，而每个房间光源与其他房间的光源是隔离的。

[Irrlicht 引擎学习笔记 (15)--LightManager {% include relref_csdn.html %}](https://blog.csdn.net/gqkly/article/details/51870636)

{% include image.html url="/assets/images/201230-irrlicht-intro/20.managedlights_2.webp" urlx="/assets/images/201230-irrlicht-intro/020shot.jpg" %}


## Tutorial 21: Quake3 Explorer

q3 map 浏览器。可以完成管理。

{% include image.html url="/assets/images/201230-irrlicht-intro/21.quake3explorer.webp" urlx="/assets/images/201230-irrlicht-intro/021shot.jpg" %}


## Tutorial 22: Material Viewer

material 测试，可以手工编辑。

{% include image.html url="/assets/images/201230-irrlicht-intro/22.materialviewer.webp" urlx="/assets/images/201230-irrlicht-intro/022shot.jpg" %}


## Tutorial 23: SMeshBufferHandling

手工创建 meshes，支持定制处理。

{% include image.html url="/assets/images/201230-irrlicht-intro/23.smeshhandling.webp" urlx="/assets/images/201230-irrlicht-intro/023shot.jpg" %}


## Tutorial 24: CursorControl

修改 鼠标 cursors。

{% include image.html url="/assets/images/201230-irrlicht-intro/24.cursorcontrol.webp" urlx="/assets/images/201230-irrlicht-intro/024shot.jpg" %}


## Tutorial 25: Xml Handling

XML 的使用，可以用来加载和保存配置。

{% include image.html url="/assets/images/201230-irrlicht-intro/25.xmlhandling.webp" urlx="/assets/images/201230-irrlicht-intro/025shot.jpg" %}


## Tutorial 26: OcclusionQuery

用 OcclusionQuery 渲染加速。超出视距的节点不绘制。

{% include image.html url="/assets/images/201230-irrlicht-intro/26.occlusionquery.webp" urlx="/assets/images/201230-irrlicht-intro/026shot.jpg" %}


## 27.PostProcessing

创建屏幕双缓冲。颜色反转，用 HLSL and GLSL 写的。

{% include image.html url="/assets/images/201230-irrlicht-intro/27.postprocessing.webp" %}


## 28.CubeMapping

cubemap textures 使用，和环境 mapping。

{% include image.html url="/assets/images/201230-irrlicht-intro/28.cubemapping_4.webp" %}


## 29.HardwareSkinning

HardwareSkinning


## 30.Profiling

一些 profiling tools。

{% include image.html url="/assets/images/201230-irrlicht-intro/30.profiling.webp" %}


## Demo

一个完整的游戏 demo。

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


## 八叉树 Octree

如在室内场景管理中有两个经常用到的层次体系：BSP(Binary Space Partitioning) 树，这是八叉树的推广，和包围体树 (Boundingvolume tree)。前者用于加速剔除，而后者主要用于碰撞检测。

一般来说，对于室内场景使用 BSP 树，因为 1）室内场景遮挡比较严重，使用 BSP 树在特定的位置分割有助于提升效率；2）室内很可能朝某个方向延伸比较多，比如一条细长的走廊。
对于大规模室外场景，使用八叉树比较好，因为场景中的物体比较分散，而且不会出现太多的遮挡，
由于不用存储分割平面位置，使用八叉树这种规则的空间结构能够提高效率。
当然，如果这个大规模室外场景的物体主要集中在地面，使用四叉树进行空间管理会比较好。

{% include image.html url="/assets/images/201230-irrlicht-intro/1010823-20190507135423258-1913374272.png" %}


## Refs

- [1] [Irrlicht 引擎例子说明及中文链接 {% include relref_cnblogs.html %}](https://www.cnblogs.com/lancidie/archive/2011/03/13/1982741.html)
- [2] [3D 游戏场景管理概述 {% include relref_csdn.html %}](https://blog.csdn.net/u012234115/article/details/47156217)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-12-30-irrlicht-intro.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://irrlicht.sourceforge.net/]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/4ce0a4f4.html" %})
- [http://irrlicht.sourceforge.net/docu/example001.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cf015d5.html" %})
- [http://irrlicht.sourceforge.net/docu/example002.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d470f08f.html" %})
- [http://irrlicht.sourceforge.net/docu/example003.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/016d2c90.html" %})
- [http://irrlicht.sourceforge.net/docu/example004.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/734c770b.html" %})
- [http://irrlicht.sourceforge.net/docu/example005.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/2e6df6d0.html" %})
- [http://irrlicht.sourceforge.net/docu/example006.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cafcd71.html" %})
- [http://irrlicht.sourceforge.net/docu/example007.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d16644d7.html" %})
- [http://irrlicht.sourceforge.net/docu/example008.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f6b6c656.html" %})
- [http://irrlicht.sourceforge.net/docu/example009.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/5d639f5c.html" %})
- [http://irrlicht.sourceforge.net/docu/example010.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/56533bae.html" %})
- [http://irrlicht.sourceforge.net/docu/example011.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/7e014783.html" %})
- [http://irrlicht.sourceforge.net/docu/example012.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/5038a4d2.html" %})
- [http://irrlicht.sourceforge.net/docu/example013.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/908b2729.html" %})
- [http://irrlicht.sourceforge.net/docu/example014.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/70f4ca86.html" %})
- [http://irrlicht.sourceforge.net/docu/example015.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/fc98dca0.html" %})
- [http://irrlicht.sourceforge.net/docu/example016.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/dc3bbbb3.html" %})
- [http://irrlicht.sourceforge.net/docu/example017.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/65d43334.html" %})
- [http://irrlicht.sourceforge.net/docu/example018.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d74639c1.html" %})
- [http://irrlicht.sourceforge.net/docu/example019.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/c270d6b4.html" %})
- [http://irrlicht.sourceforge.net/docu/example020.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/d80461a3.html" %})
- [http://irrlicht.sourceforge.net/docu/example021.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/0cfa7b9f.html" %})
- [http://irrlicht.sourceforge.net/docu/example022.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/6e7ceb41.html" %})
- [http://irrlicht.sourceforge.net/docu/example023.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/e6faf851.html" %})
- [http://irrlicht.sourceforge.net/docu/example024.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/30c4976c.html" %})
- [http://irrlicht.sourceforge.net/docu/example025.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/2872869b.html" %})
- [http://irrlicht.sourceforge.net/docu/example026.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/e17a2c6d.html" %})
- [http://irrlicht.sourceforge.net/tut_devcpp.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f1b6649e.html" %})
- [http://irrlicht.sourceforge.net/tut_codeblocks.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/959cf6e9.html" %})
- [http://irrlicht.sourceforge.net/tut_codew.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a455348c.html" %})
- [http://irrlicht.sourceforge.net/tut_ode.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f195a7b1.html" %})
- [http://irrlicht.sourceforge.net/tut_toka.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/b00f362b.html" %})
- [http://irrlicht.sourceforge.net/tut_physx.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/7270aa13.html" %})
- [http://irrlicht.sourceforge.net/tut_newton.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/ac6f4f9d.html" %})
- [http://irrlicht.sourceforge.net/tut_newtondevcpp.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a2cfe98f.html" %})
- [https://blog.csdn.net/gqkly/article/details/51870182]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/blog.csdn.net/055cce4d.html" %})
- [https://blog.csdn.net/gqkly/article/details/51870581]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/blog.csdn.net/4ad69362.html" %})
- [https://blog.csdn.net/gqkly/article/details/51870636]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/blog.csdn.net/615e3a13.html" %})
- [https://www.cnblogs.com/lancidie/archive/2011/03/13/1982741.html]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/www.cnblogs.com/949091ac.html" %})
- [https://blog.csdn.net/u012234115/article/details/47156217]({% include relrefx.html url="/backup/2020-12-30-irrlicht-intro.md/blog.csdn.net/fd396aec.html" %})
