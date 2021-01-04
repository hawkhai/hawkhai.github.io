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

* [irrEdit -- realtime 3D world editor](https://www.ambiera.com/irredit/index.html)
* [Irrlicht 游戏开发 -- 一些文章 {% include relref_csdn.html %}](https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game)
* [基于 irrlicht 的多人第一人称即时战术沙盒生存游戏 {% include relref_github.html %}](https://github.com/SingingRivulet/Smoothly)
* [基于 irrlicht 的实时体积云](https://gitee.com/sinriv/irrSky)
* [irrlicht 引擎：真实的水面渲染 {% include relref_csdn.html %}](https://qilinzi.blog.csdn.net/article/details/89464394)
* [流体 3D 效果。Ray Marching Metaball in Unity3D](https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d)

{% include image.html url="/assets/images/210104-irrlicht-analyze/1_5pb-g7j7rcn1nfcgxemowq.gif" caption="okay" %}


## 前置代码检查


### git 检出指定版本代码

```shell
# [irrlicht] 提交原始 Irrlicht 代码
git checkout ea8f3ada185a44c77087a6735bf9a4c77fe875f6
```


### 比较版本差异

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://www.ambiera.com/irredit/index.html]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/www.ambiera.com/d99c5582.html" %})
- [2] [https://blog.csdn.net/jiangcaiyang123/column/info/irrlicht-game]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/blog.csdn.net/7c644017.html" %})
- [3] [https://github.com/SingingRivulet/Smoothly]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/github.com/f44cb2d3.html" %})
- [4] [https://gitee.com/sinriv/irrSky]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/gitee.com/d80898a7.html" %})
- [5] [https://qilinzi.blog.csdn.net/article/details/89464394]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/qilinzi.blog.csdn.net/a65eca94.html" %})
- [6] [https://medium.com/@avseoul/ray-marching-metaball-in-unity3d-fc6f83766c5d]({% include relref.html url="/backup/2021-01-04-irrlicht-analyze.md/medium.com/e863e277.html" %})
