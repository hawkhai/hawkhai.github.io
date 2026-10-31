# 博客内容与渲染约束

适用范围：本仓库文章、资源、模板及内容生成工具。完整说明与例子见 [内容格式规范](docs/content-formatting.md)，全站核实记录见 [2026-10-31 审计报告](docs/format-audit-2026-10-31.md)。

## 仓库归属

- 博客文章、模板、工具和本文件的改动都属于 `E:\kSource\blog`，Git 操作必须在该仓库执行；先用 `git rev-parse --show-toplevel` 确认。博客约束只写入本仓库 `AGENTS.md`，不要写入全局 `C:\Users\CF\.codex\AGENTS.md` 或 EasyClaw 技能仓库。其他项目的双仓库提交约定不适用于博客；本地 commit 不自动授权 push 或发布。
- 本地被忽略的 `invisible/` 是独立 Git 仓库，其页面可能参与本地渲染。普通页面编号检查也扫描它，但将问题单列到 `audit.json` 的 `external_page_heading_candidates`，不混成本仓库必须修改/提交的文件。汇报必须说明这些未修复候选，不能由本仓库 error 为 0 宣称该独立仓库也没有问题。

## 以本站渲染链为准

- 当前实测环境为 Jekyll 3.9.0、kramdown 2.3.0、GFM 输入、Rouge；公式为 MathJax 2.7.5，Mermaid 使用仓库中的 bundle。不要拿 GitHub、编辑器或通用 Markdown 预览的效果代替本站验收。
- 内容依次经过 YAML → Liquid/includes → Markdown → layout → 浏览器脚本。代码围栏不阻止 Liquid；HTML 中出现 TeX 分隔符不等于最终公式失败。
- 不把升级渲染器、替换 CDN 或批量重写历史文章当作普通格式修复。修改版本或模板时，重新验证规范中的正反例。
- GitHub Pages 启用 `jekyll-optional-front-matter`：没有 YAML 头的 Markdown 也可能成为页面。`AGENTS.md` 和 `docs/` 是仓库文档，必须保持在 `_config.yml` 的 `exclude` 中；代码围栏或没有 YAML 头都不能保护其 Liquid 示例。

## 写作硬约束

1. 文件使用 UTF-8；不得写入 NUL、退格、换页等控制字符。生成含 TeX 的 Python 文本使用 raw string 或正确转义，并检查生成文件。
2. 新文章使用 `YYYY-MM-DD-slug.md` 和完整 YAML front matter，至少包含 `layout: post`、`title`；按仓库习惯补充分类、标签。功能开关使用真正的 YAML `true` / `false`，不能写成字符串。
3. 含数学公式的文章开启 `mathjax: true`。**新写或修正的行内公式使用 `$$…$$`；块公式使用独占行的 `$$`，上下留空行。** 不直接以原始 `\(...\)` / `\[...\]` 作为 Markdown 源码分隔符。历史单美元公式可正常工作，未经实际验证不要批量替换。
4. Mermaid 开启 `mermaid: true`，使用 `<div class="mermaid">` 容器；本站没有把 `mermaid` 代码围栏转换为该容器的通用逻辑。使用兼容当前 bundle 的语法，复杂标签加双引号，浏览器必须实际生成 SVG。`flowchart: true` + `flow` 围栏属于另一套 flowchart.js 语法，不能混用。
5. 本地图优先使用 `image.html` include，传入 `/assets/...` 路径，不提前拼 `/blog`。该模板无条件添加 `baseurl`，不能直接传远程绝对 URL。
6. `image.html` 默认请求“原图文件名 + `.thumbnail.webp`”，再通过 lazysizes 换成原图。没有缩略图时显式写 `nolazyload=true`；**`nolazyload=false` 不能用来恢复默认行为**，因为模板判断的是是否为 null。图注和尺寸按模板支持的参数填写；该模板没有 `alt` 参数的转发逻辑，需要替代文本时使用带 `alt` 的原生图片标签。
7. 站内资源、下载链接使用 `{% include relref.html url="/assets/..." %}` 或 `relative_url` 过滤器；禁止新写裸 `/assets/...` 根链接或本机盘符链接。文件及路径大小写必须和磁盘一致，兼容 Linux 部署。
8. 表头、分隔行、数据行列数必须一致。公式中的绝对值/范数使用 `\lvert`、`\rvert`、`\lVert`、`\rVert`，不要把未转义的 ASCII `|` 放进数学单元格。普通文本竖线可写 `\|`；本版本代码跨度中的 `a|b` 可以正常保留，不要机械加反斜杠。
9. 展示 Liquid 字面示例时用 `raw` / `endraw` 标签包住整个示例，包括代码围栏。Jekyll 3.9 不支持用新版本的 `render_with_liquid: false` 代替这一步。
10. `<EOS>`、`<BOS>`、命令占位符、C++ 模板等正文尖括号内容放进反引号，或写 HTML 实体；禁止让它们成为裸 HTML。HTML 容器中需要继续解析 Markdown 时显式使用 `markdown="1"`，Mermaid 容器除外。
11. 标题、段落、列表、表格、图片、公式和代码块之间保留清晰空行；代码围栏闭合，嵌套示例使用更长的外层围栏；链接文字有含义，重要图片配说明，数据与图表结论相符。
12. 不把 `.spacefix.json`、生成缓存、备份文件放在 `_posts`；Jekyll 可能把带日期的非 Markdown 文件识别成文章。历史特殊文件名须以实际渲染结果为准，不擅自重命名。
13. **标题编号只能由一方提供。** 默认由 `_sass/_page.scss` 为正文 h2/h3/h4 加编号，目录另有列表序号，`toc: false` 不会关闭正文编号。新文章优先不手写标题序号；保留 `一、`、`1.`、`2.1`、`（一）` 等手写章节号时，必须设置 `toclistyle: none`，关闭正文与目录所有层级的自动序号。不要为去重机械删除课程/书籍章节号或改动已有标题锚点。日期、数量、位数和版本名不能仅因开头有数字就当成序号。

## 本站 JS 扩展约束

以下来自 [Windows Jekyll Markdown 扩展语法](_posts/note/progenv/2021-04-02-win-jekyll-ex.md)，以当前 `assets/blog.js` 和模板实现为准，不把历史演示中的手工 JS 再复制进文章：

- 代码折叠：紧接目标代码块之前放置 `<div class="highlighter-rouge" foldctrl="1"></div>` 控制节点；脚本移除控制节点并折叠下一代码块。不要在两者之间插入另一代码块；浏览器确认展开按钮有效、展开后代码完整可读。
- 列表图片：`image.html` 的 `relocate="3.3"` 按最近前置 `ol/ul` 的层级定位，索引从 1 开始；也可在目标项放 `<span imgid="headw"></span>`，图片使用 `relocate="headw"`。优先使用显式标记，避免增删列表项后数字位置失效；多图迁移由脚本逆序处理，验收看实际图片归属。新写标记使用成对 span 标签，不复制历史自闭合写法。
- 表宽控制：在目标 Markdown 表之前放 `<table class="tablestyle" ntablew="2:3:5" tablew="100%"></table>`；比例使用正整数，项数与列数一致，控制节点必须紧邻下一张目标表。浏览器脚本会删除控制节点，再按比例设置列宽；不能把它当空表清理。
- 上述扩展依赖客户端脚本；静态 HTML 中存在控制节点不代表功能已生效。展示这些扩展的 Liquid 源码仍需按前述 raw 规则保护。

## 根目录脚本使用边界

已逐项阅读根目录 14 个 `.py` 与 10 个 `.bat`。以下是实际行为约束，不能把旧脚本里的全站改写规则直接提升为写作标准：

| 脚本 | 使用约束 |
| --- | --- |
| `checkall.py`、`checkall.bat` | 串行调用重缩进、头部重写、图片/URL 转换和资源整理；bat 默认加 `netfake ignoreerr`，`quick` 只跳过头部步骤。成功标志不能代替只读审计，禁用网络/忽略错误也不代表已验证资源。 |
| `headfmt.py` | 会重写 front matter、生成 `config/frontmatter-values.json`，可能打开编辑器并调用 `invisible/tempd.py encrypt`。历史标题偏好是“分类 -- 标题”，由 `titlecheck` 例外；不能为了通过它批量改已有标题。新增 front matter 字段须核对其字段白名单；`codeformat: false` 也不保证所有入口都不写文件。 |
| `mdformat.py`、`mdrstrip.py` | 均为资源/正文处理入口，分别依赖 `mdformat/` 与 `mdrstrip/`。`format`、`copyres`、`clearimg`、`rebuild` 会影响写回、复制、清理及缓存；先读实际调用链和 `only` 的匹配范围。`ignoreerr` 不作为验收方式，不能凭入口名或没有 `format` 推断完全只读。 |
| `mdimage.py`、`mdurl.py` | 可递归转换临时图片语法、全角字符、URL 和旧公式图片。`mdurl.py` 即使不带 `format` 也可能下载资源，`mdimage.py` 也有图片重存分支；不能当只读检查使用。新公开内容不依赖旧内网图片下载入口。 |
| `checkcache.py` | 默认也会更新两份 `config/large-files.txt` 与 MD5 缓存，`remove` 还会删除命中特征的网页快照。坏页关键词只是候选，核实原文后才可删除；不能把登录页或超时快照当参考正文。 |
| `checkpunct.py` | 主入口固定检查 `invisible/study_notes` 文件；`replace` 会写回，但当前引号函数实际只去除引号内侧空格，没有实现其文案声称的中文引号替换。标点检查未完整排除代码/公式，结果仅供复核，不全站自动替换。 |
| `fmtline.py`、`reindent.py` | 前者按换行参数递归改写多种源码；后者会重缩进 Python，且本版本默认不留备份，混合换行需显式 `--newline=LF/CRLF`。即使 `--dryrun` 也先调用外部 `pythonxcheck`，使用前检查其实现。不要为了文章排版运行全仓库重缩进。 |
| `mddedup.py` | 写死了另一台机器的一篇课程笔记路径，只适用于特定标题去重，不能直接用于全站。 |
| `jekyllserv.py`、`startblog.bat`、`work.bat` | 服务启动会复制平台 Gemfile/lock、修改域名/baseurl、更新备份索引和本地 IP 脚本；`startblog.bat` 还启动 `pythonx/mygit.py all`，不能当普通预览使用。只检查 Ruby/Bundler 可用 `startblog.bat check`。保留 `bundle exec ruby -EUTF-8 -S jekyll` 的 UTF-8 启动方式，避免 Windows GBK 导致 Sass 编译失败；`work.bat` 有固定盘符和旧目录跳转，使用前核对。 |
| `mdserv.py`、`mdserv.bat` | 本地元数据服务（8888），修改分类/标签接口会写文章，标签控制接口会增删 `.mdtag`；不是无副作用的预览服务器。 |
| `imgserv.py`、`imgserv.bat` | 文件与图片服务（9001），含上传写文件和日志接口，也可能绑定局域网 IP；普通格式预览使用 loopback 上的 `python -m http.server`。 |
| `git_assume.bat`、`git_no-assume.bat`、`git_lsfiles.bat` | 前者隐藏配置/依赖及 `.gitmodules` 的工作树改动，取消脚本没有对称恢复 `.gitmodules`；逐项核对索引标志。筛选小写 h 时 PowerShell 要区分大小写（`Select-String -CaseSensitive '^h '`），不能把大写 H 误判为 assume-unchanged。 |
| `git_config_win.bat`、`admin_start.bat` | 前者改全局换行配置，后者请求管理员 shell；日常内容修复不需要运行，也不为了本任务修改全局 Git 配置或提升权限。 |

旧脚本多数依赖相邻 `pythonx`，不能用错误工作目录执行或为方便而改写其外部依赖。只读审计工具应保持标准库/现有 Jekyll 依赖，不新增对这些批量处理入口的调用。

## 修改与验收

- 保留用户已有改动。格式修复只改能定位、能证明的问题；不猜测缺失资源的内容，不伪造图表、预测结果或训练数据，不为了统一风格改动已验证的实验 notebook。
- 提交配置前检查 `git ls-files -v`。本机 `_config.yml`、Gemfile 等可能设有 assume-unchanged，工作树值不等于部署值；不能直接把本机域名、baseurl 或依赖覆盖到线上。配置修复只提交相对 HEAD 的必要补丁，并用部署配置核实。
- 对全部文章的核实至少包含：实际 Jekyll 渲染、源文件与渲染结果的 SHA-256 对照、资源存在性及大小写、数学和图表开关、表格列数、围栏和特殊字符。自动扫描是候选发现工具，不能证明数学推导正确或所有外链健康。
- 对修改过的公式、图片、流程图和复杂表格补做浏览器抽查；等待脚本完成、图片进入视口后检查。Mermaid 看 SVG，公式看实际排版与错误标记，图片看加载结果，不能只看源码存在。
- 只读核实命令（在仓库根目录，按本机环境调整解释器路径）：

  ```powershell
  & 'C:\Ruby25-x64\bin\ruby.exe' -EUTF-8 tools/render_post_formats.rb
  & 'C:\Ruby25-x64\bin\ruby.exe' -EUTF-8 tools/check_pages_documentation.rb
  & 'F:\pythonx\decode\pyenv\Python312\python.exe' tools/audit_post_formats.py --fail-on-error
  & 'F:\pythonx\decode\pyenv\Python312\python.exe' tools/test_audit_post_formats.py
  ```

  产物默认写入被忽略的 `tempdir/format-audit/`。Python 需要 3.9+（使用 `Path.is_relative_to`）；本机 `python`/`python3` 包装脚本实际指向旧版本，先确认解释器，不要因命令名推断版本。`--fail-on-error` 发现 error 会返回 1，不会自动修复；`HEADING_NUMBER_CONFLICT` 已用真实渲染回归验证可阻断。编号检查读取实际布局、正文标题及目录开关，覆盖 HTML/Setext/include 生成的标题，代码示例与布局标题不计入正文；必须先重新渲染，不能拿缺失或陈旧结果证明没有冲突。
- 不为检查格式而运行 `checkall.py`、`headfmt.py`、`mdformat.py`、`mdrstrip.py`、`jekyllserv.py` 等旧流程：它们包含改写文章、切换配置、复制/清理资源等副作用。需要使用时先读具体分支与参数，限定范围并复核 diff。
- 不提交 `_site`、临时预览 HTML、审计临时目录或本机环境文件。审计快照可保存到 `docs/`；不能把“0 渲染异常”表述成“全站无格式错误”。
- **提交前不得只检查 `_posts`。** 检查范围必须同时包含普通页面、没有 YAML 头的 Markdown、Liquid/includes、模板、配置和引用资源；至少执行上面的文章渲染与 `check_pages_documentation.rb`，涉及部署配置时使用实际将提交的配置核实。只读渲染检查不等于完整构建，本机依赖版本也不一定等于 GitHub Pages。
- **push 成功不等于任务完成。** 每次 push 后，必须找到与本次提交完整 SHA 对应的 GitHub Pages workflow，等待其结束，并逐项确认 `build`、`deploy` 都为 `completed / success`。不能拿旧提交的绿灯、仅 build 成功、任务已入队、skipped 或 cancelled 代替。
- 线上任一步失败时读取日志、定位并修复，再推送并重新验收；依赖 warning 与真正的构建异常分开诊断。因权限、网络或服务故障无法确认结果时，明确报告“线上尚未验证”，不得宣称已发布成功。最终汇报提供提交号和可核验的 workflow 链接。

## 2026-10-31 构建故障记录

- 新增 `docs/content-formatting.md` 后，文档里的字面双左花括号被 Liquid 当作变量起点，触发 `Liquid::SyntaxError`。GitHub Pages 的 optional-front-matter 插件会处理没有 YAML 头的 Markdown，代码围栏也不能阻止 Liquid 执行。
- 当时仅验证了 285 篇文章，没有检查新增普通页面，导致本机文章检查通过而线上 [#1899](https://github.com/hawkhai/hawkhai.github.io/actions/runs/41193577814)、[#1900](https://github.com/hawkhai/hawkhai.github.io/actions/runs/41194086428) 失败。不能再把文章审计的 `error: 0` 当作整站构建或部署成功。
- 修复提交 `52d4fddf` 将 `AGENTS.md`、`docs/` 加入构建排除项，并新增普通页面检查；本机 945 个普通页面通过，随后确认线上 [#1901](https://github.com/hawkhai/hawkhai.github.io/actions/runs/41194663810) 的 build、deploy 均成功。
- 后续必须保留文档排除规则，按“提交前覆盖文章与页面 → push 后核对本次 SHA → 等待 build、deploy 双成功”完成验收。
