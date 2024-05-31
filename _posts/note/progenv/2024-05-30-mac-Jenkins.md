---
layout: post
title: "开发环境 -- 搭建 MacOS Jenkins 环境"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "Jenkins"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

MacOS 搭建 Jenkins 环境。
```
brew upgrade cmake
```

## Error: Failed to install Homebrew Portable Ruby (and your system version is too old)!

```
rm -rf /Users/apple/Library/Caches/Homebrew/portable-ruby-3.1.4.arm64_big_sur.bottle.tar.gz
```


## mac m1上运行jenkins

首先在docker官网上下载好支持m1版本的desktop客户端，随后打开jenkins.io查看安装命令:


```
docker run \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean

podman run \
  -u root \
  --rm \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean

```

https://cloud.tencent.com/developer/article/1893274
{% include image.html url="/images/WechatIMG17.jpg" %}

http://localhost:8080
安装好后输入密码注册即可，选择推荐插件，成功图：
9b12c3f8df204c1295512f83b4e89cfc
cat /var/jenkins_home/secrets/initialAdminPassword
podman


