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
mermaid: true
glslcanvas:
codeprint:
---

用 Jekyll Markdown 写 blog 文档，受到一些限制，通过 JS 扩展了几个简单的语法。


## Mermaid 流程图


### 新引擎结构图

```
<div class="mermaid">
graph TB
    subgraph 引擎
        Irrlicht(Irrlicht) --> OpenGL[Driver OpenGL]
        Irrlicht --> OpenGLES[Driver OpenGL ES]
        OpenGL -- "OpenGL" --> Windows[Windows]
        OpenGLES -- "OpenGL ES" --> Emulator[OpenGL ES Emulator]
        Emulator -- "OpenGL" --> Windows
        OpenGLES -- "OpenGL ES" --> Android
        OpenGLES -- "OpenGL ES" --> iOS
    end

    subgraph 特效
        Windows -.- OpenGLShader>支持 OpenGL 特效]
        Windows -.- OpenGLESShader>支持 OpenGL ES 特效]
        Android -.- OpenGLESShader
        iOS -.- OpenGLESShader
    end

    新引擎结构图

classDef orange fill:#f96;
classDef yellow fill:#fefe00;
classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;
class Irrlicht orange;
class Windows orange;
class Android orange;
class iOS orange;
class OpenGL yellow;
class OpenGLES yellow;
class 新引擎结构图 titlec;
class OpenGLShader dotbox;
class OpenGLESShader dotbox;
</div>
```

<div class="mermaid">
graph TB
    subgraph 引擎
        Irrlicht(Irrlicht) --> OpenGL[Driver OpenGL]
        Irrlicht --> OpenGLES[Driver OpenGL ES]
        OpenGL -- "OpenGL" --> Windows[Windows]
        OpenGLES -- "OpenGL ES" --> Emulator[OpenGL ES Emulator]
        Emulator -- "OpenGL" --> Windows
        OpenGLES -- "OpenGL ES" --> Android
        OpenGLES -- "OpenGL ES" --> iOS
    end

    subgraph 特效
        Windows -.- OpenGLShader>支持 OpenGL 特效]
        Windows -.- OpenGLESShader>支持 OpenGL ES 特效]
        Android -.- OpenGLESShader
        iOS -.- OpenGLESShader
    end

    新引擎结构图

classDef orange fill:#f96;
classDef yellow fill:#fefe00;
classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;
class Irrlicht orange;
class Windows orange;
class Android orange;
class iOS orange;
class OpenGL yellow;
class OpenGLES yellow;
class 新引擎结构图 titlec;
class OpenGLShader dotbox;
class OpenGLESShader dotbox;
</div>


### 第一组配色

```
<div class="mermaid">
graph TB
    subgraph 第一组配色
        橙色 [橙色<br/>#F93]
        淡橙色 [淡橙色<br/>#FFB366]
        蓝色 [蓝色<br/>#66B2FF]
        淡紫色 [淡紫色<br/>#CCE5FF]
        绿色 [绿色<br/>#6F6]
        浅蓝色 [浅蓝色<br/>#9FF]
        黄色 [黄色<br/>#FF0]
    end

    DEMO

classDef corange   fill:#F93;
classDef corangelt fill:#FFB366;
classDef cblue     fill:#66B2FF;
classDef cpurplelt fill:#CCE5FF;
classDef cgreen    fill:#6F6;
classDef cbluelt   fill:#9FF;
classDef cyellow   fill:#FF0;

classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;

class 橙色 corange;
class 淡橙色 corangelt;
class 蓝色 cblue;
class 淡紫色 cpurplelt;
class 绿色 cgreen;
class 浅蓝色 cbluelt;
class 黄色 cyellow;
class DEMO titlec;
</div>
```

<div class="mermaid">
graph TB
    subgraph 第一组配色
        橙色[橙色<br/>#F93]
        淡橙色[淡橙色<br/>#FFB366]
        蓝色[蓝色<br/>#66B2FF]
        淡紫色[淡紫色<br/>#CCE5FF]
        绿色[绿色<br/>#6F6]
        浅蓝色[浅蓝色<br/>#9FF]
        黄色[黄色<br/>#FF0]
    end

    DEMO

classDef corange   fill:#F93;
classDef corangelt fill:#FFB366;
classDef cblue     fill:#66B2FF;
classDef cpurplelt fill:#CCE5FF;
classDef cgreen    fill:#6F6;
classDef cbluelt   fill:#9FF;
classDef cyellow   fill:#FF0;

classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;

class 橙色 corange;
class 淡橙色 corangelt;
class 蓝色 cblue;
class 淡紫色 cpurplelt;
class 绿色 cgreen;
class 浅蓝色 cbluelt;
class 黄色 cyellow;
class DEMO titlec;
</div>


### 第二组配色

<div class="mermaid">
graph TB
    subgraph 第二组配色
        靛蓝色[靛蓝色<br/>#4273c1]
        绿色2[绿色2<br/>#6eaf49]
        灰色2[灰色2<br/>#a1a5a6]
        蓝色2[蓝色2<br/>#5c9ad1]
        黄色2[黄色2<br/>#fbbe04]
        橙色2[橙色2<br/>#ea7c2e]
    end

    DEMO2

classDef indigo    fill:#4273c1;
classDef green     fill:#6eaf49;
classDef gray      fill:#a1a5a6;
classDef blue      fill:#5c9ad1;
classDef yellow    fill:#fbbe04;
classDef orange    fill:#ea7c2e;

classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;

class DEMO2 titlec;

class 靛蓝色 indigo;
class 绿色2 green;
class 灰色2 gray;
class 蓝色2 blue;
class 黄色2 yellow;
class 橙色2 orange;
</div>

```
<div class="mermaid">
graph TB
    subgraph 第二组配色
        靛蓝色[靛蓝色<br/>#4273c1]
        绿色2[绿色2<br/>#6eaf49]
        灰色2[灰色2<br/>#a1a5a6]
        蓝色2[蓝色2<br/>#5c9ad1]
        黄色2[黄色2<br/>#fbbe04]
        橙色2[橙色2<br/>#ea7c2e]
    end

    DEMO2

classDef indigo    fill:#4273c1;
classDef green     fill:#6eaf49;
classDef gray      fill:#a1a5a6;
classDef blue      fill:#5c9ad1;
classDef yellow    fill:#fbbe04;
classDef orange    fill:#ea7c2e;

classDef dotbox fill:#ffc864,stroke:#f668,stroke-width:1px;
classDef titlec fill:#ccc1,stroke:#aaa4,stroke-width:1px,stroke:1;

class DEMO2 titlec;

class 靛蓝色 indigo;
class 绿色2 green;
class 灰色2 gray;
class 蓝色2 blue;
class 黄色2 yellow;
class 橙色2 orange;
</div>
```


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


### 样例

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


### 样例

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
