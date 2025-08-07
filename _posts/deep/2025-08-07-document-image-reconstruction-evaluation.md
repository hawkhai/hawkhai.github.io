---
layout: post
title: "机器学习笔记 -- 文档恢复质量评估系统 v3.0"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习"]
toc: true
toclistyle:
comments:
visibility: hide
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster:
---

* <https://github.com/AI4Bharat/DocSim> -- 可以用来模拟样本生成。
* <https://github.com/zimeon/docsim>

* LPIPS 这玩意不行，抵抗偏移的能力差。
* CLIP / Chinese-CLIP
* DINOv2
* Donut
* LayoutLMv3


## 🎯 系统概述

这是一个完整的文档恢复质量评估系统，基于 **DINOv2 深度学习特征提取** 和 **智能相似度分析** ，提供科学的文档恢复质量评价标准。系统采用两阶段工作流程： **特征提取阶段** 和 **质量分析阶段** ，支持批量处理和多线程并发。


## 🏗️ 系统架构


### 📋 核心组件

```
doc_restore_eval/
├── 🔧 核心工具
│   ├── image_cutter.py           # DINOv2 特征提取引擎 (18KB)
│   ├── similarity_analyzer.py    # 相似度分析核心 (31KB)
│   ├── layout_export.py          # 版面重建工具 (15KB)
│   └── doc_restore_analyze.py    # 特征文件收集器 (2KB)
├── 🚀 工作流程脚本
│   ├── myfeature_extractor.py    # 第一步：批量特征提取 (5KB)
│   └── myfeature_analyze.py      # 第二步：多图对比分析 (14KB)
├── 📊 分析报告
│   └── weight_comparison_report.py # 权重方案对比工具 (10KB)
└── 📁 输出目录
    ├── histograms/               # 相似度分布直方图
    ├── models/                   # DINOv2 模型缓存
    └── *.json                    # 分析结果文件
```


## 🔄 完整工作流程


### 第一阶段：特征提取 ( `myfeature_extractor.py` )

**功能** ：批量处理图片，提取 DINOv2 深度学习特征

**核心技术** ：
- **智能图片缩放** ：短边≥518px，长边≤2500px
- **动态网格切割** ：518×518 像素块，74 像素步长
- **DINOv2 特征提取** ：支持 4 种模型（vits14/vitb14/vitl14/vitg14）
- **本地模型缓存** ：避免重复下载大型模型
- **CPU/GPU 自适应** ：支持 `--force-cpu` 参数

**输入** ：原始图片文件
**输出** ：patches 目录 + .npy 特征文件

```bash
# 使用示例
python myfeature_extractor.py
# 支持参数：--dinov2-model, --force-cpu, --no-embeddings
```


### 第二阶段：质量分析 ( `myfeature_analyze.py` )

**功能** ：多图片对比分析，生成质量评估报告

**核心算法** ：
- **多线程并发处理** ：最多 8 个线程同时分析
- **空间筛选匹配** ：中心距离≤148 像素的 box 匹配
- **余弦相似度计算** ：基于 768 维 DINOv2 特征向量
- **" 最差优先 "权重算法** ：重点关注最严重的质量问题

**输入** ：多个图片目录（normal/good/bad）
**输出** ：similarity_results.json + 可视化直方图


## ✨ 核心特性


### 🧠 **DINOv2 深度学习特征提取**

- **多模型支持** ：vits14(384×384) / vitb14,vitl14,vitg14(518×518)
- **官方配置兼容** ：完全符合 HuggingFace 官方预处理流程
- **本地模型缓存** ：自动检测 `./models/{model}_pretrain.pth`
- **智能设备选择** ：GPU 优先，支持 CPU 强制模式
- **高质量特征** ：768 维语义向量，捕获文档结构信息


### 🔬 **科学的相似度计算**

- **余弦相似度** ：基于 DINOv2 嵌入向量的语义相似度
- **空间筛选** ：中心距离≤148 像素的精确 box 匹配
- **最大值策略** ：每个 normal box 取与 good/bad 的最大相似度
- **稳健聚合** ：文件级取最小 5% 均值，减少异常值影响


### ⚖️ **" 最差优先 "权重算法**

```
Bottom 1% Mean:    40% （最严重问题，木桶效应）
Bottom 5% Mean:    25% （低端稳健性）
10th Percentile:   20% （中等稳健性）
Median:           15% （整体水平参考）
```

**设计理念** ：
- **木桶效应** ：文档质量由最差部分决定
- **用户体验** ：用户更容易注意到明显错误
- **实用导向** ：避免严重错误比提高平均水平更重要


### 🚀 **高性能并发处理**

- **多线程特征提取** ：ThreadPoolExecutor 并发处理
- **智能任务分配** ：动态负载均衡，最多 8 个工作线程
- **内存优化** ：流式处理大图片，智能缩放控制
- **进度监控** ：实时显示处理进度和完成状态


### 📊 **全面质量评估**

- **分布分析** ：变异系数 (CV)、偏度、峰度统计
- **异常检测** ：IQR 方法识别 outliers
- **可视化输出** ：统一坐标系直方图，便于对比
- **详细报告** ：JSON 格式结果，支持后续分析


### 🎨 **智能版面重建**

- **BFS 同步膨胀** ：最优碰撞停止算法
- **小区域合并** ：消除扫描噪声，提升重建质量
- **可视化对比** ：原始 box + 彩色区域 mask
- **性能优化** ：向量化 alpha 混合，大幅提升速度


## 📁 文件结构

```
doc_restore_eval/
├── similarity_analyzer.py          # 主分析脚本 (v2.0)
├── weight_comparison_report.py     # 权重方案对比工具
├── doc_restore_data.json          # 输入数据
├── similarity_results.json        # 分析结果
├── weight_comparison_report.json  # 权重对比报告
├── histograms/                     # 直方图输出目录
│   ├── file1_similarity_histogram.png
│   └── ...
└── README.md                       # 本文档
```


## 🚀 使用方法


### 基本分析

```bash
python similarity_analyzer.py
```


### 权重方案对比

```bash
python weight_comparison_report.py
```


## 📈 输出说明


### 1. **similarity_results.json**

```json
{
  "overall_statistics": {
    "good_weighted_final_score_mean": 0.814,
    "bad_weighted_final_score_mean": 0.579,
    // ... 更多统计信息
  },
  "file_results": {
    "文件 key": {
      "good_weighted_final_score": 0.853,
      "bad_weighted_final_score": 0.612,
      "good_distribution_quality": {
        "distribution_type": "concentrated",
        "coefficient_of_variation": 0.089,
        "stability_score": 0.911
      },
      // ... 14 种详细统计评分
    }
  }
}
```


### 2. **直方图可视化**

- **紫色粗线** ：平衡最终得分 （主要评价指标）
- **深红虚线** ：Bottom 1% （25% 权重）
- **红色点线** ：Bottom 5% （15% 权重）
- **橙色点线** ：10th Percentile （20% 权重）
- **蓝色点线** ：Median （40% 权重）


### 3. **控制台输出**

```
✅ Core Algorithm: Cosine similarity with 148px center distance filtering
✅ Balanced Weighting: Optimized for better extreme/median balance
✅ Distribution Analysis: Quality assessment with CV and outlier detection

🎯 Recommendation: Use 'Balanced F inal Scores' as primary evaluation metric
📊 For detailed analysis, check distribution quality indicators
```


## 🔧 算法参数

| 参数 | 值 | 说明 |
|------|----|----|
| 距离阈值 | 148 像素 | box 中心距离筛选 |
| 聚合比例 | 5% | 文件级最小值比例 |
| 直方图 bins | 30 | 分布可视化精度 |
| 异常值检测 | IQR×1.5 | 标准异常值识别 |


## 📊 统计指标说明


### **核心评分指标**

1. **Balanced Final Score** ：主要评价指标，平衡权重组合
2. **Bottom 1% Mean** ：极端最差情况评估
3. **Bottom 5% Mean** ：低端稳健性评估
4. **10th Percentile** ：中等稳健性指标
5. **Median** ：整体分布中心


### **辅助分析指标**

- **Q1/Q3/IQR** ：四分位数分析
- **Trimmed Mean** ：截尾均值（去除 10% 极值）
- **MAD** ：中位数绝对偏差
- **Skewness/Kurtosis** ：分布形状特征
- **Entropy** ：信息熵（基于直方图）


### **分布质量指标**

- **Coefficient of Variation** ：变异系数，越小越稳定
- **Distribution Type** ：concentrated/balanced/dispersed
- **Stability Score** ：稳定性评分 (1-CV)
- **Outlier Ratio** ：异常值比例


## 🎯 使用建议


### **主要评价指标**

推荐使用 **Balanced Final Score** 作为主要评价标准：
- 平衡了极端值敏感性和整体稳健性
- 减少了原方案的过度悲观倾向
- 更好地反映文档恢复的整体质量


### **分布质量分析**

结合分布质量指标进行深入分析：
- **CV < 0.1** ：高度集中，质量稳定
- **CV 0.1-0.3** ：平衡分布，质量中等
- **CV > 0.3** ：分散分布，质量不稳定


### **异常样本识别**

关注以下情况：
- Bad 得分 > Good 得分：算法异常，需要调查
- 高异常值比例：数据质量问题
- 极端偏度 / 峰度：分布异常


## 🔄 版本历史


### v2.0（当前版本）

- ✅ 实现平衡权重算法，优化极端值 / 中位数平衡
- ✅ 添加分布质量评估功能
- ✅ 增强直方图可视化，显示权重信息
- ✅ 提供权重方案对比工具
- ✅ 完善错误处理和用户体验


### v1.0（原始版本）

- ✅ 基础相似度计算和统计评分
- ✅ 13 种统计学评分方法
- ✅ 原始权重方案 (1%:40%, 5%:20%, 5th:10%, Median:30%)


## 🤝 贡献指南

如需进一步优化算法：

1. **权重调整** ：修改 `calculate_weighted_final_score()` 函数
2. **新增指标** ：在 `calculate_statistical_scores()` 中添加
3. **可视化改进** ：修改 `plot_similarity_histogram()` 函数
4. **分布分析** ：扩展 `assess_distribution_quality()` 功能


## 📞 技术支持

如遇到问题或需要定制化功能，请检查：
1. 输入数据格式是否正确
2. embedding 文件路径是否存在
3. 依赖包是否完整安装
4. 输出目录权限是否充足

---

**🎉 Doc Restore Similarity Analyzer v2.0 - 为文档恢复质量评估提供科学、稳健的分析工具！**



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-08-07-document-image-reconstruction-evaluation.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/AI4Bharat/DocSim]({% include relrefx.html url="/backup/2025-08-07-document-image-reconstruction-evaluation.md/github.com/3ae2e93f.html" %})
- [https://github.com/zimeon/docsim]({% include relrefx.html url="/backup/2025-08-07-document-image-reconstruction-evaluation.md/github.com/fd27695f.html" %})
