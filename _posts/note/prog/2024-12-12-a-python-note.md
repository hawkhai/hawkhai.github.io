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



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2024-12-12-a-python-note.md.js" %}'></script></p>
