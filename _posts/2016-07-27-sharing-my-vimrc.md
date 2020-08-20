---
layout: post
title: "Sharing my .vimrc"
location: "Japan"
categories: ["Code"]
comments: true
---

Vim has always been my go to editor/IDE when I'm outside of Visual Studio. Here's my base `_vimrc` for Windows.

{% highlight conf %}
let mapleader = " "

filetype off
syntax on
colorscheme darkblue

" let pc=$PC
" if pc == 'HOME'
"     set guifont=Letter\ Gothic\ Std:h11
" else
"     set guifont=Lucida\ Sans\ Typewriter:h9
" endif

" Save marks to up to 100 files, save global marks as well (f1). To disable, f0
set viminfo='100,f1

" Folding options
set foldmethod=indent
set foldnestmax=20
set nofoldenable
set foldlevel=0

set guifont=Lucida\ Sans\ Typewriter
set lines=70 columns=160
set ai
set nu
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set wrap
set backspace=2
set encoding=utf-8
set fileencodings=utf-8
set nocompatible
set noswapfile
set shortmess+=I
set ignorecase
set guioptions-=T
set guioptions-=r
set guioptions-=m
set splitright
set splitbelow
set ruler
set rtp+=$HOME/vimfiles/bundle/Vundle.vim/
call vundle#begin('$USERPROFILE/vimfiles/bundle/')
Plugin 'VundleVim/Vundle.vim'
" 1. Vim should be 64-bit (link in ycm site)
" 2. Python should be 64-bit
Plugin 'Valloric/YouCompleteMe'
Plugin 'fatih/vim-go'
Plugin 'PProvost/vim-ps1'
call vundle#end()
filetype plugin indent on
" To ignore plugin indent changes, instead use:
" filetype plugin on
" let g:netrw_liststyle=3

let g:ycm_disable_for_files_larger_than_kb = 0
let g:ycm_autoclose_preview_window_after_completion = 1

" Enable powershell syntax plug
autocmd BufNewFile,BufReadPost *.ps1 set filetype=ps1

" Search for the word under cursor in the current dir (recursively)
command CSM :execute "vimgrep /" . expand("<cword>") . "/j ** <Bar> :cw"
nnoremap <leader>ms :CSM<CR>

" Simple mappings for window manipulations
nnoremap <leader>wq <C-W>q
nnoremap <leader>ws <C-W>s
nnoremap <leader>wv <C-W>v
nnoremap <leader><left><left> <C-W><left>
nnoremap <leader><right><right> <C-W><right>
nnoremap <leader><up><up> <C-W><up>
nnoremap <leader><down><down> <C-W><down>

" Display buffers, then prep the colon for the next command
nnoremap <leader>b :ls<CR>:

" Shortcut for save
nnoremap <leader>s :w<CR>

" Shortcut for netrw explorer
nnoremap <leader>e :e.<CR>

" JSON pretty print (all buffer)
nnoremap <leader>pj :%!python -m json.tool<CR>

" Diff all windows (should prep 2 windows for this)
nnoremap <leader>dt :windo diffthis<CR>
nnoremap <leader>do :windo diffoff!<CR>
{% endhighlight %}

And here's my base `.vimrc` for Linux and OSX.

{% highlight conf %}
let mapleader = " "

filetype off
syntax on
colorscheme elflord
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'jelera/vim-javascript-syntax'
Plugin 'fatih/vim-go'
Plugin 'majutsushi/tagbar'
call vundle#end()
filetype plugin indent on

" Save marks to up to 100 files, save global marks as well (f1). To disable, f0
set viminfo='100,f1

" Folding options
set foldmethod=indent
set foldnestmax=20
set nofoldenable
set foldlevel=0

set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set autoindent
set nu
set encoding=utf-8
set noswapfile
set shortmess+=I
set backspace=2
set nocompatible
set ignorecase
set splitright
set splitbelow
set ruler
" Temporary enable/disable YouCompleteMe. Active = disable, commented = enable
" let g:loaded_youcompleteme = 1
let g:ycm_global_ycm_extra_conf = "~/.ycm_extra_conf.py"
let g:ycm_disable_for_files_larger_than_kb = 0
let g:ycm_autoclose_preview_window_after_completion = 1

" Options for netrw
let g:netrw_liststyle = 0
let g:netrw_altv = 1

" 1. :PluginInstall
" 2. :GoInstallBinaries (gotags, vim-go)
" 3. Install 'ctags'
" 4. go get -u github.com/jstemmer/gotags
let g:tagbar_type_go = {
    \ 'ctagstype' : 'go',
    \ 'kinds'     : [
        \ 'p:package',
        \ 'i:imports:1',
        \ 'c:constants',
        \ 'v:variables',
        \ 't:types',
        \ 'n:interfaces',
        \ 'w:fields',
        \ 'e:embedded',
        \ 'm:methods',
        \ 'r:constructor',
        \ 'f:functions'
    \ ],
    \ 'sro' : '.',
    \ 'kind2scope' : {
        \ 't' : 'ctype',
        \ 'n' : 'ntype'
    \ },
    \ 'scope2kind' : {
        \ 'ctype' : 't',
        \ 'ntype' : 'n'
    \ },
    \ 'ctagsbin'  : 'gotags',
    \ 'ctagsargs' : '-sort -silent'
\ }

nnoremap <F8> :TagbarToggle<CR>

" Search for the word under cursor in the current dir (recursively)
command CSM execute ":vimgrep /" . expand("<cword>") . "/j ** <Bar> :cw"
nnoremap <leader>ms :CSM<CR>
set wildignore+=jennah

" Simple mappings for window manipulations
nnoremap <leader>wq <C-W>q
nnoremap <leader>ws <C-W>s
nnoremap <leader>wv <C-W>v
nnoremap <leader><left><left> <C-W><left>
nnoremap <leader><right><right> <C-W><right>
nnoremap <leader><up><up> <C-W><up>
nnoremap <leader><down><down> <C-W><down>

" Display buffers, then prep the colon for the next command
nnoremap <leader>b :ls<CR>:

" Shortcut for save
nnoremap <leader>s :w<CR>

" Shortcut for netrw explorer
nnoremap <leader>e :e.<CR>

" JSON pretty print (all buffer)
nnoremap <leader>pj :%!python -m json.tool<CR>

" Diff all windows (should prep 2 windows for this)
nnoremap <leader>dt :windo diffthis<CR>
nnoremap <leader>do :windo diffoff!<CR>

" Highlight/no highlight for search
nnoremap <leader>hl :set hlsearch<CR>
nnoremap <leader>hn :set nohlsearch<CR>

" Diff all windows (should prep two windows for this)
nnoremap <leader>dt :windo diffthis<CR>
nnoremap <leader>do :windo diffoff!<CR>
{% endhighlight %}

### Update (2016/08/24)

Updated `vimrc` can be viewed [here](https://github.com/hawkhai/vim).
