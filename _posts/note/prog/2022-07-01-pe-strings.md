---
layout: post
title: "编程与调试 C++ -- PE 文件可见字符串提取"
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

**给定一个 PE 二进制文件，导出其中可能的所有字符串。**

网上找了一大堆，实在没找到满意的，最后自己写了一个，输入一个 50 MB 的 PE 文件，第一个版本需要 30 分钟出答案，优化到最后一个版本，只须要 10 秒。

通过脚本生成 C 代码，把判定树做到 PE 文件里面，做成 函数跳转，避免字典查询。


## 现有方案

* 微软的 `strings.exe` ，貌似只支持搜索不支持导出。
    * 在二进制 PE 文件中搜索 ANSI 和 UNICODE 字符串。
    * <https://docs.microsoft.com/zh-cn/sysinternals/downloads/strings>

  ```
  C:\kSource\blog>D:\Strings\strings.exe

  Strings v2.54 - Search for ANSI and Unicode strings in binary images.
  Copyright (C) 1999-2021 Mark Russinovich
  Sysinternals - www.sysinternals.com

  usage: D:\Strings\strings.exe [-a] [-f offset] [-b bytes]
                                [-n length] [-o] [-s] [-u] <file or directory>
  -a     Ascii-only search (Unicode and Ascii is default)
  -b     Bytes of file to scan
  -f     File offset at which to start scanning.
  -o     Print offset in file string was located
  -n     Minimum string length (default is 3)
  -s     Recurse subdirectories
  -u     Unicode-only search (Unicode and Ascii is default)
  -nobanner
         Do not display the startup banner and copyright message.
  ```
* mingw 的 `strings.exe` ，说是可以导出 PE 文件的字符串，实际上对中文支持不好。
  ```
  C:\kSource\blog>C:\Qt\Tools\mingw810_32\bin\strings.exe -help
  Usage: C:\Qt\Tools\mingw810_32\bin\strings.exe [option(s)] [file(s)]
   Display printable strings in [file(s)] (stdin by default)
   The options are:
    -a - --all    Scan the entire file, not just the data section [default]
    -d --data     Only scan the data sections in the file
    -f --print-file-name      Print the name of the file before each string
    -n --bytes=[number]       Locate & print any NUL-terminated sequence of at
    -<number>       least [number] characters (default 4).
    -t --radix={o,d,x}  Print the location of the string in base 8, 10 or 16
    -w --include-all-whitespace Include all whitespace as valid string characters
    -o      An alias for --radix=o
    -T --target=<BFDNAME>     Specify the binary file format
    -e --encoding={s,S,b,l,B,L} Select character size and endianness:
            s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
    -s --output-separator=<string> String used to separate strings in output.
    @<file>       Read options from <file>
    -h --help     Display this information
    -v -V --version     Print the program's version number
  C:\Qt\Tools\mingw810_32\bin\strings.exe: supported targets:
                pe-i386 pei-i386 elf32-i386 elf32-iamcu elf32-little elf32-big
                plugin srec symbolsrec verilog tekhex binary ihex
  Report bugs to <http://www.sourceware.org/bugzilla/>
  ```

以上都不怎能理想，我需要的是 gbk、utf8、utf16le 三种编码。


## 字符串编码

我正在编写一些分析 PE 文件中的字符串的代码（Python，但实际上并不重要）。
我正在寻找一个可以调用的命令行工具，它将返回 PE 文件中的完整字符串列表。
我知道 PEDUMP，但它似乎给出了不完整的字符串。
此外，此工具能够处理不同类型的字符串非常重要，例如 C 字符串（NULL 终止），Pascal 字符串（长度前缀）等。

* ASCII 美国信息交换标准代码
    * 7 bit 表示一个字符
    * 共 128 个字符
* ISO-8859-1 对于 ASCII 的扩展
    * 8 bit 表示一个字符，会使用整个 byte
    * 共 256 个字符
* GB2312 国标，汉字的编码集
    * 1/2 byte 表示一个字符
    * 共 6763 个汉字
* GBK 对于 GB2312 的扩展，能表示更多的字符
    * 1/2 byte 表示一个字符
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
* UTF (Unicode Translation Format) 通用转换格式
    * 是 Unicode 的实现，解决了 Unicode 空间浪费的问题
    * UTF-8, UTF-16, UTF-16LE(little endian), UTF-16BE(big endian), UTF-32
* UTF-8 变长多字节编码，1~4 字节表示一个字符
    * 1 byte 表示一个 US-ASCIl 字符
    * 2 byte 表示一个拉丁文字符（拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文等）
    * 3 byte 表示一个汉字（中日韩文字、东南亚文字、中东文字等）
    * 4 byte 表示其他极少使用的语言
* UTF-8-BOM (Byte Order Mark)
    * Unicode 规定使用 BOM 来标识字节顺序，UTF-8-BOM 的文件会以 EF BB BF 开头
    * UTF-16 和 UTF-32 需要决定是按 2 Byte 读还是按 4 byte 读，需要 BOM 来决定顺序
    * UTF-8 是按 1 byte 读的，没有字节序问题，是不需要 BOM 来标识字节序的
        * 建议：使用 UTF-8 时，最好使用不带 BOM 的 UTF-8

* GBK 编码是 GB2312 编码的超集，向下完全兼容 GB2312。
* GB18030 编码向下兼容 GBK 和 GB2312。
* GBK、GB2312 等与 UTF8 之间都必须通过 Unicode 编码才能相互转换。
* GBK、GB2312 以及 Unicode 都既是字符集，也是编码方式，而 UTF-8 只是编码方式，并不是字符集。

* "utf8"，1~4 字节表示一个字符
* "gbk"，1~2 byte 表示一个字符
* "utf-16-le"，2/4 byte 表示一个字符

抽象出问题：给定一个二进制串，暴力枚举里面所有可能的各种编码的字符串。
计算给定二进制字符串的所有可能解码组合。动态规划 增强的 brute-force 方法。

[^_^]: (https://www.5axxw.com/questions/content/h0ffdn)
[^_^]: (blog.csdn.net/MC_007/article/details/82712359)


## 第一个版本

针对每一种编码可能，尝试每一种可能的编码长度，尝试解码。
只尝试解码 `gbk` 字符集里面的字符串。

* `def trystr(fdata, startp, encoding, xli, fcache, checkenc):`
    * fdata -- 文件二进制
    * startp -- 开始解码的位置
    * encoding -- 编码方式
    * xli -- 这种编码方式，单个字符可能的长度
    * fcache -- 缓存，避免重复解码。
    * checkenc -- 检查这个字符是不是我们需要的。

手工撸了一个暴力解码：
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
    fpath = r"E:\kapp\toyapp\test.dll"
    strset = set()
    hackstring(fpath, "gbk", None, [1, 2,], strset, True)
    hackstring(fpath, "utf-16-le", "gbk", [2, 4], strset, True)
    hackstring(fpath, "utf8", "gbk", [1, 2, 3, 4], strset, True)
```

输入一个 50 MB 的 PE 文件，需要 30 分钟出答案。


## 优化……


### 编码树

首先写一个程序生成所有 gbk 编码 字符 的解码树。
* gbk.table.json
  ```json
  {
    "09": "\t",
    "0a": "\n",
    "81": {
      "40": "丂",
      "41": "丄",
      "42": "丅",
      "43": "丆"
    },
    "82": {
      "40": "侤",
      "41": "侫",
      "42": "侭",
      "43": "侰"
    }
  }
  ```
* utf8.table.json
  ```json
  {
    "09": "\t",
    "0a": "\n",
    "0b": "\u000b",
    "0c": "\f",
    "ce": {
      "91": "Α",
      "92": "Β",
      "93": "Γ",
      "94": "Δ",
      "95": "Ε"
    },
    "e3": {
      "80": {
        "80": "　",
        "81": "、",
        "82": "。",
        "83": "〃",
        "85": "々",
        "86": "〆"
      },
      "81": {
        "81": "ぁ",
        "82": "あ",
        "83": "ぃ",
        "84": "い",
        "85": "ぅ",
        "86": "う"
      }
    }
  }
  ```
* utf16le.table.json
  ```json
  {
    "00": {
      "25": "─",
      "30": "　",
      "4e": "一",
      "9f": "鼀"
    },
    "01": {
      "01": "ā",
      "04": "Ё",
      "25": "━",
      "30": "、",
      "4e": "丁",
      "4f": "企"
    },
    "02": {
      "25": "│",
      "30": "。",
      "4e": "丂",
      "4f": "伂"
    }
  }
  ```

完整的版本：
<a href="{% include relref.html url="/source/mycode/gbk.table.json" %}" target="_blank">gbk.table.json</a>
<a href="{% include relref.html url="/source/mycode/utf8.table.json" %}" target="_blank">utf8.table.json</a>
<a href="{% include relref.html url="/source/mycode/utf16le.table.json" %}" target="_blank">utf16le.table.json</a>

一共 **21891** 个字符。


### 内存结构

线段树存储，大概长这样。
```
09 0a ['\t', '\n']
81 82 ['func_81', 'func_82']
    81 - 40 43 [' 丂 ', ' 丄 ', ' 丅 ', ' 丆 ']
    82 - 40 43 [' 侤 ', ' 侫 ', ' 侭 ', ' 侰 ']
```

用什么数据结构存储呢？**最快的应该是把这个数据结构做到 PE 文件里面，避免任何查询操作，直接就是函数跳转。**
代码大概这样：
```c
int func_81(GETBYTE getbyte) { if (!getbyte) return -1;
    if (getbyte(1) >= 0x40 && getbyte(1) <= 0x43) {
        const static MYCHAR chararray[] = { 0x4e02, 0x4e04, 0x4e05, 0x4e06 };
        return chararray[getbyte(1) - 0x40];
    }
    return -1;
}

int func_82(GETBYTE getbyte) { if (!getbyte) return -1;
    if (getbyte(1) >= 0x40 && getbyte(1) <= 0x43) {
        const static MYCHAR chararray[] = { 0x4fa4, 0x4fab, 0x4fad, 0x4fb0 };
        return chararray[getbyte(1) - 0x40];
    }
    return -1;
}

int func_gbk(GETBYTE getbyte) { if (!getbyte) return -1;
    if (getbyte(0) >= 0x09 && getbyte(0) <= 0x0a) {
        const static MYCHAR chararray[] = { 0x9, 0xa };
        return chararray[getbyte(0) - 0x09];
    }
    if (getbyte(0) >= 0x81 && getbyte(0) <= 0x82) {
        const static MYFUNC funcarray[] = { func_81, func_82 };
        return funcarray[getbyte(0) - 0x81](getbyte);
    }
    return -1;
}
```

脚本代码生成的代码：
<a href="{% include relref.html url="/source/mycode/mycode_gbk.txt" %}" target="_blank">mycode_gbk.c</a>
<a href="{% include relref.html url="/source/mycode/mycode_utf8.txt" %}" target="_blank">mycode_utf8.c</a>
<a href="{% include relref.html url="/source/mycode/mycode_utf16le.txt" %}" target="_blank">mycode_utf16le.c</a>

最后编译出来：<a href="{% include relref.html url="/source/mycode/toystrings.exe" %}" target="_blank">toystrings.exe</a>。

直接命令行输入文件，结果存在文件 `*.pedump.strings.txt` 里面。
```
C:\kSource\pythonx>filetool\toystrings.exe filetool\toystrings.exe
https://sunocean.life/tools/
filetool\toystrings.exe
time=94 // 毫秒
```

结果存在文件 `toystrings.exe.pedump.strings.txt` 里面。
```
462848 77 44 gbk 44 "!This program cannot be run in DOS mode.

$"
462848 128 6 gbk 5 "eW 瀡 !6"
462848 131 3 gbk 3 "v!6"
....
```

第一行，文件大小 462848，从 77 开始的 44 字节，gbk 编码，字符串 44 长度："!This program cannot be run in DOS mode...
所有可能的字符串都导出来了。


## 如何防破解

[^_^]: <www.csdn.net/tags/MtTaMg0sNDE0MzQ1LWJsb2cO0O0O.html>

有过破解 native 程序经验的人都知道，在大量的汇编代码面前不可能是从头开始理解代码的，必须找到一两个点进行突破。
字符串往往就是这样的关键点，在代码中 hardcode 的字符串会可以原封不动的在生成的 binary 中查找到。
所以要增加破解的难度，对字符串进行混淆（或者叫加密，下面的文字可能混淆和加密混着用，在这里没有区别）是很重要的一步。
只要字符串在代码中出现，那么其必然会在 binary 中出现，所以要想在 binary 中查找不到字符串，必须在代码进行编译之前进行变形。
所以从理论上来说，可以从下面几个角度进行入手：
1. 编译之前调用程序对字符串进行处理
2. 代码中直接写入混淆后的字符串
3. 编译过程中使用宏等其他手段自动混淆
4. 对生成的 binary 进行处理

[Literalstring encryption as part of the build process](http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro)
这里还有一个项目：[strenc](https://code.google.com/p/strenc/)
[StringsObfuscation System](http://www.codeproject.com/Articles/502283/Strings-Obfuscation-System)
[如何防止客户端被破解 {% include relref_github.html %}](http://tanqisen.github.io/blog/2014/06/06/how-to-prevent-app-crack/)
[Literalstring encryption as part of the build process](http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro)
[PE 文件中隐藏明文字符串](http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2)
[PE 文件中隐藏明文字符串（续）](http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%88%E7%BB%AD%EF%BC%89)
In-Depth:Quasi Compile-Time String Hashing



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2022-07-01-pe-strings.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://docs.microsoft.com/zh-cn/sysinternals/downloads/strings]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/docs.microsoft.com/2cbae266.html" %})
- [http://www.sourceware.org/bugzilla/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.sourceware.org/60356a6f.html" %})
- [https://www.5axxw.com/questions/content/h0ffdn]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.5axxw.com/464cd928.html" %})
- [https://docs.python.org/zh-tw/3.8/library/string.html]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/docs.python.org/6888d893.html" %})
- [http://www.codeproject.com/Articles/2724/Literal-string-encryption-as-part-of-the-build-pro]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.codeproject.com/7ea30383.html" %})
- [https://code.google.com/p/strenc/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/code.google.com/0512edd5.html" %})
- [http://www.codeproject.com/Articles/502283/Strings-Obfuscation-System]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/www.codeproject.com/1fc2ca9c.html" %})
- [http://tanqisen.github.io/blog/2014/06/06/how-to-prevent-app-crack/]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/tanqisen.github.io/c26c44a2.html" %})
- [http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/a.vifix.us/d237afa7.html" %})
- [http://a.vifix.us/blog/pe%E6%96%87%E4%BB%B6%E4%B8%AD%E9%9A%90%E8%97%8F%E6%98%8E%E6%96%87%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%88%E7%BB%AD%EF%BC%89]({% include relrefx.html url="/backup/2022-07-01-pe-strings.md/a.vifix.us/8be44b0a.html" %})
