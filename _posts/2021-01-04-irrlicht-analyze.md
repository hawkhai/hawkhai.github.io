---
layout: post
title: "Irrlicht 3D 笔记 -- Irrlicht 3D 代码简析"
author:
location: "珠海"
categories: ["Irrlicht"]
tags: ["Irrlicht"]
toc: true
toclistyle: none
comments:
visibility: hidden
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---

Irrlicht 是四大开源 3D 引擎之一（其余三者为 Orge、Nebula 与 KlayGE）。

* libgdx It has the Box2D physics engine integrated.
* [Irrlicht 网页版本 HelloWorld](http://michaelzeilfelder.de/pub/emscripten/01.HelloWorld.html)
* 同作者，open source WebGL 3D library。[CopperLicht](https://www.ambiera.com/copperlicht/)
* 同作者，free easy-to-use 3D engine。[CopperCube](https://www.ambiera.com/coppercube/)


## Textures and Mapping

* Bump mapping
* Parallax mapping
* Light maps
* Sphere mapping


## 一些资料

* 地图编辑器。[irrEdit -- realtime 3D world editor](https://www.ambiera.com/irredit/index.html)
* 一些不错的文章。[Irrlicht 游戏开发 {% include relref_csdn.html %}](https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game)
* 一个完整的游戏。[基于 irrlicht 的多人第一人称即时战术沙盒生存游戏 {% include relref_github.html %}](https://github.com/SingingRivulet/Smoothly)
* 基于 irrlicht 的体积云。[基于 irrlicht 的实时体积云 {% include relref_github.html %}](https://github.com/SingingRivulet/irrSky)
* 真实的水面渲染。[irrlicht 引擎：真实的水面渲染 {% include relref_csdn.html %}](https://qilinzi.blog.csdn.net/article/details/89464394)
    [原创网址 {% include relref_csdn.html %}](https://blog.csdn.net/boyuejiang/article/details/8908379)
* irrlicht 引擎：硬件蒙皮骨骼动画。[麒麟子 {% include relref_csdn.html %}](https://blog.csdn.net/qq_36720848/article/details/89464731)
* 流体 3D 效果，很酷。[Ray Marching Metaball in Unity3D](https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d)

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_tkrfrnv-ypcyqhjvc4dawq.webp"
caption="Inigo Quilez’s Metaball on Shadertoy"
url2="/assets/images/210104-irrlicht-analyze/1_5pb-g7j7rcn1nfcgxemowq.gif" caption2="okay" %}


## 前置代码检查


### git 检出指定版本代码

```shell
# [irrlicht] 提交原始 Irrlicht 代码
git checkout ea8f3ada185a44c77087a6735bf9a4c77fe875f6
```


### 比较版本差异

```
E:\kSource\pythonx>python codecompare.py allcode
3806
targetCount 4257 diffCount 0 missCount 0
```


### irrlicht Android

* [wrapirrlicht-for-android](https://code.google.com/archive/p/wrapirrlicht-for-android/source)
    [Wrapping Irrlicht For Android](https://www.codeproject.com/articles/333135/wrapping-irrlicht-for-android)
* 37 commits，4 years ago。[irrlicht for opengles {% include relref_github.html %}](https://github.com/wangtianhang/irrlicht)
* 811 commits，10 years ago。[My port of irrlicht to Android {% include relref_github.html %}](https://github.com/dschaefer/irrlicht-android)
    * 14 commits，10 years ago。[Example projects {% include relref_github.html %}](https://github.com/dschaefer/irrlicht-examples)
* 24 commits，9 years ago。[Android Port for the opengl-es version of Irrlicht {% include relref_github.html %}](https://github.com/reizencroft/irrAndroid)
* 22 commits，9 years ago。[3d graphics engine for android {% include relref_github.html %}](https://github.com/nonameentername/irrlicht-android)
* 13 commits，19 days ago。[irrlicht-android {% include relref_github.html %}](https://github.com/vell001/irrlicht-android)
    [另外一个版本 {% include relref_github.html %}](https://github.com/vell001/Irrlicht-vell)
* 9 commits，3 years ago。[irrlicht-code-5603-branches-ogl-es on android {% include relref_github.html %}](https://github.com/marky0720/irrlicht_Android_ogl_es)
* [Game Demo for Android /Win32 with Irrlicht, sdl2.0, librocket, box2d {% include relref_github.html %}](https://github.com/iaco79/IrrGameDemo)
* [a game demo on android using irrlicht {% include relref_github.html %}](https://github.com/ghd214/irrlichtAndroidGame)
* [arris69 / IrrLicht-Android {% include relref_github.html %}](https://github.com/arris69/IrrLicht-Android)
* 815 commits，14 days ago。Skylicht Engine is C++ Game Engine based on Irrlicht 3D。<https://github.com/skylicht-lab/skylicht-engine>
    Skylicht Particle Component is a cleanup version of SPARK. We have optimized by GPU Billboard Instancing.
* 324 commits，6 years ago。[SPARK Particle Engine {% include relref_github.html %}](https://github.com/Synxis/SPARK)
* 320 次提交，1 年前。[3D 引擎，渲染系统使用的 OpenGL 及 OpenGL ES，Windows 上 OpenGL ES 使用 AMD 的 ES 模拟器](https://gitee.com/panqingyun/E3D-Engine) 这个 AMD 的 ES 模拟器 可以尝试跑一下。

-----

<font class='ref_snapshot'>参考资料快照</font>

- [http://michaelzeilfelder.de/pub/emscripten/01.HelloWorld.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/michaelzeilfelder.de/cca4ee41.html" %})
- [https://www.ambiera.com/copperlicht/]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/64c21d36.html" %})
- [https://www.ambiera.com/coppercube/]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d0f56d20.html" %})
- [https://www.ambiera.com/irredit/index.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d99c5582.html" %})
- [https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/7c644017.html" %})
- [https://github.com/SingingRivulet/Smoothly]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f44cb2d3.html" %})
- [https://github.com/SingingRivulet/irrSky]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/4979c7ca.html" %})
- [https://qilinzi.blog.csdn.net/article/details/89464394]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/qilinzi.blog.csdn.net/a65eca94.html" %})
- [https://blog.csdn.net/boyuejiang/article/details/8908379]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/cf839113.html" %})
- [https://blog.csdn.net/qq_36720848/article/details/89464731]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/88012b77.html" %})
- [https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/medium.com/e863e277.html" %})
- [https://code.google.com/archive/p/wrapirrlicht-for-android/source]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/code.google.com/4ee9cd81.html" %})
- [https://www.codeproject.com/articles/333135/wrapping-irrlicht-for-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.codeproject.com/caf8ea4d.html" %})
- [https://github.com/wangtianhang/irrlicht]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ac80b636.html" %})
- [https://github.com/dschaefer/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/952c0493.html" %})
- [https://github.com/dschaefer/irrlicht-examples]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/5ed0c1f8.html" %})
- [https://github.com/reizencroft/irrAndroid]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6a912d5e.html" %})
- [https://github.com/nonameentername/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/e73734fa.html" %})
- [https://github.com/vell001/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/87c6d55b.html" %})
- [https://github.com/vell001/Irrlicht-vell]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f38373f4.html" %})
- [https://github.com/marky0720/irrlicht_Android_ogl_es]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ae50da7e.html" %})
- [https://github.com/iaco79/IrrGameDemo]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/07dfbea5.html" %})
- [https://github.com/ghd214/irrlichtAndroidGame]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/1e3635bc.html" %})
- [https://github.com/arris69/IrrLicht-Android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bcf56cc0.html" %})
- [https://github.com/skylicht-lab/skylicht-engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bc413eab.html" %})
- [https://github.com/Synxis/SPARK]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6726b92b.html" %})
- [https://gitee.com/panqingyun/E3D-Engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/gitee.com/0f8e6927.html" %})
