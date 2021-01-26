---
layout: post
title: "特效编程笔记 -- Windows EGL for OpenGL ES"
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

EGL 是渲染 API（如 OpenGL ES）和原生窗口系统之间的接口。
因此 EGL 被设计出来，作为 OpenGL 和原生窗口系统之间的桥梁。
[doc {% include relref_khronos.html %}](https://www.khronos.org/registry/EGL/sdk/docs/man/html/eglChooseConfig.xhtml)

* **eglBindAPI** Set the current rendering API.
* **eglChooseConfig** return a list of EGL frame buffer configurations that match specified attributes.
    根据指定的 attributes，返回合适的 配置列表。
* **eglCreateContext** create a new EGL rendering context.
    创建一个 EGL 渲染上下文。
* **eglCreateWindowSurface** create a new EGL window surface.
    创建一个 EGL 窗口 surface。
* **eglDestroyContext** destroy an EGL rendering context.
    销毁一个 EGL 渲染上下文。
* **eglDestroySurface** destroy an EGL surface.
    销毁一个 EGL surface。
* **eglGetConfigAttrib** return information about an EGL frame buffer configuration.
    从 EGLConfig 里面获取属性。
* **eglGetConfigs** return a list of all EGL frame buffer configurations for a display.
    根据 一个 display 返回一个 EGL frame buffer configurations。
* **eglGetDisplay** return an EGL display connection.
    获取当前的 EGL display。
* **eglGetError** return error information.
    获取 错误信息。
* **eglInitialize** initialize an EGL display connection.
    初始化。
* **eglMakeCurrent** attach an EGL rendering context to EGL surfaces.
    渲染上下文完成渲染。
    调用 eglMakeCurrent 生成一个当前 context。
    eglMakeCurrent 绑定 ctx 到当前渲染线程，并且画和读 surfaces。
* **eglSwapBuffers** post EGL surface color buffer to a native window.
    post egl surface。
* **eglSwapInterval** specifies the minimum number of video frame periods per buffer swap for the window associated with the current context.
* **eglTerminate** terminate an EGL display connection.


## 确定可用的 Surface 的配置

一旦初始化了 EGL，就可以确定可用渲染表面的类型和配置了。有两种方法：
* 先使用 eglGetConfigs 查询每个配置，再使用 eglGetConfigAttrib 找出最好的选择。
* 指定一组需求，使用 eglChooseChofig 让 EGL 推荐最佳配置。

```cpp
// 初始化
EGLBoolean eglInitialize(EGLDisplay display, // 创建步骤时返回的对象
                         EGLint *majorVersion, // 返回 EGL 主版本号
                         EGLint *minorVersion); // 返回 EGL 次版本号
// 获取所有配置的函数
EGLBoolean eglGetConfigs(EGLDisplay display, // 指定显示的连接
                         EGLConfig *configs, // 指定 GLConfig 列表
                         EGLint maxReturnConfigs, // 最多返回的 GLConfig 数
                         EGLint *numConfigs); // 实际返回的 GLConfig 数
// 查询 EGLConfig 配置
EGLBoolean eglGetConfigAttrib(EGLDisplay display, // 指定显示的连接
                              EGLConfig config, // 指定要查询的 GLConfig
                              EGLint attribute, // 返回特定属性
                              EGLint *value); // 返回值
// 让 EGL 选择配置
EGLBoolean eglChooseChofig(EGLDispay display, // 指定显示的连接
                           const EGLint *attribList, // 指定 configs 匹配的属性列表，可以为 NULL
                           EGLConfig *config,   // 调用成功，返会符合条件的 EGLConfig 列表
                           EGLint maxReturnConfigs, // 最多返回的符合条件的 GLConfig 数
                           ELGint *numConfigs );  // 实际返回的符合条件的 EGLConfig 数
// 创建渲染区域 Surface
EGLSurface eglCreateWindowSurface(EGLDisplay display, // 指定显示的连接
                                  EGLConfig config, // 符合条件的 EGLConfig
                                  EGLNatvieWindowType window, // 指定原生窗口
                                  const EGLint *attribList); // 指定窗口属性列表，可为 NULL
// 创建上下文
EGLContext eglCreateContext(EGLDisplay display, // 指定显示的连接
                            EGLConfig config, // 前面选好的 EGLConfig
                            EGLContext shareContext, // 允许其它 EGLContext 共享数据，使用 EGL_NO_CONTEXT 表示不共享
                            const EGLint* attribList); // 指定操作的属性列表，只能接受一个属性 EGL_CONTEXT_CLIENT_VERSION

// 关联上下文
EGLBoolean eglMakeCurrent(EGLDisplay display, // 指定显示的连接
                          EGLSurface draw, // EGL 绘图表面
                          EGLSurface read, // EGL 读取表面
                          EGLContext context); // 指定连接到该表面的上下文
```


## wWinMain

```cpp
int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPWSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
    CELLWinApp app(hInstance);
    app.main(800, 600);
    return 0;
```


## CELLWinApp.h

```cpp
#pragma once

#include <Windows.h>
#include <tchar.h>
#include <stdio.h>

#include <EGL/egl.h>
#include <gles2/gl2.h>

class CELLWinApp
{
public:
    CELLWinApp(HINSTANCE inst) {
        m_hInstance = inst;
        m_hWnd = nullptr;

        m_config = nullptr;
        m_display = EGL_NO_DISPLAY;
        m_context = EGL_NO_CONTEXT;
        m_surface = EGL_NO_SURFACE;

        m_width = m_height = 0;

        WNDCLASSEX  winClass;
        winClass.lpszClassName = _T("CELLWinApp");
        winClass.cbSize = sizeof(winClass);
        winClass.style = CS_HREDRAW | CS_VREDRAW | CS_OWNDC;
        winClass.lpfnWndProc = lpfnWndProc;
        winClass.hInstance = m_hInstance;
        winClass.hIcon = 0;
        winClass.hIconSm = 0;
        winClass.hCursor = LoadCursor(m_hInstance, IDC_ARROW);
        winClass.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
        winClass.lpszMenuName = NULL;
        winClass.cbClsExtra = 0;
        winClass.cbWndExtra = 0;
        RegisterClassEx(&winClass);
    }
    virtual ~CELLWinApp() {
        UnregisterClass(_T("CELLWinApp"), m_hInstance);
    }

    int main(int width, int height);

private:
    bool initGLES();
    void destroyGLES();

protected:

    static LRESULT CALLBACK lpfnWndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);

    virtual void render();
    virtual LRESULT onEvent(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam);

private:
    HINSTANCE m_hInstance;
    HWND m_hWnd;
    // for gles 2.0
    EGLConfig  m_config;
    EGLSurface m_surface;
    EGLContext m_context;
    EGLDisplay m_display;

    int m_width;
    int m_height;
};
```


## CELLWinApp.cpp

```cpp
#include "CELLWinApp.h"
#include <tchar.h>
#include <stdio.h>

#include <EGL/egl.h>
#include <gles2/gl2.h>

int CELLWinApp::main(int width, int height) {
    m_hWnd = CreateWindowEx(NULL, // dwExStyle
        _T("CELLWinApp"), // lpClassName
        _T("CELLWinApp"), // lpWindowName
        WS_OVERLAPPEDWINDOW, // dwStyle
        CW_USEDEFAULT, // X
        CW_USEDEFAULT, // Y
        width, // nWidth
        height, // nHeight
        NULL, // hWndParent
        NULL, // hMenu
        m_hInstance, // hInstance
        this // lpParam
    );
    if (m_hWnd == 0) {
        return -1;
    }

    ShowWindow(m_hWnd, SW_SHOW);
    if (!initGLES()) {
        return  -2;
    }

    MSG msg = { 0 };
    while (msg.message != WM_QUIT)
    {
        if (msg.message == WM_DESTROY ||
            msg.message == WM_CLOSE)
        {
            break;
        }
        /**
        * 有消息，处理消息，无消息，则进行渲染绘制。
        */
        if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        } else {
            render();
            eglSwapBuffers(m_display, m_surface);
            Sleep(1);
        }
    }

    destroyGLES();
    return  0;
}

void CELLWinApp::render()
{
    glClearColor(1, 0, 0, 1);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glViewport(0, 0, m_width, m_height);
}

bool CELLWinApp::initGLES() {
    const EGLint attribs[] =
    {
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_OPENGL_ES2_BIT,
        EGL_BLUE_SIZE, 8,
        EGL_GREEN_SIZE, 8,
        EGL_RED_SIZE, 8,
        EGL_DEPTH_SIZE,24,
        EGL_NONE
    };

    m_display = eglGetDisplay(EGL_DEFAULT_DISPLAY);

    EGLint major;
    EGLint minor;
    eglInitialize(m_display, &major, &minor);

    EGLint numConfigs(0);
    eglChooseConfig(m_display, attribs, &m_config, 1, &numConfigs);

    EGLint format(0);
    eglGetConfigAttrib(m_display, m_config, EGL_NATIVE_VISUAL_ID, &format);

    m_surface = eglCreateWindowSurface(m_display, m_config, m_hWnd, NULL);
    EGLint attr[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE, EGL_NONE };
    m_context = eglCreateContext(m_display, m_config, 0, attr);

    if (eglMakeCurrent(m_display, m_surface, m_surface, m_context) == EGL_FALSE) {
        return false;
    }
    eglQuerySurface(m_display, m_surface, EGL_WIDTH, &m_width);
    eglQuerySurface(m_display, m_surface, EGL_HEIGHT, &m_height);
    return true;
}

void CELLWinApp::destroyGLES() {
    if (m_display != EGL_NO_DISPLAY) {
        eglMakeCurrent(m_display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
        if (m_context != EGL_NO_CONTEXT) {
            eglDestroyContext(m_display, m_context);
        }
        if (m_surface != EGL_NO_SURFACE) {
            eglDestroySurface(m_display, m_surface);
        }
        eglTerminate(m_display);
    }
    m_display = EGL_NO_DISPLAY;
    m_context = EGL_NO_CONTEXT;
    m_surface = EGL_NO_SURFACE;
}

LRESULT CELLWinApp::onEvent(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch (msg)
    {
    case WM_CHAR:
        char szChar[20];
        sprintf_s(szChar, 20, "char code is %d", wParam);
        MessageBoxA(hWnd, szChar, "char", 0);
        break;
    case WM_LBUTTONDOWN:
        MessageBoxA(hWnd, "mouse clicked", "message", 0);
        break;
    case WM_CLOSE:
    case WM_DESTROY:
    {
        ::PostQuitMessage(0);
    }
    break;
    case WM_MOUSEMOVE:
        break;
    default:
        return  DefWindowProc(hWnd, msg, wParam, lParam);
    }
    return  S_OK;

}

LRESULT CALLBACK CELLWinApp::lpfnWndProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    CELLWinApp* pThis = (CELLWinApp*)GetWindowLong(hWnd, GWL_USERDATA);
    if (pThis) {
        return  pThis->onEvent(hWnd, msg, wParam, lParam);
    }
    if (WM_CREATE == msg)
    {
        CREATESTRUCT* pCreate = (CREATESTRUCT*)lParam;
        SetWindowLong(hWnd, GWL_USERDATA, (DWORD_PTR)pCreate->lpCreateParams);
    }
    return  DefWindowProc(hWnd, msg, wParam, lParam);
}
```


## 另外一个完整的例子

{% include image.html url="/assets/images/210126-shader-windows-opengles~f7/eglexample.webp" %}

```cpp
#include "stdafx.h"
#include <iostream>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <EGL/egl.h>
#include <EGL/eglplatform.h>
#include <GLES2/gl2.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>

using namespace std;

const GLchar* vertexShaderSource[] = {
    "uniform mat4 uMVPMatrix;\n"
    "attribute vec4 aPosition;\n"
    "attribute vec2 aTexCoord;\n"
    "varying vec2 vTexCoord;\n"
    "void main() {\n"
        "gl_Position = uMVPMatrix * aPosition;\n"
        "vTexCoord = aTexCoord;\n"
    "}\n"
};

const GLchar* fragmentShaderSource[] = {
    "#extension GL_OES_EGL_image_external : require\n"
    "precision mediump float;\n"
    "uniform sampler2D sTexture;\n"
    "varying vec2 vTexCoord;\n"
    "void main() {\n"
        "gl_FragColor = vec4(abs(vTexCoord.s), abs(vTexCoord.t), 1.0, 1.0);\n"
    "}\n"
};

float cubeVertices[] = {
    -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, -1, 1, 1, 1, -1, 1, -1, -1,
    1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1,
    -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1,
    -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1,
    1, -1, -1, -1, 1, 1,
    -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1
};

float cubeTexCoords[] = {
    0, 0, 1, 0, 0, 1, 1, 1,
    0, 1, 0, 0, 1, 1, 1, 0,
    0, 0, 1, 0, 0, 1, 1, 1,
    0, 1, 0, 0, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 1, 1, 0,
    1, 0, 0, 0,
    0, 0, 1, 0, 0, 1, 1, 1
};

struct ShaderHandles {
    GLuint aPosition;
    GLuint aTexCoord;
    GLuint mvMatrix;
    GLuint mvpMatrix;
};

struct Matrices {
    glm::mat4x4 modelView;
    glm::mat4x4 modelViewProjection;
};

glm::vec3 rotation;

GLuint shader;
ShaderHandles shaderHandles;
Matrices matrices;

bool quit = false;

int winWidth = 640;
int winHeight = 360;

LONGLONG qpcFrequency;
double timeFactor = .1f;

inline float deg_to_rad(float rad) {
    return rad * float(M_PI / 180);
}

LRESULT CALLBACK wndProc(HWND hwnd, unsigned int msg, WPARAM wParam, LPARAM lParam)
{
    switch (msg)
    {
    case WM_CLOSE: {
        quit = true;
        DestroyWindow(hwnd);
        PostQuitMessage(0);
        return 0;
    }
    case WM_SIZE: {
        winWidth = LOWORD(lParam);
        winHeight = HIWORD(lParam);
        return 0;
    }
    }

    return (DefWindowProc(hwnd, msg, wParam, lParam));
}

HWND createWindow(int width, int height) {
    HINSTANCE hInstance = GetModuleHandle(NULL);
    WNDCLASSEX wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);
    wcex.style = CS_OWNDC;
    wcex.lpfnWndProc = &DefWindowProc;
    wcex.cbClsExtra = 0;
    wcex.cbWndExtra = 0;
    wcex.hInstance = hInstance;
    wcex.hIcon = NULL;
    wcex.hCursor = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground = 0;
    wcex.lpszMenuName = NULL;
    wcex.lpszClassName = L"eglsamplewnd";
    wcex.hIconSm = NULL;
    wcex.lpfnWndProc = wndProc;

    RegisterClassEx(&wcex);
    RECT rect = { 0, 0, width, height };
    int style = WS_BORDER | WS_CAPTION | WS_SYSMENU | WS_THICKFRAME;
    AdjustWindowRect(&rect, style, FALSE);

    HWND hwnd = CreateWindow(L"eglsamplewnd", L"EGL OpenGL ES 2.0 example", style, CW_USEDEFAULT, CW_USEDEFAULT, rect.right - rect.left, rect.bottom - rect.top, NULL, NULL, GetModuleHandle(NULL), NULL);
    ShowWindow(hwnd, SW_SHOW);

    return hwnd;
}

GLuint compileShaders(const GLchar** vertexShaderSource, const GLchar** fragmentShaderSource)
{
    //Compile vertex shader
    GLuint vertexShader(glCreateShader(GL_VERTEX_SHADER));
    glShaderSource(vertexShader, 1, vertexShaderSource, NULL);
    glCompileShader(vertexShader);
    int logLength;
    glGetShaderiv(vertexShader, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar* strInfoLog = new GLchar[logLength + 1];
        glGetShaderInfoLog(vertexShader, logLength, NULL, strInfoLog);
        cout << "vertex shader error log:\n" << strInfoLog << "\n";
    };

    //Compile fragment shader
    GLuint fragmentShader(glCreateShader(GL_FRAGMENT_SHADER));
    glShaderSource(fragmentShader, 1, fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);
    glGetShaderiv(fragmentShader, GL_INFO_LOG_LENGTH, &logLength);
    if (logLength > 0) {
        GLchar* strInfoLog = new GLchar[logLength + 1];
        glGetShaderInfoLog(fragmentShader, logLength, NULL, strInfoLog);
        cout << "fragment shader error log:\n" << strInfoLog << "\n";
    };

    //Link vertex and fragment shader together
    GLuint program(glCreateProgram());
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);

    //Delete shaders objects
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);
    return program;
}

void glErrorLog() {
    GLuint glError = glGetError();
    if (glError != GL_NO_ERROR) {
        cout << "OpenGL Error : " << glError << "\n";
    }
}

void initScene() {
    QueryPerformanceCounter((LARGE_INTEGER*)&qpcFrequency);

    glEnable(GL_DEPTH_TEST);
    glClearColor(0.0f, 0.0f, 0.2f, 1.0f);

    rotation = glm::vec3(15.0, 45.0, 0.0);

    shader = compileShaders(vertexShaderSource, fragmentShaderSource);
    glUseProgram(shader);

    shaderHandles.aPosition = glGetAttribLocation(shader, "aPosition");
    shaderHandles.aTexCoord = glGetAttribLocation(shader, "aTexCoord");

    shaderHandles.mvpMatrix = glGetUniformLocation(shader, "uMVPMatrix");
    shaderHandles.mvMatrix = glGetUniformLocation(shader, "uMVMatrix");

    glVertexAttribPointer(shaderHandles.aPosition, 3, GL_FLOAT, false, 0, &cubeVertices);
    glVertexAttribPointer(shaderHandles.aTexCoord, 2, GL_FLOAT, false, 0, &cubeTexCoords);
    glEnableVertexAttribArray(shaderHandles.aPosition);
    glEnableVertexAttribArray(shaderHandles.aTexCoord);
}

void renderScene(double timeFactor) {
    glViewport(0, 0, winWidth, winHeight);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    matrices.modelView = glm::mat4(1.0);
    matrices.modelView = glm::translate(matrices.modelView, glm::vec3(0.0f, 0.0f, -6.0f));
    matrices.modelView = glm::rotate(matrices.modelView, deg_to_rad(rotation.x), glm::vec3(1.0f, 0.0f, 0.0f));
    matrices.modelView = glm::rotate(matrices.modelView, deg_to_rad(rotation.y), glm::vec3(0.0f, 1.0f, 0.0f));

    matrices.modelViewProjection = glm::perspective(45.0f, (float)winWidth / (float)winHeight, 0.1f, 100.0f) * matrices.modelView;

    glUniformMatrix4fv(shaderHandles.mvpMatrix, 1, false, &matrices.modelViewProjection[0][0]);
    glUniformMatrix4fv(shaderHandles.mvMatrix, 1, false, &matrices.modelView[0][0]);

    glDrawArrays(GL_TRIANGLE_STRIP, 0, 26);
    glErrorLog();

    rotation.y += (rotation.y < 360.0) ? timeFactor : -360.0f + timeFactor;
}

void outputGLESInfo() {
    cout << "GL_VENDOR = " << glGetString(GL_VENDOR) << "\n";
    cout << "GL_RENDERER = " << glGetString(GL_RENDERER) << "\n";
    cout << "GL_VERSION = " << glGetString(GL_VERSION) << "\n";
    cout << "GL_SHADING_LANGUAGE_VERSION = " << glGetString(GL_SHADING_LANGUAGE_VERSION) << "\n";
    cout << "Extensions :\n";
    string extBuffer;
    stringstream extStream;
    extStream << glGetString(GL_EXTENSIONS);
    while (extStream >> extBuffer) {
        cout << extBuffer << "\n";
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
    HWND hwnd = createWindow(winWidth, winHeight);
    HDC hdc = GetDC(hwnd);

    EGLDisplay eglDisplay = eglGetDisplay(hdc);
    if (eglDisplay == EGL_NO_DISPLAY) {
        cout << "Could not get egl display!" << endl;
        return 1;
    }

    EGLint eglVersionMajor, eglVersionMinor;
    eglInitialize(eglDisplay, &eglVersionMajor, &eglVersionMinor);
    eglBindAPI(EGL_OPENGL_ES_API);

    EGLint configAttributes[] =
    {
        EGL_RED_SIZE, 8,
        EGL_GREEN_SIZE, 8,
        EGL_BLUE_SIZE, 8,
        EGL_DEPTH_SIZE, 24,
        EGL_RENDERABLE_TYPE, EGL_WINDOW_BIT | EGL_OPENGL_ES2_BIT,
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_OPENGL_ES2_BIT,
        EGL_NONE
    };

    EGLint surfaceAttributes[] = { EGL_NONE };
    EGLint contextAttributes[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE };

    EGLint nrOfConfigs;
    EGLConfig windowConfig;
    eglChooseConfig(eglDisplay, configAttributes, &windowConfig, 1, &nrOfConfigs);
    EGLSurface eglSurface = eglCreateWindowSurface(eglDisplay, windowConfig, hwnd, surfaceAttributes);
    if (eglSurface == EGL_NO_SURFACE) {
        // http://docs.neomades.com/en/current/GenericAPI/reference/javax/microedition/khronos/egl/EGL10.html
        // public static final int EGL_BAD_CONFIG
        // EGL error code indicating 'bad config'.
        // Constant Value : 12293 (0x00003005)
        cerr << "Could not create EGL surface : " << eglGetError() << endl;
        return 1;
    }

    EGLContext eglContext = eglCreateContext(eglDisplay, windowConfig, NULL, contextAttributes);

    if (eglContext == EGL_NO_CONTEXT) {
        cout << "Could not create egl context : " << eglGetError() << endl;
        return 1;
    }

    cout << "EGL Version = " << eglQueryString(eglDisplay, EGL_VERSION) << "\n";
    cout << "EGL Vendor = " << eglQueryString(eglDisplay, EGL_VENDOR) << "\n";
    cout << "EGL Client APIs : \n" << eglQueryString(eglDisplay, EGL_CLIENT_APIS) << "\n";
    cout << "EGL Extensions : \n" << eglQueryString(eglDisplay, EGL_EXTENSIONS) << "\n";

    cout << "EGL Configurations:\n";

    EGLConfig* eglConfigs;
    int eglNumConfigs;
    eglGetConfigs(eglDisplay, NULL, 0, &eglNumConfigs);
    eglConfigs = new EGLConfig[eglNumConfigs];

    for (int i = 0; i < eglNumConfigs; i++) {
        cout << "Config " << i << "\n";
        cout << "Supported APIs :\n";
        int eglRenderable;
        eglGetConfigAttrib(eglDisplay, eglConfigs[i], EGL_RENDERABLE_TYPE, &eglRenderable);
        if (eglRenderable & EGL_OPENGL_ES_BIT) cout << "OPENGL ES" << "\n";
        if (eglRenderable & EGL_OPENGL_ES2_BIT) cout << "OPENGL ES2" << "\n";
        if (eglRenderable & EGL_OPENVG_BIT) cout << "OPENVG" << "\n";
        if (eglRenderable & EGL_OPENGL_BIT) cout << "OPENGL" << "\n";
        cout << "\n";
    }

    EGLint attr[] = {
        EGL_BLUE_SIZE, 8,
        EGL_GREEN_SIZE, 8,
        EGL_RED_SIZE, 8,
        EGL_DEPTH_SIZE, 24,
        EGL_RENDERABLE_TYPE, EGL_WINDOW_BIT | EGL_OPENGL_ES2_BIT,
        EGL_SURFACE_TYPE, EGL_WINDOW_BIT | EGL_OPENGL_ES2_BIT,
        EGL_NONE
    };

    EGLConfig* eglConfig = new EGLConfig;
    int elgNumConfig;
    if (!eglChooseConfig(eglDisplay, attr, eglConfig, sizeof(eglConfig), &eglNumConfigs)) {
        cout << "Could not get valid egl configuration!" << endl;
        return 1;
    }

    eglMakeCurrent(eglDisplay, eglSurface, eglSurface, eglContext);
    outputGLESInfo();
    initScene();

    // Render loop
    MSG uMsg;
    PeekMessage(&uMsg, NULL, 0, 0, PM_REMOVE);

    LONGLONG qpcStart, qpcEnd;

    while (!quit) {

        QueryPerformanceCounter((LARGE_INTEGER*)&qpcStart);
        renderScene(timeFactor);

        while (PeekMessage(&uMsg, NULL, 0, 0, PM_REMOVE) > 0) {
            TranslateMessage(&uMsg);
            DispatchMessage(&uMsg);
        }

        if (quit) {
            break;
        }

        eglSwapBuffers(eglDisplay, eglSurface);
        QueryPerformanceCounter((LARGE_INTEGER*)&qpcEnd);
        double dTime = (double)(qpcEnd - qpcStart) / (double)qpcFrequency;
        timeFactor += dTime * 0.01f;
    }

    if (true) {
        eglMakeCurrent(eglDisplay, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
        if (eglContext != EGL_NO_CONTEXT) {
            eglDestroyContext(eglDisplay, eglContext);
        }
        if (eglSurface != EGL_NO_SURFACE) {
            eglDestroySurface(eglDisplay, eglSurface);
        }
        eglTerminate(eglDisplay);
    }
    return 0;
}
```


## Refs

- [1] [Using OpenGL ES on windows desktops via EGL](https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/)
- [2] [GLES：不同平台下面 EGL 的使用 {% include relref_github.html %}](https://github.com/havenow/OpenGLES)
- [3] [OpenGLES / 简单的使用 EGL.md {% include relref_github.html %}](https://github.com/havenow/OpenGLES/blob/master/%E7%AE%80%E5%8D%95%E7%9A%84%E4%BD%BF%E7%94%A8EGL.md)
- [4] [Introduce some smooth and free android emulator for develop. （开发神器 — 一些免费流畅的 Android 模拟器） {% include relref_github.html %}](https://github.com/havenow/Android-Smooth-Emulator-for-Develop)
- [5] [EGL 介绍和使用 {% include relref_csdn.html %}](https://blog.csdn.net/afei__/article/details/84867104)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-01-26-shader-windows-opengles-egl.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.khronos.org/registry/EGL/sdk/docs/man/html/eglChooseConfig.xhtml]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/www.khronos.org/97f7cafc.xhtml" %})
- [http://docs.neomades.com/en/current/GenericAPI/reference/javax/microedition/khronos/egl/EGL10.html]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/docs.neomades.com/a1c25f33.html" %})
- [https://www.saschawillems.de/blog/2015/04/19/using-opengl-es-on-windows-desktops-via-egl/]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/www.saschawillems.de/5efcfffd.html" %})
- [https://github.com/havenow/OpenGLES]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/github.com/82a2418c.html" %})
- [https://github.com/havenow/OpenGLES/blob/master/%E7%AE%80%E5%8D%95%E7%9A%84%E4%BD%BF%E7%94%A8EGL.md]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/github.com/ad2ee01a.md" %})
- [https://github.com/havenow/Android-Smooth-Emulator-for-Develop]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/github.com/9a266167.html" %})
- [https://blog.csdn.net/afei__/article/details/84867104]({% include relref.html url="/backup/2021-01-26-shader-windows-opengles-egl.md/blog.csdn.net/c9956269.html" %})
