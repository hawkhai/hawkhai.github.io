---
layout: post
title: "机器学习 -- Attention is all you need"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
---

注意力机制。网上很多文章，但是我这篇文章应该是最浅显易懂的。零基础都能看懂，并且学会手算。
各位专家帮忙 Review，如果存在错误或者不严谨的地方，我再改改。


## 简单描述

**注意力机制通俗解释**
以淘宝搜索为例：

1. **查询** ：我们输入查询（query，$Q$），比如“笔记本”。

2. **计算相似性** ：淘宝后台拿到这个查询 Q，并用这个查询 Q 和后台商品的关键字（key，$K$）进行相似度计算，
    得到物品和我的查询的相似性（或者说物品对应的相似性权重），相似度越高，越有可能推送给我们。

3. **得到价值** ：这个时候还有考虑物品的价值（value，$V$），这个 V 不是指物品值几块钱，
    而是物品在算法中的价值。如果商家给了淘宝广告费，或物品物美价廉、评价好、点赞多等等，那么就越有可能推送给我们。

4. **计算带权重的价值** ：用相似性乘价值，就得到了带权重的价值。
    淘宝最后会按照值从高到低的顺序返回显示在页面上。


## 向量描述

$$
\operatorname{Attention}(Q, K, V)=\operatorname{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V
$$

**上面的整个过程用向量矩阵表达，就是 注意力机制。** 往往得到的矩阵非常庞大。
高维空间的 Token 表示，往往蕴含很多相关信息。

注意力机制的本质是一种权重分配机制，即对不同重要程度的信息赋予不同的权重，让系统学会注意力关注重点信息，同时忽略无关信息。

自注意力是对每个输入赋予的权重取决于输入数据之间的关系，即通过输入项内部之间的相互博弈决定每个输入项的权重。

[代码 transformer/Modules.py {% include relref_github.html %}](https://github.com/jadore801120/attention-is-all-you-need-pytorch/blob/master/transformer/Modules.py)：
```python
class ScaledDotProductAttention(nn.Module):

    def __init__(self, temperature, attn_dropout=0.1):
        super().__init__()
        self.temperature = temperature
        self.dropout = nn.Dropout(attn_dropout)

    def forward(self, q, k, v, mask=None):

        attn = torch.matmul(q / self.temperature, k.transpose(2, 3))

        if mask is not None:
            attn = attn.masked_fill(mask == 0, -1e9)

        attn = self.dropout(F.softmax(attn, dim=-1))
        output = torch.matmul(attn, v)

        return output, attn
```


## 手算示例

$Q$、$K$、$V$ 都是 $X$ 的线性变换。
为了方便，我们直接用 $X$ 做自注意力机制。

$$
\text { Attention }(X, X, X)=\operatorname{softmax}\left(\frac{X X^T}{\sqrt{d_k}}\right) X
$$

假如 $X$ “笔记本”每个字的向量表示分别是：
* “笔” `[1, 2, 1, 2, 1]`
* “记” `[1, 1, 1, 2, 1]`
* “本” `[3, 2, 1, 1, 1]`

$X^T$ 就是：

“笔” | ”记” | “本”
---- | ---- | ----
1 | 1 | 3
2 | 1 | 2
1 | 1 | 1
2 | 2 | 1
1 | 1 | 1

那么 $XX^T$ 就是：

~    | “笔” | ”记” | “本”
---- | ---- | ---- | ----
“笔“ | 11   | 9    | 11
“记” | 9    | 8    | 9
“本” | 11   | 9    | 16

而分母 $\sqrt{d_k}$ 可以先不管，是个常数，这个的目的是保证梯度的。
“$\sqrt{d_k}$，影响 $softmax$ 分布，没有它某个 Token 容易出现极端概率。”
{% include image.html url="/assets/images/240630-attention/20240721170523.png" %}

$\operatorname{softmax}({X X^T})$ 就是：

~    | “笔” | ”记” | “本”
---- | ---- | ---- | ----
“笔“ | 0.468 | 0.064     | 0.468
“记” | 0.422 | 0.156     | 0.422
“本” | 0.0069 | 9.05E-04 | 0.992

这里 每行的和都是 等于 $1$ 的，这个是 $softmax$ 函数的特性。

最终 $\operatorname{softmax}\left(X X^T\right) X$ 就成了：

* “笔” `[1.94, 1.94, 1, 1.53, 1]`
* “记” `[1.84, 1.84, 1, 1.58, 1]`
* “本” `[2.98, 2, 1, 1.01, 1]`

**此时每个汉字在高维空间的位置 就被更新了。**
是不是很神奇？！


## 更多 ...

Attention is all you need
transformer
bert
@vcubingx

{% include image.html url="/assets/images/240630-attention/accesswximg.png" %}


## What does it mean for computers to understand language? \| LM1

<https://www.youtube.com/watch?v=1il-s4mgNdI>
<https://www.bilibili.com/video/BV1jx4y1t7Lq/>


## Why Recurrent Neural Networks are cursed \| LM2

<https://www.youtube.com/watch?v=rTz6hadM1Lg>
<https://www.bilibili.com/video/BV1qi421e7DH/>


## How did the Attention Mechanism start an AI frenzy? \| LM3

注意力机制被用于 Transformer 中，起源于修复 RNN 的问题。
<https://www.youtube.com/watch?v=lOrTlKrdmkQ>
<https://www.bilibili.com/video/BV1Dw4m1e74b/>


## Transformer 论文逐段精读【论文精读】

<https://www.bilibili.com/video/BV1pu411o7BE/>
假设更一般，对数据信息的抓取能力更差，所以需要更多数据更大的模型才能训练出来。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-06-30-attention.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/jadore801120/attention-is-all-you-need-pytorch/blob/master/transformer/Modules.py]({% include relrefx.html url="/backup/2024-06-30-attention.md/github.com/88984250.html" %})
- [https://www.youtube.com/watch?v=1il-s4mgNdI]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.youtube.com/b22ed315.html" %})
- [https://www.bilibili.com/video/BV1jx4y1t7Lq/]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.bilibili.com/dbbaac38.html" %})
- [https://www.youtube.com/watch?v=rTz6hadM1Lg]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.youtube.com/337c0aa5.html" %})
- [https://www.bilibili.com/video/BV1qi421e7DH/]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.bilibili.com/ce799314.html" %})
- [https://www.youtube.com/watch?v=lOrTlKrdmkQ]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.youtube.com/49f0d0af.html" %})
- [https://www.bilibili.com/video/BV1Dw4m1e74b/]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.bilibili.com/4ff97324.html" %})
- [https://www.bilibili.com/video/BV1pu411o7BE/]({% include relrefx.html url="/backup/2024-06-30-attention.md/www.bilibili.com/d4534f87.html" %})
