---
layout: post
title: "kvision -- 灰度 5GrayScale"
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
permalink: /kvision/5GrayScale
date: 2022-10-10 23:14:23 +0800
layoutclear: false
archived: true
---

<style>
.captioned-img img.lazyloaded { border-radius: 0px; border: #f0f0f0; border-width: 1px; }
div.page { max-width: 100%; }
</style>

**原图** vs **逼近效果** vs **目标效果**

{% include image.html url="/kvision/ksample/5GrayScale/01.jpg" width="30%" url2="/kvision/ksample/5GrayScale/01.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/01.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/02.jpg" width="30%" url2="/kvision/ksample/5GrayScale/02.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/02.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/03.jpg" width="30%" url2="/kvision/ksample/5GrayScale/03.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/03.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/04.jpg" width="30%" url2="/kvision/ksample/5GrayScale/04.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/04.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/05.jpg" width="30%" url2="/kvision/ksample/5GrayScale/05.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/05.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/06.jpg" width="30%" url2="/kvision/ksample/5GrayScale/06.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/06.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/07.jpg" width="30%" url2="/kvision/ksample/5GrayScale/07.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/07.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/08.jpg" width="30%" url2="/kvision/ksample/5GrayScale/08.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/08.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/09.jpg" width="30%" url2="/kvision/ksample/5GrayScale/09.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/09.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/10.jpg" width="30%" url2="/kvision/ksample/5GrayScale/10.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/10.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/11.jpg" width="30%" url2="/kvision/ksample/5GrayScale/11.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/11.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/12.jpg" width="30%" url2="/kvision/ksample/5GrayScale/12.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/12.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/13.jpg" width="30%" url2="/kvision/ksample/5GrayScale/13.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/13.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/14.png" width="30%" url2="/kvision/ksample/5GrayScale/14.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/14.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/15.jpg" width="30%" url2="/kvision/ksample/5GrayScale/15.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/15.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/16.jpg" width="30%" url2="/kvision/ksample/5GrayScale/16.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/16.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/17.jpg" width="30%" url2="/kvision/ksample/5GrayScale/17.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/17.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/18.jpg" width="30%" url2="/kvision/ksample/5GrayScale/18.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/18.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/19.png" width="30%" url2="/kvision/ksample/5GrayScale/19.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/19.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/20.jpg" width="30%" url2="/kvision/ksample/5GrayScale/20.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/20.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/21.jpg" width="30%" url2="/kvision/ksample/5GrayScale/21.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/21.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/22.jpg" width="30%" url2="/kvision/ksample/5GrayScale/22.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/22.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/23.jpg" width="30%" url2="/kvision/ksample/5GrayScale/23.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/23.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/24.jpg" width="30%" url2="/kvision/ksample/5GrayScale/24.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/24.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/25.jpg" width="30%" url2="/kvision/ksample/5GrayScale/25.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/25.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/26.jpg" width="30%" url2="/kvision/ksample/5GrayScale/26.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/26.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/27.jpg" width="30%" url2="/kvision/ksample/5GrayScale/27.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/27.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/28.jpg" width="30%" url2="/kvision/ksample/5GrayScale/28.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/28.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/29.jpg" width="30%" url2="/kvision/ksample/5GrayScale/29.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/29.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/30.jpg" width="30%" url2="/kvision/ksample/5GrayScale/30.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/30.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/31.jpg" width="30%" url2="/kvision/ksample/5GrayScale/31.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/31.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/32.jpg" width="30%" url2="/kvision/ksample/5GrayScale/32.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/32.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/33.jpg" width="30%" url2="/kvision/ksample/5GrayScale/33.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/33.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/34.jpg" width="30%" url2="/kvision/ksample/5GrayScale/34.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/34.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/35.jpg" width="30%" url2="/kvision/ksample/5GrayScale/35.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/35.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/36.png" width="30%" url2="/kvision/ksample/5GrayScale/36.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/36.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/37.png" width="30%" url2="/kvision/ksample/5GrayScale/37.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/37.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/38.png" width="30%" url2="/kvision/ksample/5GrayScale/38.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/38.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/39.jpg" width="30%" url2="/kvision/ksample/5GrayScale/39.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/39.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/40.jpg" width="30%" url2="/kvision/ksample/5GrayScale/40.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/40.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/41.png" width="30%" url2="/kvision/ksample/5GrayScale/41.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/41.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/42.jfif" width="30%" url2="/kvision/ksample/5GrayScale/42.jfif.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/42.jfif.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/43.jpg" width="30%" url2="/kvision/ksample/5GrayScale/43.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/43.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/44.jpg" width="30%" url2="/kvision/ksample/5GrayScale/44.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/44.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/45.jpg" width="30%" url2="/kvision/ksample/5GrayScale/45.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/45.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/46.jpg" width="30%" url2="/kvision/ksample/5GrayScale/46.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/46.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/47.jpg" width="30%" url2="/kvision/ksample/5GrayScale/47.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/47.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/48.webp" width="30%" url2="/kvision/ksample/5GrayScale/48.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/48.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/49.jpg" width="30%" url2="/kvision/ksample/5GrayScale/49.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/49.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/50.webp" width="30%" url2="/kvision/ksample/5GrayScale/50.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/50.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/51.jfif" width="30%" url2="/kvision/ksample/5GrayScale/51.jfif.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/51.jfif.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/52.jpg" width="30%" url2="/kvision/ksample/5GrayScale/52.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/52.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/53.webp" width="30%" url2="/kvision/ksample/5GrayScale/53.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/53.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/54.webp" width="30%" url2="/kvision/ksample/5GrayScale/54.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/54.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/55.webp" width="30%" url2="/kvision/ksample/5GrayScale/55.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/55.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/56.webp" width="30%" url2="/kvision/ksample/5GrayScale/56.webp.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/56.webp.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/57.jpg" width="30%" url2="/kvision/ksample/5GrayScale/57.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/57.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/58.png" width="30%" url2="/kvision/ksample/5GrayScale/58.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/58.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/59.jpg" width="30%" url2="/kvision/ksample/5GrayScale/59.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/59.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/60.jpg" width="30%" url2="/kvision/ksample/5GrayScale/60.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/60.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/61.jpg" width="30%" url2="/kvision/ksample/5GrayScale/61.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/61.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/62.jpg" width="30%" url2="/kvision/ksample/5GrayScale/62.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/62.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/63.jpg" width="30%" url2="/kvision/ksample/5GrayScale/63.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/63.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/64.jpg" width="30%" url2="/kvision/ksample/5GrayScale/64.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/64.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/65.jpg" width="30%" url2="/kvision/ksample/5GrayScale/65.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/65.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/66.jpg" width="30%" url2="/kvision/ksample/5GrayScale/66.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/66.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/67.jpg" width="30%" url2="/kvision/ksample/5GrayScale/67.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/67.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/68.jpg" width="30%" url2="/kvision/ksample/5GrayScale/68.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/68.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/69.jpg" width="30%" url2="/kvision/ksample/5GrayScale/69.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/69.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/70.jpg" width="30%" url2="/kvision/ksample/5GrayScale/70.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/70.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/71.jpg" width="30%" url2="/kvision/ksample/5GrayScale/71.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/71.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/72.jpg" width="30%" url2="/kvision/ksample/5GrayScale/72.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/72.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/73.png" width="30%" url2="/kvision/ksample/5GrayScale/73.png.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/73.png.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/74.jpg" width="30%" url2="/kvision/ksample/5GrayScale/74.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/74.jpg.guide.png" width3="30%" %}
{% include image.html url="/kvision/ksample/5GrayScale/75.jpg" width="30%" url2="/kvision/ksample/5GrayScale/75.jpg.result.png" width2="30%" url3="/kvision/ksample/5GrayScale/75.jpg.guide.png" width3="30%" %}
ok



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/kvision/5GrayScale.md.js" %}'></script></p>
