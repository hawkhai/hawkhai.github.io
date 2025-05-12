---
layout: post
title: "机器学习 -- Miniforge替代Anaconda"
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

```
conda install anaconda-clean
anaconda-clean --yes
rm --rf ~/anaconda3
```

## 安装Miniforge

参考官网地址:https://github.com/conda-forge/miniforge
官网下载地址:https://conda-forge.org/download

```
bash Miniforge3-MacoSX-arm64.sh
```


## 活 Miniforge 环境

安装完成后，终端会提示你执行以下命令来激活 conda 环境
```
source ~/.bashrc # 或者 ~/.zshrc1
```

至此安装完毕，可输入conda或mamba命令验证是否安装成功
```
conda --version
mamba --version
```

## Anaconda环境迁移

```
#拷贝Anaconda envs到Miniforge envs
# 完全兼容 mamba env list mamba activate ENV NAME
cp anaconda3/envs/* miniforge3/envs/
