---
layout: post
title: "学习笔记 -- WordTap 英语学习入门：点读查词、听读发音与文章跟打"
author: qhai
location: "珠海"
categories: ["学习笔记"]
tags: ["WordTap", "英语学习", "英语点读", "词汇学习", "文章跟打", "开源工具"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
permalink: /blog/2026/10/10/wordtap-technical-english
excerpt: "英语点读为学习而生。用两句英文体验点词查义、音标、听读入口和文章跟打，也可以从课文或词库开始，按自己的节奏继续学习。"
date: 2026-10-10 00:00:00 +0800
archived:
layoutclear:
wordtap: true
wordtap_share: true
image: /assets/wordtap/english-learning/wordtap-blog-cover.jpg
last_modified_at: 2026-10-21
---

**英语点读为学习而生。点词查义 · 听读发音 · 文章跟打。**

WordTap 是一款以英语点读为核心的开源英语学习工具。点击英文单词即可查看释义、音标并听发音，结合课文阅读、词汇积累和文章跟打，让理解、听读与拼写练习围绕同一份学习材料展开。

可以选择内置课程，也可以使用自己的英文材料。无需注册，学习记录保存在当前浏览器。

本教程使用公开站的当前功能。先做一次两句英文的小练习，再换成你正在学的课文或词汇。

**[开始学习](https://wordtap.cn/)** · [GitHub 源码](https://github.com/hawkhai/wordtap.cn)

## 1. 选择课程，或使用自己的学习材料

打开课程菜单，可以选择新概念、人教版等课文，也可以从“英语词汇”选择词库、搜索词头并打开一篇文章。课程和词库加载后都能点词学习；词汇跟打使用例句，无例句时练词头。

也可以在“输入或粘贴文章”区域使用自己的材料。本次粘贴下面两句原创英文：

```text
I learn a little English every day.
New words help me understand the world.
```

点击编辑区之外，让可点读正文出现。先试着理解：第一句说的是怎样的学习习惯？第二句里的新单词能帮助我们做什么？

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/01-read.jpg"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/01-read.jpg" alt="WordTap 英语学习：两句英文已出现在输入区和点读正文中" width="912" style="width:912px;max-width:100%;height:auto;"></a>

*图 1｜课程、词库和自己的材料都能用于学习。这里使用两句原创英文，准备点读。*

## 2. 点词查义、看音标，再听发音

点击第一句的 `learn`，在释义卡片中查看词义和音标；打开“显示音标”可以在正文的英文原词下方显示词典音标。词义需要结合当前句子理解，音标是认读辅助。

点击单词会尝试播放发音，也可以用释义卡片中的朗读入口重听。将鼠标移到句子上，句末会显示小朗读按钮；点击可听整句，再次点击可以停止。触屏直接点句末按钮。单词、句子和全文朗读会互相停止，避免同时播放。

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/02-lookup.jpg"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/02-lookup.jpg" alt="WordTap 英语学习：点击 learn 后，原句、中文释义和音标同时可见" width="912" style="width:912px;max-width:100%;height:auto;"></a>

*图 2｜原文、learn 的中文释义和音标同时可见。单词和句子朗读帮助你把词形与声音联系起来。*

两句可以理解为：“我每天学一点英语。新单词帮助我理解世界。”你可以换一种自己的说法，确认自己理解了句意，再继续练习。

可用声音取决于设备、浏览器和所选服务。基础点读、ECDICT 查词和跟打不需要额外安装服务；可选 Gateway 提供在线全文朗读。截图和无声动图仅展示操作入口，不能证明实际发音效果。

## 3. 用刚学过的句子练习拼写

点击“文章跟打”，在输入框中键入第一句。可以故意把 `every` 写成 `everx`：

```text
I learn a little English everx day.
```

原句对应字母会标红，提示应为 `y`、当前为 `x`。把它改回 `every`，再读一次整句。

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/03-typing-error.jpg"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/03-typing-error.jpg" alt="WordTap 英语学习：跟打输入 everx 后显示应输入 y 的错误提示" width="912" style="width:912px;max-width:100%;height:auto;"></a>

*图 3｜everx 的最后一个字母出错，原句标记和输入提示指出需要把 x 改为 y。*

跟打只比较英文字母，忽略大小写、空格和标点。它用于拼写与输入练习，不评价句意理解或发音，也不提供语法批改。

## 4. 修正后确认，继续下一句

第一句输入正确后，按 Enter 或点击“下一句”确认。再输入第二句：

```text
New words help me understand the world.
```

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/04-typing.jpg"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/04-typing.jpg" alt="WordTap 英语学习：第二句输入正确但尚未确认，已完成 1 / 2 句" width="912" style="width:912px;max-width:100%;height:auto;"></a>

*图 4｜第二句已输对，仍等待确认；此时只完成了第 1 / 2 句。*

“自动朗读新句”和“输入后自动朗读下一个单词”可以按需要开关。本组截图关闭这两项，以便观察拼写反馈；开启后可以结合听读练习。

## 5. 完成一次练习，下次继续学习

确认第二句后，会看到完成提示和重新练习入口。可以重练，也可以退出跟打回到点读。

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/05-completed.jpg"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/05-completed.jpg" alt="WordTap 英语学习：两句英文跟打已确认完成，可重新练习" width="912" style="width:912px;max-width:100%;height:auto;"></a>

*图 5｜两句都已确认完成。完成表示输入练习结束，是否理解和记住还需要继续复习。*

在“我的单词”查看查过的词；文章可在“保存过的文章”中找到。使用同一浏览器、同一站点可以恢复文章和跟打草稿，继续上次练习。

公开站“考试学习”页的“导出学习数据”包含单词、文章、考试进度、考试生词和跟打进度；“我的单词”中的单词导出只包含单词。换设备时手动导入备份，核对文章与进度后再清理旧设备数据。个人版旧格式备份不包含文章，使用该版本时另存原文。

翻译和音频缓存不包含在完整备份中。首次加载、未缓存资源和在线服务仍需要网络；在线查词或语音可能把相应单词、文本发送给服务方。

## 换成你正在学习的内容

选择一篇课文、一组词汇例句，或 2–5 句自己的英文材料：**先理解句意 → 点词查义与听读 → 跟打巩固 → 下次继续复习。** 可以由老师、家长或学习搭子陪伴操作，按自己的学习节奏进行。

**[开始英语学习](https://wordtap.cn/)**。这次学习对你有帮助？欢迎给 [WordTap 点个 Star](https://github.com/hawkhai/wordtap.cn)，支持后续维护。[遇到问题或有建议](https://github.com/hawkhai/wordtap.cn/issues)也可以反馈浏览器、示例和复现步骤。

<a href="{{ site.baseurl }}/assets/wordtap/english-learning/wordtap-20s.gif"><img src="{{ site.baseurl }}/assets/wordtap/english-learning/wordtap-20s.gif" alt="WordTap 英语点读、查词与跟打五步演示，无音轨" width="1000" style="width:1000px;max-width:100%;height:auto;"></a>

图片取自 2026-10-21 本地构建预览，五张静态图和动图使用同一段材料。动图是五张真实截图组成的 20 秒步骤演示，无音轨；不代表输入速度、实际声音或学习效果。入口可能随版本更新。


<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-10-10-wordtap-technical-english.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://wordtap.cn/]({% include relrefx.html url="/backup/2026-10-10-wordtap-technical-english.md/wordtap.cn/b6eeb1f3.html" %})
