---
layout: post
title: "MATHEMATICS -- RSA 非对称加密简明原理与大素数生成算法"
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
codeprint:
---


## RSA 原理

将两个大素数相乘十分容易，但是想要对其乘积进行因式分解却极其困难，因此可以将乘积 $N$ 与公开指数 $E$ 一起作为公钥。

基于欧拉定理和费马小定理，下面公式成立：

$$密文=明文^E\ mod\ N$$<br/>
$$明文=密文^D\ mod\ N$$

公钥 $$(E, N)$$，私钥 $$(D, N)$$。

| 名称 | 说明 |
| ---- | ---- |
| $N$ | $N=p\times q$，其中 $p$ 与 $q$ 是两个不同的大素数 |
| $L$ | 可取 $\varphi(N)=(p-1)(q-1)$；更严格也常用 Carmichael 函数 $\lambda(N)=\operatorname{lcm}(p-1,q-1)$ |
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

循环“迭代”（非常规迭代，因为每轮之间是独立的）。“迭代”过程中，如果某步断定是一个合数【断定方式是：有某几个公式，素数一定成立，合数可能成立。所以只要不成立，那么一定是合数。】那么一定是合数。否则只能说明它通过了这一轮测试，是“可能为素数”；对任意奇合数，随机选基的一轮 Miller-Rabin 测试误判概率至多为 1/4，多做几轮可以把误判概率压低。wikipedia：<https://en.wikipedia.org/wiki/Miller%e2%80%93Rabin_primality_test>。

#### AKS 算法

2002 年几个印度人发明的 AKS 方式，则是给出了一个多项式可解的判别法！


### 怎么保证不用太多次加 2 ，就能保证获得一个素数？

这个有赖于素数的概率分布情况。对于整数 n，n 处的连续两个素数的平均间隔大概是 $ln(n)$，而 $ln(n)$ 往往很小了，所以从 $n$ 开始不用做多少次（几百位的一个数，也就是只需要几十几百次而已），就往往发现了一个素数了。而且因为这个平均间隔是比较小的，如果不是要找比 n 大最接近 n 的素数，那么这时候都可以在 +2 好多次（比如几万几十万）都没有找到一个素数的情况下，一下加一个较大的数字然后再次尝试。不可能每次总是需要 +2 好多好多次。


## 棱镜计划

RSA 的安全性不仅取决于大数分解困难，也取决于足够的密钥长度、正确的填充方案和可靠的随机数生成。如果密钥生成的熵不足，或者随机数生成器存在缺陷，攻击者就可能把搜索空间大幅缩小；历史上 Dual_EC_DRBG 之类的随机数后门争议，核心风险就在这里。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-09-12-math-prime-rsa.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://en.wikipedia.org/wiki/Miller%e2%80%93Rabin_primality_test]({% include relrefx.html url="/backup/2020-09-12-math-prime-rsa.md/en.wikipedia.org/5e1ad223.html" %})
