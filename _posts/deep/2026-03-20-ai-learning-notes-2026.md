---
layout: post
title: "机器学习笔记 -- 自然语言处理、智能感知与通信、智慧医疗"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习", "NLP", "智慧医疗"]
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

Vector Space Models
<https://www.kaggle.com/code/shivamsourav2002/vector-space-models>

N-gram 语言模型与平滑技术
<https://www.kaggle.com/code/rtatman/tutorial-getting-n-grams>
Spanish text corpora
<https://www.sketchengine.eu/guide/n-grams-multiword-expressions/>

CBOW（Continuous Bag-of-Words）模型详解
Neural Network Word Embedding Using Keras
<https://www.kaggle.com/code/ozlerhakan/neural-network-word-embedding-using-keras>
<https://github.com/y33-j3T/Coursera-Deep-Learning/blob/master/Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204%20-%20Word%20Embeddings%20with%20Neural%20Networks/NLP_C2_W4_lecture_nb_01.ipynb>

<https://www.geeksforgeeks.org/machine-learning/introduction-to-recurrent-neural-network/>
下面 pytorch 版本更简单，colab 支持
<https://docs.pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html>

* 特征提取偏差：CNN 将皮草误识别为猫、手机误识别为鼠标，主要源于训练数据不足或特征提取能力不足，可通过增加数据或更换更强 CNN 解决。
* 数据增强副作用：CNN 训练时的旋转增强导致模型无法区分上下空间关系（如将天空误判为沙滩），需移除旋转类数据增强操作。
* 单帧信息局限：单张图像无法区分动作的连续性（如 "throwing" vs "catching"），需引入时序信息（Video）或连续帧来解决。


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
- [https://www.kaggle.com/code/shivamsourav2002/vector-space-models]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/www.kaggle.com/65842495.html" %})
- [https://www.kaggle.com/code/rtatman/tutorial-getting-n-grams]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/www.kaggle.com/d94e51e6.html" %})
- [https://www.sketchengine.eu/guide/n-grams-multiword-expressions/]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/www.sketchengine.eu/d691b9d2.html" %})
- [https://www.kaggle.com/code/ozlerhakan/neural-network-word-embedding-using-keras]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/www.kaggle.com/8dc1a642.html" %})
- [https://github.com/y33-j3T/Coursera-Deep-Learning/blob/master/Natural%20Language%20Processing%20with%20Probabilistic%20Models/Week%204%20-%20Word%20Embeddings%20with%20Neural%20Networks/NLP_C2_W4_lecture_nb_01.ipynb]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/github.com/6bbe232c.html" %})
- [https://www.geeksforgeeks.org/machine-learning/introduction-to-recurrent-neural-network/]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/www.geeksforgeeks.org/33fe67c3.html" %})
- [https://docs.pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/docs.pytorch.org/6785d3ed.html" %})
- [https://omniscient-house-4e0.notion.site/deb10f4bbd7941daa551d075063ba5be]({% include relrefx.html url="/backup/2026-03-20-ai-learning-notes-2026.md/omniscient-house-4e0.notion.site/8d1cae52.html" %})
