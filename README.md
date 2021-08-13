This is a modified version of [Gaurav Chaurasia's Much-Worse Jekyll theme {% include relref_github.html %}](https://github.com/gchauras/much-worse-jekyll-theme/).

Source for [https://blog.hawkhai.com](https://blog.hawkhai.com).

Source for [https://sunocean.life/blog](https://sunocean.life/blog).


# Windows Environment setup

搭建 Windows Jekyll 环境

<https://blog.hawkhai.com/blog/2020/08/29/win-jekyll-install>


# Environment setup

```bash
$ sudo apt-get install nodejs git curl zlib1g-dev build-essential libssl-dev \
    libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev \
    libcurl4-openssl-dev python3-software-properties libffi-dev ruby-dev

$ git clone https://github.com/rbenv/rbenv.git ~/.rbenv
$ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(rbenv init -)"' >> ~/.bashrc
$ exec $SHELL

$ git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
$ echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
$ exec $SHELL

$ # mkdir ~/.rbenv/cache/
$ # mv ruby-2.3.1.tar.bz2 ~/.rbenv/cache/

$ rbenv install 2.3.1
$ rbenv global 2.3.1
$ ruby -v

$ gem install bundler
$ rbenv rehash
```

Troubleshooting:
<https://gems.ruby-china.com/>
bundle update json

Then in the root of the project:

```
$ bundle install
```

Host using local server:

```
$ bundle exec jekyll serve --host 0.0.0.0 --port [port]
```


# Troubleshooting

- If build for ruby2.3.1 fails, refer to <https://github.com/rbenv/ruby-build/wiki>.



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/README.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://github.com/gchauras/much-worse-jekyll-theme/]({% include relrefx.html url="/backup/README.md/github.com/14f1bec6.html" %})
- [https://blog.hawkhai.com]({% include relrefx.html url="/backup/README.md/blog.hawkhai.com/051e312b.html" %})
- [https://github.com/rbenv/rbenv.git]({% include relrefx.html url="/backup/README.md/github.com/309fee20.html" %})
- [https://github.com/rbenv/ruby-build.git]({% include relrefx.html url="/backup/README.md/github.com/48bc0079.html" %})
- [https://gems.ruby-china.com/]({% include relrefx.html url="/backup/README.md/gems.ruby-china.com/6d6c20fb.html" %})
- [https://github.com/rbenv/ruby-build/wiki]({% include relrefx.html url="/backup/README.md/github.com/4c7e830d.html" %})
