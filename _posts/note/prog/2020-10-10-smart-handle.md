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


## TortoiseSVN 源码版本

```cpp
// TortoiseSVN - a Windows shell extension for easy version control

// Copyright (C) 2011 - TortoiseSVN

// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.

// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software Foundation,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
#pragma once

/**
 * \ingroup Utils
 * Helper classes for handles.
 */
template <typename HandleType,
    template <class> class CloseFunction,
    HandleType NULL_VALUE = NULL>
class CSmartHandle : public CloseFunction<HandleType>
{
public:
    CSmartHandle()
    {
        m_Handle = NULL_VALUE;
    }

    CSmartHandle(HandleType h)
    {
        m_Handle = h;
    }

    HandleType operator=(HandleType h)
    {
        if (m_Handle != h)
        {
            CleanUp();
            m_Handle = h;
        }

        return(*this);
    }

    bool CloseHandle()
    {
        return CleanUp();
    }

    void Detach()
    {
        m_Handle = NULL_VALUE;
    }

    operator HandleType()
    {
        return m_Handle;
    }

    HandleType * GetPointer()
    {
        return &m_Handle;
    }

    operator bool()
    {
        return IsValid();
    }

    bool IsValid()
    {
        return m_Handle != NULL_VALUE;
    }

    ~CSmartHandle()
    {
        CleanUp();
    }

protected:
    bool CleanUp()
    {
        if ( m_Handle != NULL_VALUE )
        {
            bool b = Close(m_Handle);
            m_Handle = NULL_VALUE;
            return b;
        }
        return false;
    }

    HandleType m_Handle;
};

class CEmptyClass
{
};

template <typename T>
struct CCloseHandle
{
    bool Close(T handle)
    {
        return !!::CloseHandle(handle);
    }

protected:
    ~CCloseHandle()
    {
    }
};

template <typename T>
struct CCloseRegKey
{
    bool Close(T handle)
    {
        return RegCloseKey(handle) == ERROR_SUCCESS;
    }

protected:
    ~CCloseRegKey()
    {
    }
};

template <typename T>
struct CCloseLibrary
{
    bool Close(T handle)
    {
        return !!::FreeLibrary(handle);
    }

protected:
    ~CCloseLibrary()
    {
    }
};

template <typename T>
struct CCloseViewOfFile
{
    bool Close(T handle)
    {
        return !!::UnmapViewOfFile(handle);
    }

protected:
    ~CCloseViewOfFile()
    {
    }
};

template <typename T>
struct CCloseFindFile
{
    bool Close(T handle)
    {
        return !!::FindClose(handle);
    }

protected:
    ~CCloseFindFile()
    {
    }
};

// Client code (definitions of standard Windows handles).
typedef CSmartHandle<HANDLE,  CCloseHandle>                                         CAutoGeneralHandle;
typedef CSmartHandle<HKEY,    CCloseRegKey>                                         CAutoRegKey;
typedef CSmartHandle<PVOID,   CCloseViewOfFile>                                     CAutoViewOfFile;
typedef CSmartHandle<HMODULE, CCloseLibrary>                                        CAutoLibrary;
typedef CSmartHandle<HANDLE,  CCloseHandle, INVALID_HANDLE_VALUE>                   CAutoFile;
typedef CSmartHandle<HANDLE,  CCloseFindFile, INVALID_HANDLE_VALUE>                 CAutoFindFile;
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-10-10-smart-handle.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/wzy_1988/article/details/46620113]({% include relrefx.html url="/backup/2020-10-10-smart-handle.md/blog.csdn.net/a15a2001.html" %})
