---
layout: post
title: "图形学笔记 -- OpenGL 毕业报告 / 模拟显卡 GPU，C++ 实现光栅化渲染器"
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

OpenGL 毕业报告 / 模拟显卡 GPU，C++ 实现光栅化渲染器。
主要参考 mini3d 代码，重写了一遍，加深理解。

{% include image.html url="/assets/images/210427-a-software-renderer-in-c/mini3d.webp" %}

实现一个固定管线的软件渲染器。普通坐标（Ordinary Coordinate 笛卡尔坐标）和齐次坐标（Homogeneous Coordinate）。
标准观察体（canonical view volume, CVV）[投影变换 {% include relref_cnblogs.html %}](https://www.cnblogs.com/mikewolf2002/archive/2012/11/25/2787265.html)
{% include image.html url="/assets/images/210427-a-software-renderer-in-c/361409-20160124194128859-98919634.png" %}

当年还用不了 D3D 和 OGL，开发游戏，做图形实现软件渲染是必备技能，当年机型差，连浮点数都用不了，要用定点数来计算，矩阵稍不注意就越界了。


## 数学基础部分

```cpp
typedef struct Matrix { float m[4][4]; } matrix_t;
typedef struct Vector { float x, y, z, w; } vector_t;
typedef vector_t point_t;

inline int clamp(int x, int min, int max) { return (x < min) ? min : ((x > max) ? max : x); }

// 计算插值：t 为 [0, 1] 之间的数值
inline float interp(float x1, float x2, float t) { return x1 + (x2 - x1) * t; }

// | v |
float vector_length(const vector_t *v);
// z = x + y
void vector_add(vector_t *z, const vector_t *x, const vector_t *y);
// z = x - y
void vector_sub(vector_t *z, const vector_t *x, const vector_t *y);
// 矢量点乘
float vector_dotproduct(const vector_t *x, const vector_t *y);
// 矢量叉乘
void vector_crossproduct(vector_t *z, const vector_t *x, const vector_t *y);
// 矢量插值，t 取值 [0, 1]
void vector_interp(vector_t *z, const vector_t *x1, const vector_t *x2, float t);
// 矢量归一化
void vector_normalize(vector_t *v);

// c = a + b
void matrix_add(matrix_t *c, const matrix_t *a, const matrix_t *b);
// c = a - b
void matrix_sub(matrix_t *c, const matrix_t *a, const matrix_t *b);
// c = a * b
void matrix_mul(matrix_t *c, const matrix_t *a, const matrix_t *b);
// c = a * f
void matrix_scale(matrix_t *c, const matrix_t *a, float f);
// y = x * m
void matrix_apply(vector_t *y, const vector_t *x, const matrix_t *m);
// 单位矩阵
void matrix_set_identity(matrix_t *m);
// 0 矩阵
void matrix_set_zero(matrix_t *m);
// 平移变换
void matrix_set_translate(matrix_t *m, float x, float y, float z);
// 缩放变换
void matrix_set_scale(matrix_t *m, float x, float y, float z);
// 旋转矩阵
void matrix_set_rotate(matrix_t *m, float x, float y, float z, float theta);
// 设置摄像机
void matrix_set_lookat(matrix_t *m, const vector_t *eye, const vector_t *at, const vector_t *up);
// D3DXMatrixPerspectiveFovLH
void matrix_set_perspective(matrix_t *m, float fovy, float aspect, float zn, float zf);
```


## 坐标变换

```cpp
typedef struct Transform {
    matrix_t world;         // 世界坐标变换
    matrix_t view;          // 摄影机坐标变换
    matrix_t projection;    // 投影变换
    matrix_t transform;     // transform = world * view * projection
    float w, h;             // 屏幕大小
} transform_t;

// 矩阵更新，计算 transform = world * view * projection
void transform_update(transform_t *ts);
// 初始化，设置屏幕长宽
void transform_init(transform_t *ts, int width, int height);
// 将矢量 x 进行 project
void transform_apply(const transform_t *ts, vector_t *y, const vector_t *x);
// 检查齐次坐标同 cvv 的边界用于视锥裁剪
int transform_check_cvv(const vector_t *v);
// 归一化，得到屏幕坐标
void transform_homogenize(const transform_t *ts, vector_t *y, const vector_t *x);
```


## 几何计算

几何计算：顶点、扫描线、边缘、矩形、步长计算。

```cpp
typedef struct Color { float r, g, b; } color_t;
typedef struct TexCoord { float u, v; } texcoord_t;
typedef struct Vertex { point_t pos; texcoord_t tc; color_t color; float rhw; } vertex_t;

typedef struct Edge { vertex_t v, v1, v2; } edge_t;
typedef struct Trapezoid { float top, bottom; edge_t left, right; } trapezoid_t;
typedef struct Scanline { vertex_t v, step; int x, y, w; } scanline_t;

void vertex_rhw_init(vertex_t *v);
void vertex_interp(vertex_t *y, const vertex_t *x1, const vertex_t *x2, float t);
void vertex_division(vertex_t *y, const vertex_t *x1, const vertex_t *x2, float w);
void vertex_add(vertex_t *y, const vertex_t *x);

// 根据三角形生成 0-2 个梯形，并且返回合法梯形的数量
int trapezoid_init_triangle(trapezoid_t *trap, const vertex_t *p1, const vertex_t *p2, const vertex_t *p3);
// 按照 Y 坐标计算出左右两条边纵坐标等于 Y 的顶点
void trapezoid_edge_interp(trapezoid_t *trap, float y);
// 根据左右两边的端点，初始化计算出扫描线的起点和步长
void trapezoid_init_scan_line(const trapezoid_t *trap, scanline_t *scanline, int y);
```


## 渲染设备

```cpp
#define RENDER_STATE_WIREFRAME      1        // 渲染线框
#define RENDER_STATE_TEXTURE        2        // 渲染纹理
#define RENDER_STATE_COLOR          4        // 渲染颜色

#define DEVICE_KEYS_SIZE            512

// 渲染设备
struct Device {
    transform_t transform;      // 坐标变换器
    int width;                  // 窗口宽度
    int height;                 // 窗口高度
    UINT32 **framebuffer;       // 像素缓存：framebuffer[y] 代表第 y 行
    float **zbuffer;            // 深度缓存：zbuffer[y] 为第 y 行指针
    UINT32 **texture;           // 纹理：同样是每行索引
    int tex_width;              // 纹理宽度
    int tex_height;             // 纹理高度
    float max_u;                // 纹理最大宽度：tex_width - 1
    float max_v;                // 纹理最大高度：tex_height - 1
    int render_state;           // 渲染状态
    UINT32 background;          // 背景颜色
    UINT32 foreground;          // 线框颜色

public:
    void draw_plane(int a, int b, int c, int d);
    void draw_box(float theta);
    void camera_at_zero(float x, float y, float z);
    void init_texture();

    // 设备初始化，fb 为外部帧缓存，非 NULL 将引用外部帧缓存（每行 4 字节对齐）
    void device_init(int width, int height, void *fb);
    // 删除设备
    void device_destroy(Device *device);
    // 设置当前纹理
    void device_set_texture(void *bits, long pitch, int w, int h);
    // 清空 framebuffer 和 zbuffer
    void device_clear(int mode);
    // 画点
    void device_pixel(int x, int y, UINT32 color);
    // 绘制线段
    void device_draw_line(int x1, int y1, int x2, int y2, UINT32 c);
    // 根据坐标读取纹理
    UINT32 Device_texture_read(float u, float v);

    // 渲染实现
    // 绘制扫描线
    void device_draw_scanline(scanline_t *scanline);
    // 主渲染函数
    void device_render_trap(trapezoid_t *trap);
    // 根据 render_state 绘制原始三角形
    void device_draw_primitive(const vertex_t *v1, const vertex_t *v2, const vertex_t *v3);
};
```


## Win32 窗口

Win32 窗口及图形绘制：为 device 提供一个 DibSection 的 FB。

```cpp
class Window {
    int screen_w, screen_h;
    int screen_mx, screen_my, screen_mb;
    HWND screen_handle;        // 主窗口 HWND
    HDC screen_dc;            // 配套的 HDC
    HBITMAP screen_hb;        // DIB
    HBITMAP screen_ob;        // 老的 BITMAP
    unsigned char *screen_fb;    // frame buffer
    long screen_pitch;

public:
    static int device_exit;
    static int device_keys[DEVICE_KEYS_SIZE];    // 当前键盘按下状态

public:
    Window() {
        screen_mx = 0, screen_my = 0, screen_mb = 0;
        screen_handle = NULL;
        screen_dc = NULL;
        screen_hb = NULL;
        screen_ob = NULL;
        screen_fb = NULL;
        screen_pitch = 0;
        device_exit = 0;
        memset(device_keys, 0, sizeof(int) * DEVICE_KEYS_SIZE);
    }

    int screen_init(int w, int h, const TCHAR *title);    // 屏幕初始化
    int screen_close(void);                                // 关闭屏幕
    void screen_update(void);                            // 显示 FrameBuffer
    unsigned char *getScreenFrameBuffer() { return screen_fb; }

    // win32 event handler
    static LRESULT win_events(HWND, UINT, WPARAM, LPARAM);
    void win_dispatch(void);                            // 处理消息
};
```


## 主程序

```cpp
#include "mini3d.h"
#include "window.h"

#define DEVICE_WIDTH    800
#define DEVICE_HEIGHT   600

int main(void)
{
    TCHAR *title = _T("Mini3d (software render tutorial) - ")
        _T("Left/Right: rotation, Up/Down: forward/backward, Space: switch state");

    Window window;
    if (window.screen_init(DEVICE_WIDTH, DEVICE_HEIGHT, title))
        return -1;

    Device device;
    device.device_init(DEVICE_WIDTH, DEVICE_HEIGHT, window.getScreenFrameBuffer());
    device.camera_at_zero(3, 0, 0);

    device.init_texture();
    device.render_state = RENDER_STATE_TEXTURE;

    int kbhit = 0;
    float theta = 1;
    float pos = 3.5;
    int states[] = { RENDER_STATE_TEXTURE, RENDER_STATE_COLOR, RENDER_STATE_WIREFRAME };
    int indicator = 0;

    while (window.device_exit == 0 && window.device_keys[VK_ESCAPE] == 0) {
        window.win_dispatch(); // 事件分发

        device.device_clear(1);
        device.camera_at_zero(pos, 0, 0);

        if (window.device_keys[VK_UP]) pos -= 0.01f;
        if (window.device_keys[VK_DOWN]) pos += 0.01f;
        if (window.device_keys[VK_LEFT]) theta += 0.01f;
        if (window.device_keys[VK_RIGHT]) theta -= 0.01f;

        if (window.device_keys[VK_SPACE]) {
            if (kbhit == 0) {
                kbhit = 1;
                if (++indicator >= 3) indicator = 0;
                device.render_state = states[indicator];
            }
        } else {
            kbhit = 0;
        }

        device.draw_box(theta);
        window.screen_update();
        Sleep(1);
    }
    return 0;
}
```


## Refers

* [如何开始用 C++ 写一个光栅化渲染器？ {% include relref_zhihu.html %}](https://www.zhihu.com/question/24786878)

* [如何写一个软件渲染器？](http://www.skywind.me/blog/archives/1498)
    * [skywind3000 / mini3d {% include relref_github.html %}](https://github.com/skywind3000/mini3d/blob/master/mini3d.c)

* [为何很多 C++ 开源库都爱自己实现 string？](http://www.skywind.me/blog/archives/2495)

* [游戏服务端架构发展史（上）](http://www.skywind.me/blog/archives/1265)
* [游戏服务端架构发展史（中）](http://www.skywind.me/blog/archives/1301)
* [游戏服务端架构发展史（下）](http://www.skywind.me/blog/archives/1327)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-27-A-software-renderer-in-c.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/mikewolf2002/archive/2012/11/25/2787265.html]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.cnblogs.com/12243d3c.html" %})
- [https://www.zhihu.com/question/24786878]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.zhihu.com/a9c1d5eb.html" %})
- [http://www.skywind.me/blog/archives/1498]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.skywind.me/2dc5685a.html" %})
- [https://github.com/skywind3000/mini3d/blob/master/mini3d.c]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/github.com/ef02bf9f.html" %})
- [http://www.skywind.me/blog/archives/2495]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.skywind.me/788f5a14.html" %})
- [http://www.skywind.me/blog/archives/1265]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.skywind.me/46bc1762.html" %})
- [http://www.skywind.me/blog/archives/1301]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.skywind.me/14e75068.html" %})
- [http://www.skywind.me/blog/archives/1327]({% include relrefx.html url="/backup/2021-04-27-A-software-renderer-in-c.md/www.skywind.me/62cbe657.html" %})
