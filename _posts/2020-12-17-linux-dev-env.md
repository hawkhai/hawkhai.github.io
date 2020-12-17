---
layout: post
title: "开发环境 -- Linux 环境设置 & 各种环境"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "Linux"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## CentOS7 升级 cmake

[Centos 安装最新版本 cmake](https://cloud.tencent.com/developer/article/1668873)

```shell
# from https://cloud.tencent.com/developer/article/1668873
wget -c https://github.com/Kitware/CMake/releases/download/v3.17.0-rc3/cmake-3.17.0-rc3.tar.gz
tar zxvf cmake-3.17.0-rc3.tar.gz
cd cmake-3.17.0-rc3
./bootstrap
gmake
gmake install
```


### 如果找不到 libssl

```
centos 运行 sudo yum install openssl-devel
ubuntu 运行 sudo apt-get install libssl-dev
```


### `GLIBCXX_3.4.20' not found

[version `GLIBCXX_3.4.21' not found 解决办法 {% include relref_csdn.html %}](https://blog.csdn.net/rznice/article/details/51090966)

```
/home/leo/Desktop/kSource/cmake-3.17.0-rc3/Bootstrap.cmk/cmake: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found
/home/leo/Desktop/kSource/cmake-3.17.0-rc3/Bootstrap.cmk/cmake: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found

/usr/local/lib64/libstdc++.so.6  GLIBCXX_3.4.20
/usr/local/lib64/libstdc++.so.6  GLIBCXX_3.4.21
```

```shell
cp /usr/local/lib64/libstdc++.so.6.0.21 /usr/lib64/
cd /usr/lib64/
sudo cp libstdc++.so.6 libstdc++.so.6.bak2 # 备份一个，以防不测。
rm -f libstdc++.so.6
ln -s libstdc++.so.6.0.21 libstdc++.so.6
```

-----

<font class='ref_snapshot'>参考资料快照</font>

- [1] [https://cloud.tencent.com/developer/article/1668873]({% include relref.html url="/backup/2020-12-17-linux-dev-env.md/cloud.tencent.com/68a27e33.html" %})
- [2] [https://blog.csdn.net/rznice/article/details/51090966]({% include relref.html url="/backup/2020-12-17-linux-dev-env.md/blog.csdn.net/6d068a72.html" %})
