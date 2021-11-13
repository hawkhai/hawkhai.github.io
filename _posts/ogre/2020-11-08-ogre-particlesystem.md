---
layout: post
title: "3D 引擎 Ogre3D -- Ogre3D 脚本系统关键字说明"
author:
location: "珠海"
categories: ["3D 引擎"]
tags: ["图形学", "Ogre3D"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---

{% include image.html url="/assets/images/201108-ogre-particlesystem/v2-18e3e24cdca1fae8cc8a4a732a46decd_1440w.jpg" %}

去年搞了一阵子 Ogre3D，对它的粒子系统进行了微调，以适应手机屏幕，并对其进行了扩充，接入了 ParticleUniverse。


## 材质 / 技术（Techniques）

格式：Format: technique 技术名

技术只有为数不多的几个属于它们自己的属性：


### scheme

设置技术所属的“方案”

格式 : scheme &lt; 方案名 &gt;

示例 : scheme hdr

默认 : scheme Default


### lod_index

设置该技术所属的细节层次索引。

格式 : lod_index &lt; 数字 &gt;

数字的合法数值范围是 0（最高细节层次）到 65535，尽管这是不可能的。在技术之间的细节层次索引中不能留空当。也就是说，细节层次索引要按顺序排列，例如：0，1，2，3，……；而不能出现：0，10，20，30，……，这样的情况。

示例 : lod_index 1

默认 : lod_index 0


### lod_distances

材质属性，与 lod_index 有直接关系

格式 : lod_distances &lt;distance_1&gt; [&lt;distance_2&gt; ... &lt;distance_n&gt;]

示例 : lod_distances 300.0 600.5 1200


## 渲染通路（Pass）


### ambient

设置此渲染通路中周围环境的反射系数

格式 : ambient (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)

数值的取值范围在 0.0 到 1.0 之间。

示例 : ambient 0.0 0.8 0.0

默认 : ambient 1.0 1.0 1.0 1.0


### diffuse

设置此渲染通路中漫反射系数。

格式 : diffuse (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)

数值的取值范围在 0.0 到 1.0 之间。

示例 : diffuse 1.0 0.5 0.5

Default: diffuse 1.0 1.0 1.0 1.0


### specular

设置此渲染通路中镜面反射颜色的反射系数。

格式 : specular (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour) &lt;shininess&gt;

数值的取值范围在 0.0 到 1.0 之间。闪耀值（shininess）可以是任意比 0 大的值。

示例 : specular 1.0 1.0 1.0 12.5

默认 : specular 0.0 0.0 0.0 0.0 0.0


### emissive

设置一个物体自发光的量。

格式 : emissive (&lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]\| vertexcolour)

数值的取值范围在 0.0 到 1.0 之间。

示例 : emissive 1.0 0.0 0.0

默认 : emissive 0.0 0.0 0.0 0.0


### scene_blend

设置此渲染通路与场景中现有的内容混合的方式

格式 1: scene_blend &lt;add\|modulate\|alpha_blend\|colour_blend&gt;

示例 : scene_blend add

可用的混合形式参数如下：

* **add**

渲染输出的颜色被叠加到场景中，用在爆炸、闪光、闪电、鬼魂等地方效果很好。相当于“scene_blend one one”

* **modulate**

另一种将渲染输出加到场景内容中，一般用于给场景着色和加深场景颜色。对于浓烟弥漫的玻璃，半透明的物体等，有很好的使用效果。相当于“scene_blend dest_colour zero”。

* **colour_blend**

基于输入文件的亮度给场景着色，但是并不加深颜色。相当于“scene_blend src_colour one_minus_src_colour”。

* **alpha_blend**

渲染输出的 alpha 值被用作遮罩。相当于“scene_blend src_alpha one_minus_src_alpha”

格式 2: scene_blend &lt;src_factor&gt; &lt;dest_factor&gt;

示例 : scene_blend one one_minus_dest_alpha

这种格式允许你通过设置源和目标因数，从而完全控制混合操作。最终被写入渲染目标的颜色结果是 (texture * sourceFactor) + (scene_pixel * destFactor)。两个参数的可选值如下：

**one**

常数值 1.0

**zero**

常数值 0.0

**dest_colour**

已存在的像素颜色

**src_colour**

纹理像素颜色

**one_minus_dest_colour**

1 -（dest_colour）

**one_minus_src_colour**

1 -（src_colour）

**dest_alpha**

已存在的像素 alpha 值

**src_alpha**

纹理像素 alpha 值

**one_minus_dest_alpha**

1 -（dest_alpha）

**one_minus_src_alpha**

1 -（src_alpha）

默认 : scene_blend one zero （这句意为不透明的）


### depth_check

设置此渲染通路的深度缓冲检测的状态是打开状态还是关闭状态。

格式 : depth_check &lt;on\|off&gt;

默认 : depth_check on


### depth_write

设置此渲染通路的深度缓冲写入的状态是打开状态还是关闭状态。

格式 : depth_write &lt;on\|off&gt;

默认 : depth_write on


### depth_func

当深度检测打开时，设置用于比较深度值的函数。

格式 : depth_func &lt;func&gt;

能的函数如下：

**always_fail**

永远不向渲染目标写入像素

**always_pass**

总是将像素写入渲染目标

**less**

如果将要写入的像素的深度小于现在缓冲区内容的深度，则写入

**less_equal**

如果将要写入的像素的深度小于等于现在缓冲区内容的深度，则写入

**equal**

如果将要写入的像素的深度等于现在缓冲区内容的深度，则写入

**not_equal**

如果将要写入的像素的深度不等于现在缓冲区内容的深度，则写入

**greater_equal**

如果将要写入的像素的深度大于等于现在缓冲区内容的深度，则写入

**greater**

如果将要写入的像素的深度大于现在缓冲区内容的深度，则写入

默认 : depth_func less_equal


### depth_bias

设置此渲染通路的深度值的偏向。可用于使共面的多边形中的一个位于其它之上。例如：印制花纹图案。

格式 : depth_bias &lt;constant_bias&gt; [&lt;slopescale_bias&gt;]

深度偏向值最终由偏向常数（constant_bias）*最小可观察的深度（minObservableDepth）+ 最大坡度（maxSlope）*坡度偏向（slopescale_bias）共同决定。坡度偏向与多边形到镜头的角度有关，形成相应的偏向值，但是在一些时间比较早的硬件上，这被忽略了。偏向常数是形成最小深度值的一个因素，所以 1 的价值就在于一点一点地缓慢地推进深度。


### alpha_rejection

设置此项，可以使用 alpha 作为一个阀值，令渲染通路拒绝来自管线的像素。

格式 : alpha_rejection &lt;function&gt; &lt;value&gt;

示例 : alpha_rejection greater_equal 128

如上例所示，拒绝所有来自管线的 alpha 值大于等于 128 的像素。 function 参数可以选择在 depth_function 属性的参数列表中所列的参数。value 参数理论上可以是 0 到 255 之间的任意数，但是考虑到硬件兼容性，最好限制在 0 到 128 之间。

默认 : alpha_rejection always_pass


### cull_hardware

设置此渲染通路的硬件裁剪模式。

格式 : cull_hardware &lt;clockwise\|anticlockwise\|none&gt;

硬件渲染引擎裁剪三角形的典型方法是基于三角形顶点的环绕顺序。顶点环绕顺序又与渲染操作中顶点传送和编号的方向有关，从镜头中看到的有可能是顺时针的也可能是逆时针的。如果选择了 'cull_hardware clockwise' 设置，则所有从镜头看顺时针顺序的三角形被硬件剪裁掉。显然，'anticlockwise' 设置裁剪掉逆时针顺序的三角形。'none' 设置关闭硬件裁剪，即所有三角形都渲染（用于渲染双侧道路）。

默认 : cull_hardware clockwise

默认值与 OpenGL 的默认值相同，与 Direct3D 的默认值相反（因为 OGRE 与 OpenGL 一样使用右手坐标系）。


### cull_software

设置此渲染通路的软件裁剪模式。

格式 : cull_software &lt;back\|front\|none&gt;

在某些情形下，引擎也会在将几何体送往硬件渲染前进行软件裁剪。此设置仅在场景管理器使用它时起效（因为最好用在大量平面的世界几何体，而不是移动的几何体，因为用于移动的物体上代价会很大），但是如果在送入硬件之前可以有效裁剪的话还是可以使用的。在这种情况下，裁剪就要基于面向镜头的是三角形的背面还是正面 —— 这个定义是基于面法向的（即：垂直于多边形平面且标示出正面方向的向量）。因为 OGRE 期望平面的逆时针方向为正向，所以软件裁剪 'cull_software back' 相当于硬件裁剪 'cull_hardware clockwise' 设置，也是为什么这两个作为默认设置的原因。虽然反映裁剪方式的命名是不同的，但是由于多数时候面法向都是预先计算好的且不一定是 OGRE 期望的方式，因此如果你有使用你自定义的面法向的场景管理器，也可以设置 'cull_hardware none' 然后完全基于你的面法向进行软件裁剪。

默认 : cull_software back


### lighting

设置动态光照是处于打开状态还是关闭状态。如果光照被关闭，那么所有使用此渲染通路的物体将被完全照亮。**如果使用了顶点程序，则此属性无效。**

格式 : lighting &lt;on\|off&gt;

关闭动态光照会使得任何环境光、漫反射光、镜面反射光、放射光和阴影属性都成为了多余的。当打开光照时，物体按照顶点的法向被照亮。

默认 : lighting on


### shading

设置此渲染通路中为表现动态光照而使用的各种阴影形式。

格式 : shading &lt;flat\|gouraud\|phong&gt;

当动态光照打开时，效果就在每个顶点处生成颜色值。这些值是否全平面插入（如何插入）就依赖于这个属性设置。

**flat**

无插值参与。每个平面的阴影由平面上第一个顶点的颜色决定。

**gouraud**

平面上每个顶点的颜色采用线性插入。

**phong**

在全平面上插入顶点法线向量，被用于决定每个像素的颜色。能够得到更加自然的光照效果，但是代价也相应更高，在高级应用中表现更好。并不是所有硬件都支持此属性。

默认 : shading gouraud


### polygon_mode

设置多边形应该如何被栅格化。例如：它们应该是被填充后画出来，还是作为点（只有顶点）、线（只有外边框）画出来。

格式 : polygon_mode &lt;solid\|wireframe\|points&gt;

**solid**

一般情况 —— 填充多边形

**wireframe**

多边形只画外边框

**points**

只画每个多边形的点

默认 : polygon_mode solid


### fog_override

这个属性告诉渲染通路是否撤销场景的雾设置，而强制执行此渲染通路它自己的设置。当场景中其他的物体被雾遮挡，而你不想让雾影响某些物体时非常有用。当然反之亦然。注意这只影响固定功能雾 —— 原来的场景雾参数仍然被送入渲染器，使用 fog_params 参数绑定（这就允许你关闭固定功能雾，转而在渲染器中计算；如果你想关闭阴影雾，你可以通过阴影参数关闭它。）

格式 : fog_override &lt;override?&gt; [&lt;type&gt; &lt;colour&gt; &lt;density&gt; &lt;start&gt; &lt;end&gt;]

默认 : fog_override false

如果你指定第一个参数为真，并给出了其余参数，就表明你要告诉渲染通路如果在使用这些雾设置和使用场景设置之间选择的话，优先选择使用这些雾设置。如果你指定第一个参数为真，但没给出其余参数，就表明你要告诉渲染通路不使用任何雾设置，无论场景如何设置。以下是参数的解释：

**type**

none = 没有雾，相当于使用 'fog_override true'。

linear = 线性雾，从 &lt;start&gt; 开始到 &lt;end&gt; 结束的这一段距离有雾。

exp = 雾以几何方式增加（fog = 1/e^（distance * density））, 使用浓度 &lt;density&gt; 参数控制。

exp2 = 雾以几何的二次方增加，更加快速（fog = 1/e^（distance * density）^2），使用浓度 &lt;density&gt; 参数控制。

**colour**

3 个 0 到 1 之间的符点数组成的序列，表示红色、绿色、蓝色的亮度。

**density**

用于 'exp' 或者 'exp2' 雾类型的浓度参数。虽不用于线性模式，但是也必须写上，作为占位符。

**start**

线性雾距离镜头的开始距离。在其它模式下，尽管不用这个参数，也必须写上，作为占位符。

**end**

线性雾距离镜头的结束距离。在其它模式下，尽管不用这个参数，也必须写上，作为占位符。

示例 : fog_override true exp 1 1 1 0.002 100 10000


### colour_write

设置此渲染通路的颜色写入是打开还是关闭的。

格式 : colour_write &lt;on\|off&gt;

如果颜色写入被关闭，那么此渲染通路中没有可见像素写入屏幕。你也许认为这没什么用，但是如果你关闭颜色写入并且合理利用其他一些小的渲染设置，你可以使用这个渲染通路在执行后续的填充颜色数据的渲染通路之前初始化深度缓冲区。这样可以极大地提升效果，尤其是当你使用复杂的片断程序的时候，因为如果深度检测失败了，片断程序根本就不会运行。

默认 : colour_write on


### start_light

设置此渲染通路使用的首个光源。

格式 : start_light &lt;number&gt;

你可以使用这个属性设置此渲染通路的光源的开始位置。换句话说，如果你设置 start_light 为 2，那么被处理的第一个光源就是实际列表中的第三个光源。例如，你可以利用这个选项，使用不同的渲染通路处理第一组的几个光源对第二组的几个光源，或者使用它与**iteration**选项协作，从列表的给定点开始迭代（例如，在第一个渲染通路里处理头两个光源，然后从此开始每次两个光源重复进行）

默认 : start_light 0


### max_lights

设置此渲染通路使用的光源的最大数量。

格式 : max_lights &lt;number&gt;

光源的最大数量由渲染系统设定，通常为 8，常用于渲染固定功能材质。

默认 : max_lights 8


### iteration

设置此渲染通路是否被迭代，多次重复执行。

格式 1: iteration &lt;once \| once_per_light&gt; [lightType]

格式 2: iteration &lt;number&gt; [&lt;per_light&gt; [lightType]]

格式 3: iteration &lt;number&gt; [&lt;per_n_lights&gt; &lt;num_lights&gt; [lightType]]

示例：

**iteration once**

渲染通路只执行一次，默认设置。

**iteration once_per_light point**

渲染通路每个光源点执行一次。

**iteration 5**

此渲染通路的渲染状态将被建立，并且绘图调用将执行 5 次。

**iteration 5 per_light point**

此渲染通路的渲染状态将被建立，并且绘图调用将每个光源点各执行 5 次。

**iteration 1 per_n_lights 2 point**

此渲染通路的渲染状态将被建立，并且绘图调用将每 2 个光源点执行 5 次。

默认 : iteration once


### point_size

此设置允许你在渲染一个点列或者一个 point sprites 列时改变点的大小

格式 : point_size &lt;size&gt;

默认 : point_size 1.0


### point_sprites

这个设置指定此渲染通路的硬件 point sprites 渲染是否打开。

格式 : point_sprites &lt;on\|off&gt;

默认 : point_sprites off


### point_size_attenuation

定义点的大小是否根据视觉空间距离增加而衰减，以及以何种方式衰减。

格式 : point_size_attenuation &lt;on\|off&gt; [constant linear quadratic]

默认 : point_size_attenuation off


### point_size_min

设置点衰减（详见上面 point_size_attenuation）的最小值

格式 : point_size_min &lt;size&gt;

默认 : point_size_min 0


### point_size_max

设置点衰减（详见上面 point_size_attenuation）的最大值。

格式 : point_size_max &lt;size&gt;

默认 : point_size_max 0


## 纹理单元


### 纹理别名 texture_alias

设置此纹理单元的别名。

格式 : texture_alias &lt; 纹理别名 &gt;

示例 : texture_alias NormalMap

如果此材质被其他材质复制且在新材质中只有纹理会被改变，这种情况下，设置别名是很有用处的。

默认：如果一个纹理单元有名字，那么此纹理单元的别名默认就是这个名字。


### 纹理 texture

设置这一层要使用的静态纹理图像的名字。

格式 : texture &lt;texturename&gt; [&lt;type&gt;] [unlimited \| numMipMaps] [alpha] [&lt;PixelFormat&gt;]

示例 : texture funkywall.jpg

这个设置与 anim_texture 属性是互斥的。注意纹理文件不能包含空格。喜欢在文件名里用空格的 Windows 用户们，请不要使用空格，而使用下划线替代。

参数 type 允许你指定创建的纹理类型 —— 默认值是 '2d'，但是你可以改变；下面给出了全部列表：

**1d**

1 维纹理；即仅有 1 像素高的纹理。这种纹理可以用于在纹理内（也可能在片断程序内）编码一个功能和使用它来进行简单查找。当你用一维纹理坐标的片断程序时这个设置是很重要的，因为 GL 要求你使用相匹配的纹理类型。（虽然 D3D 会让你通过，但是为了跨平台考虑，还是要注意这一点。）为了有最好的兼容性和显示效果，纹理宽度仍然需要是 2 的整数次幂，并且有深度。

**2d**

如果你省略 type 参数，则假设 2d 为默认值。纹理的宽度和高度都最好是 2 的整数次幂，使之成为一个正方形，因为这样的设置在大多数硬件上表现最好。可以由 2D 纹理坐标指向。

**3d**

三维纹理，例如 volume 纹理。这类纹理有 2 的整数次幂的宽和高，且有深度。可由 3D 纹理坐标指向，例如通过像素渲染器（pixel shader）。

**cubic**

这类纹理由贴在立方体内侧的 6 个 2D 纹理组成。可由 3D 纹理坐标指向，并且对于立方体反射映射（cubic reflection maps）和标准映射（normal maps）很有用。

'numMipMaps' 选项允许你指定这个纹理的 mipmap 数量。默认值无限（'unlimited'）意味着 mips 的大小生成下限到 1x1。你可以随意指定一个固定的数（甚至是 0）。注意，如果你在多个材质脚本中使用相同的纹理，生成的 mipmap 数量将与装载纹理的第一个纹理单元中指定的数量一致 —— 所以务必保持你的使用一致。

'alpha' 选项允许你指定一个单独的通道（透明的）纹理作为 alpha 装载，而不是默认的载入红色通道。这有助于在固定功能的管线中使用只有 alpha 的纹理。默认值：none

&lt;PixelFormat&gt; 选项允许你指定想要创建的像素格式，可能不同于装载的纹理文件的像素格式。应当牢记于心的是最终的像素格式会受到硬件能力的限制，所以你可能得不到完全符合你的要求的格式。可用选项如下：

**PF_L8**

8 位像素格式，所有位表示 luminace。

**PF_L16**

16 位像素格式，所有位表示 luminace。

**PF_A8**

8 位像素格式，所有位表示 alpha。

**PF_A4L4**

8 位像素格式，4 位 alpha，4 位 luminace。

**PF_BYTE_LA**

2 字节像素格式，1 字节 luminace，1 字节 alpha。

**PF_R5G6B5**

16 位像素格式，5 位红，6 位绿，5 位蓝。

**PF_B5G6R5**

16 位像素格式，5 位蓝，6 位绿，5 位红。

**PF_R3G3B2**

8 位像素格式，3 位红，3 位绿，2 位蓝。

**PF_A4R4G4B4**

16 位像素格式，alpha、红、绿、蓝各 4 位。

**PF_A1R5G5B5**

16 位像素格式，1 位 alpha，红、绿、蓝各 5 位。

**PF_R8G8B8**

24 位像素格式，红、绿、蓝各 8 位。

**PF_B8G8R8**

24 位像素格式，蓝、绿、红各 8 位。

**PF_A8R8G8B8**

32 位像素格式，alpha、红、绿、蓝各 8 位。

**PF_A8B8G8R8**

32 位像素格式，alpha、蓝、绿、红各 8 位。

**PF_B8G8R8A8**

32 位像素格式，蓝、绿、红、alpha 各 8 位。

**PF_R8G8B8A8**

32 位像素格式，红、绿、蓝、alpha 各 8 位。

**PF_X8R8G8B8**

32 位像素格式，8 位红，8 位绿，8 位蓝，与 PF_A8R8G8B8 一样，不过去掉了 alpha。

**PF_X8B8G8R8**

32 位像素格式，8 位蓝，8 位绿，8 位红，与 PF_A8B8G8R8 一样，不过去掉了 alpha。

**PF_A2R10G10B10**

32 位像素格式，2 位 alpha，红、绿、蓝各 10 位。

**PF_A2B10G10R10**

32 位像素格式，2 位 alpha，蓝、绿、红各 10 位。

**PF_FLOAT16_R**

16 位像素格式，16 位符点数红

**PF_FLOAT16_RGB**

48 位像素格式，16 位符点数红，16 位符点数绿，16 位符点数蓝。

**PF_FLOAT16_RGBA**

64 位像素格式，16 位符点数红，16 位符点数绿，16 位符点数蓝，16 位符点数 alpha。

**PF_FLOAT32_R**

32 位像素格式，32 位符点数红。

**PF_FLOAT32_RGB**

96 位像素格式，32 位符点数红，32 位符点数绿，32 位符点数蓝。

**PF_FLOAT32_RGBA**

128 位像素格式，32 位符点数红，32 位符点数绿，32 位符点数蓝，32 位符点数 alpha。

**PF_SHORT_RGBA**

64 位像素格式，16 位红、绿、蓝、alpha。

**活动纹理 anim_texture**

设置用于活动纹理层的图像。这种情况下的活动纹理指的是有多幅画面，而每一幅画面都是单独的一个图像文件。有两种格式，一种是隐式的决定图像名，一种是显式的命名。

格式 1 ( 短格式 ): anim_texture &lt;base_name&gt; &lt;num_frames&gt; &lt;duration&gt;

示例 : anim_texture flame.jpg 5 2.5

上面格式 1 的例子建立了一个有 5 幅画面组成的活动纹理层，分别被命名为 flame_0.jpg，flame_1.jpg，flame_2.jpg 等等，长度 2.5 秒（2fps）。如果延时（duration）设置为 0，那么不发生自动转换，需要在代码中手动改变。

格式 2 ( 长格式 ): anim_texture &lt;frame1&gt; &lt;frame2&gt; ... &lt;duration&gt;

示例 : anim_texture flamestart.jpg flamemore.png flameagain.jpg moreflame.jpg lastflame.tga 2.5

上面格式 2 的例子也建立了与格式 1 的例子一样延时的动画，只不过这次是由 5 个单独命名的图像文件组成的。第一种格式更简单，之所以给出第二种格式是为了解决图像不能统一命名的情况。

默认 : 无


### 立方体纹理 cubic_texture

设置在立方体纹理内使用的图像。由 6 个独立的图像组成一个立方体的 6 个面。如果硬件支持的话，这类纹理常被用在反射映射（reflection maps）或者天空盒（skyboxes）中。共有两种格式，一种是简短格式，图像名按一定特殊格式命名；另一种格式虽然更灵活，可以任意取名，但是长度也相应更长。

格式 1 ( 短格式 ): cubic_texture &lt;base_name&gt; &lt;combinedUVW\|separateUV&gt;

格式 1 这种格式的基础名如 'skybox.jpg'，系统会希望你提供的各面图像名为 skybox_fr.jpg，skybox_bk.jpg，skybox_up.jpg，skybox_dn.jpg，skybox_lf.jpg，and skybox_rt.jpg。

格式 2 ( 长格式 ): cubic_texture &lt;front&gt; &lt;back&gt; &lt;left&gt; &lt;right&gt; &lt;up&gt; &lt;down&gt; separateUV

格式 2 这种格式，每一面都显式地指定，以防如果没办法按一致的标准命名。你可以使用带 separateUV 参数的格式 2，因为 combinedUVW 需要一个单独的纹理名赋值给复合 3D 纹理（见下面）。

两种格式中，最后一个参数的意思如下：

**combinedUVW**

6 个纹理被合在一个立方体纹理映射中，使用带 U，V，W 元素的 3D 纹理坐标。对于反射映射是必要的，因为你永远不知道你将要需要的是哪一个面。需要注意的是，不是所有的显卡都支持立方体环境映射。

**separateUV**

6 个纹理被分开来保存，但是被一个纹理层引用。在任一时刻只有一个纹理处于活动状态（实际上，它们被作为 6 幅画面保存起来），所以使用 2D UV 坐标。这种类型适用于天空盒（skyboxes）因为每次只有一面被渲染，而且在更老的显卡上也有硬件支持。

默认 : 无


### 绑定类型 binding_type

告诉这个纹理单元是绑定到片断处理单元还是绑定到顶点处理单元（[3.1.10 顶点纹理拾取（Vertex Texture Fetch）](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_10%20%E9%A1%B6%E7%82%B9%E7%BA%B9%E7%90%86%E6%8B%BE%E5%8F%96%EF%BC%88Vertex%20Texture%20Fetch%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.10%20%E9%A1%B6%E7%82%B9%E7%BA%B9%E7%90%86%E6%8B%BE%E5%8F%96%EF%BC%88Vertex%20Texture%20Fetch%EF%BC%89)）。

格式 : binding_type &lt;vertex\|fragment&gt;

默认 : binding_type fragment


### 内容类型 content_type

告诉这个纹理单元从哪里取得它的内容，默认是从用 texture，cubic_texture，anim_texture 属性定义的一个命名纹理中取得内容。但是，你也可以从其他自动化的来源获取。选项如下：

**named**

默认选项，内容来自一个有名字的纹理，以平常的方式从一个文件或者根据给定的名字手动创建装载。

**shadow**

这个选项允许你拉入一个阴影纹理，并且只有在你使用纹理阴影和 'custom sequence' 阴影类型（详见 [[文档 : 手册 :1-4-0:7. 阴影 \|7. 阴影）时才可用。除非你使用基于光源的渲染通路循环或者在同一渲染通路的多个纹理单元中使用 light_start 选项使得光源从更高的序号开始，否则，讨论中的阴影纹理将会从第 n 个最近光源产生阴影。当你在同一个渲染通路的多个纹理单元中使用这个选项时，每一个引用下一个阴影纹理。万一你想要在另一个渲染通路里再次使用同一个阴影纹理，阴影纹理序号在下一个渲染通路内被重置（例如：单独的 specular/gloss 渲染通路）。依靠使用这个选项，正确的光源可视区域投影就被使用固定的方式建立起来了。如果你使用渲染器，只需在渲染器中引用 texture_viewproj_matrix auto 参数即可。

格式 : content_type &lt;named\|shadow&gt;

默认 : content_type named


### 纹理坐标集 tex_coord_set

设置这个纹理层要使用的纹理坐标集。一个网格可以定义多个纹理坐标集，此属性设置这个材质使用哪一个坐标集。

格式 : tex_coord_set &lt;set_num&gt;

示例 : tex_coord_set 2

默认 : tex_coord_set 0


### 纹理寻址模式 tex_address_mode

定义在这个纹理层的纹理坐标超过 1.0 时发生的事情。你可以选择简单格式，一次对全部 3 个纹理坐标指定寻址模式，或者扩展的格式，使用三分之二的参数每个纹理坐标指定不同的模式。

简单格式 : tex_address_mode &lt;uvw_mode&gt;

扩展格式 : tex_address_mode &lt;u_mode&gt; &lt;v_mode&gt; [&lt;w_mode&gt;]

**wrap**

任何超过 1.0 的值都被置为 0.0。纹理被重复一次。

**clamp**

超过 1.0 的值被固定为 1.0。超过 1.0 的其它地方的纹理，沿用最后像素的纹理。用于当叠加过滤时，需要从 0.0 到 1.0 精确覆盖且没有模糊边界的纹理。

**mirror**

每到边界处纹理翻转，意思就是每个 1.0 u 或者 v 处纹理被镜像翻转。

**border**

超出 [0.0, 1.0] 范围的值都被置为边界色，也可以设置 tex_border_colour 属性。

默认 : tex_address_mode wrap


### 纹理边界色 tex_border_colour

设置边界色。（参考 tex_address_mode）。

格式 : tex_border_colour &lt;red&gt; &lt;green&gt; &lt;blue&gt; [&lt;alpha&gt;]

颜色的数值取值范围在 0.0 到 1.0。

示例 : tex_border_colour 0.0 1.0 0.3

默认 : tex_border_colour 0.0 0.0 0.0 1.0


### 过滤 filtering

设置当放大或缩小纹理时，使用的纹理过滤形式。这个属性有两种格式，简单格式就是指定预先定义好的过滤选项集的名字；复杂格式，就要你自己分别设定缩小，放大，mip 过滤。

**简单格式**

格式 : filtering &lt;none\|bilinear\|trilinear\|anisotropic&gt;

默认 : filtering bilinear

这种格式，你只需要提供如下的一个参数：

**none**

不使用过滤或 mipmapping 缩放。这相当于复杂格式的 'filtering point point none'。

**bilinear**

当放大或缩小一个纹理时，使用 2x2 box 过滤，从列表中挑出一个 mipmap 但是在 mipmaps 的各级之间不使用过滤。这相当于复杂格式的 'filtering linear linear point'。

**trilinear**

当放大或缩小一个纹理时，使用 2x2 box 过滤，最近的 2 个 mipmaps 被一起过滤。这相当于复杂格式的 'filtering linear linear linear'。

**anisotropic**

除了过滤算法考虑了与镜头相关的三角形坡面而不是一味地简单做一个 2x2 像素过滤之外，这个属性与 'trilinear' 相同。这使得三角形的锐角看起来较少失真。相当于复杂格式的 'filtering anisotropic anisotropic linear'。注意，要想这个属性有所不同，你还必须设置 max_anisotropy 属性。

**复杂格式**

Format: filtering &lt;minification&gt; &lt;magnification&gt; &lt;mip&gt;

Default: filtering linear linear point

这个格式给你对于缩小，放大，和 mip 过滤完全的控制权。参数如下：

**none**

无 —— 唯一的一个 'mip' 过滤可用的参数，此参数完全关闭了 mipmapping。对于缩小和放大的最低设置是 'point'。

**point**

挑选缩小和放大模式最近的像素。在 mip 模式中，此选项挑选出最符合 mipmap 要求的。

**linear**

围绕最近像素点过滤出一个 2x2 大小的像素块。在 'mip' 过滤中，这可以在 mipmap 各层级之间衔接。

**anisotropic**

仅针对缩小和放大模式可用，对于三角形的摄像机空间斜坡过滤补偿。注意，要想这个属性有所不同，还必须设置 max_anisotropy 属性。


### 最大各向异性 max_anisotropy

当过滤纹理时，设置渲染器将要补偿的各项异性的程度。这个度就是纹理在屏幕可见部分的高和宽的比值，就如伸向远方且竖直方向的纹理坐标比水平方向的纹理坐标变化的更快的地平面有比面对着你的墙更高的各向异性（如果你的目光与墙面垂直，则各向异性为 1）。为了进行补偿，你需要把 max_anisotropy 属性设置为比 1 大的值。最大值由硬件决定，而通常来说设为 8 或者 16。

为了使用这个属性，你必须设置这个纹理的缩小和 / 或放大过滤。

格式 : max_anisotropy &lt;value&gt;

默认 : max_anisotropy 1


### mipmap_bias

设置用于 mipmap 计算的偏向值，因此允许你决定哪一级的纹理细节用于哪个距离。在规定的距离计算之后应用偏向值，对每一个偏向单元做出 1 级 mipmap 级别调整。负的偏向值强制增大使用的 mip 级别，正的偏向值减小使用的 mip 级别。偏向是符点数，所以你可以使用所有的数值进行调整。

为了使用这个属性，你的硬件必须支持 mipmap 偏向（通过渲染系统能力暴露出来），而且你的缩小过滤必须被设置成 point 或 linear。

格式 : mipmap_bias &lt;value&gt;

默认 : mipmap_bias 0


### colour_op

决定这个纹理层的颜色如何与它下面的一层叠加复合起来（或者如果它是第一层的话，如何将它与光照效果复合起来）。

格式 : colour_op &lt;replace\|add\|modulate\|alpha_blend&gt;

这个方法是混合纹理层最简单的方法，因为它只需要一个参数，给你最普通的混合类型，并且自动建立两种混合方法：一种是针对单渲染通路多纹理硬件可用时的混合；另一种是针对单渲染通路多纹理硬件不可用时通过多渲染通路完成混合。然而，这是相当受限的，并且无法使用更加灵活的多纹理操作，简单地因为这些在多渲染通路回撤模式下不能被自动地支持，或者你需要使用 colour_op_multipass_fallback 显式地设置一个回撤点。

**replace**

不加调整，用纹理颜色替换所有颜色。

**add**

加颜色成分。

**modulate**

乘颜色成分。

**alpha_blend**

基于纹理 alpha 混合。

默认 : colour_op modulate

**colour_op_ex**

这是 colour_op 属性的扩展版，对于在这个纹理层与前面一个纹理层之间应用的混合允许极详细的控制。多纹理硬件可以应用更加复杂的混合操作，但受限于硬件所能用的纹理单元数。

格式 : colour_op_ex &lt;operation&gt; &lt;source1&gt; &lt;source2&gt; [&lt;manual_factor&gt;] [&lt;manual_colour1&gt;] [&lt;manual_colour2&gt;]

示例 : colour_op_ex add_signed src_manual src_current 0.5

看下面有关使用这个方法在多渲染通路和多纹理之间可能出现的问题。纹理颜色操作决定了渲染后最终平面出现的颜色。纹理单元被用来从各种不同的源中混合颜色值（例如，将通过光源计算的表面四散光与纹理的颜色叠加复合到一起）。这种方法允许你指定使用的“操作”，例如用“加”还是“乘”计算，以及用什么值作参数，是固定值还是以前算好的值。

**Operation options**

**source1**

不加任何改变地使用 source1。

**source2**

不加任何改变地使用 source2。

**modulate**

source1 乘 source2。

**modulate_x2**

source1 乘 source2，再乘 2 ( 加亮 ).

**modulate_x4**

source1 乘 source2，再乘 4 ( 加亮 ).

**add**

source1 加 source2。

**add_signed**

source1 加 source2，再减 0.5.

**add_smooth**

source1 加 source2, 再减它们的乘积。

**subtract**

source1 减 source2

**blend_diffuse_alpha**

使用向顶点插入 alpha 值的方法调整 source1，用（1-alpha）调节 source2，再把两次调节后的结果相加。

**blend_texture_alpha**

同 blend_diffuse_alpha，但是对纹理使用 alpha。

**blend_current_alpha**

同 blend_diffuse_alpha，但是对之前的 stages 使用当前 alpha（对于第一层来说，与 blend_diffuse_alpha 相同）

**blend_manual**

同 blend_diffuse_alpha，但是使用一个恒量 alpha 值，这个值在 &lt;manual&gt; 中指定。

**dotproduct**

source1 点积 source2

**blend_diffuse_colour**

使用向顶点中插入的颜色值调节 source1，然后加上用（1-colour）调节过的 source2。

**Source1 and source2 options**

**src_current**

建立于前面 stages 的颜色

**src_texture**

来自被赋值给这一层的纹理的颜色

**src_diffuse**

来自顶点的插入的四散光颜色（对于第一层来说，与 src_current 相同）。

**src_specular**

来自顶点的插入的镜面反射光颜色。

**src_manual**

在命令尾部手动指定的颜色。

例如 'modulate' 取用前面纹理层的颜色结果，并且把新的纹理乘到这个结果上。牢记颜色是 0.0-1.0 的 RGB 值，所以把它们乘在一起通过做乘法使之着色会得到相同范围的结果。但是要注意连续的乘法一般有加深变暗纹理的效果，因此有像 modulate_x2 一样的增亮操作。由于某些 APIs（包括 Direct3D）的限制，'texture' 参数只能被用作第一个参数，而不能是第二个参数。

还应注意的是，最后一个参数只有在你决定手动给操作传递数值时，才是必要的。因此，在你使用 'blend_manual' 操作时，才需要你填充这些参数。

**重点**: OGRE 试图使用多纹理硬件混合纹理层。但是，如果纹理单元数不足（GeForce2 是 2 个，GeForce3 是 4 个），它就不得不退而使用多路渲染，例如用不同纹理多次渲染同一物体。这不仅是低效的而且可供使用的混合操作的范围也小。因此，如果你使用这个方法，你就需要设置 colour_op_multipass_fallback 属性用来指定在硬件不足时使用哪种效果（默认是 'modulate'，如果你在此运用了华丽的混合操作，结果肯定不如预期来得好）。如果你希望避免这种情况，使用更简单的 colour_op 属性，虽没有太多的灵活混合操作，但是可以自动建立多路渲染，因为它只允许有直接多路等价渲染的操作。

默认 : none (colour_op modulate)


### colour_op_multipass_fallback

在如果使用了 colour_op_ex 属性且没有足够的多纹理硬件支持时，设置这个纹理层的多路后撤操作。

格式 : colour_op_multipass_fallback &lt;src_factor&gt; &lt;dest_factor&gt;

示例 : colour_op_mulitpass_fallback one one_minus_dest_alpha

因为你使用 colour_op_ex 属性创建的一些效果仅在多纹理硬件下支持，如果硬件缺乏，系统不得不后撤为多路渲染，不幸的是有许多效果并不被支持。这个属性就可以让你指定最适合你的后撤操作。

参数与 scene_blend 属性相同；这是因为多路渲染是有效地场景混合渲染，每一层都在采用了一种令物体透明的技术的前一层之上被渲染，它重复地在同一地方渲染就得到了多纹理效果。如果你使用了更简单的（同时也低灵活性的）colour_op 属性，你不需要调用属性，因为系统为你创建了后撤操作。


### alpha_op_ex

行为方式与 colour_op_ex 如出一辙，只不过它是决定 alpha 值如何在纹理层之间复合，而不是 colour 值。唯一的区别是 colour_op_ex 最后是两个颜色值，而 alpha_op_ex 是一个浮点值。


### env_map

打开 / 关闭纹理坐标效果，以决定这一层能否环境映射。

格式 : env_map &lt;off\|spherical\|planar\|cubic_reflection\|cubic_normal&gt;

环境映射依靠使用基于物体的顶点或法线与观察着眼睛之间的关系自动生成的纹理坐标使得物体看起来是有反射效果的。

**spherical**

球面环境映射。需要一个单独的纹理，这个纹理或者是被反射场景的凸透镜视图，或者是其它球面映射的纹理（平滑高亮的纹理是比较好的）。这一效果基于视线和物体顶点法线之间的关系，所以当有大量渐变法线时效果最好，例如：弯曲的物体。

**planar**

与球面环境映射相似，但是效果基于视口内的顶点位置而不是顶点法线。这一效果也因此用于平面物体（由于法线全都一样，球面 env_map 表现不好）或者没有法线的物体。

**cubic_reflection**

一种更高级的反射映射形式，使用一组 6 个纹理组成一个立方体的内表面，如果沿着场景的坐标轴看其中每一个纹理都是一个视图。在所有情况下工作得都极好，可是比球面映射需要更高规格的显卡。而且需要你绑定 cubic_texture 到这个纹理单元并且使用 'combinedUVW' 选项。

**cubic_normal**

生成三维纹理坐标，其中包括含有顶点数据的法线信息中的摄像机空间法向量。此外，这个特性的完全使用也需要设置 'combinedUVW' 选项的 cubic_texture。

默认 : env_map off


### scroll

给纹理设置一个固定的滚动偏移量。

格式 : scroll &lt;x&gt; &lt;y&gt;

此方法给纹理的偏移在这一层设定了一个固定的量。对于不改变纹理坐标模式的小调整很有用。但是如果你想要一个动态的滚动效果，详见 scroll_anim 属性。


### scroll_anim

给纹理层设置一个动态的滚动。对于在纹理层上创建固定速度的滚动效果很有用（对于不同的滚动速度，详见 wave_xform 属性）。

格式 : scroll_anim &lt;xspeed&gt; &lt;yspeed&gt;


### rotate

将一个纹理旋转一个固定的角度。

这个属性只将纹理方向旋转一个固定的角度，对于固定的调整比较有用。如果你想要动态调整，详见 rotate_anim。

格式 : rotate &lt;angle&gt;

参数 &lt;angle&gt; 是逆时针旋转的角的度数。


### rotate_anim

为这一层创建动态旋转效果。对于创建固定速度的旋转动作比较有用（对于变速的情况，详见 wave_xform）。

格式 : rotate_anim &lt;revs_per_second&gt;

参数 &lt;revs_per_second&gt; 是每秒逆时针旋转的次数。


### scale

调整这个纹理层应用的比例系数。用于调整纹理的大小，不改变几何体。这是一个固定的比例系数，如果你想要动态的比例系数，详见 wave_xform。

格式 : scale &lt;x_scale&gt; &lt;y_scale&gt;

比例的有效值要大于 0，比例系数如果为 2，就表示在那一维上的纹理有 2 倍那么大。


### wave_xform

建立一个基于波功能的动态改变形式。用于更高级的纹理层改变效果。你可以在一个纹理层中随意添加多个此属性的实例。

格式 : wave_xform &lt;xform_type&gt; &lt;wave_type&gt; &lt;base&gt; &lt;frequency&gt; &lt;phase&gt; &lt;amplitude&gt;

示例 : wave_xform scale_x sine 1.0 0.2 0.0 5.0

**xform_type**

**scroll_x**

变动 x 滚动值

**scroll_y**

变动 y 滚动值

**rotate**

变动旋转值

**scale_x**

变动 x 比例值

**scale_y**

变动 y 比例值

**wave_type**

波形：sine 正弦，triangle 三角，square 方形，sawtooth 锯齿，inverse_sawtooth 反锯齿。

**sine**

典型的正弦波，在最小值和最大值之间平稳地循环。

**triangle**

以恒定的速度增加减少的有角度的波，在极值时立即改变。

**square**

最大是波长的一半，最小是瞬时转换之间的停止时间。

**sawtooth**

经过一段时间，从最小逐渐持续增加到最大，最后立即回到最小。

**inverse_sawtooth**

经过一段时间，从最大逐渐持续减少到最小，最后又立即返回最大。

**base**

基值，如果 amplitude &gt; 0 就是指最小值，amplitdue &lt; 0 就是指最大值。

**frequency**

频率，波每秒重复的次数，即速度。

**phase**

波开始的偏移量。

**amplitude**

波的大小。幅度（可负）。

波的输出范围在 {base, base+amplitude}。所以，以在 x 方向调整纹理为例，沿正弦波方向从 1（标准值）调整到 5，即表示每 5 秒一个周期（每秒 0.2 个波）。


### transform

这个属性允许你为纹理单元指定一个 4x4 变换矩阵，因而取代上述的滚动、旋转、比例属性。

格式 : transform m00 m01 m02 m03 m10 m11 m12 m13 m20 m21 m22 m23 m30 m31 m32 m33

上面 4x4 矩阵中的数值序号为 m&lt;row&gt;&lt;col&gt;，前面一个为行号，后面一个为列号。


## 在渲染通路中使用顶点程序和片断程序

**参数详解**

参数可以被指定为如下四种之一。无论你要定义一个参数只为这个程序特别使用，还是指定默认的程序参数，语法都是一样的。程序特殊使用的参数设置会重载默认值。

* param_indexed
* param_indexed_auto
* param_named
* param_named_auto


### param_indexed

此命令设置索引参数的数值。

格式：param_indexed &lt;index&gt; &lt;type&gt; &lt;value&gt;

示例：param_indexed 0 float4 10.0 0 0 0

'index' 简单地是表示应当被写进参数表的位置的数值，应当从你的程序定义派生。

'type' 的值可以是 float4，matrix4x4，float&lt;n&gt;，int4，int&lt;n&gt;。

'value' 简单地是由空格或者 tab 制表符分割的数值列表，这些数值可以被转换成你指定过的类型。


### param_indexed_auto

此命令告诉 Ogre 用源数值自动更新给定的参数。这就将你从编写代码的繁重劳动中解放出来，当参数总是在改变的时候，不用逐桢去更新。

格式：param_indexed_auto &lt;index&gt; &lt;value_code&gt; &lt;extra_params&gt;

示例：param_indexed_auto 0 worldviewproj_matrix

'value_code' 是如下列表中的一个值：

**world_matrix**

当前世界矩阵。

**inverse_world_matrix**

当前世界矩阵的反转矩阵。

**transpose_world_matrix**

当前世界矩阵的转置矩阵

**inverse_transpose_world_matrix**

当前世界矩阵的反转转置矩阵。

**world_matrix_array_3x4**

一组世界矩阵，每一个由 3x4 矩阵表示（3 行 4 列）通常用于 doing hardware skinning。你应当令你的顶点程序入口数量足够多以便应付实际使用中的骨骼数量，即要有一组 numBones*3 个 float4。

**view_matrix**

当前视点矩阵。

**inverse_view_matrix**

当前视点矩阵的反转矩阵。

**transpose_view_matrix**

当前视点矩阵的转置矩阵。

**inverse_transpose_view_matrix**

当前视点矩阵的反转转置矩阵。

**projection_matrix**

当前投影矩阵。

**inverse_projection_matrix**

当前投影矩阵的反转矩阵。

**transpose_projection_matrix**

当前投影矩阵的转置矩阵。

**inverse_transpose_projection_matrix**

当前投影矩阵的反转转置矩阵。

**worldview_matrix**

当前世界视点联合矩阵。

**inverse_worldview_matrix**

当前世界视点联合矩阵的反转矩阵。

**transpose_worldview_matrix**

当前世界视点联合矩阵的转置矩阵。

**inverse_transpose_worldview_matrix**

当前世界视点联合矩阵的反转转置矩阵。

**viewproj_matrix**

当前视点投影联合矩阵。

**inverse_viewproj_matrix**

当前视点投影联合矩阵的反转矩阵。

**transpose_viewproj_matrix**

当前视点投影联合矩阵的转置矩阵。

**inverse_transpose_viewproj_matrix**

当前视点投影联合矩阵的反转转置矩阵。

**worldviewproj_matrix**

当前世界视点投影联合矩阵。

**inverse_worldviewproj_matrix**

当前世界视点投影联合矩阵的反转矩阵。

**transpose_worldviewproj_matrix**

当前世界视点投影联合矩阵的转置矩阵。

**inverse_transpose_worldviewproj_matrix**

当前世界视点投影联合矩阵的反转转置矩阵。

**render_target_flipping**

如果绕过投影矩阵变换，此值用来调节改变 y 坐标。如果渲染目标需要纹理翻转，此值为-1，反之，为 +1。

**light_diffuse_colour**

给定光源的漫反射颜色；这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将被置为黑。

**light_specular_colour**

给定光源的镜面反射颜色；这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将被置为黑。

**light_attenuation**

一个 float4 包含给定光源的 4 个光源衰减变量。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。参数的顺序是范围，常量衰减，线性衰减，二次衰减。

**spotlight_params**

一个 float4 包含 3 个点光源参数和一个控制值。参数的顺序是 cos（内角 /2），cos（外角 /2），falloff，且最后的 w 值为 1.0f。对于非点光源，此值为 float4(1,0,0,1)。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的第 'n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果光源比这个还少，那么细节就不像点光源了。

**light_position**

给定光源在世界空间中的位置。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。注意，这个属性可用于所有光源，甚至直射光，因为参数被设置为 4D 向量。点光源会是（pos.x，pos.y，pos.z，1.0f），与此同时，直射光会是（-dir.x，-dir.y，-dir.z，0.0f）。像点积之类的操作在这两种情况下都可以使用。

**light_direction**

给定光源在世界空间内的方向。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。 不建议使用 —— 这个属性只用于直射光，而我们建议你使用 light_position 替代，因为它返回的是一个一般的 4D 向量。

**light_position_object_space**

给定光源在物体空间中的位置（即物体在（0，0，0）时）。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。注意，这个属性可用于所有光源，甚至直射光，因为参数被设置为 4D 向量。点光源会是（pos.x，pos.y，pos.z，1.0f），与此同时，直射光会是（-dir.x，-dir.y，-dir.z，0.0f）。像点积之类的操作在这两种情况下都可以使用。

**light_direction_object_space**

给定光源在物体空间内的方向（即物体在（0，0，0）时）。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。 不建议使用，点光源除外，对于直射光我们建议你使用 light_position_object_space 替代，因为它返回的是一个一般的 4D 向量。

**light_distance_object_space**

给定光源距物体中心的距离 —— 这对于相对小的物体的每个顶点距离计算是有用的估计。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的第 'n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。

**light_position_view_space**

给定光源在视点空间中的位置（即物体在（0，0，0）时）。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。注意，这个属性可用于所有光源，甚至直射光，因为参数被设置为 4D 向量。点光源会是（pos.x，pos.y，pos.z，1.0f），与此同时，直射光会是（-dir.x，-dir.y，-dir.z，0.0f）。像点积之类的操作在这两种情况下都可以使用。

**light_direction_view_space**

给定光源在视点空间内的方向（即物体在（0，0，0）时）。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。如果附近没有光源，那么参数将全被置为 0。 不建议使用，点光源除外，对于直射光我们建议你使用 light_position_object_space 替代，因为它返回的是一个一般的 4D 向量。

**light_power**

给定光源的 ' 能量 ' 调节，HDR 渲染中有用。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源 —— 注意直射光总在列表的首位且总是存在的）。

**light_diffuse_colour_array**

同 light_diffuse_colour，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_specular_colour_array**

同 light_specular_colour，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_attenuation_array**

同 light_attenuation，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**spotlight_params_array**

同 spotlight_params，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_position_array**

同 light_position，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_direction_array**

同 light_direction，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_position_object_space_array**

同 light_position_object_space，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_direction_object_space_array**

同 light_direction_object_space，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_distance_object_space_array**

同 light_distance_object_space，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_position_view_space_array**

同 light_position_view_space，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_direction_view_space_array**

同 light_direction_view_space，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**light_power_array**

同 light_power，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**ambient_light_colour**

场景中当前设置的环境光颜色。

**surface_ambient_colour**

渲染通路的环境反射颜色属性（详见 [ambient](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89) 部分）。这样允许你手动访问固定功能管线属性。

**surface_diffuse_colour**

渲染通路的漫反射颜色属性（详见 [diffuse](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89) 部分）。这样允许你手动访问固定功能管线属性。

**surface_specular_colour**

渲染通路的镜面反射颜色属性（详见 [specular](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89) 部分）。这样允许你手动访问固定功能管线属性。

**surface_emissive_colour**

渲染通路的自发光的量（详见 [emissive](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89) 部分）。这样允许你手动访问固定功能管线属性。

**surface_shininess**

渲染通路的闪光，影响镜面高光的大小（详见 [specular](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89) 部分）。这样允许你手动绑定固定功能管线属性。

**derived_ambient_light_colour**

源环境光颜色，其 'r'、'g'、'b' 分量由 surface_ambient_colour 与 ambient_light_colour 相乘之积分别填充，'a' 分量由平面环境 alpha 分量填充。

**derived_scene_colour**

源场景色，其 'r'、'g'、'b' 分量由 derived_ambient_light_colour 与 surface_emissive_colour 相加之和分别填充，'a' 分量由平面漫反射 alpha 分量填充。

**derived_light_diffuse_colour**

源漫反射光颜色，其 'r'、'g'、'b' 分量由 surface_diffuse_colour 与 light_diffuse_colour 相乘之积分别填充，'a' 分量由平面漫反射 alpha 分量填充。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源）。

**derived_light_specular_colour**

源镜面反射光颜色，其 'r'、'g'、'b' 分量由 surface_specular_colour 与 light_specular_colour 相乘之积分别填充，'a' 分量由平面镜面反射 alpha 分量填充。这需要 'extra_params' 中的一个索引，并且关联到能够影响到这个物体的 ' 第 n 个 ' 最近光源（0 代表最近的光源）。

**derived_light_diffuse_colour_array**

同 derived_light_diffuse_colour，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**derived_light_specular_colour_array**

同 derived_light_specular_colour，只不过这是一组参数多个光源，且 'extra_params' 表示要被处理的 ' 第 n 个最近 ' 光源的数量。这个参数与基于光源的渲染通路循环选项不兼容但是可以被单渲染通路光照使用。

**fog_colour**

场景中当前设置的雾的颜色。

**fog_params**

场景中当前设置的雾的参数。（（exp_density，linear_start，linear_end，1.0 /（linear_end - linear_start））。

**camera_position**

世界空间中当前摄像机的位置。

**camera_position_object_space**

物体空间中当前摄像机的位置（当物体在（0，0，0）时）。

**time**

当前时间，可选参数（或者为 1.0f，如果没有提供的话）。

**time_0_x**

单浮点时间值，基于作为 'extra_params' 给出的“周期时间”重复。

**costime_0_x**

time_0_x 的余弦。

**sintime_0_x**

time_0_x 的正弦。

**tantime_0_x**

time_0_x 的正切。

**time_0_x_packed**

time0_x，sintime0_x，costime0_x，tantime0_x 四元向量。

**time_0_1**

同 time0_x 但是取值范围限制在 [0..1]。

**costime_0_1**

同 costime0_x 但是取值范围限制在 [0..1]。

**sintime_0_1**

同 sintime0_x 但是取值范围限制在 [0..1]。

**tantime_0_1**

同 tantime0_x 但是取值范围限制在 [0..1]。

**time_0_1_packed**

同 time0_x_packed 但是所有值的取值范围限制在 [0..1]。

**time_0_2pi**

同 time0_x 但是取值范围限制在 [0..2*Pi]。

**costime_0_2pi**

同 costime0_x 但是取值范围限制在 [0..2*Pi]。

**sintime_0_2pi**

同 sintime0_x 但是取值范围限制在 [0..2*Pi]。

**tantime_0_2pi**

同 tantime0_x 但是取值范围限制在 [0..2*Pi]。

**time_0_2pi_packed**

同 time0_x_packed 但是取值范围限制在 [0..2*Pi]。

**frame_time**

当前桢时间，可选参数（或者为 1.0f，如果没有提供的话）。

**fps**

当前每秒桢数。

**viewport_width**

当前视口像素宽度。

**viewport_height**

当前视口像素高度。

**inverse_viewport_width**

当前视口像素宽度倒数（1.0/ 当前视口像素宽度）。

**inverse_viewport_height**

当前视口像素高度倒数（1.0/ 当前视口像素高度）。

**viewport_size**

视口大小，四元向量 viewport_width、viewport_height、inverse_viewport_width、inverse_viewport_height。

**texel_offsets**

提供对纹理元素到像素映射的渲染系统特定纹理坐标偏移量细节。float4（horizontalOffset，verticalOffset，horizontalOffset / viewport_width，verticalOffset / viewport_height）。

**view_direction**

物体空间中视点方向向量。

**view_side_vector**

视点本地 X 坐标。

**view_up_vector**

视点本地 Y 坐标。

**fov**

垂直弧线可视区域。

**near_clip_distance**

近裁剪距离，世界单位。

**far_clip_distance**

远裁剪距离，世界单位（对于无限视点投影来说可能是 0）。

**texture_viewproj_matrix**

应用于被指定作为“阴影接受者”的顶点程序或者是纹理单元被标记为 content_type shadow；这为当前阴影投影机提供了视点 / 投影矩阵的细节。可选的 'extra_params' 入口指定了投影机表示哪个光源（对于 content_type shadow 的例子，在一个渲染通路里可能出现不止一个阴影纹理），其中 0 是默认的并且表示该渲染通路引用的第一个光源。

**scene_depth_range**

提供有关从当前被用来渲染的摄像机观察到的深度范围信息。float4（minDepth，maxDepth，depthRange，1 / depthRange）。

**shadow_scene_depth_range**

提供有关从与选定的光源相关的阴影摄像机观察到的深度范围信息。需要一个光源索引参数。float4（minDepth，maxDepth，depthRange，1 / depthRange）。

**texture_size**

提供选定纹理单元的纹理大小。需要一个纹理单元索引参数。float4（width，height，depth，1）。对于 2D 纹理，深度设置为 1，对于 1D 纹理，高度和深度设置为 1。

**inverse_texture_size**

提供选定纹理单元的纹理大小的倒数。需要一个纹理单元索引参数。float4（1 / width，1 / height，1 / depth，1）。对于 2D 纹理，深度设置为 1，对于 1D 纹理，高度和深度设置为 1。

**packed_texture_size**

提供选定纹理单元的打包纹理大小。需要一个纹理单元索引参数。float4（width，height，1 / width，1 / height）。对于 3D 纹理，深度被忽略掉，对于 1D 纹理，高度被设置为 1。

**pass_number**

设置 gpu 参数中活动渲染通路索引号。技术中第一个渲染通路编号为 0，第二个编号为 1，以此类推。这对于需要知道各是什么渲染通路的多通路渲染（如皮毛或者模糊渲染）是有用的。依靠在程序定义中的 [默认的程序参数](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_4%20%E9%A1%B6%E7%82%B9%E7%A8%8B%E5%BA%8F%E4%B8%8E%E7%89%87%E6%96%AD%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A3%B0%E6%98%8E%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.4%20%E9%A1%B6%E7%82%B9%E7%A8%8B%E5%BA%8F%E4%B8%8E%E7%89%87%E6%96%AD%E7%A8%8B%E5%BA%8F%E7%9A%84%E5%A3%B0%E6%98%8E) 列表里设置自动参数，没有必要在每个渲染通路中设置渲染通路号参数。（详见 [fur_example](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89)）

**pass_iteration_number**

用于需要知道当前渲染通路循环数是多少的 GPU 程序。渲染通路的第一次循环编号为 0。最后一次循环号是渲染通路循环数-1。如果一个渲染通路它的循环属性被置为 5，那么最后一次的循环号（第 5 次执行这个渲染通路）是 4。（详见 [iteration](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89)）

**animation_parametric**

用于硬件顶点动画。对于变形动画来说，设置参数值（0..1）表示第一个位置关键桢（绑定到位置）与第二个位置关键桢（绑定到第一个空的纹理坐标）之间的距离，以便顶点程序可以在它们之间插值。对于姿势动画，说明一组最多有 4 个参数权值，它们应用于一组姿势，每组姿势最多 4 个，( 每一个绑定到常量的 x、y、z、w 上），一个姿势一个。原始位置被放在一般的位置缓冲器中，且权重为 1.0 的姿势所在的位置的偏移量是前 n 个空纹理坐标；'n' 由传递给 includes_pose_animation 的值决定。如果需要的同步姿势比 4 个多，那么你会需要不止一个渲染器常量存放这些参数值，在这种情况下，你需要使用这个进行多次绑定，引用不同的常量入口；第二个会包含姿势 5 到 8 的参数，第三个包含姿势 9 到 12 的参数，以此类推。

**custom**

这允许你映射一个自定义参数到 GPU 程序参数上（详见**Renderable::setCustomParameter**）。它需要你添上 'extra_params' 中索引，该索引在 Renderable::setCustomParameter 调用时会被用到，且这会保证无论何时使用这个 Renderable，它都会有其自定义的参数映射。重要的是这个参数已经在所有 Renderables 上定义了，且包含这个自动映射的材质赋值给 Renderables，否则过程会失败。


### param_named

这同 param_indexed 是一样的，但是使用一个命名的参数替代索引号。这只能与包括参数名的高级程序一起使用；如果你要使用一个编译程序，那么你除了索引别无选择。注意，你也可以在高级程序中使用索引参数，但是这样它就不便移动了，因为如果你用高级程序渲染参数，索引号会发生改变。

格式 : param_named &lt;name&gt; &lt;type&gt; &lt;value&gt;

示例：param_named shininess float4 10.0 0 0 0

这里的 type 是必需的，因为当材质脚本被分析时，程序并不被编译和装载，所以在这时，我们不知道参数是什么类型。程序只有被使用过后才装载和编译，为的是节约内存。


### param_named_auto

功能同 param_indexed_auto，只不过这个是有名字的，用于高级程序。

格式：param_named_auto &lt;name&gt; &lt;value_code&gt; &lt;extra_params&gt;

示例：param_named_auto worldViewProj WORLDVIEWPROJ_MATRIX

extra_params 允许的数值代码和意思详见 [param_indexed_auto](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_9%20%E5%9C%A8%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%E4%B8%AD%E4%BD%BF%E7%94%A8%E9%A1%B6%E7%82%B9%E7%A8%8B%E5%BA%8F%E5%92%8C%E7%89%87%E6%96%AD%E7%A8%8B%E5%BA%8F%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.9%20%E5%9C%A8%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%E4%B8%AD%E4%BD%BF%E7%94%A8%E9%A1%B6%E7%82%B9%E7%A8%8B%E5%BA%8F%E5%92%8C%E7%89%87%E6%96%AD%E7%A8%8B%E5%BA%8F)。


## 粒子

**可用的粒子系统属性**

* [quota](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22quota%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [material](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22material%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [particle_width](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22particle_width%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [particle_height](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22particle_height%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [cull_each](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22cull_each%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [billboard_type](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22billboard_type%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [billboard_origin](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22billboard_origin%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [billboard_rotation_type](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22billboard_rotation_type%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [common_direction](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_direction%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [common_up_vector](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_up_vector%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [renderer](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22renderer%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [sorted](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22sorted%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [local_space](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22local_space%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [point_rendering](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22point_rendering%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [accurate_facing](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22accurate_facing%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [iteration_interval](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22iteration_interval%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)
* [nonvisible_update_timeout](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22nonvisible_update_timeout%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)


## 粒子系统属性

这部分描述了可以在任何一个使用脚本的粒子系统上设置的属性。所有属性都有默认值，所有设置在脚本中都是可选的。


### quota

设置这个系统在某一时刻所允许包含的最多粒子数。当达到这个限制时，粒子发射器将不允许再发射粒子，直到某些粒子被消灭（例如，它们的 time_to_live 存续时间用尽）。值得注意的是，你几乎是肯定要改变这个设置的，因为默认值太短了（粒子池只能增加，而不能减少）。

格式 : quota &lt;max_particles&gt;

示例 : quota 10000

默认 : 10


### **material**

设置这个系统中的全体粒子将要使用的材质的名字。此系统中的全部粒子使用相同的材质，尽管每一个粒子可以通过使用它自己的颜色属性为材质附加颜色。

格式 : material &lt;material_name&gt;

示例 : material Examples/Flare

默认 : none （空材质）


### **particle_width**

在世界坐标中，设置粒子的宽度。注意，当 billboard_type（）被设置为 'point' 或者 'perpendicular_self' 时，这个属性是绝对值；而当 billboard_type 是 'oriented_common'，'oriented_self' 或者 'perpendicular_common' 时，它是依方向向量的长度而定的。

格式 : particle_width &lt;width&gt;

示例 : particle_width 20

默认 : 100


### **particle_height**

在世界坐标中，设置粒子的高度。注意，当 billboard_type（）被设置为 'point' 或者 'perpendicular_self' 时，这个属性是绝对值；而当 billboard_type 是 'oriented_common'，'oriented_self' 或者 'perpendicular_common' 时，它是依方向向量的长度而定的。

格式 : particle_height &lt;height&gt;

示例 : particle_height 20

默认 : 100


### **cull_each**

所有的粒子系统都被包括在一个包含这个系统所有粒子的边界盒内。这对一般的局部的有限的粒子系统，如大部分粒子是同时可见的或是同时不可见的，是足够的。但是，对于那些在更大面积上扩散的粒子（例如，一个雨水系统），实际上你也许想要单独的处理每一个粒子以便节约时间，因为很可能只有一小部分的粒子是可见的。你可以通过设置 cull_each 的参数为真，做到这一点。

格式 : cull_each &lt;true\|false&gt;

示例 : cull_each true

默认 : false


### **renderer**

粒子系统并不渲染它本身，它们通过 ParticleRenderer 类完成这一点。那些类被带着一个管理器注册，为的是给粒子系统提供一个特殊的外观。OGRE 默认配置了一个基于公告板的渲染器（billboard-based renderer），但是更多的可以通过插件增加。粒子渲染器要用一个唯一的名字注册，你可以利用这个名字决定使用哪个渲染器。默认的是 'billboard'。

粒子渲染器可以有属性，并且可以通过在根粒子系统中设定属性进行传递。

格式 : renderer &lt;renderer_name&gt;

默认 : billboard


### **sorted**

默认情况下，粒子是不排序的。若设定这个属性为 ' 真 '，粒子将会根据摄影机的位置关系被排序，最远的优先。通过花费一小点儿排序的代价，就可以制作出特定的渲染效果。

格式 : sorted &lt;true\|false&gt;

默认 : false


### **local_space**

默认情况下，粒子是被发射到世界空间的，例如，如果你改变了粒子系统所在的节点，它不会影响到粒子本身（只是粒子发射器）。这就意味着给出了一般期望的行为，即建立了真实世界的粒子离开发射它们的物体后独立运动的模型。但是，要建立一些效果，你可能想让粒子保持附加在粒子发射器所在的局部空间内并直接跟随它们。这个选项就可以让你实现这一点。

格式 : local_space &lt;true\|false&gt;

默认 : false


### **billboard_type**

这实际上是 ' 公告板 ' 粒子渲染器（默认）的一个属性，同时也是通过在系统声明中直接声明的方法给粒子渲染器传递属性的一个示例。使用默认渲染器的粒子被用公告板进行渲染，即由 2 个旋转到面向指定方向的三角形组成的矩形构成的平面。但是，定向一个公告板有不止一种方法。传统方法是公告板直接面对摄像机：这也是默认的方法。但是，这种安排只是对于表现像光晕一样的模糊的球状物看上去还算可以。对于更多的诸如激光射线这样的线性效果，事实上你想要粒子有其自己的方向。

格式 : billboard_type &lt;point\|oriented_common\|oriented_self\|perpendicular_common\|perpendicular_self&gt;

示例 : billboard_type oriented_self

默认 : point

此参数有如下选项：

**point**

默认排列，它估计球状粒子和公告板总是完全面对摄像机。

**oriented_common**

粒子面向一个共同的固定的方向向量（参看 [common_direction](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_direction%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)），即它们的局部 Y 轴。公告板只围绕这个轴旋转，给粒子一些方向感。利于暴风雨，流星等粒子按一个方向移动的效果 —— 较 oriented_self（见下面）略快。

**oriented_self**

粒子面向它们自己的方向向量，即它们的局部 Y 轴。隨着粒子改变方向，公告板也重定向它自己面向这个方向。利于激光射线，焰火，以及其它的按其自己的方向行进的粒子。

**perpendicular_common**

粒子垂直于一个共同的固定的方向向量（参看 [common_direction](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_direction%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)），即它们的局部 Z 轴和它们的局部 Y 轴共同确定的平面，有共同的方向和向上的向量（参看 [common_up_vector](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_up_vector%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)）。公告板从未旋转至面向摄像机，你可能使用双面材质以便确保粒子不会被背面包含。利于光环，圆环等粒子将垂直于地面的效果 —— 较 perpendicular_self（见下面）略快。

**perpendicular_self**

粒子垂直于它们自己的方向向量，即它们的 Z 轴和 Y 轴共同确定的平面，有它们自己的方向向量和共同的向上向量（参见 [common_up_vector](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22common_up_vector%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7)）。公告板从未旋转至面向摄像机，你可能使用双面材质以便确保粒子不会被背面包含。利于圆环堆等粒子将垂直于它们的行进方向的效果。


### **billboard_origin**

指定所有公告板粒子的起始点，控制公告板粒子的出现位置。

格式 : billboard_origin &lt;top_left\|top_center\|top_right\|center_left\|center\|center_right\|bottom_left\|bottom_center\|bottom_right&gt;

示例 : billboard_origin top_right

默认 : center

此参数有如下选项：

**top_left**

公告板起始点在左上角。

**top_center**

公告板起始点在顶边中央。

**top_right**

公告板起始点在右上角。

**center_left**

公告板起始点在左边中央。

**center**

公告板起始点在中央。

**center_right**

公告板起始点在右边中央。

**bottom_left**

公告板起始点在左下角。

**bottom_center**

公告板起始点在底边中央。

**bottom_right**

公告板起始点在右下角。


### **billboard_rotation_type**

默认情况下，公告板粒子会根据粒子旋转去旋转纹理坐标。但是旋转纹理坐标有一些缺点，例如，纹理的四角会在旋转后丢失，而当使用折叠地址模式或者子纹理采样时，公告板的四角会被不想要的纹理区域填充。这个设置允许你指定其它的旋转类型。

格式 : billboard_rotation_type &lt;vertex\|texcoord&gt;

示例 : billboard_rotation_type vertex

默认 : texcoord

此参数有如下选项：

**vertex**

公告板粒子将依据粒子旋转规则绕它们面向的方向旋转它们的顶点。旋转顶点满足纹理角完全匹配公告板角，因此有上面提及的优点，但是需要花费较多的时间以生成顶点。

**texcoord**

公告板粒子将依据粒子旋转规则旋转纹理坐标。旋转纹理坐标比旋转顶点更快，但是有上面提及的一些缺点。


### **common_direction**

如果 [billboard_type](http://ogre3d.cn/wiki/index.php?title=%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1_%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%22%20%5Cl%20%22billboard_type%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7) 被设置为 oriented_common 或者 perpendicular_common 才需要，这个向量是用于定位系统中所有粒子的共用向量。

格式 : common_direction &lt;x&gt; &lt;y&gt; &lt;z&gt;

示例 : common_direction 0 -1 0

默认 : 0 0 1


### **common_up_vector**

如果 [billboard_type](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22billboard_type%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7) 被设置为 perpendicular_self 或者 perpendicular_common 才需要，这个向量是用于定位系统中所有粒子的共用向上向量。

格式 : common_up_vector &lt;x&gt; &lt;y&gt; &lt;z&gt;

示例 : common_up_vector 0 1 0

默认 : 0 1 0


### **point_rendering**

事实上，这是‘公告板’粒子渲染器（默认设置）的一个属性，设置与否关系到公告板将使用点渲染而不是手动生成渲染画面。

默认情况下，公告板区域依靠内存中的一块纹理矩形生成的几何体渲染的，要考虑到大小和方向设置，以及将它装载入显卡的问题。可选择的方式是使用硬件指针渲染，即意味着每个公告板只有一个位置需要被传送而不是 4 个，并且硬件依据渲染状态排序如何渲染。

虽然使用点渲染较手动生成渲染区域更快，但是多了许多限制。限制如下：

仅支持 'point' 定向类型

每个粒子的大小和外观由材质通路控制（[point_size](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22point_size%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89)， [point_size_attenuation](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22point_size_attenuation%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89)，[point_sprites](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_1_2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Cl%20%22point_sprites%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.1.2%20%E6%B8%B2%E6%9F%93%E9%80%9A%E8%B7%AF%EF%BC%88Pass%EF%BC%89)）

不支持每个粒子大小（源自上文）

不支持每个粒子旋转，且这只能通过材质定义中的纹理单元旋转控制

仅支持 'center' 起始点

一些驱动程序对于支持的点的大小有上限限制 —— 甚至相同卡的不同 API 之间也可能区别！不要依靠点的大小让屏幕上的东西变得很大，因为它们可能会受限于某些卡。大小的上限可能在 64 到 256 像素之间。

如果你使用这个选项，你将几乎是肯定要打开材质通路中的 point attenuation 和 point sprites。


### **accurate_facing**

事实上，这是‘公告板’粒子渲染器（默认设置）的一个属性，且设置与否关系到公告板区域将使用一个有些慢但更精确的计算使公告板面向摄像机。默认使用摄像机方向，这样更快，但同时意味着，当你旋转摄像机时，公告板不会保持相同的方向。'accurate_facing true' 选项基于从每一个公告板到摄像机的向量进行计算，即意味着即使摄像机旋转方向也是一致的。

格式 : accurate_facing on\|off

默认 : accurate_facing off 0


### **iteration_interval**

通常粒子系统是基于帧率被更新的；但是随着更极端的帧率范围，这可以给出不同的结果，特别是低帧率。你可以使用这个选项设定升级频率为固定的间隔，在低帧率时，粒子更新会按固定的间隔重复，直到帧率恢复正常。0 值意为默认帧时间循环。

格式 : iteration_interval &lt;secs&gt;

示例 : iteration_interval 0.01

默认 : iteration_interval 0


### **nonvisible_update_timeout**

当粒子系统在其已经无法可见需要停止更新时设置。默认情况下，可见粒子系统一直更新，即使不在视口内。这意味着当它们进入视口时可以保证一致性。但是，更新粒子系统所花费的代价可能是很昂贵的。

这个选项让你在粒子系统上设置一个 'timeout' 时限，以便如果它这么长时间不可见，即停止更新，直到它下次可见。值 0 表示关闭 timeout，总是更新。

格式 : nonvisible_update_timeout &lt;secs&gt;

示例 : nonvisible_update_timeout 10

默认 : nonvisible_update_timeout 0


## 粒子发射器

粒子发射器按**类型**划分为几类，例如：**Point**发射器从单独一点发射，而**Box**发射器则是从一块儿区域随机发射。新的发射器可以通过插件加入到 Ogre 中去。向系统中增加一个发射器需要将发射器嵌入到其它块中，以关键字“emitter”后跟发射器类型名（大小写敏感）开头。Ogre 现在支持 'Point'，'Box'，'Cylinder'，'Ellipsoid'，'HollowEllipsoid' 以及 'Ring' 发射器。


### 粒子发射器通用属性

* angle
* colour
* colour_range_start
* colour_range_end
* direction
* emission_rate
* position
* velocity
* velocity_min
* velocity_max
* time_to_live
* time_to_live_min
* time_to_live_max
* duration
* duration_min
* duration_max
* repeat_delay
* repeat_delay_min
* repeat_delay_max


### **粒子发射器属性**

这部分描述的是所有小辫子发射器的通用属性。特殊的发射器类型可能也支持它们自己的额外的属性。


### angle

设置发射的粒子可以偏离发射方向的最大角（按角度计算，参看 direction）。此值设置为 10 允许粒子在任一方向上最多偏离发射方向 10 度。值 180 意味着可以朝任意方向发射，而 0 意味着总是精确地沿发射器方向发射。

格式 : angle &lt;degrees&gt;

示例 : angle 30

默认 : 0


### **colour**

为所有发射的粒子设置一个静态颜色。也可参看 colour_range_start 和 colour_range_end 属性，设置一组颜色。颜色参数的格式是 "r g b a"，每个分量的取值范围是从 0 到 1 之间，alpha 值是可选项（如果未指定，则假定 alpha 为 1）。

格式 : colour &lt;r g b&gt; [&lt;a&gt;]

示例 : colour 1 0 0 1

默认 : 1 1 1 1


### **colour_range_start 和 colour_range_end**

除了这两个属性必须一起制定外，其它的都和 'colour' 属性一样，并且制定了被发射出去的粒子的可用颜色范围。实际的颜色将会在这两个值之间随机选择。

格式 : 同 colour

示例（随机生成红蓝之间的颜色）: colour_range_start 1 0 0 colour_range_end 0 0 1

默认 : 都是 1 1 1 1


### **direction**

设置发射器的方向。这与粒子系统所在的 SceneNode 有关，意思就是随着其它可移动物体改变节点方向，发射器也会随着移动。

格式 : direction &lt;x&gt; &lt;y&gt; &lt;z&gt;

示例 : direction 0 1 0

默认 : 1 0 0


### **emission_rate**

设置每秒要发射多少粒子。在连续发射过程中，个别发射器不是必须发射这些的 —— 这是一个相对参数，发射器可能选择每半秒就发射完所有的粒子，这主要取决于发射器。此属性也会受到粒子系统的 'quota' 设置的限制。

格式 : emission_rate &lt;particles_per_second&gt;

示例 : emission_rate 50

默认 : 10


### **position**

设置发射器相对于粒子系统所在的场景节点所处的位置。

格式 : position &lt;x&gt; &lt;y&gt; &lt;z&gt;

示例 : position 10 0 40

默认 : 0 0 0


### **velocity**

给所有粒子设置发射时的速率。也可参看 velocity_min 和 velocity_max 两个属性，它们允许你设置一个速率范围，而不是一个固定不变的值。

格式 : velocity &lt;world_units_per_second&gt;

示例 : velocity 100

默认 : 1


### **velocity_min &amp; velocity_max**

这两个属性除了是设置一个速率范围外，其它的与 'velocity' 一样。而且每一个粒子都是以在这个范围内的随机速率被发射出去的。

格式 : 同 velocity

示例 : velocity_min 50 velocity_max 100

默认 : 都是 1


### **time_to_live**

设置每个粒子在被销毁之前存活的秒数。粒子影响器是可以改变这个数值的，但是这个值是发射时才传给粒子的。参看 time_to_live_min 和 time_to_live_max 属性，这连个可以让你设置一个生命时间范围，而不是一个固定的数值。

格式 : time_to_live &lt;seconds&gt;

示例 : time_to_live 10

默认 : 5


### **time_to_live_min &amp; time_to_live_max**

这两个属性除了是设置一个生命时间范围以外，其它的与 time_to_live 一样，并且每个粒子在发射时得到这一范围内的一个随机的数值，作为其存在时间。

格式 : 同 time_to_live

示例 : time_to_live_min 2 time_to_live_max 5

默认 : 都是 5


### **duration**

设置发射器处于活动状态的秒数。发射器可以被再次打开，查看 repeat_delay。数值 0 意味着无限时。参看 duration_min 和 duration_max 属性，这两个属性可以让你设置一个时间范围，而不是一个固定值。

格式 : duration &lt;seconds&gt;

示例 : duration 2.5

默认 : 0


### **duration_min &amp; duration_max**

除了这两个属性是设置一个可变的时间范围外，其它的与 duration 一样。

格式 : 同 duration

示例 : duration_min 2 duration_max 5

默认 : 都是 0


### **repeat_delay**

设置重新开始发射需要等待的秒数。参看 repeat_delay_min 和 repeat_delay_max 属性，这两个属性允许你设置一个 repeat_delays 时间范围，而不是设置一个固定的值。

格式 : repeat_delay &lt;seconds&gt;

示例 : repeat_delay 2.5

默认 : 0


### **repeat_delay_min &amp; repeat_delay_max**

这两个属性除了是设置重新开始需要等待的时间范围外，其它的与 repeat_delay 一样，并且每次发射器被启动，它都会在这个范围内得到一个随机数值，作为重新开始发射需要的等待时间。

格式 : 同 repeat_delay

示例 : repeat_delay 2 repeat_delay 5

默认 : 都是 0


### 标准粒子发射器

Ogre 预先定义了几种粒子发射器。新的粒子发射器可以通过创建插件增加：可以查看 Plugin_ParticleFX 项目，它是教你如何创建新的粒子发射器的好例子（那里实现了这些发射器）。

* Point Emitter
* Box Emitter
* Cylinder Emitter
* Ellipsoid Emitter
* Hollow Ellipsoid Emitter
* Ring Emitter


### **Point Emitter**

这个发射器从一个定点，即它所在的位置，发射粒子。除了标准发射器属性，这个发射器没有其它属性。

要创建一个点发射器，需要在你的粒子系统脚本中包含类似下面的部分：

```
emmiter Point
{
    // Settings go here
}
```

请注意，发生器的名字（'Point'）是大小写敏感的。


### **Box Emitter**

这个发射器从一个 3 维盒子里的随机位置发射粒子。它有额外的属性：

**width**

设置盒子的宽度（这是盒子沿着它自己的 X 轴的长度，依赖于形成盒子 Z 坐标的 'direction' 属性）。

格式：width &lt;units&gt;

示例：width 250

默认：100

**height**

设置盒子的高度（这是盒子沿着它自己的 Y 轴的长度，依赖于形成盒子 Z 坐标的 'direction' 属性）。

格式：height &lt;units&gt;

示例：height 250

默认：100

**depth**

设置盒子的深度（这是盒子沿着它自己的 Z 轴的长度，与 'direction' 属性相同）

格式：depth &lt;units&gt;

示例：depth 250

默认：100

要创建一个盒发射器，需要在你的粒子系统脚本中包含类似下面的部分：

```
emitter Box
{
    // Settings go here
}
```


### **Cylinder Emitter**

这个发射器从一个沿 Z 轴摆放的圆柱体区域内的随机方向发射粒子。这个发射器有着与 Box Emitter 完全一致的参数，所以在此不多赘言 —— 宽度和高度决定圆柱体沿坐标轴的形状（如果宽度和高度不同，那么得到的结果是椭圆柱体），深度决定了圆柱体的长度。


### **Ellipsoid Emitter**

这个发射器是从一个椭圆体形状的区域里发射粒子的，例如一个球体或者压扁了的球体区域。参数再一次与 Box Emitter 相似，除了维度描述为每个坐标轴上的范围最广的点。


### **Hollow Ellipsoid Emitter**

这个发射器很像 Ellipsoid Emitter，除了椭圆体中心有一个空洞区域不发射粒子。因此，它有 3 个额外的参数定义这个空洞区域：

**inner_width**

不发射任何粒子的内部区域的宽度。

**inner_height**

不发射任何粒子的内部区域的高度。

**inner_depth**

不发射任何粒子的内部区域的深度。


### **Ring Emitter**

这个发射器从一个环状区域发射粒子。除了只有 2 个维度外，有点像 Hollow Ellipsoid Emitter。

**inner_width**

不发射任何粒子的内部区域的宽度。

**inner_height**

不发射任何粒子的内部区域的高度。

还可参看：[3.3 粒子脚本](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_3%20%E7%B2%92%E5%AD%90%E5%8F%91%E5%B0%84%E5%99%A8%E5%B1%9E%E6%80%A7%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3%20%E7%B2%92%E5%AD%90%E8%84%9A%E6%9C%AC)，[3.3.2 粒子发射器](mk:@MSITStore:C:%5C%5CProgram%20Files%5C%5Cfeiq%5C%5CAutoRecv%20Files%5C%5C%E5%BC%A0%E8%B6%85(192.168.5.70)%5C%5C2012-11-09%2010_13_00%5C%5COGRE+Manual+v1.4.0.CHM::/%E7%9B%AE%E5%BD%95/3%20%E8%84%9A%E6%9C%AC/3_3_2%20%E7%B2%92%E5%AD%90%E5%8F%91%E5%B0%84%E5%99%A8%20-%20OGRE%203D%20%E4%B8%AD%E6%96%87.htm%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.2%20%E7%B2%92%E5%AD%90%E5%8F%91%E5%B0%84%E5%99%A8)


### **Emitting Emitters**

在粒子逾期时产生新的发射器是可能的，例如产生火焰类型的效果。这是通过以下指令控制的：

**emit_emitter_quota**

这个参数是一个系统级参数，就是告诉系统任意一次可能使用多少个发射器。也就是允许进行空间分配处理。

**name**

这个参数是一个发射器级参数，即给发射器确定一个名字。这样，当粒子消亡时，其它粒子发生器可以引用这个名字作为生成的新发射器。

**emit_emitter**

这个参数是一个发射器级参数，如果指定，则意为当这个发射器发射的粒子消亡时，生成一个新的发射器。


## 粒子影响器

粒子影响器可以在粒子存续期间对粒子进行修改。它们按“类型”分为：**LinearForce**影响器，对所有粒子应用一个力；**ColourFader**影响器改变飞行中的粒子的颜色。新的影响器可以通过创建插件的形式增加到 Ogre 中来。你可以通过将影响器嵌套在另一个别的程序块里的办法，向系统中增加一个影响器，以关键字**affector**开头，后跟影响器的类型名（注意：大小写敏感）。Ogre 当前支持**LinearForce**和**ColourFader**两种影响器。

粒子影响器事实上没有统一的属性；属性都是每种影响器特有的。


### 标准粒子影响器

Ogre 预定义了几种粒子影响器。新的影响器还可以通过插件的形式增加：如何通过插件创建新的影响器，您可以参看**Plugin_ParticleFX**项目作为一个例子。（那里有这些粒子影响器的实现方式）

* Linear Force Affector
* ColourFader Affector
* ColourFader2 Affector
* Scaler Affector
* Rotator Affector
* ColourInterpolator Affector
* ColourImage Affector
* DeflectorPlane Affector
* DirectionRandomiser Affector


### **Linear Force Affector**

这个影响器对所有粒子施加一个力，改变粒子的运动轨迹。可以用于重力，风力，或者其它线性力。其额外属性有：

**force_vector**

为应用到每一个粒子的那个力设置向量。这个向量的模决定了力的大小。

格式：force_vector &lt;x&gt; &lt;y&gt; &lt;z&gt;

示例：force_vector 50 0 -50

默认：0 -100 0（一个重力效果）

**force_application**

设置这个力向量作用于粒子动量的方法。

格式：force_application &lt;add\|average&gt;

示例：force_application average

默认：add

可选参数有：

**average**

最终动量是这个力与粒子当前运动的平均值。这样也就使得其本身虽然是稳定的，但是在粒子改变方向时的速度是非线性的。

**add**

最终动量是粒子的当前运动与这个力之和。这是传统的力的叠加，但是潜在地可能导致无限速率。

要创建一个线性力影响器，需要你的粒子系统脚本中包含一段如下代码：

```
affector LinearForce
{
    // 设置写在这里
}
```

请注意：影响器类型的名字（**LinearForce**）是大小写敏感的。


### **ColourFader Affector**

此影响器修改飞行中的粒子的颜色。额外的属性有：

**red**

设置每秒时间内粒子颜色中的红色分量的调整量。

格式：red &lt;delta_value&gt;

示例：red -0.1

默认：0

**green**

设置每秒时间内粒子颜色中的绿色分量的调整量。

格式：green &lt;delta_value&gt;

示例：green -0.1

默认：0

**blue**

设置每秒时间内粒子颜色中的蓝色分量的调整量。

格式：blue &lt;delta_value&gt;

示例：blue -0.1

默认：0

**alpha**

设置每秒时间内粒子颜色中的 alpha 分量的调整量。

格式：alpha &lt;delta_value&gt;

示例：alpha -0.1

默认：0

要创建一个颜色减弱影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector ColourFader
{
    // 设置写在这里
}
```


### **ColourFader2 Affector**

此影响器类似**ColourFader Affector**，只不过这个影响器有两个颜色改变状态。在粒子存续期内，指定还剩一段时间时，激活第二个颜色改变状态。

**red1**

设置在第一个状态期间每秒时间内粒子颜色的红色分量的调整量。

格式：red &lt;delta_value&gt;

示例：red -0.1

默认：0

**green1**

设置在第一个状态期间每秒时间内粒子颜色的绿色分量的调整量。

格式：green &lt;delta_value&gt;

示例：green -0.1

默认：0

**blue1**

设置在第一个状态期间每秒时间内粒子颜色的蓝色分量的调整量。

格式：blue &lt;delta_value&gt;

示例：blue -0.1

默认：0

**alpha1**

设置在第一个状态期间每秒时间内粒子颜色的 alpha 分量的调整量。

格式：alpha &lt;delta_value&gt;

示例：alpha -0.1

默认：0

**red2**

设置在第二个状态期间每秒时间内粒子颜色的红色分量的调整量。

格式：red &lt;delta_value&gt;

示例：red -0.1

默认：0

**green2**

设置在第二个状态期间每秒时间内粒子颜色的绿色分量的调整量。

格式：green &lt;delta_value&gt;

示例：green -0.1

默认：0

**blue2**

设置在第二个状态期间每秒时间内粒子颜色的蓝色分量的调整量。

格式：blue &lt;delta_value&gt;

示例：blue -0.1

默认：0

**alpha2**

设置在第二个状态期间每秒时间内粒子颜色的 alpha 分量的调整量。

格式：alpha &lt;delta_value&gt;

示例：alpha -0.1

默认：0

**state_change**

当一个粒子还有这么多存续时间时，它将转入状态二。

格式：state_change &lt;seconds&gt;

示例：state_change 2

默认：1

要创建一个颜色减弱 2 影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector ColourFader2
{
    // 设置写在这里
}
```


### **Scaler Affector**

此影响器调节飞行中的粒子的大小。额外的属性有：

**rate**

每秒时间内在 x 和 y 方向上对粒子的调节量。

要创建一个伸缩影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector Scaler
{
    // 设置写在这里
}
```


### **Rotator Affector**

此影响器依靠旋转粒子的贴图纹理来旋转飞行中的粒子。额外的属性有：

**rotation_speed_range_start**

赋值给发射出去的粒子的旋转速度范围的初始值。

格式：rotation_speed_range_start &lt;degrees_per_second&gt;

示例：rotation_speed_range_start 90

默认：0

**rotation_speed_range_end**

赋值给发射出去的粒子的旋转速度范围的结束值。

格式：rotation_speed_range_end &lt;degrees_per_second&gt;

示例：rotation_speed_range_end 180

默认：0

**rotation_range_start**

赋值给发射出去的粒子的旋转角度的初始值。

格式：rotation_range_start &lt;degrees&gt;

示例：rotation_range_start 0

默认：0

**rotation_range_end**

赋值给发射出去的粒子的旋转角度的结束值。

格式：rotation_range_end &lt;degrees&gt;

示例：rotation_range_end 360

默认：0

要创建一个旋转影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector Rotator
{
    // 设置写在这里
}
```


### **ColourInterpolator Affector**

类似于 ColourFader 和 ColourFader2，此影响器也是修改飞行中的粒子的颜色。只不过这个影响器有一组不定个数的已经定义好的状态。它在粒子存续期内在几种状态间插值变换粒子的颜色。额外的属性有：

**time0**

状态 0 的时间点。

格式：time0 &lt;0 到 1，基于粒子的存续时间 &gt;

示例：time0 0

默认：1

**colour0**

状态 0 时的颜色。

格式：colour0 &lt;r g b&gt; [&lt;a&gt;]

示例：colour0 1 0 0 1

默认：0.5 0.5 0.5 0.0

**time1**

状态 1 的时间点。

格式：time1 &lt;0 到 1，基于粒子的存续时间 &gt;

示例：time1 0.5

默认：1

**colour1**

状态 1 时的颜色。

格式：colour1 &lt;r g b&gt; [&lt;a&gt;]

示例：colour1 0 1 0 1

默认：0.5 0.5 0.5 0.0

**time2**

状态 2 的时间点。

格式：time2 &lt;0 到 1，基于粒子的存续时间 &gt;

示例：time2 1

默认：1

**colour2**

状态 2 时的颜色。

格式：colour2 &lt;r g b&gt; [&lt;a&gt;]

示例：colour2 0 0 1 1

默认：0.5 0.5 0.5 0.0

**[...]**

状态数是可变的。最多 6 个。即 time5 和 colour5 是最后的参数。要想创建一个颜色插值影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector ColourInterpolator
{
    // 设置写在这里
}
```


### **ColourImage Affector**

这是另一个改变飞行粒子的颜色的影响器，但替代编程定义颜色的是，从一个指定的图像文件中取得颜色。在粒子的存续时间内，颜色的取值范围是从图像的左侧开始向右移动，因此，只使用了水平方向的图像。额外属性有：

**image**

赋值给发射出去的粒子的旋转速度范围的初始值。

格式：image &lt;image_name&gt;

示例：image rainbow.png

默认：无

要创建一个图像颜色影响器，需要在你的粒子系统脚本中包含如下一段代码：

```
affector ColourImage
{
    // 设置写在这里
}
```


### **DeflectorPlane Affector**

此影响器定义一个平面，这个平面反弹碰到它的粒子。额外的属性有：

**plane_point**

反弹平面上一点。与 plane_normal 一起使用。

默认：plane_point 0 0 0

**plane_normal**

反弹平面的法线向量。与 plane_point 一起使用。

默认：plane_normal 0 1 0

**bounce**

当一个粒子被反弹时的弹力大小。0 表示没有反弹，1 表示 100% 反弹。

默认：bounce 1.0


### **DirectionRandomiser Affector**

此影响器随机选定粒子运动的方向。额外属性有：

**randomness**

每一轴向上随机性的大小。

示例：randomness 5

默认：randomness 1

**scope**

每一轮受影响的粒子的百分比。

示例：scope 0.5

默认：scope 1.0

**keep_velocity**

决定是否不改变粒子的速率。

示例：keep_velocity true // 不改变粒子速率

默认：keep_velocity false // 即改变粒子速率


## 字体定义脚本

Ogre 使用基于纹理的字体渲染 TextAreaOverlayElement。你也可以使用 Font 对象去实现你想要的目标。字体的最终格式是一个由字体生成的 Material 对象，以及一组 "glyph"（字符轮廓）纹理坐标信息。

在 OGRE 中，你可以用两种方法得到字体 :

1、利用一个艺术包或者字体生成工具自己设计一个字体纹理

2、让 OGRE 生成一个基于 truetype 字体的字体纹理

前一种方法给你最大的自由度，以及最棒的性能表现效果（从启动时间上看），但是，如果你想快速使用一个字体，而不愿自己生成纹理的话，后一种方法是更为方便的。建议使用后一种方法进行原形设计，而到了最后要完成最终一步时，在转成前一种方法。

所有字体定义被保存在 .fontdef 文件中，这些文件在开始启动时，由系统进行分析。每一个 .fontdef 文件可以包含多个字体定义。在 .fontdef 文件中的一个入口的基本格式是：

```
<font_name>
{
    type <image | truetype>
    source <image file | truetype font file>
    ...
    ... custom attributes depending on type
}
```


## 使用一个现有字体纹理

如果有一个或多个艺术家与你一起工作，不要怀疑，他们可以为你制造出一个非常漂亮的字体纹理。OGRE 支持全部色彩的字体纹理，或者保持黑白单色 / 灰阶以及使用 TextArea 的色彩特性。字体纹理总有一个 alpha 通道，最好是一个 8 位的 alpha 通道，就像 TGA 和 PNG 文件支持的那样，因为它可以得到更为漂亮的边界。要使用一个现有的纹理，你需要进行如下设置：

**type image**

这只是告诉 OGRE，你想要一个预先画好的字体。

**source &lt;filename&gt;**

这是那个你想要调用的图片文件的名字。它会从标准 TextureManager 资源位置被装入，而且是任意 OGRE 支持的类型，尽管不推荐 JPEG 格式，因为缺少 alpha 而且是有损压缩。推荐 PNG 格式，它具备无损压缩和一个 8 位 alpha 通道的双重优点。

**glyph &lt;character&gt; &lt;u1&gt; &lt;v1&gt; &lt;u2&gt; &lt;v2&gt;**

这个是为指定的字提供纹理坐标。你必须为纹理中所有的每一个字，重复这一步骤。前两个数字是左上角的 x 和 y 坐标，后两个是右下角的 x 和 y 坐标。注意，你一定要使用等高的字，因为等比例字体，宽度可以有所不同。

一条给 Windows 用户的提示：建议使用（[http://www.lmnopc.com/bitmapfontbuilder/](http://www.lmnopc.com/bitmapfontbuilder/)），一个自由工具，可以用来生成纹理并且为你导出字符宽度，你可以在 Tools 文件夹下找到一个工具，将这个二进制的输出文件转换成 'glyph' 线条。


## 生成一个字体纹理

你也可以利用 truetype 字体生成一个字体纹理。不建议在成品中过多使用这个，因为每个字体渲染纹理都要花费几秒钟时间，增大载入时间。然而，不管怎样，它是一个非常好的快速得到你选择的字体的输出文本的方法。

下面是你需要提供的一些属性：

**type truetype**

告诉 OGRE 从一个字体里生成纹理。

**source &lt;ttf file&gt;**

要载入的 ttf 文件名。它将在普通资源位置和任何增加到 FontManager 中的资源位置搜索。

**size &lt;size_in_points&gt;**

按标准点计算要生成字体的大小。注意，这只影响字符在字体纹理中是多大，不影响在屏幕上显示的大小。你应当根据你期望渲染多大的字体来裁减这个的大小，因为生成一个庞大的纹理将导致字符在缩得很小的时候变得模糊（由于 mipmapping），而且相反地，生成一个小字体会导致渲染大号文本时产生块状字。

**resolution &lt;dpi&gt;**

按每英寸中的点数计算的清晰度，与上面的 point size 关联使用以决定最终大小。一般是 72 / 96 dpi。

**antialias_colour &lt;true\|false&gt;**

这是一个可选项，默认是“false”。生成器会默认使用纹理的 alpha 分量对字体抗锯齿，如果你使用 alpha 混合渲染你的文本会看起来很好。无论你想在自己的代码中使用哪个基于混合的颜色，如：add 或 modulate，你都要设置这个选项为“true”，因此颜色值也是抗锯齿的。如果你设置这个为真，并且使用 alpha 混合，你会发现你的字体的边也是抗锯齿的，快速得到一个看上去很“细”的字体，因为不仅是 alpha 混合了边界，颜色也变淡了。如果有所怀疑，让这个选项保持默认“false”，也没关系。

**code_points nn-nn [nn-nn] ..**

这一指令允许你指定哪一个 unicode 编码点应当作为字符轮廓被生成为字体纹理。如果你不指定，编码点 33-166 将会默认被生成，覆盖基本的 Latin 1 字符轮廓。如果你使用了这个标记，你应当指定一个包含编码点范围的独立空间列表，格式为“开始位置-结束位置”。数值必须是十进制数。

你也可以在运行时使用 FontManager 创建新字体。


## **示例：**

使用了一个在第二次渲染通路中包含 10 次迭代操作用以生成皮毛的简单的皮毛渲染材质脚本

```
// GLSL simple Fur
vertex_program GLSLDemo/FurVS glsl
{
    source fur.vert
    default_params
    {
        param_named_auto lightPosition light_position_object_space 0
        param_named_auto eyePosition camera_position_object_space
        param_named_auto passNumber pass_number
        param_named_auto multiPassNumber pass_iteration_number
        param_named furLength float 0.15
    }
}

fragment_program GLSLDemo/FurFS glsl
{
    source fur.frag
    default_params
    {
        param_named Ka float 0.2
        param_named Kd float 0.5
        param_named Ks float 0.0
        param_named furTU int 0
    }
}

material Fur
{
    technique GLSL
    {
        pass base_coat
        {
            ambient 0.7 0.7 0.7
            diffuse 0.5 0.8 0.5
            specular 1.0 1.0 1.0 1.5

            vertex_program_ref GLSLDemo/FurVS
            {
            }

            fragment_program_ref GLSLDemo/FurFS
            {
            }

            texture_unit
            {
                texture Fur.tga
                tex_coord_set 0
                filtering trilinear
            }
        }

        pass grow_fur
        {
            ambient 0.7 0.7 0.7
            diffuse 0.8 1.0 0.8
            specular 1.0 1.0 1.0 64
            depth_write off
            scene_blend src_alpha one
            iteration 10

            vertex_program_ref GLSLDemo/FurVS
            {
            }

            fragment_program_ref GLSLDemo/FurFS
            {
            }

            texture_unit
            {
                texture Fur.tga
                tex_coord_set 0
                filtering trilinear
            }
        }
    }
}
```

注意：使用 GPU 程序自动参数 pass_number 和 pass_iteration_number 告诉顶点或片断程序渲染通路数量和迭代数。


## References

- [1] [Ogre3D 脚本系统关键字说明 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/74046682)
- [2] [Html 转换为 MarkDown 工具](https://www.bejson.com/convert/html2markdown/)
- [3] [3.3 粒子 Particle {% include relref_cnblogs.html %}](https://www.cnblogs.com/wiki3d/p/4658247.html)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-08-ogre-particlesystem.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://ogre3d.cn/wiki/index.php?title=%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1_%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7%22%20%5Cl%20%22billboard_type%22%20%5Co%20%22%E6%96%87%E6%A1%A3:%E6%89%8B%E5%86%8C:1-4-0:3.3.1%20%E7%B2%92%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%B1%9E%E6%80%A7]({% include relrefx.html url="/backup/2020-11-08-ogre-particlesystem.md/ogre3d.cn/e5405f6b.php" %})
- [http://www.lmnopc.com/bitmapfontbuilder/]({% include relrefx.html url="/backup/2020-11-08-ogre-particlesystem.md/www.lmnopc.com/724c7cfb.html" %})
- [https://zhuanlan.zhihu.com/p/74046682]({% include relrefx.html url="/backup/2020-11-08-ogre-particlesystem.md/zhuanlan.zhihu.com/2e9faf96.html" %})
- [https://www.bejson.com/convert/html2markdown/]({% include relrefx.html url="/backup/2020-11-08-ogre-particlesystem.md/www.bejson.com/0f492a91.html" %})
- [https://www.cnblogs.com/wiki3d/p/4658247.html]({% include relrefx.html url="/backup/2020-11-08-ogre-particlesystem.md/www.cnblogs.com/e4fb1631.html" %})
