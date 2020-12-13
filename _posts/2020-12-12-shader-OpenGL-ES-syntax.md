---
layout: post
title: "“特效编程”笔记 -- GLSL ES 语法详解"
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
glslcanvas: true
---

> 无特殊说明，文中的 GLSL 均指 OpenGL ES 2.0 的着色语言。

[着色器语言 GLSL (opengl-shader-language) 入门大全](https://github.com/wshxbqq/GLSL-Card)


## 基本语法


### 向量构造

* 如果向量构造器中只提供了一个标量参数，则向量中所有值都会设定为该标量值。
* 如果提供了多个标量值或提供了向量参数，则会从左至右使用提供的参数来给向量赋值，如果使用多个标量来赋值，则需要确保标量的个数要多于向量构造器中的个数。

```glsl
vec4 myVec4 = vec4(1.0);            // myVec4 = {1.0, 1.0, 1.0, 1.0}
vec3 myVec3 = vec3(1.0, 0.0, 0.5);  // myVec3 = {1.0, 0.0, 0.5}

vec3 temp = vec3(myVec3);           // temp = myVec3
vec2 myVec2 = vec2(myVec3);         // myVec2 = {myVec3.x, myVec3.y}

myVec4 = vec4(myVec2, temp, 0.0);   // myVec4 = {myVec2.x, myVec2.y, temp, 0.0}
```


### 矩阵构造

* 如果对矩阵构造器只提供了一个标量参数，该值会作为矩阵的对角线上的值。例如 mat4(1.0) 可以构造一个 4×4 的单位矩阵。
* 矩阵可以通过多个向量作为参数来构造，例如一个 mat2 可以通过两个 vec2 来构造。
* 矩阵可以通过多个标量作为参数来构造，矩阵中每个值对应一个标量，按照从左到右的顺序。

在 OpenGL ES 中，**矩阵的值会以列的顺序来存储**。在构造矩阵时，构造器参数会按照列的顺序来填充矩阵，如下：

```glsl
mat3 myMat3 = mat3(1.0, 0.0, 0.0,  // 第一列
                   0.0, 1.0, 0.0,  // 第二列
                   0.0, 1.0, 1.0); // 第三列
```


### 矢量和矩阵的分量

依据构成向量的组件个数，向量的组件可以通过 {x, y, z, w}，{r, g, b, a} 或 {s, t, r, q} 等 swizzle 操作来获取。

在 OpenGL ES 2.0 中的某些情况下，数组下标不支持使用非常数的整型表达式（如使用整型变量索引），这是因为对于向量的动态索引操作，某些硬件设备处理起来很困难。
在 OpenGL ES 2.0 中仅对 uniform 类型的变量支持这种动态索引。

对于矩阵来说，可以通过数组下标“[]”来获取某一列的值。

```glsl
vec3 myVec3 = vec3(0.0, 1.0, 2.0); // myVec3 = {0.0, 1.0, 2.0}
vec3 temp;
temp = myVec3.xyz; // temp = {0.0, 1.0, 2.0}
temp = myVec3.xxx; // temp = {0.0, 0.0, 0.0}
temp = myVec3.zyx; // temp = {2.0, 1.0, 0.0}

mat4 myMat4 = mat4(1.0); // Initialize diagonal to 1.0 (identity)
vec4 col0 = myMat4[0];   // Get col0 vector out of the matrix
float m1_1 = myMat4[1][1]; // Get element at [1][1] in matrix
float m2_2 = myMat4[2].z;  // Get element at [2][2] in matrix
```


### 矢量和矩阵的操作

```glsl
vec3 v, u;
mat3 m;

u = v * m;
// 等价于：
u.x = dot(v, m[0]); // m[0] is the left column of m
u.y = dot(v, m[1]); // dot(a,b) is the inner (dot) product of a and b
u.z = dot(v, m[2]);

u = m * v;
// 等价于：
u.x = m[0].x * v.x + m[1].x * v.y + m[2].x * v.z; // 取 m 的行 0 * 向量 v
u.y = m[0].y * v.x + m[1].y * v.y + m[2].y * v.z;
u.z = m[0].z * v.x + m[1].z * v.y + m[2].z * v.z;

mat m, n, r;
r = m * n;
// 等价于：
r[0].x = m[0].x * n[0].x + m[1].x * n[0].y + m[2].x * n[0].z;
r[1].x = m[0].x * n[1].x + m[1].x * n[1].y + m[2].x * n[1].z;
r[2].x = m[0].x * n[2].x + m[1].x * n[2].y + m[2].x * n[2].z;
r[0].y = m[0].y * n[0].x + m[1].y * n[0].y + m[2].y * n[0].z;
r[1].y = m[0].y * n[1].x + m[1].y * n[1].y + m[2].y * n[1].z;
r[2].y = m[0].y * n[2].x + m[1].y * n[2].y + m[2].y * n[2].z;
r[0].z = m[0].z * n[0].x + m[1].z * n[0].y + m[2].z * n[0].z;
r[1].z = m[0].z * n[1].x + m[1].z * n[1].y + m[2].z * n[1].z;
r[2].z = m[0].z * n[2].x + m[1].z * n[2].y + m[2].z * n[2].z;
```


### 结构体

```glsl
struct customStruct {
    vec4 color;
    vec2 position;
} customVertex;

struct fogStruct {
    vec4 color;
    float start;
    float end;
} fogVar;

fogVar = fogStruct(vec4(0.0, 1.0, 0.0, 0.0), // color
                   0.5, // start
                   2.0); // end
```


### 数组

与 C 语言不同，在 GLSL 中，关于数组有两点需要注意：

* 除了 uniform 变量之外，数组的索引只允许使用常数整型表达式。
* 在 GLSL 中不能在创建的同时给数组初始化，即数组中的元素需要在定义数组之后逐个初始化，且数组不能使用 const 限定符。


### 函数

GLSL 中函数不能够递归调用，且必须声明返回值类型（无返回值时声明为 void）。


## 限定符

<table class="tablestyle" ntablew="3:7"></table>

| 限定符 | 描述 |
| ----- | ----- |
| < none: default > | 局部可读写变量，或者函数的参数 |
| const | 编译时常量，或只读的函数参数 |
| attribute | 由应用程序传输给顶点着色器的逐顶点的数据 |
| uniform | 在图元处理过程中其值保持不变，由应用程序传输给着色器 |
| varying | 由顶点着色器传输给片段着色器中的插值数据 |

本地变量和方法参数只能使用 const 限定符，方法返回值和结构体成员不能使用限定符。

不包含任何限定符或者包含 const 限定符的全局变量可以包含初始化器，这种情况下这些变量会在 main() 函数开始之后第一行代码之前被初始化，这些初始化值必须是常量表达式。
没有任何限定符的全局变量如果没有在定义时初始化或者在程序中被初始化，则其值在进入 main() 函数之后是未定义的。
uniform、attribute 和 varying 限定符修饰的变量不能在初始化时被赋值，这些变量的值由 OpenGL ES 计算提供。


### const 限定符

数组或者包含数组的结构体不能被声明为常量（因为数组不能在定义时被初始化）。

```glsl
const float zero = 0.0;
const float pi = 3.14159;
const vec4 red = vec4(1.0, 0.0, 0.0, 1.0);
const mat4 identity = mat4(1.0);
```


### attribute 限定符

attribute 变量只用于顶点着色器中，用来存储顶点着色器中每个顶点的输入（per-vertex inputs）。
attribute 通常用来存储位置坐标、法向量、纹理坐标和颜色等。注意 attribute 是用来存储单个顶点的信息。
OpenGL ES 2.0 实现支持的最少 attribute 个数是 8 个。

```glsl
// 顶点着色器 .vsh
attribute vec4 position;
attribute vec4 color;

varying vec4 colorVarying;

void main(void) {
    colorVarying = color;
    gl_Position = position;
}
```


### uniform 限定符

OpenGL ES 2.0 的实现必须提供至少 128 个顶点 uniform 向量及 16 片段 uniform 向量。

```glsl
uniform mat4 viewProjMatrix;
uniform mat4 viewMatrix;
uniform vec3 lightPosition;
```


### varying 限定符

OpenGL ES 2.0 实现中的 varying 变量最小支持数为 8。

varying 变量存在内插（interpolate）的过程。这些变量在片段着色器中需要有相对应的声明且数据类型一致，然后在光栅化过程中进行插值计算。


### invariant 限定符

invariant 可以作用于顶点着色器输出的任何一个 varying 变量。
所有的 invariant 输出量的上游数据流或控制流必须一致。

```glsl
invariant gl_Position; // make existing gl_Position be invariant
varying mediump vec3 Color;
invariant Color; // make existing Color be invariant
invariant varying mediump vec3 Color;
```


### precision 限定符

```glsl
highp vec4 position;
varying lowp vec4 color;
mediump float specularExp;

// 默认精度限定符放在着色器代码起始位置
precision highp float;
precision mediump int;
```

在片段着色器中可以使用以下代码，判断是否支持在片段着色器中使用高精度。

```glsl
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
```

<table class="tablestyle" ntablew="1:1:1:1:1"></table>

|  | 浮点数范围 | 浮点数大小范围 | 浮点数精度范围 | 整数范围 |
| ---- | ---- | ---- | ---- | ---- |
| highp | (-2^62, 2^62) | (2^-62, 2^62) | 相对：2^-16 | (-2^16, 2^16) |
| mediump | (-2^14, 2^14) | (2^-14, 2^14) | 相对：2^-10 | (-2^10, 2^10) |
| lowp | (-2, 2) | (2^-8, 2) | 绝对：2^-8 | (-2^8, 2^8) |

* 在一般变量中：invariant > storage > precision （storage：存储，precision：精度）
* 在函数参数中：storage > parameter > precision （parameter：参数）

```glsl
invariant varying lowp float color; // invariant > storage > precision

void doubleSize(const in lowp float s){ // storage > parameter > precision
    float s1 = s;
}
```


## 语句


### 运算符

```glsl
float myFloat;
vec4 myVec4;
mat4 myMat4;
myVec4 = myVec4 * myFloat; // Multiplies each component of myVec4 by a scalar myFloat
myVec4 = myVec4 * myVec4; // Multiplies each component of myVec4 together (e.g., myVec4 ^ 2)
myVec4 = myMat4 * myVec4; // Does a matrix * vector multiply of myMat4 * myVec4
myMat4 = myMat4 * myMat4; // Does a matrix * matrix multiply of myMat4 * myMat4
myMat4 = myMat4 * myFloat; // Multiplies each matrix component by the scalar myFloat
```


### 流程控制语句

循环终止条件也必须是循环变量和常量的简单比较，在循环内部不能改变循环变量的值。

```glsl
float myArr[4];
for(int i = 0; i < 3; i++) {
    sum += myArr[i]; // NOT ALLOWED IN OPENGL ES, CANNOT DO INDEXING WITH NONCONSTANT EXPRESSION
}
...
uniform int loopIter;
// NOT ALLOWED IN OPENGL ES, loopIter ITERATION COUNT IS NONCONSTANT
for(int i = 0; i < loopIter; i++) {
    sum += i;
}
```


## 函数

GLSL 中的函数不能够递归调用。

<table class="tablestyle" ntablew="3:7"></table>

| 限定符 | 描述 |
| ----- | ----- |
| in | 默认使用的缺省限定符，指明参数传递的是值，并且函数不会修改传入的值（C 语言中传递值） |
| inout | 指明参数传入的是引用，如果在函数中对参数的值进行了修改，当函数结束后参数的值也会修改（C 语言中传递引用） |
| out | 参数的值不会传入函数，但是在函数内部修改其值，函数结束后其值会被修改 |

```glsl
vec4 myFunc(inout float myFloat, // inout parameter
            out vec4 myVec4, // out parameter
            mat4 myMat4); // in parameter (default)
```


## 预处理

```glsl
#define
#undef
#if
#ifdef
#ifndef
#else
#elif
#endif
```

<dl>
<dt>__LINE__</dt> <dd>
当前源码中的行号。
</dd>

<dt>__FILE__</dt> <dd>
OpenGL ES 2.0 中始终为 0。
</dd>

<dt>__VERSION__</dt> <dd>
一个整数，指示当前的 glsl 版本。比如 100 ps: 100 = v1.00。
</dd>

<dt>GL_ES</dt> <dd>
如果当前是在 OpenGL ES 环境中运行则 GL_ES 被设置成 1，一般用来检查当前环境是不是 OPENGL ES。
</dd>

</dl>

```glsl
// 这一标记需要写在代码的最开始位置，对于 OpenGL ES 2.0 的着色器应将此值设置为 100。
#version 100 // OpenGL ES Shading Language v1.00

#ifdef GL_ES
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
#endif

#define NUM 100
#if NUM == 100
#endif

// Set behavior for an extension
#extension extension_name : behavior
// Set behavior for ALL extensions
#extension all : behavior

// 实现不支持 3D 纹理扩展
#extension GL_OES_texture_3D : enable
```


## 顶点着色器或片段着色器的内置常量

gl_Position 为齐次顶点位置坐标。


### 片段着色器内置变量

片段着色器中有一个只读变量 gl_FragCoord，存储了片段的窗口相对坐标 x、y、z 及 1/w。
该值是在顶点处理阶段之后对图元插值生成片段计算所得。z 分量是深度值用来表示片段的深度。

```glsl
mediump vec4 gl_FragCoord;
bool gl_FrontFacing;
mediump vec4 gl_FragColor;
mediump vec4 gl_FragData[gl_MaxDrawBuffers];
mediump vec2 gl_PointCoord;
```

Implementation dependent constants. The example values below
are the minimum values allowed for these maximums.

<dl>
<dt>const mediump int gl_MaxVertexAttribs = 8;</dt> <dd>
gl_MaxVertexAttribs 表示在 vertex shader（顶点着色器）中可用的最大 attributes 数。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 8 个。
</dd>

<dt>const mediump int gl_MaxVertexUniformVectors = 128;</dt> <dd>
gl_MaxVertexUniformVectors 表示在 vertex shader（顶点着色器）中可用的最大 uniform vectors 数。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 128 个。
</dd>

<dt>const mediump int gl_MaxVaryingVectors = 8;</dt> <dd>
gl_MaxVaryingVectors 表示在 vertex shader（顶点着色器）中可用的最大 varying vectors 数。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 8 个。
</dd>

<dt>const mediump int gl_MaxVertexTextureImageUnits = 0;</dt> <dd>
gl_MaxCombinedTextureImageUnits 表示在 vertex shader（顶点着色器）中可用的最大纹理单元数（贴图）。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，甚至可以一个都没有（无法获取顶点纹理）。
</dd>

<dt>const mediump int gl_MaxCombinedTextureImageUnits = 8;</dt> <dd>
gl_MaxCombinedTextureImageUnits 表示在 vertex Shader 和 fragment Shader 总共最多支持多少个纹理单元。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 8 个。
</dd>

<dt>const mediump int gl_MaxTextureImageUnits = 8;</dt> <dd>
gl_MaxTextureImageUnits 表示在 fragment Shader（片元着色器）中能访问的最大纹理单元数。
个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 8 个。
</dd>

<dt>const mediump int gl_MaxFragmentUniformVectors = 16;</dt> <dd>
gl_MaxFragmentUniformVectors 表示在 fragment Shader（片元着色器）中可用的最大 uniform vectors 数。
这个值的大小取决于 OpenGL ES 在某设备上的具体实现，不过最低不能小于 16 个。
</dd>

<dt>const mediump int gl_MaxDrawBuffers = 1;</dt> <dd>
gl_MaxDrawBuffers 表示可用的 drawBuffers 数。
在 OpenGL ES 2.0 中这个值为 1，在将来的版本可能会有所变化。
</dd>
</dl>


## 内置函数

片段着色器中用来计算镜面光的代码：

```glsl
float nDotL = dot(normal, light);
float rDotV = dot(viewDir, (2.0 * normal) * nDotL – light);
float specular = specularColor * pow(rDotV, specularPower);
```

对于纹理函数，返回类型的精度与采样器的类型相匹配。

```glsl
uniform lowp sampler2D sampler;
highp vec2 coord;
...
lowp vec4 col = texture2D(sampler, coord); // texture2D returns lowp
```

对于纹理函数，返回类型的精度与采样器的类型相匹配。

```glsl
uniform lowp sampler2D sampler;
highp vec2 coord;
...
lowp vec4 col = texture2D(sampler, coord); // texture2D returns lowp
```


### 角度和三角函数

Syntax & Description

<dl>
<dt> genType radians (genType degrees) </dt><dd> Converts degrees to radians. </dd>
<dt> genType degrees (genType radians) </dt><dd> Converts radians to degrees. </dd>
<dt> genType sin (genType angle) </dt><dd> The standard trigonometric sine function. </dd>
<dt> genType cos (genType angle) </dt><dd> The standard trigonometric cosine function. </dd>
<dt> genType tan (genType angle) </dt><dd> The standard trigonometric tangent. </dd>
<dt> genType asin (genType x) </dt><dd> Arc sine. Returns an angle whose sine is x. The range of values returned by this function is [-π/2, π/2]. Results are undefined if ∣x∣ > 1. </dd>
<dt> genType acos (genType x) </dt><dd> Arc cosine. Returns an angle whose cosine is x. The range of values returned by this function is [0, π]. Results are undefined if ∣x∣ > 1. </dd>
<dt> genType atan (genType y, genType x) </dt><dd> Arc tangent. Returns an angle whose tangent is y/x. The signs of x and y are used to determine what quadrant the angle is in. The range of values returned by this function is [−π,π]. Results are undefined if x and y are both 0. </dd>
<dt> genType atan (genType y_over_x) </dt><dd> Arc tangent. Returns an angle whose tangent is y_over_x. The range of values returned by this function is [−π/2, π/2]. </dd>
</dl>


### 通用函数

Syntax & Description

<dl>
<dt> genType abs (genType x) </dt><dd> Returns x if x >= 0, otherwise it returns –x. </dd>
<dt> genType sign (genType x) </dt><dd> Returns 1.0 if x > 0, 0.0 if x = 0, or –1.0 if x < 0. </dd>
<dt> genType floor (genType x) </dt><dd> Returns a value equal to the nearest integer that is less than or equal to x. </dd>
<dt> genType ceil (genType x) </dt><dd> Returns a value equal to the nearest integer that is greater than or equal to x. </dd>

<dt> genType fract (genType x) </dt><dd> Returns x – floor (x). </dd>
<dt> genType mod (genType x, float y) </dt><dd> Modulus (modulo). Returns x – y ∗ floor (x/y). </dd>
<dt> genType mod (genType x, genType y) </dt><dd> Modulus. Returns x – y ∗ floor (x/y). </dd>

<dt> genType min (genType x, genType y) </dt>
<dt> genType min (genType x, float y) </dt><dd> Returns y if y < x, otherwise it returns x. </dd>

<dt> genType max (genType x, genType y) </dt>
<dt> genType max (genType x, float y) </dt><dd> Returns y if x < y, otherwise it returns x. </dd>

<dt> genType clamp (genType x, genType minVal, genType maxVal) </dt>
<dt> genType clamp (genType x, float minVal, float maxVal) </dt><dd> Returns min (max (x, minVal), maxVal) Results are undefined if minVal > maxVal. </dd>

<dt> genType mix (genType x, genType y, genType a) </dt>
<dt> genType mix (genType x, genType y, float a) </dt><dd> Returns the linear blend of x and y: x(1-a)+ya. </dd>

<dt> genType step (genType edge, genType x) </dt>
<dt> genType step (float edge, genType x) </dt><dd> Returns 0.0 if x < edge, otherwise it returns 1.0. </dd>

<dt> genType smoothstep (genType edge0, genType edge1, genType x) </dt>
<dt> genType smoothstep (float edge0, float edge1, genType x) </dt><dd>
Returns 0.0 if x <= edge0 and 1.0 if x >= edge1 and performs smooth Hermite interpolation between 0 and 1 when edge0 < x < edge1.
This is useful in cases where you would want a threshold function with a smooth transition.
This is equivalent to: genType t; t = clamp ((x – edge0) / (edge1 – edge0), 0, 1);
return t * t * (3 – 2 * t); Results are undefined if edge0 >= edge1. </dd>
</dl>


### 几何函数

Syntax & Description

<dl>
<dt> float length (genType x) </dt><dd> Returns the length of vector x. </dd>
<dt> float distance (genType p0, genType p1) </dt><dd> Returns the distance between p0 and p1. </dd>
<dt> float dot (genType x, genType y) </dt><dd> Returns the dot product of x and y. </dd>
<dt> vec3 cross (vec3 x, vec3 y) </dt><dd> Returns the cross product of x and y. </dd>
<dt> genType normalize (genType x) </dt><dd> Returns a vector in the same direction as x but with a length of 1. </dd>
<dt> genType faceforward(genType N, genType I, genType Nref) </dt><dd> If dot(Nref, I) < 0 return N, otherwise return –N. </dd>
<dt> genType reflect (genType I, genType N) </dt><dd> For the incident vector I and surface orientation N, returns the reflection direction: I – 2 ∗ dot(N, I) ∗ N. N must already be normalized in order to achieve the desired result. </dd>
<dt> genType refract(genType I, genType N, float eta) </dt><dd>
For the incident vector I and surface normal N, and the ratio of indices of refraction eta, return the refraction vector.
The result is computed by k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I));
if (k < 0.0) return genType(0.0) else return eta * I - (eta * dot(N, I) + sqrt(k)) * N.
The input parameters for the incident vector I and thesurface normal N must already be normalized to get the desired results. </dd>
</dl>


### 矩阵函数

Syntax & Description

<dl>
<dt> mat matrixCompMult (mat x, mat y) </dt><dd>
Multiply matrix x by matrix y component-wise, i.e., result[i][j] is the scalar product of x[i][j] and y[i][j].
Note: to get linear algebraic matrix multiplication, usethe multiply operator (*).
</dd>
</dl>


### 矢量关系函数

Syntax & Description

<dl>
<dt> bvec lessThan(vec x, vec y) </dt>
<dt> bvec lessThan(ivec x, ivec y) </dt><dd> Returns the component-wise compare of x < y.</dd>
<dt> bvec lessThanEqual(vec x, vec y) </dt>
<dt> bvec lessThanEqual(ivec x, ivec y) </dt><dd> Returns the component-wise compare of x <= y.</dd>
<dt> bvec greaterThan(vec x, vec y) </dt>
<dt> bvec greaterThan(ivec x, ivec y) </dt><dd> Returns the component-wise compare of x > y.</dd>
<dt> bvec greaterThanEqual(vec x, vec y) </dt>
<dt> bvec greaterThanEqual(ivec x, ivec y) </dt><dd> Returns the component-wise compare of x >= y.</dd>
<dt> bvec equal(vec x, vec y) </dt>
<dt> bvec equal(ivec x, ivec y) </dt>
<dt> bvec equal(bvec x, bvec y) </dt>
<dt> bvec notEqual(vec x, vec y) </dt>
<dt> bvec notEqual(ivec x, ivec y) </dt>
<dt> bvec notEqual(bvec x, bvec y) </dt><dd> Returns the component-wise compare of x == y; Returns the component-wise compare of x != y.</dd>
<dt> bool any(bvec x) </dt><dd> Returns true if any component of x is true.</dd>
<dt> bool all(bvec x) </dt><dd> Returns true only if all components of x are true.</dd>
<dt> bvec not(bvec x) </dt><dd> Returns the component-wise logical complement of x.</dd>
</dl>


### 纹理查找函数

图像纹理有两种：一种是平面 2d 纹理，另一种是盒纹理。针对不同的纹理类型有不同访问方法。
* 函数中带有 Cube 字样的是指需要传入盒状纹理。
* 带有 Proj 字样的是指带投影的版本。

以下函数只在顶点着色器中可用：

```glsl
vec4 texture2DLod(sampler2D sampler, vec2 coord, float lod);
vec4 texture2DProjLod(sampler2D sampler, vec3 coord, float lod);
vec4 texture2DProjLod(sampler2D sampler, vec4 coord, float lod);
vec4 textureCubeLod(samplerCube sampler, vec3 coord, float lod);
```

以下函数只在片段着色器中可用：

```glsl
vec4 texture2D(sampler2D sampler, vec2 coord, float bias);
vec4 texture2DProj(sampler2D sampler, vec3 coord, float bias);
vec4 texture2DProj(sampler2D sampler, vec4 coord, float bias);
vec4 textureCube(samplerCube sampler, vec3 coord, float bias);
```

在定点着色器和片段着色器中都可用：

```glsl
vec4 texture2D(sampler2D sampler, vec2 coord);
vec4 texture2DProj(sampler2D sampler, vec3 coord);
vec4 texture2DProj(sampler2D sampler, vec4 coord);
vec4 textureCube(samplerCube sampler, vec3 coord);
```

Syntax & Description

<dl>
<dt> vec4 texture2D (sampler2D sampler, vec2 coord) </dt>
<dt> vec4 texture2D (sampler2D sampler, vec2 coord, float bias) </dt>
<dt> vec4 texture2DProj (sampler2D sampler, vec3 coord) </dt>
<dt> vec4 texture2DProj (sampler2D sampler, vec3 coord, float bias) </dt>
<dt> vec4 texture2DProj (sampler2D sampler, vec4 coord) </dt>
<dt> vec4 texture2DProj (sampler2D sampler, vec4 coord, float bias) </dt>
<dt> vec4 texture2DLod (sampler2D sampler, vec2 coord, float lod) </dt>
<dt> vec4 texture2DProjLod (sampler2D sampler, vec3 coord, float lod) </dt>
<dt> vec4 texture2DProjLod (sampler2D sampler, vec4 coord, float lod) </dt><dd>
Use the texture coordinate coord to do a texture lookup in the 2D texture currently bound to sampler.
For the projective(“Proj”) versions, the texture coordinate(coord.s, coord.t) is divided by the lastcomponent of coord.
The third componentof coord is ignored for the vec4 coordvariant. </dd>
<dt> vec4 textureCube (samplerCube sampler, vec3 coord) </dt>
<dt> vec4 textureCube (samplerCube sampler, vec3 coord, float bias) </dt>
<dt> vec4 textureCubeLod (samplerCube sampler, vec3 coord, float lod) </dt><dd>
Use the texture coordinate coord to do a texture lookup in the cube map texture currently bound to sampler.
The direction of coord is used to select which face to do a 2-dimensional texture lookup in. </dd>
</dl>


## Sample Program

A shader pair that applies diffuse and ambient lighting to a
textured object.

这个例子是 OpenGL® ES 官方唯一的例子，能看懂了，估计就差不多了。

Vertex Shader:

```glsl
// model-view-projection matrix
uniform mat4 mvp_matrix; // 透视矩阵 * 视图矩阵 * 模型变换矩阵
// normal matrix
uniform mat3 normal_matrix; // 法线变换矩阵（用于物体变换后法线跟着变换）
// light direction in eye coords
uniform vec3 ec_light_dir; // 光照方向
// vertex position
attribute vec4 a_vertex; // 顶点坐标
// vertex normal
attribute vec3 a_normal; // 顶点法线
// texture coordinates
attribute vec2 a_texcoord; // 纹理坐标
varying float v_diffuse; // 法线与入射光的夹角
varying vec2 v_texcoord; // 2d 纹理坐标

void main(void) {
    // 归一化法线
    // put vertex normal into eye coords
    vec3 ec_normal = normalize(normal_matrix * a_normal);
    // v_diffuse 是法线与光照的夹角。根据向量点乘法则，当两向量长度为 1 是乘积，即 cosθ 值。
    // emit diffuse scale factor, texcoord, and position
    v_diffuse = max(dot(ec_light_dir, ec_normal), 0.0);
    v_texcoord = a_texcoord;
    gl_Position = mvp_matrix * a_vertex;
}
```

Fragment Shader:

```glsl
precision mediump float;
uniform sampler2D t_reflectance;
uniform vec4 i_ambient;
varying float v_diffuse;
varying vec2 v_texcoord;

void main (void) {
    vec4 color = texture2D(t_reflectance, v_texcoord);
    // 这里分解开来是 color*vec3(1,1,1)*v_diffuse + color*i_ambient
    // 色 * 光 * 夹角 cos + 色 * 环境光
    gl_FragColor = color*(vec4(v_diffuse) + i_ambient);
}
```


## 参考

- [OpenGL-ES-2_0-Reference-card.pdf](https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf)
- [OpenGL® ES Common Profile Specification Version 2.0.25 (Full Specification)](https://www.khronos.org/registry/OpenGL/specs/es/2.0/es_full_spec_2.0.pdf)
- [The OpenGL® ES Shading Language](https://www.khronos.org/registry/OpenGL/specs/es/2.0/GLSL_ES_Specification_1.00.pdf)
- [OpenGL ES 开篇](http://colin1994.github.io/2017/04/01/OpenGLES-Lesson00/)
- [OpenGL ES 基础概念](http://colin1994.github.io/2017/04/01/OpenGLES-Lesson01/)
- [OpenGL ES 渲染基本图元](http://colin1994.github.io/2017/04/18/OpenGLES-Lesson03/)
- [GLSL 详解（基础篇）](http://colin1994.github.io/2017/11/11/OpenGLES-Lesson04/)
- [GLSL 详解（高级篇）](http://colin1994.github.io/2017/11/12/OpenGLES-Lesson05/)
- [OpenGL ES 2.0 着色器语言 GLSL（一）](https://aillieo.cn/post/2017-01-15-opengl-es-glsl-01/)
- [OpenGL ES 2.0 着色器语言 GLSL（二）](https://aillieo.cn/post/2017-01-15-opengl-es-glsl-02/)

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://github.com/wshxbqq/GLSL-Card]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/github.com/eb0ca84c.html" %})
- [2] [https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/www.khronos.org/98468c82.pdf" %})
- [3] [https://www.khronos.org/registry/OpenGL/specs/es/2.0/es_full_spec_2.0.pdf]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/www.khronos.org/3de8e2e8.pdf" %})
- [4] [https://www.khronos.org/registry/OpenGL/specs/es/2.0/GLSL_ES_Specification_1.00.pdf]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/www.khronos.org/c9f59425.pdf" %})
- [5] [http://colin1994.github.io/2017/04/01/OpenGLES-Lesson00/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/colin1994.github.io/8dca1d49.html" %})
- [6] [http://colin1994.github.io/2017/04/01/OpenGLES-Lesson01/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/colin1994.github.io/9d400944.html" %})
- [7] [http://colin1994.github.io/2017/04/18/OpenGLES-Lesson03/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/colin1994.github.io/ccc07110.html" %})
- [8] [http://colin1994.github.io/2017/11/11/OpenGLES-Lesson04/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/colin1994.github.io/38603e34.html" %})
- [9] [http://colin1994.github.io/2017/11/12/OpenGLES-Lesson05/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/colin1994.github.io/83ea5c3d.html" %})
- [10] [https://aillieo.cn/post/2017-01-15-opengl-es-glsl-01/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/aillieo.cn/b0590368.html" %})
- [11] [https://aillieo.cn/post/2017-01-15-opengl-es-glsl-02/]({% include relref.html url="/backup/2020-12-12-shader-OpenGL-syntax.md/aillieo.cn/86b76eca.html" %})
