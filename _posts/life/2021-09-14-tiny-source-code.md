---
layout: post
title: "编程与调试 -- Tiny Source Code, Tiny My Life"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["C/C++", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid: true
glslcanvas:
codeprint:
---

```
"C:\Program Files (x86)\Debugging Tools for Windows\gflags.exe" /p /enable ncnn_test.exe /full
```

```cpp
#define CASE_RETURN(x) case x: return L ## #x

inline std::string GetKernelCode(const std::string & filename)
{
    std::stringstream buffer;
    buffer << std::ifstream(filename.c_str()).rdbuf();
    return buffer.str();
}

if (!PathFileExists(fpath)) {
    CreateDirectory(fpath, NULL);
}

wchar_t fpath[MAX_PATH + 1] = { 0 };
DWORD res = GetTempPath(MAX_PATH, fpath);
if (res <= 0 || res >= MAX_PATH) {
    return gpuip::GPUIP_CODE::CODE_ERROR;
}

// 加载 dll 不要弹框报错。
auto modex = SEM_FAILCRITICALERRORS |     //
             SEM_NOALIGNMENTFAULTEXCEPT | //
             SEM_NOGPFAULTERRORBOX |      //
             SEM_NOOPENFILEERRORBOX;
auto modebak = ::SetErrorMode(modex);

HINSTANCE hDLL = LoadLibrary(current.c_str());

auto modey = ::SetErrorMode(modebak);
assert(modey == modex);

/**
4294967293 fffffffd -- -3 fffffffd
4294967294 fffffffe -- -2 fffffffe
4294967295 ffffffff -- -1 ffffffff
0 0 -- 0 0
1 1 -- 1 1
2 2 -- 2 2
3 3 -- 3 3*/
    for (int i = -3; i <= 3; i++) {
        unsigned int ui = (unsigned int) i;
        printf("%u %x -- %d %x \n", i, i, ui, ui);
    }

// 64 位版本：
int a = sizeof(int); // 4
a = sizeof(long); // 4
a = sizeof(long long); // 8
a = sizeof(__int64); // 8
a = sizeof(void*); // 8
a = 0;
```

出现 `.dims = (int)` 的都不对。

x | cv::Mat | cv::UMat | cv::_InputArray
---- | ---- | ---- | ----
0 | int flags; | int flags; | int flags;
1 | int dims; | int dims; | void\* obj;
2 | int rows; | int rows; | Size sz.width;
3 | int cols; | int cols; | Size sz.height;
4 | uchar\* data; | MatAllocator\* allocator; |
5 | const uchar\* datastart; | UMatUsageFlags usageFlags; |
6 | const uchar\* dataend; | UMatData\* u; |
7 | const uchar\* datalimit; | size_t offset; |
8 | MatAllocator\* allocator; | MatSize size; |
9 | UMatData\* u; | MatStep step.p; |
10 | MatSize size; | MatStep step.buf\[0\]; |
11 | MatStep step.p; | MatStep step.buf\[1\]; |
12 | MatStep step.buf\[0\]; | |
13 | MatStep step.buf\[1\]; | |

x | 老版本 ncnn::Mat（40 字节）<br/>**应该以这个为准** | 最新版本 ncnn::Mat（44 字节）
---- | ---- | ----
0 | void\* data; | void\* data;
1 | int\* refcount; | int\* refcount;
2 | size_t elemsize; | size_t elemsize
3 | int elempack; | int elempack;
4 | Allocator\* allocator; | Allocator\* allocator;
5 | int dims; | int dims;
6 | int w; | int w;
7 | int h; | int h;
8 | int c; | int d;
9 | size_t cstep; | int c;
10 | | size_t cstep;

E:\kpdf\kvision\opencv\opencv-3.4.2\modules\core\include\opencv2\core\mat.inl.hpp
```
inline
Mat::~Mat()
{
    release();
    if ( step.p != step.buf )
        fastFree(step.p);
}

inline
void Mat::release()
{
    if ( u && CV_XADD(&u->refcount, -1) == 1 )
        deallocate();
    u = NULL;
    datastart = dataend = datalimit = data = 0;
    for (int i = 0; i < dims; i++)
        size.p[i] = 0;
}

// 生成汇编
if ( v83.u ) {
    v32 = &v83.u->refcount;
    v33 = GetAndSub((unsigned int *)v32);
    if ( v33 == 1 )
        CvMatDeallocate(&v83);
}
v83.u = 0;
v34 = (int *)v83.dims;
memset(&v83.data, 0, 16); // datastart = dataend = datalimit = data = 0;
if ( v83.dims >= 1 ) {
    v34 = v83.size.p;
    v35 = 0;
    do
    {
      v34[v35++] = 0;
      v31 = v83.dims;
    }
    while ( v35 < v83.dims );
}
if ( v83.step.p != v83.step.buf )
    CvFastFree((mycv *)v83.step.p, v34);
```

```cpp
inline
Mat& Mat::operator = (Mat&& m)
{
    if (this == &m)
      return *this;

    release();
    flags = m.flags; dims = m.dims; rows = m.rows; cols = m.cols; data = m.data;
    datastart = m.datastart; dataend = m.dataend; datalimit = m.datalimit; allocator = m.allocator;
    u = m.u;
    if (step.p != step.buf) // release self step/size
    {
        fastFree(step.p);
        step.p = step.buf;
        size.p = &rows;
    }
    if (m.dims <= 2) // move new step/size info
    {
        step[0] = m.step[0];
        step[1] = m.step[1];
    }
    else
    {
        CV_DbgAssert(m.step.p != m.step.buf);
        step.p = m.step.p;
        size.p = m.size.p;
        m.step.p = m.step.buf;
        m.size.p = &m.rows;
    }
    m.flags = MAGIC_VAL; m.dims = m.rows = m.cols = 0;
    m.data = NULL; m.datastart = NULL; m.dataend = NULL; m.datalimit = NULL;
    m.allocator = NULL;
    m.u = NULL;
    return *this;
}

inline
Mat& Mat::operator = (const Mat& m)
{
    if ( this != &m )
    {
        if ( m.u )
            CV_XADD(&m.u->refcount, 1);
        release();
        flags = m.flags;
        if ( dims <= 2 && m.dims <= 2 )
        {
            dims = m.dims;
            rows = m.rows;
            cols = m.cols;
            step[0] = m.step[0];
            step[1] = m.step[1];
        }
        else
            copySize(m);
        data = m.data;
        datastart = m.datastart;
        dataend = m.dataend;
        datalimit = m.datalimit;
        allocator = m.allocator;
        u = m.u;
    }
    return *this;
}

inline
Mat::Mat(const Mat& m)
    : flags(m.flags), dims(m.dims), rows(m.rows), cols(m.cols), data(m.data),
      datastart(m.datastart), dataend(m.dataend), datalimit(m.datalimit), allocator(m.allocator),
      u(m.u), size(&rows), step(0)
{
    if ( u )
        CV_XADD(&u->refcount, 1);
    if ( m.dims <= 2 )
    {
        step[0] = m.step[0]; step[1] = m.step[1];
    }
    else
    {
        dims = 0;
        copySize(m);
    }
}

inline Mat& Mat::operator=(const Mat& m)
{
    if (this == &m)
        return *this;

    if (m.refcount)
        NCNN_XADD(m.refcount, 1);

    release();

    data = m.data;
    refcount = m.refcount;
    elemsize = m.elemsize;
    elempack = m.elempack;
    allocator = m.allocator;

    dims = m.dims;
    w = m.w;
    h = m.h;
    c = m.c;

    cstep = m.cstep;

    return *this;
}

inline void Mat::release()
{
    if (refcount && NCNN_XADD(refcount, -1) == 1)
    {
        if (allocator)
            allocator->fastFree(data);
        else
            fastFree(data);
    }

    data = 0;

    elemsize = 0;
    elempack = 0;

    dims = 0;
    w = 0;
    h = 0;
    c = 0;

    cstep = 0;

    refcount = 0;
}
```

这个 函数
sub_B1894
sub_71D00
sub_B00A8
OpenCV – 3.4.2 2018-07-04

33619968 0x2010000 (MAT+ACCESS_WRITE)
16842752 0x1010000
33882112 0x2050000
1072693248 0x3ff00000
1074266112 0x40080000
17104896 0x1050000
1124007936 0x42ff0000
1081073664 0x406fe000

1. 不能包含指针转换：`(int)`，调整为 `(int64)`，避免指针截断。
    * <https://android.googlesource.com/platform/external/swiftshader/+/refs/heads/master/CMakeLists.txt>
    * <https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-4-c4189?view=msvc-170>
    * /we4101 # 'identifier' : unreferenced local variable
    * /we4244 # 'conversion' conversion from 'type1' to 'type2', possible loss of data
    * /we4189 # 'identifier' : local variable is initialized but not referenced
    * /we4311: “类型强制转换”: 从“unsigned char *”到“DWORD”的指针截断
    * /we4302: “类型强制转换”: 从“unsigned char *”到“DWORD”截断
    * /we4312: “类型强制转换”: 从“int”转换到更大的“void *”
    * /we4267: “参数”: 从“size_t”转换到“int”，可能丢失数据
    * /we4267 /we4312 /we4101 /we4244 /we4189 /we4311 /we4302
2. 所有 `while (1)` 替换为：`while (true)`，以方便阅读。
3. 指针查找：`*(_BYTE*)(v12`，正则为 :`\*\([0-9a-zA-Z_]*?\*\)\(v`。
4. 所有 float 采用 (float)，避免限制为 double，最终 32 & 64 计算的结果造成不一致。
5. `(unsigned int)(float)` 调整为 `(int)(float)`，前面 32 & 64 汇编运算结果会不一致。

内存地址是否高位为 1，int64 的情况？应该不存在。
64 位操作系统内存值的最高位可能是 1 吗？
危险的 `(unsigned int)(float)` 强转：
```
if (outx == 0) {
    auto xxd = v25 * 255.0;
    float xxdf = (float)xxd;
    int t1 = (int)xxdf;
    int t2 = (unsigned int)xxdf; // 这里 32 系统，64 系统不一样。
    printf("v25 = %f \n", v25);
    printf("v25 = %f \n", xxd);
    printf("v25 = %f %x  %x:%x \n", xxdf, *(_DWORD*)&xxdf, t1, t2);
    printf("v25 = %x %d \n", (unsigned int)xxdf, temp);
}
```
32 位系统：
```
v25 = -0.333500
v25 = -85.042499
v25 = -85.042496 c2aa15c2  ffffffab:ffffffff
v25 = ffffffff 255
// 生成的汇编不一样，造成计算误差。
movss       xmm0,dword ptr [ebp-0C8h]
call        __ftoui3 (0F1B1708h)
mov         dword ptr [ebp-0D0h],eax
```
64 位系统：
```
v25 = -0.333500
v25 = -85.042499
v25 = -85.042496 c2aa15c2  ffffffab:ffffffab
v25 = ffffffab 171
// 生成的汇编不一样，造成计算误差。
cvttss2si   rax,dword ptr [rsp+140h]
mov         dword ptr [rsp+148h],eax
```

6BlackWhiteColor\android\54.webp.result.png
-- 这玩意每次跑出来结果不一样。
* 由于矩阵没有初始化，造成的结果波动。`memset(bkground.data, 0, bkground.step * bkground.rows);`
7SaveInk\android\78.jfif.result.png -- 这个也不一样。

* `__dmb(0xBu);` -> `__dmb(_ARM_BARRIER_ISH);`
  ```
  typedef enum _tag_ARMINTR_BARRIER_TYPE
  {
      _ARM_BARRIER_SY    = 0xF,
      _ARM_BARRIER_ST    = 0xE,
      _ARM_BARRIER_ISH   = 0xB,
      _ARM_BARRIER_ISHST = 0xA,
      _ARM_BARRIER_NSH   = 0x7,
      _ARM_BARRIER_NSHST = 0x6,
      _ARM_BARRIER_OSH   = 0x3,
      _ARM_BARRIER_OSHST = 0x2
  }
  ```

```c
cv::_OutputArray
v67.a.dims = 0; // 3
v67.a.flags = 0; // 2
v67.op = (const cv::MatOp*)33619968; // 0
v67.flags = (int)thisz; // 1
```


## 整数定数除法的代换 (constant integer division)

[除法换成乘法 3435973837 {% include relref_csdn.html %}](https://blog.csdn.net/nameofcsdn/article/details/125007289)
在 gcc 里面有一个 32-bit 的 unsigned integer x，那么 `x/10` 会被转换成 `(x*3435973837)>>35`。

```cpp
for (int i = 0; i < 10; i++) {
    int a = i * 5;
    int b = a * 3435973837;
    printf("%u %u \n", a, b);
    assert(a / 5 == b);
}
```

为了效率，已经丧心病狂了。
一个 32-bit 的 unsigned integer x，那么 `x/10` 会被转换成 `(x*3435973837)>>35`。
除以 5 等价于 乘以 3435973837。
[Shift to divide by 10 {% include relref_github.html %}](https://rgplantz.github.io/2021/11/04/Shift-to-divide-by-10.html)


## ARM 原子操作

[深入浅出 ARM 原子操作 {% include relref_csdn.html %}](https://blog.csdn.net/ce123_zhouwei/article/details/108562387)
[__ldrex and __strex intrinsics deprecated](https://developer.arm.com/documentation/dui0530/m/Migrating-from-ARM-Compiler-v5-05-to-v5-06/Compiler-changes-between-ARM-Compiler-v5-05-and-v5-06/--ldrex-and---strex-intrinsics-deprecated)

```c
int sum = 0;

int old = sum;
for (int i = 0; i < 1000000; i++) // 百万次
{
    // 如果 old 等于 sum，就把 old+1 写入 sum
    while (!__sync_bool_compare_and_swap(&sum, old, old + 1))
    {
        old = sum; // 更新 old
    }
}
```
```c
do {
    while ( 1 ) {
      __dmb();
      do {
        v2 = __ldrex((unsigned __int32 *)&sum);
        v3 = v2 == v1;
        if ( v2 != v1 )
          break;
        v4 = __strex(v1 + 1, (unsigned int *)&sum);
        v3 = v4 == 0;
      }
      while ( v4 );
      __dmb();
      if ( v3 )
        break;
      v1 = sum;
    }
    --v0;
}
while ( v0 );
```

```c
v14 = (unsigned int*)(v13 + 12); // 读取地址。
__dmb(0xBu);
do
    v15 = __ldrex(v14); // 读取值，标记独占。
while (__strex(v15 + 1, v14)); // 如果没有设置成功，继续循环。
__dmb(0xBu);
```

[ldrex 与 strex 大概处理流程 {% include relref_csdn.html %}](https://blog.csdn.net/u012294613/article/details/123183813)

在 arm 系统当中通过 LDREX 和 STREX 实现内存的原子操作，首先研究一下两条指令的语义。
其实 LDREX 和 STREX 指令，是将单纯的更新内存的原子操作分成了两个独立的步骤。
大致的流程如下，但是 ARM 内部为了实现这个功能，还有不少复杂的情况要处理。

LDREX 用来读取内存中的值，并标记对该段内存的独占访问：`LDREX Rx, [Ry]`。
上面的指令意味着，读取寄存器 Ry 指向的 4 字节内存值，将其保存到 Rx 寄存器中，同时标记对 Ry 指向内存区域的独占访问。
如果执行 LDREX 指令的时候发现已经被标记为独占访问了，并不会对指令的执行产生影响。

而 STREX 在更新内存数值时，会检查该段内存是否已经被标记为独占访问，
并以此来决定是否更新内存中的值：`STREX Rx, Ry, [Rz]`。
如果执行这条指令的时候发现已经被标记为独占访问了，则将寄存器 Ry 中的值更新到寄存器 Rz 指向的内存，
并将寄存器 Rx 设置成 0。指令执行成功后，会将独占访问标记位清除。
而如果执行这条指令的时候发现没有设置独占标记，则不会更新内存，且将寄存器 Rx 的值设置成 1。
一旦某条 STREX 指令执行成功后，以后再对同一段内存尝试使用 STREX 指令更新的时候，
会发现独占标记已经被清空了，就不能再更新了，从而实现独占访问的机制。


## Hey, there! Enjoy!

Hey, there! Welcome to my blog. I hope you enjoy reading the stuff in here.
Nothing fancy, really. Just bits and bobs about tech and random topics.

```cpp
wchar_t* pstr = nullptr;
CString exe = pstr; // 不会崩溃。
exe.Append(L"test");

// 0xC0000005: 读取位置 0x00000000 时发生访问冲突。
std::wstring tempexe = pstr; // 会崩溃。
tempexe.append(L"test");
```

两个崩溃：
1. `std::string = null;`
2. `CString str; GetWindowsText(hWnd, str.GetBuffer(/* 没有指定大小 */), MAX_PATH);`

```cpp
bool endsWith(const CString& str, const CString& suffix, bool ignoreCase)
{
    int totalSize = str.GetLength();
    int suffixSize = suffix.GetLength();
    if (totalSize < suffixSize) {
        return false;
    }
    if (ignoreCase) {
        return str.Right(suffixSize).CompareNoCase(suffix) == 0;
    }
    return str.Right(suffixSize).Compare(suffix) == 0;
}
```

Windows 内存状态：
```cpp
__int64 winMemoCtrl() {
    MEMORYSTATUSEX memory_status;
    memory_status.dwLength = sizeof(memory_status);
    GlobalMemoryStatusEx(&memory_status);

    if (memory_status.ullAvailPhys <= 500 * 1024 * 1024) {
        return 30 * 1024 * 1024;
    }

    return 100 * 1024 * 1024;
}
```


## Android Studio

Android ARGB_8888 格式图片的各通道顺序其实不是 ARGB，而是 RGBA。

[Android 历史版本](https://developer.android.google.cn/studio/archive.html)
* E:\android-studio-2021.3.1.17-windows.exe
    * 最新版本，老手机（HUAWEI MT7-TL00 Android 5.1.1 API 22）无法调试 C++。
    * 新小手机（OPPO PBCM30 Android 10，API 29）可以调试。
* E:\android-studio-20191205-3.5.3-ide-191.6010548-windows.exe
    * 无法 load 起来。
* E:\android-studio-20200224-3.6-ide-192.6200805-windows.exe
    * 没有过多尝试。
* E:\android-studio-20210119-4.1.2-ide-201.7042882-windows.exe
    * 最终貌似是这个版本。
    * This version of the Android Support plugin for IntelliJ IDEA (or Android Studio)
        cannot open this project, please retry with version 2021.2.1 or newer.
        * 不能打开主工程，那玩意太新了。
    * No toolchains found in the NDK toolchains folder for ABI with prefix: arm-linux-androideabi
        * classpath "com.android.tools.build:gradle:4.1.3"

guide 原版 Android。
result，pc 32 版本，64 作为对照组。
android 文件夹，self android 32 版本，64 作为对照组。


## 操作系统和编译器预定义宏

**操作系统预定义宏：**

操作系统 | 公共定义 | 64 位系统定义
Windows | \_WIN32 | \_WIN64
macOS | \_\_APPLE\_\_ | \_\_LP64\_\_
Linux | \_\_linux\_\_ | \_\_LP64\_\_
Android | \_\_ANDROID\_\_ | \_\_LP64\_\_

**编译器预定义宏（指令集）：**

**编译器** | **编译器定义** | **x86** | **AMD64** | **ARM32** | **Thumb** | **ARM64**
MSVC | \_MSC\_VER | \_M\_IX86 | \_M\_X64 | \_M\_ARM | \_M\_THUMB | \_M\_ARM64
GCC | \_\_GNUC\_\_ | \_\_i386\_\_ | \_\_x86\_64\_\_ | \_\_arm\_\_ | \_\_thumb\_\_ | \_\_aarch64\_\_
Clang | \_\_clang\_\_ | \_\_i386\_\_ | \_\_x86\_64\_\_ | \_\_arm\_\_ | \_\_thumb\_\_ | \_\_aarch64\_\_


## C++ 数据类型

```cpp
printf("char | %d \n", sizeof(char));
printf("short | %d \n", sizeof(short));
printf("int | %d \n", sizeof(int));
printf("long | %d \n", sizeof(long));
printf("long long | %d \n", sizeof(long long));
printf("__int64 | %d \n", sizeof(__int64));
printf("float | %d \n", sizeof(float));
printf("double | %d \n", sizeof(double));
printf("long double | %d \n", sizeof(long double));
printf("void* | %d \n", sizeof(void*));
```

* **主要就是指针和 int 的问题。**

类型 | 32 | 64
---- | --- | ---
char | 1 | 1
short | 2 | 2
int | 4 | 4
long | 4 | 4
long long | 8 | 8
int64 | 8 | 8
float | 4 | 4
double | 8 | 8
long double | 8 | 8
void\* | 4 | 8

[note {% include relref_cnblogs.html %}](https://www.cnblogs.com/flowerslip/p/5934718.html)
补码最大好处就是不管是有符号数还是无符号数都可以用同一套加减法。
有符号数和无符号数在计算机里表示都是一样的，二进制的补码形式。
是有符号还是无符号，是编译器来辨认的。
* 赋值截断问题
    * 等长直接赋值，变短直接截断，变长如果正前补 0，为负前补 1，浮点数同理。
* 运算问题
    * 汇编是不区分正负数字的。溢出不溢出，是由程序员判断的，机器不知道。
* 判等问题
    * `movsx eax,byte ptr [a]` 先符号扩展，再传送
    * `movzx ecx,byte ptr [b]` 先零扩展，再传送
    * `cmp eax,ecx`


## C/C++ 中 float 的内存结构

[note {% include relref_csdn.html %}](https://blog.csdn.net/u011700339/article/details/89302321)
**float 的内存结构**
一个 32 位的 float 数和一个 64 位 double 数的存储主要分为三部分：符号位，指数位，尾数位。
以 float 数为例：
1. 符号位 (sign)：1 个 bit，0 代表正数，1 代表负数（这里和整数一致，所以汇编可以直接判断正负）
2. 指数位 (exponent)：8 个 bit，范围 \-127~128，用于存储科学计数法中的指数部分，并且采用以为存储方式，所存储的数据为原数据 \+127
3. 尾数位 (mantissa)：23bit，用于存储尾数部分
{% include image.html url="/assets/images/210914-tiny-source-code/20190414202611812.png" %}
float 数的表示形式：
$$pow(−1,sign)*(1+mag)*pow(2,exp−127)$$


## 剪贴板

```
#include <windows.h>
#include <iostream>
```

复制：
```cpp
if (OpenClipboard())
{
    HGLOBAL hGBClipboard;
    char *chBufferText;
    EmptyClipboard();
    hGBClipboard = GlobalAlloc(GMEM_DDESHARE, strClipboardText.GetLength() + 1);
    chBufferText = (char*)GlobalLock(hGBClipboard);
    strcpy(chBufferText, LPCSTR(strClipboardText));
    GlobalUnlock(hGBClipboard);
    SetClipboardData(CF_TEXT, hGBClipboard);
    CloseClipboard();
}
```

粘贴：
```cpp
if (OpenClipboard())
{
    HANDLE hClipboardData = GetClipboardData(CF_TEXT);
    char *chBufferText = (char*)GlobalLock(hClipboardData);
    strClipboardText = chBufferText;
    GlobalUnlock(hClipboardData);
    CloseClipboard();
}
```


## 主线程断言

```cpp
#include <assert.h>
#include <Windows.h>
#include <TlHelp32.h>
BOOL GetCurrentMainThreadID(DWORD* pdwThreadID)
{
    HANDLE hThreadSnap = INVALID_HANDLE_VALUE;
    BOOL bRet = FALSE;
    THREADENTRY32 te32 = {0};
    DWORD dwProcessId = 0;
    static DWORD Curl_dwMainThreadId = 0;

    if (!pdwThreadID) {
        return FALSE;
    }
    if (Curl_dwMainThreadId) {
        *pdwThreadID = Curl_dwMainThreadId;
        return TRUE;
    }

    dwProcessId = GetCurrentProcessId();
    //  Take a snapshot of all processes in the system.
    hThreadSnap = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0);
    if (hThreadSnap == INVALID_HANDLE_VALUE)
    {
        return FALSE;
    }

    //  Fill in the size of the structure before using it.
    te32.dwSize = sizeof(THREADENTRY32);
    if (Thread32First(hThreadSnap, &te32))
    {
        if (te32.th32OwnerProcessID == dwProcessId)
        {
            *pdwThreadID = te32.th32ThreadID;
            Curl_dwMainThreadId = te32.th32ThreadID;
            bRet = TRUE;
        }
    }
    while (!bRet && Thread32Next(hThreadSnap, &te32))
    {
        if (te32.th32OwnerProcessID == dwProcessId)
        {
            *pdwThreadID = te32.th32ThreadID;
            Curl_dwMainThreadId = te32.th32ThreadID;
            bRet = TRUE;
        }
    }

    // Do not forget to clean up the snapshot object.
    CloseHandle (hThreadSnap);
    return bRet;
}

void CheckAssertMainThread() {
#if _DEBUG
    DWORD dwThreadID = 0;
    if (GetCurrentMainThreadID(&dwThreadID)) {
        assert(dwThreadID != GetCurrentThreadId());
    }
#endif
}
```


## ToySingleInstance.hpp

```cpp
#pragma once

#ifndef __TOY_SINGLEINSTANCE_H__
#define __TOY_SINGLEINSTANCE_H__

#include <Windows.h>
#include <atlstr.h>

namespace toy
{
    class ToySingleInstance
    {
    public:
        ToySingleInstance(LPCTSTR strName)
            : m_hMutex(NULL)
            , m_strInstanceName(strName)
        {

        }

        ~ToySingleInstance()
        {
            Close();
        }

        BOOL IsExist()
        {
            HANDLE hMutex = ::OpenMutex(SYNCHRONIZE, FALSE, m_strInstanceName);
            if (hMutex)
            {
                ::CloseHandle(hMutex);
                return TRUE;
            }
            return FALSE;
        }

        BOOL Create()
        {
            if (IsExist())
                return FALSE;

            HANDLE hMutex = CreateMutex(
                NULL,
                TRUE,
                m_strInstanceName
            );

            if (hMutex == NULL)
            {
                return FALSE;
            }
            else if (GetLastError() == ERROR_ALREADY_EXISTS)
            {
                ::CloseHandle(hMutex);
                return FALSE;
            }

            m_hMutex = hMutex;
            hMutex = NULL;

            return TRUE;
        }

        VOID Close()
        {
            if (m_hMutex)
            {
                CloseHandle(m_hMutex);
                m_hMutex = NULL;
            }
        }

    private:
        CString m_strInstanceName;
        HANDLE m_hMutex;
    };

}

#endif
```


## crc64

from opencv ocl.cpp
```cpp
typedef uint32_t        uint;
typedef signed char     schar;
typedef unsigned char   uchar;
typedef unsigned short  ushort;
typedef int64_t         int64;
typedef uint64_t        uint64;
#define CV_BIG_INT(n)   n##LL
#define CV_BIG_UINT(n)  n##ULL

// Computes 64-bit "cyclic redundancy check" sum, as specified in ECMA-182
uint64 crc64(const uchar* data, size_t size, uint64 crcx)
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
```


## bsearch & qsort

* <https://www.tutorialspoint.com/c_standard_library/c_function_bsearch.htm>
* <https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm>

```c
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
qsort(ali, size, sizeof(int), compare);
qsort(values, 5, sizeof(int), cmpfunc);
```

```cpp
#include <stdio.h>
#include <stdlib.h>

int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int values[] = { 5, 20, 29, 32, 63 };

int main () {
   int *item;
   int key = 32;

   /* using bsearch() to find value 32 in the array */
   item = (int*) bsearch (&key, values, 5, sizeof (int), cmpfunc);
   if ( item != NULL ) {
      printf("Found item = %d\n", *item);
   } else {
      printf("Item = %d could not be found\n", *item);
   }

   return(0);
}
```


## log C#

```c#
using System.IO;
using System.Diagnostics;

private static bool m_bLocalDebug = true;

public static void WriteLog(string strLog)
{
    if (!m_bLocalDebug) {
        return;
    }
    string sFilePath = "D:\\" + DateTime.Now.ToString("yyyyMM");
    string sFileName = "logfile" + Process.GetCurrentProcess().Id + "-" + DateTime.Now.ToString("dd") + ".log";
    sFileName = sFilePath + "\\" + sFileName; // 文件的绝对路径
    if (!Directory.Exists(sFilePath)) { // 验证路径是否存在
        Directory.CreateDirectory(sFilePath);
    }
    FileStream fs;
    bool create = false;
    if (File.Exists(sFileName)) {
        fs = new FileStream(sFileName, FileMode.Append, FileAccess.Write);
    }  else {
        fs = new FileStream(sFileName, FileMode.Create, FileAccess.Write);
        create = true;
    }
    StreamWriter sw = new StreamWriter(fs);
    if (create) {
        String commandLineString = System.Environment.CommandLine;
        String[] args = System.Environment.GetCommandLineArgs();
        sw.WriteLine(commandLineString);
        for (int i = 0; i < args.Length; i++) {
            sw.WriteLine(args[i]);
        }
        sw.WriteLine("--------");
    }
    sw.WriteLine(DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + "   ---   " + strLog);
    sw.Close();
    fs.Close();
}
```


## log C++

```cpp
FILE *fp = NULL;
fp = fopen("D:\\camera.txt", "a");
if (fp)
{
    fprintf(fp, "%s %d \n", __FILE__, __LINE__);
    fclose(fp);
}

FILE* fp = NULL;
errno_t err = fopen_s(&fp, "E:\\irrlicht.txt", "a");
if (err == 0 && fp)
{
    fprintf(fp, "%s@x\n", lpcstr);
    fclose(fp);
}

char fpath[1024] = "";
_fullpath(fpath, fileLocation, 1024);
```

```c
{ // C 版本。#include <locale>
    setlocale(LC_ALL, "chs");
    FILE* fp = NULL;
    errno_t err = fopen_s(&fp, "E:\\curl.txt", "a");
    if (err == 0 && fp)
    {
        fwprintf(fp, L"%s\n", szUrl);
        for (int i = 0; i < nSize; i++) {
            fputc(pBuffer[i], fp);
        }
        fputc('\n', fp);
        fclose(fp);
    }
}
```


## C++ File

* ‘r’ 读
* ‘w’ 写
* ‘a’ 追加
* ‘r+’ == r+w（读写，可读可写，文件若不存在就报错 IOError）
* ‘w+’ == w+r（写读，可读可写，文件若不存在就创建）
* ‘a+’ == a+r（可追加可写，文件若不存在就创建）
* 对应的，如果是二进制文件，需要加一个 b：
* ‘rb’　　‘wb’　　‘ab’　　‘rb+’　　‘wb+’　　‘ab+’
* 注意！‘w’会抹去文件原有的内容，如果只是加新的内容应该用‘a’

```cpp
long getfilesize(const char* fpath) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return -1;
    fseek(fs, 0, SEEK_END);
    long length = ftell(fs);
    // rewind(fs);
    fclose(fs);
    return length;
}

bool readfileSeek(const char* fpath, char* buffer, long readsize, long seek) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return false;
    fseek(fs, seek, SEEK_SET);
    fread(buffer, 1, readsize, fs);
    fclose(fs);
    return true;
}

char* readfile(const char* fpath, long& length) {
    FILE* fs = fopen(fpath, "rb");
    assert(fs);
    if (!fs) return nullptr;
    fseek(fs, 0, SEEK_END);
    length = ftell(fs);
    rewind(fs);
    char* data = new char[length + 1];
    fread(data, 1, length, fs);
    data[length] = 0;
    fclose(fs);
    return data;
}

// 返回开始写文件的地址偏移。
long appendfile(const char* fpath, const char* data, long length) {
    FILE* fs = fopen(fpath, "ab");
    assert(fs);
    if (!fs) return -1;
    fseek(fs, 0, SEEK_END);
    long offset = ftell(fs);
    fwrite(data, 1, length, fs);
    fclose(fs);
    return offset;
}
```

```c++
bool IsFileRegular(const std::string &path) {
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISREG(st.st_mode);
}

bool IsDirectory(const std::string &path)
{
    struct stat st;
    if (stat(path.c_str(), &st))
        return false;
    return S_ISDIR(st.st_mode);
}

bool IsFilePathExists(const char* path, bool exdir) // exdir 表示进行文件夹检查，不能是 文件夹
{
    // 如果指定的存取方式有效，则函数返回 0，否则函数返回 -1。
    int code = ::access(path, 0);
    if (0 == code) {
        if (exdir && IsDirectory(path)) {
            return false;
        }
        return true;
    }
    return false;
}

bool CreateDeepDirectory(const char* szPath)
{
    if (IsDirectory(szPath)) {
        return true;
    }
    if (IsFilePathExists(szPath, false))
        return false;

#ifdef __ANDROID__
    if (0 != ::mkdir(szPath, 0777))
#else
    if (0 != ::mkdir(szPath))
#endif
    {
        StringDup strPath(szPath);
        if (!PathRemoveFileName(strPath) || IsFilePathEmpty(strPath)) {
            return false;
        }

        if (!CreateDeepDirectory(strPath))
            return false;

#ifdef __ANDROID__
        if (0 != ::mkdir(szPath, 0777))
#else
        if (0 != ::mkdir(szPath))
#endif
            return false;
    }
    return true;
}

std::string GetAbsolutePath(const std::string& filename)
{
    if (filename.empty())
        return filename;
#if defined(_WIN32)
    char fpath[_MAX_PATH] = { 0 };
    char* p = _fullpath(fpath, filename.c_str(), _MAX_PATH);
    std::string tmp(p);
    return tmp;
#else
    char fpath[4096] = { 0 };
    char* p = realpath(filename.c_str(), fpath);
    std::string tmp(p);
    return tmp;
#endif
}
```


## C++ String

On Windows, `wchar_t` is UTF-16 while on other platform such as Linux and MacOS, `wchar_t` is UTF-32!
[link](https://codingtidbit.com/2020/02/09/c17-codecvt_utf8-is-deprecated/)

```cpp
#include <string>
#include <sstream>

template<typename T>
inline std::string stringify(const T& x)
{
    std::ostringstream o;
    if (!(o << x)) return "";
    return o.str();
}

template<typename T>
inline T fromString(char *s)
{
    std::string str = s;
    std::istringstream i(str);
    T x;
    i >> x;
    return x;
}
```

```cpp
#include "stdafx.h"
#include <assert.h>
#include <string>

// C++17: codecvt_utf8 is deprecated
// std::wstring_convert<std::codecvt_utf8<wchar_t>> strConvert;

// 有的字符串可能会编码失败。
std::wstring CharToWChar(const char* str, size_t encode) {
    if (!str)
        return L"";
    int srclen = strlen(str);
    int len = MultiByteToWideChar(encode, 0, str, srclen, NULL, 0);
    if (len <= 0) {
        return L"";
    }
    wchar_t* temp = new wchar_t[len + 1];
    MultiByteToWideChar(encode, 0, str, srclen, temp, len);
    temp[len] = '\0';
    std::wstring wstr = temp;
    delete[] temp;
    return wstr;
}

// 有的字符串可能会编码失败。
std::string WCharToChar(const wchar_t* wstr, size_t encode) {
    if (!wstr)
        return "";
    int srclen = wcslen(wstr);
    int len = WideCharToMultiByte(encode, 0, wstr, srclen, NULL, 0, NULL, NULL);
    if (len <= 0) {
        return "";
    }
    char* temp = new char[len + 1];
    WideCharToMultiByte(encode, 0, wstr, srclen, temp, len, NULL, NULL);
    temp[len] = '\0';
    std::string str = temp;
    delete[] temp;
    return str;
}

std::string UTF8_ENCODE(const wchar_t* wstr) {
    if (!wstr)
        return "";
    return WCharToChar(wstr, CP_UTF8);
}
std::wstring UTF8_DECODE(const char* str) {
    if (!str)
        return L"";
    return CharToWChar(str, CP_UTF8);
}
```


## 字符串加解密

这个存在缺陷，如果转码失败会不可逆：

```cpp
wchar_t bkHexWChar(const wchar_t* buffer, int cntlen = 4) {
    wchar_t* num = new wchar_t[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(wchar_t));
    num[cntlen] = 0;
    wchar_t ch = wcstol(num, NULL, 16);
    delete[] num;
    return ch;
}

int bkHexChar(const char* buffer, int cntlen = 2) {
    char* num = new char[cntlen + 1];
    memcpy(num, buffer, cntlen * sizeof(char));
    num[cntlen] = 0;
    int ch = strtol(num, NULL, 16);
    delete[] num;
    return ch;
}

CString toHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    const int length = strk.length();
    const char* buffer = strk.c_str();
    assert(length >= 0 && length <= 0xffff);
    CString retv;
    retv.AppendFormat(L"%04x", length);
    for (int i = 0; i < length; i++) {
        // 宽字符型 wchar_t (unsigned short.)
        // wchar_t ch = buffer[i];
        // assert(ch >= 0 && ch <= 0xffff);
        unsigned char ch = buffer[i];
        assert(ch >= 0 && ch <= 0xff);
        retv.AppendFormat(L"%02x", ch);
    }
    return retv;
}

CString bkHexString(CString str) {
    std::string strk = WCharToChar(str.GetString());
    int srclen = strk.length();
    assert((srclen - 4) % 2 == 0 && srclen >= 4);
    if ((srclen - 4) % 2 != 0 || srclen < 4) {
        return L"";
    }
    const char* buffer = strk.c_str();
    const int length = bkHexChar(&buffer[0], 4);
    assert(length == (srclen - 4) / 2);
    if (length != (srclen - 4) / 2) {
        return L"";
    }
    CStringA retv;
    for (int i = 0; i < length; i++) {
        char ch = bkHexChar(&buffer[4 + i * 2]);
        retv.AppendChar(ch);
    }
    std::wstring temp = CharToWChar(retv.GetString());
    CString wstr = temp.c_str();
    return wstr;
}

int _tmain(int argc, _TCHAR* argv[])
{
    CString test = L"中文 123";

    test = toHexString(test);
    test = bkHexString(test);

    test = bkHexString(L"0004ffffff01");
    test = toHexString(test);
    return 0;
}
```

这个方案，加密字符串长一点，但是肯定没问题：

<div class="highlighter-rouge" foldctrl="1"></div>

```cpp
#include <assert.h>

#define ALG_TYPE 0x07

class b62 {
  public:
    static int ParseBase62(wchar_t ch) {
        if (ch >= L'0' && ch <= L'9') {
            return ch - L'0';
        }
        if (ch >= L'a' && ch <= L'z') {
            return ch - L'a' + 10;
        }
        if (ch >= L'A' && ch <= L'Z') {
            return ch - L'A' + 10 + 26;
        }
        return -1;
    }

    static int appendHex(CString& retv, unsigned long value) {
        int len = 0;
        for (unsigned long temp = value; len == 0 || temp; temp /= 62) {
            len++;
        }

        static wchar_t SZ_BASE62_TAB[] = L"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        retv.AppendChar(SZ_BASE62_TAB[len]);
        for (int i = 0; i < len; i++) {
            int node = value % 62;
            retv.AppendChar(SZ_BASE62_TAB[node]);
            value /= 62;
        }
        return len;
    }

    static unsigned long eatupHex(const wchar_t* ptr, unsigned int& index) {
        int len = ParseBase62(ptr[index++]);
        unsigned long value = 0;
        unsigned long mulval = 1;
        for (int i = 0; i < len; i++) {
            int node = ParseBase62(ptr[index++]);
            value += node * mulval;
            mulval *= 62;
        }
        return value;
    }

    static CString toHexString(CString str) {
        const int length = str.GetLength();
        const wchar_t* buffer = str.GetString();

        CString retv;
        appendHex(retv, ALG_TYPE);
        appendHex(retv, length);
        wchar_t check = 0;
        for (int i = 0; i < length; i++) {
            wchar_t ch = buffer[i]; // <= 0xffff
            appendHex(retv, ch ^ ALG_TYPE);
            check ^= ch;
        }
        appendHex(retv, check);
        return retv;
    }

    static CString bkHexString(CString str) {
        unsigned int index = 0;

        const wchar_t* buffer = str.GetString();
        const int algType = eatupHex(buffer, index);
        if (algType != ALG_TYPE) {
            return L"??<unknow type>";
        }

        CString retv;
        wchar_t check = 0;
        const int length = eatupHex(buffer, index);
        for (int i = 0; i < length; i++) {
            wchar_t ch = eatupHex(buffer, index) ^ ALG_TYPE;
            retv.AppendChar(ch);
            check ^= ch;
        }

        wchar_t checkz = eatupHex(buffer, index);
        assert(checkz == check);
        if (checkz != check) {
            return L"??<check error>";
        }
        return retv;
    }

}; // namespace b62
```


### 拍脑袋最终版本

Base64 编码是使用 64 个可打印 ASCII 字符（A-Z、a-z、0-9、+、/）将任意字节序列数据编码成 ASCII 字符串，另有“=”符号用作后缀用途。
因为 Base64 算法是将 3 个字节原数据编码为 4 个字节新数据，所以 Base64 编码后的数据比原始数据略长，为原来的 4/3。

两个变种：
1. 用于 URL 的改进 Base64 编码，它在末尾填充 '=' 号，并将标准 Base64 中的“+”和“/”分别改成了“-”和“_”。
2. 用于正则表达式的改进 Base64 变种，它将“+”和“/”改成了“!”和“-”。

* 设计一种编码，编码出来只有 62 个字符，并且尽可能短，每个字符独立编码，支持按字符检索。
* 62 编码，采取 59（质数）进制，XYZ 作为扩展标记。最短能从 16 进制得长度缩短到原来的 3/4 长度。
* 16 进制一次编码 4 bit，59 进制一次大概编码 6 bit。
* <= 58: 直接解析
* \>= 59: XYZ 打头扩展编码。

单独一篇文章，验证这个问题：
[实现 62 个字符的 Base64 编码]({% include relref.html url="/blog/2022/03/16/b62-at-base64" %})

```c++
/**
 * 设计一种编码，编码出来只有 62 个字符，并且尽可能短，每个字符独立编码，支持按字符检索。
 * 62 编码，采取 59（质数）进制，XYZ 作为扩展标记。最短能从 16 进制得长度缩短到原来的 3/4 长度。
 * 16 进制一次编码 4 bit，59 进制一次大概编码 6 bit。
 * <= 58: 直接解析
 * >= 59: XYZ 打头扩展编码。
 */
```

```
0 0 0
3a 58 W
3b 59 X0
75 117 XW
76 118 Y00
e0e 3598 YWW
e0f 3599 Z000
33051 208977 ZWWW
33052 208978 Z00X0
65294 414356 ZWWXW
65295 414357 Z00Y00
ffffe 1048574 ZqbY53
fffff 1048575 ZrbY53
0 0 P12000
```


## StringHelper

```cpp
#pragma once

#include <string>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <cctype>
#include <algorithm>

class StringHelper
{
public:
    static std::wstring toLower(std::wstring source)
    {
        std::transform(source.begin(), source.end(), source.begin(), [](unsigned char c){ return std::tolower(c); });
        return source;
    }

    static std::wstring toUpper(std::wstring source)
    {
        std::transform(source.begin(), source.end(), source.begin(), [](unsigned char c){ return std::toupper(c); });
        return source;
    }

    static std::wstring trimStart(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return source.erase(0, source.find_first_not_of(trimChars));
    }

    static std::wstring trimEnd(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return source.erase(source.find_last_not_of(trimChars) + 1);
    }

    static std::wstring trim(std::wstring source, const std::wstring &trimChars = L" \t\n\r\v\f")
    {
        return trimStart(trimEnd(source, trimChars), trimChars);
    }

    static std::wstring replace(std::wstring source, const std::wstring &find, const std::wstring &replace)
    {
        std::size_t pos = 0;
        while ((pos = source.find(find, pos)) != std::wstring::npos)
        {
            source.replace(pos, find.length(), replace);
            pos += replace.length();
        }
        return source;
    }

    static bool startsWith(const std::wstring &source, const std::wstring &value)
    {
        if (source.length() < value.length())
            return false;
        else
            return source.compare(0, value.length(), value) == 0;
    }

    static bool endsWith(const std::wstring &source, const std::wstring &value)
    {
        if (source.length() < value.length())
            return false;
        else
            return source.compare(source.length() - value.length(), value.length(), value) == 0;
    }

    static std::vector<std::wstring> split(const std::wstring &source, wchar_t delimiter)
    {
        std::vector<std::wstring> output;
        std::wistringstream ss(source);
        std::wstring nextItem;

        while (std::getline(ss, nextItem, delimiter))
        {
            output.push_back(nextItem);
        }

        return output;
    }

    template<typename T>
    static std::wstring toString(const T& subject)
    {
        std::wostringstream ss;
        ss << subject;
        return ss.str();
    }

    template<typename T>
    static std::string toStringA(const T& subject)
    {
        std::ostringstream ss;
        ss << subject;
        return ss.str();
    }

    template<typename T>
    static T fromString(const std::wstring &subject)
    {
        std::wistringstream ss(subject);
        T target;
        ss >> target;
        return target;
    }

    template<typename T>
    static T fromStringA(const std::string &subject)
    {
        std::istringstream ss(subject);
        T target;
        ss >> target;
        return target;
    }

    static bool isEmptyOrWhiteSpace(const std::wstring &source)
    {
        if (source.length() == 0)
            return true;
        else
        {
            for (std::size_t index = 0; index < source.length(); index++)
            {
                if (!std::isspace(source[index]))
                    return false;
            }

            return true;
        }
    }
};
```

```cpp
class StringHelper
{
public:
    template<typename T>
    static std::wstring formatSimple(const std::wstring &input, T arg)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T>
    static std::wstring formatSimple(const std::wstring &input, const std::vector<T> &args)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;
                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    ss << args[std::stoi(index)];
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T1, typename T2>
    static std::wstring formatSimple(const std::wstring &input, T1 arg1, T2 arg2)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg1;
                    else if (index == L"1")
                        ss << arg2;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }

    template<typename T1, typename T2, typename T3>
    static std::wstring formatSimple(const std::wstring &input, T1 arg1, T2 arg2, T3 arg3)
    {
        std::wostringstream ss;
        std::size_t lastCloseBrace = std::wstring::npos;
        std::size_t openBrace = std::wstring::npos;
        while ((openBrace = input.find(L'{', openBrace + 1)) != std::wstring::npos)
        {
            if (openBrace + 1 < input.length())
            {
                if (input[openBrace + 1] == L'{')
                {
                    openBrace++;
                    continue;
                }

                std::size_t closeBrace = input.find(L'}', openBrace + 1);
                if (closeBrace != std::wstring::npos)
                {
                    ss << input.substr(lastCloseBrace + 1, openBrace - lastCloseBrace - 1);
                    lastCloseBrace = closeBrace;

                    std::wstring index = trim(input.substr(openBrace + 1, closeBrace - openBrace - 1));
                    if (index == L"0")
                        ss << arg1;
                    else if (index == L"1")
                        ss << arg2;
                    else if (index == L"2")
                        ss << arg3;
                    else
                        throw std::runtime_error("Only simple positional format specifiers are handled by the 'formatSimple' helper method.");
                }
            }
        }

        if (lastCloseBrace + 1 < input.length())
            ss << input.substr(lastCloseBrace + 1);

        return ss.str();
    }
};
```


## pystring

```cpp
#ifndef INCLUDED_PYSTRING_H
#define INCLUDED_PYSTRING_H

#include <string>
#include <vector>

namespace pystring
{
    #define MAX_32BIT_INT 2147483647

    bool startswith( const std::string & str, const std::string & prefix, int start = 0, int end = MAX_32BIT_INT );
    bool endswith( const std::string & str, const std::string & suffix, int start = 0, int end = MAX_32BIT_INT );

    std::string strip( const std::string & str, const std::string & chars = "" );
    std::string lstrip( const std::string & str, const std::string & chars = "" );
    std::string rstrip( const std::string & str, const std::string & chars = "" );

    std::string upper( const std::string & str );
    std::string lower( const std::string & str );

    std::string mul( const std::string & str, int n);
    std::string join( const std::string & str, const std::vector< std::string > & seq );
    void split( const std::string & str, std::vector< std::string > & result, const std::string & sep = "", int maxsplit = -1);
    void splitlines(  const std::string & str, std::vector< std::string > & result, bool keepends = false );

    std::string replace( const std::string & str, const std::string & oldstr, const std::string & newstr, int count = -1);

    bool isalnum( const std::string & str );
    bool isalpha( const std::string & str );
    bool isdigit( const std::string & str );
    bool isspace( const std::string & str );
    bool islower( const std::string & str );
    bool isupper( const std::string & str );

namespace os
{
namespace path
{
    std::string basename(const std::string & path);
    std::string dirname(const std::string & path);
    std::string abspath(const std::string & path, const std::string & cwd);
    std::string join(const std::string & path1, const std::string & path2);
    std::string join(const std::vector< std::string > & paths);
    std::string normpath(const std::string & path);
    void split(std::string & head, std::string & tail, const std::string & path);
} // namespace path
} // namespace os

} // namespace pystring

#endif
```

```cpp
#include "pystring.h"

#include <algorithm>
#include <cctype>
#include <cstring>
#include <iostream>
#include <sstream>

namespace pystring
{

#if defined(_WIN32) || defined(_WIN64) || defined(_WINDOWS) || defined(_MSC_VER)
#ifndef WINDOWS
#define WINDOWS
#endif
#endif

typedef int Py_ssize_t;
const std::string forward_slash = "/";
const std::string double_forward_slash = "//";
const std::string triple_forward_slash = "///";
const std::string double_back_slash = "\\";
const std::string empty_string = "";
const std::string dot = ".";
const std::string double_dot = "..";
const std::string colon = ":";

#define ADJUST_INDICES(start, end, len)     \
    if (end > len)                          \
        end = len;                          \
    else if (end < 0) {                     \
        end += len;                         \
        if (end < 0)                        \
        end = 0;                            \
    }                                       \
    if (start < 0) {                        \
        start += len;                       \
        if (start < 0)                      \
        start = 0;                          \
    }

    namespace {

        void split_whitespace( const std::string & str, std::vector< std::string > & result, int maxsplit )
        {
            std::string::size_type i, j, len = str.size();
            for (i = j = 0; i < len; )
            {
                while ( i < len && ::isspace( str[i] ) ) i++;
                j = i;

                while ( i < len && ! ::isspace( str[i]) ) i++;

                if (j < i)
                {
                    if ( maxsplit-- <= 0 ) break;

                    result.push_back( str.substr( j, i - j ));

                    while ( i < len && ::isspace( str[i])) i++;
                    j = i;
                }
            }
            if (j < len)
            {
                result.push_back( str.substr( j, len - j ));
            }
        }

    } // anonymous namespace

    void split( const std::string & str, std::vector< std::string > & result, const std::string & sep, int maxsplit )
    {
        result.clear();

        if ( maxsplit < 0 ) maxsplit = MAX_32BIT_INT;//result.max_size();

        if ( sep.size() == 0 )
        {
            split_whitespace( str, result, maxsplit );
            return;
        }

        std::string::size_type i,j, len = str.size(), n = sep.size();

        i = j = 0;

        while ( i+n <= len )
        {
            if ( str[i] == sep[0] && str.substr( i, n ) == sep )
            {
                if ( maxsplit-- <= 0 ) break;

                result.push_back( str.substr( j, i - j ) );
                i = j = i + n;
            }
            else
            {
                i++;
            }
        }

        result.push_back( str.substr( j, len-j ) );
    }

    #define LEFTSTRIP 0
    #define RIGHTSTRIP 1
    #define BOTHSTRIP 2

    std::string do_strip( const std::string & str, int striptype, const std::string & chars  )
    {
        Py_ssize_t len = (Py_ssize_t) str.size(), i, j, charslen = (Py_ssize_t) chars.size();

        if ( charslen == 0 )
        {
            i = 0;
            if ( striptype != RIGHTSTRIP )
            {
                while ( i < len && ::isspace( str[i] ) )
                {
                    i++;
                }
            }

            j = len;
            if ( striptype != LEFTSTRIP )
            {
                do
                {
                    j--;
                }
                while (j >= i && ::isspace(str[j]));

                j++;
            }

        }
        else
        {
            const char * sep = chars.c_str();

            i = 0;
            if ( striptype != RIGHTSTRIP )
            {
                while ( i < len && memchr(sep, str[i], charslen) )
                {
                    i++;
                }
            }

            j = len;
            if (striptype != LEFTSTRIP)
            {
                do
                {
                    j--;
                }
                while (j >= i &&  memchr(sep, str[j], charslen)  );
                j++;
            }

        }

        if ( i == 0 && j == len )
        {
            return str;
        }
        else
        {
            return str.substr( i, j - i );
        }

    }

    std::string strip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, BOTHSTRIP, chars );
    }

    std::string lstrip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, LEFTSTRIP, chars );
    }

    std::string rstrip( const std::string & str, const std::string & chars )
    {
        return do_strip( str, RIGHTSTRIP, chars );
    }

    std::string join( const std::string & str, const std::vector< std::string > & seq )
    {
        std::vector< std::string >::size_type seqlen = seq.size(), i;

        if ( seqlen == 0 ) return empty_string;
        if ( seqlen == 1 ) return seq[0];

        std::string result( seq[0] );

        for ( i = 1; i < seqlen; ++i )
        {
            result += str + seq[i];

        }
        return result;
    }

    namespace
    {
        /* Matches the end (direction >= 0) or start (direction < 0) of self
         * against substr, using the start and end arguments. Returns
         * -1 on error, 0 if not found and 1 if found.
         */

        int _string_tailmatch(const std::string & self, const std::string & substr,
                              Py_ssize_t start, Py_ssize_t end,
                              int direction)
        {
            Py_ssize_t len = (Py_ssize_t) self.size();
            Py_ssize_t slen = (Py_ssize_t) substr.size();

            const char* sub = substr.c_str();
            const char* str = self.c_str();

            ADJUST_INDICES(start, end, len);

            if (direction < 0) {
                // startswith
                if (start+slen > len)
                    return 0;
            } else {
                // endswith
                if (end-start < slen || start > len)
                    return 0;
                if (end-slen > start)
                    start = end - slen;
            }
            if (end-start >= slen)
                return (!std::memcmp(str+start, sub, slen));

            return 0;
        }
    }

    bool endswith( const std::string & str, const std::string & suffix, int start, int end )
    {
        int result = _string_tailmatch(str, suffix,
                                       (Py_ssize_t) start, (Py_ssize_t) end, +1);
        //if (result == -1) // TODO: Error condition
        return static_cast<bool>(result);
    }

    bool startswith( const std::string & str, const std::string & prefix, int start, int end )
    {
        int result = _string_tailmatch(str, prefix,
                                       (Py_ssize_t) start, (Py_ssize_t) end, -1);
        //if (result == -1) // TODO: Error condition
        return static_cast<bool>(result);
    }

    bool isalnum( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;

        if ( len == 1 )
        {
            return ::isalnum( str[0] );
        }

        for ( i = 0; i < len; ++i )
        {
            if ( !::isalnum( str[i] ) ) return false;
        }
        return true;
    }

    bool isalpha( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isalpha( (int) str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isalpha( (int) str[i] ) ) return false;
        }
        return true;
    }

    bool isdigit( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isdigit( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( ! ::isdigit( str[i] ) ) return false;
        }
        return true;
    }

    bool islower( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::islower( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::islower( str[i] ) ) return false;
        }
        return true;
    }

    bool isspace( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isspace( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isspace( str[i] ) ) return false;
        }
        return true;
    }

    bool isupper( const std::string & str )
    {
        std::string::size_type len = str.size(), i;
        if ( len == 0 ) return false;
        if ( len == 1 ) return ::isupper( str[0] );

        for ( i = 0; i < len; ++i )
        {
           if ( !::isupper( str[i] ) ) return false;
        }
        return true;
    }

    std::string lower( const std::string & str )
    {
        std::string s( str );
        std::string::size_type len = s.size(), i;

        for ( i = 0; i < len; ++i )
        {
            if ( ::isupper( s[i] ) ) s[i] = (char) ::tolower( s[i] );
        }

        return s;
    }

    std::string upper( const std::string & str )
    {
        std::string s( str ) ;
        std::string::size_type len = s.size(), i;

        for ( i = 0; i < len; ++i )
        {
            if ( ::islower( s[i] ) ) s[i] = (char) ::toupper( s[i] );
        }

        return s;
    }

    std::string replace( const std::string & str, const std::string & oldstr, const std::string & newstr, int count )
    {
        int sofar = 0;
        int cursor = 0;
        std::string s( str );

        std::string::size_type oldlen = oldstr.size(), newlen = newstr.size();

        cursor = find( s, oldstr, cursor );

        while ( cursor != -1 && cursor <= (int)s.size() )
        {
            if ( count > -1 && sofar >= count )
            {
                break;
            }

            s.replace( cursor, oldlen, newstr );
            cursor += (int) newlen;

            if ( oldlen != 0)
            {
                cursor = find( s, oldstr, cursor );
            }
            else
            {
                ++cursor;
            }

            ++sofar;
        }

        return s;

    }

    void splitlines(  const std::string & str, std::vector< std::string > & result, bool keepends )
    {
        result.clear();
        std::string::size_type len = str.size(), i, j, eol;

         for (i = j = 0; i < len; )
         {
            while (i < len && str[i] != '\n' && str[i] != '\r') i++;

            eol = i;
            if (i < len)
            {
                if (str[i] == '\r' && i + 1 < len && str[i+1] == '\n')
                {
                    i += 2;
                }
                else
                {
                    i++;
                }
                if (keepends)
                eol = i;

            }

            result.push_back( str.substr( j, eol - j ) );
            j = i;

        }

        if (j < len)
        {
            result.push_back( str.substr( j, len - j ) );
        }

    }

    std::string mul( const std::string & str, int n )
    {
        // Early exits
        if (n <= 0) return empty_string;
        if (n == 1) return str;

        std::ostringstream os;
        for(int i=0; i<n; ++i)
        {
            os << str;
        }
        return os.str();
    }
} // namespace pystring
```


## 动态加载 dll

```cpp
//#include "pch.h"
#include <assert.h>
#include <Windows.h>
#include <string>

#ifndef __FAST_IMAGE_LIB__
#define __FAST_IMAGE_LIB__

#ifdef FAST_IMAGE_DLL_EXPORT
#define DLLEXPORT __declspec(dllexport)
#else
#define DLLEXPORT //__declspec(dllimport)
#endif

#ifdef __cplusplus
extern "C" {
#endif

namespace fastimage {

#define FAST_IMAGE_VERSION_NOTESHRINK 2
#define FAST_IMAGE_VERSION FAST_IMAGE_VERSION_NOTESHRINK

__interface IFastImageInterface {
    virtual int getFastImageVersion() = 0;
    virtual int getMagicAdvancedBitmap(FastImage fimage, FastImage & result, bool clearBackgroud = true) = 0;
    virtual void release() = 0;
    virtual int getMagicAdvancedBitmap2(FastImage fimage, FastImage & result, bool clearBackgroud = true) = 0;
};

DLLEXPORT IFastImageInterface* CreateFastImageObject();

typedef IFastImageInterface* (*CreateFastImageObjectFunc)();

} // namespace fastimage

class fastimagedll : public fastimage::IFastImageInterface {
    static std::wstring getCurrentPath() {
        wchar_t tPath[MAX_PATH];
        DWORD dwRet = GetModuleFileName(NULL, tPath, MAX_PATH);
        std::wstring strexe = tPath;
        int index = strexe.rfind('\\');
        return strexe.substr(0, index + 1);
    }

    static HINSTANCE getLibrary(const TCHAR* libPath) {
        std::wstring curdir = getCurrentPath();
        std::wstring current = curdir;
        current.append(libPath);

        WCHAR lpBuffer[MAX_PATH];
        GetCurrentDirectory(MAX_PATH, lpBuffer);
        SetCurrentDirectory(curdir.c_str());
        HINSTANCE hDLL = LoadLibrary(current.c_str());
        SetCurrentDirectory(lpBuffer);

        if (hDLL == nullptr) {
            int err = GetLastError();
            return nullptr;
        }
        return hDLL;
    }

  public:
    virtual int getFastImageVersion() {
        if (!m_interface) {
            return -1;
        }
        return m_interface->getFastImageVersion();
    }
    virtual int getMagicAdvancedBitmap(fastimage::FastImage fimage, fastimage::FastImage& result,
                                       bool clearBackgroud = true) {
        if (!m_interface) {
            return -1;
        }
        return m_interface->getMagicAdvancedBitmap(fimage, result, clearBackgroud);
    }
    virtual int getMagicAdvancedBitmap2(fastimage::FastImage fimage, fastimage::FastImage& result,
                                        bool clearBackgroud = true) {
        if (!m_interface) {
            return -1;
        }
        if (m_interface->getFastImageVersion() < FAST_IMAGE_VERSION_NOTESHRINK) {
            return -2;
        }
        return m_interface->getMagicAdvancedBitmap2(fimage, result, clearBackgroud);
    }

    virtual void release() override {
        delete this;
    }

    fastimagedll() {
        const wchar_t* libPath = L"fastimage.dll";
        m_hDLL = getLibrary(libPath);
        if (m_hDLL == nullptr) {
            int err = GetLastError();
            return;
        }

        fastimage::CreateFastImageObjectFunc fptr =
            (fastimage::CreateFastImageObjectFunc)GetProcAddress(m_hDLL, "CreateFastImageObject");
        if (fptr == nullptr) {
            int err = GetLastError();
            return;
        }
        m_interface = fptr();
    }
    virtual ~fastimagedll() {
        if (!m_interface) {
            return;
        }
        m_interface->release();
        m_interface = nullptr;
        // m_hDLL 不释放了。
    }

  private:
    fastimage::IFastImageInterface* m_interface = nullptr;
    HINSTANCE m_hDLL = nullptr;
}; // class fastimagedll

#ifdef __cplusplus
}
#endif
#endif
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-14-tiny-source-code.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://android.googlesource.com/platform/external/swiftshader/+/refs/heads/master/CMakeLists.txt]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/android.googlesource.com/b62cb28d.txt" %})
- [https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-4-c4189?view=msvc-170]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/learn.microsoft.com/0c120c99.html" %})
- [https://blog.csdn.net/nameofcsdn/article/details/125007289]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/blog.csdn.net/817e0ab4.html" %})
- [https://rgplantz.github.io/2021/11/04/Shift-to-divide-by-10.html]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/rgplantz.github.io/343af929.html" %})
- [https://blog.csdn.net/ce123_zhouwei/article/details/108562387]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/blog.csdn.net/c29f479a.html" %})
- [https://developer.arm.com/documentation/dui0530/m/Migrating-from-ARM-Compiler-v5-05-to-v5-06/Compiler-changes-between-ARM-Compiler-v5-05-and-v5-06/--ldrex-and---strex-intrinsics-deprecated]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/developer.arm.com/b6ef944f.html" %})
- [https://blog.csdn.net/u012294613/article/details/123183813]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/blog.csdn.net/48a4b95e.html" %})
- [https://developer.android.google.cn/studio/archive.html]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/developer.android.google.cn/94ce01e4.html" %})
- [https://www.cnblogs.com/flowerslip/p/5934718.html]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/www.cnblogs.com/ffc4e6db.html" %})
- [https://blog.csdn.net/u011700339/article/details/89302321]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/blog.csdn.net/7a1d031d.html" %})
- [https://www.tutorialspoint.com/c_standard_library/c_function_bsearch.htm]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/www.tutorialspoint.com/c5079b0f.htm" %})
- [https://www.tutorialspoint.com/c_standard_library/c_function_qsort.htm]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/www.tutorialspoint.com/0bec0743.htm" %})
- [https://codingtidbit.com/2020/02/09/c17-codecvt_utf8-is-deprecated/]({% include relrefx.html url="/backup/2021-09-14-tiny-source-code.md/codingtidbit.com/24af4f6e.html" %})
