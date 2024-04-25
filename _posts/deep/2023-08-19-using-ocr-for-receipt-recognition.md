---
layout: post
title: "人工智能 -- Deep Dive Into OCR for Receipt Recognition"
author:
location: "珠海"
categories: ["人工智能"]
tags: ["人工智能"]
toc: true
toclistyle: none
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "人工智能课程"
---

> No matter what you choose, an LSTM or another complex method, there is no silver bullet. Some methods are hard to use and not always useful.

二维周期函数来调整网格识别：
{% include image.html url="/assets/images/230819-using-ocr-for-receipt-r~b4/640assfx.jpg" %}
{% include image.html url="/assets/images/230819-using-ocr-for-receipt-r~b4/6402233.jpg" %}

为此，我们使用了 OCRopus 库来进行识别。
1. Tesseract
    Tesseract 是 Google 开发的 OCR 引擎，支持多种语言的文本识别，包括英语、中文、日语等。该引擎基于 LSTM 模型，具有高精度和良好的可扩展性，是目前最流行的 OCR 引擎之一。
2. OCRopus
    OCRopus 是一款基于 Python 的 OCR 引擎，支持多种语言的文本识别，包括中文、日语、韩语等。该引擎具有高精度和良好的可扩展性，可以轻松地集成到不同的应用中。


## OCR 识别开源项目对比

OCR 技术路线图总体上可分为五步：

图像预处理、切割字符、识别字符、恢复版面、后处理文字。

图像非均匀分割技术
LSTM 网络
No matter what you choose, an LSTM or another complex method, there is no silver bullet.
Some methods are hard to use and not always useful.


## refs

[Deep Dive Into OCR for Receipt Recognition](https://dzone.com/articles/using-ocr-for-receipt-recognition)
<https://mp.weixin.qq.com/s/24hJjWnlh4rHotb6YZb1MQ>
原文链接：<https://dzone.com/articles/using-ocr-for-receipt-recognition>
原文作者：Ivan Ozhiganov



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-08-19-using-ocr-for-receipt-recognition.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://dzone.com/articles/using-ocr-for-receipt-recognition]({% include relrefx.html url="/backup/2023-08-19-using-ocr-for-receipt-recognition.md/dzone.com/fea6307b.html" %})
- [https://mp.weixin.qq.com/s/24hJjWnlh4rHotb6YZb1MQ]({% include relrefx.html url="/backup/2023-08-19-using-ocr-for-receipt-recognition.md/mp.weixin.qq.com/0a4c9800.html" %})
