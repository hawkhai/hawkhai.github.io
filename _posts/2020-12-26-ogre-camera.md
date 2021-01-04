---
layout: post
title: "Ogre3D 笔记 -- Ogre3D 摄像机方向总结"
author:
location: "珠海"
categories: ["Ogre3D"]
tags: ["Ogre3D"]
toc: true
toclistyle:
comments:
visibility: hiddenz
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---

OGRE 成功的作品，主要是 天龙八部 和 火炬之光。

以前看代码，老是看不太懂，最近补充了一下基础理论。
摄像机方向控制三个方法：四元数、姿态角（Euler 角）、摄像矩阵（ViewMatrix），不同 3D 引擎 大同小异。


## 透视投影和正交投影

摄像机默认是近大远小的椎体视角，小地图使用的是类似平行光的视角，需要：

```cpp
cam->setProjectionType(Ogre::PT_ORTHOGRAPHIC);
```


## setDirection

`setDirection` 不支持以 `Ogre::Vector3::UNIT_Y` 为参数。
原因：比如 `setDirection` 为向纸面内看物体 A，此时 Ogre 的显示为 A，而不是倒立的 A，这是因为 `Ogre::Vector3::UNIT_Y` 是 Ogre 默认的 'UP' 视角。
所以 `setDirection(Ogre::Vector3::UNIT_Y)` 会出错，需要先设定向上的坐标轴：

```cpp
cam->setFixedYawAxis(true, gre::Vector3::NEGATIVE_UNIT_Z);
cam->setDirection(0.0f, -1.0f, 0.0f);
```


## 姿态角（Euler 角）

改变方向也可以通过 Yaw Roll Pitch 来实现。
注意以此旋转依旧要设：`cam->setFixedYawAxis(true, Ogre::Vector3::NEGATIVE_UNIT_Z);`

* Yaw 是围绕当前坐标系的 Y 轴旋转。
* Roll 是围绕当前坐标系的 X 轴旋转。
* Pitch 是围绕当前坐标系的 Z 轴旋转。

```cpp
// 2 的代码写的麻烦一点就是：
cam->setFixedYawAxis(true, Ogre::Vector3::NEGATIVE_UNIT_Z);
cam->setDirection(1.0f, 0.0f, 0.0f);
cam->yaw(Ogre::Degree(90));
// 改变了 UP 之后，当前坐标系也不清晰了，也可以这样写
cam->setFixedYawAxis(true, Ogre::Vector3::NEGATIVE_UNIT_Z);
cam->setDirection(1.0f, 0.0f, 0.0f);
cam->rotate(Ogre::Vector3(0.0f, 0.0f, 1.0f), Ogre::Degree(-90));
// 也可以利用四元数旋转
cam->setFixedYawAxis(true, Ogre::Vector3::NEGATIVE_UNIT_Z);
cam->setDirection(1.0f, 0.0f, 0.0f);
cam->rotate(Ogre::Quaternion(Ogre::Degree(-90), Ogre::Vector3(0.0f, 0.0f, 1.0f)));
```


## 矩阵的方法

矩阵的方法，不再需要设置 'UP' 的方向。

```
世界矩阵 => 摄像矩阵 (ViewMatrix) => 投影矩阵 (ProjectionMatrix)
```

旋转是在 ViewMatrix 中的处理，我需要的矩阵只是 Y 轴和 Z 轴做了对换，所以：

```cpp
1 0  0 0
0 0 -1 0
0 1  0 -1000 // -1000 是摄像机的位置
0 0  0 1
```

```cpp
Ogre::Matrix4 mx = Ogre::Matrix4::IDENTITY;
mx[1][1] = 0.0f;
mx[1][2] = -1.0f;
mx[2][1] = 1.0f;
mx[2][2] = 0.0f;
mx[2][3] = -1000.f;
cam->setCustomViewMatrix(true, mx);
```


## 四元数的方法

四元数的方法，不再需要设置 'UP' 的方向。
从 3 中的最后一个方法可以知道，四元数就是绕一个向量，旋转一定的角度。
事实上我的变化，一直是在受 `setFixedYawAxis` 干扰，实际只是原始坐标轴 X 旋转了 90 度。

```cpp
cam->setOrientation(Ogre::Quaternion(Ogre::Degree(-90), Ogre::Vector3(1.0f, 0.0f, 0.0f)));
```

注 1：四元数的 w, x, y, z 分别等于：

```cpp
float w = cos(angle / 2);
float x = axis.x * sin(angle / 2);
float y = axis.y * sin(angle / 2);
float z = axis.z * sin(angle / 2);
```

注 2：现在还不清楚四元数用于旋转时具体的计算方法，也没必要知道。
不过要记住四元数的 w 是不能为 0 的，也就是说不能旋转 180。
可以用下面代码回避：

```cpp
if (1.0f + src.dotProduct(dir) < 0.0001f) {
    // 点乘 =-1.0，那么就是方向相反了
    src->yaw(Ogre::Degree(180));
} else {
    Ogre::Quaternion quat = src.getRotationTo(dir);
    src.rotate(quat);
}
```


## Refs

- [1] [OpenGL 坐标系统](https://learnopengl-cn.readthedocs.io/zh/latest/01%20Getting%20started/08%20Coordinate%20Systems/)
- [2] [Reiiden 制作笔记 D（OGRE 摄像机方向总结） {% include relref_csdn.html %}](https://blog.csdn.net/kira8dao7/article/details/6309671)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [https://learnopengl-cn.readthedocs.io/zh/latest/01%20Getting%20started/08%20Coordinate%20Systems/]({% include relref.html url="/backup/2020-12-26-ogre-camera.md/learnopengl-cn.readthedocs.io/cfc9cf0a.html" %})
- [https://blog.csdn.net/kira8dao7/article/details/6309671]({% include relref.html url="/backup/2020-12-26-ogre-camera.md/blog.csdn.net/7e7e982c.html" %})
