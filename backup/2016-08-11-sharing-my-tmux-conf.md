---
layout: post
title: "Sharing my .tmux.conf"
location: "Japan"
categories: ["Code"]
comments: true
---

I use `tmux` heavily and in tandem with `vim`. Much more so now when it's supported on Bash on Windows as well. I don't have to spin up a Linux VM just for the purpose of being my `tmux` "server".

{% highlight conf %}
# Set a Ctrl-b shortcut for reloading tmux config
unbind r
bind r source-file ~/.tmux.conf

# Prefix is Ctrl-a
unbind C-b
set -g prefix C-a
bind C-a send-prefix

# Rename terminals
set -g set-titles on
set -g set-titles-string '#(whoami)@#h@#(curl ipecho.net/plain;echo)'

# Status bar customization
set -g status-bg black
set -g status-fg white
set -g status-interval 5
set -g status-left-length 90
set -g status-right-length 60
set -g status-left "#[fg=Green]#(whoami)#[fg=white]@#[fg=red]#(hostname -s)#[fg=white]|#[fg=yellow]#(curl ipecho.net/plain;echo)#[fg=white]|#[fg=yellow]#(hostname -I)#[fg=white]"
set -g status-justify left
set -g status-right '#[fg=Cyan]#S #[fg=white]%a %d %b %R'

# Easy to remember split pane commands
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %

# Vim friendly settings (from https://gist.github.com/anonymous/6bebae3eb9f7b972e6f0)
setw -g monitor-activity on
set -g visual-activity on
set -g mode-keys vi

# Extend history limit
set -g history-limit 10000
{% endhighlight %}
