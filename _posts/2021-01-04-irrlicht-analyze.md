---
layout: post
title: "Irrlicht 3D 笔记 -- Irrlicht 3D 代码简析"
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
sortrefs: true
---

Irrlicht 是四大开源 3D 引擎之一（其余三者为 Orge、Nebula 与 KlayGE）。
Changes in 1.8.4 (9th July 2016, svn r5321)

* libgdx It has the Box2D physics engine integrated.
* [Irrlicht 网页版本 HelloWorld](http://michaelzeilfelder.de/pub/emscripten/01.HelloWorld.html)
* 同作者，open source WebGL 3D library。[CopperLicht](https://www.ambiera.com/copperlicht/)
* 同作者，free easy-to-use 3D engine。[CopperCube](https://www.ambiera.com/coppercube/)

* [基于 GPU 的粒子碰撞（理论篇） {% include relref_github.html %}](https://chengkehan.github.io/ParticleCollisionGPUTheory.html)
* [基于 GPU 的粒子碰撞（实践篇） {% include relref_github.html %}](https://chengkehan.github.io/ParticleCollisionGPUPractice.html)
* [基于 GPU 的粒子碰撞（总结篇） {% include relref_github.html %}](https://chengkehan.github.io/ParticleCollisionGPUConclusion.html)
* [基于物理渲染的基础理论（译） {% include relref_github.html %}](https://chengkehan.github.io/BasicTheoryOfPhysicallyBasedRendering.html)

{% include image.html url="/assets/images/210104-irrlicht-analyze/3p.gif" %}

几个有用的工具，用来抓取图形渲染帧，在分析其它项目以及排查渲染方面的 bug 时非常有用。
[渲染帧抓取工具 {% include relref_github.html %}](https://chengkehan.github.io/FrameCaptureTools.html)

* [Adreno GPU Profiler](https://developer.qualcomm.com/software/adreno-gpu-profiler)
* [RenderDoc {% include relref_github.html %}](https://github.com/baldurk/renderdoc) is a stand-alone graphics debugging tool.
* [Tegra Graphics Debugger](https://developer.nvidia.com/tegra-graphics-debugger)
* [Intel® Graphics Performance Analyzers](https://software.intel.com/en-us/gpa)


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

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_tkrfrnv-ypcyqhjvc4dawq.webp" caption="Inigo Quilez’s Metaball on Shadertoy" %}

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_5pb-g7j7rcn1nfcgxemowq.gif" caption="okay" %}

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_butc_yqwin57a1e3s1fwvg.webp" caption="Shading and Lighting" %}

{% include image.html url="/assets/images/210104-irrlicht-analyze/04181351-50925b16c31b4032a8f2a1d6ad865e6b.png" caption="irrlicht 引擎：真实的水面渲染" %}


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

1. https://github.com/ghd214/irrlichtAndroidGame 9 years ago，a game demo on android using irrlicht，编译出来了，包含音乐等，还不错。
1. https://github.com/nonameentername/irrlicht-android 9 years ago，通过 swig 链接，实现了基本的 JNI，是一个完整的例子，但是没有跑起来。
  ```shell
$(shell swig -c++ -java -package $(PACKAGE_NAME) \
    -outdir $(JAVA_DIR) \
    -o $(NDK_DIR)/wrapper_wrap.cpp \
    $(LOCAL_PATH)/wrapper.i \
)
  ```
  {% highlight cpp %}
#ifndef __IRRLICHT_NATIVE_H__
#define __IRRLICHT_NATIVE_H__

#include <string>

class NativeIrrlicht {
public:
    NativeIrrlicht();
    ~NativeIrrlicht();

    void onCreate();
    void onPause();
    void onResume();
    void onDestroy();
    void init();
    void initGL(int w, int h);
    void onResize(int w, int h);
    void sendEvent(int action, float x, float y);
    bool getStatus();
    void setPath(std::string path);
    void drawIteration();
};
#endif
  {% endhighlight %}

2. ~~<https://github.com/dschaefer/irrlicht-android>~~ 811 commits，10 years ago，没找打 AndroidManifest.xml。
3. ~~<https://github.com/reizencroft/irrAndroid>~~ 24 commits，9 years ago，非 JNI 模式。
4. https://github.com/skylicht-lab/skylicht-engine 815 commits，14 days ago。Irrlicht 引擎升级，涉及到一些纹理的处理，SPARK 粒子引擎值得研究一下。是一个非常完整的引擎，官网：skylicht.com。
5. https://github.com/nailgun/android_irrlicht_vuforia Vuforia 扩增实境软件开发工具包。没跑起来。Demo android application with irrlicht and vuforia. Source based on image targets vuforia sample.
6. https://github.com/iaco79/IrrGameDemo 具备参考价值。Game Demo for Android / Win32 with Irrlicht, sdl2.0, librocket, box2d。
7. https://github.com/dschaefer/irrlicht-examples
8. https://github.com/havlenapetr/gamekit
9. https://github.com/cskeyn/BulletAndroid
10. https://github.com/marky0720/IrrlichtAndroid
11. https://github.com/nonameentername/pyirrlicht-android
12. https://github.com/xiaomingzhong/IrrlichtAndroid-master

14. https://github.com/vell001/irrlicht-android
15. https://github.com/xiaomingzhong/irrlicht-android
16. https://github.com/disktree/irrlicht
17. https://github.com/xiaomingzhong/irrlicht-android-studio
18. https://github.com/xiaobenshu/irrlicht_Android
19. https://github.com/okuoku/irrlicht-android
20. https://github.com/nailgun/irrlicht_android
21. ~~<https://github.com/marky0720/irrlicht_Android_ogl_es>~~ 非 JNI 模式。
22. https://github.com/arris69/IrrLicht-Android
23. https://github.com/nailgun/irrlicht_android_viewer
24. https://github.com/vell001/Irrlicht-vell
25. https://github.com/danyr/gamekit
26. https://github.com/antmuse/AntThread
27. https://github.com/Picaroon/gamekit

https://github.com/wangtianhang/irrlicht
https://github.com/Synxis/SPARK

这几个还需要 gitee 查找资料。

https://code.google.com/archive/p/wrapirrlicht-for-android/source
https://www.codeproject.com/articles/333135/wrapping-irrlicht-for-android
https://gitee.com/panqingyun/E3D-Engine


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
* [arris69 / IrrLicht-Android {% include relref_github.html %}](https://github.com/arris69/IrrLicht-Android)
* 815 commits，14 days ago。Skylicht Engine is C++ Game Engine based on Irrlicht 3D。<https://github.com/skylicht-lab/skylicht-engine>
    Skylicht Particle Component is a cleanup version of SPARK. We have optimized by GPU Billboard Instancing.
* 324 commits，6 years ago。[SPARK Particle Engine {% include relref_github.html %}](https://github.com/Synxis/SPARK)
* 320 次提交，1 年前。[3D 引擎，渲染系统使用的 OpenGL 及 OpenGL ES，Windows 上 OpenGL ES 使用 AMD 的 ES 模拟器](https://gitee.com/panqingyun/E3D-Engine) 这个 AMD 的 ES 模拟器 可以尝试跑一下。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-04-irrlicht-analyze.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/7c644017.html" %})
- [https://blog.csdn.net/qq_36720848/article/details/89464731]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/88012b77.html" %})
- [https://blog.csdn.net/boyuejiang/article/details/8908379]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/cf839113.html" %})
- [https://chengkehan.github.io/BasicTheoryOfPhysicallyBasedRendering.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/chengkehan.github.io/13dc14d1.html" %})
- [https://chengkehan.github.io/ParticleCollisionGPUConclusion.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/chengkehan.github.io/7e9d7f8f.html" %})
- [https://chengkehan.github.io/FrameCaptureTools.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/chengkehan.github.io/8cad55e3.html" %})
- [https://chengkehan.github.io/ParticleCollisionGPUPractice.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/chengkehan.github.io/a6cbbd0a.html" %})
- [https://chengkehan.github.io/ParticleCollisionGPUTheory.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/chengkehan.github.io/aa507dcc.html" %})
- [https://code.google.com/archive/p/wrapirrlicht-for-android/source]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/code.google.com/4ee9cd81.html" %})
- [https://developer.nvidia.com/tegra-graphics-debugger]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/developer.nvidia.com/1e05e468.html" %})
- [https://developer.qualcomm.com/software/adreno-gpu-profiler]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/developer.qualcomm.com/a5a0a370.html" %})
- [https://gitee.com/panqingyun/E3D-Engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/gitee.com/0f8e6927.html" %})
- [https://github.com/iaco79/IrrGameDemo]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/07dfbea5.html" %})
- [https://github.com/danyr/gamekit]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/09b59859.html" %})
- [https://github.com/antmuse/AntThread]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/0f8fb319.html" %})
- [https://github.com/ghd214/irrlichtAndroidGame]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/1e3635bc.html" %})
- [https://github.com/SingingRivulet/irrSky]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/4979c7ca.html" %})
- [https://github.com/marky0720/IrrlichtAndroid]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/59036d28.html" %})
- [https://github.com/disktree/irrlicht]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/5cc1d8e2.html" %})
- [https://github.com/dschaefer/irrlicht-examples]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/5ed0c1f8.html" %})
- [https://github.com/cskeyn/BulletAndroid]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/5f10f216.html" %})
- [https://github.com/okuoku/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/64b51a86.html" %})
- [https://github.com/Synxis/SPARK]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6726b92b.html" %})
- [https://github.com/reizencroft/irrAndroid]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6a912d5e.html" %})
- [https://github.com/nailgun/android_irrlicht_vuforia]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/78ef1963.html" %})
- [https://github.com/xiaomingzhong/IrrlichtAndroid-master]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/849732cd.html" %})
- [https://github.com/vell001/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/87c6d55b.html" %})
- [https://github.com/xiaomingzhong/irrlicht-android-studio]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/8afaee92.html" %})
- [https://github.com/xiaobenshu/irrlicht_Android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/8f711333.html" %})
- [https://github.com/dschaefer/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/952c0493.html" %})
- [https://github.com/nailgun/irrlicht_android_viewer]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/983d7ba1.html" %})
- [https://github.com/nailgun/irrlicht_android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/a197b51d.html" %})
- [https://github.com/wangtianhang/irrlicht]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ac80b636.html" %})
- [https://github.com/xiaomingzhong/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ae10ec45.html" %})
- [https://github.com/marky0720/irrlicht_Android_ogl_es]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ae50da7e.html" %})
- [https://github.com/havlenapetr/gamekit]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/b9bcafef.html" %})
- [https://github.com/baldurk/renderdoc]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bb00e08f.html" %})
- [https://github.com/skylicht-lab/skylicht-engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bc413eab.html" %})
- [https://github.com/arris69/IrrLicht-Android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bcf56cc0.html" %})
- [https://github.com/Picaroon/gamekit]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/c90ca4ec.html" %})
- [https://github.com/nonameentername/pyirrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/e39426a3.html" %})
- [https://github.com/nonameentername/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/e73734fa.html" %})
- [https://github.com/vell001/Irrlicht-vell]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f38373f4.html" %})
- [https://github.com/SingingRivulet/Smoothly]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f44cb2d3.html" %})
- [https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/medium.com/e863e277.html" %})
- [http://michaelzeilfelder.de/pub/emscripten/01.HelloWorld.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/michaelzeilfelder.de/cca4ee41.html" %})
- [https://qilinzi.blog.csdn.net/article/details/89464394]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/qilinzi.blog.csdn.net/a65eca94.html" %})
- [https://software.intel.com/en-us/gpa]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/software.intel.com/5d46a23a.html" %})
- [https://www.ambiera.com/copperlicht/]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/64c21d36.html" %})
- [https://www.ambiera.com/coppercube/]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d0f56d20.html" %})
- [https://www.ambiera.com/irredit/index.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d99c5582.html" %})
- [https://www.codeproject.com/articles/333135/wrapping-irrlicht-for-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.codeproject.com/caf8ea4d.html" %})
