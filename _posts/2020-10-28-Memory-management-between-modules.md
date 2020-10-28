---
layout: post
title: "Windows 跨模块内存管理"
location: "珠海"
categories: ["编程"]
tags: [Windows Prog, Memory, C++]
toc: true
---

很多 Windows API 设计的歪瓜裂枣、奇形怪状的，搞不清楚为什么，后来发现了原因。

特级大师作品一览。

<table class="tablestyle" ntablew="2:2:2"></table>

| 函数 | 说明 | 评论 |
| ---- | ---- | ---- |
| GetWindowText(HWND,LPTSTR,int) | 取得窗口标题。需要在参数中给出保存标题所使用的内存指针，和这块内存的尺寸。 | 晕！我又不知道窗口标题的长度，居然还要我提供尺寸？！没办法，只能估摸着给一个大一些的尺寸吧。 |
| sprintf(char *,const char *,...) | 格式化一个字符串。这个函数不用给出缓冲区的长度啦。 | 恩，虽然不用给出长度了，但你敢给个小尺寸吗？哼！ |
| int CListBox::GetTextLen(int) <br/> CListBox::GetText(int,LPTSTR) | 取得列表窗中子项目的标题。需要调用两个函数，先取得长度，然后分配内存，再实际取得标题内容。 | 呵呵。 |


## 谁申请谁释放

一般来说，为了避免由于跨模块调用（尤其是使用动态链接库）的时候，内存分配方和释放方不同而可能引发的问题（一般是由于分配方与释放方使用了不同的堆），肯定是要坚持“谁分配，谁释放”的原则的。

因此大部分的 API 一般是由调用方提供一个字符串缓冲区以及缓冲区可以接受字符的最大长度，然后由被调用方将自己的字符串复制到调用方指定的位置去的。

Windows API 为了解决这个问题，各种办法都出来了。这里肯定是不能采用高级数据类型的。


### 搞两次

搞两次，第一次得到大小，第二次真正调用。

WideCharToMultiByte 就是这个办法，非常奇怪。


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

还有两个变种：

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


### Windows COM BSTR 等 全局的管理

被调用方分配内存，然后调用方释放。使用统一的分配 API：SysAllocString / SysFreeString。


### 用回调函数

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

包装成一个 Bundle 也是这个的一个变种。一个建议的接口实现：

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


## 参考

* [windows api 设计的如何？C 语言怎么从函数中返回未知长度的字符串，可以让它的调用者优雅地接收？](https://www.zhihu.com/question/33058061)
* [C 接口中的内存分配释放](https://zhuanlan.zhihu.com/p/95299255)
* [失传的 C 结构体打包技艺](https://github.com/ludx/The-Lost-Art-of-C-Structure-Packing)
* [结构体中最后成员为一个零长数组与一个指针](http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E6%88%90%E5%91%98%E4%B8%BA%E4%B8%80%E4%B8%AA%E9%9B%B6%E9%95%BF%E6%95%B0%E7%BB%84%E4%B8%8E%E4%B8%80%E4%B8%AA%E6%8C%87%E9%92%88/)
* [结构体中最后一个成员为 \[0\] 或 \[1\] 长度数组 \(柔性数组成员\) 的用法](http://wenboo.site/2017/09/05/%E7%BB%93%E6%9E%84%E4%BD%93%E4%B8%AD%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E6%88%90%E5%91%98%E4%B8%BA-0-%E6%88%96-1-%E9%95%BF%E5%BA%A6%E6%95%B0%E7%BB%84-%E6%9F%94%E6%80%A7%E6%95%B0%E7%BB%84%E6%88%90%E5%91%98-%E7%9A%84%E7%94%A8%E6%B3%95/)
