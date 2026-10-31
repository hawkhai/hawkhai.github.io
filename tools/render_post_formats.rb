# frozen_string_literal: true
# Read-only source audit: writes only to the selected output directory.
require 'json'
require 'fileutils'
require 'optparse'
require 'jekyll'
require 'digest'
require 'cgi'

options = { source: File.expand_path('..', __dir__) }
OptionParser.new do |parser|
  parser.on('--source PATH') { |v| options[:source] = File.expand_path(v) }
  parser.on('--output PATH') { |v| options[:output] = File.expand_path(v) }
end.parse!
root = options[:source]
output = options[:output] || File.join(root, 'tempdir', 'format-audit')
FileUtils.mkdir_p(File.join(output, 'rendered'))
config = Jekyll.configuration('source' => root,
  'destination' => File.join(output, 'unused-site'), 'quiet' => true,
  'future' => true, 'unpublished' => true, 'incremental' => false)
site = Jekyll::Site.new(config)
site.reset
site.read
payload = site.site_payload
records = []
site.posts.docs.sort_by(&:path).each do |doc|
  path = doc.path.sub(root + '/', '').sub(root + '\\', '')
  path = Pathname.new(doc.path).relative_path_from(Pathname.new(root)).to_s.tr('\\', '/')
  record = { 'path' => path, 'url' => doc.url,
    'source_sha256' => Digest::SHA256.file(doc.path).hexdigest,
    'flags' => doc.data.select { |key, _| %w[layout mathjax mermaid flowchart glslcanvas visibility published].include?(key) } }
  begin
    rendered = Jekyll::Renderer.new(site, doc, payload).run
    relative = path.sub(/\.(md|markdown)$/i, '.html')
    target = File.join(output, 'rendered', relative)
    FileUtils.mkdir_p(File.dirname(target))
    File.write(target, rendered, mode: 'w:UTF-8')
    record['rendered'] = relative
    record['status'] = 'ok'
    record['bytes'] = rendered.bytesize
  rescue StandardError => error
    record['status'] = 'error'
    record['error'] = "#{error.class}: #{error.message}"
  end
  records << record
  puts "Rendered #{records.length}: #{path}" if records.length % 50 == 0
end

converter = site.find_converter_instance(Jekyll::Converters::Markdown)
fixtures = {
  'inline-dollar' => 'inline $p_{b,i,c}$ and $a*b*c$ end',
  'inline-double-dollar' => 'inline $$p_{b,i,c}$$ end',
  'loss-example' => "对这份定长数据，记作 $$p_{b,i,c}$$。\n\n$$\n\\mathcal{L}=-\\frac{1}{7B}\\sum_{b=0}^{B-1}\\sum_{r=0}^{6} \\log p_{b,\\,7+r,\\,\\mathrm{labels}_{b,7+r}}.\n$$\n",
  'inline-parenthesis' => 'inline \\(p_{b,i,c}\\) end',
  'block-double-dollar' => "$$\n\\mathcal{L}=-\\frac{1}{7B}\\sum_{b=0}^{B-1}p_b\n$$\n",
  'block-bracket' => "\\[\n\\mathcal{L}=-\\frac{1}{7B}p_b\n\\]\n",
  'mermaid-fence' => "```mermaid\ngraph LR\n A-->B\n```\n",
  'mermaid-div' => "<div class=\"mermaid\">\ngraph LR\n A-->B\n</div>\n",
  'table-pipe-escaped' => "| Name | Value |\n| --- | --- |\n| x | `a\\|b` |\n",
  'table-pipe-unescaped' => "| Name | Value |\n| --- | --- |\n| x | `a|b` |\n",
  'table-text-pipe-escaped' => "| Name | Value |\n| --- | --- |\n| x | a\\|b |\n",
  'table-inline-math-pipe' => "| Name | Value |\n| --- | --- |\n| x | $$|x|$$ |\n",
  'table-safe-math' => "| Name | Value |\n| --- | --- |\n| x | $$\\lvert x\\rvert$$ |\n",
  'html-special-token' => 'before <EOS> after, and `<EOS>`',
  'html-markdown' => "<div>\n**bold**\n</div>\n\n<div markdown=\"1\">\n**bold**\n</div>\n"
}
fixture_results = fixtures.map do |name, markdown|
  { 'name' => name, 'markdown' => markdown, 'html' => converter.convert(markdown) }
end
info = { 'engine' => { 'ruby' => RUBY_VERSION, 'jekyll' => Jekyll::VERSION,
  'kramdown' => Kramdown::VERSION, 'input' => config.dig('kramdown', 'input'),
  'baseurl' => config['baseurl'], 'source' => root },
  'records' => records, 'fixtures' => fixture_results }
File.write(File.join(output, 'render-results.json'), JSON.pretty_generate(info), mode: 'w:UTF-8')
fixture_html = fixture_results.map do |item|
  "<section id=\"#{item['name']}\"><h2>#{item['name']}</h2><pre>#{CGI.escapeHTML(item['markdown'])}</pre><div class=\"result\">#{item['html']}</div></section>"
end.join("\n")
base = config['baseurl'].to_s
# No CDN/theme upgrades: use the same MathJax version, Mermaid bundle and config as the site.
browser_html = <<~HTML
  <!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>Jekyll rendering fixtures</title>
  <style>body{max-width:1100px;margin:32px auto;padding:0 20px;font:17px/1.7 system-ui}section{border-top:1px solid #ccd;padding:12px 0}pre{background:#f4f6f8;padding:12px;overflow:auto;font-size:14px}table{border-collapse:collapse}th,td{border:1px solid #bbc;padding:6px 18px}.mermaid{max-width:700px}.mermaid svg{max-height:150px}img{max-width:100%}</style>
  <h1>本站 Jekyll 渲染对照样例</h1><p>上方为源码，下方为本站 kramdown 输出。包含故意错误的反例，不代表所有样例都应成功。</p>
  #{fixture_html}
  <section id="image-direct"><h2>真实文章图片：直接加载原图</h2>
  <img alt="Transformer baseline loss" src="#{base}/assets/images/261031-transformer-from-scratch/baseline_loss.png"></section>
  <script>var MathJaxLocalUrl = #{JSON.generate(base + '/assets/mathjax.js')};</script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
  <script src="#{base}/assets/mathjax.js"></script>
  <script src="#{base}/assets/mermaid.min.js"></script><script>mermaid.initialize({startOnLoad:true});</script>
  </html>
HTML
File.write(File.join(output, 'fixtures.html'), browser_html, mode: 'w:UTF-8')
puts JSON.generate('posts' => records.length, 'render_errors' => records.count { |r| r['status'] == 'error' }, 'output' => output)
