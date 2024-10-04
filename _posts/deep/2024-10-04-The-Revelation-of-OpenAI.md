---
layout: post
title: "机器学习 -- OpenAI 启示录"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

## [GPT、DALL·E、Sora，为什么 OpenAI 可以跑通所有 AGI 技术栈？ weixin](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247495280&idx=1&sn=8a95107cc3a7ea50afa066d3f466e236&chksm=c1aa2d52f67d274007c6e2f8a51bd60f464ee23060824880813bbcf7d209f41bc5c2f1934798&scene=0&xtrack=1)


OpenAI 的 blog 中对 Sora 的定位正是「作为世界模拟器的视频生成模型」。这里是 OpenAI 2016 (!) 年一篇文章的原话 (链接：https://openai.com/research/generative-models)：

> 我们常常会忽略自己对世界的深刻理解：比如，你知道这个世界由三维空间构成，里面的物体能够移动、相撞、互动；人们可以行走、交谈、思考；动物能够觅食、飞翔、奔跑或吠叫；显示屏上能展示用语言编码的信息，比如天气状况、篮球比赛的胜者，或者 1970 年发生的事件。
> 这样庞大的信息量就摆在那里，而且很大程度上容易获得——不论是在由原子构成的物理世界，还是由数字构成的虚拟世界。挑战在于，我们需要开发出能够分析并理解这些海量数据的模型和算法。
> 生成模型是朝向这个目标迈进的最有希望的方法之一。要训练一个生成模型，我们首先会在某个领域收集大量的数据（想象一下，数以百万计的图片、文本或声音等），然后训练这个模型去创造类似的数据。这个方法的灵感来自于理查德·费曼的一句名言：
> 「我所无法创造的，我也不能理解。」（即：要真正理解一个事物，你需要去创造它） 
> 这个方法的妙处在于，我们使用的神经网络作为生成模型，其参数的数量远远少于训练它们的数据量，这迫使模型必须发现并有效地吸收数据的精髓，以便能够创造出新的数据。

### 公理 1: The bitter lesson。

我认为所有做 AI 的人都应该熟读这篇文章。「The bitter lesson」说的事情是，长期来看，AI 领域所有的奇技淫巧都比不过强大的算力夹持的通用的 AI 算法（这里「强大的算力」隐含了大量的训练数据和大模型）。某种意义上，强大的算力加持的通用的 AI 算法才是 AGI 路径的正道，才是 AI 技术真正进步的方向。从逻辑主义，到专家系统，到 SVM 等核方法，到深度神经网络，再到现在的大语音模型，莫不过此。
www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf

### 公理 2: Scaling Law。

这条公理说了，一旦选择了良好且通用的数据表示，良好且通用的数据标注，良好且通用的算法，那么你就能找到一套通用规律，保证数据越多，模型越大，效果越好。而且这套规律稳定到了可以在训练模型之前就能预知它的效果：

## [2万字复盘：OpenAI的技术底层逻辑](https://new.qq.com/rain/a/20230417A0332A00)

OpenAI 在过去 5 年坚定的选择了用 GPT（Generative Pre-trainning Transformer）架构持续加注 LLM（Large Language Model）的技术路径。

2018 年 6 月 OpenAI 发布 GPT-1，两个月后 Google 发布 BERT 。BERT 在下游理解类任务表现惊人，不仅高于 GPT-1（117M），且基本导致 NLP 上游任务研究意义的消失。

在整个 NLP 领域学者纷纷转向 BERT 研究时， OpenAI 进一步加码并于 2019 年 2 月推出 GPT-2（1.5B）。GPT-2 虽然在生成任务上表现惊艳，但是在理解类任务的表现上仍然全面落后于 BERT。

在这样的背景下，OpenAI 依然坚持 GPT 路线并且大幅度加大 Scale 速度，于 2020 年 5 月推出了 GPT-3（175B）。GPT-3 模型参数 175B（百倍于 GPT-2），训练数据量 500B Tokens（ 50 倍于 GPT-2）。



## [OpenAI到底做对了什么？](https://baijiahao.baidu.com/s?id=1770459534019883480&wfr=spider&for=pc)


技术路线一：无监督学习

OpenAI刚成立不久，就在Ilya Sutskever的领导下下注“无监督学习”这条道路。熟悉AI研究领域的朋友都知道，今天这个看起来无比正确的决定，在2015-2016年，绝对不是那么显而易见。因为彼时的人工智能领域，通过标注数据方法的“监督学习”大行其道，在很多垂直领域比如推荐系统、机器视觉等，效果也更好。


技术路线二：生成式模型


“What I cannot create, I do not understand. 如果不能创造，就无法理解”。

为什么OpenAI选择押注自然语言？套用著名哲学家维特根斯坦“语言的边界就是世界的边界”。如果用Ilya Sutskever的话来说 “语言是世界的映射，GPT是语言的压缩”。就人类智能而言，自然语言是核心中的核心，而其他视觉、语音等都不过是自然语言的辅助佐料。


技术路线四：解码器

在Transformer打开了大语言模型的理论窗口之后，大语言模型发展出了三种路线。第一种，以Google BERT、ELECTRA为代表的Encoder-Only（编码器）路线；第二种，以Google T5、BART为代表的Encoder- Decoder（编解码器）路线；第三种，以OpenAI GPT为代表的Decoder-Only（解码器）路线。

这三种路线，Encoder-Only路线适合理解类任务，很难应对生成式任务，也不具有好的扩展性和适应性，虽然被Google BERT在个别子领域一度带火，但现在几乎处于被主流抛弃的地步。Encoder- Decoder路线适合特定场景任务，但通用性和扩展性也比较差。Decoder-Only路线首先非常适合生成类任务，同时对各类任务都具有很好的通用性，在工程上也具有很高的可扩展性（scale），非常适合将模型规模做大。








