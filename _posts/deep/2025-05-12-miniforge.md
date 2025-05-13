---
layout: post
title: "机器学习 -- Miniforge 替代 Anaconda"
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


## 安装 Miniforge

参考官网地址：<https://github.com/conda-forge/miniforge>
官网下载地址：<https://conda-forge.org/download>

```
bash Miniforge3-MacoSX-arm64.sh
```

清华源的 forge 镜像
<https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/>


## 活 Miniforge 环境

安装完成后，终端会提示你执行以下命令来激活 conda 环境
```
source ~/.bashrc # 或者 ~/.zshrc1
```

至此安装完毕，可输入 conda 或 mamba 命令验证是否安装成功
```
conda --version
mamba --version
```


## Anaconda 环境迁移

```
# 拷贝 Anaconda envs 到 Miniforge envs
# 完全兼容 mamba env list mamba activate ENV NAME
cp anaconda3/envs/* miniforge3/envs/
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-05-12-miniforge.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/conda-forge/miniforge]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/github.com/bf4aed31.html" %})
- [https://conda-forge.org/download]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/conda-forge.org/19fedc62.html" %})
- [https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/mirrors.tuna.tsinghua.edu.cn/87c0cdd8.html" %})
