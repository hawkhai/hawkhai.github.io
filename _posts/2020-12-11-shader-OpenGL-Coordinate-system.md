---
layout: post
title: "特效编程笔记 -- OpenGL 图形学 / 坐标系统"
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
cluster: "LearnOpenGL"
---

> OpenGL 坐标系统。开创者没用整数，就用 -1 到 1 的浮点数，装下了整个数学，也装下了整个 UNIVERSE，可以无穷大，也可以无穷小。

- <https://learnopengl-cn.readthedocs.io/zh/latest/01%20Getting%20started/08%20Coordinate%20Systems/>
- <https://www.mdeditor.tw/pl/pZYE>
- <https://mp.weixin.qq.com/s/0HZgyZra90LQLFAq6dQJ9A>


## 理论

主要有 5 个不同的坐标系统：

- 局部空间 (Local Space，或者称为物体空间 (Object Space))
- 世界空间 (World Space)
- 观察空间 (View Space，或者称为视觉空间 (Eye Space))
- 裁剪空间 (Clip Space)
- 屏幕空间 (Screen Space)

$$
V_{clip} = M_{projection} \cdot M_{view} \cdot M_{model} \cdot V_{local}
$$

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/coordinate_systems2.png" %}

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/173184e0cdd334b3.jpg" %}

在上图中，OpenGL 定义了后三个坐标系（裁剪坐标、NDC 坐标、屏幕坐标），前三个坐标（物体坐标、世界坐标、摄像机坐标）是为了用户方便而自定义的坐标。

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/173184b55b0849f7.jpg" %}

$$
\left[\begin{array}{l}
x^{\prime} \\
y^{\prime} \\
z^{\prime} \\
1
\end{array}\right]
=
\left[\begin{array}{llll}
1 & 0 & 0 & \Delta x \\
0 & 1 & 0 & \Delta y \\
0 & 0 & 1 & \Delta z \\
0 & 0 & 0 & 1
\end{array}\right]
\left[\begin{array}{l}
x \\
y \\
z \\
1
\end{array}\right]
=
\left[\begin{array}{c}
x+\Delta x \\
y+\Delta y \\
z+\Delta z \\
1
\end{array}\right]
$$

OpenGL 在每次顶点着色器运行之后，希望可见的顶点都可以转化为标准化设备坐标 (Normalized Device Coordinate, NDC)，也就是说，每个顶点的 x，y，z 坐标都应该在（-1.0，1.0）之间，超出这个坐标范围的顶点都将不可见。通常我们会自定一个坐标的范围，之后再在顶点着色器中将这些坐标转换为标准化设备坐标。然后将这些标准化的坐标传入光栅器，变换为屏幕上的二维坐标或者像素。

物体坐标到世界坐标，主要是位移；世界坐标到视觉坐标，主要包含位移和旋转。最终要换算到 NDC 立方体内，显卡完成后继工作。
glm::mat4 内存结构是列保存的（**刚好是上面数学矩阵的转置**）：

```
// 列优先记法
| 0 4  8 12 |
| 1 5  9 13 |
| 2 6 10 14 |
| 3 7 11 15 |
```

* [OpenGL Projection Matrix](http://www.songho.ca/opengl/gl_projectionmatrix.html)
* [OpenGL Sphere](http://www.songho.ca/opengl/gl_sphere.html)


## 示例

原始坐标：

```cpp
float vertices[] = {
    -0.5f,-0.5f,0.0f, // left,down
     0.5f,-0.5f,0.0f, // right,down
     0.5f, 0.5f,0.0f, // right,top
    -0.5f, 0.5f,0.0f, // left,top
};
```

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/20201210173525.png" %}

```cpp
glm::mat4 model=glm::mat4(1.0f);
// 默认应该是正交投影，饶 x 轴逆时针旋转 55°
model=glm::rotate(model,glm::radians(55.0f),glm::vec3(1.0f,0.0f,0.0f));
```

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/20201210173853.png" %}

```cpp
glm::mat4 view = glm::mat4(1.0f);
// 往上平移 0.5f，往后平移 1.0f。
// 只能看到半截，因为默认是一个 [-1,1] 的立方体正交，另外半截超出边界了。
view=glm::translate(view,glm::vec3(0.0f,0.5f,-1.0f));
```

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/20201210174245.png" %}

```cpp
glm::mat4 projection = glm::mat4(1.0f);
// 最终结果，是一个摄像机在原点的透视。
// 摄像机位置应该在 原点。
projection=glm::perspective(glm::radians(90.0f),800.0f/600.0f,0.1f,10.0f);
```

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/20201210174453.png" %}


## 相机控制

右手坐标系。Z 轴正方向为前进方向。

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/20190827164053851.png" %}

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/pitch.gif" caption="pitch()：俯仰，将物体绕 X 轴旋转（localRotationX）" %}

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/yaw.gif" caption="yaw()：航向，将物体绕 Y 轴旋转（localRotationY）" %}

{% include image.html url="/assets/images/201211-shader-opengl-coordinat~fa/roll.gif" caption="roll()：横滚，将物体绕 Z 轴旋转（localRotationZ）" %}


## 四元数概念及其应用

[四元数概念及其应用](http://www.cppblog.com/kongque/archive/2010/08/18/123824.html)


### 什么是四元数

$i$，$j$，$k$ 为虚数。

$Q = w + xi + yj + zk$

其中 $w$ 是实数，而 $x$，$y$，$z$ 为复数。

另外一种常见的表达方式是：

$Q = [w, v]$

其中 $v=(x,y,z)$ 称为矢量部（虽然称为矢量，但是这个不是三维空间中的矢量，而是四维空间的，想象吧 L），$w$ 称为标量部。
使用一个单位四元数来描述方向，请记住必须是单位四元数才可以描述方向。


### 使用四元数来避免 Gimbal Lock

基本思路如下：

1. 使用一个四元数来标识一个方向。
2. 创建一个临时的四元数来标识当前方向到新方向的变化。
3. 右乘临时的四元数和初始四元数，结果是一个合并了两个四元数的新的四元数。
4. 将四元数转换成矩阵。


### Shader 四元数旋转

[Shader 四元数旋转 {% include relref_github.html %}](https://chengkehan.github.io/QuaternionShader.html)

```glsl
#define Quaternion float4

inline Quaternion SetAxisAngle(float3 axis, float radian)
{
    float sinValue = 0;
    float cosValue = 0;
    sincos(radian * 0.5, sinValue, cosValue);
    Quaternion q = Quaternion(sinValue * axis.xyz, cosValue);
    return q;
}

inline float3 MultiplyQP(Quaternion rotation, float3 p)
{
    float3 xyz = rotation.xyz * 2;
    float3 xx_yy_zz = rotation.xyz * xyz.xyz;
    float3 xy_xz_yz = rotation.xxy * xyz.yzz;
    float3 wx_wy_wz = rotation.www * xyz.xyz;

    float3 res;
    res.x = (1 - (xx_yy_zz.y + xx_yy_zz.z)) * p.x + (xy_xz_yz.x - wx_wy_wz.z) * p.y + (xy_xz_yz.y + wx_wy_wz.y) * p.z;
    res.y = (xy_xz_yz.x + wx_wy_wz.z) * p.x + (1 - (xx_yy_zz.x + xx_yy_zz.z)) * p.y + (xy_xz_yz.z - wx_wy_wz.x) * p.z;
    res.z = (xy_xz_yz.y - wx_wy_wz.y) * p.x + (xy_xz_yz.z + wx_wy_wz.x) * p.y + (1 - (xx_yy_zz.x + xx_yy_zz.y)) * p.z;
    return res;
}
```

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://learnopengl-cn.readthedocs.io/zh/latest/01%20Getting%20started/08%20Coordinate%20Systems/]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/learnopengl-cn.readthedocs.io/cfc9cf0a.html" %})
- [https://www.mdeditor.tw/pl/pZYE]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/www.mdeditor.tw/c5442ada.html" %})
- [https://mp.weixin.qq.com/s/0HZgyZra90LQLFAq6dQJ9A]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/mp.weixin.qq.com/25763337.html" %})
- [http://www.songho.ca/opengl/gl_projectionmatrix.html]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/www.songho.ca/7c7467ff.html" %})
- [http://www.songho.ca/opengl/gl_sphere.html]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/www.songho.ca/ca4b2763.html" %})
- [http://www.cppblog.com/kongque/archive/2010/08/18/123824.html]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/www.cppblog.com/e2810916.html" %})
- [https://chengkehan.github.io/QuaternionShader.html]({% include relref.html url="/backup/2020-12-11-shader-OpenGL-Coordinate-system.md/chengkehan.github.io/e4504ae9.html" %})
