---
layout: post
title: "机器学习 -- ChatGPT Prompt 提示词 吴恩达（进行中）"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "机器学习课程"
---

<https://www.bilibili.com/video/BV1Z14y1Z7LJ/>
<https://zhuanlan.zhihu.com/p/626290417>


## ChatGPT 提示工程师


### 基础大模型（Base Large Language Model）的特点

基于文本训练数据做预测。

输出内容不可控，有可能是有害的内容。


### 指令调整型大模型（Instruction tuned Large Language Model）的特点

首先使用已经在大量文本数据上训练过的基本大模型；

然后用输入、输出的指令进行微调；

然后使用 RLHF（人类反馈强化学习）的技术进一步优化；

输出内容可控，内容是有益、诚实和无害的。


## 第 2 集 指南


### 第一原则：编写具体和明确的指令。

第一，明确不等于少，而是指指令清晰和明确，如果只需要少量的文字就可以达到清晰和明确的效果，也是可以的。

第二，策略。

使用好分隔符

避免提示注入

prompt 中指定验证条件

“少量样本”提示


### 第二原则

给模型足够的时间去思考，你可以把 ChatGPT 想象成一个活生生的人，你需要它回答问题，要留够时间让它去思考。


### 限制

ChatGPT 也有一个问题，那就是容易出现幻觉。幻觉就是，ChatGPT 编造听起来很合理的故事，但是完全不符合事实。

要避免产生幻觉，可以采取如下的策略：提取引用，使用引用进行回答，避免幻觉。


## 第 3 集 迭代

很多的情况下，与 ChatGPT 交互一次是不能得到最佳的答案的，需要不断的迭代，直到获得理想的答案。迭代的步骤如下：

提示、分析结果、改进提示、循环直至得到理想的回答。


## 第 4 集 摘要

ChatGPT 可以对大量文字进行总结。


## 第 5 集 推理

ChatGPT 可以对内容进行推理，如提取标签、提取名称、识别情感。


## 第 6 集 聊天机器人

通过 ChatGPT 可以定制一个聊天机器人，第一是确定聊天机器人的角色，第二确定内容的输出格式。


## 第 7 集 扩展

ChatGPT 可以对某个主题的内容，进行内容扩展。


## 第 8 集 转换

ChatGPT 可以对内容进行如下的转换：

语言翻译。

格式转换，如 html、Markdown、json。

语气转换，如朋友语气、专家语气、老师语气、医生语气。

帮助拼写。

语法纠正。


## 第 9 集 总结



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-07-28-chatgpt-prompt.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.bilibili.com/video/BV1Z14y1Z7LJ/]({% include relrefx.html url="/backup/2023-07-28-chatgpt-prompt.md/www.bilibili.com/1c30226b.html" %})
- [https://zhuanlan.zhihu.com/p/626290417]({% include relrefx.html url="/backup/2023-07-28-chatgpt-prompt.md/zhuanlan.zhihu.com/d7c51936.html" %})
