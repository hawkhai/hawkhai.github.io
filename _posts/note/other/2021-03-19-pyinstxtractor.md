---
layout: post
title: "编程笔记 -- PyInstaller & Extractor"
author:
location: "珠海"
categories: ["编程"]
tags: ["编程"]
toc:
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
l2dwidget: true
---

[from {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/109266820)

```bat
python pyinstxtractor.py xx.exe
uncompyle6

set CL=-FI"Full-Path\stdint.h" (use real value for Full-Path for the environment)
pip install pycrypto
pyinstaller.exe -F --key 123456 xxx.py
```


## PyInstaller Extractor

[PyInstaller Extractor {% include relref_github.html %}](https://github.com/extremecoders-re/pyinstxtractor)


## conda or pyenv

* [Miniconda is a free minimal installer for conda.](https://docs.conda.io/en/latest/miniconda.html)
* [Simple Python version management {% include relref_github.html %}](https://github.com/pyenv/pyenv)
* [tiny-AES-c wrapper in Cython](https://pypi.org/project/tinyaes/)

```shell
$ conda create -n my-py3.6-environment python=3.6
$ conda activate my-py3.6-environment
```

```bat
pipenv install

[[source]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
verify_ssl = true
name = "pypi"

# 把 pyinstaller 安装到开发环境中
pipenv install pyinstaller --dev

# 进入虚拟环境
pipenv shell

import os
import sys
os.chdir(os.path.dirname(__file__))
sys.path.append("..")
import settings

# 直接运行 js 代码
import js2py

context = js2py.EvalJs()
with open("./ids-encrypt.js") as f:
    js_content = f.read()

def encryptAES(data, salt):
    # 执行整段 JS 代码
    context.execute(js_content)
    result = context.encryptAES(data, salt)
    return result
```


## A cross-version Python bytecode decompiler

* [uncompyle6 {% include relref_github.html %}](https://github.com/rocky/python-uncompyle6/)
* [在线 pyc, pyo 反编译 python 反编译](http://tools.bugscaner.com/decompyle/)

```bat
# 通过清华镜像源，下载快
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uncompyle
uncompyle test.pyc > test.py
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-19-pyinstxtractor.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://zhuanlan.zhihu.com/p/109266820]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/zhuanlan.zhihu.com/161c2608.html" %})
- [https://github.com/extremecoders-re/pyinstxtractor]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/90c1b6cf.html" %})
- [https://docs.conda.io/en/latest/miniconda.html]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/docs.conda.io/29df5080.html" %})
- [https://github.com/pyenv/pyenv]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/477faba6.html" %})
- [https://pypi.org/project/tinyaes/]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/pypi.org/0fc1f0c7.html" %})
- [https://github.com/rocky/python-uncompyle6/]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/1bcbcaee.html" %})
- [http://tools.bugscaner.com/decompyle/]({% include relref.html url="/backup/2021-03-19-pyinstxtractor.md/tools.bugscaner.com/cfa1ae9d.html" %})
