---
layout: post
title: "英语语法零基础完整体系：从句子骨架到复杂句"
author: qhai
location: "珠海"
categories: ["学习"]
tags: ["英语", "语法", "零基础", "学习笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
date: 2026-08-29 00:00:00 +0800
archived:
layoutclear:
---

英语语法并不是一大堆互不相干的规则。它真正研究的只有一件事：**单词怎样组合，才能把“谁、做什么、怎么样、在何时何地、为什么”说清楚。**

这篇文章按零基础学习者最容易理解的顺序，把词类、句子成分、基本句型、时态、语态、非谓语动词和三大从句串成一张完整地图。第一次阅读不必背完，先看懂结构，再回头记细节。

> 本文根据 `wordtap_web/public/shuimu` 中标题或正文含“语法”的 JSON 课程整理。192 份课程 JSON 中有 119 份命中“语法”：入门 50 份、中级 69 份；其中 112 份设有明确的“语法点拨”章节。原课程按课次讲解，本文改为按知识依赖关系重新组织，并补充了术语解释、结构公式、易错辨析和例句分析。

## 一、先建立一张语法地图

一句英语可以从四层来看：

1. **单词（word）**：`student`、`read`、`carefully`。
2. **短语（phrase）**：几个词组成一个整体，但通常没有完整的“主语 + 谓语”，如 `in the room`。
3. **从句（clause）**：内部有自己的“主语 + 谓语”，如 `when he arrived`。
4. **句子（sentence）**：能独立表达完整意思，如 `The class began.`。

看一个逐层扩展的例子：

```text
Birds fly.
鸟飞。

Small birds fly in the sky.
小鸟在天空中飞。

Small birds fly in the sky when spring comes.
春天到来时，小鸟在天空中飞。
```

- `birds`、`fly` 是单词。
- `small birds`、`in the sky` 是短语。
- `when spring comes` 有主语 `spring` 和谓语 `comes`，是从句。
- 整体能独立表达完整意思，是句子。

接下来所有语法，都只是在回答四个问题：

| 层次 | 要解决的问题 | 典型知识 |
| --- | --- | --- |
| 词 | 这个词是什么，能做什么？ | 名词、动词、形容词、副词、代词等 |
| 成分 | 这个词或短语在句中负责什么？ | 主语、谓语、宾语、表语、定语、状语、补语 |
| 句型 | 核心成分怎样搭成完整句子？ | 主谓、主谓宾、主系表等 |
| 复合句 | 怎样把多个“小句子”接起来？ | 名词性从句、定语从句、状语从句 |

### 短语也有“中心词”

短语通常以其中一个词为中心，其他词围绕它补充信息。看中心词，就能判断整个短语大致能做什么。

| 短语类型 | 中心 | 例子 | 常见工作 |
| --- | --- | --- | --- |
| 名词短语 | 名词/代词 | `the tall boy` | 主语、宾语、表语 |
| 动词短语 | 动词 | `has been working` | 谓语 |
| 形容词短语 | 形容词 | `very proud of you` | 定语、表语、补语 |
| 副词短语 | 副词 | `quite slowly` | 状语 |
| 介词短语 | 介词 + 宾语 | `under the table` | 定语、状语、表语等 |

```text
The tall boy has been working very hard in the library.
```

- `the tall boy` 是名词短语，作主语。
- `has been working` 是动词短语，作谓语。
- `very hard` 是副词短语，作方式状语。
- `in the library` 是介词短语，作地点状语。

“短语类型”和“句子成分”仍不是一回事。例如介词短语 `in the library` 可以作地点状语，也可以放在名词后作定语：

```text
The students in the library are quiet.
图书馆里的学生很安静。
```

## 二、词类：单词的“职业”

词类说明一个词通常具有什么性质；句子成分说明它在当前句子里做什么工作。两者不能混为一谈。

例如 `light` 可以有不同职业：

```text
The light is on.       light 是名词：灯
This bag is light.     light 是形容词：轻的
Please light the fire. light 是动词：点燃
```

### 1. 名词：人、事、物或概念的名称

名词（noun，缩写 `n.`）如 `teacher`、`book`、`water`、`happiness`。它最常作主语、宾语或表语。

```text
Tom reads books.
Tom 读书。
```

- `Tom` 是名词，作主语。
- `books` 是名词，作宾语。

### 2. 代词：代替名词

代词（pronoun，`pron.`）如 `I`、`you`、`it`、`this`、`someone`。它能避免重复。

```text
Lucy has a cat. She loves it.
露西有一只猫。她很喜欢它。
```

`She` 代替 Lucy，`it` 代替 a cat。

### 3. 动词：动作或状态

动词（verb，`v.`）如 `run`、`eat`、`know`、`be`。英语句子通常不能没有谓语动词。

```text
They work.       他们工作。
She is happy.    她很开心。
```

### 4. 形容词：说明名词“什么样”

形容词（adjective，`adj.`）常修饰名词，或放在系动词后说明主语。

```text
a quiet room     一个安静的房间
The room is quiet. 这个房间很安静。
```

### 5. 副词：说明动作“怎样、何时、何地、到什么程度”

副词（adverb，`adv.`）常修饰动词、形容词、副词，甚至整个句子。

```text
He runs quickly.       quickly 修饰 runs：跑得快
It is very cold.       very 修饰 cold：非常冷
She speaks really slowly. really 修饰 slowly：确实很慢
Fortunately, we won.  Fortunately 修饰整句：幸运的是
```

### 6. 介词：表示事物之间的关系

介词（preposition，`prep.`）如 `in`、`on`、`at`、`with`、`for`。介词后通常接名词或代词宾格，合起来构成介词短语。

```text
on the table      在桌上
with her          和她一起
for three days    持续三天
```

### 7. 连词：连接词、短语或句子

连词（conjunction，`conj.`）如 `and`、`but`、`because`、`if`。

```text
Tea and coffee are ready.
茶和咖啡准备好了。

I stayed home because it rained.
因为下雨，我待在家里。
```

### 8. 限定词、数词和感叹词

- **限定词**放在名词前限定范围，如 `a`、`the`、`this`、`my`、`some`。
- **数词**表示数量或顺序，如 `three`、`third`。
- **感叹词**表达情绪，如 `Oh!`、`Wow!`。

## 三、句子成分：每一部分在句中干什么

同一个词类能担任不同成分；同一个成分也能由不同结构担任。先记住最关键的七种成分。

### 1. 主语 S：这句话在说“谁或什么”

主语（subject，`S`）通常位于谓语前，是动作的执行者或句子描述的对象。

```text
The boy smiles.
那个男孩微笑。
```

`The boy` 是主语。

主语不一定是“人”，也不一定只含一个词：

```text
Reading every day is useful.
每天阅读很有用。
```

`Reading every day` 整体是主语。

### 2. 谓语 V：主语“做什么”或“处于什么状态”

谓语（predicate verb，常简写为 `V`）是句子的发动机，核心必须是一个有时态和人称变化的动词。

```text
She works.           works 是谓语
She is working.      is working 是完整谓语
She can work.        can work 是完整谓语
```

注意：不要把 `is`、`working` 随意拆开；在后两句中，整组才是谓语。

### 3. 宾语 O：动作影响的“人或物”

宾语（object，`O`）通常放在及物动词或介词后。

```text
I like music.
我喜欢音乐。
```

`music` 是 `like` 的宾语。

```text
She looked at me.
她看着我。
```

`me` 是介词 `at` 的宾语；`at me` 整体不是 `look` 的直接宾语。

### 4. 表语 P：说明主语“是谁、是什么、怎么样”

表语（predicative，`P`）位于系动词后，用来说明主语的身份、性质或状态。

```text
He is a doctor.    a doctor 说明身份
The soup smells good. good 说明状态
```

常见系动词包括：

- 状态：`be`
- 感官：`look`、`sound`、`smell`、`taste`、`feel`
- 变化：`become`、`get`、`turn`、`grow`
- 保持：`keep`、`remain`、`stay`

判断窍门：若动词近似一座等号桥，右边是在说明左边，通常就是“系动词 + 表语”。

```text
The leaves turned yellow.
叶子变黄了。

leaves ≈ yellow
```

### 5. 定语：给名词贴标签，回答“哪一个、什么样的”

定语（attribute）专门修饰名词或代词。

```text
a red apple              red 是前置定语
the book on the desk     on the desk 是后置定语
the girl who is singing  who is singing 是定语从句
```

可以把中心名词想成一个人，定语就是贴在他身上的标签：哪个女孩？——“正在唱歌的”女孩。

### 6. 状语：交代动作或整句话的背景

状语（adverbial）常说明时间、地点、方式、原因、目的、条件、程度等。

```text
He spoke slowly.                  方式：怎样说
We met in the park.               地点：在哪里见
I left because I was tired.       原因：为什么离开
If it rains, we will stay home.   条件：在什么条件下
```

快速区别：**定语主要修饰名词；状语主要修饰动作、性质或整句话。**

### 7. 补语 C：把意思补充完整

补语（complement，`C`）补充说明主语或宾语。初学阶段最重要的是宾语补足语。

```text
They call him Jack.
他们叫他杰克。
```

`him` 是宾语，`Jack` 补充说明 him 是谁，所以是宾语补足语。

```text
The news made me happy.
这个消息让我开心。
```

`happy` 说明宾语 me 变成什么状态，也是宾语补足语。

### 8. 同位语和插入语

**同位语**换一种说法解释前面的名词，两者指同一个人或物。

```text
Mr. Li, our English teacher, is kind.
李老师，也就是我们的英语老师，很友善。
```

`our English teacher` 是 `Mr. Li` 的同位语。

**插入语**表达说话者的态度或补充信息，删掉后主干仍完整。

```text
This plan, I think, will work.
我认为，这个方案会奏效。
```

常见插入语形式：

```text
I think / I believe / you know       简短分句
however / therefore / perhaps        副词
in fact / in my opinion              介词短语
to be honest / to tell the truth     不定式短语
generally speaking                   分词短语
```

```text
To be honest, I don't agree.
老实说，我不同意。

The answer, in my opinion, is wrong.
在我看来，这个答案是错的。
```

插入语通常用逗号、破折号或括号与主干分开，不参与主谓一致。分析长句时可先把它括起来，再找主干。

## 四、五个基本句型：英语句子的骨架

修饰语可以很长，但简单句的核心大多能归入五种句型。

### 1. 主语 + 谓语：S + V

谓语是不及物动词，不需要宾语。

```text
Birds fly.          鸟会飞。
The baby cried.     婴儿哭了。
```

### 2. 主语 + 谓语 + 宾语：S + V + O

谓语是及物动词，后面需要动作对象。

```text
I love music.
我喜欢音乐。
```

### 3. 主语 + 系动词 + 表语：S + V + P

```text
She is patient.
她很有耐心。

The idea sounds great.
这个主意听起来很棒。
```

### 4. 主语 + 谓语 + 间接宾语 + 直接宾语：S + V + IO + DO

间接宾语通常是“给谁”，直接宾语通常是“给什么”。

```text
Dad bought me a bike.
爸爸给我买了一辆自行车。
```

- `me`：间接宾语（人）
- `a bike`：直接宾语（物）

常能改成：

```text
Dad bought a bike for me.
```

### 5. 主语 + 谓语 + 宾语 + 宾补：S + V + O + C

```text
We found the room empty.
我们发现房间是空的。
```

判断宾补的实用方法：在宾语和补语之间加“是”或“变得”，意思若基本成立，通常就是宾补。这里 `the room is empty` 成立。

### 6. 别把地点状语误认成宾语

```text
I go to school every day.
```

主干是 `I go`（S + V）。`to school` 是地点/方向状语，`every day` 是时间状语。`school` 虽然是介词 `to` 的宾语，却不是动词 `go` 的直接宾语。

分析句子时要先找谓语，再问这个动词是否直接接对象。

### 7. There be 存在句：某处“有”某物

`There be` 用来介绍某人或某物存在于某处。这里的 `there` 只是把句子引出来，不等于表示地点的“那里”；`be` 后面的名词才是真正主语。

```text
There is a book on the desk.
桌上有一本书。
```

结构：

```text
There + be + 真正主语 + 地点/时间
```

`be` 要与后面的主语保持一致，并可随时态变化：

```text
There is a problem.                 现在有一个问题。
There are two problems.             现在有两个问题。
There was a meeting yesterday.      昨天有一场会议。
There will be a meeting tomorrow.   明天会有一场会议。
There has been a change.            已经发生了一个变化。
```

有多个并列主语时，日常英语通常按最靠近 `be` 的名词决定单复数：

```text
There is a pen and two books on the desk.
There are two books and a pen on the desk.
```

否定句在 `be` 后加 `not`，疑问句把 `be` 移到 `there` 前：

```text
There isn't any milk.
Is there any milk?
```

比较 `there be` 和 `have`：

```text
There is a library near my home.  我家附近有一座图书馆。（存在）
My school has a library.           我的学校有一座图书馆。（所属）
```

## 五、动词系统：英语语法的核心

### 1. 实义动词、系动词、助动词和情态动词

| 类型 | 作用 | 例子 |
| --- | --- | --- |
| 实义动词 | 表示真实动作或状态 | `eat`、`run`、`know` |
| 系动词 | 连接主语和表语 | `be`、`seem`、`become` |
| 助动词 | 帮助构成时态、否定、疑问、语态 | `be`、`do`、`have` |
| 情态动词 | 表示能力、可能、义务、建议等态度 | `can`、`may`、`must`、`should` |

一个词可因用途不同而扮演不同角色：

```text
I have a car.          have 是实义动词“拥有”
I have finished it.   have 是构成完成时的助动词
```

### 2. 及物动词和不及物动词

- **及物动词**可以直接接宾语：`read a book`。
- **不及物动词**不能直接接宾语：`arrive at the station`，不能说 `arrive the station`。

有些动词两种用法都有：

```text
The door opened.       门开了。（不及物）
She opened the door.   她打开门。（及物）
```

### 3. 动词的五种基本形式

以 `work` 和不规则动词 `write` 为例：

| 名称 | work | write | 常见用途 |
| --- | --- | --- | --- |
| 原形 | work | write | 情态动词后、祈使句、一般现在时部分形式 |
| 第三人称单数 | works | writes | 一般现在时，主语为 he/she/it 等 |
| 过去式 | worked | wrote | 一般过去时 |
| 过去分词 | worked | written | 完成时、被动语态、非谓语 |
| 现在分词/动名词 | working | writing | 进行时、非谓语 |

三个最常用动词的形式必须熟悉：

| 原形 | 现在时 | 过去式 | 过去分词 | -ing 形式 |
| --- | --- | --- | --- | --- |
| be | am/is/are | was/were | been | being |
| do | do/does | did | done | doing |
| have | have/has | had | had | having |

第三人称单数变化：

```text
多数加 -s：work → works
s/x/ch/sh/o 结尾常加 -es：watch → watches, go → goes
辅音字母 + y：study → studies
特殊：have → has
```

`-ing` 变化：

```text
多数直接加 -ing：work → working
不发音 e 结尾通常去 e：write → writing
ie 结尾变 y：lie → lying
重读闭音节末尾常双写辅音：run → running, begin → beginning
```

规则过去式/过去分词变化：

```text
多数加 -ed：work → worked
以 e 结尾加 -d：live → lived
辅音字母 + y：study → studied
重读闭音节末尾常双写辅音：stop → stopped
```

不规则动词没有一条通用公式，要按三栏积累：

```text
go—went—gone
see—saw—seen
take—took—taken
put—put—put
```

### 4. 主谓一致的第一条规则

一般现在时中，主语为第三人称单数时，实义动词通常加 `-s/-es`。

```text
I work here.
He works here.
```

`be` 的变化要单独记：

```text
I am / you are / he is / we are / they are
```

### 5. 什么是限定动词和非限定动词

一个完整分句至少需要一个能表示时态、并在必要时配合主语变化的动词，这叫**限定动词**。它承担谓语核心的工作。

```text
She works here.        works 是限定动词，表示现在时和第三人称单数
She worked here.       worked 是限定动词，表示过去时
```

不定式、动名词和分词本身不承担句子的时态和人称变化，叫**非限定动词**，也就是后文的非谓语动词。

```text
She wants to work here.
```

全句的时态落在 `wants` 上；`to work` 不会因为主语是 she 而变成 `to works`。

### 6. 三个基本助动词 be、do、have

助动词不是多余的小词，它们负责把否定、疑问、时态和语态装到实义动词上。

| 助动词 | 主要工作 | 例子 |
| --- | --- | --- |
| be | 构成进行时和被动语态 | `is reading`、`was built` |
| do | 帮助一般现在/过去时构成否定、疑问和强调 | `doesn't know`、`Did you go?` |
| have | 构成完成体 | `has finished` |

`do` 后一定用动词原形：

```text
She didn't went.  ×
She didn't go.    ✓
```

### 7. 半助动词：长得像短语，用起来像助动词

半助动词由多个词组成，表达时间、可能、义务或习惯等意义。

```text
be going to do    打算/将要做
be about to do    马上要做
be likely to do   很可能做
be able to do     能够做
have to do        不得不做
used to do        过去常常做
had better do     最好做
```

例子：

```text
The train is about to leave.
火车马上要开了。

She used to live here.
她过去住在这里。（现在通常已不住）
```

## 六、时态：时间 + 动作状态

“时态”最好拆成两部分理解：

- **时间**：现在、过去、将来。
- **状态（体）**：一般、进行、完成、完成进行。

传统英语教学把四个时间范围和四种动作状态交叉，得到“16 时态”。现代语法对“将来时”的分析方式有所不同，但下面这张表非常适合初学者建立结构感。

| 时间 \ 状态 | 一般 | 进行 | 完成 | 完成进行 |
| --- | --- | --- | --- | --- |
| 现在 | do/does | am/is/are doing | have/has done | have/has been doing |
| 过去 | did | was/were doing | had done | had been doing |
| 将来 | will do | will be doing | will have done | will have been doing |
| 过去将来 | would do | would be doing | would have done | would have been doing |

先理解四种“状态”：

- **一般**：把动作看成事实、习惯或一个整体。
- **进行**：强调某一时刻动作正在展开。
- **完成**：站在某一时间点回看，动作已经完成或已有结果。
- **完成进行**：站在某一时间点回看，强调动作持续了多久或一直在进行。

实际交流中，各时态的使用频率差别很大。前八种最常用，后面的形式虽然较少见，也应能看懂。

### 1. 一般现在时：习惯、事实、长期状态

结构：

```text
肯定：主语 + 动词原形/第三人称单数
否定：主语 + do/does not + 动词原形
疑问：Do/Does + 主语 + 动词原形 ...?
```

```text
She walks to work every day.
她每天步行上班。

Does she walk to work every day?
她每天步行上班吗？
```

用了 `does` 后，`walks` 必须还原为 `walk`，因为第三人称信息已经由 `does` 承担。

### 2. 现在进行时：此刻或当前阶段正在发生

结构：`am/is/are + doing`

```text
They are having dinner now.
他们现在正在吃晚饭。
```

`know`、`believe`、`belong` 等状态动词通常不用进行时；初学时不要机械地把所有动词都变成 `be doing`。

### 3. 一般过去时：过去发生并结束

结构：

```text
肯定：主语 + 动词过去式
否定：主语 + did not + 动词原形
疑问：Did + 主语 + 动词原形 ...?
```

```text
We visited Beijing last year.
我们去年游览了北京。

Did you visit Beijing last year?
你们去年游览北京了吗？
```

### 4. 过去进行时：过去某一时刻正在发生

结构：`was/were + doing`

```text
I was reading when he called.
他打电话来时，我正在看书。
```

常见搭配：较长的背景动作用过去进行时，插入的短动作用一般过去时。

### 5. 一般将来时：将要发生

常见结构：

```text
will + 动词原形
be going to + 动词原形
```

```text
I will call you tonight.
我今晚会给你打电话。

Look at the clouds. It is going to rain.
看那些云，要下雨了。
```

`will` 常表达临时决定、承诺或预测；`be going to` 常表达已有计划或有迹象的预测。实际语境中二者会有重叠。

### 6. 现在完成时：过去与现在有联系

结构：`have/has + 过去分词`

常见意义：

- 已完成，结果影响现在：`I have lost my key.`（我把钥匙丢了，现在没有钥匙。）
- 从过去持续到现在：`She has lived here for five years.`（她在这里住五年了。）
- 截至现在的经历：`Have you ever seen snow?`（你见过雪吗？）

`for + 时间段`，`since + 起点`：

```text
for three years
since 2023
since I came here
```

一般过去时只报告过去；现在完成时强调与现在的联系：

```text
I lost my key yesterday.  昨天丢的，说明过去事件
I have lost my key.       钥匙现在仍找不到，强调当前结果
```

### 7. 过去完成时：过去的过去

结构：`had + 过去分词`

```text
The train had left before we arrived.
我们到达之前，火车已经开走了。
```

时间线是：火车离开 → 我们到达 → 现在说这件事。

### 8. 现在完成进行时：从过去持续到现在，强调过程

结构：`have/has been + doing`

```text
It has been raining for two hours.
雨已经连续下了两个小时。
```

比较：

```text
I have read the book.              强调读完或已有阅读经历
I have been reading the book.      强调一直在读，未必读完
```

### 9. 过去完成进行时：过去某时之前一直在做

结构：`had been + doing`

```text
He had been waiting for an hour before the bus came.
公共汽车来之前，他已经等了一个小时。
```

观察点在过去的 `the bus came`，等待在此之前开始并持续了一段时间。

### 10. 将来进行时：将来某时正在做

结构：`will be + doing`

```text
This time tomorrow, I will be flying to Shanghai.
明天这个时候，我将正在飞往上海。
```

它也可礼貌地询问对方已经安排好的事情：

```text
Will you be using the car tonight?
你今晚会用车吗？
```

### 11. 将来完成时：到将来某时已经完成

结构：`will have + 过去分词`

```text
By Friday, I will have finished the report.
到星期五，我将已经完成报告。
```

`by + 将来时间` 是常见信号，重点是截止那个时间的完成结果。

### 12. 将来完成进行时：到将来某时已经持续多久

结构：`will have been + doing`

```text
By next June, she will have been teaching here for ten years.
到明年六月，她将在这里教书满十年。
```

### 13. 过去将来时：站在过去看未来

一般过去将来时结构：`would + 动词原形`，或 `was/were going to + 动词原形`。

```text
He said that he would call me the next day.
他说他第二天会给我打电话。
```

说话动作 `said` 在过去；打电话在当时看来还没有发生，所以是“过去的未来”。

其余三种形式主要用于较复杂的叙述：

```text
He said he would be working at eight.          他说八点时他会在工作。
He thought he would have finished by Friday.  他以为星期五前会完成。
By June, he would have been working there for ten years.
到六月，他在那里工作就将满十年。
```

最后一句是过去将来完成进行时，比较少见；会识别即可，不必优先用于口语。

### 14. 同一个动作，时态怎样改变视角

```text
I write reports.                  我平时写报告。
I am writing a report.            我正在写一份报告。
I wrote a report yesterday.       我昨天写了一份报告。
I was writing at eight.           我八点时正在写。
I have written the report.        我已经写完这份报告。
I had written it before he came.  他来之前我已经写完。
I will write it tomorrow.         我明天会写。
I will have written it by noon.   到中午我会写完。
```

选时态时依次问：

1. 观察点在现在、过去还是将来？
2. 我在说事实整体、正在进行、已经完成，还是持续过程？
3. 句中是否存在另一个时间点作为参照？

时间词只能提供线索，不能代替理解。例如 `always` 既能用于一般现在时表示习惯，也能用于进行时表达抱怨：

```text
He always helps me.          他总是帮助我。（中性习惯）
He is always losing keys.    他老是丢钥匙。（带抱怨）
```

### 15. 时间和条件状语从句中的“主将从现”

谈论未来时，`when`、`if`、`unless`、`as soon as` 等引导的时间或条件从句通常用一般现在时表示将来；主句可用 `will`。

```text
I will call you when I arrive.
我到了就给你打电话。

If it rains tomorrow, we will stay home.
如果明天下雨，我们就待在家里。
```

不要写成 `when I will arrive` 或 `if it will rain`（除非 `will` 表意愿等特殊含义）。

## 七、语态：主动还是被动

### 1. 主动语态

主语是动作执行者：

```text
Tom cleaned the room.
汤姆打扫了房间。
```

### 2. 被动语态

主语是动作承受者。基本结构：`be + 过去分词`。

```text
The room was cleaned by Tom.
房间被汤姆打扫了。
```

转换步骤：

1. 把主动句宾语移到主语位置。
2. 按原句时态变化 `be`。
3. 实义动词改成过去分词。
4. 原主语有必要时放在 `by` 后。

常见时态的被动结构：

| 时态 | 结构 | 例句 |
| --- | --- | --- |
| 一般现在时 | am/is/are done | English is spoken here. |
| 一般过去时 | was/were done | The bridge was built in 2020. |
| 一般将来时 | will be done | The work will be finished tomorrow. |
| 现在进行时 | am/is/are being done | The road is being repaired. |
| 现在完成时 | have/has been done | The email has been sent. |

### 3. 被动语态与系表结构的区别

两者都可能是 `be + 过去分词`，但意义不同：

```text
The door was closed by John.  被动：约翰关了门，强调动作
The door was closed.          可能是状态：门处于关闭状态
```

有明确执行者、动作过程或可加入 `by...` 时，更像被动；只描述主语状态时，更像“系动词 + 表语”。具体判断要结合上下文。

### 4. 否定、疑问和情态动词的被动

变化只发生在第一个助动词上：

```text
The work has not been finished.
工作还没有完成。

Has the work been finished?
工作完成了吗？

The work must be finished today.
工作必须今天完成。
```

情态动词的被动结构是：`情态动词 + be + 过去分词`。

### 5. 双宾语句的两种被动

```text
They gave me a prize.
他们给了我一个奖品。

I was given a prize.
A prize was given to me.
```

人或物都可以移到主语位置，但把物作为主语时，原来的间接宾语前通常要恢复 `to` 或 `for`。

### 6. 宾补和感官/使役结构的被动

```text
They elected him captain.
He was elected captain.
```

宾语变成主语后，原宾补仍保留。

主动语态中，`make/see/hear` 等后面可能接不带 `to` 的不定式；改为被动后通常要恢复 `to`：

```text
They made him wait.
He was made to wait.

We saw her enter the room.
She was seen to enter the room.
```

### 7. 短语动词变被动时不能丢介词

```text
They looked after the child carefully.
The child was carefully looked after.
```

`look after` 是一个整体，不能写成 `The child was looked.`。

### 8. 哪些句子通常不能变被动

- 不及物动词没有宾语可提升：`He arrived.`
- 某些表示所属或关系的状态动词不自然：`have`、`belong to`、`resemble`。
- 宾语是反身代词且动作回到主语自身时通常不转换。

```text
She has a car.              通常不改被动
The car belongs to her.     通常不改被动
He hurt himself.            通常不改被动
```

### 9. get 被动

口语中可用 `get + 过去分词`，常强调变化、意外或主语受到影响：

```text
He got hurt in the game.
他在比赛中受伤了。

They got married last year.
他们去年结婚了。
```

正式写作和中性陈述通常仍优先使用 `be` 被动。

### 10. have/get something done：让别人替自己做

结构：`have/get + 宾语 + 过去分词`。宾语承受动作，实际执行者通常是别人。

```text
I had my hair cut yesterday.
我昨天去剪了头发。（请别人剪）

She is going to get her phone repaired.
她打算找人修手机。
```

它有时也表示遭遇不好的事情：

```text
He had his wallet stolen.
他的钱包被偷了。
```

## 八、名词、冠词、数词：怎样正确说“一个、一些、这个”

### 1. 可数名词与不可数名词

- **可数名词**可一个个数：`a book`、`two books`。
- **不可数名词**通常不直接按个数数：`water`、`information`、`advice`。

不可数名词不能直接与 `a/an` 搭配，也通常没有复数形式：

```text
some information       一些信息
a piece of information 一条信息
```

不要说 `an information` 或 `informations`。

名词还可从意义上分为：

- **普通名词**：一类人或物，如 `city`、`teacher`。
- **专有名词**：特定名称，首字母通常大写，如 `China`、`Tom`。
- **具体名词**：能通过感官感知，如 `apple`、`music`。
- **抽象名词**：思想、品质或状态，如 `love`、`freedom`。
- **集合名词**：把一群成员看成一个单位，如 `family`、`team`。

有些名词会随含义改变可数性：

```text
chicken        鸡肉（不可数）
a chicken      一只鸡（可数）

paper          纸（不可数）
a paper        一篇论文/一份报纸（可数，依语境）

two coffees    两杯咖啡（把饮料按“份”来数）
```

### 2. 名词复数

常规变化：

- 多数词加 `-s`：`book → books`
- 以 `s/x/ch/sh` 等结尾加 `-es`：`box → boxes`
- 辅音字母 + `y`：`city → cities`
- 部分 `f/fe` 变 `ves`：`knife → knives`

常见不规则形式：`man → men`、`child → children`、`mouse → mice`。它们需要单独积累。

还有三类容易忽略：

```text
sheep → sheep           单复数同形
deer → deer
tooth → teeth           内部元音变化
foot → feet
analysis → analyses     外来词复数
```

只以复数形式出现的名词常接复数谓语：`scissors`、`trousers`、`glasses`。要数它们，可以使用 `a pair of`：

```text
These scissors are sharp.
This pair of scissors is sharp.
```

### 3. 名词所有格：表示“谁的”

有生命的人或动物常用 `'s`：

```text
Tom's bag              汤姆的包
the girl's room        那个女孩的房间
the girls' room        那些女孩共用的房间
children's books       儿童读物
```

无生命事物常用 `of`：

```text
the door of the room   房间的门
the end of the story   故事的结尾
```

时间、距离、组织和国家等也常用 `'s`：`today's news`、`the company's plan`。

### 4. 限定词：确定名词的范围

限定词放在名词短语前，告诉读者“哪一个、谁的、多少”。主要包括：

```text
冠词：a, an, the
指示限定词：this, that, these, those
物主限定词：my, your, his, her, its, our, their
数量限定词：some, any, much, many, few, little, several, enough
分配限定词：each, every, either, neither
```

冠词、指示限定词和物主限定词通常不能在同一个位置叠加：

```text
the my book    ×
my book        ✓
the book       ✓
```

多个修饰语的大致顺序是：

```text
前位限定词 + 核心限定词 + 数量词 + 形容词 + 名词
all            my          three    old       books
```

### 5. some、any、no 与 every

```text
I have some questions.       我有一些问题。
Do you have any questions?   你有问题吗？
I don't have any questions.  我没有问题。
I have no questions.         我没有问题。
```

`some` 常用于肯定句，`any` 常用于疑问和否定句。但期待肯定回答的请求或提议常用 `some`：

```text
Would you like some tea?
你想喝点茶吗？
```

`every` 强调群体中的每一个，后接可数名词单数；`all` 强调整体，常接复数或不可数名词。

```text
Every student has a book.
All students have books.
All water contains minerals.
```

### 6. many、much、few、little 与 a lot of

| 搭配对象 | 数量多 | 几乎没有 | 有一些 |
| --- | --- | --- | --- |
| 可数名词复数 | many | few | a few |
| 不可数名词 | much | little | a little |

```text
Few people understood.       几乎没人懂。（偏否定）
A few people understood.     有几个人懂。（偏肯定）
There is little hope.        几乎没有希望。
There is a little hope.      还有一点希望。
```

`a lot of/lots of` 可同时修饰可数复数和不可数名词，在肯定句中很常用。

### 7. each、every、both、either 与 neither

```text
Each student has a card.       每名学生各有一张卡，强调个体。
Every student has a card.      每名学生都有卡，强调整体中的全部成员。
Both answers are correct.      两个答案都正确。
Either answer is acceptable.   两个答案中任意一个都可以。
Neither answer is correct.     两个答案都不正确。
```

### 8. 不定冠词 a/an

`a/an` 表示“一个、某个”，只能放在可数名词单数前。

- `a` 用在辅音音素前：`a university`（开头读 /j/）。
- `an` 用在元音音素前：`an hour`（`h` 不发音）。

判断依据是**发音**，不是字母。

`a/an` 还可表示职业、类别或“每一”：

```text
She is an engineer.       她是一名工程师。
A whale is a mammal.      鲸是一种哺乳动物。
twice a week              每周两次
```

### 9. 定冠词 the

`the` 表示说话双方都知道、前文提过或独一无二的对象。

```text
I saw a dog. The dog was very friendly.
我看到一只狗。那只狗很友善。
```

第一次出现、不确定是哪只，用 `a dog`；第二次已明确，用 `the dog`。

常见使用场景还包括：

```text
the sun                   独一无二或语境中唯一
the first lesson          序数词前
the tallest boy           最高级前
play the piano            西洋乐器前
the rich                  “富人”这一类人
the Yangtze River         江河、海洋、山脉等名称
```

人名、普通城市名、国家名、语言和学科前通常不用 `the`：`Tom`、`Beijing`、`China`、`English`、`history`。但名称本身含普通复数名词或表示政治联合体时可能使用 `the`，如 `the United States`。

### 10. 零冠词

泛指复数名词和不可数名词时，常不用冠词：

```text
Dogs are friendly.  狗通常很友善。
Water is important. 水很重要。
```

固定制度或功能意义前也常用零冠词：

```text
go to school       去上学（强调学生身份和学校功能）
go to bed          去睡觉
have breakfast     吃早饭
by bus             乘公共汽车
```

若指具体建筑或物件，则可能使用冠词：

```text
I went to the school to meet the teacher.
我去了那所学校见老师。（指具体地点）
```

### 11. 基数词、序数词和常用数字表达

- 基数词回答“多少”：`one, two, twenty-one, one hundred`。
- 序数词回答“第几”：`first, second, third, fourth`。

```text
There are three rooms.      有三个房间。
My room is on the third floor. 我的房间在三楼。
```

年份常分成两段读，日期常用序数词：`August 29th, 2026`。

常见结构：

```text
21          twenty-one
105         one hundred and five（英式）/ one hundred five（美式）
2,350       two thousand three hundred and fifty
1/2         one half
1/3         one third
3/4         three quarters
2.5         two point five
30%         thirty percent
```

`hundred/thousand/million` 前有具体数字时通常不加 `-s`；表示模糊数量时用复数并接 `of`：

```text
three hundred students
hundreds of students
```

年龄、尺寸等作前置定语时使用单数并用连字符：

```text
a ten-year-old boy     一个十岁男孩
a five-kilometre walk  五公里的步行路程
```

时间常有两种读法：

```text
6:05   six oh five / five past six
6:15   six fifteen / a quarter past six
6:30   six thirty / half past six
6:45   six forty-five / a quarter to seven
```

日期中的日通常读序数词：

```text
August 29, 2026     August the twenty-ninth, twenty twenty-six
29 August 2026      the twenty-ninth of August, twenty twenty-six
```

美式日期常写“月—日—年”，英式日期常写“日—月—年”。纯数字日期如 `03/04/2026` 容易产生歧义，正式写作宜拼出月份。

## 九、代词：用对主格、宾格和所有格

### 1. 人称代词

| 人称 | 主格：作主语 | 宾格：作宾语 | 形容词性物主代词 | 名词性物主代词 |
| --- | --- | --- | --- | --- |
| 我 | I | me | my | mine |
| 你/你们 | you | you | your | yours |
| 他 | he | him | his | his |
| 她 | she | her | her | hers |
| 它 | it | it | its | its |
| 我们 | we | us | our | ours |
| 他们 | they | them | their | theirs |

```text
She gave me her book. Mine was at home.
她把她的书给了我。我的书在家里。
```

- `She` 作主语，用主格。
- `me` 作宾语，用宾格。
- `her` 后接名词 `book`。
- `Mine` 本身就等于 `my book`，后面不能再接名词。

### 2. 反身代词

`myself`、`yourself`、`himself`、`herself`、`itself`、`ourselves`、`yourselves`、`themselves` 表示“某人自己”。

```text
She taught herself English.
她自学英语。
```

### 3. 指示代词

| 距离/数量 | 单数 | 复数 |
| --- | --- | --- |
| 近 | this | these |
| 远 | that | those |

```text
This is my cup. Those are yours.
这是我的杯子。那些是你的。
```

### 4. 不定代词

`someone`、`anyone`、`everyone`、`nothing` 等不指明具体对象。由 `some/any/every/no + one/body/thing` 构成的代词通常按单数处理。

```text
Everyone is ready.
每个人都准备好了。
```

形容词修饰这类代词时通常后置：

```text
something interesting  有趣的东西
```

`both`、`either`、`neither` 用于两者；`all`、`any`、`none` 可用于三者或更多：

```text
Both of them are ready.       他们两人都准备好了。
Neither of them is ready.     他们两人都没准备好。
None of them is ready.        他们当中没有人准备好。
```

### 5. 疑问代词

`who` 问人，`what` 问事物或内容，`which` 在有限范围中选择，`whose` 问所属。

```text
Who called you?                 谁给你打了电话？
What happened?                  发生了什么？
Which do you prefer, tea or coffee? 茶和咖啡你更喜欢哪一种？
Whose is this?                  这是谁的？
```

### 6. 相互代词

`each other` 和 `one another` 表示“互相”。现代英语中二者通常可以互换。

```text
The two friends help each other.
这两个朋友互相帮助。
```

### 7. one/ones：代替前面出现的同类名词

```text
My phone is old. I need a new one.
我的手机旧了，我需要一部新的。

These shoes are small. Show me the larger ones.
这些鞋小了，请给我看看大一点的。
```

`one/ones` 代替同类中的另一个；`it/they` 通常指前面提到的同一个对象。

```text
I bought a phone, but it was broken.  it 指刚买的那一部
I need a phone, so I will buy one.     one 指任意一部同类手机
```

### 8. it 的四种常见工作

```text
I found my key. It was under the bed.  指代前文事物
It is raining.                          表示天气
It is five o'clock.                     表示时间
It is important to rest.                形式主语
I find it easy to use.                  形式宾语
```

最后两句中，真正内容分别是 `to rest` 和 `to use`；`it` 先占据英语习惯的位置，使句子不至于头重脚轻。

## 十、形容词与副词：一个修饰名词，一个修饰动作

### 1. 最基本的区别

```text
She is a careful driver.  careful 修饰名词 driver
She drives carefully.     carefully 修饰动词 drives
```

系动词后通常用形容词作表语：

```text
The soup tastes good.  汤尝起来不错。
```

不是 `tastes well`；这里是在说明 soup 的性质。`well` 表示“身体健康”时也可作形容词：`I am well.`。

### 2. 形容词的位置

- 单个形容词通常放名词前：`a beautiful garden`。
- 形容词短语通常放名词后：`a box full of books`。
- 修饰不定代词时后置：`nothing serious`。

多个形容词同时放在名词前时，常见顺序是：

```text
限定词 → 评价 → 大小 → 年龄 → 形状 → 颜色 → 来源 → 材料 → 用途 → 名词
a lovely small old round brown French wooden table
```

实际写作中不要堆太多形容词；这个顺序主要用于判断哪种表达更自然。

复合形容词常用连字符连接，内部名词通常用单数：

```text
a five-minute break    五分钟的休息
a well-known writer    一位知名作家
```

### 3. -ing 与 -ed 形容词

一般来说，`-ing` 说明事物“令人产生某种感受”，`-ed` 说明人“感到怎样”。

```text
The movie is boring.  电影令人无聊。
I am bored.           我感到无聊。

The result is surprising. 结果令人惊讶。
We are surprised.          我们感到惊讶。
```

### 4. 比较级和最高级

结构：

```text
A + be + 比较级 + than + B
A + be + the + 最高级 + 范围
```

```text
Tom is taller than Jack.
汤姆比杰克高。

Tom is the tallest boy in his class.
汤姆是班里最高的男孩。
```

短词常加 `-er/-est`，长词常用 `more/most`：

```text
tall → taller → tallest
beautiful → more beautiful → most beautiful
```

常见不规则变化：`good/well → better → best`，`bad → worse → worst`。

其他常用比较结构：

```text
as tall as              和……一样高
not as/so tall as       不如……高
much/far/a little taller 高得多/稍高一些
the taller of the two   两者中较高的那个
the more, the better    越多越好
taller and taller       越来越高
```

比较对象必须逻辑一致：

```text
Tom's room is larger than Jack's.  ✓ 汤姆的房间和杰克的房间相比
Tom's room is larger than Jack.    × 字面变成房间和杰克本人相比
```

### 5. 副词的类型和常见位置

副词可分为：

- 方式：`slowly`、`carefully`
- 地点：`here`、`outside`
- 时间：`now`、`yesterday`
- 频度：`always`、`often`、`never`
- 程度：`very`、`quite`、`almost`
- 句子副词：`fortunately`、`perhaps`、`however`

频度副词 `always`、`usually`、`often`、`sometimes`、`never` 通常放在实义动词前、`be` 后：

```text
He often walks to work.
He is often late.
```

`already` 常用于肯定句，`yet` 常放在疑问句或否定句末：

```text
I have already finished.
Have you finished yet?
I haven't finished yet.
```

多个句末状语同时出现时，常见顺序是“方式 → 地点 → 时间”：

```text
She sang beautifully at the concert last night.
她昨晚在音乐会上唱得很美。
```

### 6. hard/hardly、late/lately 等易混副词

```text
He works hard.       他工作努力。
He hardly works.     他几乎不工作。

He arrived late.     他到得晚。
I haven't seen him lately. 最近我没见过他。

The plane flew high. 飞机飞得高。
He is highly respected. 他备受尊敬。
```

加 `-ly` 后不一定只是同一个词的普通副词形式，词义可能已经改变。

## 十一、介词：用关系来理解，不要只背中文

### 1. 时间介词 at、on、in

- `at`：具体时刻或点，`at 7:00`、`at noon`
- `on`：具体某一天或某天的上午/下午，`on Monday`、`on Monday morning`
- `in`：较长时间，`in 2026`、`in August`、`in winter`

```text
The meeting starts at 9:00 on Monday morning in August.
会议在八月的一个星期一上午九点开始。
```

### 2. 地点介词 at、on、in

- `at`：把地点看作一个点，`at the station`
- `on`：在表面上，`on the wall`
- `in`：在内部或范围内，`in the room`、`in China`

### 3. 时间边界：for、since、by、until

- `for + 时间段`：持续多久，`for two hours`
- `since + 起点`：自从何时，`since Monday`
- `by + 截止点`：不迟于，`by Friday`
- `until + 终点`：一直到，`until Friday`

```text
I have worked here since 2020.
我从 2020 年起就在这里工作。

Please finish it by Friday.
请最迟在星期五前完成。

I will stay here until Friday.
我会一直待到星期五。
```

### 4. 易混的地点和方向

```text
in the room       在房间里（静态位置）
into the room     进入房间（方向）
on the table      在桌面上
above the table   在桌子上方，不一定接触
between A and B   在两者之间
among the students 在学生群体之中
```

### 5. 运动方向介词

```text
to        朝向并到达：go to school
towards   朝……方向，不强调到达：walk towards the door
into      从外到内：jump into the water
out of    从内到外：run out of the room
across    从表面一边到另一边：walk across the road
through   从内部穿过：walk through the tunnel
along     沿着：walk along the river
past      经过：walk past the bank
```

### 6. 方式、工具、材料和执行者

```text
by bus                 乘公共汽车（交通方式）
with a knife           用刀（具体工具）
by Shakespeare         由莎士比亚创作（被动句执行者）
made of wood           由木头制成，仍看得出原材料
made from grapes       由葡萄制成，原材料形态已改变
in English             用英语
```

### 7. 介词与连接词不要混淆

介词后接名词性成分；从属连词后接完整的“主语 + 谓语”。

```text
because of the rain       介词短语：因为下雨
because it rained         从句：因为下雨

despite the rain          介词短语：尽管下雨
although it rained        从句：尽管下雨

during the meeting        介词短语：会议期间
while we were meeting     从句：我们开会时
```

### 8. 固定搭配要整体学习

介词不能完全靠中文逐字推导，要和前面的词一起记：

```text
listen to music
wait for someone
depend on something
be interested in
be good at
be afraid of
```

建议把它们当成一个词块，而不是分别背 `listen` 和 `to`。

## 十二、连词：把信息连接起来

### 1. 并列连词

并列连词连接语法地位相同的内容：

- `and`：并且
- `but`：但是
- `or`：或者，否则
- `so`：所以
- `for`：因为（较正式）
- `yet`：然而

```text
I was tired, but I kept working.
我很累，但继续工作。
```

成对使用的关联连词也连接同等级成分：

```text
both A and B               A 和 B 都
either A or B              A 或 B
neither A nor B            A 和 B 都不
not only A but also B      不仅 A，而且 B
```

连接的两部分应保持平行：

```text
She likes reading and swimming.   ✓ 两边都是 doing
She likes to read and swimming.   △ 不平行，宜统一形式
```

并列两个完整句子时，前面通常加逗号：

```text
I called him, but he did not answer.
```

只连接词或短语时通常不用逗号：`tea and coffee`。

### 2. 从属连词

从属连词把一个不能独立承担主要信息的从句连接到主句：

```text
I stayed home because it was raining.
主句             原因状语从句
```

中文可以说“因为……所以……”，标准英语通常只保留一个逻辑连接词：

```text
Because it was raining, I stayed home.
It was raining, so I stayed home.
```

不要写成 `Because ..., so ...`。

常见从属连词按意义归类：

| 关系 | 常见连接词 |
| --- | --- |
| 时间 | when, while, before, after, since, until |
| 原因 | because, since, as |
| 条件 | if, unless, provided that |
| 让步 | although, though, even if |
| 目的 | so that, in order that |
| 结果 | so...that, such...that |
| 比较 | than, as...as |

同一个词可能有多种语法身份：

```text
I left after lunch.          after 是介词，后接名词
I left after we ate lunch.   after 是连词，后接从句
```

## 十三、四类句子和疑问句结构

### 1. 陈述句

陈述事实或观点，通常是“主语 + 谓语”：

```text
She likes coffee.
```

### 2. 一般疑问句

能用 yes/no 回答。

```text
Is she ready?
Can you swim?
Do they live here?
Did he call you?
```

规则：句中已有 `be`、情态动词或助动词，就把它移到主语前；若只有实义动词，则借助 `do/does/did`。

### 3. 特殊疑问句

用 `what`、`who`、`which`、`when`、`where`、`why`、`how` 提问。

```text
Where do you live?
你住在哪里？

Why was she late?
她为什么迟到？
```

通常结构是：`疑问词 + 一般疑问句语序`。

但若疑问词本身就是主语，不再使用倒装：

```text
Who called you?  谁给你打了电话？
```

不是 `Who did call you?`（除非特意强调）。

比较主语疑问和宾语疑问：

```text
Who loves Lucy?      谁喜欢露西？who 是主语，不用 do
Who does Lucy love?  露西喜欢谁？who 是宾语，要用 does
```

选择疑问句给出选项，不能只用 yes/no 回答：

```text
Would you like tea or coffee?
你想喝茶还是咖啡？
```

否定疑问句常表达惊讶、确认或期待赞同：

```text
Aren't you ready?
你还没准备好吗？
```

### 4. 祈使句

用于命令、请求、建议，通常省略主语 you，直接以动词原形开头。

```text
Open the window, please.
请打开窗户。

Don't touch it.
不要碰它。

Let's begin.
我们开始吧。
```

### 5. 感叹句

`what` 强调名词，`how` 强调形容词或副词。

```text
What a beautiful day it is!
多么美好的一天啊！

How beautiful the day is!
这一天多美啊！
```

结构：

```text
What + (a/an) + 形容词 + 名词 + 主语 + 谓语!
How + 形容词/副词 + 主语 + 谓语!
```

### 6. 反意疑问句

前面陈述，后面用简短问句确认。基本规律是“前肯后否，前否后肯”。

```text
You are tired, aren't you?
你累了，对吧？

He doesn't smoke, does he?
他不抽烟，对吧？
```

回答依据事实，而不是依据前句肯否：

```text
You don't like tea, do you?
Yes, I do.   不，我喜欢。（按英语逻辑：是的，我喜欢。）
No, I don't. 对，我不喜欢。（按英语逻辑：不，我不喜欢。）
```

几个常见特殊形式：

```text
I'm late, aren't I?               I am 的反意部分通常用 aren't I
Let's begin, shall we?            Let's... 用 shall we
Open the door, will you?          普通祈使句常用 will you
Everyone is here, aren't they?    不定代词指人时，反意部分常用 they
Nothing happened, did it?         nothing 已含否定，后面用肯定形式
```

## 十四、非谓语动词：动词不当“句子发动机”时

一个简单句原则上只有一套核心谓语。另一个动作若不通过连词组成从句，通常要变成非谓语形式。

```text
I want go home.       × 两个动词直接相撞
I want to go home.    ✓ want 是谓语，to go 是非谓语
```

非谓语有三大类：不定式、动名词和分词。

先看完整形式表。`do` 代表动词原形：

| 类型 | 一般主动 | 一般被动 | 完成主动 | 完成被动 |
| --- | --- | --- | --- | --- |
| 不定式 | to do | to be done | to have done | to have been done |
| 动名词 | doing | being done | having done | having been done |
| 分词 | doing / done | being done | having done | having been done |

初学先掌握 `to do / doing / done`，其余形式的核心只是增加“动作更早发生”或“主语承受动作”的信息。

### 1. 动词不定式：to do

不定式常带有“将要、目的、一次具体动作”的感觉，可作主语、宾语、表语、定语、状语和宾补。

```text
To learn English takes time.      作主语：学英语需要时间。
I want to learn English.          作宾语：我想学英语。
My plan is to learn English.      作表语：我的计划是学英语。
I need a book to read.            作定语：我需要一本可读的书。
I came here to learn English.     作目的状语：我来这里学英语。
She told me to wait.              作宾补：她叫我等。
```

不定式也可以不带 `to`，称为裸不定式，常见于：

```text
情态动词后：You must leave.
使役动词后：Let me go. / They made him wait.
感官动词后：I saw her cross the street.
had better 后：You had better rest.
```

不定式的逻辑主语可由 `for + 宾格` 引出：

```text
It is important for you to practise.
练习对你来说很重要。
```

表示对某人品质的评价时常用 `of`：

```text
It was kind of you to help me.
你帮助我，真是太友善了。
```

完成式表示不定式动作早于谓语动作：

```text
He seems to have forgotten my name.
他似乎已经忘了我的名字。
```

被动式表示不定式的逻辑主语承受动作：

```text
The bridge needs to be repaired.
这座桥需要修理。
```

### 2. 动名词：doing

动名词把动作当作一件事情，具有名词性质。

```text
Reading is useful.          作主语：阅读有益。
I enjoy reading.            作宾语：我喜欢阅读。
My hobby is reading.        作表语：我的爱好是阅读。
```

介词后若接动词，通常用动名词：

```text
Thank you for helping me.
谢谢你帮助我。
```

动名词前可使用物主限定词或宾格表示逻辑主语。正式书面语偏好物主形式：

```text
I appreciate your helping me.
我很感谢你的帮助。
```

动名词也有完成式和被动式：

```text
He denied having taken the money.
他否认拿过那笔钱。

She dislikes being treated like a child.
她不喜欢被当成小孩。
```

### 3. 现在分词与过去分词

- `doing` 常表达主动、进行。
- `done` 常表达被动、完成或状态。

```text
The girl standing by the door is Lucy.
站在门边的女孩是露西。（女孩主动站着）

The bike repaired yesterday is mine.
昨天修好的自行车是我的。（自行车被修）
```

分词也可作状语：

```text
Seeing the dog, the boy ran away.
男孩看见那条狗，便跑开了。
```

这里 `seeing` 的逻辑主语必须和主句主语 `the boy` 一致。不要写出“悬垂分词”：

```text
Walking down the street, the rain started. ×
```

这句话字面上成了“雨在街上走”。可改为：

```text
While I was walking down the street, it started to rain.
```

分词作宾补时，可表示看见动作正在进行或动作已完成/被动：

```text
I saw him crossing the street.  我看见他正在过马路。
I heard my name called.          我听见有人叫我的名字。
```

完成分词强调动作先发生：

```text
Having finished the work, she went home.
完成工作后，她回家了。
```

独立主格结构有自己的逻辑主语，用来补充时间、原因或伴随情况：

```text
The weather being fine, we went for a walk.
天气很好，我们出去散步了。

The work finished, everyone went home.
工作完成后，大家都回家了。
```

它较常见于正式书面语。小白先会识别即可，日常表达完全可以改成完整状语从句。

### 4. doing 和 to do 的常见意义差别

```text
I stopped smoking.     我戒烟了。（停止这件事）
I stopped to smoke.    我停下来去抽烟。（停下别的事，目的是抽烟）

I remember locking the door.  我记得锁过门。（回忆过去）
Remember to lock the door.     记得去锁门。（动作尚未做）
```

具体接 `doing` 还是 `to do`，仍需按动词搭配积累。

### 5. 常见搭配分组记忆

常接 `doing` 的动词：

```text
enjoy, avoid, finish, mind, practise, suggest, consider, keep
```

```text
She enjoys cooking.
```

常接 `to do` 的动词：

```text
want, hope, decide, plan, promise, refuse, learn, manage
```

```text
They decided to leave.
```

常用“动词 + 人 + to do”的动词：

```text
ask, tell, want, invite, advise, allow, encourage, remind
```

```text
The teacher encouraged us to speak English.
```

### 6. 既接 doing 又接 to do 的动词

有些意思基本相同：

```text
It started raining. / It started to rain.
开始下雨了。
```

有些意思明显不同：

```text
Try pressing this button.   试试按这个按钮。（尝试一种办法）
Try to press this button.    努力按下这个按钮。（设法完成）

He forgot locking the door. 他忘记自己锁过门。（忘了过去的记忆）
He forgot to lock the door.  他忘记去锁门。（该做却没做）

We regret telling you this.  我们后悔告诉了你这件事。
We regret to tell you this.  我们遗憾地要告诉你这件事。
```

### 7. 非谓语选择的四步判断法

1. 先确认句中已经有核心谓语。
2. 判断非谓语动作与其逻辑主语是主动还是被动。
3. 判断非谓语动作与谓语动作同时、稍后，还是更早发生。
4. 检查前面动词或介词是否有固定搭配要求。

```text
The man invited to the meeting arrived early.
```

`arrived` 是谓语；man 是“被邀请”，所以用过去分词 `invited` 作后置定语。

## 十五、从句：把一个小句子放进大句子

从句内部通常有“主语 + 谓语”，但它在大句子里只担任一个成分。

先区分四种句子结构：

```text
简单句：I was tired.
只有一个独立分句。

并列句：I was tired, so I went home.
两个独立分句由并列连词连接。

主从复合句：I went home because I was tired.
一个主句带一个从句。

并列复合句：I was tired, so I went home because I needed rest.
至少两个独立分句，并且含有从句。
```

**主句**可以独立表达核心意思；**从句**由连接词引导，在大句子中担任一项工作。不要以句子长短判断类别：一个简单句可能很长，一个复合句也可能很短。

### 1. 三大从句一眼区分

| 从句 | 在大句子里相当于 | 作用 |
| --- | --- | --- |
| 名词性从句 | 一个名词 | 作主语、宾语、表语、同位语 |
| 定语从句 | 一个形容词 | 修饰名词或代词 |
| 状语从句 | 一个副词 | 说明时间、原因、条件、让步等 |

## 十六、名词性从句：把一句话当名词用

### 1. 宾语从句

整个从句作动词或介词的宾语。

```text
I know that she is right.
我知道她是对的。
```

主句主干是 `I know ...`，`that she is right` 回答“知道什么”，所以是宾语从句。

常见引导词：

- `that`：只连接，不在从句中作成分，通常无实际词义。
- `whether/if`：是否。
- `what/who/which/when/where/why/how`：保留自身含义，并常在从句中作成分。

```text
I wonder whether he will come.
我想知道他是否会来。

Tell me where you live.
告诉我你住在哪里。
```

宾语从句使用**陈述语序**：

```text
Do you know where he is?    ✓
Do you know where is he?    ×
```

`that` 引导普通宾语从句时常可省略：

```text
I think (that) she is right.
```

但多个并列 `that` 从句中，后面的 `that` 通常保留，以免结构不清：

```text
He said (that) he was tired and that he wanted to leave.
```

#### whether 与 if 的区别

两者引导宾语从句时常都表示“是否”：

```text
I don't know whether/if he will come.
```

下列情况通常使用 `whether`：

```text
whether or not                 与 or not 直接连用
It depends on whether...       介词后
Whether he will come is unclear. 主语从句位于句首
I don't know whether to go.    后接不定式
```

#### that 与 what 的区别

`that` 只负责连接，在从句中不作成分；`what` 相当于“the thing(s) that”，自身要在从句中作主语、宾语或表语。

```text
I know that she bought a book.
that 不作成分；从句本身结构完整。

I know what she bought.
what 作 bought 的宾语，意思是“她买的东西”。
```

#### 宾语从句的时态

主句是现在时，从句按事实选择时态：

```text
I know that he is busy.
I know that he left yesterday.
```

主句是过去时，转述内容通常相应后移；但客观真理和现在仍成立的事实可以不后移：

```text
He said that he was busy.
The teacher told us that water boils at 100°C at standard pressure.
```

### 2. 主语从句

整个从句作主语。

```text
What he said is true.
他说的话是真的。
```

`What he said` 整体是主语。为避免头重脚轻，英语常用形式主语 `it`：

```text
It is clear that he is right.
很明显，他是对的。
```

真正主语是后面的 `that he is right`，`it` 只是先占位置。

常见形式主语句型：

```text
It is + 形容词 + that...       It is obvious that she cares.
It is + 名词 + that...         It is a pity that you cannot come.
It is + 过去分词 + that...     It is believed that the story is true.
It + 动词 + that...            It seems that he is tired.
```

主语从句通常看作单数概念，谓语多用单数：

```text
What he needs is more time.
```

如果 `what` 从句后的表语明确为复数，实际使用中也可能采用复数：`What we need are better tools.`。

### 3. 表语从句

放在系动词后说明主语。

```text
The problem is that we have no time.
问题是我们没有时间。
```

### 4. 同位语从句

解释一个抽象名词的具体内容，常见名词有 `fact`、`news`、`idea`、`hope`、`question`。

```text
The news that we won the game is exciting.
我们赢得比赛这个消息令人兴奋。
```

这里 `that we won the game` 是在解释 news 的内容。

同位语从句还可由 `whether` 或疑问词引导：

```text
The question whether we should go remains unanswered.
我们是否应该去，这个问题仍没有答案。

I have no idea why she left.
我不知道她为什么离开。
```

### 5. 名词性从句检查清单

1. 先判断整个从句在主句中作主语、宾语、表语还是同位语。
2. 从句一律使用陈述语序。
3. 检查引导词是否在从句中缺少成分：不缺常考虑 `that/whether`，缺人或事物成分常考虑 `who/what/which`。
4. 区分 `that`（无成分、无具体词义）与 `what`（有成分，意为“……的事物”）。
5. 再根据时间关系选择从句时态。

## 十七、定语从句：用一句话给名词贴标签

### 1. 基本结构和术语

```text
The man who is speaking is my teacher.
```

- `the man`：先行词，即被修饰的词。
- `who`：关系词，既连接主从句，又在从句中作主语。
- `who is speaking`：定语从句，说明是哪一个 man。

### 2. 关系代词怎么选

| 先行词 | 关系词 | 在从句中的作用 |
| --- | --- | --- |
| 人 | who | 主语或宾语 |
| 人 | whom | 宾语，较正式 |
| 人或物 | that | 主语或宾语 |
| 物 | which | 主语或宾语 |
| 人或物 | whose | 定语，表示“谁的” |

```text
The woman who called me is a doctor.
给我打电话的女士是一名医生。

The book which I bought is useful.
我买的那本书很有用。

The student whose phone rang was embarrassed.
手机响了的那名学生很尴尬。
```

关系代词作宾语时，在限制性定语从句中常可省略：

```text
The book (that) I bought is useful.
```

作主语时不能省略：

```text
The book that is on the desk is mine.
```

在下列常见限制性结构中，传统考试语法通常偏好 `that`：

- 先行词同时包括人和物。
- 先行词被最高级、序数词、`the only`、`the very` 修饰。
- 先行词是不定代词 `all`、`everything`、`nothing` 等。

```text
This is the best film that I have seen.
这是我看过的最好的电影。
```

但非限制性定语从句或介词直接放在关系词前时不能用 `that`。

### 3. 关系副词 when、where、why

它们在从句中作状语：

```text
I remember the day when we met.       when = on which
我记得我们相遇的那一天。

This is the house where I was born.   where = in which
这是我出生的房子。

Tell me the reason why you left.      why = for which
告诉我你离开的原因。
```

不能只看到时间、地点名词就机械选择 `when/where`，要看关系词在从句中担任什么成分：

```text
This is the place where I work.
where 作 work 的地点状语。

This is the place that I visited.
that 作 visited 的宾语。
```

### 4. 介词 + 关系代词

正式表达中，可把介词放在 `whom/which` 前：

```text
The person to whom I spoke was helpful.
= The person who/whom I spoke to was helpful.

The house in which she lives is old.
= The house which/that she lives in is old.
```

介词提前后不能用 `who` 或 `that`，也不能省略关系代词。

### 5. 限制性与非限制性定语从句

限制性定语从句不可随意删掉，不用逗号：

```text
Students who work hard will improve.
努力学习的学生会进步。（只谈这类学生）
```

非限制性定语从句只是补充说明，通常用逗号隔开，不能用 `that`：

```text
Tom, who works hard, has improved.
汤姆很努力，他已经进步了。（补充说明 Tom）
```

非限制性定语从句也可以补充说明整个主句，此时常用 `which`：

```text
He missed the train, which made him late.
他错过了火车，这件事导致他迟到。
```

`which` 指代前面整件事，而不是 train。

### 6. as 引导的定语从句

`as` 常出现在 `such...as`、`the same...as` 中，也可引导非限制性定语从句，表达“正如”。

```text
Choose such books as interest you.
选择那些使你感兴趣的书。

As we all know, practice is important.
众所周知，练习很重要。
```

### 7. 定语从句与同位语从句的区别

```text
The news that surprised me was false.
让我吃惊的那条消息是假的。
```

`that` 在从句中作主语，`that surprised me` 修饰 news，是定语从句。

```text
The news that we won surprised me.
我们获胜的消息让我吃惊。
```

`that` 不作成分，后面的句子解释 news 的内容，是同位语从句。

### 8. 定语从句检查清单

1. 找先行词，看它指人、物、时间、地点还是原因。
2. 把先行词放回从句，判断缺主语、宾语、定语还是状语。
3. 缺主语/宾语常选关系代词；缺时间/地点/原因状语才考虑 `when/where/why`。
4. 判断是否有逗号；非限制性从句不能用 `that`。
5. 关系词作从句主语时，检查谓语与先行词一致。

## 十八、状语从句：说明时间、原因、条件等背景

### 1. 时间状语从句

常见引导词：`when`、`while`、`before`、`after`、`until`、`since`、`as soon as`。

```text
When I arrived, they were eating.
我到达时，他们正在吃饭。

Please wait here until I come back.
请在这里等到我回来。
```

`while` 常强调两个持续动作同时进行：

```text
She cooked while I was cleaning.
我打扫卫生时，她在做饭。
```

几个连接词的重点不同：

```text
when       某时发生，可接短动作或长动作
while      在……期间，常接持续动作
as         随着；两个动作同时发展
before     在……之前
after      在……之后
since      自从，主句常用完成时
until      一直持续到某时
as soon as 一……就……
by the time 到……时候为止，主句常用完成时
```

```text
It has been five years since we met.
我们认识已经五年了。

By the time I arrived, the meeting had ended.
我到达时，会议已经结束了。
```

### 2. 原因状语从句

常见引导词：`because`、`since`、`as`、`now that`。

```text
I stayed home because I was sick.
我因为生病而待在家里。
```

`because` 通常直接、明确地回答 why；`since/as` 常表示双方已知或较明显的原因。

### 3. 条件状语从句

常见引导词：`if`、`unless`、`as long as`、`provided that`、`in case`。

```text
You will improve if you practise every day.
如果每天练习，你会进步。

You won't improve unless you practise.
除非练习，否则你不会进步。
```

`unless` 约等于 `if ... not`，不要再重复加否定。

区分真实条件和虚拟条件：

```text
If it rains tomorrow, we will stay home.
明天如果下雨，我们会待在家。（真实可能）

If it rained tomorrow, we would stay home.
明天要是真下雨，我们就会待在家。（说话者认为可能性较小）
```

`in case` 表示“以防”，不是普通的“如果”：

```text
Take an umbrella in case it rains.
带把伞，以防下雨。
```

### 4. 让步状语从句

常见引导词：`although`、`though`、`even though`、`even if`、`while`、`no matter + 疑问词`。

```text
Although it was raining, we went out.
虽然下雨了，我们还是出门了。
```

中文“虽然……但是……”在英语里通常不同时使用 `although` 和 `but`。

`even if` 强调假设，`even though` 强调已知事实：

```text
Even if it rains, we will go.       即使下雨（还不知道会不会下），我们也去。
Even though it was raining, we went. 尽管当时确实在下雨，我们还是去了。
```

`no matter + 疑问词` 可与 `疑问词 + -ever` 表达相近的让步意义：

```text
No matter what happens, stay calm.
Whatever happens, stay calm.
无论发生什么，都要保持冷静。
```

### 5. 目的状语从句与结果状语从句

```text
I spoke slowly so that everyone could understand me.
我说得很慢，以便每个人都能听懂。（目的）

I was so tired that I fell asleep at once.
我太累了，以至于立刻睡着了。（结果）
```

常用结构：

```text
so that + 完整句子
so + 形容词/副词 + that + 完整句子
such + (a/an) + 形容词 + 名词 + that + 完整句子
```

比较 `so` 和 `such`：

```text
It was so cold that the lake froze.
天气如此寒冷，以至于湖面结冰了。

It was such a cold day that the lake froze.
那是如此寒冷的一天，以至于湖面结冰了。
```

### 6. 比较与方式状语从句

```text
He is taller than I am.
他比我高。

Do as I told you.
照我告诉你的去做。
```

### 7. 地点状语从句

常由 `where`、`wherever` 引导，说明主句动作发生在哪里。

```text
Sit where you can see the screen.
坐在你能看见屏幕的地方。

Wherever she goes, her dog follows.
无论她去哪里，她的狗都跟着。
```

比较定语从句：

```text
Sit in the place where you can see the screen.
```

有先行词 `the place`，所以 `where...` 是定语从句；没有先行词、直接修饰 sit 时，是地点状语从句。

### 8. 状语从句的省略

当从句主语和主句主语相同，并且从句谓语含 `be` 时，常可省略“主语 + be”。

```text
While (she was) walking home, she called me.
回家途中，她给我打了电话。

If (it is) necessary, call the police.
必要时报警。

Though (he was) tired, he kept working.
尽管疲惫，他仍继续工作。
```

省略后，逻辑主语必须清楚，不能造成悬垂结构。

## 十九、主谓一致：主语决定谓语的单复数

### 1. 基本原则

```text
The boy is here.
The boys are here.

The boy likes music.
The boys like music.
```

真正需要明显变化的地方主要是 `be`，以及一般现在时实义动词的第三人称单数。

找主语时不要被中间的介词短语骗走：

```text
The colour of the walls is beautiful.
墙壁的颜色很漂亮。
```

主语中心词是单数 `colour`，不是离谓语更近的复数 `walls`。

### 2. and 连接主语

表示不同的人或物，通常用复数：

```text
Tom and Jack are friends.
```

若整体表示一个概念、一道菜或同一个人，可能用单数：

```text
Bread and butter is my usual breakfast.
面包加黄油是我通常的早餐。
```

若每个并列主语前都有 `each/every/no`，谓语通常用单数：

```text
Every boy and every girl has a ticket.
每个男孩和女孩都有票。
```

### 3. 就近原则

`either...or...`、`neither...nor...`、`not only...but also...` 连接主语时，谓语通常与最近的主语一致。

```text
Either you or he is responsible.
不是你就是他要负责。

Either he or you are responsible.
不是他就是你要负责。
```

### 4. 意义一致

表示时间、距离、金钱等的复数形式若被看成一个整体，谓语常用单数。

```text
Ten years is a long time.
十年是一段很长的时间。
```

书名、剧名、国家或组织名称即使形式像复数，也常作为一个整体：

```text
The United States is a large country.
"Gulliver's Travels" is a famous book.
```

有些以 `-s` 结尾的学科或疾病名通常按单数：`mathematics`、`physics`、`news`。

```text
The news is surprising.
```

### 5. 集合名词

集合名词要看强调整体还是成员。英式英语中尤其常见：

```text
The team is winning.       把团队看成整体
The team are arguing.      强调队员们各自在争论
```

`police`、`cattle` 等通常接复数谓语：`The police are investigating.`。

### 6. 不定代词作主语

`everyone`、`someone`、`anyone`、`nobody`、`each`、`either`、`neither` 等通常接单数谓语。

```text
Everyone is welcome.
Neither is correct.
```

`all/some/most/none + of` 的单复数取决于 `of` 后的名词：

```text
Some of the water is dirty.
Some of the students are absent.
```

### 7. 数量表达作主语

```text
A number of students are absent.  许多学生缺席。
The number of students is rising. 学生人数正在上升。
```

`a number of` 近似 many，中心意义是复数学生；`the number of` 的中心词是 number。

分数、百分数和 `half/part/rest + of` 的单复数也看 `of` 后面的名词：

```text
Two thirds of the work is finished.
Two thirds of the students are here.
```

### 8. 单复数取决于强调对象的结构

```text
More than one student has asked this question.
不止一名学生问过这个问题。（形式上按单数）

One and a half hours is enough.
一个半小时足够了。（看作一段时间）

The scissors are on the table.
剪刀在桌上。

This pair of scissors is new.
这把剪刀是新的。（中心词 pair）
```

### 9. 定语从句中的一致

关系词的单复数取决于先行词：

```text
She is one of the students who work hard.
她是那些努力学习的学生之一。
```

`who` 指 `students`，所以用 `work`。

比较强调结构：

```text
It is I who am responsible.       正式语法中 who 指 I
It is they who are responsible.   who 指 they
```

### 10. 主谓一致的判断顺序

1. 找到完整主语，圈出中心词。
2. 暂时划掉 `of...`、介词短语、定语从句和插入语。
3. 看是否有 `or/nor` 等需要就近一致的连接结构。
4. 判断主语表达一个整体还是多个成员。
5. 最后决定谓语单复数，不要只看离谓语最近的名词。

## 二十、直接引语和间接引语

### 1. 直接引语

原样引用说话内容：

```text
Tom said, "I am tired."
```

### 2. 间接引语

转述说话内容：

```text
Tom said that he was tired.
```

转换时常涉及：

- 人称变化：`I → he`
- 时态后移：`am → was`
- 时间地点变化：`now → then`、`today → that day`、`here → there`
- 疑问句改为陈述语序

常见时态后移：

| 直接引语 | 间接引语中常变为 |
| --- | --- |
| 一般现在时 | 一般过去时 |
| 现在进行时 | 过去进行时 |
| 一般过去时/现在完成时 | 过去完成时 |
| will | would |
| can | could |
| may | might |

```text
She said, "I am working."
She said that she was working.

He said, "I finished it."
He said that he had finished it.
```

常见时间、地点词变化要根据转述时的实际视角调整，而不是死背：

| 原说法 | 后来转述时可能变为 |
| --- | --- |
| now | then |
| today | that day |
| yesterday | the day before |
| tomorrow | the next/following day |
| last week | the week before |
| next week | the following week |
| here | there |
| this/these | that/those |

```text
She asked, "Where do you live?"
She asked where I lived.
```

一般疑问句用 `whether/if` 引导，不保留疑问语序：

```text
He asked, "Are you ready?"
He asked whether I was ready.
```

命令和请求常改成 `tell/ask + 人 + (not) to do`：

```text
The teacher said to us, "Open your books."
The teacher told us to open our books.

She said to me, "Don't be late."
She told me not to be late.
```

建议可根据意义选择 `suggest doing` 或 `suggest that...`：

```text
He said, "Let's take a break."
He suggested taking a break.
```

若转述的是客观真理，时态可不后移：

```text
The teacher said that the earth moves around the sun.
```

如果转述内容在转述时仍然为真，口语中也常保留原时态：

```text
Anna said that she lives in Beijing.
安娜说她住在北京。（转述时仍住在那里）
```

时态后移表达的是说话视角和时间距离，并不是每个场景都机械变换。

## 二十一、特殊结构：倒装、强调、省略和否定

### 1. 倒装

正常语序是主语在谓语前。为了语法或强调，把谓语全部或部分放到主语前，叫倒装。

一般疑问句就是最常见的部分倒装：

```text
Are you ready?
```

否定意义的副词或短语置于句首时，主句常部分倒装：

```text
Never have I seen such a view.
我从未见过这样的景色。

Only then did I understand.
直到那时我才明白。
```

地点词置于句首时，有时全部倒装：

```text
Here comes the bus.
公共汽车来了。
```

倒装分两类：

- **全部倒装**：整个谓语放到主语前，常见于地点/方向词置于句首。
- **部分倒装**：只把助动词、情态动词或 `be` 放到主语前，形式类似一般疑问句。

常见部分倒装触发结构：

```text
Never did he complain.                  他从不抱怨。
Not until midnight did she return.      直到午夜她才回来。
Only after the meeting did I understand. 会议结束后我才明白。
Not only did he apologize, but he also paid for the damage.
他不仅道歉了，还赔偿了损失。
```

`only` 修饰状语并位于句首时，主句倒装；若 `only` 修饰主语，则不倒装：

```text
Only then did I understand.  ✓
Only Tom understood.         ✓ 不倒装，因为 Only Tom 是主语
```

`so/neither/nor + 助动词 + 主语` 表示“……也一样”：

```text
I like coffee, and so does she.
我喜欢咖啡，她也喜欢。

I can't swim, and neither can he.
我不会游泳，他也不会。
```

“一……就……”的正式倒装：

```text
No sooner had I arrived than it started to rain.
Hardly had I arrived when it started to rain.
我刚到就下起雨来。
```

注意主语是代词时，`here/there` 开头的口语句通常不全部倒装：

```text
Here it comes.  它来了。
```

### 2. 强调句

结构：`It is/was + 被强调部分 + that/who + 其余部分`。

```text
Tom met Lucy in the park yesterday.

It was Tom who met Lucy in the park yesterday.       强调 Tom
It was Lucy that Tom met in the park yesterday.      强调 Lucy
It was in the park that Tom met Lucy yesterday.      强调地点
It was yesterday that Tom met Lucy in the park.      强调时间
```

检验方法：去掉 `It is/was` 和 `that/who` 后，剩余部分仍能还原成完整句子。

强调谓语动词时不能用上述强调句，而使用 `do/does/did + 动词原形`：

```text
I do understand you.
我的确理解你。

He did call me yesterday.
他昨天确实给我打了电话。
```

强调句与形式主语句不要混淆：

```text
It was yesterday that he left.  强调句；去掉框架可还原 He left yesterday.
It is clear that he left.        形式主语；that 从句是真正主语。
```

### 3. 省略

上下文清楚时，为避免重复可省去部分内容。

```text
I can play the guitar, and she can, too.
我会弹吉他，她也会。
```

第二个 `can` 后省略了 `play the guitar`。

```text
When necessary, call me.
必要时给我打电话。
```

这是 `When it is necessary` 的省略。

常见省略还有：

```text
She likes tea, but I don't.          省略 like tea
I haven't finished, but I hope to.  省略 finish
Tom is taller than Jack is.         省略 tall
If possible, finish it today.       省略 it is
```

并列结构中只能省略双方共享且不会引起歧义的部分。考试中先还原完整结构，再判断省略是否成立。

### 4. 否定

基本否定通常借助 `not`：

```text
She is not ready.
She does not know.
```

注意部分否定：

```text
Not everyone agreed.
并非所有人都同意。
```

这不等于 `No one agreed`（没有人同意）。

避免不符合标准英语的双重否定：

```text
I don't know anything.  ✓
I know nothing.         ✓
I don't know nothing.   ×（标准英语中会变成双重否定）
```

否定范围会改变句意：

```text
All students are not ready.  可能有歧义，常被理解为“并非所有学生都准备好了”。
Not all students are ready.  明确表示“并非所有学生都准备好了”。
No student is ready.         没有一名学生准备好。
```

`both...not` 通常表示部分否定，清楚的表达是 `not both`；完全否定两者使用 `neither`。

```text
Not both answers are correct.  并非两个答案都正确。
Neither answer is correct.     两个答案都不正确。
```

有些词形式上没有 `not`，意义却是否定：`never`、`hardly`、`seldom`、`little`、`few`、`without`、`unless`。

否定转移常见于 `think/believe/suppose/expect`：

```text
I don't think he will come.
我认为他不会来。
```

英语习惯把否定放在主句，实际否定意义落在从句的“会来”上。

## 二十二、情态动词和虚拟语气：表达态度与“非事实”

### 1. 常见情态动词

情态动词后接动词原形，没有第三人称单数 `-s`。

| 情态动词 | 常见含义 | 例句 |
| --- | --- | --- |
| can/could | 能力、可能、请求 | Can you help me? |
| may/might | 可能、许可 | It may rain. |
| must | 必须；有把握的推测 | You must stop. |
| have to | 客观上不得不 | I have to work. |
| should/ought to | 应该、建议 | You should rest. |
| will/would | 意愿、将来、礼貌请求 | Would you sit down? |

`mustn't` 是“禁止”，`don't have to` 是“不必”，两者完全不同：

```text
You mustn't park here.      禁止在此停车。
You don't have to come.     你不必来。
```

#### can、could 与 be able to

```text
She can swim.                 她会游泳。（现在能力）
She could swim at five.       她五岁时就会游泳。（过去的一般能力）
She was able to escape.       她成功逃脱了。（过去某次成功做到）
```

`could` 还可使请求更委婉：`Could you open the window?`。这里不是过去时。

#### may、might 与许可/可能

```text
May I come in?        我可以进来吗？（正式许可）
It may rain.          可能下雨。
It might rain.        也许下雨，语气通常更不确定。
```

表示许可时，否定回答宜用 `mustn't` 或 `can't`，因为 `may not` 也可能被理解成“可能不”。

#### must 与 have to

`must` 常带有说话者认为“必须”的态度；`have to` 常强调外部规定或现实需要。过去和将来的“不得不”通常用 `had to`、`will have to`。

```text
I must remember her birthday.   我一定要记住她的生日。
We have to wear uniforms.       我们按规定必须穿制服。
I had to leave early yesterday. 我昨天不得不早走。
```

#### should、ought to 与 had better

三者都可表达建议；`had better` 常暗示不照做会有不良结果，后接动词原形。

```text
You should see a doctor.
You ought to see a doctor.
You had better see a doctor.
```

`had better` 的否定是 `had better not do`。

#### need 与 dare

`need`、`dare` 既可作普通实义动词，也可在否定句和疑问句中作情态动词。

```text
You don't need to wait.  need 是实义动词
You needn't wait.        need 是情态动词
Does he dare to ask?     dare 是实义动词
Dare he ask?             dare 是情态动词，较正式
```

#### 情态动词表示推测

对现在情况的推测：

```text
He must be tired.       他一定累了。（把握很大）
He may/might be tired.  他可能累了。
He can't be tired.      他不可能累。（有把握的否定推测）
```

`mustn't` 不表示“不可能”，它表示“禁止”。

对过去情况的推测或评价，用“情态动词 + have + 过去分词”：

| 结构 | 常见意思 | 例句 |
| --- | --- | --- |
| must have done | 过去一定做了 | He must have forgotten. |
| may/might have done | 过去可能做了 | She may have left. |
| can't/couldn't have done | 过去不可能做了 | He can't have seen us. |
| should/ought to have done | 本来应该做却可能没做 | You should have called. |
| needn't have done | 本来没必要却做了 | You needn't have come. |
| could have done | 本来能够做却未必做了 | I could have helped. |
| would have done | 在某条件下本来会做 | I would have agreed. |

比较：

```text
I didn't need to buy food.  当时不需要买，可能买了也可能没买。
I needn't have bought food. 我买了，但后来发现没必要。
```

### 2. 什么是“语气”

语气表示说话者如何看待一件事：

- 陈述语气：把事情当事实陈述。
- 祈使语气：命令、请求或建议。
- 虚拟语气：谈假设、愿望、建议，尤其是与事实相反或尚未实现的情况。

### 3. 虚拟条件句

| 情况 | if 从句 | 主句 |
| --- | --- | --- |
| 与现在事实相反 | 一般过去时（be 常用 were） | would/could/might + 动词原形 |
| 与过去事实相反 | had + 过去分词 | would/could/might have + 过去分词 |
| 与将来可能性很小的情况相反 | should do / were to do / 一般过去时 | would/could/might + 动词原形 |

```text
If I were you, I would apologize.
如果我是你，我会道歉。（事实上我不是你）

If I had known, I would have helped.
如果我当时知道，我就会帮忙。（事实上当时不知道）
```

### 4. 错综时间条件句

如果条件发生在过去，但结果影响现在，从句和主句要各自选择合适的时间形式：

```text
If I had gone to bed earlier, I would not be tired now.
如果我昨晚早点睡，我现在就不会累。
```

`had gone` 指过去没有做到；`would not be` 指现在的相反结果。

### 5. 含蓄条件句

条件不一定由 `if` 明说，也可能藏在 `without`、`but for`、`otherwise` 或上下文里。

```text
Without your help, I would have failed.
没有你的帮助，我本来会失败。

I was busy; otherwise, I would have joined you.
我当时很忙，否则就会加入你们。
```

### 6. 省略 if 的虚拟倒装

正式文体可省略 `if`，把 `had`、`were` 或 `should` 移到主语前。

```text
Had I known, I would have helped.
= If I had known, I would have helped.

Were I you, I would wait.
= If I were you, I would wait.

Should you need help, call me.
= If you should need help, call me.
```

### 7. wish 后的虚拟语气

```text
I wish I were taller.          希望现在更高（与现在相反）
I wish I had studied harder.   希望过去更努力（对过去后悔）
I wish it would stop raining.  希望将来雨能停
```

### 8. 建议、要求类从句

`suggest`、`demand`、`insist`、`recommend` 等表示建议、要求时，后面的从句常用 `(should) + 动词原形`。

```text
The doctor suggested that he (should) rest.
医生建议他休息。
```

注意 `suggest` 表示“暗示”时不使用这套虚拟形式：

```text
His smile suggested that he was pleased.
他的微笑表明他很满意。
```

同类名词和形容词后的从句也常使用 `(should) do`：

```text
My suggestion is that we (should) start early.
我的建议是我们早点出发。

It is essential that every member (should) attend.
每位成员都参加非常重要。
```

### 9. would rather、It is time 与 as if

```text
I would rather you stayed here.
我宁愿你留在这里。（对现在/将来的愿望，用一般过去时）

I would rather you had told me earlier.
我宁愿你当时早点告诉我。（对过去的愿望）

It is time we went home.
我们该回家了。

He talks as if he knew everything.
他说得好像什么都知道似的。（实际并非如此）
```

如果 `as if/as though` 后说的事情很可能是真实的，也可以使用普通陈述语气：

```text
It looks as if it is going to rain.
看起来要下雨了。
```

## 二十三、构词法：看懂一个生词是怎样造出来的

构词法不是句子结构，但它能帮助你判断生词的词类和大致意思。

### 1. 前缀：通常改变词义

```text
happy → unhappy        un- 表示“不”
possible → impossible  im- 表示“不”
write → rewrite        re- 表示“重新”
understand → misunderstand  mis- 表示“错误地”
```

前缀通常不改变词类：`happy` 和 `unhappy` 都是形容词。

### 2. 后缀：常改变词类

```text
teach → teacher        -er 常构成人
happy → happiness      -ness 构成名词
care → careful         -ful 构成形容词
careful → carefully    -ly 构成副词
modern → modernize     -ize 构成动词
```

看到空格题时，可以先看句子需要哪种词类，再选择相应形式：

```text
She answered the question _____.
```

空格修饰动词 `answered`，需要副词，因此 `careful` 要变成 `carefully`。

### 3. 合成词与转化

两个词可组合成一个新词：

```text
tooth + brush → toothbrush
black + board → blackboard
part + time → part-time
```

同一个词不改变形式也能转换词类：

```text
email 名词：I sent an email.
email 动词：Please email me.

clean 形容词：The room is clean.
clean 动词：Please clean the room.
```

不能只凭外形判断词类，最终仍要看它在句中的位置和工作。

## 二十四、标点与大小写：让句子边界清楚

### 1. 句号、问号和感叹号

- 陈述句通常以句号结束。
- 直接疑问句用问号；间接疑问句不用问号。
- 强烈感情或命令可用感叹号，但正式写作不要滥用。

```text
Where is he?             直接问题
I wonder where he is.    间接问题，使用句号
```

### 2. 逗号

逗号常用于：

- 较长的句首状语从句后：`When I arrived, the meeting began.`
- 并列两个独立分句的连词前：`I called, but he did not answer.`
- 非限制性定语从句两侧：`Tom, who lives next door, is a doctor.`
- 插入语、同位语和列举：`My brother, however, disagreed.`

不要只用逗号连接两个完整句子，这叫逗号拼接：

```text
I was tired, I went home.        ×
I was tired, so I went home.     ✓
I was tired; I went home.        ✓
I was tired. I went home.        ✓
```

### 3. 分号和冒号

分号连接意义紧密的两个独立分句，或分隔内部已有逗号的复杂项目。

```text
The rain stopped; the sun came out.
雨停了；太阳出来了。
```

冒号用于引出解释、列举或结论；冒号前通常应是完整结构。

```text
She needs three things: time, money, and help.
```

### 4. 撇号和连字符

撇号用于所有格或缩写：

```text
Tom's book
the students' room
it's = it is / it has
```

`its` 是物主限定词，没有撇号：

```text
The dog moved its tail.
```

连字符常用于复合前置修饰语：`a ten-year-old child`。同样内容放在表语位置时通常不用连字符：`The child is ten years old.`。

### 5. 引号与大小写

直接引语使用引号，句首、专有名词、星期、月份、语言和国籍词首字母大写：

```text
Lucy said, "I will visit China in September."
```

普通季节名和学科名通常不大写：`spring`、`history`；语言名称大写：`English`。

## 二十五、怎样分析一个长句

遇到长句不要从第一个词开始逐字翻译。按下面的顺序拆：

1. 圈出所有有时态的谓语动词。
2. 找每个谓语对应的主语。
3. 用连词和关系词划分主句、从句。
4. 先保留主干，暂时拿掉定语、状语和插入语。
5. 判断从句在主句中担任什么成分。
6. 最后把修饰信息逐层放回去。

例句：

```text
The book that you gave me is useful because it explains grammar clearly.
```

第一步，找谓语：`gave`、`is`、`explains`。

第二步，划分结构：

```text
[The book (that you gave me)] is useful [because it explains grammar clearly].
```

- 主句：`The book is useful.`
- `that you gave me`：修饰 book，是定语从句。
- `because it explains grammar clearly`：说明 useful 的原因，是原因状语从句。

翻译时先译主干“这本书很有用”，再加两层信息：“你给我的这本书很有用，因为它把语法解释得很清楚。”

## 二十六、零基础最常见的十个错误

### 1. 一个句子没有谓语

```text
I very happy.     ×
I am very happy.  ✓
```

### 2. 两个谓语直接相撞

```text
I want learn English.     ×
I want to learn English.  ✓
```

### 3. 第三人称单数漏掉 -s

```text
He like coffee.   ×
He likes coffee.  ✓
```

### 4. 助动词后仍使用变化形式

```text
Does she likes it?  ×
Does she like it?   ✓
```

### 5. 形容词和副词混用

```text
He runs quick.      ×
He runs quickly.    ✓
```

### 6. 可数名词单数“裸奔”

```text
I bought book.    ×
I bought a book.  ✓
```

可数名词单数前通常需要冠词、物主代词、指示词等限定词。

### 7. 介词后误用主格

```text
This is for she.   ×
This is for her.   ✓
```

### 8. 从句仍用疑问语序

```text
I don't know where is he.  ×
I don't know where he is.  ✓
```

### 9. 中式连接词成双出现

```text
Although it rained, but we left.  ×
Although it rained, we left.      ✓
```

### 10. 只按中文逐词翻译

“我很喜欢它”不能写成 `I very like it.`。英语副词 `very` 通常不能直接修饰普通动词，应该说：

```text
I like it very much.
```

## 二十七、核心结构速查表

| 想表达什么 | 核心结构 |
| --- | --- |
| 主语做动作 | S + V (+ O) |
| 主语是什么/怎么样 | S + 系动词 + P |
| 某处有某物 | There + be + 主语 + 地点 |
| 正在做 | be + doing |
| 已经做 | have + done |
| 被做 | be + done |
| 能/必须/应该做 | 情态动词 + do |
| 想要做 | want + to do |
| 喜欢做 | enjoy + doing |
| 把一句话当名词 | that/whether/疑问词 + 陈述语序 |
| 用一句话修饰名词 | 先行词 + 关系词 + 定语从句 |
| 表达时间/原因/条件 | 从属连词 + 状语从句 |
| 与事实相反的现在假设 | If + 一般过去时, would + do |
| 与事实相反的过去假设 | If + had done, would have done |
| 强调某一成分 | It is/was + 强调部分 + that/who... |

看到英文术语时，可用下面这组白话对应：

| 术语 | 白话问题 |
| --- | --- |
| 主语 subject | 在说谁/什么？ |
| 谓语 predicate verb | 它做什么/处于什么状态？ |
| 宾语 object | 动作作用到谁/什么？ |
| 表语 predicative | 主语是谁/是什么样？ |
| 定语 attribute | 哪一个/什么样的名词？ |
| 状语 adverbial | 何时、何地、怎样、为什么、在什么条件下？ |
| 补语 complement | 对主语或宾语还要补充说明什么？ |
| 先行词 antecedent | 定语从句修饰的是哪个词？ |
| 限定动词 finite verb | 哪个动词承担时态和主谓变化？ |
| 非谓语 non-finite verb | 哪个动词不承担句子时态？ |

## 二十八、一套可执行的学习顺序

不要同时背所有语法。推荐分五轮：

### 第一轮：能造最短的正确句子

掌握词类、七种成分、五个基本句型、`be/do/have` 和一般现在时。目标是能判断：谁是主语，哪个是谓语，动词后缺不缺宾语或表语。

### 第二轮：能谈现在、过去和将来

掌握一般现在、现在进行、一般过去、过去进行、一般将来和现在完成时。每学一种时态，都同时练肯定、否定、一般疑问和特殊疑问。

### 第三轮：把名词短语说准确

掌握可数/不可数、单复数、冠词、代词、形容词、副词、数词和常用介词。

### 第四轮：把句子扩展开

掌握并列连词、非谓语动词和三大从句。每看到从句都问：“它在大句子里相当于名词、形容词，还是副词？”

### 第五轮：提升准确度和表达力

学习主谓一致、被动语态、间接引语、虚拟语气、倒装、强调、省略和否定。

每天可做一个“造句闭环”：

1. 选一个基本句型造肯定句。
2. 改成否定句。
3. 改成一般疑问句和特殊疑问句。
4. 换一个时态。
5. 加一个定语和一个状语。
6. 最后尝试加一个从句。

例如：

```text
She reads books.
She doesn't read books.
Does she read books?
What does she read?
She read a book yesterday.
The quiet girl read a book carefully in the library yesterday.
The quiet girl read a book that her teacher recommended.
```

## 二十九、综合练习

先自己完成，再看答案。

### 练习一：判断句子成分

分析下面句子的主干，并指出各部分对应的成分。

1. The little boy smiled happily.
2. My father gave me a useful book.
3. We found the test difficult.
4. The woman in the red coat is my teacher.
5. What he said surprised everyone.

### 练习二：改错

1. She go to school every day.
2. I am like music.
3. He asked me where did I live.
4. Because I was tired, so I went home.
5. The news are very important.
6. I look forward to meet you.

### 练习三：合并句子

1. I know the girl. The girl is singing.（用定语从句）
2. He was ill. He stayed home.（用 because）
3. I do not know. Will she come?（用 whether）
4. Work hard. You will succeed.（用 if）

### 练习四：选择正确的时态

用括号中动词的正确形式填空。

1. She usually _____ (walk) to work.
2. When I called, they _____ (have) dinner.
3. He _____ (live) here since 2020.
4. The train _____ already _____ (leave) before we arrived.
5. This time tomorrow, I _____ (take) an exam.
6. By next Friday, we _____ (finish) the project.
7. She was tired because she _____ (work) all morning.
8. If it _____ (rain) tomorrow, we will cancel the picnic.

### 练习五：语态与非谓语

1. The bridge _____ (build) in 1990.
2. The road _____ (repair) now.
3. He was made _____ (wait) outside.
4. She avoided _____ (answer) the question.
5. The girl _____ (stand) by the window is my sister.
6. The books _____ (write) by this author are popular.
7. _____ (finish) her homework, Lucy went to bed.
8. I need to get my computer _____ (repair).

### 练习六：选择合适的从句引导词

1. I know _____ she is worried, but I do not know _____ happened.
2. This is the house _____ I was born.
3. This is the house _____ we visited yesterday.
4. The student _____ notebook is missing should come here.
5. I am not sure _____ he will agree or not.
6. _____ it was raining, they continued playing.
7. You will miss the bus _____ you hurry.
8. The fact _____ the earth moves around the sun is well known.

### 练习七：中译英

1. 桌上有两本英语书。
2. 我到车站时，公共汽车已经开走了。
3. 你知道她为什么离开吗？
4. 站在门边的男孩是我的弟弟。
5. 如果我是你，我会接受这个建议。
6. 这就是我昨天告诉你的那本书。
7. 并非所有学生都理解这个问题。
8. 直到会议结束，我才明白他的意思。

## 三十、练习答案

### 练习一

1. `The little boy`（S）+ `smiled`（V）；`little` 是定语，`happily` 是方式状语。
2. `My father`（S）+ `gave`（V）+ `me`（间接宾语）+ `a useful book`（直接宾语）。
3. `We`（S）+ `found`（V）+ `the test`（O）+ `difficult`（宾补）。
4. `The woman in the red coat`（S）+ `is`（系动词）+ `my teacher`（P）；`in the red coat` 是后置定语，修饰 woman。
5. `What he said` 是主语从句，`surprised` 是谓语，`everyone` 是宾语。

### 练习二

```text
1. She goes to school every day.
2. I like music.
3. He asked me where I lived.
4. Because I was tired, I went home.
5. The news is very important.
6. I look forward to meeting you.
```

第 6 句中 `to` 是介词，不是不定式符号，所以后接动名词 `meeting`。

### 练习三

```text
1. I know the girl who is singing.
2. He stayed home because he was ill.
3. I do not know whether she will come.
4. If you work hard, you will succeed.
```

### 练习四

```text
1. walks
2. were having
3. has lived / has been living
4. had; left
5. will be taking
6. will have finished
7. had been working
8. rains
```

第 3 题如果强调“居住这一状态”，`has lived` 很自然；如果强调一直持续的过程，也可用 `has been living`。第 8 题是未来真实条件句，从句用一般现在时表示将来。

### 练习五

```text
1. was built
2. is being repaired
3. to wait
4. answering
5. standing
6. written
7. Having finished
8. repaired
```

- 第 3 题主动句 `make someone do` 变被动后恢复 `to`。
- 第 5 题女孩主动站着，用现在分词；第 6 题书是“被写”，用过去分词。
- 第 8 题使用 `get + 宾语 + 过去分词`，表示找别人修电脑。

### 练习六

```text
1. that; what
2. where
3. that/which（也可省略）
4. whose
5. whether
6. Although/Though/Even though
7. unless
8. that
```

第 2 题从句 `I was born` 缺地点状语，所以用 `where`；第 3 题 `visited` 缺宾语，所以用关系代词。第 8 题的从句解释 fact 的内容，`that` 不作成分，是同位语从句。

### 练习七

参考答案：

```text
1. There are two English books on the desk.
2. The bus had left when I arrived at the station.
3. Do you know why she left?
4. The boy standing by the door is my brother.
5. If I were you, I would accept this advice.
6. This is the book (that/which) I told you about yesterday.
7. Not all students understand the question.
8. Not until the meeting ended did I understand what he meant.
```

第 8 题把 `Not until...` 放到句首后，主句使用部分倒装；`what he meant` 是 `understand` 的宾语从句。

## 附录：原始 JSON 素材覆盖索引

为了便于回查，原始课程与本文章节的对应关系如下。这里按知识主题合并，而不是机械照搬课程顺序。

| JSON 范围 | 原素材重点 | 本文对应内容 |
| --- | --- | --- |
| `beginner/001`—`005` | 主系表、人称/指示代词、疑问句、句子成分 | 第二至五章、第十三章 |
| `beginner/006`—`011` | 名词、祈使句、There be、冠词、空间介词、情态动词 | 第四、八、十一、十三、二十二章 |
| `beginner/012`—`018` | 进行时、一般现在/将来、名词的数、不定代词、动词形式 | 第五、六、八、九章 |
| `beginner/019`—`025` | 形容词、时间介词、日期时刻、连词、数词 | 第八、十、十一、十二章 |
| `beginner/026`—`035` | 过去时、引语、副词、完成时、过去分词、感叹句、反意疑问句 | 第六、十、十三、二十章 |
| `beginner/036`—`045` | 比较等级、倒装、定语从句、完成进行时、简单句、时间从句、插入语 | 第三、四、六、十七、十八、二十一章 |
| `beginner/046`—`050` | 条件从句、宾语从句、被动语态、主谓一致 | 第七、十六、十八、十九章 |
| `intermediate/001`—`004` | 复杂主谓一致、被动与系表区别、被动特殊规则 | 第七、十九章 |
| `intermediate/005`—`010` | 时间、原因、条件、目的和结果状语从句 | 第十八章 |
| `intermediate/011`—`018` | 过去完成时、引语转换、虚拟条件、情态动词、动名词、被动转换 | 第六、七、十四、二十、二十二章 |
| `intermediate/019`—`027` | 时间/地点介词、形容词、副词、助动词、半助动词 | 第五、十、十一章 |
| `intermediate/028`—`037` | 非谓语、语气、错综和含蓄虚拟、名词性从句中的虚拟 | 第十四、二十二章 |
| `intermediate/038`—`050` | 名词性从句、定语从句、状语从句 | 第十五至十八章 |
| `intermediate/051`—`059` | 主谓一致、倒装、There be、强调、省略、否定 | 第四、十九、二十一章 |
| `intermediate/060`—`070` | 十一组语法综合测试 | 第二十九、三十章的分级练习与解析 |

个别 JSON 的正文没有独立“语法点拨”，但视频标题仍标注了语法主题，例如过去完成时、条件状语从句时态、引语转换和被动转换；这些内容也已经纳入对应章节。

## 结语：语法是结构，不是术语比赛

“定语”“状语”“宾补”这些名称本身并不难，它们只是给不同工作岗位起的名字：

- 围着名词、回答“哪一个/什么样”的，是定语。
- 围着动作或整句、回答“何时/何地/怎样/为什么”的，是状语。
- 跟在系动词后说明主语的，是表语。
- 跟在宾语后继续说明宾语的，是宾补。

真正有效的学习方式不是孤立背定义，而是每学一个结构就做三件事：**看懂公式、拆解例句、自己造句。** 当你能迅速找到一个句子的主语和谓语，语法这张地图就已经有了坐标；后面的时态、非谓语和从句，只是在这副骨架上继续增加更精确的信息。
