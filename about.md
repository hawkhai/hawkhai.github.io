---
layout: post
title: 关于
author:
location:
categories: ["BLOG"]
tags: ["BLOG"]
toc: true
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

人生从来不晚，从头开始，走自己的路，靠自己：学习、带娃、锻炼身体。
“健康饮食、情绪稳定、适当运动、规律作息”
日拱一卒，虽远必至！Life is never too late to begin...
我们一方面要清醒地认识到目前的困难形势；另一方面，不管做什么，都要满怀热情。这种积极性，才是克服困难、拓宽前路、获得成功的唯一途径。
一些理论上的“不可能”，经过反复探索和实践，最后成了“可能”，自然，这需要投入更多的热情，遭遇更多的失败，抱有更坚定的信念。

少吃外卖、自己做饭；锻炼身体、降低欲望；反人性的思考，过随遇而安的生活；坚持做难的事，对结果顺其自然；对自己好，不要在意别人的看法。

绝大部分人都在谋生，而不是工作。谋生，这个事情今天做一遍，明天做一遍，一样的事情，一年做 365 遍，一年就过去了，重复十年，就老了。
每一天都比前一天多学东西，多有长进，多有收益，多有积累，每天都向上一个台阶，这才是工作。

This is my personal web site.
I started to convert my notes into the web pages since mid 2020.
These are mostly fundamental information or tutorials to share with others.
I hope you find what you are looking for here.
And, I welcome any feedback on the contents and your suggestions.

[^_^]: <http://www.songho.ca/>

以前笔记都记录在 Evernote 里面，搞了多年，发现越来越多、越来越乱，没法玩了。
搞成 blog，并按照一定的结构整理存档，更利于查阅和迭代。
接下来几年会逐步把一些笔记整理成 blog。路虽远行则将至。


## 为什么要写博客（Why write blog）

学习是一件非常困难的事情。首先是工作本身已经很累了，然后是一些客观的家里的事情会消耗你的时间，再然后是新知识本身的难度，面对一堆看不懂的公式，再掂量一下自己有限的智商，不学习貌似日子还是可以继续过下去，那我为什么还要学习呢？夜深人静的时候，媳妇已经睡下，想到自己人生将半，学习计划还是得坚持下去：夜来欹枕细思量，独卧残灯漏夜长；**名不显时心不朽，再挑灯火夜读书。**

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
这个博客系统加入了自动外链快照功能，博文里面包含的网址，会自动爬取快照存档，方便溯源。

> You do not need to leave your room. Remain sitting at your table and listen.
> Do not even listen, simply wait, be quiet still and solitary.
> The world will freely offer itself to you to be unmasked,
> it has no choice, it will roll in ecstasy at your feet.
> --- Franz Kafka

1. 知识内化：记笔记的过程是一个归纳整理、再理解、再吸收的过程，可以加深我们对知识的理解。
2. 形成知识体系：零散的知识很容易被遗忘，而形成知识体系之后，知识之间就能有更强的连接。
3. 方便回顾：笔记就像我们的硬盘，当缓存失效后，我们依然可以通过硬盘调回，保证知识不丢失。

> “处乱世而不惊，临虚空而不惧，喜迎阴晴圆缺，笑傲雨雪风霜”。


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


## The Annotated Turing

[Turing 机、人工智能以及我们的世界](http://www.matrix67.com/blog/archives/4930)

自由意志的问题，这是史上最大的谜团，并不是机械运动所能解释清楚的，理论上讲，给予足够的计算能力，你可以解释任意复杂的系统，为何会做出它现有的表现，纯粹的技巧而已。
惟独无法解释的，是自身的感受，主体和客观世界的鸿沟，举个例子，你可以从头到尾地追踪全身上下的每一条神经通路，精细到每一次离子通道的开闭，把每个 Na+ 和 K+ 都剖析得体无完肤，却唯独无法说明究竟是谁在感知。正如 KK 感触颇深的蜂群，深入到细微之处，我们只是一个个杂乱无章的工蜂，但上升到整体，就有了意识的“觉醒”，能够感知周遭的一切。
最为吊诡的是，如果说干脆否定这个感知主体的存在，它又是你做出这个判断所能依赖的唯一基石：说到底，所有的概念和理论都来源于人对外界的的感觉。

我除了知道自己具有意识之外，我什么也不知道。因为即使去证明，也只能证明我能去证明……


## 人生思考

[对 2030 年中国的一些预测 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/S3D1T6WTvodwwv-4aGASrg)

**宝宝补全我们的人生。**
我们绝大部分人五代后都会没有后代，基因终结。
人类生育率 2.1 是世代更替水平，这需要一半的家庭生三胎，在当前的情况下可以认为是不可能，将来更不可能。
100 个人按照 2.1 的生育率要生 105 个孩子才能保证人口不减少，因为中间会有各种疾病夭折和意外事故。
100 个人里面有 10 个人不结婚或者结婚后不孕不育或者丁克，剩下 90 个人结婚总共 45 对夫妻，有 10 对夫妻生了一胎，有 15 对夫妻生了二胎，那么剩下的 20 对夫妻总共要生 105-10×1-15×2=65 个孩子才能保证人口不减少，也就是平均要生 3.25 个孩子，近似于不可能。工业化国家的人口是不可再生资源，只要生育率低于 2.1，就会持续减少，越低减少速度越快，少了就没有了。

2020 年，中国育龄妇女总和生育率为 1.3，100 个人迭代 1 次是 65 个人，迭代 5 次是 100×(0.65^5)=11.603 个人，迭代 10 次是 1.346 个人，基本上没有了。

人生最大的幸福，莫过于家人健康，宝宝健康，做自己开心的事情。


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
- [http://www.matrix67.com/blog/archives/4930]({% include relrefx.html url="/backup/about.md/www.matrix67.com/84c24598.html" %})
- [https://mp.weixin.qq.com/s/S3D1T6WTvodwwv-4aGASrg]({% include relrefx.html url="/backup/about.md/mp.weixin.qq.com/ee9e9120.html" %})
- [https://twitter.com/]({% include relrefx.html url="/backup/about.md/twitter.com/4fd9c9a2.html" %})
- [https://github.com/]({% include relrefx.html url="/backup/about.md/github.com/008ec445.html" %})
