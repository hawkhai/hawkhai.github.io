---
layout: post
title: "读书笔记 -- 逐梦旅程《Irrlicht 3D 游戏引擎程序设计》"
author:
location: "珠海"
categories: ["读书"]
tags: ["读书笔记", "Irrlicht"]
toc: true
toclistyle:
comments: true
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

> 上帝说，要有光，于是，就有了光。
> [站在巨人的肩膀上：游戏引擎导论 {% include relref_csdn.html %}](https://blog.csdn.net/poem_qianmo/article/details/8250057)

**Irrlicht 有的地方设计的有点奇怪，开始的时候没有理解，后来发现了原因：Irrlicht 诞生于固定管线时代，后来支持的可编程管线。**

{% include image.html url="/assets/images/210131-book-irrlicht/048057-01.jpg" %}

**前言**
Irrlicht 图形学基础，网格、纹理、覆盖层，场景管理，摄像机，地形、纹理和渲染，光照与材质，声音，粒子系统，碰撞检测，数据和文件的处理，着色器，游戏人工智能，部署一个 Irrlicht 应用程序等。
动态阴影、粒子系统、角色动画、碰撞检测等。
[baike](https://baike.baidu.com/item/Irrlicht%203D%E6%B8%B8%E6%88%8F%E5%BC%95%E6%93%8E%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/22344168)

<p class="counter-reset h2counter"></p>


## Irrlicht 游戏引擎 1


### Irrlicht 使用许可与系统要求 1


### 获得 Irrlicht 引擎 2


### 在 Windows 下设置编译器 4

#### 设置编译器的原理 4

#### 设置动态链接库的方法 5

#### 其他设置方法 10

#### 环境变量的设置方法 11

#### 设置过程中常见的问题 12


### 重新编译 Irrlicht 引擎 13


### 测试是否已经正确设置 15


### 在 Linux 环境中使用鬼火游戏引擎 16

#### 在 Linux 下编译静态库 16

#### 编译 Hello World 程序并运行 17

#### 在 Linux 下创建第一个项目 18

#### 第三方编程工具 Code::Blocks 19


## 编写第一个 Irrlicht 程序 20


### Irrlicht 引擎的结构 20

#### 引入命名空间 20

#### 了解 Irrlicht 引擎的结构 21


### 分析简单的代码 21


### 简单的扩展 24


### 类的形式 26


### 让窗口显示内容 28


### 比较成型的模式 29


### 让我们的程序发生变化 30


## 图形学基础 33


### 计算机显示原理 33

#### 图形系统的硬件 33

#### 光栅扫描系统 34

#### 计算机图形标准 35


### 图形学的数学基础 36

#### 向量及向量运算 36

#### 坐标 36

#### 基本几何变换 38

#### 三维空间的变换 40


### 双缓存和垂直同步 42


### 纹理 43


### Z 缓冲 45


### 摄像机 46


### 粒子系统 47


## 网格、纹理、覆盖层 50


### 网格简介 50


### 不同格式网格模型的区别 52


### 初识纹理 54


### 动态网格模型 56

{% include image.html url="/assets/images/210131-book-irrlicht/20210131171950.jpg" %}
{% include image.html url="/assets/images/210131-book-irrlicht/20210131172041.jpg" %}


### 覆盖层 59


### 使用精灵表 63


### 绘制基本图形 67


## 场景管理 69


### 场景节点和实体 69

#### 场景节点 69

#### 实体 71


### 场景节点类型 72


### 场景管理器 74


### 动态节点 74


### 场景的应用示例 77

#### 场景节点的应用 77

#### 动态节点的应用 81

#### 自定义场景节点 83

{% include image.html url="/assets/images/210131-book-irrlicht/20210131172734.jpg" %}

```cpp
//! This method is called just before the rendering process of the whole scene.
//! draws all scene nodes
void CSceneManager::drawAll()
{
    // render camera scenes
    // render lights scenes
    // render skyboxes
    // render default objects
    // render shadows
    // render transparent objects.
    // render transparent effect objects.
    // render custom gui nodes
}
```


## 摄像机 87


### 摄像机投影 87

#### 正交投影 88

#### 透视投影 89

#### 两种投影在代码上的实现 90


### 裁剪 92


### 摄像机观看视角的类型 95

#### 普通摄像机 95

#### 第一人称射击摄像机 95

#### Maya 摄像机 96


### FPS 摄像机的使用示例 96


## 地形、纹理和渲染 99


### 地形场景节点类 99


### 高度图 101


### 纹理 102

#### 纹理简介 102

#### 使用纹理 103


### 渲染示例 106

#### 渲染地形 106

#### 纹理渲染 111


### 创建地形 114


## 光照与材质 119


### 光照模型 119


### 光源 119


### 深入光源 120

#### 模拟环境光 121

#### 模拟漫射光 123

#### 灯光的衰减 123


### 光源 124

#### 光源的类型 124

#### 光源属性 125

#### 添加灯光 126


### 一些简单的光照示例 127

#### 用代码实现环境光 127

#### 用代码实现漫射光 129

#### 用代码实现镜面反射光 132


### 材质 135


### 阴影 136


### 着色 137

#### 着色模式 137

#### 设置着色模式 138


### 示例 138

#### 光照和材质示例 138

#### 显示实时动态阴影 140


## 声 音 144

声音是任何能够被人耳所感知的信号。即 $$50Hz$$~$$22000Hz$$ 之间的压力波，具有振幅和频率等属性。


### 声音基础 144

#### 声音的生成 144

#### 声音的编码存储 145

#### 声音的合成 146


### irrKlang 简介 146


### irrKlang 的使用 147

#### 实践 Hello World 147

#### 播放 3D 声音文件 151

#### 声音特效 154


## 粒子系统 157


### 粒子系统简介 157


### 粒子编辑器 —— irrEdit 158

#### 添加自己的粒子系统 158

#### 设置粒子系统 159


### 粒子系统各部分的代码实现 160

#### 粒子结构 160

#### 发射器 161

#### 影响器 163


### 绘制一个粒子系统 164

#### 编写代码完成一个简单的粒子系统 164

#### 使用代码制作水面 169

#### 环形粒子系统 173


## 碰撞检测 177


### 碰撞检测概述 177


### 几何和数学知识 178

#### 多边形和多面体 178

#### BSP 树 179

#### 空间四叉树和空间八叉树 179

#### Minkowski 和与 Minkowski 差 180

{% include image.html url="/assets/images/210131-book-irrlicht/1.jpg" %}
{% include image.html url="/assets/images/210131-book-irrlicht/2.jpg" %}
{% include image.html url="/assets/images/210131-book-irrlicht/3.jpg" %}

#### 包围体 181


### 常用的碰撞检测算法 183

#### 距离跟踪法 183

#### 基于图像空间的碰撞检测法 183

#### 空间分解法 184

#### 层次包围盒法 185


### 代码解析 185


## 数据和文件的处理 192


### Irrlicht 文件系统简介 192


### 文件的读取和写入 194

#### 写文件 194

#### 普通文件的读写 195

#### 一行一行读取和按分隔符读取 198

#### XML 文件的读写 200

#### 从 XML 文件中加载数据 201

#### 向 XML 文件写入数据 204

#### 从 XML 文件中读取特殊数据类型的数据 205


### 从档案中读取数据 207


## 着色器 210


### 图形渲染管线简介 210


### 着色器简介 211

#### 顶点着色器 211

#### 片断（像素）着色器 211

#### 几何着色器 212


### 使用着色器 212

#### 安装并使用 GLSL demo 212

Gooch & Toon 着色器。有点意思。
<http://mew.cx/glsl/glsldemo/>
{% include image.html url="/assets/images/210131-book-irrlicht/glsldemo.jpg" %}

{% include image.html url="/assets/images/210131-book-irrlicht/toon.png" caption="Toon" %}
{% include image.html url="/assets/images/210131-book-irrlicht/gooch.png" caption="Gooch" %}

* C:\Qt5.14.1\5.14.1\Src\qt3d\src\extras\shaders\gl3\gooch.frag
* C:\cocos2d-x-3.17.2\tests\cpp-tests\Resources\Sprite3DTest\toon.frag

#### 在 Irrlicht 引擎中使用着色器 214


### 进一步了解着色器 223

着色器 GUI 编辑器：
* [DirectX HLSL 编辑器 FX Composer](https://developer.nvidia.com/fx-composer)
* [TyphoonLabs' OpenGL Shader Designer](http://www.opengl.org/sdk/tools/ShaderDesigner/)
* [Shader Maker](https://cgvr.cs.uni-bremen.de/teaching/shader_maker/)
    Shader Maker is a simple, cross-platform GLSL editor. It works on Windows, Linux, and Mac OS X.


## 游戏人工智能 224


### 什么是智能 224


### 什么是游戏 AI 225


### AI 的组成与设计 226

#### 抉择与推理 226

#### 解决方案的类型 226

#### 智能体的反应能力 226

#### 系统的真实性 226

#### 游戏类型 227

#### 游戏内容 227

#### 游戏平台 227


### AI 的输入处理和感知 228

#### 感知系统 228

#### 更新规则 229

#### 反应时间 229

#### 门限 229

#### 负荷平衡 229

#### 计算代价与预处理 229

更新寄存器主要有轮询（polling）和事件（event）。


### OpenSteer 230

帮助编写游戏 AI 的类库：
[OpenSteer -- Steering Behaviors for Autonomous Characters](http://opensteer.sourceforge.net/)


## 部署一个 Irrlicht 应用程序 232


### 什么是部署 232


### 针对不同平台打包发布应用 232

#### 在 Windows 平台下部署 Irrlicht 应用程序 232

* 打包成 exe [Inno Setup](https://jrsoftware.org/isinfo.php)
    Inno Setup is a free installer for Windows programs by Jordan Russell and Martijn Laan. First introduced in 1997, Inno Setup today rivals and even surpasses many commercial installers in feature set and stability.
* 打包成 msi [WixEdit -- The editor for WiX XML source files {% include relref_github.html %}](https://wixedit.github.io/)

#### 在 Linux 平台下部署 Irrlicht 应用程序 233

#### 在 Mac OS X 平台下部署 Irrlicht 应用程序 234


### 部署源代码 236

#### 为什么要部署源代码 236

#### 如何部署 236


## Refs

- [1] [Irrlicht 3D 游戏引擎程序设计](http://www.tup.tsinghua.edu.cn/booksCenter/BOOK_04805701.html)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-31-book-Irrlicht.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/poem_qianmo/article/details/8250057]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/blog.csdn.net/47230e7d.html" %})
- [https://baike.baidu.com/item/Irrlicht%203D%E6%B8%B8%E6%88%8F%E5%BC%95%E6%93%8E%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/22344168]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/baike.baidu.com/99fa3fc0.html" %})
- [http://mew.cx/glsl/glsldemo/]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/mew.cx/a0bcb8f7.html" %})
- [https://developer.nvidia.com/fx-composer]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/developer.nvidia.com/cf354232.html" %})
- [http://www.opengl.org/sdk/tools/ShaderDesigner/]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/www.opengl.org/ab208a0b.html" %})
- [https://cgvr.cs.uni-bremen.de/teaching/shader_maker/]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/cgvr.cs.uni-bremen.de/a27bd13e.html" %})
- [http://opensteer.sourceforge.net/]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/opensteer.sourceforge.net/f3224cda.html" %})
- [https://jrsoftware.org/isinfo.php]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/jrsoftware.org/9690ed4e.php" %})
- [https://wixedit.github.io/]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/wixedit.github.io/ec7dbe39.html" %})
- [http://www.tup.tsinghua.edu.cn/booksCenter/BOOK_04805701.html]({% include relrefx.html url="/backup/2021-01-31-book-Irrlicht.md/www.tup.tsinghua.edu.cn/d2f80721.html" %})
