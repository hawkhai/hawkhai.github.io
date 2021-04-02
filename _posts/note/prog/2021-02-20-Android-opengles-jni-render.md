---
layout: post
title: "编程 C++ -- Android OpenGL ES 渲染 Java & C++ JNI 实现原理"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程", "C++", "Android"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

> 寂寞啦，怀念小时候的胡同和弄堂啦，怎么办呢？就坐飞机去那些柯布西耶的科学还没照耀到的偏远古镇，旅游一下。


## Android JNI OpenGL ES -- eglCreateWindowSurface

需要 Java 代码 和 C++ 代码协作，完成渲染，渲染的关键部分需要在 C++ 3D 引擎里面完成，这就需要用 egl 来粘连 Java & C++ 代码。


### 现象

Java 端 `MagicSurfaceView extends SurfaceView`。
开始的时候采用 `GLSurfaceView`，然后 C++ 端创建 Window 会失败。因为 `GLSurfaceView` 已经默认创建了一个，不能重复创建。

正确的做法是：

```java
Surface surface = getHolder().getSurface();
AssetManager assetmgr = getContext().getAssets();
DisplayMetrics metrics = getResources().getDisplayMetrics();
IrrlichtJNI.nativeInitGL(surface, assetmgr, metrics, getWidth(), getHeight());
```

然后 C++ 端拿到 surface 对象后，

```cpp
#include <android/native_window_jni.h>
#include <android/native_window.h>

AAssetManager *assetManager = AAssetManager_fromJava(env, assetmgr);
ANativeWindow *window = ANativeWindow_fromSurface(env, surface); // 创建 window 对象
...
eglCreateWindowSurface...
// nativeWindow 不用了要释放
ANativeWindow *nativeWindow = gdevice->getANativeWindow();
ANativeWindow_release(nativeWindow);
```

现在的问题是，Irrlicht 崩溃了，崩溃的很突然，还莫名其妙：

```cpp
bool CEGLManager::generateSurface() {
    if (EglDisplay == EGL_NO_DISPLAY)
        return false;

    if (EglSurface != EGL_NO_SURFACE)
        return true;

    // We should assign new WindowID on platforms, where WindowID may change at runtime,
    // at this time only Android support this feature.
    // this needs an update method instead!

#if defined(_IRR_COMPILE_WITH_ANDROID_DEVICE_)
    EglWindow = (ANativeWindow*) Data.OGLESAndroid.Window;
#endif

#if defined(_IRR_EMSCRIPTEN_PLATFORM_)
    // eglChooseConfig is currently only implemented as stub in emscripten (version 1.37.22 at point of writing)
    // But the other solution would also be fine as it also only generates a single context so there is not much to choose from.
    EglConfig = chooseConfig(ECS_IRR_CHOOSE);
#else
    EglConfig = chooseConfig(ECS_EGL_CHOOSE_FIRST_LOWER_EXPECTATIONS);
#endif

    if ( EglConfig == 0 ) {
        os::Printer::log("Could not get config for EGL display.");
        return false;
    }

#if defined(_IRR_COMPILE_WITH_ANDROID_DEVICE_)
    EGLint Format = 0;
    eglGetConfigAttrib(EglDisplay, EglConfig, EGL_NATIVE_VISUAL_ID, &Format);

    ANativeWindow_setBuffersGeometry(EglWindow, 0, 0, Format);
#endif

    // Now we are able to create EGL surface.
    EglSurface = eglCreateWindowSurface(EglDisplay, EglConfig, EglWindow, 0);

    if (EGL_NO_SURFACE == EglSurface)
        EglSurface = eglCreateWindowSurface(EglDisplay, EglConfig, 0, 0);

    if (EGL_NO_SURFACE == EglSurface)
        os::Printer::log("Could not create EGL surface.");

#ifdef EGL_VERSION_1_2
    if (MinorVersion > 1)
        eglBindAPI(EGL_OPENGL_ES_API);
#endif

    if (Params.Vsync)
        eglSwapInterval(EglDisplay, 1);

    return true;
}

bool CEGLManager::activateContext(const SExposedVideoData& videoData, bool restorePrimaryOnZero) {
    if (!bEglMakeCurrent) {
        // 成功调用一次就可以了，频繁调用 Adreno 貌似容易崩溃。
        eglMakeCurrent(EglDisplay, EglSurface, EglSurface, EglContext);
        bEglMakeCurrent = eglGetError() == EGL_SUCCESS;
    }
    if (testEGLError()) {
        os::Printer::log("Could not make EGL context current.");
        return false;
    }
    return true;
}
```

Ogre 崩溃也崩溃了：

```cpp
// RenderingAPIException: Fail to create EGLSurface based on NativeWindowType
// in createSurfaceFromWindow at RenderSystems/GLSupport/src/EGL/OgreEGLWindow.cpp (line 217)
// Ogre::Exception::ERR_RENDERINGAPI_ERROR
::EGLSurface EGLWindow::createSurfaceFromWindow(::EGLDisplay display, NativeWindowType win) {
    ::EGLSurface surface;
    surface = eglCreateWindowSurface(display, mEglConfig, (EGLNativeWindowType) win, NULL);
    EGL_CHECK_ERROR
    if (surface == EGL_NO_SURFACE) {
        OGRE_EXCEPT(Exception::ERR_RENDERINGAPI_ERROR,
                    "Fail to create EGLSurface based on NativeWindowType");
    }
    return surface;
}

void EGLWindow::swapBuffers() {
    if (mClosed || mIsExternalGLControl) {
        return;
    }
    if (eglSwapBuffers(mEglDisplay, mEglSurface) == EGL_FALSE) {
        EGL_CHECK_ERROR
        OGRE_EXCEPT(Exception::ERR_RENDERINGAPI_ERROR, "Fail to SwapBuffers");
    }
}
```


### 解决

* `eglCreateWindowSurface` 为啥会崩溃呢？研究发现参数 win 为空，那 win 为什么为空呢？
* 然后发现 `ANativeWindow_fromSurface` 返回了空？这个为什么返回空呢？
* 思来想去，最后发现是因为 Java 端传入的 surface 还没有初始化完成造成的。

```java
public class IrrlichtGLView extends SurfaceView implements SurfaceHolder.Callback {

    private boolean firstTime = true;
    private boolean windowready = false;

    public IrrlichtGLView(Context context) {
        super(context);
        getHolder().addCallback(this);
    }

    public IrrlichtGLView(Context context, AttributeSet attrs) {
        super(context, attrs);
        getHolder().addCallback(this);
    }

    public IrrlichtGLView(Context context, AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);
        getHolder().addCallback(this);
    }

    public void onDrawFrame() {
        if (!windowready) {
            return;
        }
        // render a frame
        if (firstTime) {
            Surface surface = getHolder().getSurface();
            AssetManager assetmgr = getContext().getAssets();
            DisplayMetrics metrics = getResources().getDisplayMetrics();
            IrrlichtJNI.nativeInitGL(surface, assetmgr, metrics, getWidth(), getHeight());
            firstTime = false;
        }
        IrrlichtJNI.nativeDrawIteration();
    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        windowready = true;
    }

    @Override
    public void surfaceChanged(SurfaceHolder holder, int i, int j, int k) {
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {
    }
}
```


### 启示

* **不要动不动就怀疑引擎有 bug，人家的代码既工整又优美，先多从自身找找原因。**开始的时候，因为 bug 本身若隐若现（小概率出现），疑惑这里疑惑那里，还怀疑人家引擎，也没多思考。
* 崩溃的位置不一定是出问题的位置，可以从参数问题上顺藤摸瓜，直到找到真正的原因。崩溃在 C++，最后改在 Java。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relrefx.html url="/assets/reviewjs/blogs/2021-02-20-Android-opengles-jni-render.md.js" %}'></script></p>
