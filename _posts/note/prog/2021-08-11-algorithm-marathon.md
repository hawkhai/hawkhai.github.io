---
layout: post
title: "编程马拉松 HACKATHON 2021 -- 数据特征匹配和编译原理"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

1. 数据结构在硬盘上如何存储、如何以最小的 IO 代价读取需要的数据？
2. 字符串匹配算法（包含多模式），相似度匹配算法；
3. 编译原理；
    * TLSH，SSDEEP 算法。
    * LEX、YACC、LLVM。[TinyCompiler {% include relref_github.html %}](https://github.com/stardust95/TinyCompiler)
    * Windows 核心编程 文件操作 和映射。
4. 参考链接：
    * <https://github.com/trendmicro/tlsh>
    * <https://github.com/ssdeep-project/ssdeep>

* 检索 tlsh & ssdeep 算法。??

* ssdeep cluster analysis for malware files
    * <https://github.com/DinoTools/python-ssdeep>
    * <https://github.com/zom3y3/ssdc>
    * <https://github.com/ZSShen/MeltingPot>
    * <https://github.com/JPCERTCC/impfuzzy>

* 安全 ClamAV

* 数据特征匹配和编译原理

* 搜索技术

* [8.5k] Fuzzy String Matching in Python <https://github.com/seatgeek/fuzzywuzzy>
    * 各种字符匹配算法
    * [1k] Rapid fuzzy string matching in Python using various string metrics <https://github.com/maxbachmann/RapidFuzz>
* [638] A library implementing different string similarity and distance measures using Python. <https://github.com/luozhouyang/python-string-similarity>

* [997] 📚 single header utf8 string functions for C and C++ <https://github.com/sheredom/utf8.h>
* [678] C++ functions matching the interface and behavior of python string methods with std::string <https://github.com/imageworks/pystring>


## Process Hacker

<https://processhacker.sourceforge.io/>


## 经典 KMP 算法

```cpp
#include <stdio.h>
#include <string>
#include <vector>
#include <assert.h>

void getNext(std::string needle, std::vector<int>& next) {
    int i = 0, j = -1;
    // j 表示最长相同前后缀的长度
    next[0] = j;
    while (i < needle.size()) {
        // j == -1 为边界条件判断
        // j = next[j] 可能使 j 退回到 -1
        if (j == -1 || needle[i] == needle[j]) {
            i++;
            j++;
            next[i] = j;
        }
        else {
            j = next[j];
        }
    }
}

int strStr(std::string haystack, std::string needle) {
    if (needle.empty()) return 0;
    int m = haystack.size(), n = needle.size();
    for (int i = 0; i <= m - n; i++) {
        for (int j = 0; j < n; j++) {
            if (needle[j] != haystack[i + j])
                break;
            if (j == n - 1)
                return i;
        }
    }
    return -1;
}

int strStrKMP(std::string haystack, std::string needle) {
    if (needle.empty()) return 0;
    int i = 0, j = 0;
    int m = haystack.size(), n = needle.size();
    std::vector<int> next(n + 1);
    getNext(needle, next);
    while (i < m && j < n) {
        if (j == -1 || haystack[i] == needle[j]) {
            i++;
            j++;
        }
        else {
            j = next[j];
        }
        if (j == n)
            return i - j;
    }
    return -1;
}

void randcarray(char* a, int size) {
    int len = rand() % size;
    for (int i = 0; i < len; i++) {
        a[i] = 'a' + rand() % 10;
    }
    a[len] = 0;
}

int main() {
    char a[10] = { 0 };
    char b[10] = { 0 };
    for (int i = 0; i < 10000; i++) {
        randcarray(a, 10);
        randcarray(b, 10);
        int x = strStr(a, b);
        int y = strStrKMP(a, b);
        assert(x == y);
        if (x > 0) {
            x = y;
        }
    }
    return 0;
}
```


## ssdeep & pyssdeep


## murmur


## tlsh



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-08-11-algorithm-marathon.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/stardust95/TinyCompiler]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/f9a59853.html" %})
- [https://github.com/trendmicro/tlsh]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/cc0a8021.html" %})
- [https://github.com/ssdeep-project/ssdeep]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/8f5b1bea.html" %})
- [https://github.com/DinoTools/python-ssdeep]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/e17265d4.html" %})
- [https://github.com/zom3y3/ssdc]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/b227aab8.html" %})
- [https://github.com/ZSShen/MeltingPot]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/fea2a8c9.html" %})
- [https://github.com/JPCERTCC/impfuzzy]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/c42b10a8.html" %})
- [https://github.com/seatgeek/fuzzywuzzy]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/1c8f1638.html" %})
- [https://github.com/maxbachmann/RapidFuzz]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/cd3e5286.html" %})
- [https://github.com/luozhouyang/python-string-similarity]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/ca448faf.html" %})
- [https://github.com/sheredom/utf8.h]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/1fb3e284.html" %})
- [https://github.com/imageworks/pystring]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/94e8df70.html" %})
- [https://processhacker.sourceforge.io/]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/processhacker.sourceforge.io/83bbc907.html" %})
