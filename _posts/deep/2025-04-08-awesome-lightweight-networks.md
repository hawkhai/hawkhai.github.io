---
layout: post
title: "机器学习 -- 轻量级模型"
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

目前在深度学习领域主要分为两类，一派为学院派（Researcher），研究强大、复杂的模型网络和实验方法，旨在追求更高的性能； 另一派为工程派（Engineer），旨在将算法更稳定、更高效的落地部署在不同硬件平台上。
[note {% include relref_github.html %}](https://github.com/murufeng/awesome_lightweight_networks)

EfficientNet (EfficientNet-B0~B7 - 2019, EfficientNetV2 - 2021) -- efficientnet_b0
* EfficientNet B0 ~ B7：虽然不算最轻量，但 B0/B1 仍兼具精度和效率，适合移动设备。

MobileNet (MobileNetV2 - 2018, MobileNetV3 - 2019) -- mobilenet_v3_large
* MobileNetV2：经典轻量级模型，速度快、精度尚可。用于分类、检测、分割等任务。
* MobileNetV3 (Large / Small)：更高效，适合边缘设备，分为 small 和 large 两个版本。

ShuffleNet (ShuffleNetV2 - 2018) -- shufflenet_v2_x1_0
* ShuffleNetV2：极度轻量，非常适合低计算资源场景。

0408-shufflenet_v2_x0_5-0.964 | 3MB | 0.964
0408-shufflenet_v2_x1_0-0.986 | 10MB | 0.986
0408-mobilenet_v3_small-0.987 | 12MB | 0.987
0408-mobilenet_v2-0.995       | 18MB | 0.995
0408-efficientnet_b0-0.995    | 32MB | 0.995
0408-mobilenet_v3_large-0.994 | 33MB | 0.994



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-04-08-awesome-lightweight-networks.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/murufeng/awesome_lightweight_networks]({% include relrefx.html url="/backup/2025-04-08-awesome-lightweight-networks.md/github.com/2d379123.html" %})
