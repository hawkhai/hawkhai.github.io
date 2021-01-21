---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 光线追踪（图）"
author:
location: "珠海"
categories: ["特效"]
tags: ["特效", "OpenGL"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

什么是光线追踪？看看你周围，那些被光束照亮的物体。
从目光后方的光束，到光与之交互的物体的路径，就是光线追踪。

EA 的 3A 引擎 Frostbite，支持光线追踪。
Unity 和 Unreal 共同支持全球 90% 的游戏，现在在其引擎中支持微软 DirectX 光线追踪。
实时光线追踪技术元年：2018 年。

被这两个文章深深的吸引了。https://yangwc.com/
* [光线追踪器 Ray Tracer：入门篇](https://yangwc.com/2019/05/08/RayTracer-Basis/)
* [光线追踪器 Ray Tracer：进阶篇](https://yangwc.com/2019/05/23/RayTracer-Advance/)

{% include image.html url="/assets/images/210111-shader-opengl-lighting-~2a/e066a486-ec44-42fe-9205-c345fe0fa356.png" %}


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
所以现阶段还是**全局光照中的光线追踪方案占主流**，NVIDIA 虽然发布了新的 TURING 架构显卡引入光线追踪框架，
但是实时光线追踪真正进入游戏普及估计还是任重道远（希望能很快打脸）。


## 光线追踪全局光照方案的渲染管线

关于光线追踪的基本原理，简单来说就是向场景发射 N 条光线，然后根据碰撞点的材质进行 BXDF，BRDF 的运算，然后（根据俄罗斯轮盘）再进行漫反射，镜面反射，或者折射，如此循环直到光线逃离场景或者到达最大反射次数，最后对 N 条光线进行蒙特卡洛积分即可获得结果。
对于实时光线追踪和离线光线追踪，这里发射光线的方式还是有些差异的：实时光线追踪是从视点发射光线，光线数量一般是屏幕的大小，比如屏幕是 1920\*1080， 则需要发射 1920\*1080 条射线，每条射线对应一个像素点，依照需求，可能要发射多次来采样平均得到理想的结果；
而对于离线光线追踪，每个静态物体都要根据光照 UV 生成 M 个 Patch（数量和 Lightmap 大小有关），每个 Patch 要向法线方向的半球发射 N 条射线（数量由用户采样数量决定），最终对 N 条射线进行蒙特卡洛积分，得到这个物体的 Lightmap。


## Refs

- [1] [iGame GeForce RTX 显卡邀你抢先体验光线追踪版《我的世界》](https://3c.3dmgame.com/show-14-12283-1.html)
- [2] [光线追踪器 Ray Tracer：进阶篇](https://yangwc.com/2019/05/23/RayTracer-Advance/)
- [3] [浅谈光线追踪 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/45087397)
- [4] [《赛博朋克 2077》光线追踪效果展示 光追效果截图](https://wap.gamersky.com/gl/Content-1340332.html)
- [5] [光线追踪-引擎 Jan 3, 2020 • Huailiang {% include relref_github.html %}](https://huailiang.github.io/blog/2020/ray/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://yangwc.com/]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/3cebfc82.html" %})
- [https://yangwc.com/2019/05/08/RayTracer-Basis/]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/aae340fb.html" %})
- [https://yangwc.com/2019/05/23/RayTracer-Advance/]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/yangwc.com/d2661e77.html" %})
- [https://zhuanlan.zhihu.com/p/102397700]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/zhuanlan.zhihu.com/8582b378.html" %})
- [https://3c.3dmgame.com/show-14-12283-1.html]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/3c.3dmgame.com/43a63afe.html" %})
- [https://zhuanlan.zhihu.com/p/45087397]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/zhuanlan.zhihu.com/f04a523c.html" %})
- [https://wap.gamersky.com/gl/Content-1340332.html]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/wap.gamersky.com/9312b476.html" %})
- [https://huailiang.github.io/blog/2020/ray/]({% include relref.html url="/backup/2021-01-11-shader-OpenGL-Lighting-Advanced-RayTracer-Advance.md/huailiang.github.io/48dc6f83.html" %})
