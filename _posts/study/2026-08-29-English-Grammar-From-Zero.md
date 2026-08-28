---
layout: post
title: "英语语法零基础教程：从句子骨架到三大从句"
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
date: 2026-08-29 12:00:00 +0800
archived:
layoutclear:
---

英语语法并不是一大堆互不相干的规则。它真正研究的只有一件事：**单词怎样组合，才能把“谁、做什么、怎么样、在何时何地、为什么”说清楚。**

这篇文章按零基础学习者最容易理解的顺序，把词类、句子成分、基本句型、时态、语态、非谓语动词和三大从句串成一张完整地图。第一次阅读不必背完，先看懂结构，再回头记细节。

> 本文根据 `wordtap_web/public/shuimu` 中标题或正文含“语法”的 JSON 课程整理。素材共涉及入门课程 `beginner/001.json`—`050.json`，以及中级课程中的主谓一致、语态、非谓语、虚拟语气、三大从句和特殊句式等内容。原课程按课次讲解，本文改为按知识依赖关系重新组织，并补充了术语解释、结构公式和例句分析。

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

## 六、时态：时间 + 动作状态

“时态”最好拆成两部分理解：

- **时间**：现在、过去、将来。
- **状态（体）**：一般、进行、完成、完成进行。

零基础先掌握下列八种最常用形式。

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

### 9. 时间和条件状语从句中的“主将从现”

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

### 2. 名词复数

常规变化：

- 多数词加 `-s`：`book → books`
- 以 `s/x/ch/sh` 等结尾加 `-es`：`box → boxes`
- 辅音字母 + `y`：`city → cities`
- 部分 `f/fe` 变 `ves`：`knife → knives`

常见不规则形式：`man → men`、`child → children`、`mouse → mice`。它们需要单独积累。

### 3. 不定冠词 a/an

`a/an` 表示“一个、某个”，只能放在可数名词单数前。

- `a` 用在辅音音素前：`a university`（开头读 /j/）。
- `an` 用在元音音素前：`an hour`（`h` 不发音）。

判断依据是**发音**，不是字母。

### 4. 定冠词 the

`the` 表示说话双方都知道、前文提过或独一无二的对象。

```text
I saw a dog. The dog was very friendly.
我看到一只狗。那只狗很友善。
```

第一次出现、不确定是哪只，用 `a dog`；第二次已明确，用 `the dog`。

### 5. 零冠词

泛指复数名词和不可数名词时，常不用冠词：

```text
Dogs are friendly.  狗通常很友善。
Water is important. 水很重要。
```

### 6. 基数词和序数词

- 基数词回答“多少”：`one, two, twenty-one, one hundred`。
- 序数词回答“第几”：`first, second, third, fourth`。

```text
There are three rooms.      有三个房间。
My room is on the third floor. 我的房间在三楼。
```

年份常分成两段读，日期常用序数词：`August 29th, 2026`。

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

### 3. 比较级和最高级

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

### 4. 常见副词位置

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

## 十四、非谓语动词：动词不当“句子发动机”时

一个简单句原则上只有一套核心谓语。另一个动作若不通过连词组成从句，通常要变成非谓语形式。

```text
I want go home.       × 两个动词直接相撞
I want to go home.    ✓ want 是谓语，to go 是非谓语
```

非谓语有三大类：不定式、动名词和分词。

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

### 4. doing 和 to do 的常见意义差别

```text
I stopped smoking.     我戒烟了。（停止这件事）
I stopped to smoke.    我停下来去抽烟。（停下别的事，目的是抽烟）

I remember locking the door.  我记得锁过门。（回忆过去）
Remember to lock the door.     记得去锁门。（动作尚未做）
```

具体接 `doing` 还是 `to do`，仍需按动词搭配积累。

## 十五、从句：把一个小句子放进大句子

从句内部通常有“主语 + 谓语”，但它在大句子里只担任一个成分。

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

### 4. 限制性与非限制性定语从句

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

### 5. 定语从句与同位语从句的区别

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

### 4. 让步状语从句

常见引导词：`although`、`though`、`even though`、`even if`、`while`、`no matter + 疑问词`。

```text
Although it was raining, we went out.
虽然下雨了，我们还是出门了。
```

中文“虽然……但是……”在英语里通常不同时使用 `although` 和 `but`。

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

### 6. 比较与方式状语从句

```text
He is taller than I am.
他比我高。

Do as I told you.
照我告诉你的去做。
```

## 十九、主谓一致：主语决定谓语的单复数

### 1. 基本原则

```text
The boy is here.
The boys are here.

The boy likes music.
The boys like music.
```

真正需要明显变化的地方主要是 `be`，以及一般现在时实义动词的第三人称单数。

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

### 5. 集合名词

集合名词要看强调整体还是成员。英式英语中尤其常见：

```text
The team is winning.       把团队看成整体
The team are arguing.      强调队员们各自在争论
```

`police`、`cattle` 等通常接复数谓语：`The police are investigating.`。

### 6. 定语从句中的一致

关系词的单复数取决于先行词：

```text
She is one of the students who work hard.
她是那些努力学习的学生之一。
```

`who` 指 `students`，所以用 `work`。

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

```text
She asked, "Where do you live?"
She asked where I lived.
```

若转述的是客观真理，时态可不后移：

```text
The teacher said that the earth moves around the sun.
```

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

### 4. wish 后的虚拟语气

```text
I wish I were taller.          希望现在更高（与现在相反）
I wish I had studied harder.   希望过去更努力（对过去后悔）
I wish it would stop raining.  希望将来雨能停
```

### 5. 建议、要求类从句

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

## 二十三、怎样分析一个长句

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

## 二十四、零基础最常见的十个错误

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

## 二十五、一套可执行的学习顺序

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

## 二十六、综合练习

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

## 二十七、练习答案

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

## 结语：语法是结构，不是术语比赛

“定语”“状语”“宾补”这些名称本身并不难，它们只是给不同工作岗位起的名字：

- 围着名词、回答“哪一个/什么样”的，是定语。
- 围着动作或整句、回答“何时/何地/怎样/为什么”的，是状语。
- 跟在系动词后说明主语的，是表语。
- 跟在宾语后继续说明宾语的，是宾补。

真正有效的学习方式不是孤立背定义，而是每学一个结构就做三件事：**看懂公式、拆解例句、自己造句。** 当你能迅速找到一个句子的主语和谓语，语法这张地图就已经有了坐标；后面的时态、非谓语和从句，只是在这副骨架上继续增加更精确的信息。
