---
layout: post
title: "Irrlicht 3D 笔记 -- Irrlicht 3D 代码简析 🐬"
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


## 一些资料

* 地图编辑器。[irrEdit -- realtime 3D world editor](https://www.ambiera.com/irredit/index.html)
* 一些不错的文章。[Irrlicht 游戏开发 {% include relref_csdn.html %}](https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game)
* 一个完整的游戏。[基于 irrlicht 的多人第一人称即时战术沙盒生存游戏 {% include relref_github.html %}](https://github.com/SingingRivulet/Smoothly)
* 基于 irrlicht 的体积云。[基于 irrlicht 的实时体积云 {% include relref_github.html %}](https://github.com/SingingRivulet/irrSky)
* 真实的水面渲染。[irrlicht 引擎：真实的水面渲染 {% include relref_csdn.html %}](https://qilinzi.blog.csdn.net/article/details/89464394)
* 流体 3D 效果，很酷。[Ray Marching Metaball in Unity3D](https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d)

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_tkrfrnv-ypcyqhjvc4dawq.webp" caption="Inigo Quilez’s Metaball on Shadertoy" %}

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_5pb-g7j7rcn1nfcgxemowq.gif" caption="okay" %}


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

* 37 commits，4 years ago。[irrlicht for opengles {% include relref_github.html %}](https://github.com/wangtianhang/irrlicht)
* 811 commits，10 years ago。[My port of irrlicht to Android {% include relref_github.html %}](https://github.com/dschaefer/irrlicht-android)
    * 14 commits，10 years ago。[Example projects {% include relref_github.html %}](https://github.com/dschaefer/irrlicht-examples)
* 24 commits，9 years ago。[Android Port for the opengl-es version of Irrlicht {% include relref_github.html %}](https://github.com/reizencroft/irrAndroid)
* 22 commits，9 years ago。[3d graphics engine for android {% include relref_github.html %}](https://github.com/nonameentername/irrlicht-android)
* 13 commits，19 days ago。[irrlicht-android {% include relref_github.html %}](https://github.com/vell001/irrlicht-android)
* 9 commits，3 years ago。[irrlicht-code-5603-branches-ogl-es on android {% include relref_github.html %}](https://github.com/marky0720/irrlicht_Android_ogl_es)

* 815 commits，14 days ago。Skylicht Engine is C++ Game Engine based on Irrlicht 3D。<https://github.com/skylicht-lab/skylicht-engine> Skylicht Particle Component is a cleanup version of SPARK. We have optimized by GPU Billboard Instancing.
* 324 commits，6 years ago。[SPARK Particle Engine {% include relref_github.html %}](https://github.com/Synxis/SPARK)

* 320 次提交，1 年前。[3D 引擎，渲染系统使用的 OpenGL 及 OpenGL ES，Windows 上 OpenGL ES 使用 AMD 的 ES 模拟器](https://gitee.com/panqingyun/E3D-Engine)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://www.ambiera.com/irredit/index.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d99c5582.html" %})
- [2] [https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/7c644017.html" %})
- [3] [https://github.com/SingingRivulet/Smoothly]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f44cb2d3.html" %})
- [4] [https://github.com/SingingRivulet/irrSky]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/4979c7ca.html" %})
- [5] [https://qilinzi.blog.csdn.net/article/details/89464394]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/qilinzi.blog.csdn.net/a65eca94.html" %})
- [6] [https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/medium.com/e863e277.html" %})
- [7] [https://github.com/wangtianhang/irrlicht]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ac80b636.html" %})
- [8] [https://github.com/dschaefer/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/952c0493.html" %})
- [9] [https://github.com/dschaefer/irrlicht-examples]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/5ed0c1f8.html" %})
- [10] [https://github.com/reizencroft/irrAndroid]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6a912d5e.html" %})
- [11] [https://github.com/nonameentername/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/e73734fa.html" %})
- [12] [https://github.com/vell001/irrlicht-android]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/87c6d55b.html" %})
- [13] [https://github.com/marky0720/irrlicht_Android_ogl_es]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/ae50da7e.html" %})
- [14] [https://github.com/skylicht-lab/skylicht-engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/bc413eab.html" %})
- [15] [https://github.com/Synxis/SPARK]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/6726b92b.html" %})
- [16] [https://gitee.com/panqingyun/E3D-Engine]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/gitee.com/0f8e6927.html" %})
