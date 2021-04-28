---
layout: post
title: "开发环境 -- Windows Jekyll Markdown 扩展语法"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "Jekyll"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---

用 Jekyll Markdown 写 blog 文档，受到一些限制，通过 JS 扩展了几个简单的语法。


## 列表插入图片

{% highlight plaintext %}
<span imgid="3.3" />
{{ '{%' }} include image.html url="/assets/images/210402-win-jekyll-ex/gitee.png" caption="..." relocate="3.3" %}
{% endhighlight %}

1. 包含 `relocate` 属性的节点，向前挪动到最近的一个 `ol/ul` 列表对应 index 位置。
2. 可以通过 `<span imgid="3.3" />` 指定位置。


### 实现

```js
function changeImagePositionk() {
    var lrelocate = $("#postdiv div[relocate]");
    lrelocate = $(lrelocate.get().reverse()); // 倒叙，保证多图的情况能正常。
    lrelocate.each(function() {
        var imgnode = $(this);
        var target = imgnode;
        var tname = target[0].tagName.toUpperCase();
        while (tname != "OL" && tname != "UL" && target.length) {
            target = target.prev();
            tname = target[0].tagName.toUpperCase();
        }
        var relocate = imgnode.attr("relocate");
        if (target.length && relocate) {
            // <span imgid="3.3" />
            var insert = target.find("span[imgid='"+relocate+"']");
            if (insert.length) {
                imgnode.insertAfter(insert);
                return;
            }
        }
        var li = relocate.split("."); // ["2", "3"]
        for (var i = 0; i < li.length && target.length; i++) {
            // https://www.cnblogs.com/ooo0/p/6278102.html
            if (i == 0) {
                var children = target.children("li");
                target = children.eq(parseInt(li[i]) - 1);
            } else {
                var children = target.children("ol,ul").children("li");
                target = children.eq(parseInt(li[i]) - 1);
            }
        }
        if (target.length) {
            imgnode.insertAfter(target);
        }
    });
}

// 文档加载完成时
$(document).ready(function () {
    checkTableStyle();
    changeImagePositionk();
});
```


### 样例：

```
1. gitee
2. headw
    * test <span imgid="headw" />
    * test
3. question

{{ '{%' }} include image.html url="/assets/images/210402-win-jekyll-ex/gitee.png" relocate="1" caption="1" width="100px" %}
{{ '{%' }} include image.html url="/assets/images/210402-win-jekyll-ex/question.jpg" relocate="2.2" caption="2.2" width="100px" %}
{{ '{%' }} include image.html url="/assets/images/210402-win-jekyll-ex/headw.png" relocate="headw" caption="headw" width="100px" %}
```

1. gitee
2. headw
    * test <span imgid="headw" />
    * test
3. question

{% include image.html url="/assets/images/210402-win-jekyll-ex/gitee.png" relocate="1" caption="1" width="100px" %}
{% include image.html url="/assets/images/210402-win-jekyll-ex/question.jpg" relocate="2.2" caption="2.2" width="100px" %}
{% include image.html url="/assets/images/210402-win-jekyll-ex/headw.png" relocate="headw" caption="headw" width="100px" %}


## 表格宽度管理

```
<table class="tablestyle" ntablew="2:3:5"></table>
```

Markdown 表格前面加一行，JS 就会根据对应参数调整当前表格的列宽。


### 实现

```js
function setTableStyle(ithis, ratiostr, tablew) {

    if (tablew) {
        ithis.css('width', tablew);
    }

    var li = ratiostr.split(":"); // ["2", "3", "4", "5"]
    var total = 0;
    for (var i = 0; i < li.length; i++) {
        li[i] = parseInt(li[i]);
        total += li[i];
    }
    if (total <= 0) {
        return;
    }
    for (var i = 0; i < li.length; i++) {
        li[i] = li[i] / total * 100;
        var selector = 'th:nth-of-type(' + (i+1) + '),td:nth-of-type(' + (i+1) + ')';
        var width = li[i] + '%';
        // th:nth-of-type(n+2) -- 支持表达式 n+2 之类的
        // https://www.w3school.com.cn/cssref/css_selectors.asp
        ithis.find(selector).each(function() {
            $(this).css('width', width);
        });
    }
}

function checkTableStyle() {
    // 先给所有 table 编号。
    $("table").each(function() {
        var $this = $(this);
        if (!$this.attr("tsNumbered")) {
            $this.attr("tsNumbered", 1);
            var number = $.fn.tsNumber;
            $.fn.tsNumber++;
            $this.attr("tsNumber", number);
        }
    });
    $("table.tablestyle").each(function() {
        var $this = $(this);
        var ratiostr = $this.attr("ntablew");
        var number = parseInt($this.attr("tsNumber"));
        var tablew = $this.attr("tablew");
        $this.remove(); // $this.hide();
        if (!ratiostr) {
            return;
        }

        $("table").each(function() {
            var ithis = $(this);
            var inumber = parseInt(ithis.attr("tsNumber"));
            // 紧接着的那个 table
            if (inumber == number + 1) {
                setTableStyle(ithis, ratiostr, tablew);
            }
        });
    });
}

// 文档加载完成时
$(document).ready(function () {
    checkTableStyle();
});
```


### 样例：

```
<table class="tablestyle" ntablew="2:3:5"></table>

| A | B | C |
| ---- | ---- | ---- |
| 2 | 3 | 5 |
```

<table class="tablestyle" ntablew="2:3:5"></table>

| A | B | C |
| ---- | ---- | ---- |
| 2 | 3 | 5 |

<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2021-04-02-win-jekyll-ex.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.cnblogs.com/ooo0/p/6278102.html]({% include relrefx.html url="/backup/2021-04-02-win-jekyll-ex.md/www.cnblogs.com/b0b3e429.html" %})
- [https://www.w3school.com.cn/cssref/css_selectors.asp]({% include relrefx.html url="/backup/2021-04-02-win-jekyll-ex.md/www.w3school.com.cn/ee1d6669.asp" %})
