---
layout: post
title: "Vibe Coding 氛围编程"
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
permalink:
archived:
date: 2025-06-24 09:52:22 +0800
layoutclear: false
---

AI 编程不仅仅是编码领域的事情，而是典型的软件开发，符合软件工程规律。
遵守以下流程，不轻易跳步。AI 虽然强大，也受制于你给他什么，Garbag in Garbag out，一步渣步步渣。

> 未来的软件，不但是给人用的，同时也是给 AI 用的。
> 所以不但要提供 GUI 界面，还须要提供 MCP 接口，以供 豆包、元宝 之类的 AI 应用直接调用整合。
> 不提供 MCP 接口的软件，会被慢慢淘汰。
> AI 智能体（Agents）。它们是计算机，但行为类似人类。它们就像「互联网的灵魂」，需要与软件基础设施交互。
> 所以，我们需要让软件更易于被 AI 理解和操控。

AI 就像新型计算机，LLM 像新的「CPU」。
上下文窗口相当于内存；而整个 LLM 则负责在这些资源之间协调内存与计算，以解决问题。

{% include image.html url="/assets/images/250624-vibe_coding/640zz.png" %}

LLM 就像「人类精神」的模拟体 —— 它们是人类的「随机模拟器」。
* 优点：LLM 拥有百科全书般的知识与记忆能力，远远超过任何单一人类个体。它们可以轻松记住 Git SHA 哈希值、各种信息、文件结构等内容。
    就像电影《雨人》里的「自闭症天才」，能一字不差地背下电话簿。
* 缺点：LLM 同时也存在很多「认知缺陷」，比如容易幻觉（hallucination），胡编乱造，缺乏对自身知识状态的良好感知。
* 智能参差不齐：它们在某些任务上表现超人，但有时却会犯一些基本错误，比如说「9.11 大于 9.9」。这种「锯齿形智能」现象很独特。
* 前向性遗忘：LLM 不具备持久学习的能力。

我们正在与 AI 合作 —— AI 负责生成，人类负责验证。我们需要尽可能地加快这个生成—验证的循环，这样才能真正提高效率。
* 加快验证速度。GUI 非常关键。视觉界面能调动人类大脑「图像识别 GPU」，而阅读文本费力又不直观。图形界面是直通大脑的高速通道。
* 牢牢地把 AI 控制在手上。很多人现在对「AI 智能体」（agent）过于兴奋。但实际上，如果 AI 给软件 repo 提交了 10,000 行代码，那人类审查员就是最大瓶颈：还得逐行确保没有引入 bug，没有安全问题等等。

{% include image.html url="/assets/images/250624-vibe_coding/640xx.png" %}

「与 LLM 合作的最佳实践」：
「明确的提示语」（prompt）很关键；
如果提示太模糊，AI 可能偏离预期，导致验证失败；
一旦验证失败，就要不断试错、反复循环；
所以花点时间写更明确、清晰的 prompt，其实是提高效率的关键。


## References

* [史诗级预言！Karpathy 演讲刷屏：软件 3.0，人人皆「代码之神」 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/yfjm23XhFwQQOPcOkbJDMQ)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-06-24-vibe_coding.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s/yfjm23XhFwQQOPcOkbJDMQ]({% include relrefx.html url="/backup/2025-06-24-vibe_coding.md/mp.weixin.qq.com/93a2c705.html" %})
