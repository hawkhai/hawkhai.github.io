---
layout: post
title: "深度学习 -- 吴恩达机器学习（进行中……）"
author:
location: "珠海"
categories: ["深度学习"]
tags: ["机器学习", "深度学习"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
codeprint:
date: 2022-08-31 19:57:58 +0800
---

[机器学习应补充哪些数学基础？ {% include relref_weixin.html %}](https://mp.weixin.qq.com/s?__biz=MzU2NTUwNjQ1Mw==&mid=2247485091&idx=1&sn=8844a2dfafcd35ea45d1bf0146ba8a5a&chksm=fcbbfe59cbcc774f68a18bd11d529422e0048896ffa3a253c52a749fc6e45d7292e1791052da&scene=27#wechat_redirect)

入门的话，本科的数学分析，线性代数，概率论与数理统计足够了。
微积分：MIT 18.01, MIT 18.02
线性代数：MIT 18.06
概率论与数理统计：MIT 6.041
凸优化：CVX101


## 吴恩达

* [吴恩达机器学习系列课程 {% include relref_bili.html %}](https://www.bilibili.com/video/BV164411b7dx)
* [视频的讲义 {% include relref_github.html %}](https://github.com/TheisTrue/MLofAndrew-Ng)


### 有监督学习和无监督学习

监督（supervised）= 标签（label），是否有监督，就是输入数据（input）是否有标签，有标签则为有监督学习，没标签则为无监督学习。
至于半监督学习，就是一半（一点点）数据有标签，一半（极其巨大）数据没标签。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20190717172554930.png" %}

#### 监督学习

[from {% include relref_jianshu.html %}](https://www.jianshu.com/p/682c88cee5a8)

定义：根据已有的数据集，知道输入和输出结果之间的关系。根据这种已知的关系，训练得到一个最优的模型。
也就是说，在监督学习中训练数据既有特征（feature）又有标签（label），通过训练，让机器可以自己找到特征和标签之间的联系，
在面对只有特征没有标签的数据时，可以判断出标签。

监督学习的分类：回归（Regression）、分类（Classification）。

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/20211108161254.png" %}

#### 无监督学习

定义：我们不知道数据集中数据、特征之间的关系，而是要根据聚类或一定的模型得到数据之间的关系。

Cocktail party problem algorithm:
$$
[W, s, v]=\operatorname{svd}\left((\operatorname{repmat}(\operatorname{sum}(x . * x, 1), \operatorname{size}(x, 1), 1) . * x) * x^{\prime}\right)
$$

[note](https://cs.nyu.edu/~roweis/kica.html)
** xx are the mixed microphone measurements (one per column)
** W is the unmixing matrix.
```
% W = kica(xx);
yy = sqrtm(inv(cov(xx')))*(xx-repmat(mean(xx,2),1,size(xx,2)));
[W,ss,vv] = svd((repmat(sum(yy.*yy,1),size(yy,1),1).*yy)*yy');
```


## **Octave** P6 start...


### 1-1. 欢迎参加《机器学习》课程 06:56

完成了。


### 1-2. 什么是机器学习？ 07:15

完成了。


### 1-3. 监督学习 12:30

定义：根据已有的数据集，知道输入和输出结果之间的关系。


### 1-4. 无监督学习 14:14

定义：我们不知道数据集中数据、特征之间的关系，而是要根据聚类或一定的模型得到数据之间的关系。


### 2-1. 模型描述 08:11

yes.


### 2-2. 代价函数 08:13

代价函数：
$$
J \left( \theta_0, \theta_1 \right) = \frac{1}{2m}\sum\limits_{i=1}^m \left( h_{\theta}(x^{(i)})-y^{(i)} \right)^{2}
$$

{% include image.html url="/assets/images/211011-ml-mlofandrew-ng/v2-c94c2b2ffd3d45539f5c80ab2addffcd_720w.jpg" %}

为什么要除以 2，感觉是要让数字小一点，更直观，便于计算。


### 2-3. 代价函数（一） 11:10


### 2-4. 代价函数（二） 08:49


### 2-5. 梯度下降 11:31


### 2-6. 梯度下降知识点总结 11:52


### 2-7. 线性回归的梯度下降 10:21


### 3-1. 矩阵和向量 08:46


### 3-2. 加法和标量乘法 06:55


### 3-3. 矩阵向量乘法 13:40


### 3-4. 矩阵乘法 11:10


### 3-5. 矩阵乘法特征 09:03


### 3-6. 逆和转置 11:14


### 4-1. 多功能 08:23


### 4-2. 多元梯度下降法 05:05


### 4-3. 多元梯度下降法演练 .I.–. 特征缩放 08:53


### 4-4. 多元梯度下降法 II.–. 学习率 08:59


### 4-5. 特征和多项式回归 07:40


### 4-6. 正规方程（区别于迭代方法的直接解法） 16:19


### 4-7. 正规方程在矩阵不可逆情况下的解决方法 06:00


### 4-8. 导师的编程小技巧 03:34


### 5-1. 基本操作 14:00


### 5-2. 移动数据 16:08


### 5-3. 计算数据 13:16


### 5-4. 数据绘制 09:39


### 5-5. 控制语句：for，while，if. 语句 12:57


### 5-6. 矢量 13:49


### 6-1. 分类 08:09


### 6-2. 假设陈述 07:25


### 6-3. 决策界限 14:50


### 6-4. 代价函数 10:25


### 6-5. 简化代价函数与梯度下降 10:16


### 6-6. 高级优化 14:07


### 6-7. 多元分类：一对多 06:16


### 7-1. 过拟合问题 09:43


### 7-2. 代价函数 10:12


### 7-3. 线性回归的正则化 10:41


### 7-4.Logistic. 回归的正则化 08:35


### 8-1. 非线性假设 09:37


### 8-2. 神经元与大脑 07:48


### 8-3. 模型展示Ⅰ 12:02


### 8-4. 模型展示Ⅱ 11:47


### 8-5. 例子与直觉理解Ⅰ 07:16


### 8-6. 例子与直觉理解Ⅱ 10:21


### 8-7. 多元分类 03:52


### 9-1. 代价函数 06:44


### 9-2. 反向传播算法 12:00


### 9-3. 理解反向传播 12:45


### 9-4. 使用注意：展开参数 07:48


### 9-5. 梯度检测 11:38


### 9-6. 随机初始化 06:52


### 9-7. 组合到一起 13:24


### 9-8. 无人驾驶 06:31


### 10-1. 决定下一步做什么 05:51


### 10-2. 评估假设 07:36


### 10-3. 模型选择和训练、验证、测试集 12:04


### 10-4. 诊断偏差与方差 07:43


### 10-5. 正则化和偏差、方差 11:21


### 10-6. 学习曲线 11:54


### 10-7. 决定接下来做什么 06:51


### 11-1. 确定执行的优先级 09:30


### 11-2. 误差分析 13:13


### 11-3. 不对称性分类的误差评估 11:36


### 11-4. 精确度和召回率的权衡 14:06


### 11-5. 机器学习数据 11:10


### 12-1. 优化目标 14:48


### 12-2. 直观上对大间隔的理解 10:37


### 12-3. 大间隔分类器的数学原理 19:42


### 12-4. 核函数 1 15:45


### 12-5. 核函数 2 15:44


### 12-6. 使用 SVM 21:03


### 13-1. 无监督学习 03:18


### 13-2.K-Means 算法 12:33


### 13-3. 优化目标 07:05


### 13-4. 随机初始化 07:50


### 13-5. 选取聚类数量 08:23


### 14-1. 目标 .I：数据压缩 10:10


### 14-2. 目标 .II：可视化 05:28


### 14-3. 主成分分析问题规划 1 09:06


### 14-4. 主成分分析问题规划 2 15:15


### 14-5. 主成分数量选择 10:31


### 14-6. 压缩重现 03:55


### 14-7. 应用 .PCA. 的建议 12:49


### 15-1. 问题动机 07:39


### 15-2. 高斯分布 10:28


### 15-3. 算法 12:03


### 15-4. 开发和评估异常检测系统 13:08


### 15-5. 异常检测 .VS. 监督学习 07:37


### 15-6. 选择要使用的功能 12:18


### 15-7. 多变量高斯分布 13:47


### 15-8. 使用多变量高斯分布的异常检测 14:04


### 16-1. 问题规划 07:55


### 16-2. 基于内容的推荐算法 14:32


### 16-3. 协同过滤 10:15


### 16-4. 协同过滤算法 08:28


### 16-5. 矢量化：低轶矩阵分解 08:29


### 16-6. 实施细节：均值规范化 08:32


### 17-1. 学习大数据集 05:46


### 17-2. 随机梯度下降 13:20


### 17-3.Mini-Batch. 梯度下降 06:19


### 17-4. 随机梯度下降收敛 11:32


### 17-5. 在线学习 12:51


### 17-6. 减少映射与数据并行 14:09


### 18-1. 问题描述与 .OCR.pipeline 07:03


### 18-2. 滑动窗口 14:41


### 18-3. 获取大量数据和人工数据 16:21


### 18-4. 天花板分析：下一步工作的 .pipeline 13:51


### 19-1. 总结与感谢 04:43


## 李宏毅

* [李宏毅 2020 机器学习 & 深度学习 {% include relref_bili.html %}](https://www.bilibili.com/video/BV1JE411g7XF)
* 课件：<http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html>

P3 08:42



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-10-11-ml-MLofAndrew-Ng.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s?__biz=MzU2NTUwNjQ1Mw==&mid=2247485091&idx=1&sn=8844a2dfafcd35ea45d1bf0146ba8a5a&chksm=fcbbfe59cbcc774f68a18bd11d529422e0048896ffa3a253c52a749fc6e45d7292e1791052da&scene=27#wechat_redirect]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/mp.weixin.qq.com/68945947.html" %})
- [https://www.bilibili.com/video/BV164411b7dx]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/72ebaee9.html" %})
- [https://github.com/TheisTrue/MLofAndrew-Ng]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/github.com/f1eeb779.html" %})
- [https://www.jianshu.com/p/682c88cee5a8]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.jianshu.com/fdc8f898.html" %})
- [https://cs.nyu.edu/~roweis/kica.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/cs.nyu.edu/89374dba.html" %})
- [https://www.bilibili.com/video/BV1JE411g7XF]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/www.bilibili.com/68e17dc9.html" %})
- [http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html]({% include relrefx.html url="/backup/2021-10-11-ml-MLofAndrew-Ng.md/speech.ee.ntu.edu.tw/f319f059.html" %})
