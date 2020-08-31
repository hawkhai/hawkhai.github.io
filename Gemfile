source 'https://rubygems.org'

require 'json'
require 'open-uri'
versions = JSON.parse(open('https://pages.github.com/versions.json').read)

# versions['github-pages'] -> 207
gem 'github-pages', 207, group: :jekyll_plugins

gem "therubyracer"

gem 'wdm', '>= 0.1.0' if Gem.win_platform?
