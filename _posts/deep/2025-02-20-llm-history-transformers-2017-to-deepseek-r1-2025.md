---
layout: post
title: "机器学习 -- 大型语言模型简史：从 Transformers (2017) 到 DeepSeek-R1(2025)"
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
cluster: "机器学习课程"
---

[大型语言模型简史：从 Transformers (2017) 到 DeepSeek-R1(2025)](https://medium.com/@lmpo/%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%AE%80%E5%8F%B2-%E4%BB%8Etransformer-2017-%E5%88%B0deepseek-r1-2025-cc54d658fb43)

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/1_mtohu_WU9ykYZUztwmDTjg.webp" %}

> GRPO 人工智能的每次发展，基本原理感觉都很简单，那些完成严格数学表达，完整代码实现的人，应该都是天才。
> 在尝试了大量可能后，找到了那条最优美的路。简洁的像诗歌，璀璨如星辰。
> 每当深夜阅读这些文章，总会令人惊叹与震撼，感受那纯粹的美妙。高雅又优雅！
> 不管什么奇奇怪怪的模型结构，不管多少维度的 Tensor 都能算梯度，并完成正向反向传播。
> 这些极度聪明的人推动了人工智能的发展。而我，不够聪明，无法参与其中。


## 交叉熵、信息熵、相对熵、KL 散度

*Amount of Information*
for an event:
* small probability --> large amount of information
* large probability --> small amount of information
* amount of information of independent events can be summed

for a probability distribution:
* pdf more uniform --> more random --> larger entropy
* pdf more condensed --> more certain --> smaller entropy

KL 散度（也叫相对熵）公式：

$$
D_{K L}(p \| q)=\sum_{i=1}^n p\left(x_i\right) \log \left(\frac{p\left(x_i\right)}{q\left(x_i\right)}\right)
$$

**交叉熵**
交叉熵主要应用：主要用于度量同一个随机变量 $X$ 的预测分布 $Q$ 与真实分布 $P$ 之间的差距。
差距可理解为：距离、误差、失望值、困难程度、混乱程度、一辆车、一套房。

$$
\begin{aligned}
& H(P, Q)=-\sum_{i=1}^n p\left(x_i\right) \log q\left(x_i\right) \\
& H(P, Q)=\sum_x p(x) \cdot \log \left(\frac{1}{q(x)}\right)
\end{aligned}
$$

**CrossEntropyLoss**

$$
\operatorname{loss}(x, \operatorname{class})=-\log \left(\frac{\exp (x[\operatorname{class}])}{\sum_j \exp (x[j])}\right)=-x[\operatorname{class}]+\log \left(\sum_j \exp (x[j])\right)
$$

程序算交叉熵：
```python
entroy = nn.CrossEntropyLoss()
input = torch.Tensor([[-0.7715, -0.6205, -0.2562]])
target = torch.tensor([0])
output = entroy(input, target) # 打印输出：1.3447
```

为什么在很多的网络模型中，使用交叉熵做损失函数而不使用 KL 散度做损失函数呢？
* 此时：KL 散度 = 交叉熵-信息熵 = 交叉熵 - 0 = 交叉熵
* 因为有真实分布，所以用交叉熵。如果没有真实分布，请用 KL 散度。

[香农熵，交叉熵和 KL 散度 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1JY411q72n/)


## GRPO（Group Relative Policy Optimization）

DeepSeek-R1 GRPO 算法揭秘
<https://www.bilibili.com/video/BV15zNyeXEVP/>

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/bc1c0ea5c7052810b5f2ea6482be5b75.png" %}
<https://blog.csdn.net/v_JULY_v/article/details/136656918>

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/1e5e5964c5cf44759136de53a5a89808.png" %}

<https://huggingface.co/docs/trl/main/en/grpo_trainer>


## DeepSeek V3 & R1

<https://space.bilibili.com/288748846>
* DeepSeek V3 模型架构创新点
    * MoE(Mixture of Experts): 提出了一种解决 expert 不均衡问题的非 loss 解法
    * MLA(Multi-head Latent Attention): 多头注意力情况下，推理面临的 K,V 缓存空间大问题
    * MTP(multi-token prediction): 训练阶段让模型预测后几跳的 token，提升模型性能

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/20250304003905.png" %}
{% include image.html url="/assets/images/250220-llm-history-transformer~a8/20250304003923.png" %}
{% include image.html url="/assets/images/250220-llm-history-transformer~a8/20250304003933.png" %}
{% include image.html url="/assets/images/250220-llm-history-transformer~a8/20250304003942.png" %}

* DeepSeek-R1 GRPO 算法揭秘
* 单卡 20G 显存，复现 DeepSeek R1 顿悟时刻



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://medium.com/@lmpo/%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%AE%80%E5%8F%B2-%E4%BB%8Etransformer-2017-%E5%88%B0deepseek-r1-2025-cc54d658fb43]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/medium.com/32ba340f.html" %})
- [https://www.bilibili.com/video/BV1JY411q72n/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/41ca4b25.html" %})
- [https://www.bilibili.com/video/BV15zNyeXEVP/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/28741d25.html" %})
- [https://blog.csdn.net/v_JULY_v/article/details/136656918]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/blog.csdn.net/d3167ade.html" %})
- [https://huggingface.co/docs/trl/main/en/grpo_trainer]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/huggingface.co/fe7b7c63.html" %})
- [https://space.bilibili.com/288748846]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/space.bilibili.com/fe2c6382.html" %})
