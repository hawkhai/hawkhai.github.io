---
layout: post
title: "特效编程笔记 --《The Book of Shaders》读书笔记"
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
codeprint:
---

The Book of Shaders -- 这是一本非常坑爹的书，因为作者没写完。

可编程渲染管线 OpenGL Shader / GLSL

编辑器：<https://thebookofshaders.com/edit.php>

Firefox 着色编辑器：<https://developer.mozilla.org/zh-CN/docs/Tools/Shader_Editor>


## TOOLS

* ShaderToy.com Shader

    <https://www.shadertoy.com/>

* glslViewer

    GlslViewer is a flexible console-base OpenGL Sandbox to display 2D/3D GLSL shaders without the need of an UI.

    <https://github.com/patriciogonzalezvivo/glslViewer>

* glslCanvas

    用 WebGL 显示 shader。Simple tool to load GLSL shaders on HTML Canvas using WebGL.

    <https://github.com/patriciogonzalezvivo/glslCanvas>

* GraphToy

    在 WebGL 中可视化 GLSL 函数。

    <http://www.iquilezles.org/apps/graphtoy/>

    Shadershop：视觉化和直观的方式教你如何建造复杂的函数。<http://tobyschachman.com/Shadershop/>

* Three.js

    无数程序示例，教程，书籍，教你如何用这个 JavaScript 库做出酷炫的 3D 图像。

    <http://threejs.org/>

* Processing

    Processing is a flexible software sketchbook and a language for learning how to code within the context of the visual arts.
    更多 Processing 的 shader 教程戳 [tutorial](https://processing.org/tutorials/pshader/)。

    <https://processing.org/>

* openFrameworks

    开源的、跨平台的 C++ 工具包，它的设计目的为开发创造过程提供一个更加简单和直观的框架。
    [Introducing Shaders](https://openframeworks.cc/ofBook/chapters/shaders.html)

    <http://openframeworks.cc/>


## 抽象性、盲视、无记忆

为了能使许多管线并行运行，每一个线程必须与其他的相独立。
我们称这些线程对于其他线程在进行的运算是“盲视”的。
这个限制就会使得所有数据必须以相同的方向流动。
所以就不可能检查其他线程的输出结果，修改输入的数据，或者把一个线程的输出结果输入给另一个线程。
如果允许线程到线程的数据流动将使所有的数据面临威胁。

并且 GPU 会让所有并行的微处理器（管道们）一直处在忙碌状态；只要它们一有空闲就会接到新的信息。
一个线程不可能知道它前一刻在做什么。
它可能是在画操作系统界面上的一个按钮，然后渲染了游戏中的一部分天空，然后显示了一封 email 中的一些文字。
每个线程不仅是“盲视”的，而且还是“无记忆”的。
同时，它要求编写一个通用的规则，依据像素的不同位置依次输出不同的结果。


### 着色器输入

```glsl
uniform vec3      iResolution;           // viewport resolution (in pixels)
uniform float     iTime;                 // shader playback time (in seconds)
uniform float     iTimeDelta;            // render time (in seconds)
uniform int       iFrame;                // shader playback frame
uniform float     iChannelTime[4];       // channel playback time (in seconds)
uniform vec3      iChannelResolution[4]; // channel resolution (in pixels)
uniform vec4      iMouse;                // mouse pixel coords. xy: current (if MLB down), zw: click
uniform samplerCube iChannel0..3;        // input channel Cube
uniform sampler2D iChannel0..3;          // input channel 2D
uniform vec4      iDate;                 // (year, month, day, time in seconds)
uniform float     iSampleRate;           // sound sample rate (i.e., 44100)
```


## Hello World

```glsl
#ifdef GL_ES
precision mediump float; // 中等精度
#endif

uniform float u_time; // 统一值，时间（加载后的秒数）iTime
uniform vec2 u_resolution; // 画布尺寸（宽，高）iResolution
uniform vec2 u_mouse; // 鼠标位置（在屏幕上哪个像素）iMouse xy：当前位置, zw：点击位置

void main() {
    gl_FragColor = vec4(abs(sin(u_time)),0.0,1.0,1.0); // 红绿蓝和透明度通道
}
```

GLSL 语言规范并不保证变量会被自动转换类别。
要求有最精简的语言规范。因而，自动强制类型转换并没有包括在其中。
最好养成在 float 型数值里加一个 . 的好习惯。


### Uniforms

每个线程和其他线程之间不能有数据交换，但我们能从 CPU 给每个线程输入数据。
因为显卡的架构，所有线程的输入值必须统一（uniform），而且必须设为只读。
也就是说，每条线程接收相同的数据，并且是不可改变的数据。


### gl_FragCoord

varying（变化值）。gl_FragCoord 存储了活动线程正在处理的像素或屏幕碎片的坐标。
因为每个像素的坐标都不同，所以我们把它叫做 varying（变化值）。

```glsl
#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution;
    gl_FragColor = vec4(st.x,st.y,0.0,1.0);
}
```

[OpenGL·投影与变换 {% include relref_jianshu.html %}](https://www.jianshu.com/p/64c236d5c67a)

{% include image.html url="/assets/images/201102-shader-thebookofshaders/2852335-c8a888f710b623d1.webp" %}


## 算法绘画 造型函数

```glsl
y = mod(x,0.5); // 返回 x 对 0.5 取模的值
//y = fract(x); // 仅仅返回数的小数部分
//y = ceil(x);  // 向正无穷取整
//y = floor(x); // 向负无穷取整
//y = sign(x);  // 提取 x 的正负号
//y = abs(x);   // 返回 x 的绝对值
//y = clamp(x,0.0,1.0); // 把 x 的值限制在 0.0 到 1.0
//y = min(0.0,x);   // 返回 x 和 0.0 中的较小值
//y = max(0.0,x);   // 返回 x 和 0.0 中的较大值
```


### 颜色

下面的代码展示了所有访问相同数据的方式：

```glsl
vec4 vector;
vector[0] = vector.r = vector.x = vector.s;
vector[1] = vector.g = vector.y = vector.t;
vector[2] = vector.b = vector.z = vector.p;
vector[3] = vector.a = vector.w = vector.q;
```

#### HSB

```glsl
#ifdef GL_ES
precision mediump float;
#endif

#define TWO_PI 6.28318530718

uniform vec2 u_resolution;
uniform float u_time;

//  Function from Iñigo Quiles
//  https://www.shadertoy.com/view/MsS3Wc
vec3 hsb2rgb( in vec3 c ){
    vec3 rgb = clamp(abs(mod(c.x*6.0+vec3(0.0,4.0,2.0),
                             6.0)-3.0)-1.0,
                     0.0,
                     1.0 );
    rgb = rgb*rgb*(3.0-2.0*rgb);
    return c.z * mix( vec3(1.0), rgb, c.y);
}

void main(){
    vec2 st = gl_FragCoord.xy/u_resolution;
    vec3 color = vec3(0.0);

    // Use polar coordinates instead of cartesian
    vec2 toCenter = vec2(0.5)-st;
    float angle = atan(toCenter.y,toCenter.x);
    float radius = length(toCenter)*2.0;

    // Map the angle (-PI to PI) to the Hue (from 0 to 1)
    // and the Saturation to the radius
    color = hsb2rgb(vec3((angle/TWO_PI)+0.5,radius,1.0));

    gl_FragColor = vec4(color,1.0);
}
```

{% include canvas.html fragUrl="/source/shader/shader.frag" width="256" height="256" %}


### 形状

#### 叉乘 $a \times b$

也叫向量积。结果是一个和已有两个向量都垂直的向量，向量模长是向量 A，B 组成平行四边形的面积；向量方向是垂直于向量 A，B 组成的平面。

#### 点乘 $a \cdot b$

也叫数量积。几何意义：投影。结果是一个向量在另一个向量方向上投影的长度，是一个标量。

$\mathbf{A} \cdot \mathbf{B}=\|\mathbf{A} \|\| \mathbf{B}\| \cos \theta$

```glsl
#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359
#define TWO_PI 6.28318530718

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

void main() {
  vec2 st = gl_FragCoord.xy / u_resolution.xy;
  st.x *= u_resolution.x / u_resolution.y;
  vec3 color = vec3(0.0);
  float d = 0.0;
  st = st *2.-1.;
  int N = 5; // Number of sides of your shape
  float a = atan(st.x,st.y)+PI;
  float r = TWO_PI/float(N);
  d = cos(floor(.5+a/r)*r-a)*length(st);
  color = vec3(1.0-smoothstep(.4,.41,d));
  gl_FragColor = vec4(color,1.0);
}
```

{% include canvas.html width="256" height="256" %}


### 做一个 shader 来表现流体的质感

```glsl
// Author @patriciogv - 2015
// http://patriciogonzalezvivo.com

#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

vec3 mod289(vec3 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec2 mod289(vec2 x) { return x - floor(x * (1.0 / 289.0)) * 289.0; }
vec3 permute(vec3 x) { return mod289(((x*34.0)+1.0)*x); }

float snoise(vec2 v) {
    const vec4 C = vec4(0.211324865405187,  // (3.0-sqrt(3.0))/6.0
                        0.366025403784439,  // 0.5*(sqrt(3.0)-1.0)
                        -0.577350269189626,  // -1.0 + 2.0 * C.x
                        0.024390243902439); // 1.0 / 41.0
    vec2 i  = floor(v + dot(v, C.yy) );
    vec2 x0 = v -   i + dot(i, C.xx);
    vec2 i1;
    i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
    vec4 x12 = x0.xyxy + C.xxzz;
    x12.xy -= i1;
    i = mod289(i); // Avoid truncation effects in permutation
    vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 ))
        + i.x + vec3(0.0, i1.x, 1.0 ));

    vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
    m = m*m ;
    m = m*m ;
    vec3 x = 2.0 * fract(p * C.www) - 1.0;
    vec3 h = abs(x) - 0.5;
    vec3 ox = floor(x + 0.5);
    vec3 a0 = x - ox;
    m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );
    vec3 g;
    g.x  = a0.x  * x0.x  + h.x  * x0.y;
    g.yz = a0.yz * x12.xz + h.yz * x12.yw;
    return 130.0 * dot(m, g);
}

void main() {
    vec2 st = gl_FragCoord.xy/u_resolution.xy;
    st.x *= u_resolution.x/u_resolution.y;
    vec3 color = vec3(0.0);
    vec2 pos = vec2(st*3.);

    float DF = 0.0;

    // Add a random position
    float a = 0.0;
    vec2 vel = vec2(u_time*.1);
    DF += snoise(pos+vel)*.25+.25;

    // Add a random position
    a = snoise(pos*vec2(cos(u_time*0.15),sin(u_time*0.1))*0.1)*3.1415;
    vel = vec2(cos(a),sin(a));
    DF += snoise(pos+vel)*.25+.25;

    color = vec3( smoothstep(.7,.75,fract(DF)) );

    gl_FragColor = vec4(1.0-color,1.0);
}

```

{% include canvas.html width="256" height="256" %}


### Smiley Tutorial

<https://www.shadertoy.com/view/lsXcWn>

{% include image.html url="/assets/images/201102-shader-thebookofshaders/chrome_2.webp" %}

理论：<https://zhuanlan.zhihu.com/p/274849965>


## <font color="red">The Book of Shaders</font>

TODO: <https://thebookofshaders.com/13/?lan=ch>
-- **<font color="red">后面的看不了了？喔靠。</font>**

<https://github.com/patriciogonzalezvivo/thebookofshaders>

Step-by-step guide through the abstract and complex universe of Fragment Shaders.

[thebookofshaders.com](https://thebookofshaders.com/?lan=ch)


### Shader School <sup>有点老旧了<sup>

<https://github.com/stackgl/shader-school>

[A workshopper for GLSL shaders and graphics programming {% include relref_github.html %}](https://github.com/stackgl/shader-school)


### Other

* 各种例子：<https://github.com/McNopper/OpenGL>

    [OpenGL 3 and 4 with GLSL](http://nopper.tv)

* GlslViewer is a flexible console-base OpenGL Sandbox to display 2D/3D GLSL shaders without the need of an UI.

    You can definitely make your own UI or wrapper using the Python Module (include) or any other tool that communicates back/forth with glslViewer thought the standard POSIX console In/Out or OSC.

    GlslViewer support both 2D shaders and/or 3D shaders when a geometry (LST, PLY, OBJ or GLTF) is provided.

    <https://github.com/patriciogonzalezvivo/glslViewer>

    [Console-based GLSL Sandbox for 2D/3D shaders shaders](http://patriciogonzalezvivo.com/2015/glslViewer/)

* A Processing/Java library for high performance GPU-Computing (GLSL).

    <https://github.com/diwi/PixelFlow>

    Fluid Simulation + SoftBody Dynamics + Optical Flow + Rendering + Image Processing + Particle Systems + Physics + ...

    [PixelFlow {% include relref_github.html %}](https://diwi.github.io/PixelFlow/)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-11-02-shader-thebookofshaders.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://thebookofshaders.com/edit.php]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/thebookofshaders.com/3f2fc15d.php" %})
- [https://developer.mozilla.org/zh-CN/docs/Tools/Shader_Editor]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/developer.mozilla.org/971a6524.html" %})
- [https://www.shadertoy.com/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/www.shadertoy.com/c13e8871.html" %})
- [https://github.com/patriciogonzalezvivo/glslViewer]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/3ab3746c.html" %})
- [https://github.com/patriciogonzalezvivo/glslCanvas]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/5ca399c8.html" %})
- [http://www.iquilezles.org/apps/graphtoy/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/www.iquilezles.org/20a82882.html" %})
- [http://tobyschachman.com/Shadershop/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/tobyschachman.com/217a68f7.html" %})
- [http://threejs.org/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/threejs.org/bccb0fea.html" %})
- [https://processing.org/tutorials/pshader/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/processing.org/867be363.html" %})
- [https://processing.org/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/processing.org/f9515281.html" %})
- [https://openframeworks.cc/ofBook/chapters/shaders.html]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/openframeworks.cc/790196af.html" %})
- [http://openframeworks.cc/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/openframeworks.cc/f38e9e37.html" %})
- [https://www.jianshu.com/p/64c236d5c67a]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/www.jianshu.com/4137c4a6.html" %})
- [https://www.shadertoy.com/view/MsS3Wc]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/www.shadertoy.com/1a7822f1.html" %})
- [http://patriciogonzalezvivo.com]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/patriciogonzalezvivo.com/5d3a45d3.html" %})
- [https://www.shadertoy.com/view/lsXcWn]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/www.shadertoy.com/2115a8e3.html" %})
- [https://zhuanlan.zhihu.com/p/274849965]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/zhuanlan.zhihu.com/ddfcca9b.html" %})
- [https://thebookofshaders.com/13/?lan=ch]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/thebookofshaders.com/e20b68f2.html" %})
- [https://github.com/patriciogonzalezvivo/thebookofshaders]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/66beb98c.html" %})
- [https://thebookofshaders.com/?lan=ch]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/thebookofshaders.com/e26e2da0.html" %})
- [https://github.com/stackgl/shader-school]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/87397fc6.html" %})
- [https://github.com/McNopper/OpenGL]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/0f0f0a81.html" %})
- [http://nopper.tv]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/nopper.tv/809dad1c.html" %})
- [http://patriciogonzalezvivo.com/2015/glslViewer/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/patriciogonzalezvivo.com/7660f1c4.html" %})
- [https://github.com/diwi/PixelFlow]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/github.com/db4769bd.html" %})
- [https://diwi.github.io/PixelFlow/]({% include relref.html url="/backup/2020-11-02-shader-thebookofshaders.md/diwi.github.io/fcf5d56e.html" %})
