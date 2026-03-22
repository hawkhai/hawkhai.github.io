---
layout: post
title: "机器学习笔记 -- 自然语言处理、智能感知与通信、智慧医疗"
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
cluster:
---


## 自然语言处理

Hung-Yi Lee

* Homepage: <https://speech.ee.ntu.edu.tw/~hylee/index.php>
* NLP: <https://speech.ee.ntu.edu.tw/~hylee/dlhlp/2020-spring.php>


## 高级软件工程

gstack：把 Claude Code 变成软件工厂
<https://omniscient-house-4e0.notion.site/deb10f4bbd7941daa551d075063ba5be>


## 智能感知与通信


### 智能感知技术

从压缩感知到视觉跟踪
稀疏表示理论、RIP 严格数学基础与 L1 Tracker 应用

RIP（Restricted Isometry Property）严格数学基础

**定义** ：字典 $D$ 对所有 k-稀疏向量 $x$ 保持长度近似不变：

$$
(1 - \delta_k)|x|_2^2 \le |D x|_2^2 \le (1 + \delta_k)|x|_2^2
$$

* $\delta_k \in (0,1)$ 称为 **RIP 常数**
* 含义：任意 k 个原子形成的子字典近似正交
* 数学基础：RIP 是保证 ℓ₁ 最小化恢复稀疏解的充分条件
* **Candes 定理** （严格条件）：如果 $\delta_{2k} < \sqrt{2} - 1$，ℓ₁优化可以准确恢复 k-稀疏向量。

> 本质上，RIP 是一个“长度保持不变”的条件，它量化了字典与理想正交字典的接近程度。


## 智慧医疗技术与系统



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-03-20-ai-learning-notes-2026.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://speech.ee.ntu.edu.tw/~hylee/index.php]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/speech.ee.ntu.edu.tw/dd2ca1ba.php" %})
- [https://speech.ee.ntu.edu.tw/~hylee/dlhlp/2020-spring.php]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/speech.ee.ntu.edu.tw/23ab625b.php" %})
- [https://omniscient-house-4e0.notion.site/deb10f4bbd7941daa551d075063ba5be]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/omniscient-house-4e0.notion.site/8d1cae52.html" %})
