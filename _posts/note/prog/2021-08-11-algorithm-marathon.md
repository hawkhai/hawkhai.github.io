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
    * LEX、YACC、**LLVM**??。[131] [TinyCompiler {% include relref_github.html %}](https://github.com/stardust95/TinyCompiler)
    * Windows 核心编程 文件操作 和映射。
4. 参考链接：
    * [508] <https://github.com/trendmicro/tlsh>
    * [397] <https://github.com/ssdeep-project/ssdeep>
5. 检索 tlsh & ssdeep 算法。??
    * ~~[116] 另外一个 Python 封装 <https://github.com/DinoTools/python-ssdeep>~~
    * ~~[20] ssdeep cluster analysis for malware files <https://github.com/zom3y3/ssdc>~~
    * [15] Parallel ssdeep clustering kit <https://github.com/a4lg/fast-ssdeep-clus>
    * ~~[21] 构建一个基于 elasticsearch 的本地搜索 <https://github.com/intezer/ssdeep-elastic>~~
    * ~~[22] A tool to cluster similar executables (PEs, DEXs, and etc), extract common signature, and generate Yara patterns for malware detection. <https://github.com/ZSShen/MeltingPot>~~
    * [4.4k] 图形库 Gephi - The Open Graph Viz Platform <https://github.com/gephi/gephi>
    * [8.5k] **Fuzzy String Matching in Python** <https://github.com/seatgeek/fuzzywuzzy>
        * [1k] Levenshtein Distance [python-Levenshtein {% include relref_github.html %}](https://github.com/ztane/python-Levenshtein/)
        * 相似度 Simple Ratio
        * 部分相似度 Partial Ratio
        * 关键字排序相似度 Token Sort Ratio
        * 关键字集合相似度 Token Set Ratio
        * 列表相似度命中 Process

* [958] tiny recursive descent expression parser, compiler, and evaluation engine for math expressions <https://github.com/codeplea/tinyexpr>
* [2.1k] A generic post-processing injector for games and video software. <https://github.com/crosire/reshade>
* [编译原理（Principles and Techniques of Compilers）](https://cs.nju.edu.cn/changxu/2_compiler/index.html)
* Kenneth C. Louden《COMPILER CONSTRUCTION: PRINCIPLES AND PRACTICE》<https://blog.csdn.net/bigconvience/article/details/45965539>

* 安全 ClamAV & yara

* 数据特征匹配和编译原理

* 字符串搜索技术 ?? --

* [8.5k] Fuzzy String Matching in Python <https://github.com/seatgeek/fuzzywuzzy>
    * [1k] Rapid fuzzy string matching in Python using various string metrics <https://github.com/maxbachmann/RapidFuzz>
* [638] A library implementing different string similarity and distance measures using Python. <https://github.com/luozhouyang/python-string-similarity>
    * A library implementing different string similarity and distance measures. A dozen of algorithms (including Levenshtein edit distance and sibblings, Jaro-Winkler, Longest Common Subsequence, cosine similarity etc.) are currently implemented. Check the summary table below for the complete list...
* ~~[997] 📚 single header utf8 string functions for C and C++ <https://github.com/sheredom/utf8.h>~~
* [678] **C++ functions matching the interface and behavior of python string methods with std::string** <https://github.com/imageworks/pystring>
* [556] 编译期间字符串加密，貌似很牛逼。A heavily vectorized c++17 compile time string encryption. <https://github.com/JustasMasiulis/xorstr>
* [468] C 语言实现的一个 HashMap。A simple string hashmap in C <https://github.com/petewarden/c_hashmap>

* ~~[591] QAmatch(qa_match) / 文本匹配 / 文本分类 / 文本 embedding / 文本聚类 / 文本检索 <https://github.com/MachineLP/TextMatch>~~
    * ~~TextMatch is a semantic matching model library for QA & text search ... It's easy to train models and to export representation vectors.~~

* Levenshtein，快速计算字符串相似度。[2.4k] <https://github.com/life4/textdistance>
    * Compute distance between sequences. 30+ algorithms, pure python implementation, common interface, optional external libs usage.
* A python library for doing approximate and phonetic matching of strings. [1.5k] <https://github.com/jamesturk/jellyfish>
    * Jellyfish is a python library for doing approximate and phonetic matching of strings.
    * Levenshtein Distance 编辑距离算法
    * Damerau-Levenshtein Distance 从一个词转换为另一个词的最少操作数，与 Levenshtein Distance 不同的是，除了单个字符的插入、删除和变更之外，还包括两个相邻字符的转换。
    * Jaro Distance 两个单词之间由一个转换为另一个所需的单字符转换的最小数量。
    * Jaro-Winkler Distance 通过前缀因子 p 使 Jaro Distance 相同时共同前缀长度 l 越大的相似度越高。Jaro–Winkler Distance 越小，两个字符串越相似。
    * Match Rating Approach Comparison
    * Hamming Distance 汉明距离度量了通过替换字符的方式将字符串 x 变成 y 所需要的最小的替换次数。
    * use DBSCAN with Levenshtein distances: <https://scikit-learn.org/stable/faq.html#how-do-i-deal-with-string-data-or-trees-graphs>


## LeetCode

[LeetCode 刷题总结 - 字符串篇](https://www.bbsmax.com/A/nAJv1akozr/)

* LeetCode 10 正则表达式匹配
* LeetCode 28 字符串匹配算法
* LeetCode 44 Wildcard Matching（字符串匹配问题）


## 聚类算法

* [895] Python implementations of the k-modes and k-prototypes clustering algorithms, for clustering categorical data <https://github.com/nicodv/kmodes>
* [15] Kmeans and kmodes implementation in Python <https://github.com/hjian42/K-Means-and-K-Modes>


## ClamAV & yara

* 十六进制特征码（shellcode）
* YARA 和 PEiD 可识别加壳文件
* Python 中可以使用 python-magic 程序包确定文件具体类型。
* Python 中可以使用内置的 hashlib 模块或者 PyCrypto 模块生成哈希值。
* 模糊哈希用户确定文件之间的相似度。可使用 ssdeep 命令。


## Process Hacker

这个软件不错。<https://processhacker.sourceforge.io/>


## 经典 KMP 算法

<div class="highlighter-rouge" foldctrl="1"></div>

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


## 其他 murmur / tlsh / ssdeep

高运算性能，低碰撞率的 hash 算法 MurmurHash 算法.zip
* [2k] <https://github.com/aappleby/smhasher>

* [文本相似度 - NLP {% include relref_csdn.html %}](https://blog.csdn.net/zwjyyy1203/article/details/88601256)
    * SimHash 是一种局部敏感 hash，它也是 Google 公司进行海量网页去重使用的主要算法。
* [K-means、DBSCAN 聚类算法 {% include relref_csdn.html %}](https://blog.csdn.net/qq_42549612/article/details/105420109)


## 备注

* 【8.5k】【模糊匹配】 <https://github.com/seatgeek/fuzzywuzzy>
* 【2.4k】【字符串距离】 <https://github.com/life4/textdistance>
* 【1k】【模糊匹配】 <https://github.com/maxbachmann/RapidFuzz>
* 【644】【字符串相似度】 <https://github.com/luozhouyang/python-string-similarity>

* 【131】【编译器】 <https://github.com/stardust95/TinyCompiler>
* 【960】【表达式运算】 <https://github.com/codeplea/tinyexpr>

* 【510】【模糊哈希】 <https://github.com/trendmicro/tlsh>
* 【398】【模糊哈希】 <https://github.com/ssdeep-project/ssdeep>
* 【116】【模糊哈希】 <https://github.com/DinoTools/python-ssdeep>

* 【2.1k】【渲染注入】 <https://github.com/crosire/reshade>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-08-11-algorithm-marathon.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/stardust95/TinyCompiler]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/f9a59853.html" %})
- [https://github.com/trendmicro/tlsh]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/cc0a8021.html" %})
- [https://github.com/ssdeep-project/ssdeep]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/8f5b1bea.html" %})
- [https://github.com/DinoTools/python-ssdeep]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/e17265d4.html" %})
- [https://github.com/zom3y3/ssdc]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/b227aab8.html" %})
- [https://github.com/a4lg/fast-ssdeep-clus]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/ec803475.html" %})
- [https://github.com/intezer/ssdeep-elastic]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/baf1806a.html" %})
- [https://github.com/ZSShen/MeltingPot]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/fea2a8c9.html" %})
- [https://github.com/gephi/gephi]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/3cf185b4.html" %})
- [https://github.com/seatgeek/fuzzywuzzy]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/1c8f1638.html" %})
- [https://github.com/ztane/python-Levenshtein/]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/de4059e4.html" %})
- [https://github.com/codeplea/tinyexpr]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/0fedbec9.html" %})
- [https://github.com/crosire/reshade]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/1f749f9f.html" %})
- [https://blog.csdn.net/bigconvience/article/details/45965539]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/blog.csdn.net/79f55bc5.html" %})
- [https://github.com/maxbachmann/RapidFuzz]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/cd3e5286.html" %})
- [https://github.com/luozhouyang/python-string-similarity]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/ca448faf.html" %})
- [https://github.com/sheredom/utf8.h]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/1fb3e284.html" %})
- [https://github.com/imageworks/pystring]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/94e8df70.html" %})
- [https://github.com/JustasMasiulis/xorstr]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/930489e2.html" %})
- [https://github.com/petewarden/c_hashmap]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/f40e7ecf.html" %})
- [https://github.com/MachineLP/TextMatch]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/ae9d7064.html" %})
- [https://github.com/life4/textdistance]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/5f733930.html" %})
- [https://github.com/jamesturk/jellyfish]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/47014fd6.html" %})
- [https://scikit-learn.org/stable/faq.html#how-do-i-deal-with-string-data-or-trees-graphs]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/scikit-learn.org/bdc82d38.html" %})
- [https://www.bbsmax.com/A/nAJv1akozr/]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/www.bbsmax.com/37dc9268.html" %})
- [https://github.com/nicodv/kmodes]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/53ffffbe.html" %})
- [https://github.com/hjian42/K-Means-and-K-Modes]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/772575be.html" %})
- [https://processhacker.sourceforge.io/]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/processhacker.sourceforge.io/83bbc907.html" %})
- [https://github.com/aappleby/smhasher]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/github.com/78724418.html" %})
- [https://blog.csdn.net/zwjyyy1203/article/details/88601256]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/blog.csdn.net/7d43181f.html" %})
- [https://blog.csdn.net/qq_42549612/article/details/105420109]({% include relrefx.html url="/backup/2021-08-11-algorithm-marathon.md/blog.csdn.net/f3efb9ea.html" %})
