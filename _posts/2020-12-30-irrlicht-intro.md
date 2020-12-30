---
layout: post
title: "Irrlicht 笔记 -- Irrlicht 初探"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---

官网：<http://irrlicht.sourceforge.net/>


## development code

version | svn addr
---- | ----
development code | svn://svn.code.sf.net/p/irrlicht/code/trunk [unstable]
1.8.5 | svn://svn.code.sf.net/p/irrlicht/code/branches/releases/1.8
OpenGL ES driver | svn://svn.code.sf.net/p/irrlicht/code/branches/ogl-es


## Tutorials

<table class="tablestyle" ntablew="3:8:2:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | ---- |
| [1.HelloWorld] | Shows how to set up the Visual Studio IDE for using the Irrlicht Engine and how to write a simple HelloWorld program with it. The tutorial will show how to use the basics of the VideoDriver, the GUIEnvironment and the SceneManager. | easy | ![s001shot.jpg] |
| [2.Quake3Map] | This tutorial shows how to load a Quake 3 map into the engine, create a SceneNode for optimizing the speed of rendering and how to create a user controlled camera. | easy | ![s002shot.jpg] |
| [3.Custom SceneNode] | This tutorials shows how to create a custom scene node and how to use it in the engine. This is useful if you want to extend the render techniques of the Irrlicht Engine. | advanced | ![s003shot.jpg] |
| [4.Movement] | This Tutorial shows how to move and animate SceneNodes. The basic concept of SceneNodeAnimators is shown as well as manual movement of nodes using the keyboard. | easy | ![s004shot.jpg] |
| [5.User Interface] | This tutorial shows how to use the built in User Interface of the Irrlicht Engine. It will give a brief overview and show how to create and use windows, buttons, scroll bars, static texts and list boxes. | average | ![s005shot.jpg] |
| [6.2D Graphics] | This Tutorial shows how to do 2d graphics with the Irrlicht Engine. It shows how to draw images, keycolor based sprites, transparent rectangles and different fonts. You will may consider this useful if you want to make a 2d game with the engine, or if you want to draw a cool interface or head up display for your 3d game. | easy | ![s006shot.jpg] |
| [7.Collision] | In this tutorial, I will show how to collision detection with the Irrlicht Engine. I will describe 3 methods: Automatic collision detection for moving through 3d worlds with stair climbing and sliding, manual triangle picking and manual scene node picking. | average | ![s007shot.jpg] |
| [8.SpecialFX] | This tutorials describes how to do special effects. It shows how to use stencil buffer shadows, the particle system, billboards, dynamic light and the water surface scene node. | average | ![s008shot.jpg] |
| [9.MeshViewer] | This tutorial shows how to create a more complex application with the engine. We construct a simple mesh viewer using the user interface API and the scene management of Irrlicht. | advanced | ![s009.jpg] |
| [10.Shaders] | This tutorial shows how to use shaders for D3D8, D3D9 and OpenGL with the engine and how to create new material types with them. It also shows how to disable the generation of mipmaps at texture loading, and how to use text scene nodes. | advanced | ![s010shot.jpg] |
| [11.Per Pixel Lighting] | This tutorial shows how to use one of the built in more complex materials in irrlicht: Per pixel lighted surfaces using normal maps and parallax mapping. It will also show how to use fog and moving particle systems. And don’t panic: You dont need any experience with shaders to use these materials in Irrlicht. | average | ![s011shot.jpg] |
| [12.Terrain Rendering] | This tutorial will briefly show how to use the terrain renderer of Irrlicht. It will also show the terrain triangle selector to be able to do collision detection with terrain. | easy | ![s012shot.jpg] |
| [13.Render To Texture] | This tutorial shows how to render to a texture using Irrlicht. Render to texture is a feature with which it is possible to create nice special effects. In addition, this tutorial shows how to enable specular highlights. | average | ![s013shot.jpg] |
| [14.Win32 window] | This example only runs in Windows and demonstrates that Irrlicht can run inside a win32 window. MFC and .NET Windows.Forms windows are possible too. | easy | ![s014shot.jpg] |
| [15.Load .irr file] | This tutorial shows how to use .irr files. | easy | ![s015shot.jpg] |
| [16.Quake3Map Shader] | This tutorial shows how to work with all elements and effects from a q3 map. | average | ![s016shot.jpg] |
| [17.Hello World Mobile] | This tutorial shows Irrlicht for Windows CE. | advanced | ![s017shot.jpg] |
| [18.SplitScreen] | This tutorial presents usage of split screen setups. Developed by Max Winkel. | average | ![s018shot.jpg] |
| [19.Mouse And Joystick] | This tutorial explains joystick and mouse usage in Irrlicht. | easy | ![s019shot.jpg] |
| [20.Managed Lights] | Irrlicht supports special light setup via light managers. This tutorial shows several possibilities to choose the proper lights from the scene. | advanced | ![s020shot.jpg] |
| [21.Quake3Explorer] | This tutorial contains a full q3 map explorer. One can load q3 maps, walk through the maps, and play around with the advanced GUI. | advanced | ![s021shot.jpg] |
| [22.MaterialViewer] | This tutorial allows to test all material settings Irrlicht provides. One can use this app to prepare manually configured materials for an own app. | easy | ![s022shot.jpg] |
| [23.SMeshHandling] | This tutorial explains how to manually create meshes in Irrlicht. In contrast to example 3, this technique is pretty easy, does not require that much code, and can use all the advanced things of Irrlicht’s mesh handling. | average | ![s023shot.jpg] |

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

[s001shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s001shot.jpg" %}
[s002shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s002shot.jpg" %}
[s003shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s003shot.jpg" %}
[s004shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s004shot.jpg" %}
[s005shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s005shot.jpg" %}
[s006shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s006shot.jpg" %}
[s007shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s007shot.jpg" %}
[s008shot.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s008shot.jpg" %}
[s009.jpg]: {% include relref.html url="/assets/images/201230-irrlicht-intro/s009.jpg" %}
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

External Tutorials (not included in SDK, written by external authors)

<table class="tablestyle" ntablew="3:8:2:3"></table>

| Name | Summary | Difficulty | Shot |
| ---- | ---- | ---- | ---- |
| [DevCpp] | A detailed tutorial on how to use the engine with Dev C++, written by Andy Spurgeon. | easy | ![s001bshot.jpg] |
| [Code::Blocks] | A detailed on how to use the engine with the Code::Blocks IDE, written by Alvaro F. Celis. | easy | ![codeblocks.jpg] |
| [Codewarrior] | A detailed tutorial on how to use the engine with Metroworks Codewarrior, written by André Simon. | easy | ![s001cshot.jpg] |
| [ODE Integration] | Another popular and open source physics engine is ODE. This tutorial shows how to use Irrlicht with ODE. | advanced | ![odelogo.jpg] |
| [Tokamak Integration] | Tokamak is a popular physics engine. Matthew Couch wrote this tutorial which shows how to integrate Tokamak into the Irrlicht Engine. | advanced | ![s008bshot.jpg] |
| [PhysX Integration] | Ageia PhysX is the physics engine formerly called Novodex. This tutorials, written by Andrew J Santa Maria shows how to use it with Irrlicht. | advanced | ![physx.jpg] |
| [Newton Integration] | Another cool physics engine is Newton Game Dynamics. This external tutorial, written by mercior shows how to use it with Irrlicht. | advanced | ![newston.jpg] |
| [Newton DevC++ Integration] | This small tutorial will explain how to integrate the Newton Physics SDK together with Irrlicht into Dev-C++. | average | ![devcpp_newton.jpg] |

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
- [25] [http://irrlicht.sourceforge.net/tut_devcpp.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f1b6649e.html" %})
- [26] [http://irrlicht.sourceforge.net/tut_codeblocks.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/959cf6e9.html" %})
- [27] [http://irrlicht.sourceforge.net/tut_codew.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a455348c.html" %})
- [28] [http://irrlicht.sourceforge.net/tut_ode.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/f195a7b1.html" %})
- [29] [http://irrlicht.sourceforge.net/tut_toka.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/b00f362b.html" %})
- [30] [http://irrlicht.sourceforge.net/tut_physx.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/7270aa13.html" %})
- [31] [http://irrlicht.sourceforge.net/tut_newton.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/ac6f4f9d.html" %})
- [32] [http://irrlicht.sourceforge.net/tut_newtondevcpp.html]({% include relref.html url="/backup/2020-12-30-irrlicht-intro.md/irrlicht.sourceforge.net/a2cfe98f.html" %})
