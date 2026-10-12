---
layout: post
title: "工作笔记 -- ai timeline"
author:
location: "twiki"
categories: ["工作笔记"]
tags: ["编程", "工作笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
archived:
layoutclear: false
---


## 为什么世界模型需要分层规划？

[H-JEPA！LeCun 世界模型创业交卷，代码权重全部开源 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/U8r0Nn9fT7eC7BAXx1ZUPQ)
让模型在不同抽象层级和时间尺度上预测，再通过分层规划，把复杂目标落实为动作。

**假设你正坐在纽约大学的办公室里，准备去巴黎。规划整趟行程时，你关注的是目的地、航班和时间安排。确定行程后，你开始进一步安排如何离开办公室、下楼、打车去机场。等到了真正走出办公室时，你关注的信息又变成了眼前的地面、楼梯，以及下一步该落在哪里，先迈哪只脚。**

这些规划层级既覆盖不同的时间跨度，也需要不同的信息。规划航程时，脚下某一级台阶的高度并不重要；走下楼梯时，这个细节却直接决定你该怎样迈步。
而这，也并不是人类规划独有的特性。对于机器人来说，高层需要理解任务目标、环境关系和未来方向，低层则需要掌握具体动作和身体控制细节。
比如，四足机器人已经走到了目标位置，但腿部姿态与目标画面不同，模型仍可能因为这些差异，认为自己离目标很远。

----

01:30 探索的缘起

07:25 怎么读论文？（用 AI 学 AI）

10:20 辅助小工具和路书

视频教程：

* 吴恩达的机器学习 / AI 课程
* 李宏毅：生成式 AI 时代下的机器学习（2025）
* Andrej Karpathy YouTube
* B 站：李沐论文精读系列
* B 站：3Blue1Brown 的数学与神经网络介绍部分
* B 站：王木头学科学
* B 站：Zomi

书籍：

* 《一站式 LLM 底层技术原理入门指南》
* 《动手学深度学习（PyTorch 版）》：作者李沐本人有配套中文视频
* 《深度学习的数学》


## 19:35 Part 1：模型的范式变迁

故事要从 1999 年的第一颗 GPU 开始讲起

Brook: 用 GPU 进行计算 （2004.08）

AlexNet: 深度学习的开端（2012.10）

对序列建模：seq2seq 和 Attention 的引入（2014.09）

蒸馏：模型能被学习吗？（2015.03）

ResNet: 比深更深（2015.12）

Transformer 来了！拉开一个时代的序幕（2017.06）

AlphaGo Zero: 强化学习的突破（2017.10）

现代 MoE 的开端（2017.01）

CoT: Prompt Engineering 的奠基之作（2022.01）

LoRA: 那个我们每天都在用的东西（2021.06）

ReAct: Agent 从理论到落地（2022.10）

The Bitter Lesson: 过去 70 年的教训（2018.08）


## 01:52:58 Part 2：Infra 与数据的变迁

ZeRO: 大规模的 GPU 并行计算（2019.10）

Scaling Law & Chinchilla: 上帝的指挥棒（2020.01 2022.03）

LAION-5B: 开源社区的英雄主义（2022.10）

The RefinedWeb: 互联网的数据也很够用（2023.06）

MegaScale: 万卡 GPU 集群的训练（2024.02）


## 02:21:29 Part 3：语言模型的发展

Word2Vec: 用机器学习将单词向量化（2013.01）

Google Translate: 神经网络的大规模线上部署（2016.09）

GPT-1，它来了（2018.06）

BERT: 曾经的王（2018.10）

GPT-2: 是时候告别微调了（2019.02）

GPT-3: ChatGPT 来临前夜（2020.05）

InstructGPT: 给 LLM 以文明（2022.03）

Tulu 3: 后训练的开源（2024.11）


## 03:08:08 Part 4：多模态模型的发展

DeepVideo: 深度学习进入视频领域，Andrej 初出茅庐（2014.06）

双流网络 : Karén 和学术重镇牛津登场（2014.06）

图像生成的序章 : GAN 来了（2014.06）

Diffusion: 在 GAN 的阴影下，悄然成长（2015.03）

DDPM: Diffusion 重回图像舞台的中央（2020.06）

ViT: 当图像遇到 Transformer（2020.10）

CLIP: 文生图的奠基石（2021.03）

Latent Diffusion 论文（2021.12）；Stable Diffusion 公开发布（2022.08）

DiT: 人们期待一个融合的未来（2022.12）


## 03:56:38 最后的聊天

架构抱住了硬件的大腿

今天技术的边界到达了哪？

给“站在AI世界门外张望的人”和“已经在体系中工作多年的人”的建议

<https://www.bilibili.com/video/BV1pkyqBxEdB/>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-05-16-ai-timeline.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s/U8r0Nn9fT7eC7BAXx1ZUPQ]({% include relrefx.html url="/backup/2026-05-16-ai-timeline.md/mp.weixin.qq.com/6123f7d9.html" %})
- [https://www.bilibili.com/video/BV1pkyqBxEdB/]({% include relrefx.html url="/backup/2026-05-16-ai-timeline.md/www.bilibili.com/60922afc.html" %})
