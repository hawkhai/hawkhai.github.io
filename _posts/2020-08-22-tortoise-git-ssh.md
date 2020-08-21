---
layout: post
title: "使用TortoiseGit，设置ssh方式连接git仓库"
location: "珠海"
categories: ["General"]
comments: true
---

开始设置之前的准备：建立项目文件夹，初始化git仓库（右键 git init），右键打开 git bash，git pull “仓库地址”，把网站上的仓库代码拉取下来。

TortoiseGit使用扩展名为ppk的密钥，而不是ssh-keygen生成的rsa密钥。
也就是说使用 ssh-keygen -t rsa -C "username@email.com" 产生的密钥，TortoiseGit中不能用。
而基于github的开发必须要用到rsa密钥，因此需要用到TortoiseGit的putty key generator工具，来生成既适用于github的rsa密钥也适用于TortoiseGit的ppk密钥。

以下是生成ppk密钥，并且在TortoiseGit中设置的步骤：

1. 开始程序菜单中，打开TortoiseGit，点击 PuTTYgen，在打开的窗口中点击Generate按钮，会出现绿色进度条，生成过程中可以多晃晃鼠标增加随机性。

{% include image.html url="../../../../images/sshgit/1-1.png" %}
{% include image.html url="../../../../images/sshgit/1-2.png" %}

2. 生成之后复制生成的全部内容，窗口先留着不关闭。

{% include image.html url="../../../../images/sshgit/2-1.png" %}

3. 在代码管理网站，如github、码云。这里拿码云为例。布局都差不多。

{% include image.html url="../../../../images/sshgit/3-1.png" %}
{% include image.html url="../../../../images/sshgit/3-2.png" %}

点击右上角，修改资料——点击左侧的ssh公钥——填写右侧的添加公钥——标题自拟，把第二步复制的代码粘贴到下面的公钥那里——点击确定。

4. 返回到第二步的窗口，点击 Save private key  按钮保存为适用于TortoiseGit的私钥，扩展名为.ppk。

5. 运行TortoiseGit开始菜单中的Pageant程序，程序启动后将自动停靠在任务栏中，双击该图标，弹出key管理列表。

{% include image.html url="../../../../images/sshgit/5-1.png" %}
{% include image.html url="../../../../images/sshgit/5-2.png" %}

6. 在弹出的key管理列表中，点击add key,将第4步中保存的私钥（.ppk）文件加进来，关闭对话框即可。

{% include image.html url="../../../../images/sshgit/6-1.png" %}

7. 回到项目目录下，右键——TortoiseGit——Settings——点击Remote，将第4步中保存的私钥（.ppk）文件加进来。

{% include image.html url="../../../../images/sshgit/7-1.png" %}

注意URL后面填的是 git仓库的 ssh地址。

8. 完成后，右键可以直接pull和push操作了。

补充：

如果一开始是用git命令（ssh-keygen -t rsa -C [邮箱]），生成的公钥和密钥（比如 id_rsa 和 id_rsa.pub）

首先，把生成的公钥粘贴到 git远程仓库管理中心。接下来用ssh的方式连接远程仓库。

有两种操作方式：

1. 用git命令

可以直接用命令“git pull【仓库的ssh地址】【分支名称】”这样拉取和推送。

2. 用 TortoiseGit 方式

需要将私钥转成.ppk格式：

  - 运行PuTTYgen，在Conversions菜单中点击Import key，选择一开始生成的私钥文件，比如id_rsa文件。

  - 点击Save private key按钮，将其保存为.ppk文件。

  - 打开Pageant，点击Add Key，选择前一步所保存的.ppk文件所在的位置即可。

PuTTYGen和Pageant都在开始菜单中的TortoiseGit文件夹下，可以找到。

from [https://www.cnblogs.com/zy20160429/p/7493693.html](https://www.cnblogs.com/zy20160429/p/7493693.html)<br/>
markdown [https://www.runoob.com/markdown/md-lists.html](https://www.runoob.com/markdown/md-lists.html)