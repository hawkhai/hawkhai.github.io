---
layout: post
title: "编程 C++ -- Windows 跨模块内存管理"
author:
location: "珠海"
categories: ["编程"]
tags: ["Prog Note", "Memory", "C++"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
---

很多 Windows API 设计的歪瓜裂枣、奇形怪状的，搞不清楚为什么，后来发现了原因。

特级大师作品一览。

<table class="tablestyle" ntablew="2:2:2"></table>

| 函数 | 说明 | 评论 |
| ---- | ---- | ---- |
| GetWindowText(HWND, LPTSTR, int) | 取得窗口标题。需要在参数中给出保存标题所使用的内存指针，和这块内存的尺寸。 | 晕！我又不知道窗口标题的长度，居然还要我提供尺寸？！没办法，只能估摸着给一个大一些的尺寸吧。 |
| sprintf(char *, const char *, ...) | 格式化一个字符串。这个函数不用给出缓冲区的长度啦。 | 恩，虽然不用给出长度了，但你敢给个小尺寸吗？哼！ |
| int CListBox::GetTextLen(int) <br/> CListBox::GetText(int, LPTSTR) | 取得列表窗中子项目的标题。需要调用两个函数，先取得长度，然后分配内存，再实际取得标题内容。 | 呵呵。 |


## 谁申请谁释放

一般来说，为了避免由于跨模块调用（尤其是使用动态链接库）的时候，内存分配方和释放方不同而可能引发的问题（一般是由于分配方与释放方使用了不同的堆），肯定是要坚持“谁分配，谁释放”的原则的。

因此大部分的 API 一般是由调用方提供一个字符串缓冲区以及缓冲区可以接受字符的最大长度，然后由被调用方将自己的字符串复制到调用方指定的位置去的。

Windows API 为了解决这个问题，各种办法都出来了。这里肯定是不能采用高级数据类型的。MD/MT 模式，MD 解决也存在缺陷，一个工程要同一个 crt 版本。


### 搞两次

搞两次，第一次得到大小，第二次真正调用。

WideCharToMultiByte 就是这个办法，非常奇怪。

```cpp
void from_utf8(const std::string &string_str, std::wstring &string_wstr) {
    if (string_str.size() < 1) {
        return;
    }
    string_wstr.clear();
    int len = MultiByteToWideChar(CP_UTF8, 0, string_str.c_str(), -1, NULL, NULL);
    string_wstr.resize(len);
    wchar_t *str_ptr = new wchar_t[len];
    MultiByteToWideChar(CP_UTF8, 0, string_str.c_str(), -1, str_ptr, len);
    string_wstr = str_ptr;
    delete [] str_ptr;
    str_ptr = NULL;
}

void to_utf8(const std::wstring &string_wstr, std::string &string_str) {
    int len = WideCharToMultiByte(CP_UTF8, 0, string_wstr.c_str(), -1, NULL, 0, NULL, NULL);
    if (len == 0) {
        return;
    }
    ++len;
    char* str_ptr = new char[len];
    WideCharToMultiByte(CP_UTF8, 0, string_wstr.c_str(), -1, str_ptr, len, NULL, NULL);
    string_str = str_ptr;
    delete[] str_ptr;
    str_ptr = NULL;
}
```


### 传入内存长度

```cpp
int WINAPI GetWindowText(
  _In_   HWND hWnd,
  _Out_  LPTSTR lpString,
  _In_   int nMaxCount
);
```

为了解决长度多大合适，又有 API：

```cpp
int WINAPI GetWindowTextLength(
  _In_  HWND hWnd
);
```

还有几个变种：

1. 根据返回错误码，决定是否长度不够，需要重新申请内存，重新调用一次。
2. 一来就搞一个最大的可能长度。
3. 预估最大值，根据返回码重新调整大小。


### 单独的释放接口

```cpp
// 假设你已经根据实际情况定义好了 _DLLEXPORT 用于导出函数。
_DLLEXPORT char* CreateString();
_DLLEXPORT void DeleteString(char* pString);

char* CreateString() {
    char* mystr = new char[100];
    strcpy(mystr, "这是一个测试。");
    return mystr;
}

void DeleteString(char* pString) {
    delete[] pString;
}
```

调用方：

```cpp
char* client = CreateString();
// 对 client 做你想做的事情。
DeleteString(client);
```


### COM BSTR 等 全局的管理

被调用方分配内存，然后调用方释放。使用统一的分配 API：SysAllocString / SysFreeString。

使用 CoTaskMemAlloc/CoTaskMemFree 申请、释放内存。因为内存的申请、释放由系统完成，故可以保证其一致性。


### 虚表或回调函数

```cpp
struct writer {
    void* data;
    void (*proc)(void*, const char*, size_t);
};

void write_string(writer w, const char* s, size_t len) {
    w.proc(w.data, s, len);
}

// ABI 这边
mystring s;
get_string(make_writer(s));

// make_writer 函数你自己提供
// 另一边
void get_string(struct writer w) {
    write_string(w, "hello", 6);
}
```

包装成一个 Bundle 也是这个的一个变种。Bundle 要求实现一个数据序列化。
基于 Key-Value Map 实现，不用关注长度，参数个数灵活，可以类比 Json 万能接口，比 Json 效率更好，如果跨进程，可能 Json 更好。

一个建议的接口实现：

```cpp
template<typename T>
interface ISampleBundle {
public:
    virtual T* dataPtr() = 0;
    virtual T* mallocData(int size) = 0;
    virtual void releaseData() = 0;
};

template<typename T>
class KSampleBundle : public ISampleBundle<T> {
public:
    KSampleBundle() {
        data = NULL;
    }
    virtual ~KSampleBundle() {
        if (data) { delete[] data; data = NULL; }
    }

    virtual void releaseData() {
        if (data) { delete[] data; data = NULL; }
    }
    virtual T* dataPtr() { return data; }
    virtual T* mallocData(int size) {
        if (data) { delete[] data; data = NULL; }
        // 当同一个工程使用多个库时，它们的含义可能不同，很容易弄混。
        // 因而很多人会多添加一个字节
        if (size <= 0) { size = 1; }
        data = new T[size + 1];
        memset(data, 0, (size + 1) * sizeof(T));
        return data;
    }

private:
    T* data;
};

[ uuid(311F23B8-165F-4324-8388-29C7E4ADB789) ]
interface ISampleEngine {
    virtual HRESULT __stdcall GetItemInfo(LPCWSTR fpath, ISampleBundle<TCHAR>& info) = 0;
}
```


### 传入迭代函数

非常蹩脚，但是也有。比如  EnumWindows。还有一种方法，就是迭代 FindWindow。

使用 EnumWindows 和 EnumChildWindows 函数以及相对的回调函数 EnumWindowsProc 和 EnumChildWindowsProc 获取所有顶层窗口以及它们的子窗口。GetDesktopWindow / GetNextWindow


## 柔性数组

结构体头部是长度，尾部是一个长度 1 的字符串。然后把唯一的字符串放在结构体尾部。

```cpp
typedef struct _OBJECT_NAME_INFORMATION {
    _UNICODE_STRING_T<PWSTR> Name;
    WCHAR NameBuffer[1];
} OBJECT_NAME_INFORMATION, *POBJECT_NAME_INFORMATION;

typedef struct _FILE_STREAM_INFORMATION {
    ULONG NextEntryOffset;
    ULONG StreamNameLength;
    LARGE_INTEGER StreamSize;
    LARGE_INTEGER StreamAllocationSize;
    WCHAR StreamName[1];
} FILE_STREAM_INFORMATION;

typedef struct _FILENAME_ATTRIBUTE { // 文件名属性的值区域
    ULONGLONG DirectoryFileReferenceNumber; // 父目录的 FRN
    ULONGLONG CreationTime;
    ULONGLONG ChangeTime;
    ULONGLONG LastWriteTime; // 最后一次 MFT 更新时间
    ULONGLONG LastAccessTime;
    ULONGLONG AllocatedSize; // 未明
    ULONGLONG DataSize; // 偶尔与文件大小 GetFileSize 不同
    ULONG FileAttributes;
    ULONG AlignmentOrReserved;
    UCHAR NameLength;
    UCHAR NameType; // POSIX 0x0 WIN32 0x01 DOS 0x02 WIN32 & DOS 0x3
    WCHAR Name[1];
} FILENAME_ATTRIBUTE, *PFILENAME_ATTRIBUTE;

```


## 复杂的堆

在 linux 下，每个进程只有一个 heap，在任何一个动态库模块 so 中通过 new 或者 malloc 来分配内存的时候都是从这个唯一的 heap 中分配的，那么自然你在其它随便什么地方都可以释放。这个模型是简单的。
但是在 windows 下面，问题变得复杂了。

1. windows 允许一个进程中有多个 heap，那么这样就需要指明一块内存要在哪个 heap 上分配，win32 的 HeapAlloc 函数就是这样设计的，给出一个 heap 的句柄，给出一个 size，然后返回一个指针。每个进程都至少有一个主 heap，可以通过 GetProcessHeap 来获得，其它的堆，可以通过 GetProcessHeaps 取到。同样，内存释放的时候通过 HeapFree 来完成，还是需要指定一个堆。

2. 这样的设计显然是比较灵活的，但是问题在于这样的话，每次分配内存的时候就必须要显式的指定一个 heap，对于 crt 中的 new/malloc，显然需要特殊处理。那么如何处理就取决于 crt 的实现了。vc 的 crt 是创建了一个单独的 heap，叫做 \_\_crtheap，它对于用户是看不见的，但是在 new/malloc 的实现中，都是用 HeapAlloc 在这个 \_\_crtheap 上分配的，也就是说 malloc(size) 基本上可以认为等同于 HeapAlloc(__crtheap, size)（当然实际上 crt 内部还要维护一些内存管理的数据结构，所以并不是每次 malloc 都必然会触发 HeapAlloc），这样 new/malloc 就和 windows 的 heap 机制吻合了。（这里说的是 vc 的 crt 实现，我不知道其它 crt 实现是否如此）

3. 如果一个进程需要动态库支持，系统在加载 dll 的时候，在 dll 的启动代码 \_DllMainCRTStartup 中，会创建这个 \_\_crtheap，所以理论上有多少个 dll，就有多少个 \_\_crtheap。最后主进程的 mainCRTStartup 中还会创建一个为主进程服务的 \_\_crtheap。（由于顺序总是先加载 dll，然后才启动 main 进程，所以你可以看到各个 dll 的 \_\_crtheap 地址比较小，而主进程的 \_\_crtheap 比较大，当然排在最前面的堆是每个进程的主 heap）。可以使用 windbg 查看。

4. 从上面的分析中可以看出，对于 crt 来说，由于每个 dll 都有自己的 heap，所以每个 dll 通过 new/malloc 分配的内存都是在自己 dll 内部的那个 heap 上用 HeapAlloc 来分配的，而如果你想在其它模块中释放，那么在释放的时候 HeapFree 就会失败了，因为各个模块的 \_\_crtheap 是不一样的。

这样，基本上事情就比较清楚了，在 windows 下一个进程存在着多个 heap，除了一个主 heap 外，还有很多的 \_\_crtheap，用来处理通过 c/c++ 的运行库进行的内存操作。所以使用 new/malloc 来分配的内存实际上都是局部的，可以在多个 dll 中共享，但是却必须是谁申请谁释放。这个是 windows 下的一个规则。（当然如果在 dll 内部使用 HeapAlloc(GetProcessHeap(), size) 来分配的内存是可以在 dll 以外释放的，因为这时内存分配在全局的主 heap 上，而不是分配在 dll 自己的 \_\_crtheap 上）


## 其它

目前，有很多清理内存的工具，主要使用 Windows 提供的 API：EmptyWorkingSet 或 SetProcessWorkingSetSize 进行内存清理，用途不大。


## 参考

* [C++ 内存管理变革 \(2\)：最袖珍的垃圾回收器](https://blog.csdn.net/xushiweizh/article/details/1396573)
* [windows api 设计的如何？C 语言怎么从函数中返回未知长度的字符串，可以让它的调用者优雅地接收？ {% include relref_zhihu.html %}](https://www.zhihu.com/question/33058061)
* [C 接口中的内存分配释放 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/95299255)
* [失传的 C 结构体打包技艺](https://github.com/ludx/The-Lost-Art-of-C-Structure-Packing)
* [结构体中最后成员为一个零长数组与一个指针](http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E6%88%90%E5%91%98%E4%B8%BA%E4%B8%80%E4%B8%AA%E9%9B%B6%E9%95%BF%E6%95%B0%E7%BB%84%E4%B8%8E%E4%B8%80%E4%B8%AA%E6%8C%87%E9%92%88/)
* [结构体中最后一个成员为 \[0\] 或 \[1\] 长度数组 \(柔性数组成员\) 的用法](http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E6%88%90%E5%91%98%E4%B8%BA-0-%E6%88%96-1-%E9%95%BF%E5%BA%A6%E6%95%B0%E7%BB%84-%E6%9F%94%E6%80%A7%E6%95%B0%E7%BB%84%E6%88%90%E5%91%98-%E7%9A%84%E7%94%A8%E6%B3%95/)
* [跨模块内存管理的陷阱 许式伟](https://blog.csdn.net/xushiweizh/article/details/1452302)
* [17. c++ - 谁分配谁释放 HEAP](https://blog.csdn.net/hgy413/article/details/6716397)
* [最快速度找到内存泄漏 许式伟](https://blog.csdn.net/xushiweizh/article/details/1451083)

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://blog.csdn.net/xushiweizh/article/details/1396573]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/blog.csdn.net/0d276c4f475d13aecd0afd2b1832c406.html" %})
- [2] [https://www.zhihu.com/question/33058061]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/www.zhihu.com/48645e8ccc177f212b76acaab661f78c.html" %})
- [3] [https://zhuanlan.zhihu.com/p/95299255]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/zhuanlan.zhihu.com/34b177e5c4ff518597e1118b6203f8e6.html" %})
- [4] [https://github.com/ludx/The-Lost-Art-of-C-Structure-Packing]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/github.com/679997b3d5fbd42c48949cd7a20b2c1e.html" %})
- [5] [http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E6%88%90%E5%91%98%E4%B8%BA%E4%B8%80%E4%B8%AA%E9%9B%B6%E9%95%BF%E6%95%B0%E7%BB%84%E4%B8%8E%E4%B8%80%E4%B8%AA%E6%8C%87%E9%92%88/]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/wenboo.site/86ddea9365d7289a81912998e462229f.html" %})
- [6] [http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E6%88%90%E5%91%98%E4%B8%BA-0-%E6%88%96-1-%E9%95%BF%E5%BA%A6%E6%95%B0%E7%BB%84-%E6%9F%94%E6%80%A7%E6%95%B0%E7%BB%84%E6%88%90%E5%91%98-%E7%9A%84%E7%94%A8%E6%B3%95/]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/wenboo.site/6786ff8ee5bba30a35b171c1bb265221.html" %})
- [7] [https://blog.csdn.net/xushiweizh/article/details/1452302]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/blog.csdn.net/8a86bc477873106e9702470ec82bf6c2.html" %})
- [8] [https://blog.csdn.net/hgy413/article/details/6716397]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/blog.csdn.net/dee4853e6a0127c597aec8435ff21bdb.html" %})
- [9] [https://blog.csdn.net/xushiweizh/article/details/1451083]({% include relref.html url="/backup/2020-10-28-Memory-management-between-modules.md/blog.csdn.net/095c8316e75846a0ec6f56620683f952.html" %})
