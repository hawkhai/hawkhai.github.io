"""Read-only format audit of every Markdown file in _posts (stdlib only).

Optionally consumes render_post_formats.rb output to check real Jekyll HTML,
plus check_pages_documentation.rb output for ordinary-page heading numbering.
Does not run legacy format/copyres scripts, fetch external URLs, or rewrite posts.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from collections import Counter
from datetime import datetime
from urllib.parse import unquote, urlsplit

VOID = set('area base br col embed hr img input link meta param source track wbr'.split())
KNOWN_TAGS = set(('a abbr address article aside audio b bdi bdo blockquote body br button canvas caption cite code col colgroup data datalist dd del details dfn dialog div dl dt em embed fieldset figcaption figure footer form h1 h2 h3 h4 h5 h6 head header hgroup hr html i iframe img input ins kbd label legend li link main mark menu meta meter nav noscript object ol optgroup option output p picture pre progress q rp rt ruby s samp script section select small source span strong style sub summary sup table tbody td template textarea tfoot th thead time title tr track u ul var video wbr svg path g rect circle line polyline polygon text defs symbol use math').split())

class ContentHTML(HTMLParser):
    def __init__(self, value):
        super().__init__(convert_charrefs=True)
        self.restrict = bool(re.search(r'''\bid\s*=\s*["']blog_content["']''', value))
        self.stack = []
        self.resources, self.ids, self.tables = [], [], 0
        self.headings = []
        self.post = False
        self.manual_numbering = False
        self.has_toc = False
        self.heading = None
        self.feed(value)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id') == 'postdiv' and 'post' in attrs.get('class', '').split():
            self.post = True
            self.manual_numbering = 'toc-listyle-none' in attrs.get('class', '').split()
        if attrs.get('id') == 'tocdiv': self.has_toc = True
        active = not self.restrict or any(a.get('id') == 'blog_content' for _, a in self.stack) or attrs.get('id') == 'blog_content'
        if active:
            if re.fullmatch(r'h[1-6]', tag) and not any(t in ('pre', 'code', 'script', 'style') for t, _ in self.stack):
                self.heading = {'level': int(tag[1]), 'id': attrs.get('id', ''), 'text': ''}
                self.headings.append(self.heading)
            if attrs.get('id'): self.ids.append(attrs['id'])
            if tag == 'table': self.tables += 1
            if tag == 'img':
                self.resources.append({'kind':'image', 'src':attrs.get('src',''), 'original':attrs.get('data-src','')})
            elif tag in ('a','source','video','iframe','script'):
                url = attrs.get('href' if tag == 'a' else 'src', '')
                if url: self.resources.append({'kind':tag, 'src':url, 'original':''})
        if tag not in VOID: self.stack.append((tag, attrs))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if self.heading and tag == 'h' + str(self.heading['level']): self.heading = None
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.heading: self.heading['text'] += data


def manual_heading_number(text):
    """Recognize explicit section labels, not dates, quantities or version names."""
    text = text.strip()
    # Dates and decimal quantities are content, not section labels.
    if re.match(r'^(?:19|20)\d{2}(?:[-./年]\d{1,2}(?:[-./月]\d{1,2}日?)?|\d{4})(?:\s|$)', text):
        return False
    if re.match(r'^\d+(?:\.\d+)+\s*(?:倍|个|位|秒|分钟|小时|版本|%|％|[KMGT]i?B\b|[GM]Hz\b|ms\b)', text):
        return False
    numerals = '零〇一二三四五六七八九十百千两'
    return bool(re.match(
        rf'^(?:[{numerals}]+[、．.]|[（(](?:\d+|[{numerals}]+)[)）]|'
        r'\d+[、．)）]|\d+\.(?!\d)|\d+(?:\.\d+)+(?=\s|[、:：])|'
        r'0\d+\s|\d+\s+(?=\d+\.\d+)|[A-Za-z][.)]\s|[IVXLCDM]+[.)]\s)', text))


def heading_number_conflicts(dom):
    """Use the actual layout classes; toc:false does not disable body counters."""
    if not dom.post or dom.manual_numbering:
        return []
    return [h for h in dom.headings if manual_heading_number(h['text']) and
            (h['level'] in (2, 3, 4) or (dom.has_toc and h['id']))]

def code_mask(body):
    """Keep line numbers stable while masking examples, raw Liquid and comments."""
    body = re.sub(r'{%[- ]*raw\s*[- ]*%}[\s\S]*?{%[- ]*endraw\s*[- ]*%}',
                  lambda m: '\n' * m[0].count('\n'), body)
    body = re.sub(r'<!--[\s\S]*?-->', lambda m:'\n'*m[0].count('\n'), body)
    lines = body.splitlines()
    clean, code_lines = [], []
    fence = None
    highlight = False
    for n, line in enumerate(lines, 1):
        stripped = re.sub(r'^(?:[ \t]*>[ \t]*)+', '', line)
        mark = re.match(r'^[ \t]{0,3}(`{3,}|~{3,})(.*)$', stripped)
        if fence:
            if mark and mark[1][0] == fence[0] and len(mark[1]) >= fence[1] and not mark[2].strip():
                fence = None
            else: code_lines.append((n,line))
            clean.append(''); continue
        if mark:
            fence = (mark[1][0],len(mark[1]),n,mark[2].strip())
            clean.append(''); continue
        if re.search(r'{%\s*highlight\b',line): highlight = True; clean.append(''); continue
        if re.search(r'{%\s*endhighlight\b',line): highlight = False; clean.append(''); continue
        if highlight or line.startswith('    ') or line.startswith('\t'):
            code_lines.append((n,line)); clean.append(''); continue
        clean.append(line)
    return clean, code_lines, fence, highlight

def no_inline_code(line):
    return re.sub(r'(`+)(.+?)\1', lambda m:' ' * len(m[0]), line)

def pipe_cells(line):
    line = re.sub(r'{[{%][\s\S]*?[}%]}', 'LIQUID', line.strip())
    parts, chunk, ticks, i = [], '', 0, 0
    while i < len(line):
        ch = line[i]
        if ch == '\\' and i+1 < len(line): chunk += line[i:i+2]; i += 2; continue
        if ch == '`':
            j=i
            while j<len(line) and line[j]=='`': j+=1
            count=j-i
            if not ticks: ticks=count
            elif ticks==count: ticks=0
            chunk+=line[i:j];i=j;continue
        if ch == '|' and not ticks: parts.append(chunk.strip());chunk=''
        else: chunk+=ch
        i+=1
    parts.append(chunk.strip())
    if parts and parts[0]=='': parts.pop(0)
    if parts and parts[-1]=='': parts.pop()
    return parts

def math_backslash_candidate(value):
    """Distinguish TeX delimiters from escaped array indices, links and prose."""
    if re.match(r'^\s*\\\[\s*$', value):
        return True
    for pattern in (r'\\\((.*?)\\\)', r'\\\[(.*?)\\\]'):
        for content in re.findall(pattern, value):
            if re.search(r'\\[A-Za-z]+|[_^=+*/]', content):
                return True
    return False

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--render-results', type=Path)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--fail-on-error', action='store_true')
    args=ap.parse_args()
    root=args.root.resolve()
    output=args.output or root/'tempdir/format-audit'
    output.mkdir(parents=True,exist_ok=True)
    render_path=args.render_results or output/'render-results.json'
    rendered=json.loads(render_path.read_text(encoding='utf-8')) if render_path.exists() else {'records':[],'engine':{}}
    render_map={r['path']:r for r in rendered['records']}
    baseurl=rendered.get('engine',{}).get('baseurl','')
    post_paths=sorted(p for p in (root/'_posts').rglob('*') if p.is_file() and p.suffix.lower() in ('.md','.markdown'))
    issues=[]; rows=[]; directory_cache={}

    def add(path,line,severity,rule,message):
        item={'path':path,'line':max(1,line),'severity':severity,'rule':rule,'message':message}
        if item not in issues: issues.append(item)

    def check_heading_numbers(path, text, dom):
        for heading in heading_number_conflicts(dom):
            title=heading['text'].strip()
            # Includes, Setext and raw HTML may not have an ATX source line.
            source_n=next((n+1 for n,line in enumerate(text.splitlines()) if title in line),1)
            add(path,source_n,'error','HEADING_NUMBER_CONFLICT',
                '手写标题编号会叠加正文/目录自动编号；移除手写编号，或设置 toclistyle: none：'+title)

    def local_resource(url):
        if not url or url.startswith(('#','data:','mailto:','javascript:','//')): return ('skip',None)
        u=urlsplit(html.unescape(url))
        if u.scheme or u.netloc: return ('external',None)
        path=unquote(u.path)
        if not path.startswith('/'): return ('relative',None)
        if baseurl and (path==baseurl or path.startswith(baseurl+'/')): path=path[len(baseurl):]
        if '{{' in path or '{%' in path: return ('dynamic',None)
        candidate=(root/path.lstrip('/')).resolve()
        if not candidate.is_relative_to(root): return ('outside',None)
        if not candidate.exists(): return ('missing',path)
        current=root; mismatch=False
        for part in Path(path.lstrip('/')).parts:
            if current not in directory_cache:
                try: directory_cache[current]=set(p.name for p in current.iterdir())
                except OSError: directory_cache[current]=set()
            names=directory_cache[current]
            if part not in names:
                actual=next((x for x in names if x.casefold()==part.casefold()),None)
                if actual: mismatch=True;part=actual
            current=current/part
        return ('case' if mismatch else 'exists',path)

    for file in post_paths:
        rel=file.relative_to(root).as_posix()
        raw=file.read_bytes()
        try: text=raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            add(rel,1,'error','ENCODING','不是可解码的 UTF-8 文件'); continue
        fm=re.match(r'\A---[ \t]*\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)',text)
        if not fm:
            add(rel,1,'error','FRONT_MATTER','缺少完整 YAML front matter')
            header='';body=text;offset=0
        else:
            header=fm[1];body=text[fm.end():];offset=text[:fm.end()].count('\n')
        record=render_map.get(rel)
        flags=record.get('flags',{}) if record else {}
        if not record: add(rel,1,'warning','NOT_RENDERED','未提供该文章的实际 Jekyll 渲染记录')
        elif record['status']!='ok': add(rel,1,'error','JEKYLL_RENDER',record.get('error','渲染失败'))
        elif record.get('source_sha256') and record['source_sha256'] != hashlib.sha256(raw).hexdigest():
            add(rel,1,'warning','STALE_RENDER','源文件已变化，应重新生成 Jekyll 渲染记录')
        if flags.get('visibility') not in (None,'','hidden'):
            add(rel,1,'warning','VISIBILITY_VALUE','visibility 值不等于模板识别的 hidden；核对是否应隐藏')
        for key in ('mathjax','mermaid','flowchart'):
            if flags.get(key) is not None and not isinstance(flags[key],bool):
                add(rel,1,'error','FLAG_TYPE',key+' 必须使用 YAML 布尔值，不能使用带引号字符串')
        for match in re.finditer(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',text):
            add(rel,text[:match.start()].count('\n')+1,'error','CONTROL_CHARACTER','包含不可见控制字符，可能损坏 TeX 或代码')
        clean, code_lines, unclosed, highlight=code_mask(body)
        if unclosed: add(rel,offset+unclosed[2],'error','FENCE_UNCLOSED','代码围栏未闭合')
        if highlight: add(rel,len(text.splitlines()),'error','HIGHLIGHT_UNCLOSED','highlight 块未闭合')
        for n,line in code_lines:
            if '{{' in line or '{%' in line:
                add(rel,offset+n,'warning','LIQUID_IN_CODE','代码中的 Liquid 仍会被执行；展示字面语法时需要 raw 保护')
        visible='\n'.join(clean)
        mermaid_count=len(re.findall(r'<div\b[^>]*class=["\'][^"\']*\bmermaid\b',visible))
        fenced_mermaid=len(re.findall(r'^[ \t]*```mermaid\b',body,re.M))
        if mermaid_count and flags.get('mermaid') is not True:
            add(rel,1,'error','MERMAID_FLAG','实际 Mermaid 容器存在，但缺少 mermaid: true')
        if fenced_mermaid:
            add(rel,1,'warning','MERMAID_FENCE','本模板只自动渲染 .mermaid 容器；代码围栏须核对浏览器是否生成 SVG')
        has_flow=bool(re.search(r'^[ \t]*```flow\b',body,re.M))
        if has_flow and flags.get('flowchart') is not True:
            add(rel,1,'error','FLOWCHART_FLAG','flow 围栏缺少 flowchart: true')
        inline_count=0;block_count=0;math_state=None
        for n,line in enumerate(clean,1):
            value=no_inline_code(line)
            if math_state is not None:
                if re.search(r'(?<!\\)\$\$',value): math_state=None
                continue
            if re.match(r'^[ \t]*\$\$',value):
                if re.match(r'^[ \t]*\$\$[A-Z][A-Z0-9_]+(?:[ \t]|$)',value) and value.count('$$')==1:
                    add(rel,offset+n,'info','DOLLAR_VARIABLE_LITERAL','疑似 qmake 等工具的 $$变量，应作为代码阅读，不按未闭合公式处理')
                    continue
                block_count+=1
                if value.count('$$')<2: math_state=n
                continue
            if math_backslash_candidate(value) and (flags.get('mathjax') is True or re.match(r'^\s*\\\[\s*$',value)):
                add(rel,offset+n,'warning','MATH_BACKSLASH_DELIMITER','直接写反斜杠括号可能被 Markdown 消耗；使用 kramdown 的 $$ 语法')
            matches=re.findall(r'(?<![\\$])\$(?!\$)([^\n$]+?)(?<!\\)\$(?!\$)',value)
            for formula in matches:
                if re.search(r'[A-Za-z\\_^{}]',formula):
                    inline_count+=1
                    add(rel,offset+n,'info','INLINE_DOLLAR_LEGACY','单美元依赖客户端扫描，遇到 * / HTML 等可能先被 Markdown 改写；新文用行内 $$')
            inline_count+=len(re.findall(r'\S[^\n]*?\$\$[^\n]+?\$\$',value))
            for token in re.findall(r'<([A-Za-z][A-Za-z0-9_:-]*)>',value):
                if token.lower() not in KNOWN_TAGS:
                    add(rel,offset+n,'warning','RAW_SPECIAL_TOKEN','裸尖括号 token 可能被当作 HTML；请用反引号或实体：<'+token+'>')
        if math_state is not None: add(rel,offset+math_state,'error','MATH_BLOCK_UNCLOSED','独立行 $$ 数学块未闭合')
        if (block_count or inline_count) and flags.get('mathjax') is not True:
            add(rel,1,'warning','MATHJAX_FLAG','发现数学候选但未启用 mathjax: true；货币/示例需人工排除')
        for n,line in enumerate(clean,1):
            if re.search(r'\]\(/(?:assets|images|source|css|fonts)/|\b(?:src|href)=["\']/(?:assets|images|source|css|fonts)/',line):
                add(rel,offset+n,'warning','BASEURL_BYPASS','站内资源使用裸根路径，会绕过 /blog 子路径；使用 relref include 或 relative_url')
            if re.match(r'^\s*\|',line):
                cells=pipe_cells(line)
                if cells and all(re.match(r'^:?-+:?$',v) for v in cells) and n>=2:
                    expected=len(cells)
                    previous=pipe_cells(clean[n-2])
                    if len(previous)!=expected:
                        add(rel,offset+n,'warning','TABLE_COLUMNS','表头与分隔行列数不同')
                    j=n
                    while j<len(clean) and clean[j].strip() and '|' in clean[j]:
                        actual=len(pipe_cells(clean[j]))
                        if actual!=expected:
                            add(rel,offset+j+1,'warning','TABLE_COLUMNS','表格行列数 '+str(actual)+' 与表头 '+str(expected)+' 不同；核对正文/公式中的竖线')
                        j+=1
        includes=list(re.finditer(r'{%[- ]*include\s+([^\s%]+)([\s\S]*?)%}',visible))
        for item in includes:
            template=item[1]
            n=visible[:item.start()].count('\n')+1+offset
            if not (root/'_includes'/template).is_file(): add(rel,n,'error','INCLUDE_MISSING','include 模板不存在：'+template)
            if template=='image.html' and re.search(r'\burl\d*\s*=\s*["\']https?://',item[2]):
                add(rel,n,'error','IMAGE_INCLUDE_EXTERNAL','image.html 会 prepend baseurl，不能直接传入远程绝对 URL')
        resources=[];tables=0;numbered_headings=0
        if record and record.get('rendered'):
            html_path=render_path.parent/'rendered'/record['rendered']
            if html_path.exists():
                dom=ContentHTML(html_path.read_text(encoding='utf-8'))
                resources=dom.resources;tables=dom.tables
                numbered_headings=sum(manual_heading_number(h['text']) for h in dom.headings)
                check_heading_numbers(rel, text, dom)
                for identifier,count in Counter(dom.ids).items():
                    if count>1: add(rel,1,'warning','DUPLICATE_ID','生成 HTML 包含重复 id：'+identifier)
        remote=0; images=0; local_checked=0
        for resource in resources:
            if resource['kind']=='image': images+=1
            original=resource.get('original')
            urls=[original] if original else [resource['src']]
            for url in urls:
                status,path=local_resource(url)
                if status=='external': remote+=1
                if status in ('exists','missing','case'): local_checked+=1
                if status in ('missing','case'):
                    leaf=path.rsplit('/',1)[-1]
                    source_n=next((n+1 for n,line in enumerate(text.splitlines()) if leaf in line),1)
                    # Only file-like local targets: post permalinks are resolved by Jekyll, not a source file.
                    if resource['kind']=='a' and not re.search(r'\.[A-Za-z0-9]{1,12}$',path): continue
                    if path.endswith('.html') and resource['kind']=='a': continue
                    add(rel,source_n,'error' if status=='missing' else 'warning',
                        'LOCAL_RESOURCE_MISSING' if status=='missing' else 'RESOURCE_CASE',
                        ('当前仓库找不到资源：' if status=='missing' else '路径大小写与磁盘不一致：')+path)
            if original:
                status,path=local_resource(resource['src'])
                if status=='missing' and resource['src'].endswith('.thumbnail.webp'):
                    leaf=original.rsplit('/',1)[-1]
                    source_n=next((n+1 for n,line in enumerate(text.splitlines()) if leaf in line),1)
                    add(rel,source_n,'warning','THUMBNAIL_MISSING','占位缩略图不存在，懒加载原图仍可能成功：'+path)
        rows.append({'path':rel,'sha256':hashlib.sha256(raw).hexdigest(),'flags':flags,
                     'rendered':bool(record and record['status']=='ok'),
                     'features':{'images':images,'tables':tables,'numbered_headings':numbered_headings,'math_blocks':block_count,'inline_math_candidates':inline_count,'mermaid':mermaid_count,'includes':len(includes),'code_blocks':len(re.findall(r'^\s*```\w+',body,re.M))},
                     'local_resources_checked':local_checked,'external_resources_unchecked':remote})

    # Ordinary pages can also use layout: post. Consume the existing page renderer
    # so the same numbering assertion applies outside _posts, without reimplementing Markdown.
    pages_path=render_path.parent/'pages-check.json'
    page_records=json.loads(pages_path.read_text(encoding='utf-8')).get('records',[]) if pages_path.exists() else []
    pages_numbering_checked=0
    external_page_heading_candidates=[]
    for page in page_records:
        html_path=pages_path.parent/page['rendered']
        if not html_path.is_file(): continue
        source=root/page['path']
        raw=source.read_bytes() if source.is_file() else b''
        if page.get('source_sha256') and hashlib.sha256(raw).hexdigest()!=page['source_sha256']:
            add(page['path'],1,'warning','STALE_PAGE_RENDER','页面源文件已变化，应重新运行普通页面检查')
        dom=ContentHTML(html_path.read_text(encoding='utf-8'))
        external_repo=next((parent for parent in source.parents if parent!=root and
                           root in parent.parents and (parent/'.git').exists()),None)
        if external_repo:
            # A local ignored checkout is not owned by this repository. Report
            # candidates, but do not make fixing/committing another repo mandatory.
            external_page_heading_candidates.extend(
                {'path':page['path'],'repository':external_repo.relative_to(root).as_posix(),
                 'heading':h['text'].strip()} for h in heading_number_conflicts(dom))
        else:
            check_heading_numbers(page['path'],raw.decode('utf-8-sig',errors='replace'),dom)
        pages_numbering_checked+=1

    sidecars=sorted(p.relative_to(root).as_posix() for p in (root/'_posts').rglob('*') if p.is_file() and p not in post_paths)
    for path in sorted(set(render_map)-{p.relative_to(root).as_posix() for p in post_paths}):
        add(path,1,'warning','NON_MARKDOWN_POST','Jekyll 实际把这个非 Markdown 文件识别为文章；核对辅助 JSON 是否应移出 _posts')
    for row in rows:
        own=[i for i in issues if i['path']==row['path']]
        row['issues']=dict(Counter(i['severity'] for i in own))
    summary={'markdown_files':len(post_paths),'rendered_markdown':sum(r['rendered'] for r in rows),
             'pages_numbering_checked':pages_numbering_checked,
             'external_page_heading_candidates':len(external_page_heading_candidates),
             'jekyll_documents':len(render_map),'sidecar_files':sidecars,
             'findings':{level:sum(i['severity']==level for i in issues) for level in ('error','warning','info')},
             'rules':dict(Counter(i['rule'] for i in issues)),
             'affected_posts':sum(bool(r['issues']) for r in rows),
             'external_resources_unchecked':sum(r['external_resources_unchecked'] for r in rows)}
    engine={k:v for k,v in rendered.get('engine',{}).items() if k!='source'}
    result={'generated_at':datetime.now().astimezone().isoformat(),'scope':'_posts 所有 Markdown；普通页面额外检查标题编号；独立嵌套仓库单列候选；代码示例/注释尽量排除；实际渲染可选','engine':engine,'summary':summary,'posts':rows,'findings':issues,'external_page_heading_candidates':external_page_heading_candidates}
    (output/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    with (output/'findings.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['path','line','severity','rule','message']);writer.writeheader();writer.writerows(issues)
    with (output/'inventory.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.writer(f);writer.writerow(['path','rendered','images','tables','math_blocks','mermaid','errors','warnings','info','source_sha256'])
        for r in rows: writer.writerow([r['path'],r['rendered'],r['features']['images'],r['features']['tables'],r['features']['math_blocks'],r['features']['mermaid'],r['issues'].get('error',0),r['issues'].get('warning',0),r['issues'].get('info',0),r['sha256']])
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if args.fail_on_error and any(i['severity']=='error' for i in issues): raise SystemExit(1)

if __name__=='__main__': main()
