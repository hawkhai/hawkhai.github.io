# 博客内容与渲染约束

适用范围：本仓库文章、资源、模板及内容生成工具。完整说明与例子见 [内容格式规范](docs/content-formatting.md)，全站核实记录见 [2026-10-31 审计报告](docs/format-audit-2026-10-31.md)。

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

## 修改与验收

- 保留用户已有改动。格式修复只改能定位、能证明的问题；不猜测缺失资源的内容，不伪造图表、预测结果或训练数据，不为了统一风格改动已验证的实验 notebook。
- 提交配置前检查 `git ls-files -v`。本机 `_config.yml`、Gemfile 等可能设有 assume-unchanged，工作树值不等于部署值；不能直接把本机域名、baseurl 或依赖覆盖到线上。配置修复只提交相对 HEAD 的必要补丁，并用部署配置核实。
- 对全部文章的核实至少包含：实际 Jekyll 渲染、源文件与渲染结果的 SHA-256 对照、资源存在性及大小写、数学和图表开关、表格列数、围栏和特殊字符。自动扫描是候选发现工具，不能证明数学推导正确或所有外链健康。
- 对修改过的公式、图片、流程图和复杂表格补做浏览器抽查；等待脚本完成、图片进入视口后检查。Mermaid 看 SVG，公式看实际排版与错误标记，图片看加载结果，不能只看源码存在。
- 只读核实命令（在仓库根目录，按本机环境调整解释器路径）：

  ```powershell
  & 'C:\Ruby25-x64\bin\ruby.exe' -EUTF-8 tools/render_post_formats.rb
  & 'C:\Ruby25-x64\bin\ruby.exe' -EUTF-8 tools/check_pages_documentation.rb
  python tools/audit_post_formats.py
  python tools/test_audit_post_formats.py
  ```

  产物默认写入被忽略的 `tempdir/format-audit/`。只有确认检查结果适合阻断时才添加 `--fail-on-error`；该参数发现 error 会返回 1，不会自动修复。
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
