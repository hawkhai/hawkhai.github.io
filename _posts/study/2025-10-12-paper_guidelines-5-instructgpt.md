---
layout: post
title: "论文写作 -- 问题应该怎么描述 / 实验性研究 instructgpt"
author: qhai
location: "珠海"
categories: ["论文写作"]
tags: ["论文写作"]
toc: true
toclistyle:
comments:
visibility: hidden
mathjax: true
mermaid:
glslcanvas:
codeprint:
permalink:
date: 2025-10-12 01:50:53 +0800
archived: true
layoutclear: true
---

# 实验性研究

> * 案例 5：“Training language models to follow instructions with human feedback” (arXiv 2022) [5]（AI 辅助）
> * 问题：用人类反馈强化学习（RLHF）验证“对齐”可行性。
> * 方法：3 步 RLHF，13k SFT + 33k RM 提示 + 人工排序，1.3B 参数。
> * 结论：InstructGPT 相比 GPT-3 偏好率达 85±3%，后续成为 GPT-4 标准流程。

## 提出的问题

传统的语言模型（如 GPT-3）在训练时是通过 **最大化下一个词的似然（next-token prediction）** ，因此虽然能生成流畅文本，但存在以下问题：

1. **不遵守指令（Not following instructions）**
   模型常常答非所问，或者不能理解“任务目标”。

2. **输出内容有害或不适当（Toxic / Untruthful output）**
   模型会输出带偏见、冒犯性、虚假信息的回答。

3. **与人类价值不一致（Misaligned with human intent）**
   模型追求“高概率”文本，而非“人类想要的”文本。

换句话说： **模型很聪明，但不听话、不懂人意。**


## 采用的方法

论文提出了一个叫做 **RLHF（Reinforcement Learning from Human Feedback）** 的三步训练流程，让模型学会“听人话”。

1. **监督微调（Supervised Fine-Tuning, SFT）**

    * 让人类标注者编写 “指令-回答” 示例。
    * 用这些高质量数据对 GPT-3 进行微调，使模型初步学会“按指令回答”。
    * 这得到一个 **SFT 模型** 。

2. **训练奖励模型（Reward Model, RM）**

    * 给 SFT 模型生成的多个回答，请标注者 **人工排序（ranking）** 哪个回答更好。
    * 用这些排序数据训练一个 **奖励模型 RM** ，输入是指令与回答，输出是一个“质量评分”。

3. **强化学习优化（PPO, Proximal Policy Optimization）**

    * 以 SFT 模型为起点，使用奖励模型的评分作为“奖励信号”，
    * 通过 **PPO 算法** 调整模型，使其生成的回答更可能得到高分。
    * 得到最终模型： **InstructGPT** 。


## 解决方案

通过上面的三步，模型能：

* 理解并执行人类的自然语言指令。
* 输出更符合人类意图、更礼貌、更有帮助的答案。
* 减少有害、虚假、无意义内容。

该过程使模型从“预测文本”变成“听懂任务、执行任务”的智能体。


## 主要结论

1. **效果显著提升** ：

   * InstructGPT 比 GPT-3 更受人类偏好（175B InstructGPT 相比 175B GPT-3 优胜率达 85±3%）。
   * 虽然参数量仅为 **1.3B（13 亿）** ，但用户更倾向于它的回答，而非 175B 的 GPT-3。

2. **模型更安全、更有用** ：

   * 减少有害内容、虚假陈述。
   * 更好地遵守指令与上下文语义。

3. **人类反馈的重要性被证实** ：

   * 小规模人类标注结合强化学习，可以显著提升大模型“可用性”。
   * 奠定了后续 ChatGPT 系列（GPT-3.5、GPT-4）的核心训练框架。

论文核心思想： **用人类反馈（Human Feedback）指导语言模型行为，使其输出更符合人类意图。**
这篇论文首次让机器“听懂人话”，从语言模型（LM）走向了“指令模型（Instruction-Following LM）”。
提出并验证了 **InstructGPT** ，即通过人类反馈优化语言模型（Human Feedback, HF），使模型更符合人类期望。


