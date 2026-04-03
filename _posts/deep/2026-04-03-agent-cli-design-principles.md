---
layout: post
title: "机器学习笔记 -- 给 Agent 设计 CLI 的原则"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习", "机器人"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
cluster:
---

[给 Agent 设计 CLI 的十个原则 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/H-hggbJAMBTuambCzNE4OQ)
[Google 官方发了 7 条 CLI 设计原则，我读完发现我们都忽略了一种新用户 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/HX24WCFcP7SLptn-RYvcBg)
[Agent 时代的 CLI 设计哲学探讨 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/dLRjlcDPp5JeXkxid0sSzg)


## 给 Agent 设计 CLI 的十个原则

[来源 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/H-hggbJAMBTuambCzNE4OQ)


### Agent 怎么想的

LLM 训练数据里有大量 shell 命令和 bash 脚本（GitHub 代码约占 5%、Stack Overflow 约占 2%），Agent 天生对命令行有相当的「直觉」。

但这个直觉有边界。Berkeley 的 BFCL V4 Leaderboard 显示，即使排名第一的模型，在复杂的多步工具调用场景下准确率也达不到 100%。SWE-bench 数据更直观：当前最强模型也只能解决约七成编码任务。

模型能力仍在飞速进步，但使用 CLI 的方式没变：跑 `--help` 、解析输出、拼命令、看退出码。模型越强，每一步判断越准 —— 但 CLI 本身设计不好，再强的模型也会掉进同样的坑。

Surge AI 有一个案例：让前沿模型处理只需改 2 行代码的问题，它走了 39 轮对话、改了 693 行代码，最终失败。原因是第一步就幻觉出了不存在的类名，然后在错误基础上越陷越深，连续 22 轮坚持「核心逻辑是对的」。而另一个模型遇到同样问题，发现文件被截断后主动要求重新读取，确认完整内容才动手，一次解决。

好的 CLI 设计，就是帮 Agent 做这个区分：减少它需要猜的东西，增加它能验证的东西。


### Agent 的弱点

- **大小写敏感短参数** ：`grep -a` / `-A` 、 `ssh -v` / `-V` 含义完全不同；Agent 基于概率选择，两个 token 概率接近时选错风险高
- **交互式提示** ：`Are you sure? [y/N]` 对 Agent 是一堵墙（2019 年 AWS CLI v2 改默认 pager 为 `less` ，导致全球数千 CI 任务挂起）
- **幻觉参数** ：Agent 会自信地使用不存在的参数；你的 CLI 不能假设只有最强模型才来调用它
- **非结构化输出** ：人类可读的 table 输出对 Agent 来说靠猜


### 原则一：名词在前（noun-verb）

```bash
# 好：docker container ls / gh pr create / lark-cli calendar +agenda
# 不好：create-pr / delete-image / search-user
```

Agent 发现命令的过程是 **树搜索** ：`mytool --help` → 看到名词 → `mytool user --help` → 看到动词。每一步有 `--help` 可查，确定性缩小范围。verb-noun 结构把所有操作平铺一层，无层级引导。

Docker 是典范：`container` / `image` / `volume` 是名词， `ls` / `rm` / `create` 是动词，Agent 学会 `docker container ls` 就能推断 `docker volume ls` 。


### 原则二：长参数优先

所有参数都应有长格式（ `--verbose` ），短格式（ `-v` ）作为可选的人类便利。

- `--dry-run` 具备自描述能力； `-n` 在不同工具中可能是 `--line-number` 、 `--numeric` 、 `--no-action`
- `--verbose` 和 `--version` 不会混淆； `-v` / `-V` 一字之差意义迥异
- LLM 见过海量 `--output` ，语义绑定强； `-o` 的语义绑定弱得多

钉钉 CLI 的 `--yes` 参数描述是『跳过确认提示（AI Agent 模式）』 —— 参数名本身就是自描述的，Agent 一看就知道该在什么时候加它。


### 原则三：输出是契约

`stdout` 输出 JSON 数据， `stderr` 输出状态信息， **严格分流** 。

结构化输出一旦发布即为 API。Kubernetes v1.14 弃用 `--export` ，v1.18 正式移除，导致数千 Helm chart 和 CI/CD 管道崩溃。 **加新的可选字段安全，改变已有字段类型或名称就是破坏性变更。**

GitHub CLI 在这方面做得趄庞：检测到输出被管道传输时，自动切换为 tab 分隔格式，去掉颜色转义符，文本不截断。飞书 CLI 支持 JSON、NDJSON、table、CSV、pretty 五种格式。


### 原则四：感知环境

检测 TTY 还是 pipe，自动调整行为。非 TTY 下默认输出 JSON，不该要求 Agent 额外加 `--json` flag。钉钉 CLI 的 `--yes` 参数就专门为此设计：跳过所有确认提示，进入 AI Agent 模式。

gcloud 文档里有一条建议值得所有 CLI 开发者记住：「不要依赖 gcloud 的原始输出格式，永远使用 `--format` 标志。」因为原始输出格式可能随版本变化。


### 原则五：干跑优先

每个有副作用的命令支持 `--dry-run` ，给 Agent 探索-验证的反馈循环。好的输出是结构化 JSON diff，告诉 Agent 什么会被创建、修改或删除。

飞书的实现更细致：干跑时会输出完整的请求 URL、方法、参数，Agent 可以在执行前确认请求的正确性。Lightning Labs 的设计更进一步：`--dry-run` 使用专门的退出码（exit code 10），这样 Agent 可以通过退出码区分「干跑成功」和「真正执行成功」。


### 原则六：退出码控制

| 退出码 | 含义 | Agent 应对 |
|--------|------|-----------|
| 0 | 成功 | 继续执行 |
| 1 | 一般错误 | 读 stderr 诊断 |
| 2 | 参数错误 | 修正参数重试 |
| 3 | 资源不存在 | 跳过或创建 |
| 4 | 权限不足 | 提示用户授权 |
| 5 | 冲突 / 已存在 | 跳过或更新 |

退出码一旦发布即为契约，不可随意修改。


### 原则七：防住幻觉

- **严格输入验证** ：验证 URL（拒绝 `javascript:` 、 `file:` 协议）、域名、输出路径（拒绝写入 `.ssh/` 、 `.gnupg/` ）
- **枚举约束** ：`--format json|table|csv` 比 `--format <string>` 安全得多
- **schema 自省** ：`mytool schema --all` 输出完整命令树 JSON；飞书 CLI 已实现 `lark-cli schema calendar.events.list`
- schema 应按需查询 —— GitHub MCP 服务器一次注入 55,000 tokens，CLI 让 Agent 按需跑 `--help`


### 原则八：幂等设计

```bash
# 命令式：资源已存在会报错
mytool user create --name "john"
# 声明式：无论调用多少次，结果一致
mytool user ensure --name "john"
# 或
 mytool user create --name "john" --if-not-exists
```

Agent 会重试（网络超时、结果不确定、任务中断恢复……）。 `kubectl apply` 是声明式设计的教科书。飞书 CLI 的 `+messages-send` 支持 `--idempotency-key` 参数：Agent 传入一个唯一标识符，即使命令被重复执行，服务端也只会处理一次。


### 原则九：错误即指南

```json
{
  "error": "permission_denied",
  "message": "缺少 calendar:read 权限",
  "suggestion": "运行 lark-cli auth login --domain calendar 授权",
  "retryable": false
}
```

错误信息四要素： **错误类型** （机器可读）、 **描述** （发生了什么）、 **修复建议** （怎么解决）、 **是否可重试** 。


### 原则十：帮助即大脑

Anthropic 发现「描述是影响工具使用准确率的最关键因素」 —— 仅通过优化工具描述就在 SWE-bench 上大幅降低错误率。

好的 `--help` ：以 2-3 个示例开头；明确标注必需 / 可选参数；参数描述含值域（ `--format json|table|csv` ）；50 行以内。


### Checklist

```
[ ] noun-verb 层级命令结构，支持树搜索
[ ] 所有参数有长格式，短格式可选
[ ] stdout 输出 JSON，stderr 输出状态信息
[ ] 非 TTY 自动调整输出（默认 JSON）
[ ] 副作用操作支持 --dry-run，输出结构化 diff
[ ] 退出码有细粒度语义文档
[ ] 参数枚举约束，输入严格验证
[ ] 支持 schema 自省命令
[ ] 关键操作幂等或支持 --if-not-exists
[ ] 错误信息含类型、描述、修复建议、可重试标志
[ ] --help 示例开头，标注必需 / 可选，50 行内
[ ] --yes / --no-interactive 跳过所有交互提示
```

开源参考：[agent-cli-guide {% include relref_github.html %}](https://github.com/Johnixr/agent-cli-guide)（GUIDE.md + CHECKLIST.md，可直接丢给 Coding Agent 使用）


### 给飞书和钉钉打个分

用这十条原则对照钉钉和飞书 CLI：

**飞书做得好的：** noun-verb 结构清晰，三层架构让 Agent 按需选择抽象层级，schema 命令提供完整 API 自省，五种输出格式，按域申请权限（最小权限原则），权限不足时自动提示修复方案。

**飞书可以改进的：** 非 TTY 下没有自动切 JSON，退出码没有文档化的细粒度语义， `--idempotency-key` 应该更广泛使用。

**钉钉做得好的：** `--yes` （AI Agent 模式）语义自描述， `--mock` 参数方便调试，帮助文本全中文（对中文 LLM 更友好），批量熔断防 Agent 失控。

**钉钉可以改进的：** 命令只有两层，缺少 shortcut 快捷层；没有 schema 自省命令；输出格式只有三种；帮助文本缺少使用示例。

---


## Google 官方发了 7 条 CLI 设计原则，我读完发现我们都忽略了一种新用户

[来源 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/HX24WCFcP7SLptn-RYvcBg)

Google Cloud 发了一篇技术文章："10 分钟构建一个同时服务 AI Agent 和人类的 CLI"。它在讲一件比 "CLI 怎么写 "重要得多的事：

**我们正在进入一个软件需要同时服务两种用户的时代 —— 人类和机器。**

> 今年写的每一个 CLI，某个时刻都会被 Agent 调用。大多数 CLI 还没准备好。

交互式确认弹窗、彩色终端输出、进度条动画、" 你确定吗？(Y/n)" —— 对人类是友好体验，对 Agent 是灾难。


### 核心思路：把数据和呈现解耦

> 把数据和呈现分离（Decouple the data from the presentation）。

CLI 内部只做一件事 —— 生成数据。呈现层是可插拔的客户端。

```bash
# 人类得到交互式 TUI
a2acli watch --task abc123

# Agent 得到结构化 NDJSON
a2acli watch --task abc123 --no-tui
```

不需要维护两套代码库。状态由后端服务管理，CLI 只是轻量传输层。Agent 通过读取 `skills/SKILL.md` 学习如何使用这个 CLI。


### 原则一：可发现性 —— 帮 Agent 找到入口

人类会随机探索、看错误信息、Google、问同事。Agent 只能从你提供的信息里推断该怎么做。

- **按功能分组，不按字母排序。** Agent 扫描的是结构，不是字母表
- **显式标注入口点。** help 描述里加 "(start here)" 或 "(typical first step)"
- **每个命令三个字段：** 短描述、长描述（是什么 / 为什么 / 与类似命令的区别）、示例（3-5 个可直接复制粘贴的）

> 示例比描述更重要。Agent 会解析示例来推断 flag 的用法。

建议在仓库根目录放 `AGENTS.md` ，显式定义 AI 开发者的交互规则、默认工作流和架构标准。


### 原则二：Agent 优先的互操作性

- 每个产生数据的命令支持 `--json` 或 `--no-tui` flag
- 支持 `NO_COLOR` 和 `[APP]_NO_TUI` 环境变量
- `stdout` 被 pipe 时自动跳过所有交互元素
- 输出必须是合法 JSON 或 NDJSON，不能混入日志
- 非 TTY 模式下不能有交互式提示

**保护 Agent 的上下文窗口：** 默认截断大文本块、脱敏敏感信息；需要完整数据时要求显式加 `--full` 或 `--verbose` 。

**CLI 必须是无状态的：** 用引用 ID（如 `--task <ID>` ）来操作，让后端服务管理长时运行的上下文。Agent 调用 CLI 不是在开启一段对话，而是在执行一个操作。


### 原则三：配置优先级

`CLI Flag > 环境变量 > 配置文件 > 默认值`

Agent 不需要知道 URL 和 token，只需传 `--env prod` ，CLI 自己去找对应配置。


### 原则四：错误要给出解决路径

```
Error: database not initialized
Hint: run 'a2acli init' to create the local database
```

每条错误信息后加 `Hint:` ，Agent 可以解析来自我纠正。 **尽早失败（Fail fast）** ：在执行重逻辑之前先验证配置和连接，不要让 Agent 等 30 秒之后才发现 token 不对。


### 原则五：Flag 一致性

同一个缩写在所有命令里必须代表同一个意思。不一致的 Flag 会破坏 Agent 的推理 —— 它在一个命令里学到的规律不能用在其他命令上。

**默认行为永远应该是最安全、最常见的路径。** 破坏性操作必须要求显式 Flag 才能触发。


### 原则六：终端的视觉设计

用 "语义色彩 token" 而非直接用颜色名称：定义 `Pass` token 对应绿色（成功）、 `Warn` 对应黄色（警告 / 进行中）、 `Error` 对应红色（失败）、 `Meta` 对应灰色（元数据）。

**不要给描述文字和帮助文本上色。** 过度上色等于什么都没强调，用空白和对齐表达层级更有效。


### 原则七：版本管理与生命周期

- `--version` 要能用，重要更新时主动提示
- **优雅处理 SIGINT（Ctrl+C）** ：不能出现数据损坏，Agent 可能在任何时刻被上层系统打断
- **写操作记录操作者** ：从 `git config user.name` 或 `$USER` 获取身份并记录，在多 Agent 协作场景下审计追溯越来越重要


### 设计范式转变

在软件工程的历史上，我们设计过面向人类的界面（GUI、CLI、Web UI），也设计过面向机器的接口（API、消息队列、数据库连接）。但我们 **从来没有认真设计过 "同时面向人类和机器 "的接口** 。

这篇文章真正在做的事，是给这个新问题提供一套工程解法 —— 同一个入口，根据调用者的身份自动切换呈现方式，同时保证数据层的一致性。

> 2026 年最好的 CLI，不是终端界面最漂亮的那些，而是当人类输入命令和当 Agent 编程调用时，同样运行良好的那些。

这不只是 CLI 的问题 —— 随着 Agent 介入各种工具链，SDK、API、内部平台工具迟早都会被 Agent 调用。"对人类友好 "和 "对 Agent 可用 "将成为每个工具都必须同时满足的要求。

原文：[Build a CLI for AI agents & humans in less than 10 mins](https://cloud.google.com/blog/products/application-development/build-a-cli-for-ai-agents-and-humans)（Google Cloud 官方）


## Agent 时代的 CLI 设计哲学探讨

[来源 {% include relref_weixin.html %}](https://mp.weixin.qq.com/s/dLRjlcDPp5JeXkxid0sSzg)

CLI-Anything 最近很火 —— 它用 AI Agent 自动为 GIMP、Blender、Audacity 等 GUI 软件生成命令行工具，号称要构建 "Agent-Native Software Ecosystem"。

但我们花了一个晚上拆解它的代码后，得出了一个不太客气的结论： **CLI-Anything 生成的 CLI 是给人用的，不是给 Agent 用的。**

更重要的是，在拆解过程中，我们推导出了一套 Agent 时代的 CLI 设计哲学 —— 五条原则，每条都有代码级的实证支撑。


### 传统 Unix 哲学回顾

- **Do one thing well** — `grep` 只搜索， `sort` 只排序
- **Pipe 组合** — `grep | sort | uniq` ，简单工具组合出复杂能力
- **Text is the universal interface** — 一切皆文本流
- **Silent on success** — 成功不废话，exit code 0
- **No captive user interface** — 不要把用户锁在交互式界面里
- **行为可预测** — 相同输入，相同输出
- **幂等性** — 重复执行应安全

精髓：一个好的 CLI 工具不是一个应用程序，而是一个 **积木块** 。


### 哪些没变，哪些变了

**依然成立：** Do one thing well、行为可预测（对 Agent 甚至比对人类更重要）、幂等性（Agent 会重试）。

**根本变化：** CLI 的消费者从人类变成了 LLM Agent。两者的差异不在于 "模型够不够聪明" —— 当前旗舰模型的 CLI 使用能力已和资深程序员相当。差异在于 **Agent 消费 CLI 输出的架构方式** ：

- 人类有很高的视觉带宽；Agent 的上下文窗口是有限的共享资源
- 人类通过管道组合工具，数据不经过大脑；Agent 通过推理循环组合 —— 每条命令输出都要进入上下文、被理解、被推理
- 人类多敲一条命令几乎零成本；Agent 多一轮调用就是一次完整的推理循环


### 原则一：上下文经济性

每轮 CLI 调用消耗的 token 要尽可能少，信息密度要尽可能高。

```bash
# 人类友好的输出（~45 tokens）
╭──────────────────────────────────╮
│  ✓ 3 layers in project           │
│  0: Background (solid)           │
│  1: Photo (image, 80%)           │
│  2: Title (text)                 │
╰──────────────────────────────────╯

# Agent 友好的输出（~25 tokens，信息量相同）
[{"i":0,"name":"Background","type":"solid"},
 {"i":1,"name":"Photo","type":"image","opacity":0.8},
 {"i":2,"name":"Title","type":"text"}]
```

token 消耗减少约 45%。单次差异不大，但复杂任务可能调用数十次 CLI，差异累积显著。

**设计含义：**
- 默认输出 JSON，而非格式化的人类可读文本
- 不附带装饰性内容（emoji、边框、banner、空行）
- 对可能返回大量数据的命令（list、log），默认限制输出量


### 原则二：调用经济性

完成一个任务所需的 CLI 调用轮次要尽可能少。

```bash
# 需要两轮调用（多一轮查询确认）
$ cli-anything-gimp layer move 2 --to 0
{"status": "ok"}
$ cli-anything-gimp layer list   # Agent 还得再调一次确认结果

# 只需一轮调用（操作 + 结果状态一起返回）
$ cli-anything-gimp layer move 2 --to 0
{"moved":2,"to":0,"current_order":["Title","Background","Photo"]}
```

**设计含义：**
- 每个状态变更命令，返回中包含操作后的关键状态
- 避免 "先执行、再查询 "两步才能完成的操作模式
- 不需要返回全部状态，只需返回与本次操作相关的状态变化


### 原则三：Cache 友好性

CLI 输出在状态未变时，应保持字面完全一致，以利于 LLM 推理的 prompt cache 命中。

很多 Agent 框架在组装每轮上下文时会将工具状态重新注入到上下文中间。如果这部分输出带时间戳，每轮都不同，从该插入点开始后面全部 cache miss。

```json
// 带时间戳 → 每轮都不同 → 从此点开始 cache miss
{"name":"my_project","layers":3,"last_modified":"2026-03-15T21:35:11Z"}

// 纯结构状态 → 项目没变就字面一致 → cache 命中
{"name":"my_project","layers":3}
```

**设计含义：**
- 避免在输出中包含不必要的易变数据（时间戳、随机 ID、进程号）
- 同一状态的查询命令，返回字节序列应完全一致（字段顺序固定、无随机性）
- 只在用户显式请求时才包含易变元数据


### 原则四：模型友好性

CLI 的设计应尽量贴合训练数据中大量存在的 CLI 范式，降低模型幻觉概率。

```bash
# 非标准 → 模型会幻觉出 --json（训练数据中更常见）
$ mytool export --machine-readable
# 标准 → 贴合高频模式，模型不会猜错
$ mytool export --json

# 非标准子命令 → 模型可能猜测为 "mytool layer list"
$ mytool do --action=list --type=layer
# 标准子命令 → 和 git/docker/kubectl 一致，模型一次调对
$ mytool layer list
```

**Convention over creativity — 在 Agent 时代，遵循约定比追求独特更重要。**

设计含义：
- Flag 命名遵循业界惯例（ `--json` 、 `--output` 、 `--verbose` 、 `--quiet` ）
- 子命令结构贴合主流范式（ `tool <noun> <verb>` 或 `tool <verb> <noun>` ）
- 使用主流 CLI 框架（Python Click、Node Commander）生成标准的 `--help` 格式


### 原则五：Skill-CLI 责任边界

确定性的可重复模式封装到 CLI 中；创意性的、依赖上下文的编排交给 Skill 引导 Agent 完成。

Agent 时代的工具链是 `Agent → Skill → CLI` 三层结构：
- 逻辑放在 CLI 里 → 执行确定性强、鲁棒，但不灵活
- 逻辑放在 Skill 里由 Agent 编排 → 灵活性高，但概率性的、可能出错

```bash
# 适合封装到 CLI：确定性的批量操作
cli-anything-gimp batch convert --input "*.png" --format webp --quality 80
# 如果让 Agent 编排：每张图 3 轮调用 × 100 张 = 300 轮推理循环

# 适合 Skill + Agent 编排：创意性的、依赖上下文的任务
# Skill 指导 Agent：先建项目 → 根据图片内容选择构图 → 加文字 → 调色 → 导出
cli-anything-gimp project new --width 1080 --height 1080
cli-anything-gimp layer add-from-file photo.jpg
cli-anything-gimp filter add brightness -l 0 -p factor=1.3  # Agent 根据图片亮度决定参数
cli-anything-gimp draw text --text "Hello" --size 48         # Agent 根据内容决定文案
cli-anything-gimp export render post.png
```

**经验法则：如果一个流程每次执行步骤都一样 → CLI；如果步骤取决于上下文 → Skill + Agent。**


### 五条原则总览

| 原则 | 优化目标 | 类别 | 根因 |
|------|---------|------|------|
| 上下文经济性 | 每轮 token 量 | 效率 | 上下文窗口是有限共享资源 |
| 调用经济性 | 任务总轮次 | 效率 | 每轮推理循环有成本 |
| Cache 友好性 | 单 token 推理成本 | 效率 | Prompt cache 按前缀匹配 |
| 模型友好性 | 调用正确率 | 可靠性 | 模型基于训练数据做概率预测 |
| Skill-CLI 责任边界 | 鲁棒性与灵活性平衡 | 架构 | Agent 编排是概率性的，CLI 执行是确定性的 |

前三条优化 **效率** ，第四条优化 **可靠性** ，第五条优化 **架构合理性** 。


### CLI-Anything 对照评估

用五条原则对照 CLI-Anything 生成的 GIMP CLI：

- **上下文经济性 ❌** — 默认输出人类格式，JSON 只是 opt-in；项目有 499 行的 `repl_skin.py` ，全是边框、emoji、彩色字符 —— Agent 不需要任何一行
- **调用经济性 ⚠️** — `layer move` 只返回 `{"moved":2, "to":0}` ，不返回新排列顺序；Agent 想确认结果还得再调一轮 `layer list`
- **Cache 友好性 ❌** — `session.py` 里随意嵌入 `datetime.now().isoformat()` ，每次快照都不同
- **模型友好性 ✅** — Click 框架 + 标准子命令结构 + `--json` flag；但这不是刻意为 Agent 设计的，只是 Python CLI 的通用最佳实践
- **Skill-CLI 责任边界 ❌** — 没有任何 batch 命令；REPL 交互模式却是默认入口 —— 一个 Agent 完全不需要的 Captive UI

**结论：** CLI-Anything 是工程完成度不错的项目，但其设计哲学停留在 "给人用的 CLI 加个 `--json` "的阶段。它提出了正确的问题，但给出了一个没想透的答案。 **最具说明性的信号是：无子命令时默认进入 REPL 模式 —— Unix 哲学就反对它，在 Agent 时代更不合适。**


### 结语

这套框架的适用范围不限于 CLI —— 任何 Agent 调用的工具接口，都面临相同的约束：

- 你的输出占用 Agent 多少上下文？
- Agent 需要几轮调用才能完成任务？
- 你的输出在状态不变时能不能保持字面一致？
- 你的接口设计贴合模型的先验知识吗？
- 哪些逻辑该你做，哪些该让 Agent 做？



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-04-03-agent-cli-design-principles.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://mp.weixin.qq.com/s/H-hggbJAMBTuambCzNE4OQ]({% include relrefx.html url="/backup/2026-04-03-agent-cli-design-principles.md/mp.weixin.qq.com/e19207e6.html" %})
- [https://mp.weixin.qq.com/s/HX24WCFcP7SLptn-RYvcBg]({% include relrefx.html url="/backup/2026-04-03-agent-cli-design-principles.md/mp.weixin.qq.com/f0b861dc.html" %})
- [https://mp.weixin.qq.com/s/dLRjlcDPp5JeXkxid0sSzg]({% include relrefx.html url="/backup/2026-04-03-agent-cli-design-principles.md/mp.weixin.qq.com/efc348ed.html" %})
- [https://github.com/Johnixr/agent-cli-guide]({% include relrefx.html url="/backup/2026-04-03-agent-cli-design-principles.md/github.com/913686d6.html" %})
- [https://cloud.google.com/blog/products/application-development/build-a-cli-for-ai-agents-and-humans]({% include relrefx.html url="/backup/2026-04-03-agent-cli-design-principles.md/cloud.google.com/c063cb00.html" %})
