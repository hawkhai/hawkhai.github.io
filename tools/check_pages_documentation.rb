# frozen_string_literal: true
# Exercise Pages' optional-front-matter generation, including non-post pages.
# Never writes a site or changes source files.
require 'jekyll'
require 'jekyll-optional-front-matter'
require 'json'
require 'fileutils'
require 'optparse'

options = {}
OptionParser.new do |parser|
  parser.on('--config PATH') { |value| options[:config] = File.expand_path(value) }
end.parse!

root = File.expand_path('..', __dir__)
output = File.join(root, 'tempdir', 'format-audit')
settings = { 'source' => root,
  'destination' => File.join(output, 'unused-pages-site'), 'quiet' => true,
  'future' => true, 'unpublished' => true, 'incremental' => false }
settings['config'] = options[:config] if options[:config]
config = Jekyll.configuration(settings)
site = Jekyll::Site.new(config)
site.reset
site.read
site.generate

repository_doc = lambda do |path|
  normalized = path.to_s.tr('\\', '/').sub(%r{\A/}, '')
  normalized == 'AGENTS.md' || normalized == 'docs' || normalized.start_with?('docs/')
end
leaks = site.pages.map(&:path).select(&repository_doc)
leaks.concat(site.static_files.map(&:relative_path).select(&repository_doc))
errors = []
payload = site.site_payload
site.pages.each do |page|
  begin
    Jekyll::Renderer.new(site, page, payload).run
  rescue StandardError => error
    errors << { 'path' => page.path, 'error' => "#{error.class}: #{error.message}" }
  end
end
result = {
  'jekyll' => Jekyll::VERSION,
  'optional_front_matter' => Gem.loaded_specs.fetch('jekyll-optional-front-matter').version.to_s,
  'baseurl' => config['baseurl'],
  'pages_checked' => site.pages.length,
  'repository_document_leaks' => leaks.uniq,
  'render_errors' => errors
}
FileUtils.mkdir_p(output)
File.write(File.join(output, 'pages-check.json'), JSON.pretty_generate(result), mode: 'w:UTF-8')
puts JSON.pretty_generate(result)
exit(leaks.empty? && errors.empty? ? 0 : 1)
