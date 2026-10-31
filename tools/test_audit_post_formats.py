"""Regression cases for formats that previously produced misleading audit findings."""
import unittest
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from audit_post_formats import (ContentHTML, code_mask, heading_number_conflicts,
                                manual_heading_number, math_backslash_candidate, pipe_cells)


class FormatAuditRegressionTests(unittest.TestCase):
    def test_table_code_pipes_are_not_extra_columns(self):
        self.assertEqual(len(pipe_cells('| x | `a|b` |')), 2)
        self.assertEqual(len(pipe_cells(r'| x | a\|b |')), 2)
        self.assertEqual(len(pipe_cells('| x | $$|x|$$ |')), 4)
        self.assertEqual(len(pipe_cells(r'| x | $$\lvert x\rvert$$ |')), 2)

    def test_literal_brackets_are_not_math_delimiters(self):
        for text in (r'array\[0\]', r'\[in\] bWait', r'Windows \(in Windows\)', r'\[1\] [title](url)'):
            self.assertFalse(math_backslash_candidate(text), text)
        for text in (r'\[', r'\(a+b\)', r'\[\frac{a}{b}\]'):
            self.assertTrue(math_backslash_candidate(text), text)

    def test_raw_liquid_and_nested_fences_are_examples(self):
        text = '{% raw %}\n```liquid\n{{ site.url }}\n```\n{% endraw %}\n````markdown\n```python\nx=1\n```\n````\ntext'
        clean, code, fence, highlight = code_mask(text)
        self.assertIsNone(fence)
        self.assertFalse(highlight)
        self.assertEqual(clean[-1], 'text')
        self.assertNotIn('{{ site.url }}', '\n'.join(line for _, line in code))
        self.assertEqual(len(clean), len(text.splitlines()))

    def test_resources_are_scoped_to_article_not_layout(self):
        document = '<img src="/header.png"><div id="blog_content"><img src="/a.webp" data-src="/a.png"><a href="/data.csv">csv</a></div><script src="/theme.js"></script>'
        result = ContentHTML(document)
        self.assertEqual([r['src'] for r in result.resources], ['/a.webp', '/data.csv'])
        self.assertEqual(result.resources[0]['original'], '/a.png')

    def test_manual_heading_labels_and_semantic_numbers(self):
        for text in ('一、先明确任务', '1. 选择课程', '2.1 输入与标签', '27.PostProcessing',
                     '（一）输入', '(2) 输出', '01 课', '3 2.1 课程', 'I. Research', 'a. Example'):
            self.assertTrue(manual_heading_number(text), text)
        for text in ('64 位指针被截断', '8 个通用寄存器', '2021.02.07 医院', '20260314 补充',
                     '2022 腾讯游戏安全决赛', '90 年代的兴衰', '4 邻域均值', '9 年后重读 AlexNet',
                     '69,709 个参数', '1.5 倍加速', '3.12 版本的新功能', '2.5 GHz', 'Python 3.12', 'QK 转置'):
            self.assertFalse(manual_heading_number(text), text)

    def test_actual_layout_body_and_toc_numbering(self):
        headings = '<h2 id="a">一、任务</h2><h3 id="b">2.1 <code>token</code></h3><h4 id="c">a. Test</h4><h5 id="d">1. Detail</h5>'
        def document(classes='post', toc=True):
            return ContentHTML('<div id="postdiv" class="' + classes + '">' +
                               ('<div id="tocdiv"></div>' if toc else '') +
                               '<div id="blog_content">' + headings + '</div></div>')
        self.assertEqual(len(heading_number_conflicts(document())), 4)
        self.assertEqual(len(heading_number_conflicts(document(toc=False))), 3)
        self.assertEqual(heading_number_conflicts(document('post toc-listyle-none')), [])
        self.assertEqual(heading_number_conflicts(ContentHTML(headings)), [])
        self.assertEqual(document().headings[1]['text'], '2.1 token')

    def test_heading_examples_and_layout_titles_are_excluded(self):
        dom = ContentHTML('<div id="postdiv" class="post"><h2>1. Layout</h2>'
                          '<div id="blog_content"><pre><code><h2>1. Example</h2></code></pre>'
                          '<!-- <h2>一、注释</h2> --><h2>正常标题</h2></div></div>')
        self.assertEqual([h['text'] for h in dom.headings], ['正常标题'])
        self.assertEqual(heading_number_conflicts(dom), [])
        dom = ContentHTML("<div id='postdiv' class='post'><h2>1. Layout</h2>"
                          "<div id='blog_content'><h2>正常标题</h2></div></div>")
        self.assertEqual(heading_number_conflicts(dom), [])

    def test_cli_rejects_number_conflicts_and_accepts_manual_mode(self):
        # Prove the new finding is wired to the existing --fail-on-error exit status.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / '_posts').mkdir()
            (root / '_posts/2026-10-31-example.md').write_text('---\nlayout: post\n---\n\n## 1. Test\n', encoding='utf-8')
            output = root / 'tempdir/format-audit'
            (output / 'rendered').mkdir(parents=True)
            (output / 'render-results.json').write_text(json.dumps({'records': [{
                'path': '_posts/2026-10-31-example.md', 'status': 'ok',
                'flags': {'layout': 'post'}, 'rendered': 'example.html'}]}), encoding='utf-8')
            page = output / 'rendered/example.html'
            command = [sys.executable, str(Path(__file__).with_name('audit_post_formats.py')),
                       '--root', str(root), '--fail-on-error']
            for classes, expected in [('post', 1), ('post toc-listyle-none', 0)]:
                page.write_text('<div id="postdiv" class="' + classes + '">'
                                '<div id="blog_content"><h2 id="test">1. Test</h2></div></div>', encoding='utf-8')
                result = subprocess.run(command, capture_output=True)
                self.assertEqual(result.returncode, expected, result.stderr)
                findings = json.loads((output / 'audit.json').read_text(encoding='utf-8'))['findings']
                self.assertEqual(sum(f['rule'] == 'HEADING_NUMBER_CONFLICT' for f in findings), expected)
            # The existing ordinary-page renderer feeds the same rule for layout: post pages.
            (root / 'guide.md').write_text('## 一、Guide\n', encoding='utf-8')
            (output / 'rendered-pages').mkdir()
            (output / 'rendered-pages/0.html').write_text(
                '<div id="postdiv" class="post"><div id="blog_content"><h2>一、Guide</h2></div></div>', encoding='utf-8')
            (output / 'pages-check.json').write_text(json.dumps({'records': [
                {'path': 'guide.md', 'rendered': 'rendered-pages/0.html'}]}), encoding='utf-8')
            result = subprocess.run(command, capture_output=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            report = json.loads((output / 'audit.json').read_text(encoding='utf-8'))
            self.assertEqual(report['summary']['pages_numbering_checked'], 1)
            self.assertEqual(report['findings'][0]['path'], 'guide.md')
            self.assertEqual(report['findings'][0]['rule'], 'HEADING_NUMBER_CONFLICT')
            # Nested local checkouts are audited but remain outside the parent's commit scope.
            (root / 'external/.git').mkdir(parents=True)
            (root / 'external/guide.md').write_text('## 一、Guide\n', encoding='utf-8')
            (output / 'pages-check.json').write_text(json.dumps({'records': [
                {'path': 'external/guide.md', 'rendered': 'rendered-pages/0.html'}]}), encoding='utf-8')
            result = subprocess.run(command, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads((output / 'audit.json').read_text(encoding='utf-8'))
            self.assertEqual(report['summary']['external_page_heading_candidates'], 1)
            self.assertEqual(report['external_page_heading_candidates'][0]['repository'], 'external')


if __name__ == '__main__':
    unittest.main()
