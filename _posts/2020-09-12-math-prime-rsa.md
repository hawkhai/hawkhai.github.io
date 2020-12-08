---
layout: post
title: "数学之美 -- RSA 非对称加密简明原理与大素数生成算法"
author:
location: "珠海"
categories: ["数学"]
tags: ["数学"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
---


## RSA 原理

将两个大素数相乘十分容易，但是想要对其乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥。

基于欧拉定理和费马小定理，下面公式成立：

$$密文=明文^E\ mod\ N$$<br/>
$$明文=密文^D\ mod\ N$$

公钥 $$(E, N)$$，私钥 $$(D, N)$$。

| 名称 | 说明 |
| ---- | ---- |
| $N$ | $N=p\times q$，且 $p$ 与 $q$ 互质 |
| $L$ | $p−1$ 与 $q−1$ 的最小公倍数 |
| $E$ | $E<L$，并与 $L$ 互质 |
| $D$ | $D<L$，$(E\times D)\ mod\ L＝1$ |


## C++ 代码

{% highlight cpp %}
#include "stdafx.h"
#include <stdio.h>

// a ^ b % p
long int rsa(long int a, long int b, long int N) {
    long int r = 1;
    while (b) {
        if (b & 1) r = r * a % N;
        a = a * a % N;
        b = b >> 1;
    }
    return r;
}

long int getD(long int E, long int N)
{
    long int p, L, D;
    for(p = 2; p < N; p++) {
        if (N % p == 0) {
            L = (p - 1) * (N / p - 1);
            for (D = 2; D < L; D++) {
                if (D * E % L == 1) return D;
            }
        }
    }
    return 0;
}

long int _tmain(long int argc, _TCHAR* argv[])
{
    long int D = 67;  // 私钥 (143, 67)
    long int E = 43;  // 公钥 (143, 43)
    long int N = 143;
    long int in = 126; // 明文

    printf("明文: %d \n", in);
    printf("密文: %d \n", rsa(in, E, N));
    printf("明文: %d \n", rsa(rsa(in, E, N), D, N));
    printf("暴力算私钥: %d \n", getD(E, N));

    return 0;
}
{% endhighlight %}

运行结果：

{% highlight plaintext %}
明文: 126
密文: 48
明文: 126
暴力算私钥: 67
{% endhighlight %}


## 非对称加密算法

RSA、Elgamal、背包算法、Rabin、D-H、ECC（椭圆曲线加密算法）。


## 大素数生成

RSA 所需要的大素数怎样生成的呢？简单说来是这样的：

1. 随机构造一个满足最终大素数长度的奇数。

2. 判断这个奇数是不是素数。如果是，ok，结束；否则，加 2，然后再检验，...，再加 2 再检验，总会遇到一个素数的。

这里面有两个难点需要解决：


### 怎样判断一个奇数是素数？

一个快算法 miller-rabin，但是不准，一个慢算法 AKS，但是准确。

#### miller-rabin 算法

循环“迭代”（非常规迭代，因为每轮之间是独立的）。“迭代”过程中，如果某步断定是一个合数【断定方式是：有某几个公式，质素一定成立，合数可能成立。所以只要不成立，那么一定是合数。而分明是合数，却成立的概率小于 1/4】，那么一定是合数。否则，每一步都能以 1/4 概率的误判率断定是一个素数。如果需要更高的概率精度，那么就多做几轮【承上面括号中内容。如果一次误判的概率小于 1/4，那么没有理由做了 n 多次，每次都撞中了小概率】。这样概率可以任意提高。wikipedia：<https://en.wikipedia.org/wiki/Miller%e2%80%93Rabin_primality_test>。

#### AKS 算法

2002 年几个印度人发明的 AKS 方式，则是给出了一个多项式可解的判别法！


### 怎么保证不用太多次加 2 ，就能保证获得一个素数？

这个有赖于素数的概率分布情况。对于整数 n，n 处的连续两个素数的平均间隔大概是 $ln(n)$，而 $ln(n)$ 往往很小了，所以从 $n$ 开始不用做多少次（几百位的一个数，也就是只需要几十几百次而已），就往往发现了一个素数了。而且因为这个平均间隔是比较小的，如果不是要找比 n 大最接近 n 的素数，那么这时候都可以在 +2 好多次（比如几万几十万）都没有找到一个素数的情况下，一下加一个较大的数字然后再次尝试。不可能每次总是需要 +2 好多好多次。


## 棱镜计划

RSA 算法本身没什么问题，因为只要你的密钥是真正随机产生的，猜对这个密钥就如同大海捞针一般难，现有计算机肯定无法在密码更换周期内攻破你的加密档案。但是，如果这个随机算法是假的呢？如果它仅仅是在一个很小的集合中产生的密钥呢？你的加密档案瞬间就被查看了，这就是 NSA 干的事情。

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://en.wikipedia.org/wiki/Miller%e2%80%93Rabin_primality_test]({% include relref.html url="/backup/2020-09-12-math-prime-rsa.md/en.wikipedia.org/5e1ad223.html" %})
