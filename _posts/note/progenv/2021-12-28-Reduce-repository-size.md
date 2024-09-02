---
layout: post
title: "开发环境 -- 缩减 git 仓库大小 Reduce Git repository size"
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


## 背景

随着时间的流逝，Git 存储库变得越来越大，将大文件添加到 Git 存储库后：
* 由于每个人都必须下载文件，因此获取存储库的速度变慢。
* 它们占用服务器上的大量存储空间。
* 可以达到 Git 仓库的存储限制。


## git 清理大文件

[检索大文件 {% include relref_csdn.html %}](https://blog.csdn.net/HappyRocking/article/details/89313501)

得依赖 BFG，工具地址：<https://rtyley.github.io/bfg-repo-cleaner/>

使用方法：
```bash
git clone --mirror git@gitlab.liebaopay.com:pc_duba/kpdf/pdfreader.git
java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 10M pdfreader.git
cd pdfreader.git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git remote set-url --push origin git@gitlab.liebaopay.com:pc_duba/kpdf/pdfreader2.git
git remote set-url origin git@gitlab.liebaopay.com:pc_duba/kpdf/pdfreader2.git
git push
```

遇到的两个问题：
1. 新仓库一定要为空，没有任何提交记录，否则提示权限不足。
2. bfg 还是很好的，貌似不会清除最新的那些文件，只会清理没用到的又在总库里面的文件。

git-filter-branch - Rewrite branches

git remote add upstream git@gitlab.liebaopay.com:pc_duba/kpdf/pdfreader-for-mac.git
git fetch upstream
git checkout --track upstream/pdfreader_cross-platform
这样就不用换仓库了，改一个新的 remote


## git 迁移仓库地址（保留分支和历史提交）

7,217 Commits / 114 Branches / 4 Tags / 7.1 GB Files

```
git@gitlab.example.com:pcapp/kpdf/pdfreader.git
https://gitlab.example.com/pcapp/kpdf/pdfreader.git

git@gitlab.example.com:yqh/pdfreader.git
https://gitlab.example.com/yqh/pdfreader.git
```

最近迁移 git 项目地址，想保留原有分支和提交。
1. 先克隆老项目的镜像
    * 命令：`git clone --mirror old.git （old.git 为老项目的 git 地址）`
    * 实例：`git clone --mirror git@gitlab.example.com:pcapp/kpdf/pdfreader.git`
2. 进入老项目的目录
    * 命令：`cd old.git`
    * 实例：`cd pdfreader.git`
3. 移除老项目的地址替换成新项目
    * 命令：`git remote set-url --push origin new.git （new.git 为新项目的 git 地址）`
    * 实例：`git remote set-url --push origin git@gitlab.example.com:yqh/pdfreader.git`
4. 将镜像推到远程
    * 命令：`git push --mirror // 这一步需要输入新的 git 的账号和密码`
    * 实例：`git push --mirror`

* filter-branch 是让 git 重写每一个分支。
* git filter-repo --strip-blobs-bigger-than 10M
* git push origin --all --force
* git filter-branch --index-filter 'git rm --cached --ignore-unmatch big_file1' HEAD~8..HEAD
* git filter-branch -f --index-filter 'git rm --cached --ignore-unmatch big_file2' HEAD~8..HEAD
* git filter-branch --force --prune-empty --index-filter 'git rm -rf --cached --ignore-unmatch XXX.framework' --tag-name-filter cat -- --all
* git push --force --all


## Refs

* <https://www.bookstack.cn/read/gitlab-doc-zh/docs-161.md>
* <https://docs.gitlab.com/ee/user/project/repository/reducing_the_repo_size_using_git.html>



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-12-28-Reduce-repository-size.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://blog.csdn.net/HappyRocking/article/details/89313501]({% include relrefx.html url="/backup/2021-12-28-Reduce-repository-size.md/blog.csdn.net/8bac9342.html" %})
- [https://rtyley.github.io/bfg-repo-cleaner/]({% include relrefx.html url="/backup/2021-12-28-Reduce-repository-size.md/rtyley.github.io/6af691d0.html" %})
- [https://www.bookstack.cn/read/gitlab-doc-zh/docs-161.md]({% include relrefx.html url="/backup/2021-12-28-Reduce-repository-size.md/www.bookstack.cn/47571ff3.html" %})
- [https://docs.gitlab.com/ee/user/project/repository/reducing_the_repo_size_using_git.html]({% include relrefx.html url="/backup/2021-12-28-Reduce-repository-size.md/docs.gitlab.com/36a2d832.html" %})
