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

> [大型语言模型简史：从 Transformers (2017) 到 DeepSeek-R1(2025)](https://medium.com/@lmpo/%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%AE%80%E5%8F%B2-%E4%BB%8Etransformer-2017-%E5%88%B0deepseek-r1-2025-cc54d658fb43)
> AI 发展太快了，以至于我们称：几个月前的技术为古代，2022 年 ChatGPT 诞生前是上古时代，BERT 之前是史前时代，Transformer 之前则是旧石器时代。
> 系统化知识传授（监督学习），实践探索（强化学习），监督学习只能从冗余的信息里面学习到知识，强化学习才是人工智能的未来。

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/1_mtohu_WU9ykYZUztwmDTjg.webp" %}

> GRPO 人工智能的每次发展，基本原理感觉都很简单，那些完成严格数学表达，完整代码实现的人，应该都是天才。
> 在尝试了大量可能后，找到了那条最优美的路。简洁的像诗歌，璀璨如星辰。
> 每当深夜阅读这些文章，总会令人惊叹与震撼，感受那纯粹的美妙。高雅又优雅！
> 不管什么奇奇怪怪的模型结构，不管多少维度的 Tensor 都能算梯度，并完成正向反向传播。
> 这些极度聪明的人推动了人工智能的发展。而我，不够聪明，无法参与其中。

> 杨立昆坚持认为现在的 LLM 路线是错误的，基本到头了，下一代架构是模仿婴儿建立世界模型 AMI。
> 难度在于怎么完成梯度反向传播，怎么完成多个子系统的对齐。
> 那些复杂的生物行为，都和语言无关，它肯定不会是在 token 空间里完成的，而是在心智空间当中。
> 目前 LLM 有点像是在边边角角上做改进，想办法搞更多数据，更多算力，或者搞点合成数据什么的。

> 抖音算法公开了。基于特征向量的数学统计。
> 算法会围绕用户的反馈建模，有没有点赞、看到了第几秒、写了什么评论、是否点开了作者主页……等等，
> 这些互动都会让算法对一个用户的了解逐渐加深，最终越来越准确的「预测」他会感兴趣的下一条视频。


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
* **因为有真实分布，所以用交叉熵。如果没有真实分布，请用 KL 散度。**

[香农熵，交叉熵和 KL 散度 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1JY411q72n/)


## GRPO（Group Relative Policy Optimization）

DeepSeek-R1 GRPO 算法揭秘
<https://www.bilibili.com/video/BV15zNyeXEVP/>

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/bc1c0ea5c7052810b5f2ea6482be5b75.png" %}
<https://blog.csdn.net/v_JULY_v/article/details/136656918>

{% include image.html url="/assets/images/250220-llm-history-transformer~a8/1e5e5964c5cf44759136de53a5a89808.png" %}


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

$$
\begin{aligned}
& \hat{A}_{i, t}=\frac{r_i-\operatorname{mean}(\mathbf{r})}{\operatorname{std}(\mathbf{r})} \\
& \mathbb{D}_{\mathrm{KL}}\left[\pi_\theta \| \pi_{\mathrm{ref}}\right]=\frac{\pi_{\mathrm{ref}}\left(o_{i, t} \mid q, o_{i,<t}\right)}{\pi_\theta\left(o_{i, t} \mid q, o_{i,<t}\right)}-\log \frac{\pi_{\mathrm{ref}}\left(o_{i, t} \mid q, o_{i,<t}\right)}{\pi_\theta\left(o_{i, t} \mid q, o_{i,<t}\right)}-1 \\
& \mathcal{L}_{\mathrm{GRPO}}(\theta)=-\frac{1}{G} \sum_{i=1}^G \frac{1}{\left|o_i\right|} \sum_{t=1}^{\left|o_i\right|}\left[\frac{\pi_\theta\left(o_{i, t} \mid q, o_{i,<t}\right)}{\left[\pi_\theta\left(o_{i, t} \mid q, o_{i,<t}\right)\right]_{\mathrm{no} \text { grad }}} \hat{A}_{i, t}-\beta \mathbb{D}_{\mathrm{KL}}\left[\pi_\theta \| \pi_{\mathrm{ref}}\right]\right.
\end{aligned}
$$

1. Ref 是原版冻结住的 LLM，存在的目的是：无论 Policy 怎么训练，都不能和 Ref 的 next token prob 偏离太夸张（KL 散度）
2. 同一组答案 RL 会拿来 train N 次，会把 train 之前 policy 的 next token prob 记下来作为基准。
    在每次 train 后 policy 会更新，下次出的 next token prob 除以基准，就形成了给 adv 加权效果，好的 adv 得到放大。

<https://huggingface.co/docs/trl/main/en/grpo_trainer>
[DeepSeek-R1 GRPO 原理 .pptx {% include relref_github.html %}](https://github.com/owenliang/qwen2.5-0.5b-grpo)
单卡 20G 显存，复现 DeepSeek R1 顿悟时刻


## 生成模型综述

[MIT 何恺明：生成模型综述 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1AW9QYoEoo/)


## 马尔可夫链清楚解释

<https://www.bilibili.com/video/BV1XYRJYWE6A>

3. Markov Chains Clearly Explained! Part - 1
4. Markov Chains： Recurrence, Irreducibility, Classes ｜ Part - 2
5. Markov Chains： n-step Transition Matrix ｜ Part - 3

1. [动画讲解马尔可夫链（一）：基本概念 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1ih4y1W7i7/)
2. [动画讲解马尔可夫链（二）：马尔可夫链的属性 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1go4y1h7s8)
3. [动画讲解马尔可夫链（三）：高阶转移矩阵与稳态的关系 {% include relref_bili.html %}](https://www.bilibili.com/video/BV14o4y1h7me)
4. [动画讲解马尔可夫链（四）：生成福尔摩斯探案集 {% include relref_bili.html %}](https://www.bilibili.com/video/BV12m4y1C7qv)
5. [动画讲解马尔可夫链（五）：隐马尔可夫模型 {% include relref_bili.html %}](https://www.bilibili.com/video/BV19a4y1P7Tc)
6. [动画讲解马尔可夫链（六）：前向算法 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1yX4y127ub)

> 回收这块，SpaceX 也就一乐，真回收还得是转转。

> 低代码编程全军覆没。
> 低代码的本意是想让不懂编程的人，像搭乐高积木那样建造自己的屋子。但现实中的楼房需要完备的设计图纸和专业的施工人员，只靠积木是搭不了几层的。实践证明，代码就是人机逻辑交互最好的语言。
> 这个世界是为人类设计的，所以人形机器人才是现阶段的最优解；电脑也是为人类设计的，像人一样使用电脑，才是现阶段 AI 的最优解。

> 端到端是大势所趋。
> 早期的自动驾驶采用流水线式的 workflow（pipeline）架构，后来逐步演变为端到端。如今，Agent 也面临类似的问题，并将经历相同的演进，实现端到端的降维打击。人类预设的 workflow 对于模型而言，更像是一种束缚，只有让其自由发挥，才能展现更强大的能力。
> 模型即应用，这一趋势愈发明显。
> 监督学习和半监督学习都受到人类知识的约束，只有强化学习才是未来，AI 自己去找规律。

> 杨立昆坚持认为现在的 LLM 路线是错误的，基本到头了，下一代架构是模仿婴儿建立世界模型 AMI。难度在于怎么完成梯度反向传播，怎么完成多个子系统的对齐。

> “为什么医生养孩子都比较佛系，老师养孩子却比较严厉？”
> “因为老师见过最优秀的孩子，而医生见过最后悔的家长。”
> 我把这个观点和主任说了，主任说，“一开始我也是这样想的，只要孩子开心快乐就好了，后来五年级六年级，成绩垫底，慌得不行！还是得拼一下。”

> 好美想拉屎 这种地方最适合拉屎了 微凉的风吹拂着屁股，草叶轻刮着你的肌肤，远方的小路随时可能有人走来，亮而圆的太阳为这次冒险增加几分心安。
> 在这光的照射下有了便意，于是躲进草地里畅快的拉起野屎来。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://medium.com/@lmpo/%E5%A4%A7%E5%9E%8B%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E7%AE%80%E5%8F%B2-%E4%BB%8Etransformer-2017-%E5%88%B0deepseek-r1-2025-cc54d658fb43]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/medium.com/32ba340f.html" %})
- [https://www.bilibili.com/video/BV1JY411q72n/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/41ca4b25.html" %})
- [https://www.bilibili.com/video/BV15zNyeXEVP/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/28741d25.html" %})
- [https://blog.csdn.net/v_JULY_v/article/details/136656918]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/blog.csdn.net/d3167ade.html" %})
- [https://space.bilibili.com/288748846]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/space.bilibili.com/fe2c6382.html" %})
- [https://huggingface.co/docs/trl/main/en/grpo_trainer]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/huggingface.co/fe7b7c63.html" %})
- [https://github.com/owenliang/qwen2.5-0.5b-grpo]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/github.com/dfca6edc.html" %})
- [https://www.bilibili.com/video/BV1AW9QYoEoo/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/d82bded4.html" %})
- [https://www.bilibili.com/video/BV1XYRJYWE6A]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/28a8ff8d.html" %})
- [https://www.bilibili.com/video/BV1ih4y1W7i7/]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/bed2f5ad.html" %})
- [https://www.bilibili.com/video/BV1go4y1h7s8]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/bc7ee898.html" %})
- [https://www.bilibili.com/video/BV14o4y1h7me]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/e50a9769.html" %})
- [https://www.bilibili.com/video/BV12m4y1C7qv]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/3bb90de6.html" %})
- [https://www.bilibili.com/video/BV19a4y1P7Tc]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/4c625309.html" %})
- [https://www.bilibili.com/video/BV1yX4y127ub]({% include relrefx.html url="/backup/2025-02-20-llm-history-transformers-2017-to-deepseek-r1-2025.md/www.bilibili.com/1cbcddd3.html" %})
