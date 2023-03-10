---
layout: post
title: "图形学笔记 -- OpenGL 图形学 / 光线追踪（图）"
author:
location: "珠海"
categories: ["图形学"]
tags: ["图形学", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

什么是光线追踪？看看你周围，那些被光束照亮的物体。
从目光后方的光束，到光与之交互的物体的路径，就是光线追踪。

EA 的 3A 引擎 Frostbite，支持光线追踪。
Unity 和 Unreal 共同支持全球 90% 的游戏，现在在其引擎中支持微软 DirectX 光线追踪。
实时光线追踪技术元年：2018 年。

被这两个文章深深的吸引了。<https://yangwc.com/>
* [光线追踪器 Ray Tracer：入门篇](https://yangwc.com/2019/05/08/RayTracer-Basis/)
* [光线追踪器 Ray Tracer：进阶篇](https://yangwc.com/2019/05/23/RayTracer-Advance/)

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/e066a486-ec44-42fe-9205-c345fe0fa356.png" %}


## 《赛博朋克 2077》技术和渲染分析

[NetFly 童鞋 游戏蛮牛 2020-12-31 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/sgyLTmUycPCFnDGvNXYJmQ)

1980 年 Turner Whitted 发表了论文提出了最经典的光线追踪渲染方法。
可以看到，眼睛射出的光线，经过了两次折射一共获得了模型中三个点的光影信息，或许它还可以获取更多，但实际上这已经比光栅渲染真实很多了。
这可不是什么时间反演，其实主要是基于物理学中，光路可逆的规律，与其计算全局的光路图，不如只计算我所希望看到的那一部分像素颜色。

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/6402.webp" %}

为了更能够接近真实的物理世界，尤其是釉面反射。1984 年的 Cook 提出随机理论，也就是分散式光线追踪（Distribution Ray Tracing）。
釉面物体上的反射光强和方向将被分散成多条光线，那么该点的颜色也会受到多个方向的物体影响。
如图，像素采集点反射后有三条光线，只有三分之二可以到达该场景的光源，所以该点的亮度会比完全暴露在光源下的部分暗三分之一左右，
虽然不够精确，但这同样也是比较符合实际物理世界规律的。

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/640.webp" %}

图形渲染的目标和物理世界殊途同归 —— 简化，统一所有的理论便是又一次的本质飞跃。
1986 年提出的 Kajiya 式漫反射理论，可以称之为渲染方程。

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/6401.webp" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20210209210745.png" %}

我们眼睛在一个模型上所看到的颜色，受到四个方面的影响，分别是模型自身发光、模型受到光照的情况、模型的材质（即反射能力）和模型的朝向。
可以看到和模型与接收光作用的这一项包括了后三者，并将这三者的影响进行球面上的积分，从而综合得到了整个空间的光线对这个模型颜色的影响。
这就是我们今天提到的光线追踪的核心了。


## 光线追踪纵览

光线追踪算法是一种非常自然的技术，相比于光栅化的方法，它更加简单、暴力、真实。
与光栅化根据物体计算所在的像素的方式不同，光线路径追踪的方法是一个相反的过程，它在于用眼睛去看世界而不是世界如何到达眼中。
如下图所示，从视点出发向屏幕上每一个像素发出一条光线 View Ray，追踪此光路并计算其逆向光线的方向，映射到对应的像素上。
通过计算光路上颜色衰减和叠加，即可基本确定每一个像素的颜色。

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/2.png" caption="光线追踪示意图" %}

[实时光线追踪技术：业界发展近况与未来挑战 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/102397700)


## 赛博朋克 2077

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image001_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image003_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image005_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image007_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image009_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image011_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image013_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image015_s.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/image017_s.jpg" %}

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20200408114606373.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20200408114608237.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20200408114610165.jpg" %}
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20200408114610908.jpg" %}


## 实时光线追踪与离线光线追踪的区别

所谓的实时光线追踪，就是随着摄像机视角的变动，后端需要实时发射追踪光线来重新计算光照信息，如果屏幕分别率很高，这个计算量是很大的，
对 GPU 的性能要求是很高的，如果性能达不到游戏直接会卡死。而离线光线追踪则不会造成这种情况，即使设置了很高的光线追踪采样率，
很多的反射次数，无非是烘焙 Lightmap 的时间会变长，最终还是可以渲染出效果很好的的 Lightmap 供场景使用。
所以现阶段还是 **全局光照中的光线追踪方案占主流** ，NVIDIA 虽然发布了新的 TURING 架构显卡引入光线追踪框架，
但是实时光线追踪真正进入游戏普及估计还是任重道远（希望能很快打脸）。


## 光线追踪全局光照方案的渲染管线

关于光线追踪的基本原理，简单来说就是向场景发射 N 条光线，然后根据碰撞点的材质进行 BXDF，BRDF 的运算，然后（根据俄罗斯轮盘）再进行漫反射，镜面反射，或者折射，如此循环直到光线逃离场景或者到达最大反射次数，最后对 N 条光线进行蒙特卡洛积分即可获得结果。
对于实时光线追踪和离线光线追踪，这里发射光线的方式还是有些差异的：实时光线追踪是从视点发射光线，光线数量一般是屏幕的大小，比如屏幕是 1920\*1080， 则需要发射 1920\*1080 条射线，每条射线对应一个像素点，依照需求，可能要发射多次来采样平均得到理想的结果；
而对于离线光线追踪，每个静态物体都要根据光照 UV 生成 M 个 Patch（数量和 Lightmap 大小有关），每个 Patch 要向法线方向的半球发射 N 条射线（数量由用户采样数量决定），最终对 N 条射线进行蒙特卡洛积分，得到这个物体的 Lightmap。


## Vulkan-光线追踪（计算着色器实现）

[from {% include relref_csdn.html %}](https://blog.csdn.net/qq_35312463/article/details/106171311)
{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/20200517125349977.png" %}


## 游戏画质设置教程

[游戏画质设置教程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1Zz4y1U7aB)

1. 环境光遮蔽：通过使用颜色更深的阴影来增加物体的立体感。
2. 体积质量（体积云、体积雾、体积光等），通过光影来提高云朵、雾气、光线等的立体感。
3. LOD 细节层次（也叫 细节层次、视野距离）：游戏中，距离玩家较远的模型会被低分辨率渲染，而视野距离的等级就是这个“不会被低分辨率渲染”的范围，设置等级越高，“不会被低分辨率渲染”的范围就越高。
4. 曲面细分：用于给顶配置显卡锦上添花的设置选项。
5. 抗锯齿。视频中提到了 DLSS，MFAA 和 MSAA，TAA，FXAA，SMAA。
    * DLSS，深度学习超采样，现如今最好的抗锯齿技术，不仅抗锯齿还能增加帧数，是 N 卡的黑科技，深度学习。
    * MSAA，一种老久的抗锯齿技术。
    * MFAA，是 N 卡对 MSAA 做出的一个优化，在 N 卡面板设置中开启 MFAA 后，在游戏中开启 MSAA 会对帧率有很大的改善。
    * TAA，近十年来比较流行的一种抗锯齿技术，抗锯齿效果非常不错，效果比 MSAA、FXAA、SMAA 都好，唯一的缺点是让画面变模糊。
    * FXAA，一种已经被淘汰的技术，抗锯齿效果并不好的同时会让画面变模糊，可以说 TAA 完全吊打 FXAA 吧。
    * SMAA，抗锯齿效果高于 FXAA，低于 TAA。缺点是无法解决远处模型的锯齿，比如远处的树木仍会闪烁。


## Refs

- [1] [iGame GeForce RTX 显卡邀你抢先体验光线追踪版《我的世界》](https://3c.3dmgame.com/show-14-12283-1.html)
- [2] [光线追踪器 Ray Tracer：进阶篇](https://yangwc.com/2019/05/23/RayTracer-Advance/)
- [3] [浅谈光线追踪 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/45087397)
- [4] [《赛博朋克 2077》光线追踪效果展示 光追效果截图](https://wap.gamersky.com/gl/Content-1340332.html)
- [5] [光线追踪-引擎 Jan 3, 2020 • Huailiang {% include relref_github.html %}](https://huailiang.github.io/blog/2020/ray/)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://yangwc.com/]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/3cebfc82.html" %})
- [https://yangwc.com/2019/05/08/RayTracer-Basis/]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/aae340fb.html" %})
- [https://yangwc.com/2019/05/23/RayTracer-Advance/]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/d2661e77.html" %})
- [https://mp.weixin.qq.com/s/sgyLTmUycPCFnDGvNXYJmQ]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/mp.weixin.qq.com/bf7f7508.html" %})
- [https://zhuanlan.zhihu.com/p/102397700]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/zhuanlan.zhihu.com/8582b378.html" %})
- [https://blog.csdn.net/qq_35312463/article/details/106171311]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/blog.csdn.net/086bb667.html" %})
- [https://www.bilibili.com/video/BV1Zz4y1U7aB]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/www.bilibili.com/95223c7c.html" %})
- [https://3c.3dmgame.com/show-14-12283-1.html]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/3c.3dmgame.com/43a63afe.html" %})
- [https://zhuanlan.zhihu.com/p/45087397]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/zhuanlan.zhihu.com/f04a523c.html" %})
- [https://wap.gamersky.com/gl/Content-1340332.html]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/wap.gamersky.com/9312b476.html" %})
- [https://huailiang.github.io/blog/2020/ray/]({% include relrefx.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/huailiang.github.io/48dc6f83.html" %})
