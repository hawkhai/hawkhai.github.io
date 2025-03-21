---
layout: post
title: "开发环境 -- 使用 TortoiseGit，设置 ssh 方式连接 git 仓库"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "TortoiseGit"]
toc: true
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


## PuTTYgen 生成 key

开始程序菜单中，打开 TortoiseGit，点击 PuTTYgen，在打开的窗口中点击 Generate 按钮，会出现绿色进度条，生成过程中可以多晃晃鼠标增加随机性。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/1-1.png"
url2="/assets/images/200822-tortoise-git-ssh/1-2.png" %}


## 复制 pubkey

生成之后复制生成的全部内容，窗口先留着不关闭。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/2-1.png" %}


## 设置 pubkey 到网站

在代码管理网站，如 github、码云。这里拿码云为例。布局都差不多。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/3-1.png"
url2="/assets/images/200822-tortoise-git-ssh/3-2.png" %}

点击右上角，修改资料 —— 点击左侧的 ssh 公钥 —— 填写右侧的添加公钥 —— 标题自拟，把第二步复制的代码粘贴到下面的公钥那里 —— 点击确定。


## 保存 prikey

返回到第二步的窗口，点击 **<font color="red">Save private key</font>** 按钮保存为适用于 TortoiseGit 的私钥，扩展名为 \.ppk。


## 打开 Pageant

运行 TortoiseGit 开始菜单中的 Pageant 程序，程序启动后将自动停靠在任务栏中，双击该图标，弹出 key 管理列表。
（这一步貌似可以省掉？）

{% include image.html url="/assets/images/200822-tortoise-git-ssh/5-1.png"
url2="/assets/images/200822-tortoise-git-ssh/5-2.png" %}


## 设置 prikey

在弹出的 key 管理列表中，点击 add key，将第 4 步中保存的私钥（\.ppk）文件加进来，关闭对话框即可。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/6-1.png" %}


## 设置保存 prikey

回到项目目录下，右键 —— TortoiseGit —— Settings —— 点击 Remote，将第 4 步中保存的私钥（\.ppk）文件加进来。

{% include image.html url="/assets/images/200822-tortoise-git-ssh/7-1.png" %}

注意 URL 后面填的是 git 仓库的 ssh 地址。


## 完成

完成后，右键可以直接 pull 和 push 操作了。


### Github 遇到的两个问题

{% include image.html url="/assets/images/200822-tortoise-git-ssh/20220124233933.png" %}

我的 Win8 当一台电脑存在多个账号的 ppk 的时候，貌似会失败，每次上传下载前，先清空 Pageant Key List 貌似就可以了（这玩意貌似存在 bug）。
{% include image.html url="/assets/images/200822-tortoise-git-ssh/20220128013736.png" caption="失败的情况" %}
{% include image.html url="/assets/images/200822-tortoise-git-ssh/20220128013751.png" caption="每次操作前清空，就可以成功了。" %}

每次下拉的时候，它会自动把对于的 ppk 加入到 Pageant 里面。


### github error

C:\kSource\keys\xx.priv2.ppk

-----------------


## 补充

如果一开始是用 git 命令（ssh\-keygen \-t rsa \-C 【邮箱】），生成的公钥和密钥（比如 id\_rsa 和 id\_rsa\.pub）。首先，把生成的公钥粘贴到 git 远程仓库管理中心。接下来用 ssh 的方式连接远程仓库。

有两种操作方式：


### 用 git 命令

可以直接用命令“git pull【仓库的 ssh 地址】【分支名称】”这样拉取和推送。


### 用 TortoiseGit 方式

需要将私钥转成 \.ppk 格式：

- 运行 PuTTYgen，在 Conversions 菜单中点击 Import key，选择一开始生成的私钥文件，比如 id\_rsa 文件。

- 点击 Save private key 按钮，将其保存为 \.ppk 文件。

- 打开 Pageant，点击 Add Key，选择前一步所保存的 \.ppk 文件所在的位置即可。

from [使用 TortoiseGit，设置 ssh 方式连接 git 仓库。 {% include relref_cnblogs.html %}](https://www.cnblogs.com/zy20160429/p/7493693.html)<br/>
markdown [https://www.runoob.com/markdown/md-lists.html](https://www.runoob.com/markdown/md-lists.html)


## git-ssh 配置和使用

<https://www.wenwl.site/pages/f0c240/>

执行命令后需要连续回车 3 次或 4 次。


## 修复 TortoiseGit 文件夹和文件状态图标不显示问题

[修复 TortoiseGit 文件夹和文件状态图标不显示问题 {% include relref_cnblogs.html %}](https://www.cnblogs.com/xiesong/p/5761352.html)

按 Win+R 键打开运行对话框，输入 regedit ，打开注册表；
找到 HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer；
新建一个“字符串值”名称为 “Max Cached Icons” 值是 “2000”；
重启一下电脑，看图标是否显示。
如果图标还不显示，看下一步。

**修改注册表**

(1) 在弹出的注册表编辑器中找到 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers 这一项。

(2) 找到后可以发现在该项下有很多个，而 Windows Explorer Shell 支持的 Overlay Icon 最多 15 个，Windows 自身使用了 4 个，只剩 11 个可扩展使用。

(3) 编辑 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellIconOverlayIdentifiers，修改 tortoise 相关的名称（如在名称前加一个空格前缀，并加数字）。

[TortoiseSVN/TortoiseGIT 文件和文件夹或图标不显示问题解决方法 {% include relref_csdn.html %}](https://blog.csdn.net/ayang1986/article/details/107381997)
{% include image.html url="/assets/images/200822-tortoise-git-ssh/15c0c5e9843e32b26ebb0d21b966ac7c.png" %}

Windows 10 takes a step away from icon overlays by moving the OneDrive file synchronization status indicator from an icon overlay to a separate Status column.

Since it’s a separate column, there’s room to put more than one status icon there.

{% include image.html url="/assets/images/200822-tortoise-git-ssh/e0a2ee7fa8d7d7e7148917a093169c1d.png" %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2020-08-22-tortoise-git-ssh.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/zy20160429/p/7493693.html]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.cnblogs.com/4fa376fa.html" %})
- [https://www.runoob.com/markdown/md-lists.html]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.runoob.com/ce4c95d5.html" %})
- [https://www.wenwl.site/pages/f0c240/]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.wenwl.site/d8ee3ea4.html" %})
- [https://www.cnblogs.com/xiesong/p/5761352.html]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/www.cnblogs.com/87730d05.html" %})
- [https://blog.csdn.net/ayang1986/article/details/107381997]({% include relrefx.html url="/backup/2020-08-22-tortoise-git-ssh.md/blog.csdn.net/6084dbfb.html" %})
