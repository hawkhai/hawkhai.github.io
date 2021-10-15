---
layout: page
title: 关于
author:
location:
categories: ["BLOG"]
tags: ["BLOG"]
toc:
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
permalink: /about/
---

{% include image.html url="/images/photo.jpg" caption="" width="300px" max_width="300px" align="right" %}

Hi, my name is hawkhai and welcome to my blog.

This is my personal web site.
I started to convert my notes into the web pages since mid 2020.
These are mostly fundamental information or tutorials to share with others.
I hope you find what you are looking for here.
And, I welcome any feedback on the contents and your suggestions.

[^_^]: <http://www.songho.ca/>

以前笔记都记录在 Evernote 里面，搞了多年，发现越来越多、越来越乱，没法玩了。
搞成 blog，并按照一定的结构整理存档，更利于查阅和迭代。
接下来几年会逐步把一些笔记整理成 blog。


## 为什么要写博客（Why write blog）

工作多年后，发现什么都没留下，一直忙于赶路，很多东西搞过，然后都忘记了。
稍微放慢一点，写写博客，用途多：

1. 文档是代码的一部分，是同步更新的，代码改了，文档也要同步得到更新。
2. 写文档和写单元测试类似，可以帮助我们写出逻辑更清晰，设计更合理的代码。
3. 写作即思考，把学习的知识按自己的结构整理记录，方便日后查阅，还方便与他人交流。
4. 短期看，写文档是浪费时间的；长期看，是节约时间的；更长期看，没有文档的代码甚至价值都不大，因为去理解它，重新用起来，需要的成本太大了。
5. 能用图的就用图，不能用图就用表，不能用表，就用文字描述，读者就是未来完全忘光了的自己。

基于文档的知识迭代，比基于脑壳的迭代，更稳固、更可靠。正所谓：好记性不如烂笔头。

1. **工程配置及编译会遇到的问题 --- 想跑起来，成本不用那么大；**
    * 眼见为实，拿到就能运行，看看效果先，建立直观感受。
2. **关键的东西需要写清楚用法 --- 如果别人要用，不用去理解实现细节；**
    * 拿到就能用，直接投入生产，我才不关心你怎么实现的。
3. **边做边写文档，描述自己做的东西 --- 如果别人要改，成本能低一些。**
    * 都是程序员，看也看不懂，改也改不动，避免互相伤害。

以前也做笔记，但是后来发现很多网址打不开了，你说找谁说理去？
这个博客系统加入了自动外链快照功能，博文里面包含的网址，会自动爬取快照存档。

> You do not need to leave your room. Remain sitting at your table and listen.
> Do not even listen, simply wait, be quiet still and solitary.
> The world will freely offer itself to you to be unmasked,
> it has no choice, it will roll in ecstasy at your feet.
> --- Franz Kafka


## 关于代码

首先，调试很重要。
大部分人的工作都是建立在现有代码的基础上的，那么怎么快速把握现有代码是重中之重。
在调试的实操中，可以有效帮助快速读懂代码，理清楚程序的主要脉络。*[豪哥]*

程序的复杂度分两种：

1. 这个逻辑本身就非常复杂，比如 3D 引擎、Chrome、机器学习；
2. 代码混乱和冗余造成的复杂，呵呵，比如公司维护了十多年的代码。

大部分时候，考验的是我们的基本功和知识储备，同时用工整的代码去对抗复杂。

客户端应用研发，大部分都是界面、回调、事件、线程之类，写来写去就那些东西。
深入一些的，也是一些算法啊什么的，开源的改吧改吧就能跑，更多的是考验快速学习能力。

想变成高手，高手也分两种：

1. 知识储备。不是这个东西多复杂，而是在这个领域做了很多年。
2. 学习能力。不断学习，触类旁通，学习能力也会得到不断强化。

高手一般都是平台培养的，和其做过的项目有关，高手无法凭空产生。
编程知识非常庞杂，我们的时间精力有限，只能说挑选一个特定领域深耕，并时刻保持旺盛的学习能力。


## Work history

* Software Engineer
  * Android
  * Windows
  * iOS
  * Linux
* And many others (mostly C/C++)...
  * Python
  * PHP
  * C/C++
  * Java
  * JavaScript


## Spoken languages

* English??
* 简体中文


## Others

Hey, there!
Welcome to my blog.
I hope you enjoy reading the stuff in here.
Nothing fancy, really.
Just bits and bobs about tech and random topics.
Enjoy!


## Contact

<div>
{% if site.email_address %}
<a href="mailto: {{ site.email_address }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-envelope fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}

{% if site.twitter_username %}
<a href="https://twitter.com/{{ site.twitter_username }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}

{% if site.github_username %}
<a href="https://github.com/{{ site.github_username }}">
    <span class="fa-stack fa-lg">
        <i class="fa fa-circle fa-stack-2x"></i>
        <i class="fa fa-github fa-stack-1x fa-inverse"></i>
    </span>
</a>
{% endif %}
</div>


## PGP public key

{% highlight shell %}

{% endhighlight %}



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/about.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [http://www.songho.ca/]({% include relrefx.html url="/backup/about.md/www.songho.ca/d3f4e364.html" %})
- [https://twitter.com/]({% include relrefx.html url="/backup/about.md/twitter.com/4fd9c9a2.html" %})
- [https://github.com/]({% include relrefx.html url="/backup/about.md/github.com/008ec445.html" %})
