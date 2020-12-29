---
layout: post
title: "特效编程笔记 -- 用 Bullet Physics 和 OpenGL 实现的 抛箱子"
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

A simple box shooter using Bullet Physics and OpenGL.

Bullet Physics 是一个开源的物理模拟引擎，世界三大物理引擎之一（另外两种是 Havok 和 PhysX）。
Bullet 是一个跨平台的开源物理引擎，支持三维碰撞检测、柔体动力学和刚体动力学，多用于游戏开发和电影制作中。Bullet 物理库在 zlib 协议下发布。
Right-handed coordinate system in bullet，和 OpenGL 一致。一个人写的，歪果人就是牛。
Bullet 的主要作者为 Erwin Coumans，曾经就职于索尼电脑娱乐美国研发职务 2003 到 2010 年，就职于 AMD 公司到 2014 年，现就职于 Google 公司。


## Box Shooter

A simple game that one can throw box to a pile of boxes to drop some of them. The implementation is using using *OpenGL* and *Bullet Physics*.

实验效果：

{% include image.html url="/assets/images/201229-shader-box-shooter/boxshooter.webp" %}


## Installing Box Shooter

To install Box Shooter, follow these steps:

```shell
mkdir build && cd build
cmake .. # Using CMake
make # make all
```


## BulletPhysics 基本概念


### 创建并初始化物理世界

```cpp
// 设置世界的空间大小，限定刚体运动的空间范围
btVector3 worldAabbMin(-10000, -10000, -10000);
btVector3 worldAabbMax(10000, 10000, 10000);

// 设置最大刚体数
int maxProxies = 1024;
// 利用以上配置创建粗测阶段所需参数
btAxisSweep3* broadphase = new btAxisSweep3(worldAabbMin, worldAabbMax, maxProxies);

// 创建好碰撞配置
// 例如一些多人射击游戏中，队友之间不会发生碰撞，但是和其他物体都能发生碰撞
btDefaultCollisionConfiguration* collisionConfiguration = new btDefaultCollisionConfiguration();
btCollisionDispatcher* dispatcher = new btCollisionDispatcher(collisionConfiguration);

// 创建求解器
btSequentialImpulseConstraintSolver* solver = new btSequentialImpulseConstraintSolver();

// 使用以上创建的设置来创建物理世界
btDiscreteDynamicsWorld* dynamicsWorld = new btDiscreteDynamicsWorld(dispatcher, broadphase, solver, collisionConfiguration);
// 设置物理世界重力（这里在 y 轴上的重力设为 10N/kg）
dynamicsWorld->setGravity(btVector3(0, -10, 0));
```

释放代码：

```cpp
#define SAFE_DELETE_PTR(ptr) do{if(ptr){delete ptr;ptr = nullptr;}}while(0);

PhysicsWorld::~PhysicsWorld() {
    // 必须先 delete DynamicWorld
    SAFE_DELETE_PTR(mDynamicsWorld);
    // 再 delete 其他相关资源
    SAFE_DELETE_PTR(mBroadphase);
    SAFE_DELETE_PTR(mCollisionConfiguration);
    SAFE_DELETE_PTR(mDispatcher);
    SAFE_DELETE_PTR(mSolver);
}
```


### 刚体

包含形状，摩擦系数，阻尼系数，弹性系数等属性。

地面一般是固定不变的，所以它是静态刚体，我们设置 mass 时要设置为 0。地面是平面形状的，所以形状要设置成 btStaticPlaneShape（即静态平面形状）。
（密度为 0 时会被 Bullet 认为是静态刚体，非 0 时则认为是动态刚体）

创建一个平面状的静态刚体（作为地面）的代码：

```cpp
// 创建 物体的初始位置旋转角度信息：旋转角度 0，位置在 Y 轴 -1 距离
btDefaultMotionState* groundMotionState = new btDefaultMotionState(btTransform(btQuaternion(0, 0, 0, 1), btVector3(0, -1, 0)));

// 创建 静态平面形状
btCollisionShape* groundShape = new btStaticPlaneShape(btVector3(0, 1, 0), 1);
// 生成设置信息
btRigidBody::btRigidBodyConstructionInfo groundRigidBodyCI(0, groundMotionState, groundShape, btVector3(0, 0, 0));
// 根据设置信息 创建刚体
btRigidBody* groundbody = new btRigidBody(groundRigidBodyCI);
// 设置摩擦系数 0.5
groundbody->setFriction(0.5f);
// 将地面刚体添加到 物理世界
dynamicWorld->addRigidBody(groundbody);
```

创建一个球状的动态刚体的代码：

```cpp
// 创建 物体的初始位置旋转角度信息：旋转角度 0，位置在 Y 轴 10 距离的高空
btDefaultMotionState* ballMotionState = new btDefaultMotionState(btTransform(btQuaternion(0, 0, 0, 1), btVector3(0, 10, 0)));

// 创建 半径 0.5 的球体形状
btCollisionShape* ballShape = new btSphereShape(0.5);

// 设置密度（特殊地，密度为 0 时会被认为静态刚体，非 0 时则作为动态刚体）
int mass = 10;

// 惯性
btVector3 inertia;
// 根据密度自动计算并设置惯性
ballShape->calculateLocalInertia(mass, inertia);

// 生成设置信息
btRigidBody::btRigidBodyConstructionInfo groundRigidBodyCI(mass, ballMotionState, ballShape, inertia);

// 根据设置信息 创建刚体
btRigidBody* ballBody = new btRigidBody(groundRigidBodyCI);
// 设置摩擦系数 0.5
ballBody->setFriction(0.5f);
// 将该刚体添加到物理世界里
dynamicsWorld->addRigidBody(ballBody);
```


### 开始模拟

物理引擎的位置角度信息和渲染逻辑的位置角度信息是分别独立的，物理模拟后须将物理引擎的位置角度信息赋给渲染逻辑的位置角度信息。

```cpp
void updateScene(float deltaTime) {
    // 主循环函数的其它内容（一般是逻辑处理）
    // balabala.....

    // 物理世界模拟
    // 通过 10 次子步骤求解，模拟出 deltaTime 后的物理世界变化。
    dynamicsWorld->stepSimulation(deltaTime, 10);

    // 更新物理世界每一个物体
    auto & objectArray = dynamicsWorld->getCollisionObjectArray();
    for (int i = 0; i < objectArray.size(); ++i)
    {
        // 处于不活动状态或者是静态刚体的话，则不处理
        if (!objectArray[i]->isActive() || objectArray[i]->isStaticObject()) continue;
        Transform* object = reinterpret_cast<Transform*>(objectArray[i]->getUserPointer());
        // 没有用户指针的话，则不处理
        if (!object)continue;

        // 更新目标物体的位置
        const auto & pos = objectArray[i]->getWorldTransform().getOrigin();
        object->setPosition(pos.x(), pos.y(), pos.z());
        // 更新目标物体的旋转角度
        const auto & rotationM = objectArray[i]->getWorldTransform().getRotation();
        object->setRotation(rotationM.getX(), rotationM.getY(), rotationM.getZ(), rotationM.getW());
    }
    // 主循环函数的其他内容（一般是渲染）
    // bala......
}
```


### 删除刚体

```cpp
for (int i = 0; i < objectArray.size(); ++i)
{
    // 清除待删除物理刚体
    int entityState = reinterpret_cast<int>(objectArray[i]->getUserPointer());
    // 本文将待删除物理刚体的用户指针指向 Entity::NoEntity（-1 值）作为待删除标记，也可用其它来作为标记
    if (entityState == Entity::NoEntity) {
        m_dynamicsWorld->removeCollisionObject(objectArray[i]);
        --i; // 删除后要退回一位
        continue;
    }

    ... // 其它代码
}
```


## 相机控制

右手正交。移除 roll。Z 轴正方向为前进方向。

{% include image.html url="/assets/images/201229-shader-box-shooter/20190827164053851.png" %}

{% include image.html url="/assets/images/201229-shader-box-shooter/pitch.gif" caption="pitch()：俯仰，将物体绕 X 轴旋转（localRotationX）" %}

{% include image.html url="/assets/images/201229-shader-box-shooter/yaw.gif" caption="yaw()：航向，将物体绕 Y 轴旋转（localRotationY）" %}

{% include image.html url="/assets/images/201229-shader-box-shooter/roll.gif" caption="roll()：横滚，将物体绕 Z 轴旋转（localRotationZ）" %}

```cpp
void Camera::update()
{
    front.x = cos(glm::radians(yaw)) * cos(glm::radians(pitch));
    front.y = sin(glm::radians(pitch));
    front.z = cos(glm::radians(pitch)) * sin(glm::radians(yaw));
    front = glm::normalize(front);
    right = glm::normalize(glm::cross(front, worldUp));
    up = glm::normalize(glm::cross(right, front));
}

glm::mat4 Camera::calculateViewMatrix()
{
    return glm::lookAt(position, position + front, up);
}

// GLFW_KEY_W
// GLFW_KEY_S
// GLFW_KEY_A
// GLFW_KEY_D
```


## Refs

- [1] [C++ 3D 物理引擎库 BulletPhysics 基本使用 {% include relref_cnblogs.html %}](https://www.cnblogs.com/KillerAery/archive/2004/01/13/9223947.html)
- [2] [【Bullet 引擎】复杂碰撞体 —— btCompoundShape {% include relref_csdn.html %}](https://blog.csdn.net/azri81226/article/details/101691134)
- [3] [【Bullet 引擎】复杂碰撞体 —— btCompoundShape {% include relref_cnblogs.html %}](https://www.cnblogs.com/esCharacter/p/8490355.html)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://www.cnblogs.com/KillerAery/archive/2004/01/13/9223947.html]({% include relref.html url="/backup/2020-12-29-shader-Box-Shooter.md/www.cnblogs.com/8a2b5679.html" %})
- [2] [https://blog.csdn.net/azri81226/article/details/101691134]({% include relref.html url="/backup/2020-12-29-shader-Box-Shooter.md/blog.csdn.net/1c18af48.html" %})
- [3] [https://www.cnblogs.com/esCharacter/p/8490355.html]({% include relref.html url="/backup/2020-12-29-shader-Box-Shooter.md/www.cnblogs.com/465dd1d7.html" %})
