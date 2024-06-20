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

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
/bin/zsh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
zsh: command not found: brew
对于搭载 Intel 芯片的 macOS，添加以下行到您的 .zshrc 文件：
`export PATH="/usr/local/bin:$PATH"`
对于搭载 Apple Silicon 的 macOS，添加以下行到您的 .zshrc 文件：
`export PATH="/opt/homebrew/bin:$PATH"`
对于 Linux，添加以下行到您的 .zshrc 文件：
`export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"`
要编辑 .zshrc 文件，您可以使用任何文本编辑器，例如，在终端中运行 `nano ~/.zshrc` ，添加适当的行，保存更改并退出编辑器。
应用更改： 添加正确的行到您的 .zshrc 文件后，通过运行以下命令来应用更改：
`source ~/.zshrc`
或者简单地关闭并重新打开您的终端。
验证安装： 要验证 Homebrew 是否已安装并且在您的 PATH 中，运行：
`brew --version`
您应该会在终端中看到打印出来的 Homebrew 版本。
如果在执行这些步骤后仍然遇到问题，请确保您的 .zshrc 文件中没有打字错误，并且确保 Homebrew 已经成功安装。
inet 10.12.152.102 netmask 0xfffff800 broadcast 10.12.159.255

<https://www.jenkins.io/download/lts/macos/>
Sample commands:
* Install the latest LTS version: `brew install jenkins-lts`
* Start the Jenkins service: brew services start jenkins-lts
* Restart the Jenkins service: `brew services restart jenkins-lts`
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

/Users/apple/.jenkins/workspace


## Jenkins 从 git 拉取大文件失败的解决方式

Additional Behaviours
高级的克隆行为
克隆和拉取操作的超时时间（分钟）调整为 60。

```sh
#!/bin/bash
# 1. 检查工作区，整个 git 干净。check_workspace

# 克隆时递归初始化所有子模块
git submodule update --init --recursive
```

```sh
#!/bin/bash
# 6. 提交构建结果。submit_result

# 获取脚本自身的完整路径（$0 是脚本的名字或路径）
# 注意：如果脚本是通过相对路径或没有路径的方式执行的，$0 可能只包含脚本名
script_path="$0"

# 如果 $0 没有包含路径，那么尝试使用 readlink（在支持的系统上）
# 注意：readlink 不是所有系统都支持，而且可能需要安装 coreutils 包
if [ ! -h "$script_path" ]; then
    # 如果脚本不是符号链接，则尝试使用 realpath（在支持的系统上）
    if command -v realpath >/dev/null 2>&1; then
        script_path=$(realpath "$script_path")
    else
        # 如果没有 realpath，则假设脚本在 $PWD（当前工作目录）中
        script_path="$PWD/$script_path"
    fi
fi

# 使用 dirname 命令提取目录部分
script_dir=$(dirname "$script_path")
current_dir=$(pwd)
python3 $script_dir/pyscript/submit_result.py

# 检查返回码
code=$?
if [ $code -ne 0 ]; then
    echo "Error: Command failed with exit status $code"
    exit 1  # 退出脚本并返回错误状态
else
    echo "Command succeeded."
fi
```

```python
#encoding=utf8
import re, os, sys

def main():
    return 0

if __name__ == "__main__":
    sys.exit(main())
```


## MacOS 苹果芯片安装 Pillow 报错 Reason: tried: '/opt/homebrew/opt/libxcb/lib/libxcb.1.dylib' (no such file)

```
ERROR: no file at "/usr/local/opt/libxcb/lib/libxcb.1.dylib"
ERROR: no file at "/usr/local/opt/libxcb/lib/libxcb-xfixes.0.dylib"
```
缺少这个包 安装就可以。
```
brew install libxcb
```
brew unlink libxcb && brew link libxcb

brew cleanup
brew uninstall libxcb
brew install libxcb


## mac Jenkins 局域网访问

当配置完 Jenkins，准备测试时，是无法通过地址访问你的页面，本机上也只能使用 localhost 和 127.0.0.1 打开页面。
需要在以下两个文件中，配置 `0.0.0.0` 。

`~/Library/LaunchAgents/homebrew.mxcl.jenkins.plist` 这个貌似不用。
{% include image.html url="/assets/images/240530-mac-jenkins/89077a86b81744a29719d6ca8568de74.png" %}

`/opt/homebrew/Cellar/jenkins-lts/2.303.2/homebrew.mxcl.jenkins-lts.plist`
{% include image.html url="/assets/images/240530-mac-jenkins/4a9c3c9e04ff48c795f7fae7a71eb440.png" %}

这个管用：
`/opt/homebrew/Cellar/jenkins-lts/2.452.1/homebrew.mxcl.jenkins-lts.plist`


## Jenkins 忘记密码，处理办法

`/Users/<username>/.jenkins/users/` 。


### 方式一：重置密码

[渗透笔记 BCrypt 实战两则 {% include relref_jianshu.html %}](https://www.jianshu.com/p/47881baf83aa)
首先，可以在官网中取得源代码 <http://www.mindrot.org/projects/jBCrypt/>
然后通过 Ant 进行编译。编译之后得到 jbcrypt.jar。也可以不需要进行编译，而直接使用源码中的 java 文件（本身仅一个文件）。
下面是官网的一个 Demo。
```java
public class BCryptDemo {

    public static void main(String[] args) {

        // Hash a password for the first time
        String password = "testpassword";
        String hashed = BCrypt.hashpw(password, BCrypt.gensalt());
        System.out.println(hashed);

        // gensalt's log_rounds parameter determines the complexity
        // the work factor is 2**log_rounds, and the default is 10
        String hashed2 = BCrypt.hashpw(password, BCrypt.gensalt(12));

        // Check that an unencrypted password matches one that has
        // previously been hashed
        String candidate = "testpassword";
        //String candidate = "wrongtestpassword";
        if (BCrypt.checkpw(candidate, hashed))
            System.out.println("It matches");
        else
            System.out.println("It does not match");
    }
}
```

修改 JENKINS_HOME/users/usernamedir 目录下的 config.xml  文件
注：usernamedir 就是你忘记密码对应的用户文件夹
如果是 java -jar 方式启动的，HOME 目录位于 /root/.jenkins
修改 config.xml，找到 passwordHash 部分，替换原有的 hash 值
```
123456 的 hash 值
<jenkins.security.seed.UserSeedProperty>
  <seed>16966906148f1cb6</seed>
</jenkins.security.seed.UserSeedProperty>
<hudson.security.HudsonPrivateSecurityRealm_-Details>
  <passwordHash>#jbcrypt:$2a$10$MiIVR0rr/UhQBqT.bBq0QehTiQVqgNpUGyWW2nJObaVAM/2xSQdSq</passwordHash>
</hudson.security.HudsonPrivateSecurityRealm_-Details>
```
重启 Jenkins
/etc/init.d/jenkins restart


### 方式二：取消密码

进入 Jenkins 主目录，备份 config.xml
cp config.xml config.xml.bak
```
修改 config.xml 文件
找到关键词 useSecurity ，把后面的值 true 改为 false 重启 Jenkins /etc/init.d/jenkins restart
```
可以无账号和密码登录 Jenkins


## Jenkins git 克隆代码超时问题解决

在 Jenkins 中，我们可以通过配置延长默认的 10 分钟超时。

1. 打开项目的配置，看到 `源码管理` 的 `Additional Behaviours` ，点击 `新增` 。
2. 从弹出的新增方式中，选择 `高级的克隆行为` 。
3. 从新增的配置框中可以配置 `克隆和拉取操作的超时时间（分钟）` ，
    点击 `?` 可以看到默认超时时间是 10 分钟的说明，保险起见，
    我们可以直接配置个 60 或 120 分钟，保证可以正常克隆完所有代码。
    并勾选 `浅克隆` ，深度为 1。
4. 配置完毕后，点击 `完成` ，然后重新构建项目即可。


## 参数化构建过程

选项参数
CMAKE_OSX_ARCHITECTURES
x86_64
arm64

文本参数
FTP_ARM64_ADDR
FTP_X86_64_ADDR



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-05-30-mac-Jenkins.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://cloud.tencent.com/developer/article/1893274]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/cloud.tencent.com/0b389d77.html" %})
- [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/raw.githubusercontent.com/613cb55a.sh" %})
- [https://www.jenkins.io/download/lts/macos/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/274b49a3.html" %})
- [https://www.jenkins.io/zh/doc/tutorials/build-a-python-app-with-pyinstaller/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/343159ca.html" %})
- [https://www.jianshu.com/p/0f913c735966]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jianshu.com/4c6e55db.html" %})
- [https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/learn.microsoft.com/ee20b775.html" %})
- [https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/install.appcenter.ms/5fa810a4.html" %})
- [https://www.jenkins.io/zh/doc/book/blueocean/getting-started/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jenkins.io/0e4c6ffa.html" %})
- [https://zhuanlan.zhihu.com/p/620236975]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/zhuanlan.zhihu.com/72822cb6.html" %})
- [https://www.jianshu.com/p/47881baf83aa]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.jianshu.com/e5a9591e.html" %})
- [http://www.mindrot.org/projects/jBCrypt/]({% include relrefx.html url="/backup/2024-05-30-mac-Jenkins.md/www.mindrot.org/d3169fb4.html" %})
