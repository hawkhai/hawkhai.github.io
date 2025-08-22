---
layout: post
title: "工作笔记 -- 氛围编程 Windsurf 最佳实践"
author: ahai
location: "twiki"
categories: ["工作笔记"]
tags: ["编程", "工作笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid: true
glslcanvas:
codeprint:
permalink:
archived:
layoutclear: true
---

得益于大模型的发展，提示词工程没那么重要了，只要把问题描述清楚就可以了，更重要的是 **上下文工程** 。

1. 头脑风暴，和 AI 讨论问题。
2. 编码实践，给 AI 下达明确的编码任务。

LLM 拥有百科全书般的知识与记忆能力，远远超过任何单一人类个体。
它们可以轻松记住 Git SHA 哈希值、各种信息、文件结构等内容。
直接把一大片的错误信息粘贴给它都是没问题的（甚至错乱都是可以的），虽然人类不行。
大模型 Token 的上下文窗口受限，而人类能够通过抽象和压缩，实现几乎无限的上下文整合与理解。
**车往哪里开，可能还是要程序员决定，因为程序员相对 AI，拥有无限的上下文。**

1. 给 AI 明确的编码任务。
2. 验收 AI 的代码。
3. 准备下一轮的提示词。「明确的提示语」（prompt）很关键； 如果提示太模糊，AI 可能偏离预期，导致验证失败； 一旦验证失败，就要不断试错、反复循环； 所以花点时间写更明确、清晰的 prompt，其实是提高效率的关键。

在关键时候帮助 Windsurf 切换上下文，至关重要。
如果发现它采集到的 上下文不准确，可以重启，可以新开 tab，可以直接给它指定明确的代码位置，就非常准了。
还有就是要把你的问题进一步抽象简化，能表现的更好。
Windsurf 升级后，在我的工作中，绝大部分代码都能一遍过。


## AI Generation + Human Verification

Karpathy 观察到，目前最有效和 AI 协作模式是“AI 负责生成，人类负责验证”，要让这个循环尽可能快速运转，有两个可以调整的方向：

第一，加速人类验证过程：设计验证友善的输出格式。

所有 AI 的输出都应该考虑人类验证的便利性，这可能意味著结构化的呈现、清楚的标记，或是互动式的介面。
比如说，以程式开发为例，与其让 AI 用文字描述改动，不如直接显示程式的红绿差异对比。这让人类能快速扫描并理解变更，大幅提升验证速度。

第二，让 AI 在控制范围内：避免过度自主。

在这里需要让 AI 尽可能提升它可以通过人类成功验证的机率。Karpathy 提到要给 AI 套上缰绳：“如果你想要完成实际工作，过度反应的 agent 就不是那么棒了。”
他在自己的工作中总是害怕得到太大的程式码差异，宁愿采用小增量的方式，确保每一步都能被理解和验证。
除此之外，模糊的提示会导致 AI 偏离预期，进而增加验证失败的机率。所以花点时间撰写具体明确的 prompt，可以大幅提高验证成功率。
Karpathy 在演讲中推荐这篇文章，可以如何和 AI 更好协作，像是提供更多背景资讯、拆解问题，当问题越具体，AI 表现得越好，以及可以建立详细的文件，这件事透过 LLM 来做会变得更轻松。

{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/ppt_rectified.png" %}
{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/GuEizCpWcAALy0Q.jfif" %}


## Windsurf 底层原理初探

可以认为由这几部分组成：
1. 远端的 大模型
2. 本地 一堆内置 MCP 工具
3. 最关键的 本地大模型服务
    * language_server_windows_x64.exe
    * GO 语言编写并直接打包的，逻辑都在里面。

#### 框架简述

1. AI 服务：Exafunction 专业 AI 推理平台
2. Tree-sitter (tree-sitter) - 增量解析库，用于语法高亮和代码分析
3. 编辑器请求 → Go LSP 服务 → 语言分析 → 意图识别
4. 语法树 + 上下文 → Exafunction AI → 意图分类 → 动作建议
5. Chardet (github.com/saintfish/chardet) 字符编码检测库
6. CEL (cel.dev) 谷歌通用表达语言（Common Expression Language，简称 CEL）
7. Common Expression Language，Google 开源的表达式求值引擎

这个系统通过语法解析 → 上下文理解 → AI 推理 → 意图分类 → 动作建议的完整管道，实现了高度智能和个性化的用户意图分析。
<div class="mermaid">
graph TD
    A[用户输入] --> B[Tree-sitter 语法解析]
    B --> C[语言类型识别]
    C --> D[上下文提取]
    D --> E[Exafunction AI 推理]
    E --> F[意图分类]
    F --> G[动作建议生成]
    G --> H[ConnectRPC 响应]
    H --> I[编辑器展示]
</div>

对话流程集成
```
用户输入 → Windsurf 前端
    ↓
AI 语言服务器 (Go)
    ↓ 分析需要的工具
大模型推理 (Exafunction)
    ↓ 生成工具调用
MCP 工具执行
    ↓ 返回结果
AI 语言服务器整合响应
    ↓
Windsurf 前端显示结果
```


## 头脑风暴

这个例子很多。

让大模型根据工程提供优化方法。
大模型一口气说了十个正确的大道理，关键时刻，可能还是依赖人的判断。
提供数据，询问怎么优化，他可以说十条建议，看起来都好有道理，能提供大量灵感：
{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/20250601184500.png" %}
{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/20250601184756.png" %}


## 最佳实践

**一切都是围绕上下文优化进行的。**
上下文包含：
1. 当前打开的工程文件夹
2. 当前打开的代码文件（关闭其它文件，仅仅保留一个最核心的文件）
3. 当前会话的上下文信息。

这些看似无关紧要的操作，对 Windsurf 非常关键。
能让他的 上下文 收集逻辑 工作的更好。


### 跑不动了，尝试重启 Windsurf

language_server_windows_x64.exe 也会得到重启。
这玩意貌似有点问题，久了内存会越来越大。


### 抽象出更小的完备问题，重新指定文件夹

启动的时候，Windsurf 会对文件夹代码进行 RAG 索引，更小的索引数据库更有利于上下文检索。

最可靠的方法是：
从你的大工程里面抽离出独立完备的小问题，然后全部搞好验收后再整合回大工程。
大问题里面抽象一个小问题，独立的文件夹工程，独立的运行跑通了，最后在积木一样拼装成大工程。

可以想象，一个巨大的项目，要 RAG 抽取上下文是非常困难的，但是一个小工程，往往非常准确。


### 每个问题，维护一个独立的上下文 Tab

避免问题和问题上下文互相干扰。


### 直接告诉 AI 关键的上下文，跳过 RAG

最好包含文件的硬盘绝对路径和代码行，大模型能看懂，这是它最擅长的事情。
{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/2025-08-20_151932_786.png" %}

直接粘贴成片的错误信息，大模型非常喜欢。

一个印象深刻的例子是：
```
这个项目以后的运行都用这个 python 跑，记住了：
I:\ocr_data\Python\Python310-mineru\Python310-mineru\python.exe
```

然后它真的记住了。


### 指出它的错误，它会积极改正

{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/2025-08-20_152320_492.png" %}

{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/20250702215231.png" %}

```
Traceback (most recent call last):
  File "I:\pdfai_serv\font\workspace\font_serv.py", line 152, in <module>
    main_serv()
  File "I:\pdfai_serv\font\workspace\font_serv.py", line 133, in main_serv
    code = kremote.remote_init(idx, parent_callback, sys.argv)
  File "I:\pdfai_serv\font\workspace\pythonx\kremote\kremote_wrapper.py", line 473, in remote_init
    result = self._remote_Init(idx, c_callback_func, argc, self.argv_array)
OSError: exception: access violation reading 0x000000000000000D
```

{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/20250702215240.png" %}
{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/20250702215251.png" %}

最佳搭档，写了好多遍都写不对，提示一下，全部秒对。

* 底层控制：直接操作内存，绕过 ctypes 的高层抽象
* 无拷贝风险：`memmove` 是真正的内存复制，不存在参数传递拷贝问题
* 明确语义：`const char**` 就是一个内存地址，我们直接往这个地址写入指针值


### 及时删除临时文件或者代码文件

它遇到问题了，就会新建文件 test，造成一堆垃圾文件代码。
这些都会严重干扰 RAG 上下文收集。

相应的，这个任务也可以直接交给大模型：
```
用 PowerShell 命令 删除临时文件或者代码文件。
```

这样做，可以有效的保证 RAG 索引的有效和小巧。


### 不用给文档，直接给它分析几个本地的文件示例

顺便说明 这样做的意图，大模型可以工作的更好。

{% include image.html url="/assets/images/250625-vibe-coding-best-practi~79/2025-08-20_153041_021.png" %}


### 源码文件拆分

源码文件拆分，每个源码大概维持在五百行左右不超过一千行。
每个函数大概维持在五十行左右不超过一百行。


### 命名！命名！命名！

因为底层是大语言模型，有歧义的文件名或者变量名会严重误导模型。
关键思考，要不断重构源文件名和变量名。

工程的整个结构和风格要遵循传统，以便和大模型的大量训练语料保持一致。
尽量不要有过多的个人风格和标新立异。

有这样一段代码：

```
model:
  choice: torchvision-mobilenet_v2 # torchvision- or custom-
  num_classes: 7 # out_channels of fc, maybe be not equal to num_classes of train_dir.
```

大模型老是出错，问题就出在 `num_classes` 的命名，后来全部改成 `fc_out_features` 并加上准确的注释，就再也没错过了：
```
model:
  choice: torchvision-mobilenet_v2 # torchvision- or custom-
  fc_out_features: 7 # out_channels of fc, maybe be not equal to num_classes of train_dir.
                     # eg: maybe more than num_classes
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-06-25-vibe-coding-best-practices-for-windsurf.md.js" %}'></script></p>
