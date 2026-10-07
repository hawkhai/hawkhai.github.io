---
layout: post
title: "给 Agent 设计 CLI：不猜、少耗 Token、易重试、好组合"
author:
location: "珠海"
categories: ["机器学习"]
tags: ["机器学习", "机器人", "CLI", "Agent"]
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

Agent 调 CLI 的循环通常是：发现命令 → 组装参数 → 执行 → 解析结果 → 决定重试或下一步。接口设计要减少每一步的猜测，也要让失败后的状态可判定。简言之：**不猜、少耗 Token、易重试、好组合**。

这里的「Agent 友好」并不要求废弃人类终端体验。`gh` 的做法是保留默认文本输出，在支持的命令上提供 `--json` 和字段选择；`gcloud` 建议脚本显式指定 `--format`，因为默认输出可能变化。真正需要稳定的是**显式选择的机器接口**及其行为契约。[GitHub CLI 格式化文档](https://cli.github.com/manual/gh_help_formatting) · [gcloud 脚本指南](https://docs.cloud.google.com/sdk/docs/scripting-gcloud)

## 一、默认可非交互：缺参数就失败，不要等待输入

- 为自动化提供 `--no-input` / `--non-interactive` 等显式开关；当 `stdin` 不是 TTY 时，不应发起提示。缺少必需参数时立即报错，说明该补哪个参数。
- 把**禁止交互**与**授权变更**分开：`--no-input` 不等于同意删除。`--yes` 可以确认已经明确指向的操作；`--force` 通常还有覆盖校验等额外语义，不能与 `--yes` 混用。
- 对不可恢复或影响范围大的操作，要求显式目标、范围和相应确认开关；即使输入来自非 TTY，也不能默默扩大权限或执行默认删除。
- 若命令会打开 pager、编辑器、浏览器或 TUI，应提供关闭方式，并在管道或自动化环境中禁用。AWS CLI 的 `--no-cli-pager` 就是一个具体例子。[CLI Guidelines：交互](https://clig.dev/#interactivity) · [AWS CLI：分页器](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)

```text
$ acme user delete --id u_42 --no-input
ERROR confirmation_required: 删除用户需要显式传入 --yes
Hint: 先运行 acme user delete --id u_42 --dry-run
```

## 二、输出是契约：格式、通道、退出状态要分清

- 数据类命令提供稳定的 `--json` 或 `--format=json`；流式事件可另提供 `--jsonl`。一次性结果用单个 JSON 值通常更方便解析，**无需把所有命令强制改成 JSONL**。
- `stdout` 放命令的主结果；`stderr` 放诊断信息。机器格式开启时，`stdout` 中不能混入日志、进度条或提示语。退出码 `0` 表示命令按其文档定义成功，非零表示失败；异步命令的 `0` 可能只表示任务已提交，必须返回任务 ID 和状态。
- 非 TTY 时关闭颜色、动画和 pager；遵循 `NO_COLOR`。**非 TTY 不必自动切换 JSON**：已有脚本可能依赖文本输出。若要自动切换，需把行为写入契约并提供显式覆盖。
- 已发布的机器字段要维护兼容性：字段含义、类型、单位及空值约定稳定；新增字段一般比重命名或改变类型安全。文档应说明 schema 版本及未知字段的处理方式。

例如查询结果可以是：

```json
{"id":"u_42","name":"Alice","status":"active"}
```

错误响应是否也采用 JSON、写往哪个通道，需要**单独约定**。传统脚本通常依赖非零退出码和 `stderr`；纯 Agent 专用 CLI 也可以约定 JSONL 错误事件。两种做法都可行，但调用方不能只靠解析一行英文错误来分支。[CLI Guidelines：输出与退出码](https://clig.dev/#the-basics) · [gcloud 命令约定](https://docs.cloud.google.com/sdk/gcloud/reference/topic/command-conventions)

## 三、错误可操作：说明失败原因和下一步

参数错误应在发出远程请求或修改文件前发现。错误至少包含稳定的类型、具体原因和下一步；如果有枚举值，列出有效值；如果值得重试，给出条件或等待时间。示例调用比泛泛一句「请检查参数」更有用。

```json
{
  "code": "INVALID_FORMAT",
  "message": "--format 的值 xml 不受支持",
  "allowed_values": ["json", "table"],
  "hint": "改用 acme user list --format=json",
  "retryable": false
}
```

退出码只适合做粗粒度分支；细分原因可用稳定的错误码。**不要把 `2=参数错误、3=不存在、4=权限不足` 当成所有 CLI 的标准**：这些数值只有在该工具明确文档化后才是契约。网络超时、限流、权限失败也不能统一「重试一次」；要区分可重试与需用户处理的情况。[gcloud 命令约定](https://docs.cloud.google.com/sdk/gcloud/reference/topic/command-conventions)

## 四、重试安全：幂等键、状态查询和预演各司其职

Agent 可能在「服务端完成了操作，但本地没收到结果」后重发同一命令。此时单靠 `--dry-run` 无法防止重复创建；干跑与真正执行之间，状态还可能变化。

- 对创建、付款、发送等可能重复产生副作用的操作，优先提供服务端识别的 `--idempotency-key`，并说明作用域、有效期和相同键配不同参数时的行为。`ensure`、`--if-not-exists` 适合可按唯一键判定的资源。
- 当幂等性检查失败时，**不能静默继续创建**；应返回「结果未知」或失败，供调用方查询后再决定。
- 变更命令在可行时提供 `--dry-run` / `--plan`，说明将变更的对象、范围和前提。外部服务可能无法保证预演与实际执行完全一致；必要时用版本号、ETag 或 `--if-match` 做并发保护。
- 成功结果返回资源 ID、关键状态和异步任务 ID；超时后提供按幂等键或任务 ID 查询状态的路径。批量操作要说明是否原子执行，并返回逐项结果，不能让一个非零退出码掩盖已经完成的部分。[gcloud 脚本指南：部分成功](https://docs.cloud.google.com/sdk/docs/scripting-gcloud)

```bash
acme invoice create --customer c_42 --idempotency-key job-20261008-17 --json
acme invoice get --request-id job-20261008-17 --json
```

上面是**建议的接口示意**，不是现有 `acme` 工具。实际产品应在帮助中定义键的稳定性、查询窗口和过期行为。

## 五、渐进发现：从帮助到具体命令，按需展开

- 顶层 `--help` 展示能力边界和常用入口；子命令帮助写清用途、必需参数、默认值、有效值、风险、输出格式及一两个可运行示例。
- 命令树和长参数尽量遵循常见用法，如 `user list`、`user get`、`user delete`，并在不同子命令中统一 `--limit`、`--output` 的含义。`noun-verb` 是有用的组织方式，**不是唯一正确语法**。
- 对动态 API 或大量子命令，可提供按命令查询的 schema 自省。不要为一次简单调用把整个命令树、长篇文档和所有错误字典都注入上下文。
- 错误中可给出相邻命令或正确调用示例，让 Agent 在一次修正后继续。`--help` 本身应可在无登录、无网络、无 TTY 时工作。[CLI Guidelines：帮助](https://clig.dev/#help)

## 六、好组合：输入输出、命名和配置可预测

- 适合管道的命令支持 `stdin`，文件参数可接受 `-` 代表标准输入或标准输出；输入数据与控制参数分开，避免把整段 JSON 塞进 shell 参数。
- 列表、查询和变更命令使用一致的资源名、ID 规则、字段名及全局参数。配置优先级要文档化，例如「显式 flag ＞ 环境变量 ＞ 配置文件 ＞ 默认值」；不要让当前工作目录或隐藏配置悄悄改变目标环境。
- 对 `prod` 等环境和项目提供显式选择与回显，尤其是写操作；避免 Agent 在错误账户或项目中执行。秘密值优先由受控凭据存储、文件或 `stdin` 提供，避免出现在命令行参数、历史记录及诊断输出中。[CLI Guidelines：管道与秘密值](https://clig.dev/#arguments-and-flags)

```bash
acme user list --filter 'status=active' --json
acme user import --file - --no-input
```

## 七、有界输出：默认给摘要，也给完整获取路径

- 对 `list`、`logs`、`search` 设置适当默认上限；提供过滤、字段选择、排序和分页。分页响应需含 `has_more`、`next_cursor` 等机器可读信息，不能只打印「已截断」然后结束。
- `--limit` 限制**最终返回条目**；`--page-size` 常指服务端每次请求的批量大小，两者不要混淆。对会变化的集合，优先使用服务端游标或稳定排序，并说明重复或漏项风险。AWS CLI 官方文档明确区分服务端分页与本地 pager，也提示不同分页参数可能造成异常结果。[AWS CLI：分页](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)
- 大字段、长日志和二进制内容默认给大小、摘要或引用 ID；用户显式请求时再展开。不要在 JSON 字符串中悄悄截断字段而不标记，否则 Agent 会把残缺内容当完整数据。
- 输出应能让调用方判断 `total` 是精确数、估计值还是未知。把稳定的状态与易变时间戳分开，便于 diff 与缓存；但**不能为了缓存命中隐藏业务必需的时间信息**。

```json
{"items":[{"id":"u_42","name":"Alice"}],"has_more":true,"next_cursor":"eyJvZmZzZXQiOjI1fQ","total":null}
```

## 用真实任务检验设计

挑选查询、创建、批量修改、超时重试和部分成功等代表性任务，让 Agent 从帮助入口独立完成。记录首次调用成功率、一次错误后的修正率、重复提交产生的副作用、每项任务的调用次数与 Token 消耗。输出格式的优劣应按完整任务衡量：字段名、数据量和模型分词方式都会影响 Token 数。

## 发布前最小检查表

```text
[ ] 无 TTY 且参数缺失时立即失败；不会打开 pager、编辑器或确认提示
[ ] 机器格式的 stdout 可直接解析，stderr 与退出码职责明确
[ ] 参数错误给出有效值、修正示例和稳定错误类型
[ ] 重试能区分未执行、已完成、部分完成和结果未知
[ ] 高风险操作可预演或明确说明预演边界，并支持条件写/幂等键
[ ] 顶层及子命令 --help 可离线使用，示例与实际参数一致
[ ] 命名、配置优先级、目标环境和输入输出通道一致
[ ] 大结果有上限和机器可读的继续获取方式；截断有显式标记
[ ] 凭据、日志和诊断输出经过脱敏；不会把秘密写进 argv
[ ] 用非 TTY、管道、超时重试、重复提交和部分成功场景做端到端测试
```

## 参考资料

- [知乎：Agent CLI 设计原则](https://zhuanlan.zhihu.com/p/2021165523954615283)：延伸阅读。
- [面向 AI Agent 的 CLI 工具设计规范](https://github.com/allanpk716/ai-agent-cli-rules/blob/main/docs/%E9%9D%A2%E5%90%91%20AI%20Agent%20%E7%9A%84%20CLI%20%E5%B7%A5%E5%85%B7%E8%AE%BE%E8%AE%A1%E8%A7%84%E8%8C%83/%E9%9D%A2%E5%90%91%20AI%20Agent%20%E7%9A%84%20CLI%20%E5%B7%A5%E5%85%B7%E8%AE%BE%E8%AE%A1%E8%A7%84%E8%8C%83.md)：一种面向 Agent 专用 CLI 的协议方案。
- [Command Line Interface Guidelines](https://clig.dev/)：通用 CLI 的帮助、输出、交互、管道与安全建议。
- [GitHub CLI 格式化文档](https://cli.github.com/manual/gh_help_formatting)、[gcloud 脚本指南](https://docs.cloud.google.com/sdk/docs/scripting-gcloud)、[gcloud 命令约定](https://docs.cloud.google.com/sdk/gcloud/reference/topic/command-conventions)、[AWS CLI 分页文档](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)：具体产品行为以官方文档为准。

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-04-03-agent-cli-design-principles.md.js" %}'></script></p>
