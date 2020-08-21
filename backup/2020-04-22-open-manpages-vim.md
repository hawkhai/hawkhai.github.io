---
layout: post
title: "Open man pages in Vim"
location: "Japan"
tags: [man, manual, vim]
---

Most of the time when I open a man page for a certain command or tool, I use Vim:

{% highlight shell %}
# Open man page for the 'dd' command:
$ man dd | col -b | vim -MR -
{% endhighlight %}

It's actually a handful to type but since I use [zsh](https://www.zsh.org/) + [fzf](https://github.com/junegunn/fzf), it's not really a big deal as recalling the command is pretty straightforward.

But yesterday, I came across this nifty little plugin called [vim-manpager](https://github.com/lambdalisue/vim-manpager). I tried adding it to my vimrc, added the environment variable below to my zshrc:

{% highlight shell %}
export MANPAGER="vim -c MANPAGER -"
{% endhighlight %}

And now, I can open all man pages by calling the `man` command directly. I can also open man pages directly from within Vim. Brilliant!
