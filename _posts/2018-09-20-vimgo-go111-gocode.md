---
layout: post
title: "Autocompletion with gocode and vim-go in Go1.11"
location: "Japan"
tags: [vim, vim-go, gocode, autocomplete]
---

I use [vim](https://github.com/vim/vim) with [vim-go](https://github.com/fatih/vim-go) as my main editor for Go-based projects (and for anything else, really). Recently, I've upgraded to Go1.11 and my autocompletion stopped working. I know `vim-go` uses [gocode](https://github.com/mdempsky/gocode) as it's autocompletion engine but since `vim-go`'s `:GoInstallBinaries` command handled the installation for me, I didn't really have to think about it. Fortunately, a quick update to my [vimrc](https://github.com/hawkhai/.files/blob/master/vimrc) file did the trick for me. I just had to add `Plugin 'mdempsky/gocode', {'rtp': 'vim/'}` to my `vimrc` (I use [Vundle](https://github.com/VundleVim/Vundle.vim)) and run `:PluginInstall` again. Works a treat.
