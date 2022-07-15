---
layout: post
title: "编程与调试 C++ -- PE 文件可见字符串提取"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程", "C/C++"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax:
mermaid:
glslcanvas:
codeprint:
---

通常，一个 PE 文件中有 4 个区段：
1. .text：（代码段），可读、可执行
2. .data：（数据段），存放全局变量、全局常量等
3. .idata：（数据段），导入函数的代码段，存放外部函数地址。（当然还有 edata ，导出函数代码段，但不常用）
4. .rdata：（数据段），资源数据段，程序用到什么资源数据都在这里（包括自己打包的，还有开发工具打包的）


## 字符串编码和操作

* ASCII 美国信息交换标准代码
    * 7 bit 表示一个字符
    * 共 128 个字符
* ISO-8859-1 对于 ASCII 的扩展
    * 8 bit 表示一个字符，会使用整个 byte
    * 共 256 个字符
* GB2312 国标，汉字的编码集
    * 2 byte 表示一个字符
    * 共 6763 个汉字
* GBK 对于 GB2312 的扩展，能表示更多的字符
    * 2 byte 表示一个字符
    * 共 21003 个汉字
* GB18030 对于 GBK 的扩展，最完整的汉字编码集
    * 变长多字节编码，1 个、2 个或 4 个 byte 表示一个字符
    * 共 70000 余个汉字
* BIG5 由台湾制定，主要用于繁体汉字编码
    * 2 byte 表示一个字符
    * 共 13060 个汉字
* Unicode 由国际标准化组织制定，整合全世界的字符
    * 2 byte 表示一个字符
    * 表示全世界所有的字符
    * 如果只使用英文字符，较浪费空间
* UTF(Unicode Translation Format) 通用转换格式，是 Unicode 的实现，解决了 Unicode 空间浪费的问题
    * UTF-8, UTF-16, UTF-16LE(little endian), UTF-16BE(big endian), UTF-32
* UTF-8 变长多字节编码，1~4 字节表示一个字符
    * 1 byte 表示一个 US-ASCIl 字符
    * 2 byte 表示一个拉丁文字符（拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文等）
    * 3 byte 表示一个汉字（中日韩文字、东南亚文字、中东文字等）
    * 4 byte 表示其他极少使用的语言
* UTF-8-BOM(Byte Order Mark)
    * Unicode 规定使用 BOM 来标识字节顺序，UTF-8-BOM 的文件会以 EF BB BF 开头
    * UTF-16 和 UTF-32 需要决定是按 2 Byte 读还是按 4 byte 读，需要 BOM 来决定顺序
    * UTF-8 是按 1 byte 读的，没有字节序问题，是不需要 BOM 来标识字节序的
        * 建议：使用 UTF-8 时，最好使用不带 BOM 的 UTF-8

GBK 编码是 GB2312 编码的超集，向下完全兼容 GB2312。
GB18030 编码向下兼容 GBK 和 GB2312，
GBK、GB2312 等与 UTF8 之间都必须通过 Unicode 编码才能相互转换。
GBK、GB2312 以及 Unicode 都既是字符集，也是编码方式，而 UTF-8 只是编码方式，并不是字符集。

* "utf8"，1~4 字节表示一个字符
    * 每个位置开始，是否成功？
* "gbk"，1~2 byte 表示一个字符
    * 每个位置开始，是否成功？
* "utf-16-le"，2/4 byte 表示一个字符
    * 每个位置开始，是否成功？

计算给定二进制字符串的所有可能解码组合
<https://www.5axxw.com/questions/content/h0ffdn>
<https://blog.csdn.net/MC_007/article/details/82712359>

我正在编写一些分析 PE 文件中的字符串的代码（Python，但实际上并不重要）。
我正在寻找一个可以调用的命令行工具，它将返回 PE 文件中的完整字符串列表。
我知道 PEDUMP，但它似乎给出了不完整的字符串。
此外，此工具能够处理不同类型的字符串非常重要，例如 C 字符串（NULL 终止），Pascal 字符串（长度前缀）等。
我在这里找到了“字符串提取器”，但它需要花钱，我不确定它是否可以处理不同类型的字符串。

```
E:\kSource\blog>D:\Qt\Tools\mingw810_64\bin\strings.exe -help
Usage: D:\Qt\Tools\mingw810_64\bin\strings.exe [option(s)] [file(s)]
 Display printable strings in [file(s)] (stdin by default)
 The options are:
  -a - --all                Scan the entire file, not just the data section [default]
  -d --data                 Only scan the data sections in the file
  -f --print-file-name      Print the name of the file before each string
  -n --bytes=[number]       Locate & print any NUL-terminated sequence of at
  -<number>                   least [number] characters (default 4).
  -t --radix={o,d,x}        Print the location of the string in base 8, 10 or 16
  -w --include-all-whitespace Include all whitespace as valid string characters
  -o                        An alias for --radix=o
  -T --target=<BFDNAME>     Specify the binary file format
  -e --encoding={s,S,b,l,B,L} Select character size and endianness:
                            s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
  -s --output-separator=<string> String used to separate strings in output.
  @<file>                   Read options from <file>
  -h --help                 Display this information
  -v -V --version           Print the program's version number
D:\Qt\Tools\mingw810_64\bin\strings.exe: supported targets:
                pe-x86-64 pei-x86-64 pe-bigobj-x86-64 elf64-x86-64 elf64-l1om
                elf64-k1om pe-i386 pei-i386 elf32-i386 elf32-iamcu elf64-little
                elf64-big elf32-little elf32-big plugin srec symbolsrec verilog
                tekhex binary ihex
Report bugs to <http://www.sourceware.org/bugzilla/>

E:\kSource\blog>
```

----

手工撸了一个超级解码：
```python
#encoding=utf8
import os
import string

def readfile(path):
    if not os.path.exists(path):
        return b""
    fin = open(path, "rb")
    page = fin.read()
    fin.close()
    return page

def trystr(fdata, startp, encoding, xli, fcache, checkenc):
    eatstr = ""
    eatsize = 0 # 消耗了多少个字节。
    while True:
        char = None
        charlen = 0
        for ilen in xli:
            try:
                char = fdata[startp:startp+ilen].decode(encoding)
                if checkenc: char.encode(checkenc)

                assert len(char) == 1, char
                char = char[0] # 字符串变成字符

                # https://docs.python.org/zh-tw/3.8/library/string.html
                if ord(char) <= 0x7f:
                    assert char in string.printable, char
                charlen = ilen
                break
            except KeyboardInterrupt as ex:
                raise ex
            except:
                continue

        if char and charlen and ord(char):
            fcache[startp] = charlen
            eatstr = eatstr + char
            startp += charlen
            eatsize += charlen
        else:
            fcache[startp] = -1
            break

    return eatsize, eatstr

def hackstring(fpath, encoding, checkenc, xli, strset, printx=False):
    fdata = readfile(fpath)
    fsize = len(fdata)
    fcache = [0 for i in range(fsize + xli[-1])]
    retv = []
    for startp in range(fsize):
        if fcache[startp]: # 这里已经校验过了。
            continue
        eatsize, eatstr = trystr(fdata, startp, encoding, xli, fcache, checkenc)
        eatbin = eatstr.encode(encoding)
        # https://docs.microsoft.com/zh-cn/sysinternals/downloads/strings
        if len(eatstr) <= 1 or len(eatbin) <= 2: continue # 只有一个字符，忽略掉。
        if eatstr in strset: continue # 已经存在了。
        strset.add(eatstr)
        if printx:
            print(fsize, startp, eatsize, encoding, len(eatstr), '"{}"'.format(eatstr))
        retv.append((fsize, startp, eatsize, encoding, len(eatstr), eatstr))
    return retv

if __name__ == "__main__":
    fpath = r"E:\kpdf\keniupdf\6500\keasyipcn.dll"
    strset = set()
    hackstring(fpath, "gbk", None, [1, 2,], strset, True)
    hackstring(fpath, "utf-16-le", "gbk", [2, 4], strset, True)
    hackstring(fpath, "utf8", "gbk", [1, 2, 3, 4], strset, True)
```

----

[^_^]: <www.csdn.net/tags/MtTaMg0sNDE0MzQ1LWJsb2cO0O0O.html>

有过破解 native 程序经验的人都知道，在大量的汇编代码面前不可能是从头开始理解代码的，必须找到一两个点进行突破。
字符串往往就是这样的关键点，在代码中 hardcode 的字符串会可以原封不动的在生成的 binary 中查找到。
所以要增加破解的难度，对字符串进行混淆（或者叫加密，下面的文字可能混淆和加密混着用，在这里没有区别）是很重要的一步。
只要字符串在代码中出现，那么其必然会在 binary 中出现，所以要想在 binary 中查找不到字符串，必须在代码进行编译之前进行变形。所以从理论上来说，可以从下面几个角度进行入手：

1. 编译之前调用程序对字符串进行处理
2. 代码中直接写入混淆后的字符串
3. 编译过程中使用宏等其他手段自动混淆
4. 对生成的 binary 进行处理

下面的几个方案就是从这几个角度提炼出来的。


## 直接在代码中写入混淆后的字符串

利用工具生成加密后的字符串，在代码中写入加密后的字符串，在使用字符串时调用一个函数进行解密
```cpp
char* string = Decrypt("aGVsbG8="); // hello
printf("string is: %s", string);
```
这里字符串 "aGVsbG8=" 是经过 base64 之后的，Decrypt 之后还原成字符串 hello。
这里加密后的内容还是字符形式的字符串。字符形式的字符串也会在 binary 中出现，如果破解者发现有大量的这种比较奇怪的字符串，实际上也是破解者的一个突破口，他们可以从这里破解出我们的加密算法，从而将所有的字符串解密出来。

对付这个问题我们有几种方法：
1. 使用多种加密算法，针对不同的字符串使用不同的算法
2. 加密后的内容不用以 0 结尾的字符串表示，使用 binary 形式，以长度表示其结尾

这种方法的有点是比较简单，但是增加开发人员的工作比较多


## 字符串以数组形式初始化

比如以下写法：
```cpp
const char* testString = "a test string!";
printf("testString: %s\n", testString);

// a test string2!
char* testString2 = ((char[]){
        'a', ' ', 't', 'e', 's',
        't', ' ', 's', 't', 'r',
        'i', 'n', 'g', '2', '!', '\0'});
printf("testString2: %s\n", testString2);
```

如果使用 strings 查找字符串，可以发现 "a teststring!" 可以找到，而 'atest string2!' 则无法找到。
查看其汇编代码，会发现这两种写法的对于字符串处理生成的代码完全不一样。

第一种写法，我们比较熟悉，直接从 binary 的 .txt 区域获取字符串：
```
.text:000000000040057B                 mov     [rbp+var_28], 40070Ch // 40070Ch 是指向 binary 中的地址
.text:0000000000400583                 mov     rax, [rbp+var_28]
.text:0000000000400587                 mov     rsi, rax
.text:000000000040058A                 mov     edi, offset aTeststringS ;"testString: %s\n"
.text:000000000040058F                 mov     eax, 0
.text:0000000000400594                 call    _printf
```
第二种写法则完全不一样，这些字符串不会保存在 binary 的 .txt 区域，而是在一个字符一个字符的 copy 到栈上面，以下 gcc 在 ubuntu64 上面生成的汇编代码：
```
.text:0000000000400599                 mov     [rbp+var_20], 61h
.text:000000000040059D                 mov     [rbp+var_1F], 20h
.text:00000000004005A1                 mov     [rbp+var_1E], 74h
.text:00000000004005A5                 mov     [rbp+var_1D], 65h
.text:00000000004005A9                 mov     [rbp+var_1C], 73h
.text:00000000004005AD                 mov     [rbp+var_1B], 74h
.text:00000000004005B1                 mov     [rbp+var_1A], 20h
.text:00000000004005B5                 mov     [rbp+var_19], 73h
.text:00000000004005B9                 mov     [rbp+var_18], 74h
.text:00000000004005BD                 mov     [rbp+var_17], 72h
.text:00000000004005C1                 mov     [rbp+var_16], 69h
.text:00000000004005C5                 mov     [rbp+var_15], 6Eh
.text:00000000004005C9                 mov     [rbp+var_14], 67h
.text:00000000004005CD                 mov     [rbp+var_13], 32h
.text:00000000004005D1                 mov     [rbp+var_12], 21h
.text:00000000004005D5                 mov     [rbp+var_11], 0
.text:00000000004005D9                 lea     rax, [rbp+var_20]
.text:00000000004005DD                 mov     [rbp+var_30], rax
.text:00000000004005E1                 mov     rax, [rbp+var_30]
.text:00000000004005E5                 mov     rsi, rax
.text:00000000004005E8                 mov     edi, offset aTeststring2S ;"testString2: %s\n"
.text:00000000004005ED                 mov     eax, 0
.text:00000000004005F2                 call    _printf
```
这个写法在 vc 上面无法编译通过：
```
char* testString2 = ((char[]){'a', ' ', 't', 'e', 's', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', '2', '!', '\0'});
```
但是稍微变形一下就可以：
```
char testString2[] = {'t', 'h', 'i', 's', ' ', 'a', '', 't', 'e', 's', 't',' ', 's', 't', 'r', 'i', 'n', 'g', '\0'};
```

我看了一下生成的汇编代码，跟前一种写法是一样的。这个方案比较 tricky，利用的是编译器生成代码的特性。其缺点是写字符串时比较麻烦，每个字符都需要用单引号给引起来。
如果字符串比较多，是一个比较大的负担。但是这种方案的好处也是十分明显的，字符串都是一个一个嵌入在代码里面，要想找出来难度非常大，另外 ，字符串只出现在栈上面，栈退出之后，字符串就在内存中就找不到了，即使搜索内存的方式也找不到，所以安全性非常高。
注意：这种写法只能用在函数内部，如果 testString2 是一个全局变量，字符串则会保存在 binary 中。


## 编译前对字符串进行处理

在网上发现好几个开源项目是做这事，其基本思路是，先自定义一个自定义格式的文件，在文件中写入字符串，然后在编译之前，将文件转换成 c/c++ 格式，被代码引用。c/c++ 文件中的字符串则经过了我们的加密。比如这个项目：

Literalstring encryption as part of the build process
<http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro>

其自定义的文件叫 crx 文件，其内容如下：
```
// my .CRX file
//
// here is my password definition:
// CXRP ="SexyBeast"
//
// here are somestrings:
// my first string
constchar* pString1 = _CXR("AbcdEfg1234  blah\tblah");
// string #2
constchar* pString2 = _CXR("This is a long one, not that itshould matter...");
```
CXRP= "SexyBeast" 这里定义的是加密用的秘钥。
\_CXR 则定义字符串，我们会将里面的字符串加密后生成 cpp 文件，如下：
```
///
#ifdef _USING_CXR
// my first string
const char* pString1 = "ab63103ff470cb642b7c319cb56e2dbd591b63a93cf88a";
#else
const char* pString1 = _CXR("AbcdEfg1234  blah\tblah"); // my first string
#endif
///
#ifdef _USING_CXR
// string #2
const char* pString2 = "baff195a3b712e15ee7af636065910969bb24997c49c6d0cc6a40d3ec1...";
#else
// string #2
const char* pString2 = _CXR("This is a long one, not that it should matter...");
#endif
```
这里可以使用 \_USING_CXR 宏来对字符串加密功能进行开关控制。
这里还有一个项目：strenc
<https://code.google.com/p/strenc/>

其自定义文件叫 .strenc，格式如下：
```
INTRO_STRING
Thisis a test of strenc()
SECOND_STRING
How's it working?
THIRD_STRING
testing"quotes" bro.
```
它的格式是字符串名字和字符串内容交叉进行，被处理后生成的是 .h 文件，用宏来表示，如下：
```
#ifndef STRINGS_KEY
    #define STRINGS_KEY "1iCEVcHQRhf+rkybltGvodTAg6m9XMDp5WuFqxO2/jzZISUenNKL80BJP4w3as7Y"
    #pragma comment(lib, "strenc")
    voidStrencDecode(char* buffer, char* Base64CharacterMap);
    const char*GetDecryptedString(const char* encryptedString) {
        char* string = newchar[1024];
        strcpy(string, encryptedString);
        StrencDecode(string, STRINGS_KEY);
        returnstring;
    }
    #define INTRO_STRING GetDecryptedString("dHWjXKijXKiWRQtxXJl59Bg5XJtK6T4FfCq1")
    #define SECOND_STRING GetDecryptedString("GHsJhJr5mAl5MBsKmBxU6La1")
    #define THIRD_STRING GetDecryptedString("MHdLMHxU6K1uXAdeMHdLRuiuXOaU11==")
#endif
```

这种方法的优点是将所有的字符串统一进行管理，将所有需要混淆的字符串都加入到这个文件中。我们还可以增强其加解密功能，不同的字符串使用不同的加解密算法或者不同的秘钥。缺点是对于已经存在的代码，我们需要将需要混淆的字符串一个一个提取出来，放在自定义格式的文件中，如果代码量比较大，搜索出所有的字符串的工作量比较大。针对这个缺点，我们引入了下面一种方案。


## 扫描所有代码，将所有字符串进行混淆处理

上面那个方案不错，但是对于已经存在的大型项目要将需要混淆的字符串找出来的工作量比较大，所有有了这个方案

这里有一个实现：

StringsObfuscation System
<http://www.codeproject.com/Articles/502283/Strings-Obfuscation-System>

它的实现是基于 vc 的，搜索 solution 中的所有 .h/.c/.cpp/.hpp 文件，将有字符串的地方使用 \__ODA__() 进行替换， \__ODA__ 的参数则为加密后的字符串， \__ODA__ 函数负责解密。
它还支持 uncode 字符串，对于 unicode 字符串，使用函数 \__ODC__ 替换字符串。它的优点就是可以很简单的就将大型项目的所有字符串都混淆。缺点是它需要在编译时，每次都扫描一遍代码，将需要替换的字符串替换掉。


## 编译期对字符串进行变换

```
#define PRIME 0x1000193
#define OFFSET 0x811C9DC5

struct Hash {
    template <unsigned int N, unsigned int I>
    struct Helper
    {
        inline static unsigned int Calculate(const char(&str)[N])
        {
        return (Helper<N, I - 1>::Calculate(str) ^ str[I- 1]) * PRIME;
        }
    };

    template <unsigned int N>
    struct Helper<N, 1>
    {
        inline static unsigned int Calculate(const char(&str)[N])
        {
        return (OFFSET ^ str[0]) * PRIME;
        }
    };

    template <unsigned int N>
    inline static unsigned int Calculate(const char(&str)[N])
    {
    return Helper<N, N>::Calculate(str);
    }
};

Hash::Calculate("hello")
```

这里的 Hash::Calculate 传入的字符串会被在编译期间计算 hash 值，字符串在开启优化之后（O3），在代码中不存在。
这里的 hash 可以作为 index 来获取到解密后的 string，定义一个这样的宏：
```
#define DECRYPT(text) GetDecryptText(Hash::Calculate(text))
```
GetDecryptText 后面再解释。在使用时，这样使用就可以：
```
printf("%s\n", DECRYPT("helloText"));
```
另外再准备一个工具，扫描所有带有 DECRYPT 宏的字符串，生成函数 GetDecryptText：
```
......
char str_0x12345678[12] = { 0 };
bool tag_0x12345678 = Decrypt(str_0x12345678,"!@##$%^&*("); // Cipher text of "Hello World"
......
const char* GetDecryptText(int hash)
{
    switch(hash)
    {
        ......
        case0x12345678: return str_0x12345678;
        ......
    }
}
```

生成的代码可以放在一个单独的 cpp 文件中。这个方案优点实际上跟方案三差不多，都会生成一个独立的 cpp 文件。优点是对现有的代码结构改变较小。缺点是：
1. 需要开启优化之后，字符串才会不出现在 binary 中，
2. 需要编译前对源代码进行全部扫描
3. 依赖 template，纯 c 环境无法使用


## 修改编译器，将所有的字符串都加密存储

修改编译器，将所有的字符串都加密存储，在引用字符串的地方调用解密函数。这个方案在网上没有看到现成的代码，但是考虑到 gcc 是开源的，应该是可以做的。


## 加壳

加壳是很成熟的方法了，可以防止直接从 binary 中搜索字符串。他的优点在于不用对代码做任何改动，并且不会引入任何运行时的额外性能开销。加壳的缺点在于：加壳过的文件比较容易认为是病毒。如果只是为了字符串加密而引入加壳则有点小题大做，脱壳之后或者程序运行之后字符串全部可见。


## 参考文献

混淆字符串
<http://blog.csdn.net/iiprogram/article/details/3732306>

如何防止客户端被破解
<http://tanqisen.github.io/blog/2014/06/06/how-to-prevent-app-crack/>

Literalstring encryption as part of the build process
<http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro>

StringsObfuscation System
<http://www.codeproject.com/Articles/502283/Strings-Obfuscation-System>

strenc
<https://code.google.com/p/strenc/>

PE 文件中隐藏明文字符串
<http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2>
pe 文件中隐藏明文字符串（续）
<http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%88%E7%BB%AD%EF%BC%89>

In-Depth:Quasi Compile-Time String Hashing
<http://www.gamasutra.com/view/news/127915/InDepth_Quasi_CompileTime_String_Hashing.php>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-07-01-pe-strings.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.5axxw.com/questions/content/h0ffdn]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.5axxw.com/464cd928.html" %})
- [https://blog.csdn.net/MC_007/article/details/82712359]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/blog.csdn.net/db3d813d.html" %})
- [http://www.sourceware.org/bugzilla/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.sourceware.org/60356a6f.html" %})
- [https://docs.python.org/zh-tw/3.8/library/string.html]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/docs.python.org/6888d893.html" %})
- [http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.codeproject.com/7ea30383.html" %})
- [https://code.google.com/p/strenc/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/code.google.com/0512edd5.html" %})
- [http://www.codeproject.com/Articles/502283/Strings-Obfuscation-System]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.codeproject.com/1fc2ca9c.html" %})
- [http://blog.csdn.net/iiprogram/article/details/3732306]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/blog.csdn.net/a53c18cf.html" %})
- [http://tanqisen.github.io/blog/2014/06/06/how-to-prevent-app-crack/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/tanqisen.github.io/c26c44a2.html" %})
- [http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/a.vifix.us/d237afa7.html" %})
- [http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%88%E7%BB%AD%EF%BC%89]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/a.vifix.us/8be44b0a.html" %})
- [http://www.gamasutra.com/view/news/127915/InDepth_Quasi_CompileTime_String_Hashing.php]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.gamasutra.com/1c078939.php" %})
