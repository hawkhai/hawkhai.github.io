---
layout: post
title: "编程与调试 C++ -- VS2005 C++98 shared_ptr & unique_ptr"
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

C++11 std::shared_ptr & std::unique_ptr，让人抓狂的是公司有的工程是 VS2005 C++98。


## unique_ptr

```cpp
#pragma once
#include <cstddef>
#include <algorithm>
#include <cassert>

template <typename T>
inline T& move(T& v)
{
    return v;
}

template<class T>
class unique_ptr
{
public:
    typedef T element_type;

    unique_ptr() : m_pObject(NULL)
    {
    }
    explicit unique_ptr(T* p) : m_pObject(p)
    {
    }

    // 转移所有权。
    unique_ptr(const unique_ptr& ptr) : m_pObject(ptr.m_pObject)
    {
        const_cast<unique_ptr&>(ptr).m_pObject = NULL;
    }
    unique_ptr& operator=(unique_ptr ptr)
    {
        swap(ptr);
        return *this;
    }

    // 卸载的时候顺利销毁。
    inline ~unique_ptr()
    {
        destroy();
    }
    inline void reset()
    {
        destroy();
    }

    void reset(T* p)
    {
        assert((NULL == p) || (m_pObject != p));
        if (p != m_pObject) {
            destroy();
            m_pObject = p;
        }
    }

    void swap(unique_ptr& lhs)
    {
        std::swap(m_pObject, lhs.m_pObject);
    }

    // 什么都不做。直接放生。
    inline void release()
    {
        m_pObject = NULL;
    }

    inline operator bool() const
    {
        return (NULL != m_pObject);
    }

    inline T& operator*() const
    {
        assert(NULL != m_pObject);
        return *m_pObject;
    }
    inline T* operator->() const
    {
        assert(NULL != m_pObject);
        return m_pObject;
    }
    inline T* get() const
    {
        return m_pObject;
    }

private:
    inline void destroy()
    {
        delete m_pObject;
        m_pObject = NULL;
    }

    inline void release() const
    {
        m_pObject = NULL;
    }

private:
    T* m_pObject;
};

template<class T, class U> inline bool operator==(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() == r.get());
}
template<class T, class U> inline bool operator!=(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() != r.get());
}
template<class T, class U> inline bool operator<=(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() <= r.get());
}
template<class T, class U> inline bool operator<(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() < r.get());
}
template<class T, class U> inline bool operator>=(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() >= r.get());
}
template<class T, class U> inline bool operator>(const unique_ptr<T>& l, const unique_ptr<U>& r)
{
    return (l.get() > r.get());
}
```


## shared_ptr

```cpp
#pragma once
#include <cstddef>
#include <algorithm>
#include <cassert>

// 对象计数器。
class shared_ptr_count
{
public:
    shared_ptr_count() : m_pCounter(NULL)
    {
    }
    shared_ptr_count(const shared_ptr_count& count) : m_pCounter(count.m_pCounter)
    {
    }

    void swap(shared_ptr_count& lhs)
    {
        std::swap(m_pCounter, lhs.m_pCounter);
    }
    long useCount() const
    {
        if (NULL != m_pCounter) {
            return *m_pCounter;
        }
        return 0;
    }

    template<class U>
    void acquire(U* p)
    {
        if (NULL != p)
        {
            if (NULL == m_pCounter)
            {
                m_pCounter = new long(1);
            }
            else
            {
                ++(*m_pCounter);
            }
        }
    }

    template<class U>
    void release(U* p)
    {
        if (NULL != m_pCounter)
        {
            --(*m_pCounter);
            if (0 == *m_pCounter)
            {
                delete p;
                delete m_pCounter;
            }
            m_pCounter = NULL;
        }
    }

private:
    long* m_pCounter;
};

template<class T>
class shared_ptr
{
public:
    typedef T element_type;

    shared_ptr() : m_pObject(NULL), m_count()
    {
    }

    explicit shared_ptr(T* p) : m_count()
    {
        acquire(p);
    }

    template <class U>
    shared_ptr(const shared_ptr<U>& ptr, T* p) : m_count(ptr.m_count)
    {
        acquire(p);
    }

    template <class U>
    shared_ptr(const shared_ptr<U>& ptr) : m_count(ptr.m_count)
    {
        assert((NULL == ptr.m_pObject) || (0 != ptr.m_count.useCount()));
        acquire(static_cast<typename shared_ptr<T>::element_type*>(ptr.m_pObject));
    }

    shared_ptr(const shared_ptr& ptr) : m_count(ptr.m_count)
    {
        assert((NULL == ptr.m_pObject) || (0 != ptr.m_count.useCount()));
        acquire(ptr.m_pObject);
    }

    shared_ptr& operator=(shared_ptr ptr)
    {
        swap(ptr);
        return *this;
    }

    ~shared_ptr()
    {
        release();
    }
    void reset()
    {
        release();
    }

    void reset(T* p)
    {
        assert((NULL == p) || (m_pObject != p));
        release();
        acquire(p);
    }

    void swap(shared_ptr& lhs)
    {
        std::swap(m_pObject, lhs.m_pObject);
        m_count.swap(lhs.m_count);
    }

    operator bool() const
    {
        return (0 < m_count.useCount());
    }
    bool unique() const
    {
        return (1 == m_count.useCount());
    }
    long useCount() const
    {
        return m_count.useCount();
    }

    T& operator*() const
    {
        assert(NULL != m_pObject);
        return *m_pObject;
    }
    T* operator->() const
    {
        assert(NULL != m_pObject);
        return m_pObject;
    }
    T* get() const
    {
        return m_pObject;
    }

private:
    void acquire(T* p)
    {
        m_count.acquire(p);
        m_pObject = p;
    }

    void release()
    {
        m_count.release(m_pObject);
        m_pObject = NULL;
    }

private:
    template<class U>
    friend class shared_ptr;

private:
    T*                  m_pObject;
    shared_ptr_count    m_count;
};

template<class T, class U> bool operator==(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() == r.get());
}
template<class T, class U> bool operator!=(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() != r.get());
}
template<class T, class U> bool operator<=(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() <= r.get());
}
template<class T, class U> bool operator<(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() < r.get());
}
template<class T, class U> bool operator>=(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() >= r.get());
}
template<class T, class U> bool operator>(const shared_ptr<T>& l, const shared_ptr<U>& r)
{
    return (l.get() > r.get());
}

template<class T, class U>
shared_ptr<T> static_pointer_cast(const shared_ptr<U>& ptr)
{
    T* p = static_cast<typename shared_ptr<T>::element_type*>(ptr.get());
    return shared_ptr<T>(ptr, p);
}

template<class T, class U>
shared_ptr<T> dynamic_pointer_cast(const shared_ptr<U>& ptr)
{
    T* p = dynamic_cast<typename shared_ptr<T>::element_type*>(ptr.get());
    if (NULL != p)
    {
        return shared_ptr<T>(ptr, p);
    }
    else
    {
        return shared_ptr<T>();
    }
}
```


## MyBuffer

```cpp
#include "stdafx.h"
#include <iostream>
#include <cstring>
#include <cstdlib>

#include <vector>
#include "shared_ptr.hpp"
#include "unique_ptr.hpp"

class MyBuffer
{
public:
    explicit MyBuffer(size_t len = 0)
    {
        m_size = len;
        m_buffer = new char[m_size + 1]; // 多搞一个。
        memset(m_buffer, 0, m_size + 1);
    };
    virtual ~MyBuffer()
    {
        delete[] m_buffer;
    }

private:
    MyBuffer(MyBuffer&);
    MyBuffer& operator=(MyBuffer&);

private:
    size_t  m_size;
    char*   m_buffer;
};
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-02-25-C++-shared_ptr.md.js" %}'></script></p>
