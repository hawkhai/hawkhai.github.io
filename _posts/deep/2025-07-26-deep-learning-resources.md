---
layout: post
title: "机器学习笔记 -- 机器学习资源（进行中）"
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
cluster: "机器学习的数学基础"
---

[机器学习资源 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Resources)


## 一、特征工程


### （一）特征预处理

- [标准化、归一化、异常特征清洗、不平衡数据 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9093890.html)
- [不平衡数据的处理方法 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/84635540)


### （二）特征表达

- [缺失值、特殊特征 (eg. 时间 )、离散特征、连续特征 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9061549.html)
- [连续特征离散化的好处](http://note.youdao.com/noteshare?id=024fa3dbabf4b5a07eb72c8021e60f62)
- [什么样的模型对缺失值更敏感？ {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88717220)


### （三）特征选择

- [过滤法、包装法、嵌入法 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/9032759.html)
- [Kaggle 中的代码实战](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection)


## 二、算法基础


### （一）评价指标

- [PR 曲线和 F1 & ROC 曲线和 AUC](http://note.youdao.com/noteshare?id=13d31b4a7dc317b3d4abd18bf42a74df)
- [AUC & GAUC {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/84350940)


### （二）正则项

- [正则化与数据先验分布的关系](http://note.youdao.com/noteshare?id=2851b97199bcdc174001d72b1bec0372)
- [L1 在 0 点处不可导怎么办？ {% include relref_cnblogs.html %}](http://www.cnblogs.com/pinard/p/6018889.html) 可采用坐标轴下降、最小角回归法
- [L1 为什么比 L2 的解更稀疏 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/74874291)


### （三）损失函数

- [常见损失函数 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/58883095)
- [常见损失函数 2 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/77686118)


### （四）模型训练

- [经验误差与泛化误差、偏差与方差、欠拟合与过拟合、交叉验证](http://note.youdao.com/noteshare?id=b629383adb3b09eb31b754c337f690b5)
- [参数初始化为什么不能全零](https://cloud.tencent.com/developer/article/1535198)
- [深度学习参数初始化 Lecunn、Xavier、He 初始化](https://cloud.tencent.com/developer/article/1542736)
- [dropout]()
- [Batch Normalization](https://cloud.tencent.com/developer/article/1551518)
- [dropout 和 BN 在训练 & 预测时有什么不同 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/61725100)
- [Layer Normalization {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/113233908)
- [Transformer 为什么用 LN 不用 BN（LN 和 BN 两者分别关注什么） {% include relref_zhihu.html %}](https://www.zhihu.com/question/395811291/answer/2141681320)
- [ResNet](https://cloud.tencent.com/developer/article/1591484)


### （五）优化算法

- [梯度下降法、牛顿法和拟牛顿法 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/37524275)
- [深度学习优化算法 SGD、Momentum、Adagrad 等 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/22252270)
- [最大似然估计 和 最大后验估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/61905474)
- [最小二乘法 和 最大似然估计的对比联系 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88716699)
- [最大似然估计 和 EM {% include relref_csdn.html %}](https://blog.csdn.net/zouxy09/article/details/8537620)
- [浅谈最优化问题的 KKT 条件 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/26514613)


### （六）其他知识点

- [先验概率 & 后验概率 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/38567891)
- [MLE 最大似然估计 & MAP 最大后验估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32480810)
- [判别模型 vs 生成模型 {% include relref_zhihu.html %}](https://www.zhihu.com/question/20446337)
- [参数模型 vs 非参数模型 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/26012348)
- [参数估计 最大似然估计与贝叶斯估计 {% include relref_csdn.html %}](https://blog.csdn.net/bitcarmanlee/article/details/52201858)
- [交叉熵 {% include relref_github.html %}](https://colah.github.io/posts/2015-09-Visual-Information/)
- [交叉熵 等价 KL 散度 等价 MLE 最大似然估计 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/346518942)
- [向量间距离度量方式](http://note.youdao.com/noteshare?id=ffba716f9f94f1cf3fac48fca300c198)
- [余弦距离和欧氏距离的转换 {% include relref_zhihu.html %}](https://www.zhihu.com/question/19640394/answer/207795500)


## 三、机器学习算法

1. 线性回归、逻辑回归、SVM
  - [LR 优缺点 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/lr_pros_and_cons.md)
  - [SVM、logistic regression、linear regression 对比 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/compare_svm_lr.md)
  - [KNN vs K-Means {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/31580379)
  - [LR 和最大熵模型的关系, LR 的并行化 {% include relref_csdn.html %}](https://blog.csdn.net/dp_BUPT/article/details/50568392)
  - [为什么 LR 要用对数似然，而不是平方损失？ {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/88717326)
  - [似然函数 {% include relref_wiki.html %}](https://zh.wikipedia.org/wiki/%E4%BC%BC%E7%84%B6%E5%87%BD%E6%95%B0)
2. 树模型
- [逻辑回归与决策树在分类上的区别 {% include relref_csdn.html %}](https://blog.csdn.net/zhang15953709913/article/details/84841988)
- [回归树、提升树、GBDT {% include relref_jianshu.html %}](https://www.jianshu.com/p/005a4e6ac775)
- [GBDT、XGBOOST、LightGBM 讲解（强烈推荐看一下） {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/gbdt_wepon.pdf)
- [XGBOOST 具体例子一步步推导，包括缺失值怎么处理（很细值得看） {% include relref_jianshu.html %}](https://www.jianshu.com/p/ac1c12f3fba1)
    [(-> 这个链接包含前面文章内容，更全的总结 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/92837676)
- [随机森林 GBDT  XGBOOST  LightGBM 比较](http://note.youdao.com/noteshare?id=65790e27fd5737155c31af2c05df8985)
- [树分裂：信息增益、信息增益率、基尼系数 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/245617910)

3. 其他
- [各种机器学习算法的应用场景 {% include relref_zhihu.html %}](https://www.zhihu.com/question/26726794)


## 四、NLP 相关

- word2vec [文章 1 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7160330.html)
    [文章 2 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7243513.html)
    [文章 3 {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/p/7249903.html)
- [LSTM {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/34203833)
- [LSTM 为什么用 tanh {% include relref_zhihu.html %}](https://www.zhihu.com/question/46197687/answer/895834510)
- [fasttext {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32965521)
- [Transformer、self-attention {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/54356280)
- [Transformer 图解 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/338817680)
- [encode-decode attention 和 transformer self-attention 对比 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/53682800)
- [Transformer 中的 positional encoding {% include relref_zhihu.html %}](https://www.zhihu.com/question/347678607/answer/864217252)
- [Bert {% include relref_github.html %}](https://fancyerii.github.io/2019/03/05/bert-prerequisites/) 零基础入门，prerequisites 很全
- [XLNet {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/70257427)
- [nlp 中的词向量对比：word2vec/glove/fastText/elmo/GPT/bert {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/56382372)
- [NLP/AI 面试全记录 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/57153934)


## 五、推荐系统 & 计算广告 相关

- [LR & FTRL {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/55135954)
- [FM 算法 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/37963267): 讲的蛮细的
- [FM 算法结合推荐系统的讲解 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/58160982)
- [DSSM 模型 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/335112207)
- [DSSM 模型的损失函数（顺带讲了 point-wise, list-wise, pair-wise 损失函数） {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/322065156)
- [在线最优化求解 Online Optimization {% include relref_github.html %}](https://github.com/wzhe06/Ad-papers/blob/master/Optimization%20Method/%E5%9C%A8%E7%BA%BF%E6%9C%80%E4%BC%98%E5%8C%96%E6%B1%82%E8%A7%A3%28Online%20Optimization%29-%E5%86%AF%E6%89%AC.pdf)


## 六、推荐书籍 / 笔记 / 代码实现

- [统计学习方法 {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book/blob/master/)
    （注意这个 pdf 是第一版，其中的勘误可在 [这里 / {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book/blob/master/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%EF%BC%88%E5%8B%98%E8%AF%AF%EF%BC%89.pdf)
        查看）
    （[代码实现及 ppt {% include relref_github.html %}](https://github.com/fengdu78/lihang-code)）
- [西瓜书的公式推导细节解析 {% include relref_github.html %}](https://datawhalechina.github.io/pumpkin-book/#/)
- [deeplearning.ai 深度学习课程的中文笔记 {% include relref_github.html %}](https://github.com/fengdu78/deeplearning_ai_books)
- [机器学习训练秘籍 (Andrew NG) {% include relref_github.html %}](https://github.com/AcceptedDoge/machine-learning-yearning-cn)
- [推荐系统实战 {% include relref_github.html %}](https://github.com/wangyuGithub01/E-book)


## 七、推荐专栏

- [刘建平 Pinard {% include relref_cnblogs.html %}](https://www.cnblogs.com/pinard/)：很多高质量文章讲解基础的知识和算法
- [华校专](http://huaxiaozhuan.com/)：基础算法讲解，多而全（其实还没怎么看
- [王喆的机器学习专栏 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/wangzhenotes)：结合论文 + 工业界的推荐系统应用，讲的很清晰
- [荐道馆 {% include relref_zhihu.html %}](https://www.zhihu.com/column/learningdeep)：讲推荐相关，文章写的比较透
- [美团技术团队](https://tech.meituan.com/tags/%E7%AE%97%E6%B3%95.html)：美团的技术博客，新技术与实际应用相结合
- [深度学习前沿笔记 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/c_188941548)：NLP 相关较多，预训练技术讲解的多
- [计算广告小觑 {% include relref_csdn.html %}](https://blog.csdn.net/breada/article/details/50572914)
- [计算广告论文、学习资料、业界分享 {% include relref_github.html %}](https://github.com/wzhe06/Ad-papers)


## 八、面试问题汇总

- [牛客网面经总结](https://www.nowcoder.com/discuss/165930)


## 九、其他面试常考

- [海量数据判重](https://www.nowcoder.com/discuss/153978)
- [常考智力题 / 逻辑题 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/IQ.md)
- [常考概率题 {% include relref_github.html %}](https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/statistic.md)


## 十、C++ 相关

- [STL 详解及常见面试题 {% include relref_csdn.html %}](https://blog.csdn.net/daaikuaichuan/article/details/80717222)


## 工作之后工程实践相关

- [基于 PQ 量化的近似近邻搜索 (ANN) ](http://xtf615.com/2020/08/01/EBR/)
- [ANN 召回算法之 IVFPQ( 跟上面的差不多，这篇图第一张画的 PQ 图更清晰 ) {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/378725270)



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-07-26-deep-learning-resources.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/wangyuGithub01/Machine_Learning_Resources]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/946e7a98.html" %})
- [https://www.cnblogs.com/pinard/p/9093890.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/5af2c785.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/84635540]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/007d73f8.html" %})
- [https://www.cnblogs.com/pinard/p/9061549.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/ad16de54.html" %})
- [http://note.youdao.com/noteshare?id=024fa3dbabf4b5a07eb72c8021e60f62]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/9c8dc335.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88717220]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/282c1223.html" %})
- [https://www.cnblogs.com/pinard/p/9032759.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/494c44f4.html" %})
- [https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.kaggle.com/326d6084.html" %})
- [http://note.youdao.com/noteshare?id=13d31b4a7dc317b3d4abd18bf42a74df]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/e2ab7ebe.html" %})
- [https://zhuanlan.zhihu.com/p/84350940]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/e14f5e21.html" %})
- [http://note.youdao.com/noteshare?id=2851b97199bcdc174001d72b1bec0372]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/9bcf97e9.html" %})
- [http://www.cnblogs.com/pinard/p/6018889.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/d1dfca42.html" %})
- [https://zhuanlan.zhihu.com/p/74874291]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/96a91346.html" %})
- [https://zhuanlan.zhihu.com/p/58883095]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/c2778f3d.html" %})
- [https://zhuanlan.zhihu.com/p/77686118]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/855ab777.html" %})
- [http://note.youdao.com/noteshare?id=b629383adb3b09eb31b754c337f690b5]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/64871d22.html" %})
- [https://cloud.tencent.com/developer/article/1535198]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/cloud.tencent.com/807912d0.html" %})
- [https://cloud.tencent.com/developer/article/1542736]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/cloud.tencent.com/97064906.html" %})
- [https://cloud.tencent.com/developer/article/1551518]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/cloud.tencent.com/9a898506.html" %})
- [https://zhuanlan.zhihu.com/p/61725100]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/ccd57b39.html" %})
- [https://zhuanlan.zhihu.com/p/113233908]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/aab0c19d.html" %})
- [https://www.zhihu.com/question/395811291/answer/2141681320]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/0d3fc98b.html" %})
- [https://cloud.tencent.com/developer/article/1591484]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/cloud.tencent.com/75d75389.html" %})
- [https://zhuanlan.zhihu.com/p/37524275]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/c5eac9d9.html" %})
- [https://zhuanlan.zhihu.com/p/22252270]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/81219569.html" %})
- [https://zhuanlan.zhihu.com/p/61905474]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/06c543ac.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88716699]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/e5f17d32.html" %})
- [https://blog.csdn.net/zouxy09/article/details/8537620]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/22d1d7a9.html" %})
- [https://zhuanlan.zhihu.com/p/26514613]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/032cec84.html" %})
- [https://zhuanlan.zhihu.com/p/38567891]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/aff113a6.html" %})
- [https://zhuanlan.zhihu.com/p/32480810]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/9dc3ded7.html" %})
- [https://www.zhihu.com/question/20446337]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/b1392a63.html" %})
- [https://zhuanlan.zhihu.com/p/26012348]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/00b8d0c8.html" %})
- [https://blog.csdn.net/bitcarmanlee/article/details/52201858]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/ebdda854.html" %})
- [https://colah.github.io/posts/2015-09-Visual-Information/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/colah.github.io/b8f6b360.html" %})
- [https://zhuanlan.zhihu.com/p/346518942]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/7b93b9ec.html" %})
- [http://note.youdao.com/noteshare?id=ffba716f9f94f1cf3fac48fca300c198]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/a96fa0c9.html" %})
- [https://www.zhihu.com/question/19640394/answer/207795500]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/3c4fc27d.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/lr_pros_and_cons.md]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/8eff022e.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/compare_svm_lr.md]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/1921ab50.html" %})
- [https://zhuanlan.zhihu.com/p/31580379]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/5d6b3b4f.html" %})
- [https://blog.csdn.net/dp_BUPT/article/details/50568392]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/69bce3b7.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/88717326]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/7a3609ec.html" %})
- [https://zh.wikipedia.org/wiki/%E4%BC%BC%E7%84%B6%E5%87%BD%E6%95%B0]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zh.wikipedia.org/09feaa14.html" %})
- [https://blog.csdn.net/zhang15953709913/article/details/84841988]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/879134d7.html" %})
- [https://www.jianshu.com/p/005a4e6ac775]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.jianshu.com/512d30d9.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Notes/blob/master/pdf/gbdt_wepon.pdf]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/ea1131e0.pdf" %})
- [https://www.jianshu.com/p/ac1c12f3fba1]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.jianshu.com/56a085fe.html" %})
- [https://zhuanlan.zhihu.com/p/92837676]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/6a16de5f.html" %})
- [http://note.youdao.com/noteshare?id=65790e27fd5737155c31af2c05df8985]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/note.youdao.com/50cd6d63.html" %})
- [https://zhuanlan.zhihu.com/p/245617910]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/13501447.html" %})
- [https://www.zhihu.com/question/26726794]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/b130a46f.html" %})
- [https://www.cnblogs.com/pinard/p/7160330.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/56fc1b1b.html" %})
- [https://www.cnblogs.com/pinard/p/7243513.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/510d37e2.html" %})
- [https://www.cnblogs.com/pinard/p/7249903.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/e450eca8.html" %})
- [https://zhuanlan.zhihu.com/p/34203833]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/1d0fc2ca.html" %})
- [https://www.zhihu.com/question/46197687/answer/895834510]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/f8094be6.html" %})
- [https://zhuanlan.zhihu.com/p/32965521]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/866c5373.html" %})
- [https://zhuanlan.zhihu.com/p/54356280]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/589b2bc2.html" %})
- [https://zhuanlan.zhihu.com/p/338817680]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/f98cb261.html" %})
- [https://zhuanlan.zhihu.com/p/53682800]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/82187b51.html" %})
- [https://www.zhihu.com/question/347678607/answer/864217252]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/4dfaa53b.html" %})
- [https://fancyerii.github.io/2019/03/05/bert-prerequisites/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/fancyerii.github.io/a835e11e.html" %})
- [https://zhuanlan.zhihu.com/p/70257427]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/ab4f5cb3.html" %})
- [https://zhuanlan.zhihu.com/p/56382372]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/4d1b48d3.html" %})
- [https://zhuanlan.zhihu.com/p/57153934]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/aa39b9f0.html" %})
- [https://zhuanlan.zhihu.com/p/55135954]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/f400c7c0.html" %})
- [https://zhuanlan.zhihu.com/p/37963267]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/37be221a.html" %})
- [https://zhuanlan.zhihu.com/p/58160982]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/58a5bc4f.html" %})
- [https://zhuanlan.zhihu.com/p/335112207]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/4e8e2579.html" %})
- [https://zhuanlan.zhihu.com/p/322065156]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/96d35007.html" %})
- [https://github.com/wzhe06/Ad-papers/blob/master/Optimization%20Method/%E5%9C%A8%E7%BA%BF%E6%9C%80%E4%BC%98%E5%8C%96%E6%B1%82%E8%A7%A3%28Online%20Optimization%29-%E5%86%AF%E6%89%AC.pdf]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/617ca1c8.pdf" %})
- [https://github.com/wangyuGithub01/E-book/blob/master/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/7f944c04.html" %})
- [https://github.com/wangyuGithub01/E-book/blob/master/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%EF%BC%88%E5%8B%98%E8%AF%AF%EF%BC%89.pdf]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/6f9531d5.pdf" %})
- [https://github.com/fengdu78/lihang-code]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/505a3b79.html" %})
- [https://datawhalechina.github.io/pumpkin-book/#/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/datawhalechina.github.io/dc925f5a.html" %})
- [https://github.com/fengdu78/deeplearning_ai_books]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/d720115f.html" %})
- [https://github.com/AcceptedDoge/machine-learning-yearning-cn]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/247b2f97.html" %})
- [https://github.com/wangyuGithub01/E-book]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/81f1b0ea.html" %})
- [https://www.cnblogs.com/pinard/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.cnblogs.com/bd9e25d1.html" %})
- [http://huaxiaozhuan.com/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/huaxiaozhuan.com/ae777d42.html" %})
- [https://zhuanlan.zhihu.com/wangzhenotes]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/7fdacec4.html" %})
- [https://www.zhihu.com/column/learningdeep]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.zhihu.com/a6901a31.html" %})
- [https://tech.meituan.com/tags/%E7%AE%97%E6%B3%95.html]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/tech.meituan.com/600f7b5e.html" %})
- [https://zhuanlan.zhihu.com/c_188941548]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/1c7b8420.html" %})
- [https://blog.csdn.net/breada/article/details/50572914]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/20807905.html" %})
- [https://github.com/wzhe06/Ad-papers]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/88963e8c.html" %})
- [https://www.nowcoder.com/discuss/165930]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.nowcoder.com/ce36cdeb.html" %})
- [https://www.nowcoder.com/discuss/153978]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/www.nowcoder.com/aab2fcc1.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/IQ.md]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/771a9208.html" %})
- [https://github.com/wangyuGithub01/Machine_Learning_Resources/blob/master/pdf/statistic.md]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/github.com/58330a7d.html" %})
- [https://blog.csdn.net/daaikuaichuan/article/details/80717222]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/blog.csdn.net/28aa3806.html" %})
- [http://xtf615.com/2020/08/01/EBR/]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/xtf615.com/bfce888c.html" %})
- [https://zhuanlan.zhihu.com/p/378725270]({% include relrefx.html url="/backup/2025-07-26-deep-learning-resources.md/zhuanlan.zhihu.com/2a4deb13.html" %})
