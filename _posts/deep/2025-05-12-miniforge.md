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

[15 分钟彻底搞懂！Anaconda Miniconda conda-forge miniforge Mamba {% include relref_bili.html %}](https://www.bilibili.com/video/BV1Fm4ZzDEeY/)

```
conda install anaconda-clean
anaconda-clean --yes
rm --rf ~/anaconda3
```

以下是一些 Anaconda 的开源替代软件：

1. Miniconda：官网为 <https://docs.conda.io/en/latest/miniconda.html> 。
    优点是体积小，安装速度快，只包含 conda、Python 等基础组件，用户可根据需求灵活安装其他包。
2. Virtualenv：官网为 <https://virtualenv.pypa.io/en/latest/> 。
    优点是轻量级，专注于创建独立的 Python 虚拟环境，不会像 Anaconda 那样安装大量不必要的包，使用简单，能有效隔离不同项目的依赖。
3. Pipenv：官网为 <https://pipenv.pypa.io/en/latest/> 。
    优点是自动管理虚拟环境和依赖文件，将 Pipfile 和 Pipfile.lock 文件结合，能精确锁定包的版本，避免依赖冲突，提供更清晰的依赖管理。
4. Poetry：官网为 <https://python-poetry.org/> 。
    优点是强大的依赖管理功能，能自动解决依赖冲突，支持版本范围约束和语义化版本控制，
    同时具备打包和发布 Python 项目的功能，简化了项目的分发流程。

----


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

- [https://www.bilibili.com/video/BV1Fm4ZzDEeY/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/www.bilibili.com/019ea07b.html" %})
- [https://docs.conda.io/en/latest/miniconda.html]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/docs.conda.io/29df5080.html" %})
- [https://virtualenv.pypa.io/en/latest/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/virtualenv.pypa.io/9fd88051.html" %})
- [https://pipenv.pypa.io/en/latest/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/pipenv.pypa.io/c1f95479.html" %})
- [https://python-poetry.org/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/python-poetry.org/0d104c6c.html" %})
- [https://github.com/conda-forge/miniforge]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/github.com/bf4aed31.html" %})
- [https://conda-forge.org/download]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/conda-forge.org/19fedc62.html" %})
- [https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/]({% include relrefx.html url="/backup/2025-05-12-miniforge.md/mirrors.tuna.tsinghua.edu.cn/87c0cdd8.html" %})
