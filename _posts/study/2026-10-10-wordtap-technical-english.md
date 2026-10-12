---
layout: post
title: "学习笔记 -- WordTap：把英文技术文档变成点词阅读和跟打练习"
author: qhai
location: "珠海"
categories: ["学习笔记"]
tags: ["WordTap", "程序员英语", "英文阅读", "开源工具", "文章跟打"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
permalink: /blog/2026/10/10/wordtap-technical-english
excerpt: "读 README、API 说明时被生词打断？WordTap 把原文查词、听发音和逐句跟打放在同一个工作区。用两句缓存说明、五张操作图体验完整流程，无需注册，代码开源。"
date: 2026-10-10 00:00:00 +0800
archived:
layoutclear:
---

读英文技术文档时，最打断思路的往往不是长篇文章，而是眼前的一小段：这个词在这里是什么意思？`it` 指哪个对象？`before` 要求哪一步先做？查到词义后，还得回到原句，把这些关系接起来。

**WordTap 是一个开源的英语阅读与文章跟打工具。** 把需要读的英文粘贴进去，就可以在原句旁查中文释义、听发音；读懂后，切换到文章跟打，用同一段材料练习输入。原文、查词与跟打放在同一个工作区，适合从手头的 README、API 说明或报错解释开始。

这一篇用两句原创的缓存说明，展示从粘贴到完成练习的五个步骤。**无需注册，基础阅读、ECDICT 查词和文章跟打不需要安装额外服务。** 你可以跟着做一次，再换成今天正在读的文档。

**[打开 WordTap，粘贴自己的英文](https://wordtap.cn/)** · [GitHub 源码 {% include relref_github.html %}](https://github.com/hawkhai/wordtap.cn)

五张图依次展示：**粘贴原文 → 点词查释义 → 跟打纠错 → 确认下一句 → 完成练习。**

## 1. 把手头的英文变成可点读正文

打开 WordTap，在“输入或粘贴文章”区域放入这两句。如果编辑区收起，先点击该入口。

```text
The cache stores recent responses.
Clear it before you retry the request.
```

这是教程原创示例，不是某个框架的操作指令。只复制英文，先不要看译文。

输入后，点击下方“点词阅读”区域，让编辑区失去焦点，就会看到可点击的正文。先试着回答：什么保存了最近的响应？重试请求之前要先做什么？

![WordTap 中的两句缓存说明已显示为可点读正文，右上方可切换到文章跟打]({{ site.baseurl }}/assets/wordtap/2026-10-10/01-read.jpg)

*图 1｜用自己的材料开始。上方粘贴原文，下方点词阅读；读完后，可从同一工作区进入“文章跟打”。*

## 2. 查一个生词，接着读原句

点击第一句的 `cache`。原词附近和侧栏会显示词典释义；这次 ECDICT 词条包含“高速缓冲存储器”等解释。在这段话里，可以理解为“缓存”。

查到释义后，可以点击工作区空白处收起浮层。下图保留左侧词典卡片和高亮单词，让两句原文完整可见。

![cache 在原句中高亮，左侧显示音标和中文释义，两句原文完整可见]({{ site.baseurl }}/assets/wordtap/2026-10-10/02-lookup.jpg)

*图 2｜查词时保留上下文。点击 `cache`，在原句旁看释义，再继续理解它保存了什么；词典中的多个意思仍需结合句子选择。*

回到两句原文，抓住这三个关系：

| 原文 | 这段话里的意思 |
| --- | --- |
| The cache stores recent responses. | 缓存保存最近的响应。`stores` 是动词“保存”。 |
| Clear it | 清除它。`it` 指前一句的缓存。 |
| before you retry the request | 在重试请求之前。`before` 说明操作顺序。 |

两句连起来是：**缓存保存最近的响应。在重试请求之前，先清除缓存。** 读技术文档时，除了查生词，也要确认代词、条件和先后顺序。

点击单词会尝试播放发音，也可以使用句末入口听整句。可用声音和播放效果取决于设备、浏览器及所选服务；看静态截图无法判断朗读效果，可以在线试听。

## 3. 把刚读过的句子打出来

点击“文章跟打”，在“在这里跟打”输入框中键入第一句：

```text
The cache stores recent responses.
```

可以故意把最后的 `responses` 写成 `responsex`，看看反馈：原句对应字母标红，输入框下方提示应输入 `s`，当前却是 `x`。把最后一个字母改回 `s`，再继续。

![第一句末词输入为 responsex，原句末字母标红，下方提示应输入 s 而当前是 x]({{ site.baseurl }}/assets/wordtap/2026-10-10/03-typing-error.jpg)

*图 3｜知道错在哪里，才能直接修改。这里故意错了一个字母，原句标记和输入提示一起指出需要把 `x` 改成 `s`。*

跟打使用你刚才读过的原文，可以让阅读和拼写练习接起来。**校验只比较英文字母，忽略大小写、空格和标点**，适合自然语言句子；不能用完成提示判断代码、命令或 URL 是否正确。

## 4. 输对后，自己确认下一步

第一句输入正确后，按 Enter 或点击“下一句”。继续键入：

```text
Clear it before you retry the request.
```

![第二句输入正确，界面显示第 2 / 2 句、已完成 1 / 2 句，以及完成练习按钮]({{ site.baseurl }}/assets/wordtap/2026-10-10/04-typing.jpg)

*图 4｜输对与完成是两个状态。第二句已输入正确，等待你按 Enter 或点击“完成练习”确认；此时进度仍是“已完成 1 / 2 句”。*

“自动朗读新句”和“输入后自动朗读下一个单词”可以按习惯开关。这组截图关闭了两项自动朗读，方便观察输入反馈；开启后可以边打边听。

## 5. 完成练习，再确认句意

确认第二句后，会看到“已完成 2 / 2 句”和重练入口。

![两句均已确认完成，文章跟打显示已完成 2 / 2 句和重新练习入口]({{ site.baseurl }}/assets/wordtap/2026-10-10/05-completed.jpg)

*图 5｜一小段练习有明确终点。“已完成 2 / 2 句”记录本次输入进度；可以重新练习，也可以退出跟打回到阅读。*

离开原文，再用自己的话回答：`it` 指什么？清除缓存和重试请求，哪一个先发生？如果说不清，就回到原句再读。跟打完成说明输入练习结束，理解技术概念仍需要你自己判断。

## 下次继续，以及换设备前怎样备份

文章会出现在“保存过的文章”列表中。使用同一个浏览器打开同一站点，可以恢复最近文章；进入跟打，可继续草稿或查看完成进度。查过的词在“我的单词”中查看。

学习记录保存在当前浏览器，不会自动跨设备同步。更换设备或清理浏览器数据前，在“考试学习”页使用“导出学习数据”，再到另一设备导入；“我的单词”中的单词导出只包含单词。

**版本提示：** 当前公开仓库的完整备份包含文章与跟打进度。旧版存在未包含文章的备份格式；使用旧版时，换设备前请另存原文。导入后确认文章和进度，再清理旧设备数据。

本地保存不等于全部离线。首次加载未缓存资源、在线查词和部分语音服务仍需要网络，相应单词或文本可能发给所选服务。详见 [仓库中的数据、离线与朗读说明 {% include relref_github.html %}](https://github.com/hawkhai/wordtap.cn#数据离线与朗读)。

## 换成你今天正在读的文档

选一段安装说明、API 参数说明或报错解释，先取 **2–5 句连贯的英文正文**，保留主语、条件和前后关系。先说出大意，再查影响理解的词，最后跟打其中一两句。项目专有术语仍以原文定义为准。

**[现在粘贴一段自己的英文](https://wordtap.cn/)**。如果这种“原文查词 → 逐句跟打”的方式对你有用，欢迎给 [WordTap 一个 Star {% include relref_github.html %}](https://github.com/hawkhai/wordtap.cn)，方便下次找到这个工具。也欢迎把这篇教程分享给正在读英文文档的朋友。

遇到问题，请到 [Issues {% include relref_github.html %}](https://github.com/hawkhai/wordtap.cn/issues) 附上浏览器版本、最短示例、操作步骤和预期结果。

仓库里有一份随项目更新的 [独立图文教程 {% include relref_github.html %}](https://github.com/hawkhai/wordtap.cn/blob/main/docs/technical-english-reading.md)。

本文五张截图于 2026-10-12 拍摄自 [WordTap 官网](https://wordtap.cn/)，静态图统一为 912px 宽，入口可能随版本更新。另有一段 [20 秒步骤动图]({{ site.baseurl }}/assets/wordtap/2026-10-10/wordtap-20s.gif)，由同组五张截图组成，画面为 1000 × 650，增加画面外的步骤标题和图注，无音轨；展示操作顺序，不代表实际打字速度或学习效果。


<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-10-10-wordtap-technical-english.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://wordtap.cn/]({% include relrefx.html url="/backup/2026-10-10-wordtap-technical-english.md/wordtap.cn/b6eeb1f3.html" %})
