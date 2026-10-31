"""Regression cases for formats that previously produced misleading audit findings."""
import unittest

from audit_post_formats import ContentHTML, code_mask, math_backslash_candidate, pipe_cells


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


if __name__ == '__main__':
    unittest.main()
