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


## Mac M1 上运行 Jenkins

**Docker Desktop 收费！**
首先在 docker 官网上下载好支持 m1 版本的 desktop 客户端，随后打开 jenkins.io 查看安装命令：

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

```

<https://cloud.tencent.com/developer/article/1893274>
{% include image.html url="/assets/images/240530-mac-jenkins/WechatIMG17.jpg" %}

http://localhost:8080
安装好后输入密码注册即可，选择推荐插件，成功图：
9b12c3f8df204c1295512f83b4e89cfc
cat /var/jenkins_home/secrets/initialAdminPassword
podman

随后可以进行一些案例，创建新项目，输入响应的 git 地址，然后加入 jenkinsfile、groovy 语言的流水线式脚本：
```js
// 写流水线的脚本
pipeline {

    // 全部的 CICD 流程都需要在这里定义
    // 任何一个代理可用就可以执行
    agent any
    // 定义一些环境信息

    // 定义流水线的加工流程
    stages {
        // 流水线的所有阶段
        // 1. 编译
        stage('bianyi') {
            steps {
                echo "bianyi..."
            }
        }
        // 2. 测试
        stage('test') {
            steps {
                echo "test..."
            }
        }
        // 3. 打包
        stage('dabao') {
            steps {
                echo "package..."
            }
        }
        // 4. 部署
        stage('build') {
            steps {
                echo "build..."
            }
        }
    }
}
```
随后在 blue ocean 运行即可。


## 直接安装

<https://www.jenkins.io/download/lts/macos/>
Sample commands:
* Install the latest LTS version: brew install jenkins-lts
* Start the Jenkins service: brew services start jenkins-lts
* Restart the Jenkins service: brew services restart jenkins-lts
* Update the Jenkins version: brew upgrade jenkins-lts

To start jenkins-lts now and restart at login:
    `brew services start jenkins-lts`
Or, if you don't want/need a background service you can just run:
    `/opt/homebrew/opt/openjdk/bin/java -Dmail.smtp.starttls.enable\=true -jar /opt/homebrew/opt/jenkins-lts/libexec/jenkins.war --httpListenAddress\=127.0.0.1 --httpPort\=8080`


## 构建脚本

* <https://www.jenkins.io/zh/doc/tutorials/build-a-python-app-with-pyinstaller/>
* <https://www.jianshu.com/p/0f913c735966>

MacOS 访问 Windows 远程桌面（RDP）的方法
* <https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac>
* <https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac>


## 使用 PyInstaller 构建 Python 应用

Blue Ocean 入门
<https://www.jenkins.io/zh/doc/book/blueocean/getting-started/>


## Mac 下如何查看 Git 的全局忽略列表

打开 Finder
在显示器的顶部菜单选择前往->前往文件夹
输入 `~/.gitignore_global`
右键用记事本打开即可

如果不显示，请允许 Mac 显示所有隐藏文件！！
打开终端，输入：
```
defaults write com.apple.finder AppleShowAllFiles -bool true 此命令显示隐藏文件
defaults write com.apple.finder AppleShowAllFiles -bool false 此命令关闭显示隐藏文件
```

命令运行之后需要重新加载 Finder：快捷键 option+command+esc，选中 Finder，重新启动即可
重启电脑也可以。
```
*~
.DS_Store
.idea
```


## Jenkins 利用 Build With Parameters 插件实现选择参数构建

<https://zhuanlan.zhihu.com/p/620236975>

1. 检查工作区，整个 git 干净。check_workspace
2. 修改版本号，并 tag push。change_version
3. 删除目标文件。delete_target
4. 执行构建。run_build
5. 检查目标文件。check_target
6. 提交构建结果。submit_result



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-05-30-mac-Jenkins.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://cloud.tencent.com/developer/article/1893274]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/cloud.tencent.com/0b389d77.html" %})
- [https://www.jenkins.io/download/lts/macos/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/274b49a3.html" %})
- [https://www.jenkins.io/zh/doc/tutorials/build-a-python-app-with-pyinstaller/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/343159ca.html" %})
- [https://www.jianshu.com/p/0f913c735966]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jianshu.com/4c6e55db.html" %})
- [https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/learn.microsoft.com/ee20b775.html" %})
- [https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/install.appcenter.ms/5fa810a4.html" %})
- [https://www.jenkins.io/zh/doc/book/blueocean/getting-started/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/0e4c6ffa.html" %})
- [https://zhuanlan.zhihu.com/p/620236975]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/zhuanlan.zhihu.com/72822cb6.html" %})
