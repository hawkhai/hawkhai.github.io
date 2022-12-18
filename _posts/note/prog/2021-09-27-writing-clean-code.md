---
layout: post
title: "编程与调试 -- 怎么写好代码？断言 vs 异常（团队内部交流）"
author: yqh
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

批判性接受，很多观点个人理解和思考，不一定正确，大家一起探讨交流。

* **断言：断言断的是我们的程序没有 bug，程序写的没问题。**
    * 写了一个函数，调用者理解错了。属于 非法情况，代码写对了就没这个问题。
    * 处理不处理都没啥用，不处理就直接崩溃，处理了就崩溃到其它地方去了。
* **异常：代码写的没问题，特殊情况确实发生了，需要得到合理的处理。**
    * 比如让用输入数字，结果输入了字母。属于必然存在的错误情况。
    * 这个是要得到合理处理的，因为这种特殊情况确实存在。


## 什么是断言

C/C++ 里面断言是 宏定义，只在 Debug 版本生效，Release 版本是一个空宏。
如果程序在 assert 处终止了，并不是说含有该 assert 的函数有错误，而是调用者出了差错，assert 可以帮助我们找到发生错误的原因。
不能使用改变环境的语句。不应该存在副作用，童畜无害。

```cpp
assert(i++ < 100); // i++ 这个逻辑就丢了。Release 和 Debug 版本就存在不一致性。
```

断言有点类似单元测试。CRT 断言：
* CRTDBG.H 头文件定义 _ASSERT 和 _ASSERTE 宏用于断言检查。
* _ASSERT：如果指定表达式的计算结果为 FALSE，则为 _ASSERT 的文件名和行号。
* _ASSERTE：与 _ASSERT 相同，再加上进行断言的表达式的字符串表示形式。


## 字符串克隆

```cpp
char* strdup(char* str) {
    int length = strlen(str);
    char* strnew = memcpy(malloc(length), str, length);
    return strnew;
}
```

上面这段代码存在问题，当 str 输入为 NULL，会发生什么？当 malloc 失败会发生什么？
改进版本 1：

```cpp
// 申请创建 str 的拷贝。当 str == NULL，程序无定义。
char* strdup(char* str) {
    // 因为它被用来检查在该程序正常工作时绝不应该发生的非法情况。
    assert(str != NULL); // 正确的 断言 使用。
    char* strnew = (char*) malloc(strlen(str) + 1);
    // 最终产品中肯定会出现并且必须对其进行处理的错误情况。
    assert(strnew != NULL); // 错误的断言使用，因为内存申请真的可能不成功。
    strcpy(strnew, str);
    return strnew;
}
```

`assert(strnew != NULL);` 错误的断言使用，因为内存申请真的可能不成功。
改进版本 2：

```cpp
// 申请创建 str 的拷贝。当 str == NULL，程序无定义。
char* strdup(char* str) {
    assert(str != NULL);
    char* strnew = (char*) malloc(strlen(str) + 1);
    if (strnew != NULL) {
        strcpy(strnew, str);
        assert(strcmp(strnew, str) == 0); // 断言一样
    }
    return strnew;
}
```


## 进一步探讨

程序错误一般会在运行一段时间后才因为异常退出。这时候触发错误导致进程退出的代码位置往往不是“案发的第一现场”，给调试工作带来了更大的难度。
* 如果有错误，就让错误早点发生。
* 如果错误概率发生，就让其稳定必现。

* 搞 Debug 版本，更多的运行时检查。
* 搞 x64 版本，开启无内存限制的页堆。
* 升级编译器，用上最新的工具。

**Win32 堆和 CRT 堆的常用字节模式和它们的含义** @156@liebao

字节模式 | 堆管理器 | 用途 | 长度
---- | ---- | ---- | ----
0xFEEEFEEE  | Win32 堆 | 填充空闲块的数据区        | 块数据区大小
0xBAADF00D  | Win32 堆 | 填充新分配块的数据区      | 块数据区大小
0xAB        | Win32 堆 | 填充在堆块的用户数据之后，用于检测堆溢出 | 不确定
0xFD        | CRT 调试堆 | 填充用户数据区前后的隔离区（no-man’s land） | 各 4 个字节
0xDD        | CRT 调试堆 | 填充释放的堆块（dead land） | 整个堆块大小
0xCD        | CRT 调试堆 | 填充新分配的堆块（clean land） | 用户数据区大小

各种运行时检查：

{% include image.html url="/assets/images/210927-writing-clean-code/20210502140538.png" relocate="DebugGZ" caption="Debug 版本，使用了未初始化指针，报错，Release 版本不报错。" %}
{% include image.html url="/assets/images/210927-writing-clean-code/20210502140610.png" relocate="DebugGZ" caption="Debug 版本，堆越界写入，回收的时候直接报错。" %}
{% include image.html url="/assets/images/210927-writing-clean-code/20210502140622.png" relocate="DebugGZ" caption="Release 版本，堆越界写入，最后报错。" %}

{% include image.html url="/assets/images/210927-writing-clean-code/20210511121604.png" relocate="DebugGZ" caption="Debug 版本，vector 越界断言。" %}
{% include image.html url="/assets/images/210927-writing-clean-code/20210511121624.png" relocate="DebugGZ" caption="Debug 版本，vector 越界断言，直接定位到代码行。" %}


## 一些关键原则

**多用断言，用对断言。**
一种程序，突然崩溃了，闷声不啃声，也不说啥原因，耽搁调试半天。
另外一种程序，自己发现错误了，会说话，能主动报告错误。无数个断言就形成了一个哨兵网络。

assert 语句，你可以把错误原因放到 assert 的参数中，这样不仅能保护你的程序不往下走，而且还能把错误原因返回给调用方。

1. 要使用断言对函数参数进行确认，利用断言来检查不可能发生的情况。
    * 要从程序中删去无定义的特性，或者在程序中使用断言来检查出无定义特性的非法使用。
    * 断言不是用来检查错误的。用来检查在该程序正常工作时绝不应该发生的非法情况，不是所测试的是错误情况，是在其最终产品中肯定会出现并且必须对其进行处理的错误情况。
    * 消除所做的隐式假定，或者利用断言检查其正确性，这些措施使得该程序极少可能被不正确地使用。
2. 在编写函数时，要进行反复的考查，并且自问：“我打算做哪些假定？”一旦确定了的假定，就要使用断言对假定进行检查。
3. 一般教科书都鼓励程序员们进行防错性的程序设计，但要记住这种编程风格会隐瞒错误。当进行防错性编程时，如果“不可能发生”的事情的确发生了，则要使用断言进行报警。


### 核反应堆

{% include image.html url="/assets/images/210927-writing-clean-code/cx.jpg" %}

假如你受雇为核反应堆编写软件，就必须对堆芯过热这一情况进行处理。
* 某些程序员解决这个问题的方法可以是自动地向堆芯灌水、插入冷却棒或者是能使反应堆冷却下来的一些其他什么方法。而且，只要程序已经控制了势态就不必向有关人员发出警报。
* 另一些程序员可能会选择另一种方法，即只要堆芯过热就向反应堆工作人员发出警报。虽然相应的处理仍由计算机自动进行，不同的是操作员总是知道这件事。
* **在进行防错性程序设计时，不要隐瞒错误。** 堆芯不会无缘无故地出现过热现象，一定是发生了某种不同寻常的事情，才会引起这一故障。因此在计算机进行相应处理的同时，最好使操作人员搞清楚发生了什么事情以避免事故的再次发生。


### 字符串拷贝

```cpp
// const 保证参数不会搞反，想用错都难。
char* strcpy(char* dest, const char* src) {
    // 断言，Debug 版本生效。
    assert((dest != NULL) && (src != NULL));
    // 入参检查，特殊情况处理。
    if (src == NULL || dest == NULL) { // 还能再抢救一下？
        // Release 极端断言情况发生了，蓝屏。
        // 特殊处理一下，让问题转移？
        return dest; // 建议做法
    }
    char* address = dest; // 功能逻辑
    while ((*dest++ = *src++) != '\0')
        NULL;
    return address;
}
```

```cpp
int resetBufferSize(int nNewSize) {
    // 在函数开始处检验传入参数的合法性
    // 异常输入，程序的逻辑未定义。
    // 说明这个函数的使用者用错函数了。
    assert(nNewSize >= 0);
    assert(nNewSize <= MAX_BUFFER_SIZE);
    ...
}

void* memcpy(void* dst, const void* src, size_t count) {
    // 安全检查
    assert(dst != NULL && src != NULL);

    unsigned char* pdst = (unsigned char*)dst;
    const unsigned char* psrc = (const unsigned char*)src;

    bool overlap = (psrc <= pdst && pdst < psrc + count) ||
                   (pdst <= psrc && psrc < pdst + count);

    // 防止内存重复。
    assert(!overlap); // Debug 版本。
    if (overlap) { // 覆盖处理，早期暴露，有一个 DirectX API 就是这样做的。
        // 让 Release 不稳定的 bug，稳定出现。
        // 将错误早点暴露出来
        while (count--) {
            *pdst++ = 0;
        }
        return dst;
    }

    while (count--) {
        *pdst++ = *psrc++;
    }
    return dst;
}
```

函数的参数，特别是指针参数必须利用断言来进行确认。
利用断言检查程序中的各种假设的正确性，任何函数都存在一些定义域，存在各种假定。
在程序设计中不要轻易认为某种情况不可能发生，对你认为不可能发生的情况必须用断言来证实。


## 高级断言

利用不同的算法对同一个东西进行检验，即使会降低程序运行速度。
非常复杂的情况，可以采用代码块来验证。

```cpp
#ifdef _DEBUG // IDE 内置的一个宏，不同 IDE 存在差异。
... // 代码块，各种检查。
#endif
```

{% include image.html url="/assets/images/210927-writing-clean-code/20211007223157.png" %}

在写 视频信息解析 代码的时候，采用 ffmpeg.exe 命令行调用。实在搞不清楚，就写了两个版本，一个正则解析命令行输出，一个解析 JSON 数据，
两份都可能存在错误，两份实现相互校验，发布版本采用 JSON 版本。

```cpp
bool VInfoEngine::runProbe(const QString& filename, int timeout) {
    bool temp = m_probe->runx(filename, timeout); // JSON 解析
#if _DEBUG
    m_probe_regex->runx(filename, timeout); // 命令行正则解析
    m_probe_regex->assertEqual(m_probe);
#endif
    return temp;
}
```

```text
Stream #0:0: Audio: mp3, 44100 Hz, stereo, fltp, 128 kb/s
Stream #0:1: Video: flv1, yuv420p, 1120x800, 23.98 fps, 23.98 tbr, 23.97 tbn
```

```json
{
    "index": 0,
    "codec_name": "h264",
    "codec_long_name": "H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10",
    "profile": "High",
    "codec_type": "video",
    "codec_tag_string": "avc1",
    "codec_tag": "0x31637661",
    "width": 640,
    "height": 480,
    "coded_width": 640,
    "coded_height": 480,
    "closed_captions": 0,
    "has_b_frames": 2,
    "pix_fmt": "yuvj420p",
    "level": 30,
    "color_range": "pc",
    "color_space": "bt470bg",
    "chroma_location": "left",
    "refs": 1,
    "is_avc": "true",
    "nal_length_size": "4",
    "r_frame_rate": "30/1",
    "avg_frame_rate": "1387907242/46242737",
    "time_base": "1/90000",
    "start_pts": 0,
    "start_time": "0.000000",
    "duration_ts": 660344400,
    "duration": "7337.160000",
    "bit_rate": "299079",
    "bits_per_raw_sample": "8",
    "nb_frames": "220214"
}
```

在后继的各种输入断言下，其实两份实现多多少少都存在 bug，不过最终都得以修复。
通过正则版本，才搞清楚 Json 里面各种数字的单位；通过 Json 版本才知道 视频存在 `SAR 4:3 DAR 16:9` 和 旋转的问题。
断言旋转角度 只有 0°、90°、-90°、-180°。

```cpp
// bitrate 以为是 1024，其实是 1000，不知道正确与否，反正正则版本是这样算的。
bitrate = (qjson.value("bit_rate").toDouble() / 1000);
```

图像处理 API：
```cpp
// 返回 0 表示成功。
// 外面需要把结果内存申请好，要和输入图片一样即可，并合理释放。
int getGrayBitmap(FastImage fimage, FastImage& result, bool clearBackgroud) {
    assert(fimage.format == FastImageType::FastImageRGBA8888);
    assert(fimage.width > 0 && fimage.height > 0 && fimage.pixels != nullptr);
    assert(result.format == FastImageType::FastImageRGBA8888);
    assert(fimage.width == result.width && fimage.height == result.height && result.pixels != nullptr);

    cv::Mat mrgba(fimage.height, fimage.width, CV_8UC4, fimage.pixels);
    cv::Mat dst = mrgba.clone();

    cv::cvtColor(mrgba, dst, CV_RGB2GRAY);
    return matToBitmap(dst, false, result);
}
```

Android 甚至断言 网络访问在主线程崩溃，界面修改不在主线程 也崩溃。☭


## Chrome 实践


### BASE 库对 ui 线程上文件操作的限制

base::ReadFileToString
此行代码在 UI 线程中会触发 \_\_debugbreak();

如果是加载界面库或必须的配置可以通过声明
base::ThreadRestrictions::ScopedAllowIO allowio;
禁止 \_\_debugbreak();


### 代码里合理使用 assert

UI 线程开始
```cpp
TlsSetValue(key, GetCurrentThreadID());

bool Utils::IsVip() {
    ASSERT(TlsGetValue(key) != GetCurrentThreadID());
}
```


## 一个标准 C 悲剧函数

`void* realloc( void* pv, size_t size );`

* 如果该内存块的新长度小于老长度，realloc 释放该块尾部不再想要的内存空间，返回的 pv 不变。
* 如果该内存块的新长度大于老长度，扩大后的内存块有可能被分配到新的地址处，该块的原有内容被拷贝到新的位置。
    返回的指针指向扩大后的内存块，并且该块扩大部分的内容未经初始化。
* 如果满足不了扩大内存块的请求，realloc 返回 NULL，当缩小内存块时，realloc 总会成功。
* 如果 pv 为 NULL，那么 realloc 的作用相当于调用 malloc(size)，并返回指向新分配内存块的指针，或者在该请求无法满足时返回 NULL。
* 如果 pv 不是 NULL，但新的块长为零，那么 realloc 的作用相当于调用 free(pv) 并且总是返回 NULL。
* 如果 pv 为 NULL 且当前的内存块长为零，结果无定义。

还有一个悲剧函数。
`int ch = getchar();`

* 接口设计的，想用错都很难。一个深刻的例子是油门和刹车都是右脚踩。
    * 如果设计的左脚刹车右脚油门，当人在慌张的时候，会两只脚踩下去，直接爆缸。
    * 当油门和刹车都是右脚踩，这两种操作就天然互斥了，同时被踩下的可能就没有了。
    * 要使用户不容易忽视错误情况，不要在正常地返回值中隐藏错误代码。
* 设计一个油门刹车，踩一半是刹车，踩到底是油门。
    * 想不搞错，估计都难了。

还有一个神奇函数，有点像状态机。

```cpp
#include <string.h>
#include <stdio.h>

int main() {
    char str[80] = "This is - test # website";
    const char s[] = "-#";
    char* token;

    /* 获取第一个子字符串 */
    token = strtok(str, s);

    /* 继续获取其他的子字符串 */
    while (token != NULL) {
        printf("\"%s\"\n", token);
        token = strtok(NULL, s);
    }
    // 注意分割处理后原字符串 str 会变，变成第一个子字符串：混蛋。
    printf("\n\"%s\"\n", str);
    return(0);
}
```

```text
"This is "
" test "
" website"

"This is "
```

真不敢相信，这些都是 C 语言大师设计的接口标准函数。

* 不要写寄生函数，即依赖于其他函数的实现。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-09-27-writing-clean-code.md.js" %}'></script></p>
