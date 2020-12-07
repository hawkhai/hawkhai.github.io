This is a modified version of [Gaurav Chaurasia's Much-Worse Jekyll theme](https://github.com/gchauras/much-worse-jekyll-theme/).

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
https://gems.ruby-china.com/
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

- If build for ruby2.3.1 fails, refer to [https://github.com/rbenv/ruby-build/wiki](https://github.com/rbenv/ruby-build/wiki).

-----

<font class='ref_snapshot'>Reference snapshot, script generated automatically.</font>

- [1] [https://github.com/gchauras/much-worse-jekyll-theme/]({% include relref.html url="/backup/README.md/github.com/14f1bec6fa447d3a3c67adb97e7761e3.html" %})
- [2] [https://blog.hawkhai.com]({% include relref.html url="/backup/README.md/blog.hawkhai.com/051e312bbaa9c18655c485efd49048cf.html" %})
- [3] [https://sunocean.life/blog]({% include relref.html url="/backup/README.md/sunocean.life/72283ac31cee46c8b5bd6e35c8b1183e.html" %})
- [4] [https://github.com/rbenv/rbenv.git]({% include relref.html url="/backup/README.md/github.com/309fee200e6c9e304f8bafd623c8c36e.html" %})
- [5] [https://github.com/rbenv/ruby-build.git]({% include relref.html url="/backup/README.md/github.com/48bc00792a4c5af49565764e26df019d.html" %})
- [6] [https://gems.ruby-china.com/]({% include relref.html url="/backup/README.md/gems.ruby-china.com/6d6c20fba54944a55fd25c8792fad07c.html" %})
- [7] [https://github.com/rbenv/ruby-build/wiki]({% include relref.html url="/backup/README.md/github.com/4c7e830d49c0c4e0b4967ce1b746e0b3.html" %})
