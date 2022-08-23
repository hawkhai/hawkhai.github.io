---
layout: post
title: "编程与调试 Memory -- Windows Windbg 崩溃分析 CASES 一些案例"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["调试", "Memory"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "WinDBG"
---


## /MD -> /MT

编译配置改了改，出现错误：
```cpp
_ASSERTE(__acrt_first_block == header);
```
{% include image.html url="/assets/images/210602-win-windbg-cases/20220822143330.png" %}

```
Program: E:\kpdf\pdfreader_image\image\Debug\fastimage.dll
File: minkernel\crts\ucrt\src\appcrt\heap\debug_heap.cpp
Line: 996

Expression: __acrt_first_block == header

For information on how your program can cause an assertion
failure, see the Visual C++ documentation on asserts.

(Press Retry to debug the application)
fastimageg.exe 已触发了一个断点。
```

造成问题的原因：
由于其依赖的 dll 是 md 构建，而一些 C++ 头文件也是包含代码的，就造成了堆不匹配，找不到，从而崩溃。


## OpenCV cv::waitKey();

OpenCV `cv::waitKey();` debug 版本会断言崩溃。
```
opencv_world453d.dll!std::_Vector_const_iterator<std::_Vector_val<std::_Simple_types<std::shared_ptr<CvWindow>>>>::operator++() 行 75	C++
opencv_world453d.dll!std::_Vector_iterator<std::_Vector_val<std::_Simple_types<std::shared_ptr<CvWindow>>>>::operator++() 行 269	C++
opencv_world453d.dll!handleMessage(tagMSG & message, int & keyCode) 行 2196	C++
opencv_world453d.dll!cvWaitKey(int delay) 行 2311	C++
opencv_world453d.dll!cv::impl::Win32BackendUI::waitKeyEx(int delay) 行 3018	C++
opencv_world453d.dll!cv::waitKeyEx(int delay) 行 650	C++
opencv_world453d.dll!cv::waitKey(int delay) 行 660	C++
IBEABFHR.exe!main() 行 25	C++
```

[note {% include relref_github.html %}](https://github.com/mikke89/RmlUi/issues/45)
崩溃原因是这个函数没有写好：
```cpp
/*
 * message received. check if it belongs to our windows (frame, hwnd).
 * returns true (and value in keyCode) if a key was pressed.
 * otherwise returns false (indication to continue event loop).
 */
static bool handleMessage(MSG& message, int& keyCode)
{
    // whether we have to call translate and dispatch yet
    // otherwise the message was handled specifically
    bool is_processed = false;

    AutoLock lock(getWindowMutex());
    auto& g_windows = getWindowsList();
    for (auto it = g_windows.begin(); it != g_windows.end() && !is_processed; ++it)
    {
        auto window_ = *it;
        if (!window_)
            continue;
        CvWindow& window = *window_;
        if (!(window.hwnd == message.hwnd || window.frame == message.hwnd))
            continue;

        is_processed = true;
        switch (message.message)
        {
            ....
        }
    }

    ....
    return false; // no value to return, keep processing
}
```

D:\2021\opencv_local\4.5.3\modules\highgui\src\window_w32.cpp
`g_windows` 在迭代的过程中发生了修改。
`for (auto it = g_windows.begin(); it != g_windows.end() && !is_processed; ++it)` 改成：
```cpp
auto begin = g_windows.begin();
auto end = g_windows.end();
for (auto it = begin, next = end; it != end && !is_processed; it = next) {
    next = std::next(it, 1);
}
```


## QImage 内存泄漏

pdfcore\impl\SimplePageEdit.cpp
```cpp
QPixmap SimplePageEdit::GetImagePixmap(const std::shared_ptr<IPageElement>& element) {
    QPixmap pixmap;

    unsigned char* data = nullptr;
    int w = 0;
    int h = 0;
    int len = 0;
    len = EnginePdfiumGetImageData(m_pDisplayModal->GetEngine(), element, w, h, data, len);
    if (len > 0) {
        data = (unsigned char*)malloc(len);
        if (nullptr == data) {
            return pixmap;
        }

        len = EnginePdfiumGetImageData(m_pDisplayModal->GetEngine(), element, w, h, data, len);

        if (len > 0) {
            pixmap = QPixmap::fromImage(QImage(data, w, h, QImage::Format_ARGB32, [](void* data) { free(data); }));
        } else {
            if (nullptr != data) {
                free(data);
                data = nullptr;
            }
        }
    }
    return pixmap;
}
```

上面这段代码，存在严重的内存泄漏，调用一次 泄漏整张图片的内存，大概几十兆，稍微多调用几次，程序就挂了。
问题出在函数 `QImage`，`free(data);` 当 data 为空的时候，free 函数不会报错。
**写的时候，应该没有全面调试和确认，没有准确查询文档。**

函数原型：
```cpp
QImage(const uchar *data, int width, int height, Format format,
        QImageCleanupFunction cleanupFunction = nullptr,
        void *cleanupInfo = nullptr);
```

其中 data 是指向颜色数据（32bit）的指针，width 表示一行有多少个像素，height 表示一列有多少个像素，format 表示图像格式（QImage 提供了多种格式）。
QImage 在析构时并不会删除 data。如果提供了 cleanupFunction 和 cleanupInfo，那么当 QImage 的图像数据不再被使用时，
会调用 **cleanupFunction** 清除 **cleanupInfo** 所指向的内存。

**正确的写法：**
```cpp
QImageCleanupFunction cleanupFunction = [](void* data) { free(data); };
void* cleanupInfo = data;
pixmap = QPixmap::fromImage(QImage(data, w, h, QImage::Format_ARGB32, cleanupFunction, cleanupInfo));
```


## 指针对象内存泄漏

KExecuteInfoMgr::ThreadExecuteImpl 函数中有内存泄漏。
ExecuteTask 指针本来指向的是一个对象，如果把它转成 PVOID 再 delete 的话，就会导致这个对象的析构函数不会被调用。

{% include image.html url="/assets/images/210602-win-windbg-cases/20220701-102551.jpg" %}


## Windows 8.0 QStandardPaths::writableLocation

Windows 8.0 系统调用 QStandardPaths::writableLocation，vcruntime140.dll 运行时库崩溃问题说明 <sup>from guohua</sup>


### 崩溃 DUMP

{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113809.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113828.png" %}


### 关键接口说明

{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113844.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113857.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113908.png" %}


### 原因分析

QStandardPaths::writableLocation 接口的实现过程会调用 GetTokenInformation 判断当前进程的权限等级，根据进程权限返回不同的路径，当 GetTokenInformation 接口返回失败时，没有校验 token_info_length 的值是否合法，就直接调用了 token_info_buf.resize 接口，当 token_info_length 的值过大时，有可能会导致 malloc 分配内存失败返回 NULL

{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113934.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113945.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-113954.png" %}


### 修改方法

由于此崩溃只出现在 Windows 8.0 系统，所以把阅读器代码里调用 QStandardPaths::writableLocation 地方统一改成了 PathUtils::writableLocation（实现如下）

{% include image.html url="/assets/images/210602-win-windbg-cases/20220307-114014.png" %}
由于考虑到海外版有不少 WIN 8.0 用户，后续不要在代码里直接调用 QStandardPaths::writableLocation


## 被注入造成堆栈破坏

pdfupdate_ex.exe_2021.10.18.256_2b498_pdfupdate_ex.exe_2021.10.18.256_0000000.txt

```
EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 0042b498 (pdfupdate_ex!DeCryptLibFile+0x00000108)
   ExceptionCode: c0000409 (Security check failure or stack buffer overrun)
  ExceptionFlags: 00000001
NumberParameters: 0

ChildEBP RetAddr  Args to Child
0019f8a8 004a03f9 004c145c 6d636bf4 929c940b KERNELBASE!UnhandledExceptionFilter+0x1cb
0019fbdc 0042b498 00000003 00000080 00000000 pdfupdate_ex!__report_gsfailure+0xdf [f:\dd\vctools\crt_bld\self_x86\crt\src\gs_report.c @ 313]
0019fc3c 767524de 006e0000 00000000 00706c30 pdfupdate_ex!DeCryptLibFile+0x108 [d:\...\include\defend\cryptfunction.cpp @ 469]
```

IDA 打开对应的 pdfupdate_ex.exe，跳转到 `0042b498`：

{% include image.html url="/assets/images/210602-win-windbg-cases/20220223165659.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20220223165710.png" %}

一上来 `CreateFileW`，返回的时候 \_\_\_security_cookie 检查失败，崩溃了。


## 64 位指针被截断


### explorer.exe fastapp_ext64.dll ACCESS_VIOLATION.dmp

```
CONTEXT:  (.ecxr)
rax=00000000823b63c0 rbx=ffffffff823b63c0 rcx=000000007de8f948
rdx=ffffffff823b63c0 rsi=0000000000000000 rdi=00000000823b62b8
rip=0000000055361dea rsp=000000007de8f8b0 rbp=00000000823b6380
 r8=0000000000000000  r9=ffffffffffffffff r10=0000000000000072
r11=ffffffff823b63c0 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
fastapp_ext64!std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >::assign+0x1a:
00000000`55361dea 4c394218        cmp     qword ptr [rdx+18h],r8 ds:ffffffff`823b63d8=????????????????
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 0000000055361dea (fastapp_ext64!std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >::assign+0x000000000000001a)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 0000000000000000
   Parameter[1]: ffffffff823b63d8
Attempt to read from address ffffffff823b63d8
```

```
ntdll!NtWaitForSingleObject+0x14:
00007ffc`e352cdf4 c3          Unable to load image C:\Program Files (x86)\toypdf\fastapp_ext64.dll, Win32 error 0n2
rax=00000000823b63c0 rbx=ffffffff823b63c0 rcx=000000007de8f948
rdx=ffffffff823b63c0 rsi=0000000000000000 rdi=00000000823b62b8
rip=0000000055361dea rsp=000000007de8f8b0 rbp=00000000823b6380
 r8=0000000000000000  r9=ffffffffffffffff r10=0000000000000072
r11=ffffffff823b63c0 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r15=0000000000000000
iopl=0         nv up ei pl nz na pe nc
cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
fastapp_ext64!std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >::assign+0x1a:
00000000`55361dea 4c394218        cmp     qword ptr [rdx+18h],r8 ds:ffffffff`823b63d8=????????????????
RetAddr           : Args to Child                                                           : Call Site
00000000`00000000 : 00000000`00000000 00000000`00000000 00000000`00000000 00000000`00000000 : fastapp_ext64!std::basic_string<wchar_t,std::char_traits<wchar_t>,std::allocator<wchar_t> >::assign+0x1a [d:\program files\microsoft visual studio 8\vc\include\xstring @ 1039]
00000000`7de8f8b0  00000000
00000000`7de8f8b4  00000000
00000000`7de8f8b8  00000000
00000000`7de8f8bc  00000000
00000000`7de8f8c0  00000000
00000000`7de8f8c4  00000000
00000000`7de8f8c8  00000000
00000000`7de8f8cc  00000000
00000000`7de8f8d0  00000000
00000000`7de8f8d4  00000000
00000000`7de8f8d8  5536b692 fastapp_ext64!KAcctrl::OnActivate+0xc2 [e:\svn\kisengine\kis_v11_released_sp5.3_1337_fb\src\waitui_tools\fastpic_ext_forpdf\acctrl.cpp @ 98]
```

`Attempt to read from address ffffffff823b63d8` 指针出错，一看，就是被扩展出来的。

```cpp
#include <iostream>

class Class {
};

int main()
{
    if (true) { // 有符号数扩展的情况
        Class* p = new Class(); // 0x0000024bcf7e4770 {...}
        long inta = (long)p; // 0xcf7e4770
        unsigned long long int64u = inta; // 0xffffffffcf7e4770
        long long int64 = inta; // 0xffffffffcf7e4770
        p = (Class*)inta; // 指针变成了 0xffffffffcf7e4770 {...}
        p = 0;
    }
    if (true) { // 无符号数扩展的情况。
        Class* p = new Class(); // 0x0000029beea22fe0 {...}
        unsigned long inta = (long)p; // 0xeea22fe0
        unsigned long long int64u = inta; // 0x00000000eea22fe0
        long long int64 = inta; // 0x00000000eea22fe0
        p = (Class*)inta; // 指针变成了 0x00000000eea22fe0 {...}
        p = 0;
    }
    return 0;
}
```


## 虚表对不上造成的崩溃


### kavdr.exe toysdk.dll ACCESS\_VIOLATION.dmp

```
eax=0064006f ebx=0512d030 ecx=0512d030 edx=052b91c0 esi=00000001 edi=00000009
eip=052b9cd7 esp=0019e8e0 ebp=0019e988 iopl=0         nv up ei ng nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210286
toysdk!GetInterface+0x4bc7:
052b9cd7 807f2d00        cmp     byte ptr [edi+2Dh],0       ds:002b:00000036=??
ChildEBP RetAddr  Args to Child
WARNING: Stack unwind information not available. Following frames may be wrong.
0019e988 0503110f 04cc7320 0512d020 0512d030 toysdk!GetInterface+0x4bc7
0019e99c 05091e7c d556ed10 00ab1bf8 00000002 kvip3thex!vip_sdk::GetProductID+0x7f [e:\..\kis_kvip_fb\publish\purevipsdk\vip_sdk_product_info.hpp @ 27]
0019eae4 00403946 04d33e28 004ad928 00ab1bf8 kvip3thex!CKVip3thSdk::ReportInfo+0x2bc [e:\..\kis_kvip_fb\src\kvip3thex\kvip3thsdk.cpp @ 277]
0019eb8c 00403513 0019ebb0 da235292 000023f0 kavdr+0x3946
0019ebf4 77c6b025 6e82d304 0019ec4c 00000010 kavdr+0x3513
0019ec64 77c6addb 00000000 00000000 77c6adf3 ntdll!SbSelectProcedure+0x395
0019ec98 00000000 00000000 00000000 00000000 ntdll!SbSelectProcedure+0x14b
```

```
eax=0064006f ebx=0512d030 ecx=0512d030 edx=052b91c0 esi=00000001 edi=00000009
eip=052b9cd7 esp=0019e8e0 ebp=0019e988 iopl=0         nv up ei ng nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210286
toysdk!GetInterface+0x4bc7:
052b9cd7 807f2d00        cmp     byte ptr [edi+2Dh],0       ds:002b:00000036=??
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 052b9cd7 (toysdk!GetInterface+0x00004bc7)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000036
Attempt to read from address 00000036
```

```cpp
inline IVipSdkConfigInterface* toysdkWarpper::GetVipConfig()
{
    return vip_sdk_ifmgr_ ? dynamic_cast<IVipSdkConfigInterface*>(vip_sdk_ifmgr_->GetInterface(CONFIG_INTERFACE_NAME)) : NULL;
}

inline DWORD GetProductID() {
    IVipSdkConfigInterface* config = toysdkWarpper::GetInstance()->GetVipConfig();
    if (NULL == config) return 0;
    const wchar_t* v = config->GetValue(PRODUCT, PRODUCT_KEY, VALUE);
    if (NULL == v) return 0;
    return _wtoi(v);
}
```


### documentrepair.exe toysdk.dll ACCESS\_VIOLATION.dmp

```
eax=005f0070 ebx=077ad008 ecx=077ad008 edx=07a291c0 esi=00000000 edi=2aee3a8e
eip=07a29cd7 esp=0019f2f8 ebp=0019f3a0 iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210206
toysdk!GetInterface+0x4bc7:
07a29cd7 807f2d00        cmp     byte ptr [edi+2Dh],0       ds:002b:2aee3abb=??
ChildEBP RetAddr  Args to Child
WARNING: Stack unwind information not available. Following frames may be wrong.
0019f3a0 076b107f 07587320 077ad020 077ad008 toysdk!GetInterface+0x4bc7
0019f3b4 0771149d 00000001 b9a70c6e 04a003f7 kvip3thex!vip_sdk::GetVipVersion+0x7f [e:\..\kis_kvip_fb\publish\purevipsdk\vip_sdk_product_info.hpp @ 11]
0019f420 00402eff 616136de 0000005f 004912d8 kvip3thex!CKVip3thSdk::Init+0x23d [e:\..\kis_kvip_fb\src\kvip3thex\kvip3thsdk.cpp @ 133]
0019f434 00403bf5 00000000 488e334b 000023f0 documentrepair+0x2eff
004a3580 00000000 00000000 00000000 00000000 documentrepair+0x3bf5
```

```
eax=005f0070 ebx=077ad008 ecx=077ad008 edx=07a291c0 esi=00000000 edi=2aee3a8e
eip=07a29cd7 esp=0019f2f8 ebp=0019f3a0 iopl=0         nv up ei pl nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210206
toysdk!GetInterface+0x4bc7:
07a29cd7 807f2d00        cmp     byte ptr [edi+2Dh],0       ds:002b:2aee3abb=??
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 07a29cd7 (toysdk!GetInterface+0x00004bc7)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 2aee3abb
Attempt to read from address 2aee3abb
```

```cpp
inline DWORD GetVipVersion() {
    IVipSdkConfigInterface* config = toysdkWarpper::GetInstance()->GetVipConfig();
    if (NULL == config) return 0;
    const wchar_t* v = config->GetValue(PRODUCT, VIP_VERSION, VALUE);
    if (NULL == v) return 0;
    return _wtoi(v);
}
```
{% include image.html url="/assets/images/210602-win-windbg-cases/20220113150034.png" %}


## std::vector 智能指针数组溢出访问

fastapp.exe_2021.6.11.1_107e7c_e48caa8.txt

```
0:000> kv
  *** Stack trace for last set context - .thread/.cxr resets it
 # ChildEBP RetAddr  Args to Child
00 (Inline) -------- -------- -------- -------- fastapp!std::_Ref_count_base::_Decref+0x2 (Inline Function @ 010a7e7c) (CONV: thiscall) [D:\MSVC\include\memory @ 540]
01 (Inline) -------- -------- -------- -------- fastapp!std::_Ptr_base<BitmapCacheEntry>::_Decref+0x4 (Inline Function @ 010a7e7c) (CONV: thiscall) [D:\MSVC\include\memory @ 774]
02 (Inline) -------- -------- -------- -------- fastapp!std::shared_ptr<BitmapCacheEntry>::{dtor}+0x4 (Inline Function @ 010a7e7c) (CONV: thiscall) [D:\MSVC\include\memory @ 1033]
03 (Inline) -------- -------- -------- -------- fastapp!std::shared_ptr<BitmapCacheEntry>::operator=+0x20 (Inline Function @ 010a7e7c) (CONV: thiscall) [D:\MSVC\include\memory @ 1037]
04 0075d5b0 010ab042 0075d608 0a3088b8 080a7bc8 fastapp!RenderCache::Add+0x13c (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\RenderCache.cpp @ 186]
05 0075d674 010aabe6 00000000 00000000 00000000 fastapp!RenderCache::SynchronousRendering+0x252 (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\RenderCache.cpp @ 1071]
06 0075d6e0 010a89e0 058b8540 0000002c 00000000 fastapp!RenderCache::Render+0x186 (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\RenderCache.cpp @ 904]
07 0075d7c4 010959e2 058b8540 0000002c 00000000 fastapp!RenderCache::RequestRendering+0x210 (FPO: [Non-Fpo]) (CONV: thiscall) [E:\src\RenderCache.cpp @ 481]
```

```
eax=ffffffff ebx=00afcf40 ecx=00000040 edx=0aa82b24 esi=ffffffff edi=88000c00
eip=00c47e7c esp=00afcf18 ebp=00afcf38 iopl=0         nv up ei ng nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010286
Unable to load image C:\Program Files (x86)\fastapp\fastapp.exe, Win32 error 0n2
fastapp!RenderCache::Add+0x13c:
00c47e7c f00fc14704      lock xadd dword ptr [edi+4],eax ds:002b:88000c04=????????
```

```
EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 00c47e7c (fastapp!RenderCache::Add+0x0000013c)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000001
   Parameter[1]: 88000c04
Attempt to write to address 88000c04
```

shared_ptr 的 size 刚好是 8，+4 相当于 \_Rep 指针出错 `88000c04`，8 开头是系统地址了，这个地址肯定是错的。

```cpp
class _Ptr_base { // base class for shared_ptr and weak_ptr
private:
    element_type* _Ptr{nullptr};
    _Ref_count_base* _Rep{nullptr};
};
```

`eax=ffffffff` 就是 `-1`，`lock xadd dword ptr [edi+4],eax ds:002b:88000c04=????????`
这个的含义就是，尝试对 _Ref_count_base 进行减 1 操作，然后崩溃了。

查看源码：
```cpp
std::vector<std::shared_ptr<BitmapCacheEntry>> cache;

// Copy the PageRenderRequest as it will be reused
auto entry = std::make_shared<BitmapCacheEntry>();
entry->cacheIdx = cacheCount;
cache[cacheCount] = entry; // 崩溃到这一行。
cacheCount++;
```

共享指针被破坏了？其实不是，是数组越界了。我们可以写一段代码模拟这个情况（需要编译 Release 版本，开启速度优化）。
```cpp
int cacheCount = -1;
auto entry = std::make_shared<MyString>(buffer);
kvalue[cacheCount] = entry; // 模拟崩溃行。
```

对应汇编为：
```
// kvalue[cacheCount] = entry;
00AC8855  mov         edi,dword ptr [eax+4]
00AC8858  or          ebx,0FFFFFFFFh
00AC885B  mov         dword ptr [eax],ecx
00AC885D  mov         dword ptr [eax+4],esi
00AC8860  test        edi,edi
00AC8862  je          threadfunc+283h (0AC8883h)
00AC8864  mov         eax,ebx
00AC8866  lock xadd   dword ptr [edi+4],eax // 就是 -1 操作
00AC886B  jne         threadfunc+283h (0AC8883h)
00AC886D  mov         eax,dword ptr [edi]
00AC886F  mov         ecx,edi
00AC8871  call        dword ptr [eax]
00AC8873  mov         eax,ebx
```

如果下标是 `-1`，崩溃为：
```
EAX = FFFFFFFF EBX = FFFFFFFF ECX = 0121BE74 EDX = 0127DEE0 ESI = 0121BE68
EDI = 88003100 EIP = 00AC8866 ESP = 042CF984 EBP = 042CFA10 EFL = 00010286
0x88003104 = 00000000
```

如果下标超出数组长度，崩溃为：
```
EAX = FFFFFFFF EBX = FFFFFFFF ECX = 00539164 EDX = 005B6EC8 ESI = 00539158
EDI = 88001700 EIP = 00D78866 ESP = 0262FD7C EBP = 0262FE08 EFL = 00010286
0x88001704 = 00000000
```

看看内存结构：
{% include image.html url="/assets/images/210602-win-windbg-cases/20210619003129.png" %}
{% include image.html url="/assets/images/210602-win-windbg-cases/20200312111504316.png" %}

每个堆块的前 8 个字节是一个 HEAP_ENTRY 结构体，头部的结构，记录了这块内存 de 信息。
Vista 引入了很多新的东西，对堆块的块头结构（HEAP_ENTRY）编码，编码的目的是引入随机性，增强堆的安全性，防止黑客轻易就可以预测堆的数据内容而实施攻击。
其中的 EncodeFlagMask 用来指示是否启用编码功能；Encoding 字段是用来编码的，编码的方法就是用这个 Encoding 结构与每个堆块的头结构做异或（XOR）。
* [Windows Heap Chunk Header Parsing and Size Calculation](https://stackoverflow.com/questions/28483473/windows-heap-chunk-header-parsing-and-size-calculation)
* [解读编码后的 HEAP_ENTRY 结构](http://advdbg.org/blogs/advdbg_system/articles/5152.aspx)
* [!heap 和 _HEAP_ENTRY {% include relref_cnblogs.html %}](https://www.cnblogs.com/xumaojun/p/8544089.html)

单独一篇文章，验证这个问题：
[Windows Windbg 崩溃分析 -- HEAP_ENTRY 结构]({% include relref.html url="/blog/2021/06/19/win-windbg-cases-heap-entry" %})


## 野指针 QString::toStdString().c_str()

危险的：`QString::toStdString().c_str()`，他的定义是：
```cpp
inline std::string QString::toStdString() const
{ return toUtf8().toStdString(); }
inline std::wstring QString::toStdWString() const {
    std::wstring str;
    str.resize(length());
#if __cplusplus >= 201703L
    str.resize(toWCharArray(str.data()));
#else
    if (length())
        str.resize(toWCharArray(&str.front()));
#endif
    return str;
}
```

```cpp
void testmain(QString& qstr) {
    const char* p = qstr.toStdString().c_str();
    std::cout << p;
}
```
上面这段代码是存在问题的，生成的汇编为：
{% include image.html url="/assets/images/210602-win-windbg-cases/20210609095612.png" %}

换一种写法：
```cpp
void testmain2(QString& qstr) {
    const std::string str = qstr.toStdString();
    std::cout << str.c_str();
}
```
生成的代码是：
{% include image.html url="/assets/images/210602-win-windbg-cases/20210609100048.png" %}

也可以这样写，生命周期 都是没问题的（调用函数生命周期内，临时变量都不会被释放）：
```cpp
void testmain2(QString& qstr) {
    std::cout << qstr.toStdString().c_str();
}
```

《C++ 程序设计语言》第 10 章中写道，“除非一个临时对象被约束到某个引用，或者被用于作为命名对象的初始化，否则它将在创建它的那个完整表达式结束时销毁”。
所谓“完整表达式”，是指不是其它表达式的子表达式的表达式。简单来说，一个完整表达式的标识一般是一个分号。


### 生命周期问题

```cpp
class Temp {
public:
    Temp(const char* p) {
        if (p) {
            int size = strlen(p) + 1;
            this->p = new char[size];
            strcpy_s(this->p, size, p);
        }
    }
    virtual ~Temp() {
        if (p) {
            delete[] p;
            p = nullptr;
        }
    }

    char* getp() {
        return p;
    }

private:
    char* p = nullptr;
};

void func() {
    // 执行顺序：构造 a，构造 b，这句代码执行完成，释放 a，函数退出，释放 b。
    Temp b = Temp("a").getp();
}
```


## 崩溃 空指针问题

```
FAULTING_IP:
dbapp!EnginePdfiumTransformByPageCTM+89
00501379 8b7004          mov     esi,dword ptr [eax+4]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 00501379 (dbapp!EnginePdfiumTransformByPageCTM+0x00000089)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000004
Attempt to read from address 00000004

BUGCHECK_STR:  ACCESS_VIOLATION

STACK_TEXT:
01efcccc 0034fc3a 01efcd10 0ee95c88 01efcd00 dbapp!EnginePdfiumTransformByPageCTM+0x89
01efcd28 00351ef1 01efcd48 3e9baddd 00000000 dbapp!DisplayModel::CvtToScreen+0x18a
```

**Attempt to read from address 00000004** 尝试读取内存 `00000004`，而此时
`mov esi,dword ptr [eax+4]`，寄存器 `eax=00000000`，`[eax+4]` 就是 `00000004`。

```
This dump file has an exception of interest stored in it.
The stored exception information can be accessed via .ecxr.
(2c9c.2d6c): Access violation - code c0000005 (first/second chance not available)
eax=00000000 ebx=0ee95c88 ecx=00000001 edx=00000002 esi=0f127678 edi=00000001
eip=00501379 esp=01efcbe0 ebp=01efcccc iopl=0         nv up ei pl zr na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00210246
dbapp!EnginePdfiumTransformByPageCTM+0x89:
00501379 8b7004          mov     esi,dword ptr [eax+4] ds:002b:00000004=????????
```

```
System Uptime: 3 days 23:44:37.243
Process Uptime: 0 days 0:01:21.000
```

这个也说明了是进程启动就崩溃了，崩溃到函数 EnginePdfiumTransformByPageCTM 里面的空指针。


## 黑指针问题 StrChrIW

```
eax=00000000 ebx=00000000 ecx=00000000 edx=00000000 esi=00000000 edi=00000490
eip=777e29dc esp=0654cf1c ebp=0654cf8c iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00000202
ntdll!ZwWaitForSingleObject+0xc:
777e29dc c20c00          ret     0Ch

eax=ffffffff ebx=0000970d ecx=78d91b15 edx=00020dc5 esi=14f5bffe edi=76c5ca20
eip=76759ed8 esp=0654fc28 ebp=0654fc40 iopl=0         nv up ei ng nz na pe nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010286
KERNELBASE!StrChrIW+0xa8:
76759ed8 0fb74602        movzx   eax,word ptr [esi+2]     ds:002b:14f5c000=????
ChildEBP RetAddr  Args to Child
0654fc40 76759afc 14f5b9fa 0000970d 16c2a420 KERNELBASE!StrChrIW+0xa8
0654fc60 00e39bed 14f5b9fa 169ddd38 16ad1858 KERNELBASE!StrStrIW+0x2c
fastapp!TextSearch::FindTextInPage+0x7d [E:\src\TextSearch.cpp @ 270]

FAULTING_IP:
KERNELBASE!StrChrIW+a8
76759ed8 0fb74602        movzx   eax,word ptr [esi+2]

EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 76759ed8 (KERNELBASE!StrChrIW+0x000000a8)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 14f5c000
Attempt to read from address 14f5c000

DEFAULT_BUCKET_ID:  INVALID_POINTER_READ
```

汇编指令：`MOVZX OPD, OPS`
将 8 位或 16 位的 OPS 零扩展为 16 位或 32 位，在传给 OPD。
相当于 函数 FindTextInPage 里面用了一个 **被释放** 或者 **未初始化** 的指针 并 调用了 **StrChrIW**。


## 崩溃 QList\<QString\> 非多线程安全

**`QCoreApplication::processEvents();` 这玩意不能轻易用，容易造成失控。**
<font color="red">为啥堆栈里面看不到？有机会了要好好研究验证一下。</font>


### 崩溃现场

这个崩溃只在特定电脑，Release 版本反复操作，一定概率出现。

```
EXCEPTION_RECORD:  ffffffff -- (.exr 0xffffffffffffffff)
ExceptionAddress: 00000000
   ExceptionCode: 80000003 (Break instruction exception)
  ExceptionFlags: 00000000
NumberParameters: 0

DEFAULT_BUCKET_ID:  INVALID_POINTER_READ
ERROR_CODE: (NTSTATUS) 0x80000003 - {

eax=65ecefd4 ebx=69284bd4 ecx=022fdb00 edx=58dd6f68 esi=65ecefd4 edi=65eceff8
eip=7aaa11f4 esp=022fdae8 ebp=022fdb18 iopl=0         nv up ei ng nz ac po cy
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010293
qt5core!QString::QString+0x4:
7aaa11f4 8b00            mov     eax,dword ptr [eax]  ds:002b:65ecefd4=????????
Minidump doesn't have an exception context
Unable to get exception context, HRESULT 0x80004002
ChildEBP RetAddr  Args to Child
WARNING: Stack unwind information not available. Following frames may be wrong.
022fdb18 0082a30d 4676af70 022fdc01 0fd14e80 qt5core!QString::QString+0x4
022fdb48 7ac3fced 022ffec0 00000000 00000002 fastapp!QMainClient::qt_static_metacall+0x9d [E:\moc\moc_QMainClient.cpp @ 107]
022fdbec 7ac41c12 0fd14e80 00000011 022fdc24 qt5core!QObject::qt_static_metacall+0x10fd
022fdc34 00762844 4bc92fd4 022fdce8 7ac3fc97 qt5core!QMetaObject::activate+0x42
022fdc40 7ac3fc97 00000001 449e0ff0 0fd14e80 fastapp!QtPrivate::QSlotObject<void (__thiscall MainFrame::*)(QString const &),
                                                        QtPrivate::List<QString const &>,void>::impl+0x54
                                                    [D:\include\QtCore\qobjectdefs_impl.h @ 425]
022fdce8 7ac41c12 4bc92f58 00000007 022fdd38 qt5core!QObject::qt_static_metacall+0x10a7
022fdd54 007ee935 00000001 00000000 000001cd qt5core!QMetaObject::activate+0x42
022fdd6c 7ac4772b 00000001 43c18ff0 4bc92f58 fastapp!QtPrivate::QSlotObject<void (__thiscall TOYPage::*)(bool,bool,int),
                                                        QtPrivate::List<bool,bool,int>,void>::impl+0x65
                                                    [D:\include\QtCore\qobjectdefs_impl.h @ 418]
022fddc8 7b5b0e55 49124fb8 4bc92f58 09f0dff8 qt5core!QMetaCallEvent::placeMetaCall+0x1b
022fdde4 7ac257ba 4bc92f58 49124fb8 4bc92f58 Qt5Widgets!QWidget::event+0xcd5
022fde14 7b592a53 7b592a6d 49124fb8 49124fb8 qt5core!QCoreApplicationPrivate::sendThroughApplicationEventFilters+0x8a
022fde18 7b592a6d 49124fb8 49124fb8 4bc92f58 Qt5Widgets!QApplicationPrivate::notify_helper+0xb3
022fde30 7b591be4 4bc92f58 49124fb8 4bc92f58 Qt5Widgets!QApplicationPrivate::notify_helper+0xcd
022fde54 77b65181 f3f738d1 00000001 00000000 Qt5Widgets!QApplication::notify+0x1874
77c56894 00000000 00000000 00000000 00000000 ntdll!TppPoolpReferenceGlobalPool+0x74
```


### 问题分析

这个堆栈和汇编一致，但是和源码不一致，Release 版本经过优化。
在函数 `QMainClient::qt_static_metacall` 里面是找不到 `qt5core!QString::QString+0x4` 构造函数的。
命令：`dds esp` 可以查看到当前堆栈残留，这里面指示的位置是正确的。

```
022fdae8  00744c9d fastapp!QMainClient::slotTabInitFinished+0x22d [E:\src\QMainClient.cpp @ 248]
022fdaec  65ecefd4
022fdaf0  2e63afc8
022fdaf4  022ffec0
022fdaf8  49124fb8
022fdafc  022fdb08
022fdb00  58dd6f68
022fdb04  69284bd4
022fdb08  69284f40
022fdb0c  69284fc0
022fdb10  022ffed8
022fdb14  022ffec0
022fdb18  022fdb48
022fdb1c  0082a30d fastapp!QMainClient::qt_static_metacall+0x9d [E:\moc\moc_QMainClient.cpp @ 107]
022fdb20  4676af70
```

`qt5core!QString::QString+0x4` 出现访问不可读的内存黑指针，第一反应是堆破坏，反复检查相关变量是否线程安全。
尝试了各种可能，后来回家路上突然来了灵感，想起了这个函数 `QCoreApplication::processEvents();`！


### 问题原因

`QList<QString>` 不是线程安全的，迭代的过程中 调用了 `QCoreApplication::processEvents();`，
然后又再次递归触发了当前函数，再次发生了迭代。
在一个线程里面对它发生了 两次迭代，两次迭代也没啥，偏偏又有一个 `.clear();`。

```cpp
QList<QString> m_printFileList;

void QMainClient::slotTabInitFinished() {
    for (auto strfile : m_printFileList) { // 这里崩溃了。
        // 这里很深的一个地方触发了：QCoreApplication::processEvents();
        // 调用过程中，再次递归调用了当前函数，再次迭代了 m_printFileList
        printDlg->addFileTarget(strfile);
    }
    m_printFileList.clear();
}
```

知道原因后，就很好改了，一个方案就是先放到一个临时变量里面，避免迭代：

```cpp
void QMainClient::slotTabInitFinished() {
    QList<QString> pflist;
    for (auto& strfile : m_printFileList) {
        pflist.push_back(strfile);
    }
    m_printFileList.clear();
    // 这个可能对当前函数形成递归崩溃，所以拷贝出来先再执行。
    for (auto& strfile : pflist) {
        printDlg->addFileTarget(strfile);
    }
}
```

我们可以写一段简单的代码模拟这个崩溃：

```cpp
void Test::slotvoid() {
    QString qstra("qstra");
    QString qstrb("qstrb");
    QList<QString> qlist;
    qlist.push_back(qstra);
    qlist.push_back(qstrb);
    for (auto istr : qlist) { // 崩溃到这一行。
        for (auto jstr : qlist) {
            std::cout << istr.toStdString() << "\t" << jstr.toStdString() << std::endl;
        }
        qlist.clear();
    }
    qlist.clear();
}
```

刚好崩溃到 拷贝构造函数：`inline QString::QString(const QString &other);`。

{% include image.html url="/assets/images/210602-win-windbg-cases/20210603114533.png" %}

至于 `QCoreApplication::processEvents();` 为啥会调用到当前槽函数，写一篇 QT 信号槽的深度理解。


### fastapp.exe_2022.6.6.2240_581c3d_d88e3f6.txt

```
CONTEXT:  (.ecxr)
eax=00000000 ebx=0a96664c ecx=04af0220 edx=00000000 esi=00000001 edi=09733c08
eip=007f1c3d esp=018fcaa0 ebp=018fcb34 iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
fastapp!CTOY_ProgressiveRenderer::Continue+0x22d:
007f1c3d 8b34f0          mov     esi,dword ptr [eax+esi*8] ds:002b:00000008=????????
Resetting default scope

EXCEPTION_RECORD:  (.exr -1)
ExceptionAddress: 007f1c3d (fastapp!CTOY_ProgressiveRenderer::Continue+0x0000022d)
   ExceptionCode: c0000005 (Access violation)
  ExceptionFlags: 00000000
NumberParameters: 2
   Parameter[0]: 00000000
   Parameter[1]: 00000008
Attempt to read from address 00000008
```

一看，肯定是个空指针，但是这个指针怎么会为空呢？
百思不得其解，真正原因就是：`processEvents` 又调用出来形成递归，修改了指针，造成回溯的时候崩溃（堆栈就在那里断了）。

> 对于不能重现的崩溃，知道代码行后，简单的办法就是，在 VS 里面找到对应的代码行，设置断点，然后查看反汇编，那种内联的 `inline` 的系统库，也能准确匹配到符号了。
> 帮助更准确的定位到源码问题。

异常线程堆栈
```
eax=00000000 ebx=0a96664c ecx=04af0220 edx=00000000 esi=00000001 edi=09733c08
eip=007f1c3d esp=018fcaa0 ebp=018fcb34 iopl=0         nv up ei pl nz na po nc
cs=0023  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202
fastapp!CTOY_ProgressiveRenderer::Continue+0x22d:
007f1c3d 8b34f0          mov     esi,dword ptr [eax+esi*8] ds:002b:00000008=????????
ChildEBP RetAddr  Args to Child
018fcb34 007c9451 018fcc90 00000000 00000000 fastapp!CTOY_ProgressiveRenderer::Continue+0x22d (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\engine\engine\toyium\core\ftoyapi\render\ctoy_progressiverenderer.cpp @ 75]
018fcb64 00715791 00000000 00000000 018fcc14 fastapp!`anonymous namespace'::RenderPageImpl+0x311 (FPO: [Non-Fpo]) (CONV: cdecl) [<..>\engine\engine\engine\toy\common\ctoy_renderpage.cpp @ 79]
018fcd14 004644d5 018fce3c 00000000 784fastapp!EnginePdfium::RenderPage+0x961 (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\engine\engine\engine\EnginePdfium.cpp @ 1600]
018fce10 00462c9f 00000000 018fceb8 018fce3c fastapp!RenderCache::RenderPageReportParameters+0x95 (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\myapp\myapp\src\RenderCache.cpp @ 1568]
018fcf34 00462701 00000000 00000000 00000000 fastapp!RenderCache::SynchronousRendering+0x34f (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\myapp\myapp\src\RenderCache.cpp @ 1100]
018fcf88 00461117 00000000 00000000 00000000 fastapp!RenderCache::RenderInner+0x181 (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\myapp\myapp\src\RenderCache.cpp @ 934]
018fd080 00462f02 00000000 00000000 00000000 fastapp!RenderCache::RequestRendering+0x207 (FPO: [Non-Fpo]) (CONV: thiscall) [<..>\myapp\myapp\src\RenderCache.cpp @ 500]
....
....
....
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-06-02-win-windbg-cases.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/mikke89/RmlUi/issues/45]({% include relrefx.html url="/backup/2021-06-02-win-windbg-cases.md/github.com/7332c83b.html" %})
- [https://stackoverflow.com/questions/28483473/windows-heap-chunk-header-parsing-and-size-calculation]({% include relrefx.html url="/backup/2021-06-02-win-windbg-cases.md/stackoverflow.com/797c2d6f.html" %})
- [http://advdbg.org/blogs/advdbg_system/articles/5152.aspx]({% include relrefx.html url="/backup/2021-06-02-win-windbg-cases.md/advdbg.org/df049c84.aspx" %})
- [https://www.cnblogs.com/xumaojun/p/8544089.html]({% include relrefx.html url="/backup/2021-06-02-win-windbg-cases.md/www.cnblogs.com/36e9d8f7.html" %})
