---
layout: post
title: "编程与调试 -- 一个让人惊讶的 python Note"
author:
location: "珠海"
categories: ["编程与调试"]
tags: ["编程"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

```python
import time

gcount = 0
xdef = {}
# 定义成 def func(t=set(), x={}, dep=0): 也是同样的输出。
def func(t=set(), x=xdef, dep=0):
    global gcount
    gcount += 1
    t.add(gcount)
    x[gcount] = gcount
    print(t, x)
    if dep < 3:
        func(t, x, dep+1)

if __name__ == "__main__":
    func()
    time.sleep(1)
    func()
    exit(0)
```

输出是：
```
{1} {1: 1}
{1, 2} {1: 1, 2: 2}
{1, 2, 3} {1: 1, 2: 2, 3: 3}
{1, 2, 3, 4} {1: 1, 2: 2, 3: 3, 4: 4}
{1, 2, 3, 4, 5} {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
{1, 2, 3, 4, 5, 6} {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
{1, 2, 3, 4, 5, 6, 7} {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
{1, 2, 3, 4, 5, 6, 7, 8} {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
```

瞬间感觉以前的代码貌似有很多 bug。

问题出在你的代码中使用了可变的默认参数，如 `t=set()` 和 `x=xdef` 。在 Python 中，可变的默认参数（比如 `set` 和 `dict` ）是会在函数调用间共享的，这意味着在递归调用或者多次调用同一函数时，这些对象会被修改并持续累积，导致意想不到的行为。


### 解释输出：

1. **第一次调用 `func()` ** ：第一次调用时， `t` 和 `x` 作为默认参数会被初始化为空集合和空字典， `gcount` 会在递归中递增， `t` 和 `x` 会按预期被修改。

2. **第二次调用 `func()` ** ：你在 `time.sleep(1)` 后再次调用 `func()` ，此时 `t` 和 `x` 还是上一次调用时的对象（它们是可变的），导致它们继续累积之前的值。所以输出就变成了从第一次调用继续递增的结果。


### 问题的原因：

默认参数是在函数定义时计算的，而不是在调用时。这就导致了 `t` 和 `x` 在多次调用中会共享同一个实例。


### 解决办法：

要避免这个问题，可以将默认参数设为 `None` ，然后在函数内部判断是否为 `None` ，如果是，则创建新的对象。这样每次调用时就会有新的 `set` 和 `dict` 实例，不会共享。

修改后的代码如下：

```python
import time

gcount = 0
xdef = {}

def func(t=None, x=None, dep=0):
    global gcount
    if t is None:
        t = set()
    if x is None:
        x = {}

    gcount += 1
    t.add(gcount)
    x[gcount] = gcount
    print(t, x)
    if dep < 3:
        func(t, x, dep+1)

if __name__ == "__main__":
    func()
    time.sleep(1)
    func()
    exit(0)
```


### 解释修改的地方：

- ** `t=None` 和 `x=None` ** ：将默认参数设为 `None` ，这样每次调用时， `t` 和 `x` 都是新的对象，不会与上一次的调用共享。

- **在函数内部** ：检查 `t` 和 `x` 是否为 `None` ，如果是，就创建新的集合和字典。


### 修改后的预期输出：

执行修改后的代码，输出应该是这样的：

```
{1} {1: 1}
{1, 2} {1: 1, 2: 2}
{1, 2, 3} {1: 1, 2: 2, 3: 3}
{1, 2, 3, 4} {1: 1, 2: 2, 3: 3, 4: 4}
{5} {5: 5}
{5, 6} {5: 5, 6: 6}
{5, 6, 7} {5: 5, 6: 6, 7: 7}
{8, 5, 6, 7} {5: 5, 6: 6, 7: 7, 8: 8}
```

这样，每次调用 `func()` 时，都会用新的 `t` 和 `x` ，不会出现跨调用的共享问题，输出也符合预期。



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-12-12-a-python-note.md.js" %}'></script></p>
