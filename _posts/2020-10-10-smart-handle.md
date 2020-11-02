---
layout: post
title: "编程 -- 利用 C++ 类生命周期，自动释放 HANDLE 句柄，打造可重入锁"
location: "珠海"
categories: ["编程"]
tags: [Windows Prog, C++]
toc: true
---

利用 C++ 类生命周期，自动释放 HANDLE 句柄，香。

```cpp
template<typename T = HANDLE, BOOL (__stdcall *Closer)(T) = ::CloseHandle>
class SmartHandleTmpl
{
    SmartHandleTmpl(const SmartHandleTmpl&);
    SmartHandleTmpl& operator=(const SmartHandleTmpl&);

public:
    SmartHandleTmpl(T handle = NULL) : _handle(handle) { }
    virtual ~SmartHandleTmpl() {
        if (_handle && _handle != INVALID_HANDLE_VALUE)
            Closer(_handle);
    }

    operator T() const { return _handle; }
    template<typename F>
    operator F*() const { return (F*) _handle; }
    T* operator&() { return &_handle; }
    T operator=(T handle) {
        if (_handle != handle && _handle && _handle != INVALID_HANDLE_VALUE)
            Closer(_handle);
        return _handle = handle;
    }

private:
    T _handle;
};

typedef SmartHandleTmpl<> SmartHandle;
// SmartHandleTmpl<HANDLE, ::FindClose>
// SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
```

另外两个就是：

```cpp
SmartHandleTmpl<HANDLE, ::FindClose>
SmartHandleTmpl<LPCVOID, ::UnmapViewOfFile>
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
