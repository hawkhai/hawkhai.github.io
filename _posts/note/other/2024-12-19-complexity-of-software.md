---
layout: post
title: "编程与调试 -- 计算机系统的设计原则 Complexity & Technical Debt"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["Python", "编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
l2dwidget: true
---


## 计算机系统的设计原则

[note csdn](https://blog.csdn.net/u012491166/article/details/106571170)

### General

### 设计

复杂的系统由有效的简单系统演变而来（John Gall）
> “A complex system that works is invariably found to have evolved from a simple system that worked. The inverse proposition also appears to be true: A complex system designed from scratch never works and cannot be made to work. You have to start over, beginning with a working simple system.” (John Gall)


Decompose complex problems into smaller sub-problems
* If a problem can be decomposed into two or more independently solvable problems, then solve them independently first!
* After you have implemented and tested the solutions, combine the parts into a larger operation

不要解决不存在的问题。

### 成本

### 任务

### 硬件

### 软件重用

优先使用已被其他人重复使用的现有经过审查的代码。
* 例如 使用STL而不是编写自己的容器。

重用最好在大部分代码中完成–考虑重用整个驱动程序或库，而不是重用功能（Jack Ganssle）。

### 优化

Algorithmic optimizations have a greater impact than micro optimizations.
* “Real efficiency gains come from changing the order of complexity of the algorithm, such as changing from O(N2) to O(NlogN) complexity”

切勿为了获得感知的效率而牺牲清晰度，尤其是在没有数据证明效率提高的情况下。

### 危险信号和危险区

### 中断

### 系统功能点规则

### 进一步阅读

## Complexity & Technical Debt 复杂度和技术负债

[note zhihu](https://zhuanlan.zhihu.com/p/87994255)

技术负债和Gall's Law有什么关系呢？当一个程序或者文件或者公司或者系统，什么都好，因为上面讨论的技术负债的原因变得过于复杂的时候，根据Gall's Law，想要重新从头开始重做基本上就是不可能的了， 只能从简单的开始然后再进化，过程中很有可能又有需要注重短线的情况复杂度会再度提高，简直是个死循环。

### Jeff Bezos Mandate

1. All teams will henceforth expose their data and functionality through service interfaces.
2. Teams must communicate with each other through these interfaces.
3. There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another teams' data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over network.
4. It doesn't matter what technology they use. HTTP, Corba, Pubsub, custom protocols -- doesn't matter. Bezos doesn't care.
5. All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.
6. Anyone who doesn't do this will be fired.
7. Thank you; have a nice day!


Jeff Bezos, 亚马逊的创始人和CEO，在AWS发布的两年前，大概是2002年的时候，给全体员工发了这个邮件，下面是大体的翻译：

1. 从现在开始所有的团队都需要使用服务接口来提供数据和功能。
2. 团队直接必须通过服务接口来交流。
3. 不允许其他形式的进程交流：不能直接连接，不能直接读取其他团队的数据，不能共享内存，不能有任何形式的后门。唯一允许的交流方式就是通过网络调取服务接口。
4. 用什么技术都无所谓，HTTP, Corba, Pubsub, 定制协议都不要紧，Jeff Bezos不管。
5. 没有任何的例外，所有的服务接口从开始就必须以公开化作为设计的原则。这也就是说，所有的团队从计划和设计之初就要让系统可以对外部人员开放。没有例外。
6. 不遵守这些的人会被开除。
7. 谢谢，祝你今天愉快。

### [Technical debt（技术负债 / 技术债） csdn](https://blog.csdn.net/chengyq116/article/details/132218525)

In software development, or any other IT field (e.g., Infrastructure, Networking, etc.) technical debt (also known as design debt or code debt) is the implied cost of future reworking required when choosing an easy but limited solution instead of a better approach that could take more time.

在程序设计及软件工程中，技术负债 / 技术债 / 设计负债 / 代码负债是指开发人员为了加速软件开发，在应该采用最佳方案时进行了妥协，改用了短期内能加速软件开发的方案，从而在未来给自己带来的额外开发负担。这种技术上的选择，虽然眼前看起来可以得到好处，但在未来必须付出额外的时间和精力持续修复之前的妥协所造成的问题及副作用，或是进行重构，把架构改善为最佳实现方式。




