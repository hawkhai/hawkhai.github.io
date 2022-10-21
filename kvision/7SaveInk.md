---
layout: post
title: "kvision -- 省墨 7SaveInk.md"
author: yqh
location: "珠海"
categories: ["工作笔记"]
tags: ["工作笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid: true
glslcanvas:
codeprint:
permalink: /kvision/7SaveInk
date: 2022-10-10 23:14:23 +0800
layoutclear: false
archived: true
---

<style>
.captioned-img img.lazyloaded { border-radius: 0px; border: #f0f0f0; border-width: 1px; }
div.page { max-width: 100%; }
</style>

**原图** vs **逼近效果** vs **目标效果**

{% include image.html url="/kvision/ksample/7SaveInk/01.jpg" width="30%" url2="/kvision/ksample/7SaveInk/01.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/01.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/02.jpg" width="30%" url2="/kvision/ksample/7SaveInk/02.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/02.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/03.jpg" width="30%" url2="/kvision/ksample/7SaveInk/03.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/03.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/04.jpg" width="30%" url2="/kvision/ksample/7SaveInk/04.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/04.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/05.jpg" width="30%" url2="/kvision/ksample/7SaveInk/05.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/05.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/06.jpg" width="30%" url2="/kvision/ksample/7SaveInk/06.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/06.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/07.jpg" width="30%" url2="/kvision/ksample/7SaveInk/07.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/07.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/08.jpg" width="30%" url2="/kvision/ksample/7SaveInk/08.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/08.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/09.jpg" width="30%" url2="/kvision/ksample/7SaveInk/09.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/09.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/10.jpg" width="30%" url2="/kvision/ksample/7SaveInk/10.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/10.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/11.jpg" width="30%" url2="/kvision/ksample/7SaveInk/11.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/11.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/12.jpg" width="30%" url2="/kvision/ksample/7SaveInk/12.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/12.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/13.jpg" width="30%" url2="/kvision/ksample/7SaveInk/13.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/13.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/14.png" width="30%" url2="/kvision/ksample/7SaveInk/14.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/14.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/15.jpg" width="30%" url2="/kvision/ksample/7SaveInk/15.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/15.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/16.jpg" width="30%" url2="/kvision/ksample/7SaveInk/16.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/16.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/17.jpg" width="30%" url2="/kvision/ksample/7SaveInk/17.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/17.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/18.jpg" width="30%" url2="/kvision/ksample/7SaveInk/18.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/18.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/19.png" width="30%" url2="/kvision/ksample/7SaveInk/19.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/19.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/20.jpg" width="30%" url2="/kvision/ksample/7SaveInk/20.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/20.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/21.jpg" width="30%" url2="/kvision/ksample/7SaveInk/21.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/21.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/22.jpg" width="30%" url2="/kvision/ksample/7SaveInk/22.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/22.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/23.jpg" width="30%" url2="/kvision/ksample/7SaveInk/23.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/23.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/24.jpg" width="30%" url2="/kvision/ksample/7SaveInk/24.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/24.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/25.jpg" width="30%" url2="/kvision/ksample/7SaveInk/25.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/25.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/26.jpg" width="30%" url2="/kvision/ksample/7SaveInk/26.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/26.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/27.jpg" width="30%" url2="/kvision/ksample/7SaveInk/27.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/27.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/28.jpg" width="30%" url2="/kvision/ksample/7SaveInk/28.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/28.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/29.jpg" width="30%" url2="/kvision/ksample/7SaveInk/29.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/29.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/30.jpg" width="30%" url2="/kvision/ksample/7SaveInk/30.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/30.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/31.jpg" width="30%" url2="/kvision/ksample/7SaveInk/31.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/31.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/32.jpg" width="30%" url2="/kvision/ksample/7SaveInk/32.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/32.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/33.jpg" width="30%" url2="/kvision/ksample/7SaveInk/33.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/33.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/34.jpg" width="30%" url2="/kvision/ksample/7SaveInk/34.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/34.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/35.jpg" width="30%" url2="/kvision/ksample/7SaveInk/35.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/35.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/36.png" width="30%" url2="/kvision/ksample/7SaveInk/36.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/36.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/37.png" width="30%" url2="/kvision/ksample/7SaveInk/37.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/37.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/38.png" width="30%" url2="/kvision/ksample/7SaveInk/38.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/38.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/39.jpg" width="30%" url2="/kvision/ksample/7SaveInk/39.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/39.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/40.jpg" width="30%" url2="/kvision/ksample/7SaveInk/40.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/40.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/41.png" width="30%" url2="/kvision/ksample/7SaveInk/41.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/41.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/42.jfif" width="30%" url2="/kvision/ksample/7SaveInk/42.jfif.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/42.jfif.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/43.jpg" width="30%" url2="/kvision/ksample/7SaveInk/43.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/43.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/44.jpg" width="30%" url2="/kvision/ksample/7SaveInk/44.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/44.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/45.jpg" width="30%" url2="/kvision/ksample/7SaveInk/45.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/45.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/46.jpg" width="30%" url2="/kvision/ksample/7SaveInk/46.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/46.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/47.jpg" width="30%" url2="/kvision/ksample/7SaveInk/47.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/47.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/48.webp" width="30%" url2="/kvision/ksample/7SaveInk/48.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/48.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/49.jpg" width="30%" url2="/kvision/ksample/7SaveInk/49.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/49.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/50.webp" width="30%" url2="/kvision/ksample/7SaveInk/50.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/50.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/51.jfif" width="30%" url2="/kvision/ksample/7SaveInk/51.jfif.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/51.jfif.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/52.jpg" width="30%" url2="/kvision/ksample/7SaveInk/52.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/52.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/53.webp" width="30%" url2="/kvision/ksample/7SaveInk/53.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/53.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/54.webp" width="30%" url2="/kvision/ksample/7SaveInk/54.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/54.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/55.webp" width="30%" url2="/kvision/ksample/7SaveInk/55.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/55.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/56.webp" width="30%" url2="/kvision/ksample/7SaveInk/56.webp.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/56.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/57.jpg" width="30%" url2="/kvision/ksample/7SaveInk/57.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/57.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/58.png" width="30%" url2="/kvision/ksample/7SaveInk/58.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/58.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/59.jpg" width="30%" url2="/kvision/ksample/7SaveInk/59.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/59.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/60.jpg" width="30%" url2="/kvision/ksample/7SaveInk/60.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/60.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/61.jpg" width="30%" url2="/kvision/ksample/7SaveInk/61.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/61.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/62.jpg" width="30%" url2="/kvision/ksample/7SaveInk/62.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/62.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/63.jpg" width="30%" url2="/kvision/ksample/7SaveInk/63.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/63.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/64.jpg" width="30%" url2="/kvision/ksample/7SaveInk/64.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/64.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/65.jpg" width="30%" url2="/kvision/ksample/7SaveInk/65.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/65.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/66.jpg" width="30%" url2="/kvision/ksample/7SaveInk/66.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/66.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/67.jpg" width="30%" url2="/kvision/ksample/7SaveInk/67.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/67.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/68.jpg" width="30%" url2="/kvision/ksample/7SaveInk/68.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/68.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/69.jpg" width="30%" url2="/kvision/ksample/7SaveInk/69.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/69.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/70.jpg" width="30%" url2="/kvision/ksample/7SaveInk/70.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/70.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/71.jpg" width="30%" url2="/kvision/ksample/7SaveInk/71.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/71.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/72.jpg" width="30%" url2="/kvision/ksample/7SaveInk/72.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/72.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/73.png" width="30%" url2="/kvision/ksample/7SaveInk/73.png.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/73.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/74.jpg" width="30%" url2="/kvision/ksample/7SaveInk/74.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/74.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/7SaveInk/75.jpg" width="30%" url2="/kvision/ksample/7SaveInk/75.jpg.result.png" width2="30%" url3="/kvision/ksample/7SaveInk/75.jpg.guide.png" width3="30%" %}
ok



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/kvision/7SaveInk.md.js" %}'></script></p>
