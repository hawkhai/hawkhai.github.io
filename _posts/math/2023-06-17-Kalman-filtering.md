---
layout: post
title: "人工智能 -- 卡尔曼滤波（Kalman filtering）"
author:
location: "珠海"
categories: ["人工智能"]
tags: ["人工智能"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster: "草履虫"
---

草履虫都能看懂的 **卡尔曼滤波** 。

卡尔曼滤波（Kalman filtering）一种利用线性系统状态方程，通过系统输入输出观测数据，对系统状态进行最优估计的算法。
由于观测数据中包括系统中的噪声和干扰的影响，所以最优估计也可看作是滤波过程。


## 原理

卡尔曼滤波器是一种基础预测定位算法。原理非常简单易懂。核心过程可以用一个图说明：

{% include image.html url="/assets/images/230617-kalman-filtering/640xsfa.jpg" %}

本质上就是这两个状态过程的迭代，来逐步的准确定位。

预测：当前状态环境下，对下一个时间段 t 的位置估计计算的值。

更新：更具传感器获取到比较准确的位置信息后来更新当前的预测问位置，也就是纠正预测的错误。

你可能要问为什么有传感器的数据了还要进行更新？因为在现实世界中传感器是存在很多噪声干扰的，所以也不能完全相信传感器数据。卡尔曼算法依赖于线性计算，高斯分布，我们以一维定位来介绍算法的实现。

{% include image.html url="/assets/images/230617-kalman-filtering/640322.jpg" %}
{% include image.html url="/assets/images/230617-kalman-filtering/64022333.png" %}

接下来我们开更新，预测后我们获取到传感器数据，表示目前传感器发现小车的位置应该是在 26 这个位置，在这种情况下，我们肯定是觉得传感器的准确度比我之前的预测瞎猜要来的准确。

所以方差自然会比较小，最终我们觉得真是的小车位置应该是更靠近传感器数据的，而且方差会缩小，以至于，想想也很清楚，我猜了一个预测值，现在有个专家告诉了我相对比较靠谱的数据，那我对小车的位置的自信度肯定会上升啊。

最终小车的位置经过这个时间段 t 的更新就是下图红色的高斯图：

{% include image.html url="/assets/images/230617-kalman-filtering/640233332432.jpg" %}

一维模型下的 Kalman 公式：

预测

{% include image.html url="/assets/images/230617-kalman-filtering/640zz.jpg" %}

更新
{% include image.html url="/assets/images/230617-kalman-filtering/640asdf.jpg" %}
{% include image.html url="/assets/images/230617-kalman-filtering/v2-5cab699068c59861e0172a72309bda1b_1440w.jpg" %}


## 参考代码

```cpp
#include <iostream>
#include <math.h>
#include <tuple>

using namespace std;

double new_mean, new_var;

tuple<double, double> measurement_update(double mean1, double var1, double mean2, double var2)
{
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2);
    new_var = 1 / (1 / var1 + 1 / var2);
    return make_tuple(new_mean, new_var);
}

tuple<double, double> state_prediction(double mean1, double var1, double mean2, double var2)
{
    new_mean = mean1 + mean2;
    new_var = var1 + var2;
    return make_tuple(new_mean, new_var);
}

int main()
{
    //Measurements and measurement variance
    double measurements[5] = { 5, 6, 7, 9, 10 };
    double measurement_sig = 4;

    //Motions and motion variance
    double motion[5] = { 1, 1, 2, 1, 1 };
    double motion_sig = 2;

    //Initial state
    double mu = 0;
    double sig = 1000;

    for (int i = 0; i < sizeof(measurements) / sizeof(measurements[0]); i++) {
        tie(mu, sig) = measurement_update(mu, sig, measurements[i], measurement_sig);
        printf("update:  [%f, %f]\n", mu, sig);
        tie(mu, sig) = state_prediction(mu, sig, motion[i], motion_sig);
        printf("predict: [%f, %f]\n", mu, sig);
    }

    return 0;
}
```


## refs

* [基础卡尔曼滤波 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/66018778)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2023-06-17-Kalman-filtering.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://zhuanlan.zhihu.com/p/66018778]({% include relrefx.html url="/backup/2023-06-17-Kalman-filtering.md/zhuanlan.zhihu.com/09703068.html" %})
