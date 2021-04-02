---
layout: post
title: "开发环境 -- 使用 TortoiseGit，设置 ssh 方式连接 git 仓库"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "TortoiseGit"]
toc:
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

开始设置之前的准备：建立项目文件夹，初始化 git 仓库（右键 git init），右键打开 git bash，git pull “仓库地址”，把网站上的仓库代码拉取下来。

首先确保安装了最新的 TortoiseGit，老版本不能 AutoLoad Putty Key，存在 bug。

TortoiseGit 使用扩展名为 ppk 的密钥，而不是 ssh\-keygen 生成的 rsa 密钥。也就是说使用 ssh\-keygen \-t rsa \-C "username@email\.com" 产生的密钥，TortoiseGit 中不能用。

而基于 github 的开发必须要用到 rsa 密钥，因此需要用到 TortoiseGit 的 putty key generator 工具，来生成既适用于 github 的 rsa 密钥也适用于 TortoiseGit 的 ppk 密钥。

PuTTYGen 和 Pageant 都在开始菜单中的 TortoiseGit 文件夹下，可以找到。

以下是生成 ppk 密钥，并且在 TortoiseGit 中设置的步骤：

#### 1. 开始程序菜单中，打开 TortoiseGit，点击 PuTTYgen，在打开的窗口中点击 Generate 按钮，会出现绿色进度条，生成过程中可以多晃晃鼠标增加随机性。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/1-1.png"
url2="/assets/images/200822-tortoise-git-ssh/1-2.png" %}

#### 2. 生成之后复制生成的全部内容，窗口先留着不关闭。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/2-1.png" %}

#### 3. 在代码管理网站，如 github、码云。这里拿码云为例。布局都差不多。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/3-1.png"
url2="/assets/images/200822-tortoise-git-ssh/3-2.png" %}

点击右上角，修改资料 —— 点击左侧的 ssh 公钥 —— 填写右侧的添加公钥 —— 标题自拟，把第二步复制的代码粘贴到下面的公钥那里 —— 点击确定。

#### 4. 返回到第二步的窗口，点击 **<font color="red">Save private key</font>** 按钮保存为适用于 TortoiseGit 的私钥，扩展名为 \.ppk。

#### 5. 运行 TortoiseGit 开始菜单中的 Pageant 程序，程序启动后将自动停靠在任务栏中，双击该图标，弹出 key 管理列表。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/5-1.png"
url2="/assets/images/200822-tortoise-git-ssh/5-2.png" %}

#### 6. 在弹出的 key 管理列表中，点击 add key，将第 4 步中保存的私钥（\.ppk）文件加进来，关闭对话框即可。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/6-1.png" %}

#### 7. 回到项目目录下，右键 —— TortoiseGit —— Settings —— 点击 Remote，将第 4 步中保存的私钥（\.ppk）文件加进来。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/7-1.png" %}

注意 URL 后面填的是 git 仓库的 ssh 地址。

#### 8. 完成后，右键可以直接 pull 和 push 操作了。

-----------------

补充：

如果一开始是用 git 命令（ssh\-keygen \-t rsa \-C 【邮箱】），生成的公钥和密钥（比如 id\_rsa 和 id\_rsa\.pub）。首先，把生成的公钥粘贴到 git 远程仓库管理中心。接下来用 ssh 的方式连接远程仓库。

有两种操作方式：

#### 1. 用 git 命令

可以直接用命令“git pull【仓库的 ssh 地址】【分支名称】”这样拉取和推送。

#### 2. 用 TortoiseGit 方式

需要将私钥转成 \.ppk 格式：

- 运行 PuTTYgen，在 Conversions 菜单中点击 Import key，选择一开始生成的私钥文件，比如 id\_rsa 文件。

- 点击 Save private key 按钮，将其保存为 \.ppk 文件。

- 打开 Pageant，点击 Add Key，选择前一步所保存的 \.ppk 文件所在的位置即可。

from [使用 TortoiseGit，设置 ssh 方式连接 git 仓库。 {% include relref_cnblogs.html %}](https://www.cnblogs.com/zy20160429/p/7493693.html)<br/>
markdown [https://www.runoob.com/markdown/md-lists.html](https://www.runoob.com/markdown/md-lists.html)

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relrefx.html url="/assets/reviewjs/blogs/2020-08-22-tortoise-git-ssh.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/zy20160429/p/7493693.html]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.cnblogs.com/4fa376fa.html" %})
- [https://www.runoob.com/markdown/md-lists.html]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.runoob.com/ce4c95d5.html" %})
