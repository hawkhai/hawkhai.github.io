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

* [Windows 上通过 bat 避免 python 冲突](https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/)
* [Windows 如何：在本机代码中设置线程名称](https://docs.microsoft.com/zh-cn/visualstudio/debugger/how-to-set-a-thread-name-in-native-code?view=vs-2019)
* [使用 windbg 定位句柄泄漏](https://gclxry.com/article/use-windbg-to-locate-handle-leaks/)
* [Windows 内存类型介绍](https://gclxry.com/article/windows-memory-introduction/)

[from {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/109266820)

```
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

```
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
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ uncompyle
uncompyle test.pyc > test.py
```


## 代码加密

<https://pyob.oxyry.com/>
<https://blog.csdn.net/ir0nf1st/article/details/61650984>

[Pyinstaller 加密打包应用的示例代码](https://www.94e.cn/info/74)


### 抓取真实 api 后

```python
def obfuscation(py_file, save_path):
    print("读取文件:", py_file)
    with open(py_file, "r", encoding="utf-8") as f:
        py_content = f.read()

    print("进行混淆中 ...")
    url = "https://pyob.oxyry.com/obfuscate"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Referer": "http://pyob.oxyry.com/",
        "content-type": "application/json",
        "cookie": "_ga=GA1.2.1306886713.1588752647; _gid=GA1.2.46944674.1588899118"
    }
    data = json.dumps({
        "append_source": "false",
        "preserve": "",
        "remove_docstrings": "true",
        "rename_default_parameters": "false",
        "rename_nondefault_parameters": "true",
        "source": py_content
    })
    result = json.loads(requests.post(url, data=data, headers=headers).text)["dest"]
    result = "# cython: language_level=3\n" + result
    print("混淆成功 ...")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(result)
    print("混淆文件已写入 {}\n".format(save_path))

if __name__ == '__main__':
    obfuscation("my.py", "../ 混淆 /my.py")
    obfuscation("approach.py", "../ 混淆 /approach.py")
```

<p><span style="color: #ff0000"><strong>编译 pyd</strong></span></p>
<p>build_pyd.py</p>

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='any words.....',
    ext_modules=cythonize(["my.py","approach.py" ])
)
```


### 执行打包

```python
import json
import os
# 清理旧 pyd 文件
import uuid
import requests

def clearPyd():
    for file in os.listdir():
        if ".pyd" in file:
            print("删除 .pyd:", file)
            os.remove(file)
    print("***********************************************************************")

# 构建 pyd 文件
def buildPyd():
    os.system("python build_pyd.py build_ext --inplace")

# 重命名 pyd 文件
def renamePyd():
    print("***********************************************************************")
    for file in os.listdir():
        if ".pyd" in file:
            print("重新命名 pyd:", file)
            os.rename(file, file[:file.find(".")] + ".pyd")
    for file in os.listdir():
        if ".c" in file:
            print("删除 .c 文件:", file)
            os.remove(file)
    print("***********************************************************************")

# 执行打包
def pyinstaller(key, ico):
    os.system("pyinstaller -F --key {} -i {} main.py".format(key, ico))

# 删除 bulid 和 spec 文件
def clearBuildAndSpec():
    import shutil
    shutil.rmtree('build')
    print("删除 bulid 文件夹")
    os.remove("main.spec")
    print("删除 spec 文件")

if __name__ == '__main__':
    clearPyd() # 清理旧 pyd 文件
    buildPyd() # 构建 pyd 文件
    renamePyd() # 重命名 pyd 文件
    pyinstaller(uuid.uuid4()[0:16], "1.ico") # 执行打包
    clearPyd() # 清理 pyd 文件
    clearBuildAndSpec() # 删除 bulid 和 spec 文件
```

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-03-19-pyinstxtractor.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://gclxry.com/article/avoid-python-conflicts-via-bat-on-windows/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/gclxry.com/43348a06.html" %})
- [https://docs.microsoft.com/zh-cn/visualstudio/debugger/how-to-set-a-thread-name-in-native-code?view=vs-2019]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/docs.microsoft.com/0e272c9c.html" %})
- [https://gclxry.com/article/use-windbg-to-locate-handle-leaks/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/gclxry.com/1fa2a3b5.html" %})
- [https://gclxry.com/article/windows-memory-introduction/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/gclxry.com/8aaf20da.html" %})
- [https://zhuanlan.zhihu.com/p/109266820]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/zhuanlan.zhihu.com/161c2608.html" %})
- [https://github.com/extremecoders-re/pyinstxtractor]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/90c1b6cf.html" %})
- [https://docs.conda.io/en/latest/miniconda.html]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/docs.conda.io/29df5080.html" %})
- [https://github.com/pyenv/pyenv]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/477faba6.html" %})
- [https://pypi.org/project/tinyaes/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/pypi.org/0fc1f0c7.html" %})
- [https://github.com/rocky/python-uncompyle6/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/github.com/1bcbcaee.html" %})
- [http://tools.bugscaner.com/decompyle/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/tools.bugscaner.com/cfa1ae9d.html" %})
- [https://pyob.oxyry.com/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/pyob.oxyry.com/c10ddfd1.html" %})
- [https://blog.csdn.net/ir0nf1st/article/details/61650984]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/blog.csdn.net/b6a1cb65.html" %})
- [https://www.94e.cn/info/74]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/www.94e.cn/8920d488.html" %})
- [https://pyob.oxyry.com/obfuscate]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/pyob.oxyry.com/5ff36f08.html" %})
- [http://pyob.oxyry.com/]({% include relrefx.html url="/backup/2021-03-19-pyinstxtractor.md/pyob.oxyry.com/fa80ee50.html" %})
