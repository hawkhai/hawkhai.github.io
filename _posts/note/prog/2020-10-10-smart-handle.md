---
layout: post
title: "编程与调试 C++ -- 利用 C++ 类生命周期，自动释放 HANDLE 句柄，打造可重入锁"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

利用 C++ 类生命周期，自动释放 HANDLE 句柄，香。


## Windows 版本

```cpp
template<typename T = HANDLE, BOOL (__stdcall *Closer)(T) = ::CloseHandle>
class SmartHandleTmpl
{
    SmartHandleTmpl(const SmartHandleTmpl&);
    SmartHandleTmpl& operator=(const SmartHandleTmpl&);

public:
    SmartHandleTmpl(T handle = NULL) : m_handle(handle) { }
    virtual ~SmartHandleTmpl() {
        if (m_handle && m_handle != INVALID_HANDLE_VALUE) {
            Closer(m_handle);
        }
    }

    operator T() const { return m_handle; }
    template<typename F>
    operator F*() const { return (F*) m_handle; }
    T* operator&() { return &m_handle; }
    T operator=(T handle) {
        if (m_handle != handle && m_handle && m_handle != INVALID_HANDLE_VALUE) {
            Closer(m_handle);
        }
        return m_handle = handle;
    }

private:
    T m_handle;
};

typedef SmartHandleTmpl<> SmartHandle;
// SmartHandleTmpl<HANDLE, ::FindClose>
// SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
// 打印机：
// SmartHandleTmpl<HANDLE, ::ClosePrinter>
```

另外两个就是：

```cpp
SmartHandleTmpl<HANDLE, ::FindClose>
SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
SmartHandleTmpl<HANDLE, ::ClosePrinter>
```

同样的原理，可以构建临界区锁：

```cpp
class SmartCriticalSection
{
public:
    SmartCriticalSection() { ::InitializeCriticalSection(&m_sesion); }
    virtual ~SmartCriticalSection() { ::DeleteCriticalSection(&m_sesion); }

    void Lock(void) { ::EnterCriticalSection(&m_sesion); }
    void Unlock(void) { ::LeaveCriticalSection(&m_sesion); };

private:
    CRITICAL_SECTION m_sesion;
};

// 类创建成员：SmartCriticalSection m_csection;
// 成员函数就可以用了：SmartLocker temp(m_csection);
// 要注意的就是，不要 TerminateThread / ExitThread 之类的，可能造成死锁。
class SmartLocker
{
public:
    SmartLocker(SmartCriticalSection& csection) : m_csection(csection) { m_csection.Lock(); }
    virtual ~SmartLocker(){ m_csection.Unlock(); }
private:
    SmartCriticalSection& m_csection;
};
```

类创建成员：`SmartCriticalSection m_csection;` 成员函数就可以用了：`SmartLocker temp(m_csection);`。要注意的就是，不要 `TerminateThread` / `ExitThread` 之类的，可能造成死锁。

```cpp
template <typename T>
std::string to_string(T value)
{
    std::ostringstream os;
    os << value;
    return os.str();
}
```


## Android 版本

Android C++ 中线程同步实现
<https://blog.csdn.net/wzy_1988/article/details/46620113>

```cpp
class Mutex {
public:
    enum {
        PRIVATE = 0,
        SHARED = 1
    };

    Mutex();
    Mutex(const char* name);
    Mutex(int type, const char* name = NULL);
    ~Mutex();

    // lock or unlock the mutex
    status_t lock();
    void unlock();

    // lock if possible; returns 0 on success, error otherwise
    status_t tryLock();

    class Autolock {
    public:
        inline Autolock(Mutex& mutex) : mLock(mutex)  { mLock.lock(); }
        inline Autolock(Mutex* mutex) : mLock(*mutex) { mLock.lock(); }
        inline ~Autolock() { mLock.unlock(); }
    private:
        Mutex& mLock;
    };
private:
    pthread_mutex_t mMutex;
};

inline Mutex::Mutex() {
    // 构造函数，初始化 mMutex 变量
    pthread_mutex_init(&mMutex, NULL);
}
inline Mutex::~Mutex() {
    // 析构函数，就是销毁 mMutex 变量
    pthread_mutex_destory(&mMutex);
}

inline status_t Mutex::lock() {
    return pthread_mutex_lock(&mMutex);
}

inline void Mutex::unlock() {
    pthread_mutex_unlock(&mMutex);
}

inline status_t Mutex::tryLock() {
    return pthread_mutex_tryLock(&mMutex);
}

typedef Mutex::Autolock AutoMutex;
class Autolock {
public:
    inline Autolock(Mutex& mutex) : mLock(mutex)  { mLock.lock(); }
    inline Autolock(Mutex* mutex) : mLock(*mutex) { mLock.lock(); }
    inline ~Autolock() { mLock.unlock(); }
private:
    Mutex& mLock;
};

Mutex gProcessMutex;
void testAutoMutex() {
    AutoMutex _l(gProcessMutex);
    // 下面是需要同步的代码内容
    // ...
}
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-10-10-smart-handle.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/wzy_1988/article/details/46620113]({% include relrefx.html url="/backup/2020-10-10-smart-handle.md/blog.csdn.net/a15a2001.html" %})
