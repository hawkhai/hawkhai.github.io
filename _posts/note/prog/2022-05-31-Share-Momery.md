---
layout: post
title: "编程与调试 C++ -- 共享内存，同步机制"
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

[^_^]: blog.csdn.net/shuilan0066/article/details/87979315


## 共享内存

Windows 下进程的地址空间在逻辑上是相互隔离的，但在物理上却是重叠的。所谓的重叠是指同一块内存区域可能被多个进程同时使用。
共享内存，各个进程可以共享同一块物理内存，进程可以直接读写内存，不需要数据拷贝。
由于多个进程共享一块内存，所以也需要同步机制。


## 实现步骤


### 本进程创建

1. 创建内存映射文件对象 CreateFileMapping，
    Windows 即在物理内存申请一块指定大小的内存区域，返回文件映射对象的句柄 hMap。
2. 将内存对象映射在进程地址空间 MapViewOfFile。


### 其它进程访问

其它进程访问这个内存对象时，
1. OpenFileMapping 获取对象句柄。
2. 调用 MapViewOfFile 映射在自己的进程空间。

这样，同一块内存块被映射到了不同的进程空间，从而达到多个进程共享同一个内存块的目的。


## 简单示例

```cpp
#pragma once
#include <windows.h>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <assert.h>

namespace NMt {
    class CReadFileLock;
    class CWriteFileLock;
};

#ifdef SHAREMEMORYDLL_EXPORTS
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT //__declspec(dllimport)
#endif

namespace ShareMemoryDll
{
    typedef uint32_t        uint;
    typedef signed char     schar;
    typedef unsigned char   uchar;
    typedef unsigned short  ushort;
    typedef int64_t         int64;
    typedef uint64_t        uint64;
#define CV_BIG_INT(n)   n##LL
#define CV_BIG_UINT(n)  n##ULL

    typedef unsigned char ShareMemoryData;
    typedef unsigned char ShareMemoryTail;

    struct ShareMemoryHeader {
        INT32 memorySize = 0; // 整个内存块的大小。
        INT32 headSize = 0; // 头的大小。
        INT32 contentSize = 0; // 内容的大小。可以变化的，不一定要写满。
        INT32 tailSize = 0; // 尾巴的大小。
        UINT64 crcCheck = 0;
        INT32 varReserved = 0; // 保留字段。

        INT32 getMaxContentSize() {
            return memorySize - headSize - tailSize;
        }
    };

    __interface IShareMemoryInterface
    {
        virtual ShareMemoryData* alloc(int size) = 0;
        virtual void free(ShareMemoryData* data) = 0;
    };

    class CShareMemoryCallback : public IShareMemoryInterface {
    public:
        virtual ShareMemoryData* alloc(int size) {
            auto retv = new ShareMemoryData[size + 1]; // 多弄一个。
            retv[size] = '$';
            return retv;
        }
        virtual void free(ShareMemoryData* data) {
            delete[] data;
        }
    };

    class DLLEXPORT ShareMemory {
    protected:
        const int getHeadSize();

        const int getTailSize();

        ShareMemoryHeader* getMemoryHeader();

        int getMemorySize();

        int getContentSize();

        ShareMemoryData* getContentPtr();

    public:
        ShareMemory(LPCWSTR lpName, bool write);

        virtual ~ShareMemory();

    private:
        int readImpl(ShareMemoryData*& data, IShareMemoryInterface* callback);

    public:
        int read(ShareMemoryData*& data, IShareMemoryInterface* callback);
        // Computes 64-bit "cyclic redundancy check" sum, as specified in ECMA-182
        static uint64 crc64(const uchar* data, size_t size, uint64 crcx);

        bool check() {
            return m_pReadFileLock && m_pWriteFileLock && m_hMap && m_pBuffer;
        }

    protected:
        std::wstring m_sLockedFilePath = L"ShareMemoryLockedFile-.mdb";
        std::wstring m_lpMapName = L"ShareMemoryMap-";
        bool m_write = false;
        NMt::CReadFileLock* m_pReadFileLock = nullptr;
        NMt::CWriteFileLock* m_pWriteFileLock = nullptr;
        HANDLE m_hMap = nullptr;
        ShareMemoryData* m_pBuffer = nullptr; // LPVOID
    };

    class DLLEXPORT ShareMemoryWrite : public ShareMemory {
    public:
        ShareMemoryWrite(LPCWSTR lpName, int size);
        ~ShareMemoryWrite();

    private:
        int writeImpl(ShareMemoryData* data, int size);

    public:
        int write(ShareMemoryData* data, int size);
    };

    class DLLEXPORT ShareMemoryRead : public ShareMemory {
    public:
        ShareMemoryRead(LPCWSTR lpName);
        ~ShareMemoryRead();
    };
};
```

```cpp
#include "pch.h"
#include "ShareMemoryDll.h"
#include "../TestFileLock/RWFileLock.h"

using namespace ShareMemoryDll;

const int ShareMemory::getHeadSize() {
    return sizeof(ShareMemoryHeader);
}

const int ShareMemory::getTailSize() {
    return sizeof(ShareMemoryTail);
}

ShareMemoryHeader* ShareMemory::getMemoryHeader() {
    if (!m_pBuffer) {
        return nullptr;
    }
    ShareMemoryHeader* header = (ShareMemoryHeader*)m_pBuffer;
    // 估计是版本不对。
    if (header->headSize != getHeadSize() || header->tailSize != getTailSize()) {
        return nullptr;
    }
    return header;
}

int ShareMemory::getMemorySize() {
    ShareMemoryHeader* header = getMemoryHeader();
    if (!header) {
        return -1;
    }
    return header->memorySize;
}

int ShareMemory::getContentSize() {
    ShareMemoryHeader* header = getMemoryHeader();
    if (!header) {
        return -1;
    }
    return header->contentSize;
}

ShareMemoryData* ShareMemory::getContentPtr() {
    if (m_pBuffer == nullptr) {
        return nullptr;
    }
    return m_pBuffer + getHeadSize();
}

ShareMemory::ShareMemory(LPCWSTR lpName, bool write) : m_write(write) {
    assert(lpName);
    m_lpMapName = L"ShareMemoryMap-";
    m_sLockedFilePath = L"ShareMemoryLockedFile-";
    if (lpName) {
        m_lpMapName.append(lpName);
        m_sLockedFilePath.append(lpName);
    }
    m_sLockedFilePath.append(L".mdb");

    m_pReadFileLock = new NMt::CReadFileLock(m_sLockedFilePath.c_str());
    m_pWriteFileLock = new NMt::CWriteFileLock(m_sLockedFilePath.c_str());
}

ShareMemory::~ShareMemory() {
    if (m_pBuffer) {
        ::UnmapViewOfFile(m_pBuffer);
        m_pBuffer = nullptr;
    }
    if (m_hMap) {
        ::CloseHandle(m_hMap);
        m_hMap = nullptr;
    }
    delete m_pReadFileLock;
    delete m_pWriteFileLock;
}

ShareMemoryWrite::~ShareMemoryWrite() {
    int a = 0;
}

ShareMemoryWrite::ShareMemoryWrite(LPCWSTR lpName, int size) : ShareMemory(lpName, true) {
    assert(size >= 0);
    if (size < 0) {
        size = 0;
    }

    ShareMemoryHeader header;
    header.headSize = getHeadSize();
    header.contentSize = 0; // 初始为空。
    header.tailSize = getTailSize();
    header.memorySize = size + getHeadSize() + getTailSize();

    m_hMap = ::CreateFileMapping(INVALID_HANDLE_VALUE, //
        NULL, //
        PAGE_READWRITE, //
        0, header.memorySize, //
        m_lpMapName.c_str());
    if (m_hMap == nullptr) {
        m_hMap = ::OpenFileMapping(FILE_MAP_ALL_ACCESS, 0, m_lpMapName.c_str());
    }

    m_pBuffer = (ShareMemoryData*)::MapViewOfFile(m_hMap, FILE_MAP_ALL_ACCESS, 0, 0, 0);
    assert(m_pBuffer);
    if (m_pBuffer) { // 把头刷进去。
        memcpy(m_pBuffer, &header, sizeof(header));
        ShareMemoryTail tail;
        tail = 0; // 把尾巴再刷进去。
        memcpy(getContentPtr(), &tail, sizeof(tail));
    }
}

int ShareMemoryWrite::writeImpl(ShareMemoryData* data, int size) {

    ShareMemoryHeader* header = getMemoryHeader();
    if (!header) {
        return -1;
    }
    if (size > header->getMaxContentSize()) {
        size = header->getMaxContentSize(); // 截断写入。
    }

    assert(header == (ShareMemoryHeader*)m_pBuffer); // 断言直接指内存。
    header->contentSize = size;
    header->crcCheck = crc64(data, size, 0);
    memcpy(m_pBuffer, header, getHeadSize()); // 重新把头刷进去。
    memcpy(getContentPtr(), data, size);
    ShareMemoryTail tail;
    tail = 0; // 把尾巴再刷进去。
    memcpy(getContentPtr() + size, &tail, sizeof(tail));
    return size;
}

int ShareMemoryWrite::write(ShareMemoryData* data, int size) {
    if (!m_pBuffer || !data || size < 0) {
        return -1;
    }

    m_pWriteFileLock->Lock();

    int retv = writeImpl(data, size);

    m_pWriteFileLock->Unlock();
    return retv;
}

ShareMemoryRead::ShareMemoryRead(LPCWSTR lpName) : ShareMemory(lpName, false) {
    m_hMap = ::OpenFileMapping(FILE_MAP_READ, 0, m_lpMapName.c_str());
    m_pBuffer = (ShareMemoryData*)::MapViewOfFile(m_hMap, FILE_MAP_READ, 0, 0, 0);
    assert(m_pBuffer);
}

ShareMemoryRead::~ShareMemoryRead() {

}

// Computes 64-bit "cyclic redundancy check" sum, as specified in ECMA-182
uint64 ShareMemory::crc64(const uchar* data, size_t size, uint64 crcx)
{
    static uint64 table[256];
    static bool initialized = false;

    if (!initialized)
    {
        for (int i = 0; i < 256; i++)
        {
            uint64 c = i;
            for (int j = 0; j < 8; j++)
                c = ((c & 1) ? CV_BIG_UINT(0xc96c5795d7870f42) : 0) ^ (c >> 1);
            table[i] = c;
        }
        initialized = true;
    }

    uint64 crc = ~crcx;
    for (size_t idx = 0; idx < size; idx++) {
        crc = table[(uchar)crc ^ data[idx]] ^ (crc >> 8);
    }
    return ~crc;
}

int ShareMemory::readImpl(ShareMemoryData*& data, IShareMemoryInterface* callback) {

    assert(data == nullptr);
    if (!m_pBuffer || !callback) {
        return -1;
    }

    ShareMemoryHeader* header = getMemoryHeader();
    if (!header) {
        return -1;
    }

    int contentSize = header->contentSize;
    data = callback->alloc(contentSize + 1);
    memcpy(&data[0], getContentPtr(), contentSize);
    data[contentSize] = 0;
    auto crcCheck = crc64(data, contentSize, 0);
    //printf("memorySize=%d contentSize=%d check=%d \r\n", //
    //    header->memorySize, header->contentSize,
    //    crcCheck == header->crcCheck);
    return contentSize;
}

int ShareMemory::read(ShareMemoryData*& data, IShareMemoryInterface* callback) {

    if (!m_pBuffer || !callback) {
        return -1;
    }

    m_pReadFileLock->Lock();

    int retv = readImpl(data, callback);

    m_pReadFileLock->Unlock();
    return retv;
}
```


## 同步机制


### 主进程负责写

这时，需要等待其它进程读操作完毕后，才能写
而且，一旦主进程开始写，其它进程不能再去写


### 其它进程访问

映射内存

全局事件

读取这部分内存，
读取时，先确保主进程不在同时写

读取锁：
```cpp
m_hWriterLockFile = ::CreateFile(m_sWriterLockFilePath,
                                 GENERIC_READ,
                                 FILE_SHARE_READ,
                                 NULL, // default security
                                 OPEN_ALWAYS,
                                 FILE_ATTRIBUTE_NORMAL,
                                 NULL);
m_hReaderWriterLockFile = ::CreateFile(m_sReaderWriterLockFilePath,
                                       GENERIC_READ,
                                       FILE_SHARE_READ,
                                       NULL, // default security
                                       OPEN_ALWAYS,
                                       FILE_ATTRIBUTE_NORMAL,
                                       NULL);
```

写入锁：
```cpp
m_hWriterLockFile = ::CreateFile(m_sWriterLockFilePath,
                                 GENERIC_READ | GENERIC_WRITE,
                                 0, // exclusive
                                 NULL, // default security
                                 OPEN_ALWAYS,
                                 FILE_ATTRIBUTE_NORMAL,
                                 NULL);
m_hReaderWriterLockFile = ::CreateFile(m_sReaderWriterLockFilePath,
                                       GENERIC_READ | GENERIC_WRITE,
                                       0, // exclusive access
                                       NULL, // default security
                                       OPEN_ALWAYS,
                                       FILE_ATTRIBUTE_NORMAL,
                                       NULL);
```

完整代码：github.com/hawkhai/ShareMemory.git


## Inter Computer Read/Write File Lock

<https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock>


## 参考资料

<http://www.cnblogs.com/dongsheng/p/4460944.html>

<http://blog.chinaunix.net/uid-26833883-id-3230564.html>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-05-31-Share-Momery.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.codeproject.com/Articles/49670/Inter-Computer-Read-Write-File-Lock]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/www.codeproject.com/5204d1cf.html" %})
- [http://www.cnblogs.com/dongsheng/p/4460944.html]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/www.cnblogs.com/44de51f5.html" %})
- [http://blog.chinaunix.net/uid-26833883-id-3230564.html]({% include relrefx.html url="/backup/2022-05-31-Share-Momery.md/blog.chinaunix.net/28af4862.html" %})
