<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="zh-cn"><head>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="https://www.googletagservices.com/activeview/js/current/osd.js?cb=%2Fr20100101"></script><script src="https://partner.googleadservices.com/gampad/cookie.js?domain=www.w3school.com.cn&amp;callback=_gfp_s_&amp;client=ca-pub-3381531532877742"></script><script src="https://pagead2.googlesyndication.com/pagead/js/r20210426/r20190131/show_ads_impl_fy2019.js" id="google_shimpl"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-878633-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-878633-1');
</script>

<meta charset="utf-8" />
<meta name="robots" content="all" />
<meta name="author" content="w3school.com.cn" />
<link rel="stylesheet" type="text/css" href="/c7.css" />

<link rel="icon" type="image/png" sizes="16x16" href="/ui2019/logo-16-red.png" />
<link rel="icon" type="image/png" sizes="32x32" href="/ui2019/logo-32-red.png" />
<link rel="icon" type="image/png" sizes="48x48" href="/ui2019/logo-48-red.png" />
<link rel="icon" type="image/png" sizes="96x96" href="/ui2019/logo-96-red.png" />
<link rel="apple-touch-icon-precomposed" sizes="180x180" href="/ui2019/logo-180.png" />


<title>CSS 选择器参考手册</title>

<meta http-equiv="origin-trial" content="A+b/H0b8RPXNaJgaNFpO0YOFuGK6myDQXlwnJB3SwzvNMfcndat4DZYMrP4ClJIzYWo3/yP2S+8FTZ/lpqbPAAEAAABueyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=" /><meta http-equiv="origin-trial" content="A9ZgbRtm4pU3oZiuNzOsKcC8ppFSZdcjP2qYcdQrFKVzkmiWH1kdYY1Mi9x7G8+PS8HV9Ha9Cz0gaMdKsiVZIgMAAAB7eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="AxL6oBxcpn5rQDPKSAs+d0oxNyJYq2/4esBUh3Yx5z8QfcLu+AU8iFCXYRcr/CEEfDnkxxLTsvXPJFQBxHfvkgMAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A9KPtG5kl3oLTk21xqynDPGQ5t18bSOpwt0w6kGa6dEWbuwjpffmdUpR3W+faZDubGT+KIk2do0BX2ca16x8qAcAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A3HucHUo1oW9s+9kIKz8mLkbcmdaj5lxt3eiIMp1Nh49dkkBlg1Fhg4Fd/r0vL69mRRA36YutI9P/lJUfL8csQoAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A0OysezhLoCRYomumeYlubLurZTCmsjTb087OvtCy95jNM65cfEsbajrJnhaGwiTxhz38ZZbm+UhUwQuXfVPTg0AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="AxoOxdZQmIoA1WeAPDixRAeWDdgs7ZtVFfH2y19ziTgD1iaHE5ZGz2UdSjubkWvob9C5PrjUfkWi4ZSLgWk3Xg8AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A7+rMYR5onPnACrz+niKSeFdH3xw1IyHo2AZSHmxrofRk9w4HcQPMYcpBUKu6OQ6zsdxf4m/vqa6tG6Na4OLpAQAAAB4eyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A+b/H0b8RPXNaJgaNFpO0YOFuGK6myDQXlwnJB3SwzvNMfcndat4DZYMrP4ClJIzYWo3/yP2S+8FTZ/lpqbPAAEAAABueyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=" /><meta http-equiv="origin-trial" content="A9ZgbRtm4pU3oZiuNzOsKcC8ppFSZdcjP2qYcdQrFKVzkmiWH1kdYY1Mi9x7G8+PS8HV9Ha9Cz0gaMdKsiVZIgMAAAB7eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="AxL6oBxcpn5rQDPKSAs+d0oxNyJYq2/4esBUh3Yx5z8QfcLu+AU8iFCXYRcr/CEEfDnkxxLTsvXPJFQBxHfvkgMAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A9KPtG5kl3oLTk21xqynDPGQ5t18bSOpwt0w6kGa6dEWbuwjpffmdUpR3W+faZDubGT+KIk2do0BX2ca16x8qAcAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A3HucHUo1oW9s+9kIKz8mLkbcmdaj5lxt3eiIMp1Nh49dkkBlg1Fhg4Fd/r0vL69mRRA36YutI9P/lJUfL8csQoAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A0OysezhLoCRYomumeYlubLurZTCmsjTb087OvtCy95jNM65cfEsbajrJnhaGwiTxhz38ZZbm+UhUwQuXfVPTg0AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="AxoOxdZQmIoA1WeAPDixRAeWDdgs7ZtVFfH2y19ziTgD1iaHE5ZGz2UdSjubkWvob9C5PrjUfkWi4ZSLgWk3Xg8AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A7+rMYR5onPnACrz+niKSeFdH3xw1IyHo2AZSHmxrofRk9w4HcQPMYcpBUKu6OQ6zsdxf4m/vqa6tG6Na4OLpAQAAAB4eyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A+b/H0b8RPXNaJgaNFpO0YOFuGK6myDQXlwnJB3SwzvNMfcndat4DZYMrP4ClJIzYWo3/yP2S+8FTZ/lpqbPAAEAAABueyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=" /><meta http-equiv="origin-trial" content="A9ZgbRtm4pU3oZiuNzOsKcC8ppFSZdcjP2qYcdQrFKVzkmiWH1kdYY1Mi9x7G8+PS8HV9Ha9Cz0gaMdKsiVZIgMAAAB7eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="AxL6oBxcpn5rQDPKSAs+d0oxNyJYq2/4esBUh3Yx5z8QfcLu+AU8iFCXYRcr/CEEfDnkxxLTsvXPJFQBxHfvkgMAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A9KPtG5kl3oLTk21xqynDPGQ5t18bSOpwt0w6kGa6dEWbuwjpffmdUpR3W+faZDubGT+KIk2do0BX2ca16x8qAcAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2MjYyMjA3OTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A3HucHUo1oW9s+9kIKz8mLkbcmdaj5lxt3eiIMp1Nh49dkkBlg1Fhg4Fd/r0vL69mRRA36YutI9P/lJUfL8csQoAAACFeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A0OysezhLoCRYomumeYlubLurZTCmsjTb087OvtCy95jNM65cfEsbajrJnhaGwiTxhz38ZZbm+UhUwQuXfVPTg0AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="AxoOxdZQmIoA1WeAPDixRAeWDdgs7ZtVFfH2y19ziTgD1iaHE5ZGz2UdSjubkWvob9C5PrjUfkWi4ZSLgWk3Xg8AAACLeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A7+rMYR5onPnACrz+niKSeFdH3xw1IyHo2AZSHmxrofRk9w4HcQPMYcpBUKu6OQ6zsdxf4m/vqa6tG6Na4OLpAQAAAB4eyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjI2MjIwNzk5LCJpc1RoaXJkUGFydHkiOnRydWV9" /><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=www.w3school.com.cn" as="script" /><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=www.w3school.com.cn"></script></head>

<body class="html">

<div id="wrapper">

<div id="header">
<a id="logo" href="/index.html" title="w3school 在线教程" style="float:left;">w3school 在线教程</a>
<div id="header_gg">
<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- W3 页眉 -->
<ins class="adsbygoogle" style="display: inline-block; width: 529px; height: 90px;" data-ad-client="ca-pub-3381531532877742" data-ad-slot="7423315034" data-adsbygoogle-status="done"><ins id="aswift_0_expand" style="display:inline-table;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:529px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_0_anchor" style="display:block;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:529px;background-color:transparent;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:529px;height:90px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="529" height="90" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-3381531532877742&amp;output=html&amp;h=90&amp;twa=1&amp;slotname=7423315034&amp;adk=10506110&amp;adf=3794579972&amp;pi=t.ma~as.7423315034&amp;w=529&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1619601650&amp;psa=0&amp;format=529x90&amp;url=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fcss_selectors.asp&amp;flash=0&amp;fwr=0&amp;rh=90&amp;rw=529&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTAuMCIsIng4NiIsIiIsIjkwLjAuNDQzMC44NSIsW11d&amp;dt=1619601650253&amp;bpp=13&amp;bdt=303&amp;idt=179&amp;shv=r20210426&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;correlator=3507923354635&amp;frm=20&amp;pv=2&amp;ga_vid=412601764.1619601650&amp;ga_sid=1619601650&amp;ga_hid=283140154&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=384&amp;ady=0&amp;biw=913&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;oid=3&amp;pvsid=1020259406535056&amp;pem=933&amp;eae=0&amp;fc=896&amp;brdim=10%2C10%2C10%2C10%2C1920%2C0%2C946%2C1020%2C930%2C889&amp;vis=1&amp;rsz=%7C%7CeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=1024&amp;bc=31&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;xpc=UbqqomNEAK&amp;p=https%3A//www.w3school.com.cn&amp;dtd=196" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!1" data-google-query-id="CJTy3qfOoPACFUlqlgodrk4PaQ" data-load-complete="true"></iframe></ins></ins></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
</div>

<div id="navfirst">
<ul id="menu">
<li id="h"><a href="/h.asp" title="HTML 系列教程">HTML 系列教程</a></li>
<li id="b"><a href="/b.asp" title="浏览器脚本教程">浏览器脚本</a></li>
<li id="s"><a href="/s.asp" title="服务器脚本教程">服务器脚本</a></li>
<li id="p"><a href="/p.asp" title="编程教程">编程教程</a></li>
<li id="x"><a href="/x.asp" title="XML 系列教程">XML 系列教程</a></li>
<li id="w"><a href="/w.asp" title="建站手册">建站手册</a></li>
<li id="r"><a href="/r.asp" title="参考手册">参考手册</a></li>
</ul>
</div>

<div id="navsecond">

<div id="course"><h2>CSS 参考手册</h2>
<ul>
<li><a href="/cssref/index.asp" title="CSS 参考手册">CSS 参考手册</a></li>
<li><a href="/cssref/css_browsersupport.asp" title="CSS 浏览器支持参考手册">CSS 浏览器支持</a></li>
<li class="currentLink"><a href="/cssref/css_selectors.asp" title="CSS 选择器参考手册">CSS 选择器</a></li>
<li><a href="/cssref/css_functions.asp" title="CSS 函数参考手册">CSS 函数</a></li>
<li><a href="/cssref/css_animatable.asp" title="CSS 动画相关属性">CSS 动画相关属性</a></li>
<li><a href="/cssref/css_websafe_fonts.asp" title="CSS 网络安全字体">CSS 网络安全字体</a></li>
<li><a href="/cssref/css_fonts_fallbacks.asp" title="CSS 字体回退">CSS 字体回退</a></li>
<li><a href="/cssref/css_units.asp" title="CSS 单位">CSS 单位</a></li>
<li><a href="/cssref/css_colors.asp" title="CSS 颜色">CSS 颜色</a></li>
<li><a href="/cssref/css_colors_legal.asp" title="CSS 颜色值">CSS 颜色值</a></li>
<li><a href="/cssref/css_default_values.asp" title="CSS 默认值">CSS 默认值</a></li>
<li><a href="/cssref/css_entities.asp" title="CSS 实体">CSS 实体</a></li>
<li><a href="/cssref/css_ref_aural.asp" title="CSS 听觉参考手册">CSS 听觉</a></li>
</ul>
<h2>CSS 属性</h2>
<ul>
<li><a href="/cssref/pr_align-content.asp" title="CSS align-content 属性">align-content</a></li>
<li><a href="/cssref/pr_align-items.asp" title="CSS align-items 属性">align-items</a></li>
<li><a href="/cssref/pr_align-self.asp" title="CSS align-self 属性">align-self</a></li>
<li><a href="/cssref/pr_all.asp" title="CSS all 属性">all</a></li>
<li><a href="/cssref/pr_animation.asp" title="CSS animation 属性">animation</a></li>
<li><a href="/cssref/pr_animation-delay.asp" title="CSS animation-delay 属性">animation-delay</a></li>
<li><a href="/cssref/pr_animation-direction.asp" title="CSS animation-direction 属性">animation-direction</a></li>
<li><a href="/cssref/pr_animation-duration.asp" title="CSS animation-duration 属性">animation-duration</a></li>
<li><a href="/cssref/pr_animation-fill-mode.asp" title="CSS animation-fill-mode 属性">animation-fill-mode</a></li>
<li><a href="/cssref/pr_animation-iteration-count.asp" title="CSS animation-iteration-count 属性">animation-iteration-count</a></li>
<li><a href="/cssref/pr_animation-name.asp" title="CSS animation-name 属性">animation-name</a></li>
<li><a href="/cssref/pr_animation-play-state.asp" title="CSS animation-play-state 属性">animation-play-state</a></li>
<li><a href="/cssref/pr_animation-timing-function.asp" title="CSS animation-timing-function 属性">animation-timing-function</a></li>
<li><a href="/cssref/pr_backface-visibility.asp" title="CSS backface-visibility 属性">backface-visibility</a></li>
<li><a href="/cssref/pr_background.asp" title="CSS background 属性">background</a></li>
<li><a href="/cssref/pr_background-attachment.asp" title="CSS background-attachment 属性">background-attachment</a></li>
<li><a href="/cssref/pr_background-blend-mode.asp" title="CSS background-blend-mode 属性">background-blend-mode</a></li>
<li><a href="/cssref/pr_background-clip.asp" title="CSS background-clip 属性">background-clip</a></li>
<li><a href="/cssref/pr_background-color.asp" title="CSS background-color 属性">background-color</a></li>
<li><a href="/cssref/pr_background-image.asp" title="CSS background-image 属性">background-image</a></li>
<li><a href="/cssref/pr_background-origin.asp" title="CSS background-origin 属性">background-origin</a></li>
<li><a href="/cssref/pr_background-position.asp" title="CSS background-position 属性">background-position</a></li>
<li><a href="/cssref/pr_background-repeat.asp" title="CSS background-repeat 属性">background-repeat</a></li>
<li><a href="/cssref/pr_background-size.asp" title="CSS background-size 属性">background-size</a></li>
<li><a href="/cssref/pr_border.asp" title="CSS border 属性">border</a></li>
<li><a href="/cssref/pr_border-bottom.asp" title="CSS border-bottom 属性">border-bottom</a></li>
<li><a href="/cssref/pr_border-bottom-color.asp" title="CSS border-bottom-color 属性">border-bottom-color</a></li>
<li><a href="/cssref/pr_border-bottom-left-radius.asp" title="CSS border-bottom-left-radius 属性">border-bottom-left-radius</a></li>
<li><a href="/cssref/pr_border-bottom-right-radius.asp" title="CSS border-bottom-right-radius 属性">border-bottom-right-radius</a></li>
<li><a href="/cssref/pr_border-bottom-style.asp" title="CSS border-bottom-style 属性">border-bottom-style</a></li>
<li><a href="/cssref/pr_border-bottom-width.asp" title="CSS border-bottom-width 属性">border-bottom-width</a></li>
<li><a href="/cssref/pr_border-collapse.asp" title="CSS border-collapse 属性">border-collapse</a></li>
<li><a href="/cssref/pr_border-color.asp" title="CSS border-color 属性">border-color</a></li>
<li><a href="/cssref/pr_border-image.asp" title="CSS border-image 属性">border-image</a></li>
<li><a href="/cssref/pr_border-image-outset.asp" title="CSS border-image-outset 属性">border-image-outset</a></li>
<li><a href="/cssref/pr_border-image-repeat.asp" title="CSS border-image-repeat 属性">border-image-repeat</a></li>
<li><a href="/cssref/pr_border-image-slice.asp" title="CSS border-image-slice 属性">border-image-slice</a></li>
<li><a href="/cssref/pr_border-image-source.asp" title="CSS border-image-source 属性">border-image-source</a></li>
<li><a href="/cssref/pr_border-image-width.asp" title="CSS border-image-width 属性">border-image-width</a></li>
<li><a href="/cssref/pr_border-left.asp" title="CSS border-left 属性">border-left</a></li>
<li><a href="/cssref/pr_border-left-color.asp" title="CSS border-left-color 属性">border-left-color</a></li>
<li><a href="/cssref/pr_border-left-style.asp" title="CSS border-left-style 属性">border-left-style</a></li>
<li><a href="/cssref/pr_border-left-width.asp" title="CSS border-left-width 属性">border-left-width</a></li>
<li><a href="/cssref/pr_border-radius.asp" title="CSS border-radius 属性">border-radius</a></li>
<li><a href="/cssref/pr_border-right.asp" title="CSS border-right 属性">border-right</a></li>
<li><a href="/cssref/pr_border-right-color.asp" title="CSS border-right-color 属性">border-right-color</a></li>
<li><a href="/cssref/pr_border-right-style.asp" title="CSS border-right-style 属性">border-right-style</a></li>
<li><a href="/cssref/pr_border-right-width.asp" title="CSS border-right-width 属性">border-right-width</a></li>
<li><a href="/cssref/pr_border-spacing.asp" title="CSS border-spacing 属性">border-spacing</a></li>
<li><a href="/cssref/pr_border-style.asp" title="CSS border-style 属性">border-style</a></li>
<li><a href="/cssref/pr_border-top.asp" title="CSS border-top 属性">border-top</a></li>
<li><a href="/cssref/pr_border-top-color.asp" title="CSS border-top-color 属性">border-top-color</a></li>
<li><a href="/cssref/pr_border-top-left-radius.asp" title="CSS border-top-left-radius 属性">border-top-left-radius</a></li>
<li><a href="/cssref/pr_border-top-right-radius.asp" title="CSS border-top-right-radius 属性">border-top-right-radius</a></li>
<li><a href="/cssref/pr_border-top-style.asp" title="CSS border-top-style 属性">border-top-style</a></li>
<li><a href="/cssref/pr_border-top-width.asp" title="CSS border-top-width 属性">border-top-width</a></li>
<li><a href="/cssref/pr_border-width.asp" title="CSS border-width 属性">border-width</a></li>
<li><a href="/cssref/pr_pos_bottom.asp" title="CSS bottom 属性">bottom</a></li>
<li><a href="/cssref/pr_box-decoration-break.asp" title="CSS box-decoration-break 属性">box-decoration-break</a></li>
<li><a href="/cssref/pr_box-shadow.asp" title="CSS box-shadow 属性">box-shadow</a></li>
<li><a href="/cssref/pr_box-sizing.asp" title="CSS box-sizing 属性">box-sizing</a></li>
<li><a href="/cssref/pr_break-after.asp" title="CSS break-after 属性">break-after</a></li>
<li><a href="/cssref/pr_break-before.asp" title="CSS break-before 属性">break-before</a></li>
<li><a href="/cssref/pr_break-inside.asp" title="CSS break-inside 属性">break-inside</a></li>
<li><a href="/cssref/pr_tab_caption-side.asp" title="CSS caption-side 属性">caption-side</a></li>
<li><a href="/cssref/pr_caret-color.asp" title="CSS caret-color 属性">caret-color</a></li>
<li><a href="/cssref/pr_charset_rule.asp" title="CSS @charset 属性">@charset</a></li>
<li><a href="/cssref/pr_class_clear.asp" title="CSS clear 属性">clear</a></li>
<li><a href="/cssref/pr_pos_clip.asp" title="CSS clip 属性">clip</a></li>
<li><a href="/cssref/pr_clip-path.asp" title="CSS clip-path 属性">clip-path</a></li>
<li><a href="/cssref/pr_text_color.asp" title="CSS color 属性">color</a></li>
<li><a href="/cssref/pr_column-count.asp" title="CSS column-count 属性">column-count</a></li>
<li><a href="/cssref/pr_column-fill.asp" title="CSS column-fill 属性">column-fill</a></li>
<li><a href="/cssref/pr_column-gap.asp" title="CSS column-gap 属性">column-gap</a></li>
<li><a href="/cssref/pr_column-rule.asp" title="CSS column-rule 属性">column-rule</a></li>
<li><a href="/cssref/pr_column-rule-color.asp" title="CSS column-rule-color 属性">column-rule-color</a></li>
<li><a href="/cssref/pr_column-rule-style.asp" title="CSS column-rule-style 属性">column-rule-style</a></li>
<li><a href="/cssref/pr_column-rule-width.asp" title="CSS column-rule-width 属性">column-rule-width</a></li>
<li><a href="/cssref/pr_column-span.asp" title="CSS column-span 属性">column-span</a></li>
<li><a href="/cssref/pr_column-width.asp" title="CSS column-width 属性">column-width</a></li>
<li><a href="/cssref/pr_columns.asp" title="CSS columns 属性">columns</a></li>
<li><a href="/cssref/pr_gen_content.asp" title="CSS content 属性">content</a></li>
<li><a href="/cssref/pr_gen_counter-increment.asp" title="CSS counter-increment 属性">counter-increment</a></li>
<li><a href="/cssref/pr_gen_counter-reset.asp" title="CSS counter-reset 属性">counter-reset</a></li>
<li><a href="/cssref/pr_class_cursor.asp" title="CSS cursor 属性">cursor</a></li>
<li><a href="/cssref/pr_text_direction.asp" title="CSS direction 属性">direction</a></li>
<li><a href="/cssref/pr_class_display.asp" title="CSS display 属性">display</a></li>
<li><a href="/cssref/pr_tab_empty-cells.asp" title="CSS empty-cells 属性">empty-cells</a></li>
<li><a href="/cssref/pr_filter.asp" title="CSS filter 属性">filter</a></li>
<li><a href="/cssref/pr_flex.asp" title="CSS flex 属性">flex</a></li>
<li><a href="/cssref/pr_flex-basis.asp" title="CSS flex-basis 属性">flex-basis</a></li>
<li><a href="/cssref/pr_flex-direction.asp" title="CSS flex-direction 属性">flex-direction</a></li>
<li><a href="/cssref/pr_flex-flow.asp" title="CSS flex-flow 属性">flex-flow</a></li>
<li><a href="/cssref/pr_flex-grow.asp" title="CSS flex-grow 属性">flex-grow</a></li>
<li><a href="/cssref/pr_flex-shrink.asp" title="CSS flex-shrink 属性">flex-shrink</a></li>
<li><a href="/cssref/pr_flex-wrap.asp" title="CSS flex-wrap 属性">flex-wrap</a></li>
<li><a href="/cssref/pr_class_float.asp" title="CSS float 属性">float</a></li>
<li><a href="/cssref/pr_font_font.asp" title="CSS font 属性">font</a></li>
<li><a href="/cssref/pr_font-face_rule.asp" title="CSS @font-face 属性">@font-face</a></li>
<li><a href="/cssref/pr_font_font-family.asp" title="CSS font-family 属性">font-family</a></li>
<li><a href="/cssref/pr_font-feature-settings.asp" title="CSS font-feature-settings 属性">font-feature-settings</a></li>
<li><a href="/cssref/pr_font-kerning.asp" title="CSS font-kerning 属性">font-kerning</a></li>
<li><a href="/cssref/pr_font_font-size.asp" title="CSS font-size 属性">font-size</a></li>
<li><a href="/cssref/pr_font-size-adjust.asp" title="CSS font-size-adjust 属性">font-size-adjust</a></li>
<li><a href="/cssref/pr_font-stretch.asp" title="CSS font-stretch 属性">font-stretch</a></li>
<li><a href="/cssref/pr_font_font-style.asp" title="CSS font-style 属性">font-style</a></li>
<li><a href="/cssref/pr_font_font-variant.asp" title="CSS font-variant 属性">font-variant</a></li>
<li><a href="/cssref/pr_font-variant-caps.asp" title="CSS font-variant-caps 属性">font-variant-caps</a></li>
<li><a href="/cssref/pr_font-weight.asp" title="CSS font-weight 属性">font-weight</a></li>
<li><a href="/cssref/pr_grid.asp" title="CSS grid 属性">grid</a></li>
<li><a href="/cssref/pr_grid-area.asp" title="CSS grid-area 属性">grid-area</a></li>
<li><a href="/cssref/pr_grid-auto-columns.asp" title="CSS grid-auto-columns 属性">grid-auto-columns</a></li>
<li><a href="/cssref/pr_grid-auto-flow.asp" title="CSS grid-auto-flow 属性">grid-auto-flow</a></li>
<li><a href="/cssref/pr_grid-auto-rows.asp" title="CSS grid-auto-rows 属性">grid-auto-rows</a></li>
<li><a href="/cssref/pr_grid-column.asp" title="CSS grid-column 属性">grid-column</a></li>
<li><a href="/cssref/pr_grid-column-end.asp" title="CSS grid-column-end 属性">grid-column-end</a></li>
<li><a href="/cssref/pr_grid-column-gap.asp" title="CSS grid-column-gap 属性">grid-column-gap</a></li>
<li><a href="/cssref/pr_grid-column-start.asp" title="CSS grid-column-start 属性">grid-column-start</a></li>
<li><a href="/cssref/pr_grid-gap.asp" title="CSS grid-gap 属性">grid-gap</a></li>
<li><a href="/cssref/pr_grid-row.asp" title="CSS grid-row 属性">grid-row</a></li>
<li><a href="/cssref/pr_grid-row-end.asp" title="CSS grid-row-end 属性">grid-row-end</a></li>
<li><a href="/cssref/pr_grid-row-gap.asp" title="CSS grid-row-gap 属性">grid-row-gap</a></li>
<li><a href="/cssref/pr_grid-row-start.asp" title="CSS grid-row-start 属性">grid-row-start</a></li>
<li><a href="/cssref/pr_grid-template.asp" title="CSS grid-template 属性">grid-template</a></li>
<li><a href="/cssref/pr_grid-template-areas.asp" title="CSS grid-template-areas 属性">grid-template-areas</a></li>
<li><a href="/cssref/pr_grid-template-columns.asp" title="CSS grid-template-columns 属性">grid-template-columns</a></li>
<li><a href="/cssref/pr_grid-template-rows.asp" title="CSS grid-template-rows 属性">grid-template-rows</a></li>
<li><a href="/cssref/pr_hanging-punctuation.asp" title="CSS hanging-punctuation 属性">hanging-punctuation</a></li>
<li><a href="/cssref/pr_dim_height.asp" title="CSS height 属性">height</a></li>
<li><a href="/cssref/pr_hyphens.asp" title="CSS hyphens 属性">hyphens</a></li>
<li><a href="/cssref/pr_import_rule.asp" title="CSS @import 属性">@import</a></li>
<li><a href="/cssref/pr_isolation.asp" title="CSS isolation 属性">isolation</a></li>
<li><a href="/cssref/pr_justify-content.asp" title="CSS justify-content 属性">justify-content</a></li>
<li><a href="/cssref/pr_keyframes.asp" title="CSS @keyframes 属性">@keyframes</a></li>
<li><a href="/cssref/pr_pos_left.asp" title="CSS left 属性">left</a></li>
<li><a href="/cssref/pr_text_letter-spacing.asp" title="CSS letter-spacing 属性">letter-spacing</a></li>
<li><a href="/cssref/pr_dim_line-height.asp" title="CSS line-height 属性">line-height</a></li>
<li><a href="/cssref/pr_list-style.asp" title="CSS list-style 属性">list-style</a></li>
<li><a href="/cssref/pr_list-style-image.asp" title="CSS list-style-image 属性">list-style-image</a></li>
<li><a href="/cssref/pr_list-style-position.asp" title="CSS list-style-position 属性">list-style-position</a></li>
<li><a href="/cssref/pr_list-style-type.asp" title="CSS list-style-type 属性">list-style-type</a></li>
<li><a href="/cssref/pr_margin.asp" title="CSS margin 属性">margin</a></li>
<li><a href="/cssref/pr_margin-bottom.asp" title="CSS margin-bottom 属性">margin-bottom</a></li>
<li><a href="/cssref/pr_margin-left.asp" title="CSS margin-left 属性">margin-left</a></li>
<li><a href="/cssref/pr_margin-right.asp" title="CSS margin-right 属性">margin-right</a></li>
<li><a href="/cssref/pr_margin-top.asp" title="CSS margin-top 属性">margin-top</a></li>
<li><a href="/cssref/pr_dim_max-height.asp" title="CSS max-height 属性">max-height</a></li>
<li><a href="/cssref/pr_dim_max-width.asp" title="CSS max-width 属性">max-width</a></li>
<li><a href="/cssref/pr_mediaquery.asp" title="CSS @media 属性">@media</a></li>
<li><a href="/cssref/pr_dim_min-height.asp" title="CSS min-height 属性">min-height</a></li>
<li><a href="/cssref/pr_dim_min-width.asp" title="CSS min-width 属性">min-width</a></li>
<li><a href="/cssref/pr_mix-blend-mode.asp" title="CSS mix-blend-mode 属性">mix-blend-mode</a></li>
<li><a href="/cssref/pr_object-fit.asp" title="CSS object-fit 属性">object-fit</a></li>
<li><a href="/cssref/pr_object-position.asp" title="CSS object-position 属性">object-position</a></li>
<li><a href="/cssref/pr_opacity.asp" title="CSS opacity 属性">opacity</a></li>
<li><a href="/cssref/pr_order.asp" title="CSS order 属性">order</a></li>
<li><a href="/cssref/pr_outline.asp" title="CSS outline 属性">outline</a></li>
<li><a href="/cssref/pr_outline-color.asp" title="CSS outline-color 属性">outline-color</a></li>
<li><a href="/cssref/pr_outline-offset.asp" title="CSS outline-offset 属性">outline-offset</a></li>
<li><a href="/cssref/pr_outline-style.asp" title="CSS outline-style 属性">outline-style</a></li>
<li><a href="/cssref/pr_outline-width.asp" title="CSS outline-width 属性">outline-width</a></li>
<li><a href="/cssref/pr_pos_overflow.asp" title="CSS overflow 属性">overflow</a></li>
<li><a href="/cssref/pr_overflow-x.asp" title="CSS overflow-x 属性">overflow-x</a></li>
<li><a href="/cssref/pr_overflow-y.asp" title="CSS overflow-y 属性">overflow-y</a></li>
<li><a href="/cssref/pr_padding.asp" title="CSS padding 属性">padding</a></li>
<li><a href="/cssref/pr_padding-bottom.asp" title="CSS padding-bottom 属性">padding-bottom</a></li>
<li><a href="/cssref/pr_padding-left.asp" title="CSS padding-left 属性">padding-left</a></li>
<li><a href="/cssref/pr_padding-right.asp" title="CSS padding-right 属性">padding-right</a></li>
<li><a href="/cssref/pr_padding-top.asp" title="CSS padding-top 属性">padding-top</a></li>
<li><a href="/cssref/pr_page-break-after.asp" title="CSS page-break-after 属性">page-break-after</a></li>
<li><a href="/cssref/pr_page-break-before.asp" title="CSS page-break-before 属性">page-break-before</a></li>
<li><a href="/cssref/pr_page-break-inside.asp" title="CSS page-break-inside 属性">page-break-inside</a></li>
<li><a href="/cssref/pr_perspective.asp" title="CSS perspective 属性">perspective</a></li>
<li><a href="/cssref/pr_perspective-origin.asp" title="CSS perspective-origin 属性">perspective-origin</a></li>
<li><a href="/cssref/pr_pointer-events.asp" title="CSS pointer-events 属性">pointer-events</a></li>
<li><a href="/cssref/pr_class_position.asp" title="CSS position 属性">position</a></li>
<li><a href="/cssref/pr_gen_quotes.asp" title="CSS quotes 属性">quotes</a></li>
<li><a href="/cssref/pr_resize.asp" title="CSS resize 属性">resize</a></li>
<li><a href="/cssref/pr_pos_right.asp" title="CSS right 属性">right</a></li>
<li><a href="/cssref/pr_scroll-behavior.asp" title="CSS scroll-behavior 属性">scroll-behavior</a></li>
<li><a href="/cssref/pr_tab-size.asp" title="CSS tab-size 属性">tab-size</a></li>
<li><a href="/cssref/pr_tab_table-layout.asp" title="CSS table-layout 属性">table-layout</a></li>
<li><a href="/cssref/pr_text_text-align.asp" title="CSS text-align 属性">text-align</a></li>
<li><a href="/cssref/pr_text-align-last.asp" title="CSS text-align-last 属性">text-align-last</a></li>
<li><a href="/cssref/pr_text_text-decoration.asp" title="CSS text-decoration 属性">text-decoration</a></li>
<li><a href="/cssref/pr_text-decoration-color.asp" title="CSS text-decoration-color 属性">text-decoration-color</a></li>
<li><a href="/cssref/pr_text-decoration-line.asp" title="CSS text-decoration-line 属性">text-decoration-line</a></li>
<li><a href="/cssref/pr_text-decoration-style.asp" title="CSS text-decoration-style 属性">text-decoration-style</a></li>
<li><a href="/cssref/pr_text_text-indent.asp" title="CSS text-indent 属性">text-indent</a></li>
<li><a href="/cssref/pr_text-justify.asp" title="CSS text-justify 属性">text-justify</a></li>
<li><a href="/cssref/pr_text-overflow.asp" title="CSS text-overflow 属性">text-overflow</a></li>
<li><a href="/cssref/pr_text-shadow.asp" title="CSS text-shadow 属性">text-shadow</a></li>
<li><a href="/cssref/pr_text_text-transform.asp" title="CSS text-transform 属性">text-transform</a></li>
<li><a href="/cssref/pr_pos_top.asp" title="CSS top 属性">top</a></li>
<li><a href="/cssref/pr_transform.asp" title="CSS transform 属性">transform</a></li>
<li><a href="/cssref/pr_transform-origin.asp" title="CSS transform-origin 属性">transform-origin</a></li>
<li><a href="/cssref/pr_transform-style.asp" title="CSS transform-style 属性">transform-style</a></li>
<li><a href="/cssref/pr_transition.asp" title="CSS transition 属性">transition</a></li>
<li><a href="/cssref/pr_transition-delay.asp" title="CSS transition-delay 属性">transition-delay</a></li>
<li><a href="/cssref/pr_transition-duration.asp" title="CSS transition-duration 属性">transition-duration</a></li>
<li><a href="/cssref/pr_transition-property.asp" title="CSS transition-property 属性">transition-property</a></li>
<li><a href="/cssref/pr_transition-timing-function.asp" title="CSS transition-timing-function 属性">transition-timing-function</a></li>
<li><a href="/cssref/pr_unicode-bidi.asp" title="CSS unicode-bidi 属性">unicode-bidi</a></li>
<li><a href="/cssref/pr_user-select.asp" title="CSS user-select 属性">user-select</a></li>
<li><a href="/cssref/pr_pos_vertical-align.asp" title="CSS vertical-align 属性">vertical-align</a></li>
<li><a href="/cssref/pr_class_visibility.asp" title="CSS visibility 属性">visibility</a></li>
<li><a href="/cssref/pr_text_white-space.asp" title="CSS white-space 属性">white-space</a></li>
<li><a href="/cssref/pr_dim_width.asp" title="CSS width 属性">width</a></li>
<li><a href="/cssref/pr_word-break.asp" title="CSS word-break 属性">word-break</a></li>
<li><a href="/cssref/pr_text_word-spacing.asp" title="CSS word-spacing 属性">word-spacing</a></li>
<li><a href="/cssref/pr_word-wrap.asp" title="CSS word-wrap 属性">word-wrap</a></li>
<li><a href="/cssref/pr_writing-mode.asp" title="CSS writing-mode 属性">writing-mode</a></li>
<li><a href="/cssref/pr_pos_z-index.asp" title="z-index">z-index</a></li>
</ul>
</div><div id="selected">
<h2>建站手册</h2>
<ul>
<li><a href="/site/index.asp" title="网站构建">网站构建</a></li>
<li><a href="/w3c/index.asp" title="万维网联盟 (W3C)">万维网联盟 (W3C)</a></li>
<li><a href="/browsers/index.asp" title="浏览器信息">浏览器信息</a></li>
<li><a href="/quality/index.asp" title="网站品质">网站品质</a></li>
<li><a href="/semweb/index.asp" title="语义网">语义网</a></li>
<li><a href="/careers/index.asp" title="职业规划">职业规划</a></li>
<li><a href="/hosting/index.asp" title="网站主机">网站主机</a></li>
</ul>

<h2 id="link_about"><a href="/about/index.asp" title="关于 W3School" target="_blank">关于 W3School</a></h2>
<h2 id="link_help"><a href="/about/about_helping.asp" title="帮助 W3School" target="_blank">帮助 W3School</a></h2>

</div>

</div>

<div id="maincontent">

<h1>CSS 选择器参考手册</h1>

<div class="prenextnav">
<ul class="prenext">
<li class="pre"><a href="/cssref/css_browsersupport.asp" title="CSS 浏览器支持参考手册">CSS 浏览器支持</a></li>
<li class="next"><a href="/cssref/css_functions.asp" title="CSS 函数参考手册">CSS 函数</a></li>
</ul>
</div>



<div>
<h2>CSS 选择器</h2>

<p>在 CSS 中，选择器是选取需设置样式的元素的模式。</p>

<p>请使用我们的 CSS 选择器测试工具，它可为您演示不同的选择器。</p>
<table class="dataintable">
<tbody><tr>
<th style="width: 25%;">选择器</th>
<th style="width: 25%;">例子</th>
<th>例子描述</th>
</tr>

<tr>
<td><a href="/cssref/selector_class.asp" title="CSS .class 选择器">.<i>class</i></a></td>
<td>.intro</td>
<td>选择 class="intro" 的所有元素。</td>
</tr>

<tr>
<td>.<i>class1</i>.<i>class2</i></td>
<td>.name1.name2</td>
<td>选择 class 属性中同时有 name1 和 name2 的所有元素。</td>
</tr>

<tr>
<td>.<i>class1</i> .<i>class2</i></td>
<td>.name1 .name2</td>
<td>选择作为类名 name1 元素后代的所有类名 name2 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_id.asp" title="CSS #id 选择器">#<i>id</i></a></td>
<td>#firstname</td>
<td>选择 id="firstname" 的元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_all.asp" title="CSS * 选择器">*</a></td>
<td>*</td>
<td>选择所有元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element.asp" title="CSS element 选择器"><i>element</i></a></td>
<td>p</td>
<td>选择所有 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element_class.asp" title="CSS element.class 选择器"><i>element</i>.<i>class</i></a></td>
<td>p.intro</td>
<td>选择 class="intro" 的所有 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element_comma.asp" title="CSS element,element 选择器"><i>element</i>,<i>element</i></a></td>
<td>div, p</td>
<td>选择所有 &lt;div&gt; 元素和所有 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element_element.asp" title="CSS element element 选择器"><i>element</i> <i>element</i></a></td>
<td>div p</td>
<td>选择 &lt;div&gt; 元素内的所有 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element_gt.asp" title="CSS element&gt;element 选择器"><i>element</i>&gt;<i>element</i></a></td>
<td>div &gt; p</td>
<td>选择父元素是 &lt;div&gt; 的所有 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_element_plus.asp" title="CSS element+element 选择器"><i>element</i>+<i>element</i></a></td>
<td>div + p</td>
<td>选择紧跟 &lt;div&gt; 元素的首个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_gen_sibling.asp" title="CSS element1~element2 选择器"><i>element1</i>~<i>element2</i></a></td>
<td>p ~ ul</td>
<td>选择前面有 &lt;p&gt; 元素的每个 &lt;ul&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attribute.asp" title="CSS [attribute] 选择器">[<i>attribute</i>]</a></td>
<td>[target]</td>
<td>选择带有 target 属性的所有元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attribute_value.asp" title="CSS [attribute=value] 选择器">[<i>attribute</i>=<i>value</i>]</a></td>
<td>[target=_blank]</td>
<td>选择带有 target="_blank" 属性的所有元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attribute_value_contain.asp" title="CSS [attribute~=value] 选择器">[<i>attribute</i>~=<i>value</i>]</a></td>
<td>[title~=flower]</td>
<td>选择 title 属性包含单词 "flower" 的所有元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attribute_value_start.asp" title="CSS [attribute|=value] 选择器">[<i>attribute</i>|=<i>value</i>]</a></td>
<td>[lang|=en]</td>
<td>选择 lang 属性值以 "en" 开头的所有元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attr_begin.asp" title="CSS [attribute^=value] 选择器">[<i>attribute</i>^=<i>value</i>]</a></td>
<td>a[href^="https"]</td>
<td>选择其 src 属性值以 "https" 开头的每个 &lt;a&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attr_end.asp" title="CSS [attribute$=value] 选择器">[<i>attribute</i>$=<i>value</i>]</a></td>
<td>a[href$=".pdf"]</td>
<td>选择其 src 属性以 ".pdf" 结尾的所有 &lt;a&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_attr_contain.asp" title="CSS [attribute*=value] 选择器">[<i>attribute</i>*=<i>value</i>]</a></td>
<td>a[href*="w3schools"]</td>
<td>选择其 href 属性值中包含 "abc" 子串的每个 &lt;a&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_active.asp" title="CSS :active 选择器">:active</a></td>
<td>a:active</td>
<td>选择活动链接。</td>
</tr>

<tr>
<td><a href="/cssref/selector_after.asp" title="CSS ::after 选择器">::after</a></td>
<td>p::after</td>
<td>在每个 &lt;p&gt; 的内容之后插入内容。</td>
</tr>

<tr>
<td><a href="/cssref/selector_before.asp" title="CSS ::before 选择器">::before</a></td>
<td>p::before</td>
<td>在每个 &lt;p&gt; 的内容之前插入内容。</td>
</tr>

<tr>
<td><a href="/cssref/selector_checked.asp" title="CSS :checked 选择器">:checked</a></td>
<td>input:checked</td>
<td>选择每个被选中的 &lt;input&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_default.asp" title="CSS :default 选择器">:default</a></td>
<td>input:default</td>
<td>选择默认的 &lt;input&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_disabled.asp" title="CSS :disabled 选择器">:disabled</a></td>
<td>input:disabled</td>
<td>选择每个被禁用的 &lt;input&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_empty.asp" title="CSS :empty 选择器">:empty</a></td>
<td>p:empty</td>
<td>选择没有子元素的每个 &lt;p&gt; 元素（包括文本节点）。</td>
</tr>

<tr>
<td><a href="/cssref/selector_enabled.asp" title="CSS :enabled 选择器">:enabled</a></td>
<td>input:enabled</td>
<td>选择每个启用的 &lt;input&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_first-child.asp" title="CSS :first-child 选择器">:first-child</a></td>
<td>p:first-child</td>
<td>选择属于父元素的第一个子元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_first-letter.asp" title="CSS ::first-letter 选择器">::first-letter</a></td>
<td>p::first-letter</td>
<td>选择每个 &lt;p&gt; 元素的首字母。</td>
</tr>

<tr>
<td><a href="/cssref/selector_first-line.asp" title="CSS ::first-line 选择器">::first-line</a></td>
<td>p::first-line</td>
<td>选择每个 &lt;p&gt; 元素的首行。</td>
</tr>

<tr>
<td><a href="/cssref/selector_first-of-type.asp" title="CSS :first-of-type 选择器">:first-of-type</a></td>
<td>p:first-of-type</td>
<td>选择属于其父元素的首个 &lt;p&gt; 元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_focus.asp" title="CSS :focus 选择器">:focus</a></td>
<td>input:focus</td>
<td>选择获得焦点的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_fullscreen.asp" title="CSS :fullscreen 选择器">:fullscreen</a></td>
<td>:fullscreen</td>
<td>选择处于全屏模式的元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_hover.asp" title="CSS :hover 选择器">:hover</a></td>
<td>a:hover</td>
<td>选择鼠标指针位于其上的链接。</td>
</tr>

<tr>
<td><a href="/cssref/selector_in-range.asp" title="CSS :in-range 选择器">:in-range</a></td>
<td>input:in-range</td>
<td>选择其值在指定范围内的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_indeterminate.asp" title="CSS :indeterminate 选择器">:indeterminate</a></td>
<td>input:indeterminate</td>
<td>选择处于不确定状态的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_invalid.asp" title="CSS :invalid 选择器">:invalid</a></td>
<td>input:invalid</td>
<td>选择具有无效值的所有 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_lang.asp" title="CSS :lang(language) 选择器">:lang(<i>language</i>)</a></td>
<td>p:lang(it)</td>
<td>选择 lang 属性等于 "it"（意大利）的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_last-child.asp" title="CSS :last-child 选择器">:last-child</a></td>
<td>p:last-child</td>
<td>选择属于其父元素最后一个子元素每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_last-of-type.asp" title="CSS :last-of-type 选择器">:last-of-type</a></td>
<td>p:last-of-type</td>
<td>选择属于其父元素的最后 &lt;p&gt; 元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_link.asp" title="CSS :link 选择器">:link</a></td>
<td>a:link</td>
<td>选择所有未访问过的链接。</td>
</tr>

<tr>
<td><a href="/cssref/selector_not.asp" title="CSS :not(selector) 选择器">:not(<i>selector</i>)</a></td>
<td>:not(p)</td>
<td>选择非 &lt;p&gt; 元素的每个元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_nth-child.asp" title="CSS :nth-child(n) 选择器">:nth-child(<i>n</i>)</a></td>
<td>p:nth-child(2)</td>
<td>选择属于其父元素的第二个子元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_nth-last-child.asp" title="CSS :nth-last-child(n) 选择器">:nth-last-child(<i>n</i>)</a></td>
<td>p:nth-last-child(2)</td>
<td>同上，从最后一个子元素开始计数。</td>
</tr>

<tr>
<td><a href="/cssref/selector_nth-of-type.asp" title="CSS :nth-of-type(n) 选择器">:nth-of-type(<i>n</i>)</a></td>
<td>p:nth-of-type(2)</td>
<td>选择属于其父元素第二个 &lt;p&gt; 元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_nth-last-of-type.asp" title="CSS :nth-last-of-type(n) 选择器">:nth-last-of-type(<i>n</i>)</a></td>
<td>p:nth-last-of-type(2)</td>
<td>同上，但是从最后一个子元素开始计数。</td>
</tr>

<tr>
<td><a href="/cssref/selector_only-of-type.asp" title="CSS :only-of-type 选择器">:only-of-type</a></td>
<td>p:only-of-type</td>
<td>选择属于其父元素唯一的 &lt;p&gt; 元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_only-child.asp" title="CSS :only-child 选择器">:only-child</a></td>
<td>p:only-child</td>
<td>选择属于其父元素的唯一子元素的每个 &lt;p&gt; 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_optional.asp" title="CSS :optional 选择器">:optional</a></td>
<td>input:optional</td>
<td>选择不带 "required" 属性的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_out-of-range.asp" title="CSS :out-of-range 选择器">:out-of-range</a></td>
<td>input:out-of-range</td>
<td>选择值超出指定范围的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_placeholder.asp" title="CSS ::placeholder 选择器">::placeholder</a></td>
<td>input::placeholder</td>
<td>选择已规定 "placeholder" 属性的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_read-only.asp" title="CSS :read-only 选择器">:read-only</a></td>
<td>input:read-only</td>
<td>选择已规定 "readonly" 属性的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_read-write.asp" title="CSS :read-write 选择器">:read-write</a></td>
<td>input:read-write</td>
<td>选择未规定 "readonly" 属性的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_required.asp" title="CSS :required 选择器">:required</a></td>
<td>input:required</td>
<td>选择已规定 "required" 属性的 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_root.asp" title="CSS :root 选择器">:root</a></td>
<td>:root</td>
<td>选择文档的根元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_selection.asp" title="CSS ::selection 选择器">::selection</a></td>
<td>::selection</td>
<td>选择用户已选取的元素部分。</td>
</tr>

<tr>
<td><a href="/cssref/selector_target.asp" title="CSS :target 选择器">:target</a></td>
<td>#news:target</td>
<td>选择当前活动的 #news 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_valid.asp" title="CSS :valid 选择器">:valid</a></td>
<td>input:valid</td>
<td>选择带有有效值的所有 input 元素。</td>
</tr>

<tr>
<td><a href="/cssref/selector_visited.asp" title="CSS :visited 选择器">:visited</a></td>
<td>a:visited</td>
<td>选择所有已访问的链接。</td>
</tr>
</tbody></table>
</div>



<div class="prenextnav">
<ul class="prenext">
<li class="pre"><a href="/cssref/css_browsersupport.asp" title="CSS 浏览器支持参考手册">CSS 浏览器支持</a></li>
<li class="next"><a href="/cssref/css_functions.asp" title="CSS 函数参考手册">CSS 函数</a></li>
</ul>
</div><div style="background-color:#fcfdf8; padding:0;">
<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- W3School ���Ĺ�� -->
<ins class="adsbygoogle" style="display: inline-block; width: 696px; height: 250px;" data-ad-client="ca-pub-3381531532877742" data-ad-slot="2086924285" data-adsbygoogle-status="done"><ins id="aswift_1_expand" style="display:inline-table;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:696px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_1_anchor" style="display:block;border:none;height:250px;margin:0;padding:0;position:relative;visibility:visible;width:696px;background-color:transparent;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:696px;height:250px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="696" height="250" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-3381531532877742&amp;output=html&amp;h=250&amp;twa=1&amp;slotname=2086924285&amp;adk=1087254536&amp;adf=3260133560&amp;pi=t.ma~as.2086924285&amp;w=696&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1619601650&amp;psa=0&amp;format=696x250&amp;url=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fcss_selectors.asp&amp;flash=0&amp;fwr=0&amp;rh=250&amp;rw=696&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTAuMCIsIng4NiIsIiIsIjkwLjAuNDQzMC44NSIsW11d&amp;dt=1619601650266&amp;bpp=4&amp;bdt=316&amp;idt=191&amp;shv=r20210426&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=529x90&amp;correlator=3507923354635&amp;frm=20&amp;pv=1&amp;ga_vid=412601764.1619601650&amp;ga_sid=1619601650&amp;ga_hid=283140154&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=217&amp;ady=2836&amp;biw=913&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;oid=3&amp;pvsid=1020259406535056&amp;pem=933&amp;eae=0&amp;fc=896&amp;brdim=10%2C10%2C10%2C10%2C1920%2C0%2C946%2C1020%2C930%2C889&amp;vis=1&amp;rsz=%7C%7CeEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=1024&amp;bc=31&amp;ifi=2&amp;uci=a!2&amp;btvi=1&amp;fsb=1&amp;xpc=fvKi41xdcD&amp;p=https%3A//www.w3school.com.cn&amp;dtd=194" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!2" data-google-query-id="COm-36fOoPACFRzKlgod1r4IqQ" data-load-complete="true"></iframe></ins></ins></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

</div>
<!-- maincontent end -->

<div id="sidebar">

<div id="tools">
<h5 id="tools_reference"><a href="/cssref/index.asp">CSS 参考手册</a></h5>
<h5 id="tools_example"><a href="/css/css_examples.asp">CSS 实例</a></h5>
<h5 id="tools_quiz"><a href="/css/css_quiz.asp">CSS 测验</a></h5>
<h5 id="tools_tutorial"><a href="/css/index.asp">CSS 教程</a></h5>
</div>

<div id="sp_sidebar">
<script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- W3School 侧栏广告位 -->
<ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-3381531532877742" data-ad-slot="6744370501" data-adsbygoogle-status="done"><ins id="aswift_2_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_2_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;"><iframe id="aswift_2" name="aswift_2" style="left:0;position:absolute;top:0;border:0;width:160px;height:600px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="160" height="600" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-3381531532877742&amp;output=html&amp;h=600&amp;slotname=6744370501&amp;adk=4175462743&amp;adf=306418561&amp;pi=t.ma~as.6744370501&amp;w=160&amp;lmt=1619601650&amp;psa=0&amp;format=160x600&amp;url=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fcss_selectors.asp&amp;flash=0&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTAuMCIsIng4NiIsIiIsIjkwLjAuNDQzMC44NSIsW11d&amp;dt=1619601650270&amp;bpp=1&amp;bdt=320&amp;idt=195&amp;shv=r20210426&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=529x90%2C696x250&amp;correlator=3507923354635&amp;frm=20&amp;pv=1&amp;ga_vid=412601764.1619601650&amp;ga_sid=1619601650&amp;ga_hid=283140154&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=1052&amp;ady=607&amp;biw=913&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;oid=3&amp;pvsid=1020259406535056&amp;pem=933&amp;eae=0&amp;fc=896&amp;brdim=10%2C10%2C10%2C10%2C1920%2C0%2C946%2C1020%2C930%2C889&amp;vis=1&amp;rsz=%7C%7CeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=1024&amp;bc=31&amp;ifi=3&amp;uci=a!3&amp;fsb=1&amp;xpc=D28QIffwNv&amp;p=https%3A//www.w3school.com.cn&amp;dtd=197" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!3" data-google-query-id="CLD_36fOoPACFYeGlgodMUUBhg" data-load-complete="true"></iframe></ins></ins></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

</div>

<div id="footer">
<p id="p1">
W3School 简体中文版提供的内容仅用于培训和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。版权所有，保留一切权利。
</p>

<p id="p2">

<a href="/about/about_use.asp" title="关于使用">使用条款</a>
<a href="/about/about_privacy.asp" title="关于隐私">隐私条款</a>
<a target="_blank" href="https://www.ykinvestment.com/">技术支持：赢科</a>
<a target="_blank" href="http://www.beian.miit.gov.cn">蒙ICP备06004630号</a>
</p>
</div>


</div>
<!-- wrapper end -->



<ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;"><ins id="aswift_3_expand" style="display:inline-table;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_3_anchor" style="display:block;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><iframe id="aswift_3" name="aswift_3" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-3381531532877742&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1619601650&amp;plat=1%3A8%2C2%3A8%2C9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1081344%2C32%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.w3school.com.cn%2Fcssref%2Fcss_selectors.asp&amp;ea=0&amp;flash=0&amp;pra=7&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTAuMCIsIng4NiIsIiIsIjkwLjAuNDQzMC44NSIsW11d&amp;dt=1619601650271&amp;bpp=1&amp;bdt=321&amp;idt=206&amp;shv=r20210426&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=529x90%2C696x250%2C160x600&amp;nras=1&amp;correlator=3507923354635&amp;frm=20&amp;pv=1&amp;ga_vid=412601764.1619601650&amp;ga_sid=1619601650&amp;ga_hid=283140154&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=-12245933&amp;ady=-12245933&amp;biw=913&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;oid=3&amp;pvsid=1020259406535056&amp;pem=933&amp;eae=2&amp;fc=896&amp;brdim=10%2C10%2C10%2C10%2C1920%2C0%2C946%2C1020%2C930%2C889&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=1024&amp;bc=31&amp;ifi=4&amp;uci=a!4&amp;fsb=1&amp;dtd=211" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!4" data-load-complete="true"></iframe></ins></ins></ins><iframe id="google_osd_static_frame_5797174561085" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe></body><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20210426/r20190131/zrt_lookup.html#" data-ad-client="ca-pub-3381531532877742" style="display: none;"></iframe></html>