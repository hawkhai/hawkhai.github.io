<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head><iframe id="pxcelframe" src="//t.sharethis.com/a/t_.htm?ver=1.395.21632&amp;cid=c010#rnd=1608277000862&amp;cid=c010&amp;dmn=www.bogotobogo.com&amp;gdpr_domain=.consensu.org&amp;gdpr_domain_temp=.consensu.org&amp;gdpr_method=cookie&amp;tt=t.dhj&amp;dhjLcy=1317&amp;lbl=pxcel&amp;flbl=pxcel&amp;ll=d&amp;ver=1.395.21632&amp;ell=d&amp;cck=__stid&amp;pn=%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;qs=na&amp;rdn=www.bogotobogo.com&amp;rpn=%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;rqs=na&amp;cc=HK&amp;cont=AS&amp;ipaddr=" style="display: none;"></iframe><script src="https://pagead2.googlesyndication.com/pagead/js/r20201203/r20190131/reactive_library_fy2019.js"></script><script type="text/javascript" src="https://m.addthis.com/live/red_lojson/300lo.json?si=5fdc5c07cbe8e8ee&amp;bkl=0&amp;bl=1&amp;pdt=1124&amp;sid=5fdc5c07cbe8e8ee&amp;pub=khhong7&amp;rev=v8.28.8-wp&amp;ln=zh&amp;pc=men&amp;cb=0&amp;ab=-&amp;dp=www.bogotobogo.com&amp;fp=python%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;fr=&amp;of=0&amp;pd=0&amp;irt=0&amp;vcl=0&amp;md=0&amp;ct=1&amp;tct=0&amp;abt=0&amp;cdn=0&amp;pi=1&amp;rb=0&amp;gen=100&amp;chr=UTF-8&amp;mk=OpenCV%203%20with%20Python%20Tutorial%3A%20Fourier%20Transform%20%3A%20FFT%20%26%20DFT%2CNumPy&amp;colc=1608276999522&amp;jsl=33&amp;uvs=5fdc5c07115641b3000&amp;skipb=1&amp;callback=addthis.cbs.jsonp__69193770192794450"></script><script type="text/javascript" src="https://v1.addthisedge.com/live/boost/khhong7/_ate.track.config_resp"></script><script src="https://apis.google.com/_/scs/apps-static/_/js/k=oz.gapi.zh_CN.YnQtsvjdhNk.O/m=auth/exm=person,plusone/rt=j/sv=1/d=1/ed=1/am=wQE/rs=AGLTcCM3AUeqdmNhXMv7bPFaglkzmd4UXQ/cb=gapi.loaded_1" async=""></script><script src="https://apis.google.com/_/scs/apps-static/_/js/k=oz.gapi.zh_CN.YnQtsvjdhNk.O/m=person,plusone/rt=j/sv=1/d=1/ed=1/am=wQE/rs=AGLTcCM3AUeqdmNhXMv7bPFaglkzmd4UXQ/cb=gapi.loaded_0" async=""></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript" async="" src="https://ssl.google-analytics.com/ga.js"></script><script src="https://www.googletagservices.com/activeview/js/current/osd.js?cb=%2Fr20100101"></script><script src="https://partner.googleadservices.com/gampad/cookie.js?domain=www.bogotobogo.com&amp;callback=_gfp_s_&amp;client=ca-pub-4716428189734495"></script><script type="text/javascript" async="" src="https://apis.google.com/js/platform.js" gapi_processed="true"></script><script src="https://pagead2.googlesyndication.com/pagead/js/r20201203/r20190131/show_ads_impl_fy2019.js" id="google_shimpl"></script><script type="text/javascript" src="https://z.moatads.com/addthismoatframe568911941483/moatframe.js"></script>
  <title>OpenCV 3   Signal Processing with NumPy II - Image Fourier Transform : FFT &amp; DFT - 2020</title>
  <meta content="OpenCV 3  Signal Processing with NumPy II - Image Fourier Transform : FFT &amp; DFT" name="description" />
  <meta content="OpenCV 3 with Python Tutorial: Fourier Transform : FFT &amp; DFT, NumPy" name="keywords" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />

  <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.no-icons.min.css" rel="stylesheet" />
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet" />
  <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Alice|Open+Sans:400,300,700" />
  <link rel="stylesheet" href="/public/css/app.css" />
  <link rel="stylesheet" href="/public/css/styles.css" />
  <link rel="stylesheet" href="/public/css/bogostyleWidePreNew.css" />
<link rel="stylesheet" type="text/css" href="https://ws.sharethis.com/button/css/buttons-secure.css" /><style type="text/css">.at-icon{fill:#fff;border:0}.at-icon-wrapper{display:inline-block;overflow:hidden}a .at-icon-wrapper{cursor:pointer}.at-rounded,.at-rounded-element .at-icon-wrapper{border-radius:12%}.at-circular,.at-circular-element .at-icon-wrapper{border-radius:50%}.addthis_32x32_style .at-icon{width:2pc;height:2pc}.addthis_24x24_style .at-icon{width:24px;height:24px}.addthis_20x20_style .at-icon{width:20px;height:20px}.addthis_16x16_style .at-icon{width:1pc;height:1pc}#at16lb{display:none;position:absolute;top:0;left:0;width:100%;height:100%;z-index:1001;background-color:#000;opacity:.001}#at_complete,#at_error,#at_share,#at_success{position:static!important}.at15dn{display:none}#at15s,#at16p,#at16p form input,#at16p label,#at16p textarea,#at_share .at_item{font-family:arial,helvetica,tahoma,verdana,sans-serif!important;font-size:9pt!important;outline-style:none;outline-width:0;line-height:1em}* html #at15s.mmborder{position:absolute!important}#at15s.mmborder{position:fixed!important;width:250px!important}#at15s{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);float:none;line-height:1em;margin:0;overflow:visible;padding:5px;text-align:left;position:absolute}#at15s a,#at15s span{outline:0;direction:ltr;text-transform:none}#at15s .at-label{margin-left:5px}#at15s .at-icon-wrapper{width:1pc;height:1pc;vertical-align:middle}#at15s .at-icon{width:1pc;height:1pc}.at4-icon{display:inline-block;background-repeat:no-repeat;background-position:top left;margin:0;overflow:hidden;cursor:pointer}.addthis_16x16_style .at4-icon,.addthis_default_style .at4-icon,.at4-icon,.at-16x16{width:1pc;height:1pc;line-height:1pc;background-size:1pc!important}.addthis_32x32_style .at4-icon,.at-32x32{width:2pc;height:2pc;line-height:2pc;background-size:2pc!important}.addthis_24x24_style .at4-icon,.at-24x24{width:24px;height:24px;line-height:24px;background-size:24px!important}.addthis_20x20_style .at4-icon,.at-20x20{width:20px;height:20px;line-height:20px;background-size:20px!important}.at4-icon.circular,.circular .at4-icon,.circular.aticon{border-radius:50%}.at4-icon.rounded,.rounded .at4-icon{border-radius:4px}.at4-icon-left{float:left}#at15s .at4-icon{text-indent:20px;padding:0;overflow:visible;white-space:nowrap;background-size:1pc;width:1pc;height:1pc;background-position:top left;display:inline-block;line-height:1pc}.addthis_vertical_style .at4-icon,.at4-follow-container .at4-icon{margin-right:5px}html&gt;body #at15s{width:250px!important}#at15s.atm{background:none!important;padding:0!important;width:10pc!important}#at15s_inner{background:#fff;border:1px solid #fff;margin:0}#at15s_head{position:relative;background:#f2f2f2;padding:4px;cursor:default;border-bottom:1px solid #e5e5e5}.at15s_head_success{background:#cafd99!important;border-bottom:1px solid #a9d582!important}.at15s_head_success a,.at15s_head_success span{color:#000!important;text-decoration:none}#at15s_brand,#at15sptx,#at16_brand{position:absolute}#at15s_brand{top:4px;right:4px}.at15s_brandx{right:20px!important}a#at15sptx{top:4px;right:4px;text-decoration:none;color:#4c4c4c;font-weight:700}#at15sptx:hover{text-decoration:underline}#at16_brand{top:5px;right:30px;cursor:default}#at_hover{padding:4px}#at_hover .at_item,#at_share .at_item{background:#fff!important;float:left!important;color:#4c4c4c!important}#at_share .at_item .at-icon-wrapper{margin-right:5px}#at_hover .at_bold{font-weight:700;color:#000!important}#at_hover .at_item{width:7pc!important;padding:2px 3px!important;margin:1px;text-decoration:none!important}#at_hover .at_item.athov,#at_hover .at_item:focus,#at_hover .at_item:hover{margin:0!important}#at_hover .at_item.athov,#at_hover .at_item:focus,#at_hover .at_item:hover,#at_share .at_item.athov,#at_share .at_item:hover{background:#f2f2f2!important;border:1px solid #e5e5e5;color:#000!important;text-decoration:none}.ipad #at_hover .at_item:focus{background:#fff!important;border:1px solid #fff}.at15t{display:block!important;height:1pc!important;line-height:1pc!important;padding-left:20px!important;background-position:0 0;text-align:left}.addthis_button,.at15t{cursor:pointer}.addthis_toolbox a.at300b,.addthis_toolbox a.at300m{width:auto}.addthis_toolbox a{margin-bottom:5px;line-height:initial}.addthis_toolbox.addthis_vertical_style{width:200px}.addthis_button_facebook_like .fb_iframe_widget{line-height:100%}.addthis_button_facebook_like iframe.fb_iframe_widget_lift{max-width:none}.addthis_toolbox a.addthis_button_counter,.addthis_toolbox a.addthis_button_facebook_like,.addthis_toolbox a.addthis_button_facebook_send,.addthis_toolbox a.addthis_button_facebook_share,.addthis_toolbox a.addthis_button_foursquare,.addthis_toolbox a.addthis_button_linkedin_counter,.addthis_toolbox a.addthis_button_pinterest_pinit,.addthis_toolbox a.addthis_button_tweet{display:inline-block}.addthis_toolbox span.addthis_follow_label{display:none}.addthis_toolbox.addthis_vertical_style span.addthis_follow_label{display:block;white-space:nowrap}.addthis_toolbox.addthis_vertical_style a{display:block}.addthis_toolbox.addthis_vertical_style.addthis_32x32_style a{line-height:2pc;height:2pc}.addthis_toolbox.addthis_vertical_style .at300bs{margin-right:4px;float:left}.addthis_toolbox.addthis_20x20_style span{line-height:20px}.addthis_toolbox.addthis_32x32_style span{line-height:2pc}.addthis_toolbox.addthis_pill_combo_style .addthis_button_compact .at15t_compact,.addthis_toolbox.addthis_pill_combo_style a{float:left}.addthis_toolbox.addthis_pill_combo_style a.addthis_button_tweet{margin-top:-2px}.addthis_toolbox.addthis_pill_combo_style .addthis_button_compact .at15t_compact{margin-right:4px}.addthis_default_style .addthis_separator{margin:0 5px;display:inline}div.atclear{clear:both}.addthis_default_style .addthis_separator,.addthis_default_style .at4-icon,.addthis_default_style .at300b,.addthis_default_style .at300bo,.addthis_default_style .at300bs,.addthis_default_style .at300m{float:left}.at300b img,.at300bo img{border:0}a.at300b .at4-icon,a.at300m .at4-icon{display:block}.addthis_default_style .at300b,.addthis_default_style .at300bo,.addthis_default_style .at300m{padding:0 2px}.at300b,.at300bo,.at300bs,.at300m{cursor:pointer}.addthis_button_facebook_like.at300b:hover,.addthis_button_facebook_like.at300bs:hover,.addthis_button_facebook_send.at300b:hover,.addthis_button_facebook_send.at300bs:hover{opacity:1}.addthis_20x20_style .at15t,.addthis_20x20_style .at300bs{overflow:hidden;display:block;height:20px!important;width:20px!important;line-height:20px!important}.addthis_32x32_style .at15t,.addthis_32x32_style .at300bs{overflow:hidden;display:block;height:2pc!important;width:2pc!important;line-height:2pc!important}.at300bs{overflow:hidden;display:block;background-position:0 0;height:1pc;width:1pc;line-height:1pc!important}.addthis_default_style .at15t_compact,.addthis_default_style .at15t_expanded{margin-right:4px}#at_share .at_item{width:123px!important;padding:4px;margin-right:2px;border:1px solid #fff}#at16p{background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);z-index:10000001;position:absolute;top:50%;left:50%;width:300px;padding:10px;margin:0 auto;margin-top:-185px;margin-left:-155px;font-family:arial,helvetica,tahoma,verdana,sans-serif;font-size:9pt;color:#5e5e5e}#at_share{margin:0;padding:0}#at16pt{position:relative;background:#f2f2f2;height:13px;padding:5px 10px}#at16pt a,#at16pt h4{font-weight:700}#at16pt h4{display:inline;margin:0;padding:0;font-size:9pt;color:#4c4c4c;cursor:default}#at16pt a{position:absolute;top:5px;right:10px;color:#4c4c4c;text-decoration:none;padding:2px}#at15sptx:focus,#at16pt a:focus{outline:thin dotted}#at15s #at16pf a{top:1px}#_atssh{width:1px!important;height:1px!important;border:0!important}.atm{width:10pc!important;padding:0;margin:0;line-height:9pt;letter-spacing:normal;font-family:arial,helvetica,tahoma,verdana,sans-serif;font-size:9pt;color:#444;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABtJREFUeNpiZGBgaGAgAjAxEAlGFVJHIUCAAQDcngCUgqGMqwAAAABJRU5ErkJggg==);padding:4px}.atm-f{text-align:right;border-top:1px solid #ddd;padding:5px 8px}.atm-i{background:#fff;border:1px solid #d5d6d6;padding:0;margin:0;box-shadow:1px 1px 5px rgba(0,0,0,.15)}.atm-s{margin:0!important;padding:0!important}.atm-s a:focus{border:transparent;outline:0;transition:none}#at_hover.atm-s a,.atm-s a{display:block;text-decoration:none;padding:4px 10px;color:#235dab!important;font-weight:400;font-style:normal;transition:none}#at_hover.atm-s .at_bold{color:#235dab!important}#at_hover.atm-s a:hover,.atm-s a:hover{background:#2095f0;text-decoration:none;color:#fff!important}#at_hover.atm-s .at_bold{font-weight:700}#at_hover.atm-s a:hover .at_bold{color:#fff!important}.atm-s a .at-label{vertical-align:middle;margin-left:5px;direction:ltr}.at_PinItButton{display:block;width:40px;height:20px;padding:0;margin:0;background-image:url(//s7.addthis.com/static/t00/pinit00.png);background-repeat:no-repeat}.at_PinItButton:hover{background-position:0 -20px}.addthis_toolbox .addthis_button_pinterest_pinit{position:relative}.at-share-tbx-element .fb_iframe_widget span{vertical-align:baseline!important}#at16pf{height:auto;text-align:right;padding:4px 8px}.at-privacy-info{position:absolute;left:7px;bottom:7px;cursor:pointer;text-decoration:none;font-family:helvetica,arial,sans-serif;font-size:10px;line-height:9pt;letter-spacing:.2px;color:#666}.at-privacy-info:hover{color:#000}.body .wsb-social-share .wsb-social-share-button-vert{padding-top:0;padding-bottom:0}.body .wsb-social-share.addthis_counter_style .addthis_button_tweet.wsb-social-share-button{padding-top:40px}.body .wsb-social-share.addthis_counter_style .addthis_button_facebook_like.wsb-social-share-button{padding-top:21px}@media print{#at4-follow,#at4-share,#at4-thankyou,#at4-whatsnext,#at4m-mobile,#at15s,.at4,.at4-recommended{display:none!important}}@media screen and (max-width:400px){.at4win{width:100%}}@media screen and (max-height:700px) and (max-width:400px){.at4-thankyou-inner .at4-recommended-container{height:122px;overflow:hidden}.at4-thankyou-inner .at4-recommended .at4-recommended-item:first-child{border-bottom:1px solid #c5c5c5}}</style><style type="text/css">.at-branding-logo{font-family:helvetica,arial,sans-serif;text-decoration:none;font-size:10px;display:inline-block;margin:2px 0;letter-spacing:.2px}.at-branding-logo .at-branding-icon{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAMAAAC67D+PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////+GlNUkcc1QAAAB1JREFUeNpiYIQDBjQmAwMmkwEM0JnY1WIxFyDAABGeAFEudiZsAAAAAElFTkSuQmCC")}.at-branding-logo .at-branding-icon,.at-branding-logo .at-privacy-icon{display:inline-block;height:10px;width:10px;margin-left:4px;margin-right:3px;margin-bottom:-1px;background-repeat:no-repeat}.at-branding-logo .at-privacy-icon{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAKCAMAAABR24SMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRF8fr9ot/xXcfn2/P5AKva////////AKTWodjhjAAAAAd0Uk5T////////ABpLA0YAAAA6SURBVHjaJMzBDQAwCAJAQaj7b9xifV0kUKJ9ciWxlzWEWI5gMF65KUTv0VKkjVeTerqE/x7+9BVgAEXbAWI8QDcfAAAAAElFTkSuQmCC")}.at-branding-logo span{text-decoration:none}.at-branding-logo .at-branding-addthis,.at-branding-logo .at-branding-powered-by{color:#666}.at-branding-logo .at-branding-addthis:hover{color:#333}.at-cv-with-image .at-branding-addthis,.at-cv-with-image .at-branding-addthis:hover{color:#fff}a.at-branding-logo:visited{color:initial}.at-branding-info{display:inline-block;padding:0 5px;color:#666;border:1px solid #666;border-radius:50%;font-size:10px;line-height:9pt;opacity:.7;transition:all .3s ease;text-decoration:none}.at-branding-info span{border:0;clip:rect(0 0 0 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.at-branding-info:before{content:'i';font-family:Times New Roman}.at-branding-info:hover{color:#0780df;border-color:#0780df}</style><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=www.bogotobogo.com" as="script" /><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=www.bogotobogo.com"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MathJax_Preview .MJXf-math {color: inherit!important}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom &gt; * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd &gt; * {display: block!important}
.MJXp-script-box &gt; *  {display: table!important; height: 50%}
.MJXp-script-box &gt; * &gt; * {display: table-cell!important; vertical-align: top}
.MJXp-script-box &gt; *:last-child &gt; * {vertical-align: bottom}
.MJXp-script-box &gt; * &gt; * &gt; * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over &gt; * {display: block!important}
.MJXp-munderover &gt; * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable &gt; * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr &gt; .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child &gt; .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr &gt; .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child &gt; .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css"></style><style type="text/css">.MathJax_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_ExBox {display: block!important; overflow: hidden; width: 1px; height: 60ex; min-height: 0; max-height: none}
.MathJax .MathJax_EmBox {display: block!important; overflow: hidden; width: 1px; height: 60em; min-height: 0; max-height: none}
.MathJax_LineBox {display: table!important}
.MathJax_LineBox span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.1') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.1') format('woff'), url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.1') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style></head>

<body class="home" style="" aria-hidden="false"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div>
    <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container-fluid">      
      <div class="navbar-header">
        <!--<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar"> -->
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse" aria-expanded="false" aria-controls="navbar"> 
          <span class="sr-only">Toggle navigation</span> 
          <span class="icon-bar"></span> 
          <span class="icon-bar"></span> 
          <span class="icon-bar"></span> 
        </button>
        <a class="navbar-brand" href="/index.php">BogoToBogo</a>
      </div>
      
      <div class="navbar-collapse collapse">
        
        <ul class="nav navbar-nav">
          <li class="active"><a href="/index.php">Home</a></li>
          <li><a href="/about_us.php">About</a></li>
          <li><a href="/Hadoop/BigData_hadoop_Install_on_ubuntu_single_node_cluster.php">Big Data</a></li>
          <li><a href="/python/scikit-learn/Artificial-Neural-Network-ANN-1-Introduction.php">Machine Learning</a></li>
          <li><a href="/AngularJS/AngularJS_Introduction.php">AngularJS</a></li> 
          <li><a href="/python/pytut.php">Python</a></li>
          <li><a href="/cplusplus/cpptut.php">C++</a></li>
          <li><a href="/GoLang/GoLang_Closures_Anonymous_Functions.php">go</a></li>
          <li><a href="/DevOps/DevOps_Jenkins_Chef_Puppet_Graphite_Logstash.php">DevOps </a></li>
          <li><a href="/DevOps/Docker/Docker-from-Monolithic-to-Micro-services-GCP-Kubernetes.php">Kubernetes </a></li>
          <li><a href="/Algorithms/algorithms.php">Algorithms</a></li> 
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">More...<b class="caret"></b></a>
            <ul class="dropdown-menu">
           
              <li><a href="/Qt/Qt5_Creating_QtQuick2_QML_Application_Animation_A.php">Qt 5</a></li>                           
              <li><a href="/Android/android.php">Android</a></li>
              
              <li><a href="/Linux/linux_tips1.php">Linux</a></li>
              <li><a href="/Java/tutorials/on_java.php">Java</a></li>
              <li><a href="/CSharp/.netframework.php">CSharp</a></li>
              <li><a href="/VideoStreaming/videostreaming_etc.php">Video Streaming</a></li>
              <li><a href="/FFMpeg/ffmpeg_fade_in_fade_out_transitions_effects_filters_slideshow_concat.php">FFmpeg</a></li>
              <li><a href="/Matlab/Matlab_Tutorial_Manipulating_Audio_I_Reverse_Delay_Tone_Control_Changing_Speed_Removing_Vocals.php">Matlab</a></li>
              <li><a href="/python/Django/Python_Django_Forums_Shared_Host.php">Django 1.8</a></li>
              <li><a href="/Laravel5/Laravel5_ToDo_List_Sample.php">Laravel 5.2</a></li>
              <li><a href="/RubyOnRails/RubyOnRails.php">Ruby On Rails</a></li>
              <li><a href="/HTML5/HTML5_Tutorial.php">HTML5 &amp; CSS</a></li>
              <!--<li><a href="/AmazingPlaces/index.php" target="_blank">
<img src="/Menus/MenuIcons/Earth_8px_transparent_background.png"
width="24" height="24"/>Earth</a> </li>-->
            </ul>
          </li>
        </ul>      
      </div>
    </div>  
  </nav>  

  <div id="main" style="height: auto !important;">
    <div class="container" style="height: auto !important;">
      <div class="row section featured topspace" style="height: auto !important;">
        <div class="row" style="height: auto !important;">
          <div class="col-sm-9 col-md-9 col-xs-9" style="height: auto !important; min-height: 0px !important;">
            <h2 class="section-title">Signal Processing with NumPy II - Image Fourier Transform : FFT &amp; DFT        <div id="___plusone_0" style="position: absolute; width: 450px; left: -10000px;"><iframe ng-non-bindable="" frameborder="0" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="position:absolute;top:-10000px;width:450px;margin:0px;border-style:none" tabindex="0" vspace="0" width="100%" id="I0_1608276999486" name="I0_1608276999486" src="https://apis.google.com/se/0/_/+1/fastbutton?usegapi=1&amp;origin=https%3A%2F%2Fwww.bogotobogo.com&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;gsrc=3p&amp;ic=1&amp;jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.zh_CN.YnQtsvjdhNk.O%2Fam%3DwQE%2Fd%3D1%2Fct%3Dzgms%2Frs%3DAGLTcCM3AUeqdmNhXMv7bPFaglkzmd4UXQ%2Fm%3D__features__#_methods=onPlusOne%2C_ready%2C_close%2C_open%2C_resizeMe%2C_renderstart%2Concircled%2Cdrefresh%2Cerefresh&amp;id=I0_1608276999486&amp;_gfid=I0_1608276999486&amp;parent=https%3A%2F%2Fwww.bogotobogo.com&amp;pfname=&amp;rpctoken=22552944" data-gapiattached="true"></iframe></div><g:plusone data-gapiscan="true" data-onload="true" data-gapistub="true"></g:plusone></h2>
            <div class="icon-image">
                <img src="/python/images/OpenCV_Logo.png" alt="OpenCV_Logo.png" />
            </div>
            <div class="SocialLinks">
  <span class="st__large" displaytext="" st_processed="yes"></span>
  <br /><br />
  <div align="center">
  <span class="st_facebook_large" displaytext="Facebook" st_processed="yes"><span style="text-decoration:none;color:#000000;display:inline-block;cursor:pointer;" class="stButton"><span class="stLarge" style="background-image: url(&quot;https://ws.sharethis.com/images/2017/facebook_32.png&quot;);"></span></span></span>
  <span class="st_twitter_large" displaytext="Tweet" st_processed="yes"><span style="text-decoration:none;color:#000000;display:inline-block;cursor:pointer;" class="stButton"><span class="stLarge" style="background-image: url(&quot;https://ws.sharethis.com/images/2017/twitter_32.png&quot;);"></span></span></span>
  <span class="st_linkedin_large" displaytext="LinkedIn" st_processed="yes"><span style="text-decoration:none;color:#000000;display:inline-block;cursor:pointer;" class="stButton"><span class="stLarge" style="background-image: url(&quot;https://ws.sharethis.com/images/2017/linkedin_32.png&quot;);"></span></span></span>
  </div>
  <br /><br />
  <script type="text/javascript" id="async-buttons" src="https://ws.sharethis.com/button/async-buttons.js"></script><script type="text/javascript" src="//w.sharethis.com/button/buttons.js"></script>
  <script type="text/javascript">stLight.options({publisher: "b9569c43-5f56-4501-92f0-4bf4aa8fceb0", doNotHash: false, doNotCopy: true, hashAddressBar: false});</script>
</div>

<div id="bookmarkshare">
  <script type="text/javascript">var addthis_config = {"data_track_clickback":true};</script>
  <a class="addthis_button" href="http://www.addthis.com/bookmark.php?v=250&amp;username=khhong7"><img src="//s7.addthis.com/static/btn/v2/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0" /></a>
  <script type="text/javascript" src="//s7.addthis.com/js/250/addthis_widget.js#username=khhong7"></script>
</div>

<br />
<hr />
<br />


<!-- Google bogo1 ad -->
<!-- Google search box -->



<!-- bogo1 -->
<div>
  <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo1 -->
  <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-4716428189734495" data-ad-slot="6542308167" data-adsbygoogle-status="done"><ins id="aswift_0_expand" style="display:inline-table;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_0_anchor" style="display:block;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:728px;height:90px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="728" height="90" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?guci=2.2.0.0.2.2.0.0&amp;client=ca-pub-4716428189734495&amp;output=html&amp;h=90&amp;slotname=6542308167&amp;adk=3310129852&amp;adf=1525819018&amp;pi=t.ma~as.6542308167&amp;w=728&amp;lmt=1608276999&amp;psa=1&amp;format=728x90&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;flash=0&amp;wgl=1&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hZHNlcnZpY2UuZ29vZ2xlLmNvbSIsInN0YXRlIjowfSx7Imlzc3Vlck9yaWdpbiI6Imh0dHBzOi8vYXR0ZXN0YXRpb24uYW5kcm9pZC5jb20iLCJzdGF0ZSI6MH1d&amp;dt=1608276999272&amp;bpp=23&amp;bdt=1230&amp;idt=144&amp;shv=r20201203&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;correlator=3507594198107&amp;frm=20&amp;pv=2&amp;ga_vid=1038897566.1608276999&amp;ga_sid=1608276999&amp;ga_hid=1295680669&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=88&amp;ady=632&amp;biw=912&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;eid=21066700%2C21066793&amp;oid=3&amp;pvsid=568029715867916&amp;pem=78&amp;rx=0&amp;eae=0&amp;fc=640&amp;brdim=86%2C9%2C86%2C9%2C1920%2C0%2C945%2C1020%2C929%2C889&amp;vis=1&amp;rsz=%7Co%7CeE%7C&amp;abl=NS&amp;pfx=0&amp;fu=8200&amp;bc=31&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;xpc=YLe9ube0bk&amp;p=https%3A//www.bogotobogo.com&amp;dtd=164" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!1" data-google-query-id="CKXk8tmC1-0CFReYvAod9-UPIQ" data-load-complete="true"></iframe></ins></ins></ins>
  <script>
   (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>


<!-- Google search box -->
<div class="AdSenseSearch">
  bogotobogo.com site search:
  <form action="//www.google.com" id="cse-search-box" target="_blank">
    <div>
      <input type="hidden" name="cx" value="partner-pub-4716428189734495:1794050961" />
      <input type="hidden" name="ie" value="UTF-8" />
      <!--<input type="text" name="q" size="55" />-->
      <input type="text" name="q" size="" width="90%" placeholder="Custom Search" style="border: 1px solid rgb(126, 157, 185); padding: 2px; background: url(&quot;https://www.google.com/cse/static/images/1x/googlelogo_lightgrey_46x16dp.png&quot;) left center no-repeat rgb(255, 255, 255); text-indent: 48px;" />
      <input type="submit" name="sa" value="Search" />
    </div>
  <input name="siteurl" type="hidden" value="www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" /><input name="ref" type="hidden" value="" /><input name="ss" type="hidden" value="" /><input name="siteurl" type="hidden" value="www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" /><input name="ref" type="hidden" value="" /><input name="ss" type="hidden" value="" /></form>
  <script type="text/javascript" src="//www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
</div>




<hr />
<div class="subtitle_2nd" id="NumPyFFT">Functions and values of NumPy FFT</div>
<p>The DFT (Discrete Fourier Transform) is defined as
<span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;msub&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;munderover&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/munderover&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;/msub&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;{&lt;/mo&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;&amp;#x03C0;&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mfrac&gt;&lt;mrow&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mfrac&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;}&lt;/mo&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1.&lt;/mn&gt;&lt;/math&gt;" role="presentation" style="text-align: center; position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" style="width: 26.302em; display: inline-block;"><span style="display: inline-block; position: relative; width: 21.194em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(0.54em, 1021.1em, 3.721em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-2"><span class="msubsup" id="MathJax-Span-3"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.138em, 1000.72em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-4" style="font-family: MathJax_Math-italic;">A</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.764em;"><span class="mi" id="MathJax-Span-5" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mo" id="MathJax-Span-6" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="munderover" id="MathJax-Span-7" style="padding-left: 0.271em;"><span style="display: inline-block; position: relative; width: 1.526em; height: 0px;"><span style="position: absolute; clip: rect(2.914em, 1001.39em, 4.572em, -999.998em); top: -3.985em; left: 0.047em;"><span class="mo" id="MathJax-Span-8" style="font-family: MathJax_Size2; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.362em, 1001.48em, 4.259em, -999.998em); top: -2.91em; left: 0em;"><span class="texatom" id="MathJax-Span-9"><span class="mrow" id="MathJax-Span-10"><span class="mi" id="MathJax-Span-11" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mo" id="MathJax-Span-12" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-13" style="font-size: 70.7%; font-family: MathJax_Main;">0</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.273em, 1001.26em, 4.169em, -999.998em); top: -5.15em; left: 0.092em;"><span class="texatom" id="MathJax-Span-14"><span class="mrow" id="MathJax-Span-15"><span class="mi" id="MathJax-Span-16" style="font-size: 70.7%; font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-17" style="font-size: 70.7%; font-family: MathJax_Main;">−</span><span class="mn" id="MathJax-Span-18" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="msubsup" id="MathJax-Span-19" style="padding-left: 0.181em;"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.407em, 1000.5em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-20" style="font-family: MathJax_Math-italic;">a</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.54em;"><span class="mi" id="MathJax-Span-21" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mi" id="MathJax-Span-22" style="font-family: MathJax_Math-italic;">e</span><span class="mi" id="MathJax-Span-23" style="font-family: MathJax_Math-italic;">x</span><span class="mi" id="MathJax-Span-24" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-25" style="font-family: MathJax_Main;">{</span><span class="mo" id="MathJax-Span-26" style="font-family: MathJax_Main;">−</span><span class="mn" id="MathJax-Span-27" style="font-family: MathJax_Main;">2</span><span class="mi" id="MathJax-Span-28" style="font-family: MathJax_Math-italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mi" id="MathJax-Span-29" style="font-family: MathJax_Math-italic;">i</span><span class="mfrac" id="MathJax-Span-30"><span style="display: inline-block; position: relative; width: 1.526em; height: 0px; margin-right: 0.137em; margin-left: 0.137em;"><span style="position: absolute; clip: rect(3.183em, 1001.39em, 4.124em, -999.998em); top: -4.657em; left: 50%; margin-left: -0.715em;"><span class="mrow" id="MathJax-Span-31"><span class="mi" id="MathJax-Span-32" style="font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-33" style="font-family: MathJax_Math-italic;">k</span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.407em, 1000.59em, 4.124em, -999.998em); top: -3.313em; left: 50%; margin-left: -0.311em;"><span class="mi" id="MathJax-Span-34" style="font-family: MathJax_Math-italic;">n</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(0.898em, 1001.53em, 1.212em, -999.998em); top: -1.297em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 1.526em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span><span class="mo" id="MathJax-Span-35" style="font-family: MathJax_Main;">}</span><span class="mspace" id="MathJax-Span-36" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mspace" id="MathJax-Span-37" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mi" id="MathJax-Span-38" style="font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-39" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mn" id="MathJax-Span-40" style="font-family: MathJax_Main; padding-left: 0.271em;">0</span><span class="mo" id="MathJax-Span-41" style="font-family: MathJax_Main;">,</span><span class="mo" id="MathJax-Span-42" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-43" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-44" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-45" style="font-family: MathJax_Main; padding-left: 0.181em;">,</span><span class="mi" id="MathJax-Span-46" style="font-family: MathJax_Math-italic; padding-left: 0.181em;">n</span><span class="mo" id="MathJax-Span-47" style="font-family: MathJax_Main; padding-left: 0.226em;">−</span><span class="mn" id="MathJax-Span-48" style="font-family: MathJax_Main; padding-left: 0.226em;">1.</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.553em; border-left: 0px solid; width: 0px; height: 3.725em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>A</mi><mi>k</mi></msub><mo>=</mo><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mo>=</mo><mn>0</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mi>n</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>a</mi><mi>m</mi></msub><mi>e</mi><mi>x</mi><mi>p</mi><mo fence="false" stretchy="false">{</mo><mo>−</mo><mn>2</mn><mi>π</mi><mi>i</mi><mfrac><mrow><mi>m</mi><mi>k</mi></mrow><mi>n</mi></mfrac><mo fence="false" stretchy="false">}</mo><mspace width="1em"/><mspace width="1em"/><mi>k</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mi>n</mi><mo>−</mo><mn>1.</mn></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-1">A_k = \sum_{m=0}^{n-1} a_m exp\{ -2\pi i \frac{mk}{n} \} \quad\quad k=0,...,n-1.</script>
The DFT is in general defined for <b>complex</b> inputs and outputs, and a single-frequency component at linear frequency f is represented by a complex exponential <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-2-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;{&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;&amp;#x03C0;&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mi mathvariant=&quot;normal&quot;&gt;&amp;#x0394;&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;}&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-49" style="width: 11.293em; display: inline-block;"><span style="display: inline-block; position: relative; width: 9.097em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1009.05em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-50"><span class="msubsup" id="MathJax-Span-51"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.407em, 1000.5em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-52" style="font-family: MathJax_Math-italic;">a</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.54em;"><span class="mi" id="MathJax-Span-53" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mo" id="MathJax-Span-54" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mi" id="MathJax-Span-55" style="font-family: MathJax_Math-italic; padding-left: 0.271em;">e</span><span class="mi" id="MathJax-Span-56" style="font-family: MathJax_Math-italic;">x</span><span class="mi" id="MathJax-Span-57" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-58" style="font-family: MathJax_Main;">{</span><span class="mn" id="MathJax-Span-59" style="font-family: MathJax_Main;">2</span><span class="mi" id="MathJax-Span-60" style="font-family: MathJax_Math-italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mi" id="MathJax-Span-61" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-62" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-63" style="font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-64" style="font-family: MathJax_Main;">Δ</span><span class="mi" id="MathJax-Span-65" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-66" style="font-family: MathJax_Main;">}</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>a</mi><mi>m</mi></msub><mo>=</mo><mi>e</mi><mi>x</mi><mi>p</mi><mo fence="false" stretchy="false">{</mo><mn>2</mn><mi>π</mi><mi>i</mi><mi>f</mi><mi>m</mi><mi mathvariant="normal">Δ</mi><mi>t</mi><mo fence="false" stretchy="false">}</mo></math></span></span><script type="math/tex" id="MathJax-Element-2">a_m = exp\{2\pi i f m \Delta t \}</script>, where <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-3-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi mathvariant=&quot;normal&quot;&gt;&amp;#x0394;&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-67" style="width: 1.526em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.526em, 1001.17em, 2.511em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-68"><span class="mi" id="MathJax-Span-69" style="font-family: MathJax_Main;">Δ</span><span class="mi" id="MathJax-Span-70" style="font-family: MathJax_Math-italic;">t</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.053em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi mathvariant="normal">Δ</mi><mi>t</mi></math></span></span><script type="math/tex" id="MathJax-Element-3">\Delta t</script> is the interval for sampling.</p>
<p>Here are the NumPy's fft functions and the values in the result:</p>
<ol>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-4-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-71" style="width: 7.41em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.866em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1005.78em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-72"><span class="mi" id="MathJax-Span-73" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-74" style="font-family: MathJax_Main; padding-left: 0.267em;">=</span><span class="mi" id="MathJax-Span-75" style="font-family: MathJax_Math-italic; padding-left: 0.267em;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-76" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-77" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-78" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-79" style="font-family: MathJax_Math-italic;">a</span><span class="mo" id="MathJax-Span-80" style="font-family: MathJax_Main;">,</span><span class="mi" id="MathJax-Span-81" style="font-family: MathJax_Math-italic; padding-left: 0.179em;">n</span><span class="mo" id="MathJax-Span-82" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>f</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mi>a</mi><mo>,</mo><mi>n</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-4">A=fft(a,n)</script></b> <br />
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-5-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-83" style="width: 2.242em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.794em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1001.66em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-84"><span class="mi" id="MathJax-Span-85" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-86" style="font-family: MathJax_Main;">[</span><span class="mn" id="MathJax-Span-87" style="font-family: MathJax_Main;">0</span><span class="mo" id="MathJax-Span-88" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mn>0</mn><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-5">A[0]</script> contains the zero-frequency term which is the mean of the signal. It is always purely real for real inputs.<br />
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-6-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;:&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo&gt;/&lt;/mo&gt;&lt;/mrow&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-89" style="width: 5.244em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.214em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1004.08em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-90"><span class="mi" id="MathJax-Span-91" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-92" style="font-family: MathJax_Main;">[</span><span class="mn" id="MathJax-Span-93" style="font-family: MathJax_Main;">1</span><span class="mo" id="MathJax-Span-94" style="font-family: MathJax_Main; padding-left: 0.271em;">:</span><span class="mi" id="MathJax-Span-95" style="font-family: MathJax_Math-italic; padding-left: 0.271em;">n</span><span class="texatom" id="MathJax-Span-96"><span class="mrow" id="MathJax-Span-97"><span class="mo" id="MathJax-Span-98" style="font-family: MathJax_Main;">/</span></span></span><span class="mn" id="MathJax-Span-99" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-100" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mn>1</mn><mo>:</mo><mi>n</mi><mrow class="MJX-TeXAtom-ORD"><mo>/</mo></mrow><mn>2</mn><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-6">A[1:n/2]</script> contains the positive-frequency terms.<br />
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-7-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo&gt;/&lt;/mo&gt;&lt;/mrow&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;:&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-101" style="width: 6.454em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.199em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1005.07em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-102"><span class="mi" id="MathJax-Span-103" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-104" style="font-family: MathJax_Main;">[</span><span class="mi" id="MathJax-Span-105" style="font-family: MathJax_Math-italic;">n</span><span class="texatom" id="MathJax-Span-106"><span class="mrow" id="MathJax-Span-107"><span class="mo" id="MathJax-Span-108" style="font-family: MathJax_Main;">/</span></span></span><span class="mn" id="MathJax-Span-109" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-110" style="font-family: MathJax_Main; padding-left: 0.226em;">+</span><span class="mn" id="MathJax-Span-111" style="font-family: MathJax_Main; padding-left: 0.226em;">1</span><span class="mo" id="MathJax-Span-112" style="font-family: MathJax_Main; padding-left: 0.271em;">:</span><span class="mo" id="MathJax-Span-113" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mi>n</mi><mrow class="MJX-TeXAtom-ORD"><mo>/</mo></mrow><mn>2</mn><mo>+</mo><mn>1</mn><mo>:</mo><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-7">A[n/2+1:]</script> contains the negative-frequency terms in the order of decreasing negative frequency
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-8-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo&gt;/&lt;/mo&gt;&lt;/mrow&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-114" style="width: 3.631em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.914em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1002.78em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-115"><span class="mi" id="MathJax-Span-116" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-117" style="font-family: MathJax_Main;">[</span><span class="mi" id="MathJax-Span-118" style="font-family: MathJax_Math-italic;">n</span><span class="texatom" id="MathJax-Span-119"><span class="mrow" id="MathJax-Span-120"><span class="mo" id="MathJax-Span-121" style="font-family: MathJax_Main;">/</span></span></span><span class="mn" id="MathJax-Span-122" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-123" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mi>n</mi><mrow class="MJX-TeXAtom-ORD"><mo>/</mo></mrow><mn>2</mn><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-8">A[n/2]</script> represents both positive and negative Nyquist frequency for an even number of input points. It is also purely real for real input. <br />
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-9-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo&gt;/&lt;/mo&gt;&lt;/mrow&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-124" style="width: 6.723em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.423em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1005.29em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-125"><span class="mi" id="MathJax-Span-126" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-127" style="font-family: MathJax_Main;">[</span><span class="mo" id="MathJax-Span-128" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-129" style="font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-130" style="font-family: MathJax_Main; padding-left: 0.226em;">−</span><span class="mn" id="MathJax-Span-131" style="font-family: MathJax_Main; padding-left: 0.226em;">1</span><span class="mo" id="MathJax-Span-132" style="font-family: MathJax_Main;">)</span><span class="texatom" id="MathJax-Span-133"><span class="mrow" id="MathJax-Span-134"><span class="mo" id="MathJax-Span-135" style="font-family: MathJax_Main;">/</span></span></span><span class="mn" id="MathJax-Span-136" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-137" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mo stretchy="false">(</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mrow class="MJX-TeXAtom-ORD"><mo>/</mo></mrow><mn>2</mn><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-9">A[(n-1)/2]</script> contains the largest positive frequency for an odd number of input points. <br />
    <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-10-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;[&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mo&gt;/&lt;/mo&gt;&lt;/mrow&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;]&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-138" style="width: 6.723em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.423em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1005.29em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-139"><span class="mi" id="MathJax-Span-140" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-141" style="font-family: MathJax_Main;">[</span><span class="mo" id="MathJax-Span-142" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-143" style="font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-144" style="font-family: MathJax_Main; padding-left: 0.226em;">+</span><span class="mn" id="MathJax-Span-145" style="font-family: MathJax_Main; padding-left: 0.226em;">1</span><span class="mo" id="MathJax-Span-146" style="font-family: MathJax_Main;">)</span><span class="texatom" id="MathJax-Span-147"><span class="mrow" id="MathJax-Span-148"><span class="mo" id="MathJax-Span-149" style="font-family: MathJax_Main;">/</span></span></span><span class="mn" id="MathJax-Span-150" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-151" style="font-family: MathJax_Main;">]</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo stretchy="false">[</mo><mo stretchy="false">(</mo><mi>n</mi><mo>+</mo><mn>1</mn><mo stretchy="false">)</mo><mrow class="MJX-TeXAtom-ORD"><mo>/</mo></mrow><mn>2</mn><mo stretchy="false">]</mo></math></span></span><script type="math/tex" id="MathJax-Element-10">A[(n+1)/2]</script> contains the largest negative frequency.<br />
</li>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-11-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;r&lt;/mi&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mi&gt;q&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-152" style="width: 5.955em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.72em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1004.63em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-153"><span class="mi" id="MathJax-Span-154" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-155" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-156" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-157" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-158" style="font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-159" style="font-family: MathJax_Math-italic;">e</span><span class="mi" id="MathJax-Span-160" style="font-family: MathJax_Math-italic;">q<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mo" id="MathJax-Span-161" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-162" style="font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-163" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mi>f</mi><mi>r</mi><mi>e</mi><mi>q</mi><mo stretchy="false">(</mo><mi>n</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-11">fftfreq(n)</script></b> <br /> 
    returns an array giving the frequencies of corresponding elements in the output.
  </li>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-12-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-164" style="width: 6.616em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.249em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1005.16em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-165"><span class="mi" id="MathJax-Span-166" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-167" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-168" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-169" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-170" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-171" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-172" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-173" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-174" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-175" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-176" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-12">fftshift(A)</script></b> <br /> 
    shifts transforms and their frequencies to put the zero-frequency components in the middle.
  </li>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-13-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-177" style="width: 7.057em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.602em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1005.51em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-178"><span class="mi" id="MathJax-Span-179" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-180" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-181" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-182" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-183" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-184" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-185" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-186" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.046em;"></span></span><span class="mi" id="MathJax-Span-187" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-188" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-189" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-190" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mi>f</mi><mi>f</mi><mi>t</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-13">ifftshift(A)</script></b> <br /> 
    undoes the shift done by <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-14-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-191" style="width: 6.499em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.244em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1005.15em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-192"><span class="mi" id="MathJax-Span-193" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-194" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-195" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-196" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-197" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-198" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-199" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-200" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-201" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-202" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-203" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-14">fftshift(A)</script>.
  </li>
</ol>
<br /><br />
<p>When <b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-15-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-204" style="width: 0.664em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.531em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.81em, 1000.49em, 2.515em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-205"><span class="mi" id="MathJax-Span-206" style="font-family: MathJax_Math-italic;">a</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.053em; border-left: 0px solid; width: 0px; height: 0.669em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></span></span><script type="math/tex" id="MathJax-Element-15">a</script></b> is a time-domain signal in <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-16-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-207" style="width: 5.961em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.796em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1004.71em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-208"><span class="mi" id="MathJax-Span-209" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-210" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mi" id="MathJax-Span-211" style="font-family: MathJax_Math-italic; padding-left: 0.271em;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-212" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-213" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-214" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-215" style="font-family: MathJax_Math-italic;">a</span><span class="mo" id="MathJax-Span-216" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mo>=</mo><mi>f</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mi>a</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-16">A = fft(a)</script> </p>
<ol>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-17-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-217" style="width: 3.75em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.956em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1002.87em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-218"><span class="mi" id="MathJax-Span-219" style="font-family: MathJax_Math-italic;">a</span><span class="mi" id="MathJax-Span-220" style="font-family: MathJax_Math-italic;">b</span><span class="mi" id="MathJax-Span-221" style="font-family: MathJax_Math-italic;">s</span><span class="mo" id="MathJax-Span-222" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-223" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-224" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>b</mi><mi>s</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-17">abs(A)</script></b> : its amplitude spectrum </li>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-18-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;{&lt;/mo&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;b&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;msup&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;}&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/msup&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-225" style="width: 5.514em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.367em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.413em, 1004.37em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-226"><span class="mo" id="MathJax-Span-227" style="font-family: MathJax_Main;">{</span><span class="mi" id="MathJax-Span-228" style="font-family: MathJax_Math-italic;">a</span><span class="mi" id="MathJax-Span-229" style="font-family: MathJax_Math-italic;">b</span><span class="mi" id="MathJax-Span-230" style="font-family: MathJax_Math-italic;">s</span><span class="mo" id="MathJax-Span-231" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-232" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-233" style="font-family: MathJax_Main;">)</span><span class="msubsup" id="MathJax-Span-234"><span style="display: inline-block; position: relative; width: 0.928em; height: 0px;"><span style="position: absolute; clip: rect(3.133em, 1000.44em, 4.411em, -999.998em); top: -4.01em; left: 0em;"><span class="mo" id="MathJax-Span-235" style="font-family: MathJax_Main;">}</span><span style="display: inline-block; width: 0px; height: 4.015em;"></span></span><span style="position: absolute; top: -4.363em; left: 0.487em;"><span class="mn" id="MathJax-Span-236" style="font-size: 70.7%; font-family: MathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.015em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.503em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo fence="false" stretchy="false">{</mo><mi>a</mi><mi>b</mi><mi>s</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo><msup><mo fence="false" stretchy="false">}</mo><mn>2</mn></msup></math></span></span><script type="math/tex" id="MathJax-Element-18">\{ abs(A) \}^2</script></b> : its power spectrum </li>
<li><b><span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-19-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mi&gt;g&lt;/mi&gt;&lt;mi&gt;l&lt;/mi&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-237" style="width: 4.896em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.882em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.501em, 1003.79em, 2.78em, -999.998em); top: -2.379em; left: 0em;"><span class="mrow" id="MathJax-Span-238"><span class="mi" id="MathJax-Span-239" style="font-family: MathJax_Math-italic;">a</span><span class="mi" id="MathJax-Span-240" style="font-family: MathJax_Math-italic;">n</span><span class="mi" id="MathJax-Span-241" style="font-family: MathJax_Math-italic;">g<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mi" id="MathJax-Span-242" style="font-family: MathJax_Math-italic;">l</span><span class="mi" id="MathJax-Span-243" style="font-family: MathJax_Math-italic;">e</span><span class="mo" id="MathJax-Span-244" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-245" style="font-family: MathJax_Math-italic;">A</span><span class="mo" id="MathJax-Span-246" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.383em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.392em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mi>n</mi><mi>g</mi><mi>l</mi><mi>e</mi><mo stretchy="false">(</mo><mi>A</mi><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-19">angle(A)</script></b> : its phase spectrum </li>
</ol>
<br />
<br />


<!-- bogo1 -->
<div>
  <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo1 -->
  <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-4716428189734495" data-ad-slot="6542308167" data-adsbygoogle-status="done"><ins id="aswift_1_expand" style="display:inline-table;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_1_anchor" style="display:block;border:none;height:90px;margin:0;padding:0;position:relative;visibility:visible;width:728px;background-color:transparent;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:728px;height:90px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="728" height="90" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?guci=2.2.0.0.2.2.0.0&amp;client=ca-pub-4716428189734495&amp;output=html&amp;h=90&amp;slotname=6542308167&amp;adk=3310129852&amp;adf=487272507&amp;pi=t.ma~as.6542308167&amp;w=728&amp;lmt=1608276999&amp;psa=1&amp;format=728x90&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;flash=0&amp;wgl=1&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hZHNlcnZpY2UuZ29vZ2xlLmNvbSIsInN0YXRlIjowfSx7Imlzc3Vlck9yaWdpbiI6Imh0dHBzOi8vYXR0ZXN0YXRpb24uYW5kcm9pZC5jb20iLCJzdGF0ZSI6MH1d&amp;dt=1608276999295&amp;bpp=4&amp;bdt=1253&amp;idt=272&amp;shv=r20201203&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=728x90%2C0x0&amp;nras=1&amp;correlator=3507594198107&amp;frm=20&amp;pv=1&amp;ga_vid=1038897566.1608276999&amp;ga_sid=1608276999&amp;ga_hid=1295680669&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=88&amp;ady=2033&amp;biw=912&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;eid=21066700%2C21066793&amp;oid=3&amp;pvsid=568029715867916&amp;pem=78&amp;rx=0&amp;eae=0&amp;fc=896&amp;brdim=86%2C9%2C86%2C9%2C1920%2C0%2C945%2C1020%2C929%2C889&amp;vis=1&amp;rsz=%7Co%7CeEbr%7C&amp;abl=NS&amp;pfx=0&amp;fu=8200&amp;bc=31&amp;ifi=2&amp;uci=a!2&amp;btvi=1&amp;fsb=1&amp;xpc=h2vS4S60SP&amp;p=https%3A//www.bogotobogo.com&amp;dtd=277" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!2" data-google-query-id="CIPw9tmC1-0CFRWWvAodz80Lag" data-load-complete="true"></iframe></ins></ins></ins>
  <script>
   (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>


<!-- Google search box -->
<div class="AdSenseSearch">
  bogotobogo.com site search:
  <form action="//www.google.com" id="cse-search-box" target="_blank">
    <div>
      <input type="hidden" name="cx" value="partner-pub-4716428189734495:1794050961" />
      <input type="hidden" name="ie" value="UTF-8" />
      <!--<input type="text" name="q" size="55" />-->
      <input type="text" name="q" size="" width="90%" />
      <input type="submit" name="sa" value="Search" />
    </div>
  </form>
  <script type="text/javascript" src="//www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
</div>


<br />
<br />
<div class="subtitle_2nd" id="imageFFT">Image FFT</div>
<pre>import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xfiles.jpg',0)
f = np.<font color="red">fft.fft2</font>(img)
fshift = np.<font color="red">fft.fftshift</font>(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()          
</pre>
<p>The '2' in <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-20-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-247" style="width: 3.407em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.735em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1002.65em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-248"><span class="mi" id="MathJax-Span-249" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-250" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-251" style="font-family: MathJax_Math-italic;">t</span><span class="mn" id="MathJax-Span-252" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-253" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-254" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mn>2</mn><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-20">fft2()</script> indicates that we're using 2-D fft. The <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-21-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-255" style="width: 3.407em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.735em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1002.65em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-256"><span class="mi" id="MathJax-Span-257" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-258" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-259" style="font-family: MathJax_Math-italic;">t</span><span class="mn" id="MathJax-Span-260" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-261" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-262" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mn>2</mn><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-21">fft2()</script> provides us the frequency transform which will be a complex array. Its first argument is the input image, which is grayscale. Second argument is optional which decides the size of output array.</p><div class="google-auto-placed ap_container" style="width: 100%; height: auto; clear: both; text-align: center;"><ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-4716428189734495" data-adsbygoogle-status="done" style="display: block; margin: auto; background-color: transparent; height: 280px;"><ins id="aswift_6_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:545px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_6_anchor" style="display: block; border: none; height: 280px; margin: 0px; padding: 0px; position: relative; visibility: visible; width: 545px; background-color: transparent; overflow: visible;"><iframe id="aswift_6" name="aswift_6" style="left:0;position:absolute;top:0;border:0;width:545px;height:280px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="545" height="280" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?guci=2.2.0.0.2.2.0.0&amp;client=ca-pub-4716428189734495&amp;output=html&amp;h=280&amp;adk=3873897336&amp;adf=2992188620&amp;pi=t.aa~a.3797681019~i.64~rp.4&amp;w=545&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1608277000&amp;num_ads=1&amp;rafmt=1&amp;armr=3&amp;sem=mc&amp;pwprc=4645920336&amp;psa=1&amp;ad_type=text_image&amp;format=545x280&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;flash=0&amp;fwr=0&amp;pra=3&amp;rh=136&amp;rw=544&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;fa=27&amp;adsid=NT&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hZHNlcnZpY2UuZ29vZ2xlLmNvbSIsInN0YXRlIjowfSx7Imlzc3Vlck9yaWdpbiI6Imh0dHBzOi8vYXR0ZXN0YXRpb24uYW5kcm9pZC5jb20iLCJzdGF0ZSI6MH1d&amp;dt=1608277000441&amp;bpp=6&amp;bdt=2399&amp;idt=6&amp;shv=r20201203&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3Dc799334dc106ffe4-22c5a4fa39c5000a%3AT%3D1608276999%3ART%3D1608276999%3AS%3DALNI_MbeRpekBKcwFBZheDgmPnMZiw3wSQ&amp;prev_fmts=728x90%2C0x0%2C728x90%2C160x600&amp;nras=2&amp;correlator=3507594198107&amp;frm=20&amp;pv=1&amp;ga_vid=1038897566.1608276999&amp;ga_sid=1608276999&amp;ga_hid=1295680669&amp;ga_fc=1&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=88&amp;ady=2857&amp;biw=912&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;eid=21066700%2C21066793&amp;oid=3&amp;psts=AGkb-H_bjqosYYbpBdsEpRvqvOrHrbuZoZ7f8bR_uwHOaUc7Ylr_g_sej2my3iejZcI&amp;pvsid=568029715867916&amp;pem=78&amp;rx=0&amp;eae=0&amp;fc=384&amp;brdim=86%2C9%2C86%2C9%2C1920%2C0%2C945%2C1020%2C929%2C889&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=8328&amp;bc=31&amp;jar=2020-12-18-04&amp;ifi=6&amp;uci=a!6&amp;btvi=2&amp;fsb=1&amp;xpc=9426VlLcqF&amp;p=https%3A//www.bogotobogo.com&amp;dtd=103" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!6" data-google-query-id="CKbku9qC1-0CFdEnvAodCf0PQQ" data-load-complete="true"></iframe></ins></ins></ins></div>
<p>If we use interactive shell, the <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-22-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-263" style="width: 0.674em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.54em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.526em, 1000.54em, 2.735em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-264"><span class="mi" id="MathJax-Span-265" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.331em; border-left: 0px solid; width: 0px; height: 1.225em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi></math></span></span><script type="math/tex" id="MathJax-Element-22">f</script> looks like this:</p>
<pre>&gt;&gt;&gt; f.shape
(194, 259)
</pre>
<br />
<p>We can see <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-23-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-266" style="width: 3.407em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.735em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1002.65em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-267"><span class="mi" id="MathJax-Span-268" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-269" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-270" style="font-family: MathJax_Math-italic;">t</span><span class="mn" id="MathJax-Span-271" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-272" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-273" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>t</mi><mn>2</mn><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-23">fft2()</script> returns a complex array:</p>
<pre>&gt;&gt;&gt; f
array([[ 842784.00000000    +0.j        , -517752.56442341 -3696.20384447j,
          91285.56071617 +4921.45028062j, ...,
         -46601.18635079 -4814.84303878j,   91285.56071617 -4921.45028062j,
        -517752.56442341 +3696.20384447j],
       [ 123232.14686474+22090.02037498j,    -856.26680325 +9182.45344817j,
        -136191.25175358-51466.45725155j, ...,
          71425.20605824+14903.15993681j, -158452.77640809-31181.5124568j ,
          -3060.27297752+19352.80159523j],
       [ -36743.19890402-14189.86326576j,   28037.83427034+45830.48236385j,
          -5472.34460100  +751.10794956j, ...,
         -17431.81487318-56998.95644394j,  -27977.32223743-17396.44346126j,
          55230.60393901+23180.07097916j],
       ..., 
       [-107889.78457811+41341.29205987j,   15392.03432529 +8349.74473343j,
          61145.55093605-59049.02715308j, ...,
          40527.83113022+19449.36030634j,   73913.64630259-52167.06835863j,
          -7173.60813531 +8395.54640485j],
       [ -36743.19890402+14189.86326576j,   55230.60393901-23180.07097916j,
         -27977.32223743+17396.44346126j, ...,
         -29773.75673263+47038.82271301j,   -5472.34460100  -751.10794956j,
          28037.83427034-45830.48236385j],
       [ 123232.14686474-22090.02037498j,   -3060.27297752-19352.80159523j,
        -158452.77640809+31181.5124568j , ...,
          58992.94700240 +3233.35145839j, -136191.25175358+51466.45725155j,
           -856.26680325 -9182.45344817j]])
</pre>
<p>We did <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-24-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-274" style="width: 5.11em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.124em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1004.03em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-275"><span class="mi" id="MathJax-Span-276" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-277" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-278" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-279" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-280" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-281" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-282" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-283" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-284" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-24">ffshift()</script> because we want to place the zero-frequency component to the center of the spectrum. In other words, once we got the result, zero frequency component (DC component) will be at top left corner. Because we want to bring it to center, we needed to shift the result by <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-25-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mfrac&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;/mfrac&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-285" style="width: 1.033em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.809em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.526em, 1000.81em, 2.87em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-286"><span class="mfrac" id="MathJax-Span-287"><span style="display: inline-block; position: relative; width: 0.54em; height: 0px; margin-right: 0.137em; margin-left: 0.137em;"><span style="position: absolute; clip: rect(3.542em, 1000.4em, 4.124em, -999.998em); top: -4.388em; left: 50%; margin-left: -0.222em;"><span class="mi" id="MathJax-Span-288" style="font-size: 70.7%; font-family: MathJax_Math-italic;">n</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.362em, 1000.32em, 4.124em, -999.998em); top: -3.627em; left: 50%; margin-left: -0.177em;"><span class="mn" id="MathJax-Span-289" style="font-size: 70.7%; font-family: MathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(0.898em, 1000.54em, 1.212em, -999.998em); top: -1.297em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 0.54em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.497em; border-left: 0px solid; width: 0px; height: 1.447em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mfrac><mi>n</mi><mn>2</mn></mfrac></math></span></span><script type="math/tex" id="MathJax-Element-25">\frac{n}{2}</script> in both the directions using <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-26-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-290" style="width: 9.904em; display: inline-block;"><span style="display: inline-block; position: relative; width: 7.977em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1007.89em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-291"><span class="mi" id="MathJax-Span-292" style="font-family: MathJax_Math-italic;">n</span><span class="mi" id="MathJax-Span-293" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-294" style="font-family: MathJax_Main;">.</span><span class="mi" id="MathJax-Span-295" style="font-family: MathJax_Math-italic; padding-left: 0.181em;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-296" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-297" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-298" style="font-family: MathJax_Main;">.</span><span class="mi" id="MathJax-Span-299" style="font-family: MathJax_Math-italic; padding-left: 0.181em;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-300" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-301" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-302" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-303" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-304" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-305" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-306" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-307" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-308" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mi>p</mi><mo>.</mo><mi>f</mi><mi>f</mi><mi>t</mi><mo>.</mo><mi>f</mi><mi>f</mi><mi>t</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-26">np.fft.fftshift()</script>.</p><div class="google-auto-placed ap_container" style="width: 100%; height: auto; clear: both; text-align: center;"><ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-4716428189734495" data-adsbygoogle-status="done" style="display: block; margin: auto; background-color: transparent; height: 280px;"><ins id="aswift_8_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:545px;background-color:transparent;"><ins id="aswift_8_anchor" style="display:block;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:545px;background-color:transparent;"></ins></ins></ins></div>
<p>Once we found the frequency transform, we can find the magnitude spectrum:</p>
<pre>magnitude_spectrum = 20*np.log(np.abs(fshift))
</pre>
<br />
<img alt="NumPyFFT_xfiles.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_xfiles.png" />
<br />
<p>Now we can see more whiter region at the center showing we have more low frequency content.</p>
<br />
<br />

<!-- Google bogo_square_ad -->
<div>
  <script type="text/javascript">
    google_ad_client = "ca-pub-4716428189734495";
    /* bogo_LargeRectangle_336_280 */
    google_ad_slot = "2712696561";
    google_ad_width = 336;
    google_ad_height = 280;
  </script>
  <script type="text/javascript" src="//pagead2.googlesyndication.com/pagead/show_ads.js">
  </script><ins id="aswift_2_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:336px;background-color:transparent;" data-ad-slot="2712696561"><ins id="aswift_2_anchor" style="display:block;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:336px;background-color:transparent;"></ins></ins>
</div>
<br />





<br />
<br />
<p>If we undo the shift using <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-27-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-309" style="width: 5.11em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.124em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1004.03em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-310"><span class="mi" id="MathJax-Span-311" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-312" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-313" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-314" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-315" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-316" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-317" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-318" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-319" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>f</mi><mi>f</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-27">ffshift()</script>:</p>
<pre>f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift = np.fft.<font color="blue">ifftshift</font>(fshift)
</pre>
<p>The picture will look like this:</p>
<img alt="NumPyFFT_xfiles_No_Shift.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_xfiles_No_Shift.png" />
<br />
<br />
<br />
<br />
<br />
<div class="subtitle_2nd" id="more_samples">More Samples</div>
<p>Here are more fft samples:</p>
<img alt="NumPyFFT_snow.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_snow.png" />
<br />
<br />
<img alt="NumPyFFT_green.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_green.png" />
<br />
<br />
<img alt="NumPyFFT_black.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_black.png" />
<br />
<br />
<img alt="NumPyFFT_checker.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_checker.png" />
<br />
<br />
<img alt="NumPyFFT_maze.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_maze.png" />
<br />
<br />
<img alt="NumPyFFT_vlines.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_vlines.png" />
<br />
<br />
<img alt="NumPyFFT_hlines.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_hlines.png" />
<br />
<br />
<img alt="NumPyFFT_circle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_circle.png" />
<br />
<br />
<img alt="NumPyFFT_whitecircle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_whitecircle.png" />
<br />
<br />
<img alt="NumPyFFT_blackcircle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_blackcircle.png" />
<br />
<br />
<br />
<br />
<div class="subtitle_2nd" id="DFT">DFT and inverse DFT</div>
<p>We found the frequency transform for an image in the previous section. So, now we can do some operations in frequency domain, like high pass filtering (HPF) and reconstruct the image using inverse DFT.</p>
<p>We can simply remove the low frequencies by masking with a rectangular window of size 60x60. Then, apply the inverse shift using <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-28-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mi&gt;s&lt;/mi&gt;&lt;mi&gt;h&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-320" style="width: 6.006em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.841em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1004.75em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-321"><span class="mi" id="MathJax-Span-322" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-323" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-324" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-325" style="font-family: MathJax_Math-italic;">t</span><span class="mi" id="MathJax-Span-326" style="font-family: MathJax_Math-italic;">s</span><span class="mi" id="MathJax-Span-327" style="font-family: MathJax_Math-italic;">h</span><span class="mi" id="MathJax-Span-328" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-329" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-330" style="font-family: MathJax_Math-italic;">t</span><span class="mo" id="MathJax-Span-331" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-332" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mi>f</mi><mi>f</mi><mi>t</mi><mi>s</mi><mi>h</mi><mi>i</mi><mi>f</mi><mi>t</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-28">ifftshift()</script> so that DC component again come at the top-left corner. Then, find inverse FFT using <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-29-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;f&lt;/mi&gt;&lt;mi&gt;t&lt;/mi&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-333" style="width: 3.81em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.049em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.481em, 1002.96em, 2.78em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-334"><span class="mi" id="MathJax-Span-335" style="font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-336" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-337" style="font-family: MathJax_Math-italic;">f<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.047em;"></span></span><span class="mi" id="MathJax-Span-338" style="font-family: MathJax_Math-italic;">t</span><span class="mn" id="MathJax-Span-339" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-340" style="font-family: MathJax_Main;">(</span><span class="mo" id="MathJax-Span-341" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.386em; border-left: 0px solid; width: 0px; height: 1.336em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mi>f</mi><mi>f</mi><mi>t</mi><mn>2</mn><mo stretchy="false">(</mo><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-29">ifft2()</script> function. The result, again, will be a complex number. We can take its absolute value.</p><div class="google-auto-placed ap_container" style="width: 100%; height: auto; clear: both; text-align: center;"><ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-4716428189734495" data-adsbygoogle-status="done" style="display: block; margin: auto; background-color: transparent; height: 280px;"><ins id="aswift_9_expand" style="display:inline-table;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:545px;background-color:transparent;"><ins id="aswift_9_anchor" style="display:block;border:none;height:280px;margin:0;padding:0;position:relative;visibility:visible;width:545px;background-color:transparent;"></ins></ins></ins></div>
<p>The DFT (Discrete Fourier Transform) is defined as:
<span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-30-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;msub&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;munderover&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/munderover&gt;&lt;msub&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;/msub&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;{&lt;/mo&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;&amp;#x03C0;&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mfrac&gt;&lt;mrow&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mfrac&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;}&lt;/mo&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1.&lt;/mn&gt;&lt;/math&gt;" role="presentation" style="text-align: center; position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-342" style="width: 26.302em; display: inline-block;"><span style="display: inline-block; position: relative; width: 21.194em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(0.54em, 1021.1em, 3.721em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-343"><span class="msubsup" id="MathJax-Span-344"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.138em, 1000.72em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-345" style="font-family: MathJax_Math-italic;">A</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.764em;"><span class="mi" id="MathJax-Span-346" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mo" id="MathJax-Span-347" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="munderover" id="MathJax-Span-348" style="padding-left: 0.271em;"><span style="display: inline-block; position: relative; width: 1.526em; height: 0px;"><span style="position: absolute; clip: rect(2.914em, 1001.39em, 4.572em, -999.998em); top: -3.985em; left: 0.047em;"><span class="mo" id="MathJax-Span-349" style="font-family: MathJax_Size2; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.362em, 1001.48em, 4.259em, -999.998em); top: -2.91em; left: 0em;"><span class="texatom" id="MathJax-Span-350"><span class="mrow" id="MathJax-Span-351"><span class="mi" id="MathJax-Span-352" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mo" id="MathJax-Span-353" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-354" style="font-size: 70.7%; font-family: MathJax_Main;">0</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.273em, 1001.26em, 4.169em, -999.998em); top: -5.15em; left: 0.092em;"><span class="texatom" id="MathJax-Span-355"><span class="mrow" id="MathJax-Span-356"><span class="mi" id="MathJax-Span-357" style="font-size: 70.7%; font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-358" style="font-size: 70.7%; font-family: MathJax_Main;">−</span><span class="mn" id="MathJax-Span-359" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="msubsup" id="MathJax-Span-360" style="padding-left: 0.181em;"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.407em, 1000.5em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-361" style="font-family: MathJax_Math-italic;">a</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.54em;"><span class="mi" id="MathJax-Span-362" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mi" id="MathJax-Span-363" style="font-family: MathJax_Math-italic;">e</span><span class="mi" id="MathJax-Span-364" style="font-family: MathJax_Math-italic;">x</span><span class="mi" id="MathJax-Span-365" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-366" style="font-family: MathJax_Main;">{</span><span class="mo" id="MathJax-Span-367" style="font-family: MathJax_Main;">−</span><span class="mn" id="MathJax-Span-368" style="font-family: MathJax_Main;">2</span><span class="mi" id="MathJax-Span-369" style="font-family: MathJax_Math-italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mi" id="MathJax-Span-370" style="font-family: MathJax_Math-italic;">i</span><span class="mfrac" id="MathJax-Span-371"><span style="display: inline-block; position: relative; width: 1.526em; height: 0px; margin-right: 0.137em; margin-left: 0.137em;"><span style="position: absolute; clip: rect(3.183em, 1001.39em, 4.124em, -999.998em); top: -4.657em; left: 50%; margin-left: -0.715em;"><span class="mrow" id="MathJax-Span-372"><span class="mi" id="MathJax-Span-373" style="font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-374" style="font-family: MathJax_Math-italic;">k</span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.407em, 1000.59em, 4.124em, -999.998em); top: -3.313em; left: 50%; margin-left: -0.311em;"><span class="mi" id="MathJax-Span-375" style="font-family: MathJax_Math-italic;">n</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(0.898em, 1001.53em, 1.212em, -999.998em); top: -1.297em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 1.526em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span><span class="mo" id="MathJax-Span-376" style="font-family: MathJax_Main;">}</span><span class="mspace" id="MathJax-Span-377" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mspace" id="MathJax-Span-378" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mi" id="MathJax-Span-379" style="font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-380" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mn" id="MathJax-Span-381" style="font-family: MathJax_Main; padding-left: 0.271em;">0</span><span class="mo" id="MathJax-Span-382" style="font-family: MathJax_Main;">,</span><span class="mo" id="MathJax-Span-383" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-384" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-385" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-386" style="font-family: MathJax_Main; padding-left: 0.181em;">,</span><span class="mi" id="MathJax-Span-387" style="font-family: MathJax_Math-italic; padding-left: 0.181em;">n</span><span class="mo" id="MathJax-Span-388" style="font-family: MathJax_Main; padding-left: 0.226em;">−</span><span class="mn" id="MathJax-Span-389" style="font-family: MathJax_Main; padding-left: 0.226em;">1.</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.553em; border-left: 0px solid; width: 0px; height: 3.725em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>A</mi><mi>k</mi></msub><mo>=</mo><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mo>=</mo><mn>0</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mi>n</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>a</mi><mi>m</mi></msub><mi>e</mi><mi>x</mi><mi>p</mi><mo fence="false" stretchy="false">{</mo><mo>−</mo><mn>2</mn><mi>π</mi><mi>i</mi><mfrac><mrow><mi>m</mi><mi>k</mi></mrow><mi>n</mi></mfrac><mo fence="false" stretchy="false">}</mo><mspace width="1em"/><mspace width="1em"/><mi>k</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mi>n</mi><mo>−</mo><mn>1.</mn></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-30">A_k = \sum_{m=0}^{n-1} a_m exp\{ -2\pi i \frac{mk}{n} \} \quad\quad k=0,...,n-1.</script>
The inverse DFT is defined as this:
<span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-31-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;msub&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mfrac&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mfrac&gt;&lt;munderover&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;/mrow&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;/munderover&gt;&lt;msub&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;mi&gt;e&lt;/mi&gt;&lt;mi&gt;x&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;{&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;&amp;#x03C0;&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mfrac&gt;&lt;mrow&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/mrow&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;/mfrac&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;}&lt;/mo&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mspace width=&quot;1em&quot; /&gt;&lt;mi&gt;m&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;0&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;.&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;n&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mn&gt;1.&lt;/mn&gt;&lt;/math&gt;" role="presentation" style="text-align: center; position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-390" style="width: 27.422em; display: inline-block;"><span style="display: inline-block; position: relative; width: 22.09em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(0.54em, 1022em, 3.721em, -999.998em); top: -2.372em; left: 0em;"><span class="mrow" id="MathJax-Span-391"><span class="msubsup" id="MathJax-Span-392"><span style="display: inline-block; position: relative; width: 1.436em; height: 0px;"><span style="position: absolute; clip: rect(3.138em, 1000.72em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-393" style="font-family: MathJax_Math-italic;">A</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.764em;"><span class="mi" id="MathJax-Span-394" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mo" id="MathJax-Span-395" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mfrac" id="MathJax-Span-396" style="padding-left: 0.271em;"><span style="display: inline-block; position: relative; width: 0.719em; height: 0px; margin-right: 0.137em; margin-left: 0.137em;"><span style="position: absolute; clip: rect(3.183em, 1000.45em, 4.124em, -999.998em); top: -4.657em; left: 50%; margin-left: -0.267em;"><span class="mn" id="MathJax-Span-397" style="font-family: MathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.407em, 1000.59em, 4.124em, -999.998em); top: -3.313em; left: 50%; margin-left: -0.311em;"><span class="mi" id="MathJax-Span-398" style="font-family: MathJax_Math-italic;">n</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(0.898em, 1000.72em, 1.212em, -999.998em); top: -1.297em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 0.719em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span><span class="munderover" id="MathJax-Span-399" style="padding-left: 0.181em;"><span style="display: inline-block; position: relative; width: 1.436em; height: 0px;"><span style="position: absolute; clip: rect(2.914em, 1001.39em, 4.572em, -999.998em); top: -3.985em; left: 0em;"><span class="mo" id="MathJax-Span-400" style="font-family: MathJax_Size2; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.362em, 1001.26em, 4.259em, -999.998em); top: -2.865em; left: 0.092em;"><span class="texatom" id="MathJax-Span-401"><span class="mrow" id="MathJax-Span-402"><span class="mi" id="MathJax-Span-403" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-404" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-405" style="font-size: 70.7%; font-family: MathJax_Main;">0</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.273em, 1001.26em, 4.169em, -999.998em); top: -5.15em; left: 0.047em;"><span class="texatom" id="MathJax-Span-406"><span class="mrow" id="MathJax-Span-407"><span class="mi" id="MathJax-Span-408" style="font-size: 70.7%; font-family: MathJax_Math-italic;">n</span><span class="mo" id="MathJax-Span-409" style="font-size: 70.7%; font-family: MathJax_Main;">−</span><span class="mn" id="MathJax-Span-410" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="msubsup" id="MathJax-Span-411" style="padding-left: 0.181em;"><span style="display: inline-block; position: relative; width: 1.212em; height: 0px;"><span style="position: absolute; clip: rect(3.138em, 1000.72em, 4.124em, -999.998em); top: -3.985em; left: 0em;"><span class="mi" id="MathJax-Span-412" style="font-family: MathJax_Math-italic;">A</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; top: -3.851em; left: 0.764em;"><span class="mi" id="MathJax-Span-413" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span></span></span><span class="mi" id="MathJax-Span-414" style="font-family: MathJax_Math-italic;">e</span><span class="mi" id="MathJax-Span-415" style="font-family: MathJax_Math-italic;">x</span><span class="mi" id="MathJax-Span-416" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-417" style="font-family: MathJax_Main;">{</span><span class="mn" id="MathJax-Span-418" style="font-family: MathJax_Main;">2</span><span class="mi" id="MathJax-Span-419" style="font-family: MathJax_Math-italic;">π<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.002em;"></span></span><span class="mi" id="MathJax-Span-420" style="font-family: MathJax_Math-italic;">i</span><span class="mfrac" id="MathJax-Span-421"><span style="display: inline-block; position: relative; width: 1.526em; height: 0px; margin-right: 0.137em; margin-left: 0.137em;"><span style="position: absolute; clip: rect(3.183em, 1001.39em, 4.124em, -999.998em); top: -4.657em; left: 50%; margin-left: -0.715em;"><span class="mrow" id="MathJax-Span-422"><span class="mi" id="MathJax-Span-423" style="font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-424" style="font-family: MathJax_Math-italic;">k</span></span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(3.407em, 1000.59em, 4.124em, -999.998em); top: -3.313em; left: 50%; margin-left: -0.311em;"><span class="mi" id="MathJax-Span-425" style="font-family: MathJax_Math-italic;">n</span><span style="display: inline-block; width: 0px; height: 3.99em;"></span></span><span style="position: absolute; clip: rect(0.898em, 1001.53em, 1.212em, -999.998em); top: -1.297em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 1.526em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span><span class="mo" id="MathJax-Span-426" style="font-family: MathJax_Main;">}</span><span class="mspace" id="MathJax-Span-427" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mspace" id="MathJax-Span-428" style="height: 0em; vertical-align: 0em; width: 0.988em; display: inline-block; overflow: hidden;"></span><span class="mi" id="MathJax-Span-429" style="font-family: MathJax_Math-italic;">m</span><span class="mo" id="MathJax-Span-430" style="font-family: MathJax_Main; padding-left: 0.271em;">=</span><span class="mn" id="MathJax-Span-431" style="font-family: MathJax_Main; padding-left: 0.271em;">0</span><span class="mo" id="MathJax-Span-432" style="font-family: MathJax_Main;">,</span><span class="mo" id="MathJax-Span-433" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-434" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-435" style="font-family: MathJax_Main; padding-left: 0.181em;">.</span><span class="mo" id="MathJax-Span-436" style="font-family: MathJax_Main; padding-left: 0.181em;">,</span><span class="mi" id="MathJax-Span-437" style="font-family: MathJax_Math-italic; padding-left: 0.181em;">n</span><span class="mo" id="MathJax-Span-438" style="font-family: MathJax_Main; padding-left: 0.226em;">−</span><span class="mn" id="MathJax-Span-439" style="font-family: MathJax_Main; padding-left: 0.226em;">1.</span></span><span style="display: inline-block; width: 0px; height: 2.377em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.553em; border-left: 0px solid; width: 0px; height: 3.781em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>A</mi><mi>m</mi></msub><mo>=</mo><mfrac><mn>1</mn><mi>n</mi></mfrac><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mi>n</mi><mo>−</mo><mn>1</mn></mrow></munderover><msub><mi>A</mi><mi>k</mi></msub><mi>e</mi><mi>x</mi><mi>p</mi><mo fence="false" stretchy="false">{</mo><mn>2</mn><mi>π</mi><mi>i</mi><mfrac><mrow><mi>m</mi><mi>k</mi></mrow><mi>n</mi></mfrac><mo fence="false" stretchy="false">}</mo><mspace width="1em"/><mspace width="1em"/><mi>m</mi><mo>=</mo><mn>0</mn><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>,</mo><mi>n</mi><mo>−</mo><mn>1.</mn></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-31">A_m = \frac{1}{n} \sum_{k=0}^{n-1} A_k exp\{ 2\pi i \frac{mk}{n} \} \quad\quad m=0,...,n-1.</script>

</p><div class="subtitle_2nd" id="code&quot;">Code</div>
<pre>import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xfiles.jpg',0)

# fft to convert the image to freq domain 
f = np.fft.fft2(img)

# shift the center
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# remove the low frequencies by masking with a rectangular window of size 60x60
# High Pass Filter (HPF)
<font color="blue">fshift[crow-30:crow+30, ccol-30:ccol+30] = 0</font>

# shift back (we shifted the center before)
f_ishift = np.fft.<font color="red">ifftshift</font>(fshift)

# inverse fft to get the image back 
img_back = np.fft.<font color="red">ifft2</font>(f_ishift)

img_back = np.<font color="red">abs</font>(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Fianl Result'), plt.xticks([]), plt.yticks([])

plt.show()
</pre>
<br />
<img alt="IDFT.png" src="/python/OpenCV_Python/images/FFT/IDFT.png" />
<br />
<p>The result shows High Pass Filtering (HPF) is an edge detection operation. This also shows that most of the image data is present in the Low frequency region of the spectrum. </p>
<p>If we watch the result more closely, especially the last image, we can see some artifacts which shows some ripple like structures there, and it is called <b>ringing effects</b>. It is caused by the rectangular window we used for masking. This mask is converted to sine shape which causes this problem. So rectangular windows is not used for filtering. Better option is Gaussian Windows.</p>
<p>Now that we know how to find DFT, IDFT etc. in Numpy. So, let's do it with OpenCV but in next chapter.</p>
<br />
<br />
<div class="subtitle_2nd" id="refs">References</div>
<ol>
<li><a href="http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html#fourier-transform" target="_blank">Fourier Transform</a></li>
</ol>
<br /><br />
<br />
<br />

<br />
<br />
<h1>OpenCV 3 Tutorial </h1>
<h1>image &amp; video processing</h1>
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_ubuntu14_install_cmake.php" target="_blank">Installing on Ubuntu 13</a> 
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_mat_object_image_matrix_image_container.php" target="_blank">Mat(rix) object (Image Container)</a> 
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_creating_mat_objects.php" target="_blank">Creating Mat objects</a>
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_load_convert_save_image.php" target="_blank">The core : Image - load, convert, and save</a> 
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_imgproc_gausian_median_blur_bilateral_filter_image_smoothing.php" target="_blank">Smoothing Filters A - Average, Gaussian</a>
  <br /><br />
  <a href="/OpenCV/opencv_3_tutorial_imgproc_gausian_median_blur_bilateral_filter_image_smoothing_B.php" target="_blank">Smoothing Filters B - Median, Bilateral</a>
  <br /><br />

<br />
<br /><br /><br />
<h1>OpenCV 3 image and video processing with Python</h1>

   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3.php" target="_blank">OpenCV 3 with Python</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php" target="_blank">Image - OpenCV BGR : Matplotlib RGB</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php" target="_blank">Basic image operations - pixel access</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php" target="_blank">iPython - Signal Processing with NumPy</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT.php" target="_blank">Signal Processing with NumPy I - FFT and DFT for sine, square waves, unitpulse, and random signal</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" target="_blank">Signal Processing with NumPy II - Image Fourier Transform : FFT &amp; DFT</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Fourier_Transform_FFT_DFT.php" target="_blank">Inverse Fourier Transform of an Image with low pass filter: cv2.idft() </a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php" target="_blank">Image Histogram</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Changing_ColorSpaces_RGB_HSV_HLS.php" target="_blank">Video Capture and Switching colorspaces - RGB / HSV</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Global_Thresholding_Adaptive_Thresholding_Otsus_Binarization_Segmentations.php" target="_blank">Adaptive Thresholding - Otsu's clustering-based image thresholding</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php" target="_blank">Edge Detection - Sobel and Laplacian Kernels</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Canny_Edge_Detection.php" target="_blank">Canny Edge Detection</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php" target="_blank">Hough Transform - Circles</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation.php" target="_blank">Watershed Algorithm : Marker-based Segmentation I</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation_2.php" target="_blank">Watershed Algorithm : Marker-based Segmentation II</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php" target="_blank">Image noise reduction : Non-local Means denoising algorithm</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php" target="_blank">Image object detection : Face detection using Haar Cascade Classifiers</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Segmentation_by_Foreground_Extraction_Grabcut_Algorithm_based_on_Graph_cuts.php" target="_blank">Image segmentation - Foreground extraction Grabcut algorithm based on graph cuts</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_reconstruction_Inpainting_Interpolation.php" target="_blank">Image Reconstruction - Inpainting (Interpolation) - Fast Marching Methods</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_mean_shift_tracking_segmentation.php" target="_blank">Video : Mean shift object tracking</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization.php" target="_blank">Machine Learning : Clustering - K-Means clustering I</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization_2.php" target="_blank">Machine Learning : Clustering - K-Means clustering II</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Classification_K-nearest_neighbors_k-NN.php" target="_blank">Machine Learning : Classification - k-nearest neighbors (k-NN) algorithm</a> 


<br />
<br />
<br />
<br />
<br />

<p></p>
<div>
    
<div class="custom-disqus">
<!-- Disqus -->
<div id="disqus_thread"></div>
<script>
    /**
     *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
     *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
     */
     
/* Disabling Disqus 4/26/2017
    var disqus_config = function () {
        this.page.url = window.location.href;
        this.page.identifier = document.title;
    };
    
    (function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
        var d = document, s = d.createElement('script');
        
        s.src = '//bogotobogocom.disqus.com/embed.js';  // IMPORTANT: Replace EXAMPLE with your forum shortname!
        
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
 Disabling Disqus */    
</script>
<noscript>Please enable JavaScript to view the &lt;a href="https://disqus.com/?ref_noscript" rel="nofollow"&gt;comments powered by Disqus.&lt;/a&gt;</noscript>

<!-- Disqus ends here -->
</div>

<br />
<br />
<br />
<br /></div>
          </div>
          <div class="col-sm-3 col-md-3 col-xs-3">
  	    <div id="___person_0" style="position: absolute; width: 450px; left: -10000px;"><iframe ng-non-bindable="" frameborder="0" hspace="0" marginheight="0" marginwidth="0" scrolling="no" style="position:absolute;top:-10000px;width:450px;margin:0px;border-style:none" tabindex="0" vspace="0" width="100%" id="I1_1608276999494" name="I1_1608276999494" src="https://apis.google.com/_/widget/render/person?usegapi=1&amp;width=1&amp;href=%2F%2Fplus.google.com%2F111664369941456137911&amp;rel=author&amp;origin=https%3A%2F%2Fwww.bogotobogo.com&amp;gsrc=3p&amp;ic=1&amp;jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.zh_CN.YnQtsvjdhNk.O%2Fam%3DwQE%2Fd%3D1%2Fct%3Dzgms%2Frs%3DAGLTcCM3AUeqdmNhXMv7bPFaglkzmd4UXQ%2Fm%3D__features__#_methods=onPlusOne%2C_ready%2C_close%2C_open%2C_resizeMe%2C_renderstart%2Concircled%2Cdrefresh%2Cerefresh%2Conload&amp;id=I1_1608276999494&amp;_gfid=I1_1608276999494&amp;parent=https%3A%2F%2Fwww.bogotobogo.com&amp;pfname=&amp;rpctoken=17453382" data-gapiattached="true"></iframe></div><div class="g-person" data-width="1" data-href="//plus.google.com/111664369941456137911" data-rel="author" data-gapiscan="true" data-onload="true" data-gapistub="true">
  	    </div>
            <div class="resume">
              <p>Ph.D. / Golden Gate Ave, San Francisco / Seoul National Univ / Carnegie Mellon / UC Berkeley / DevOps / Deep Learning / Visualization</p>
            </div>
  	    <div>
                
<div class="skyscraper">
  <br />


<div class="skyscraper">

  <div class="bogo-paypal">
    <!-- Paypal Donate button -->
    <p><i>Sponsor Open Source development activities and free contents for everyone.</i></p>

    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input type="hidden" name="cmd" value="_s-xclick" />
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHRwYJKoZIhvcNAQcEoIIHODCCBzQCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYC0In+maN+zseQtRj6SJqP9kj2LLvKf0yFklTm01uHY7UwgB3YJ0MZwvi6iERXfh4x2/KVYyMzY6elATG68c3gd6gb0Pqca380dXCg2Xua8jlW0pTZ3UabUNkpYi0iIwMSUsvWKbIw9eX8cBljOrYU1CXNuk46c0Yz2J3lGG+xCZTELMAkGBSsOAwIaBQAwgcQGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQI23eIgGIDbFqAgaDMolOA+os0Y06D0j9NgHZJahDCSSl3deolhu6gz8hNd0SKwNAMBDPd5LBjJ7v6QgReCprB9L2E6CVpXZwgyLnzPC/wHbQG0Qd9sc/CqbiFy2FaJodDtPbRS8mOh+aHph0pNXgZ2kRA8uqVGIRF5gc0d6wqx7+NrPK5FehCMWoGGTmfTTMlykPVQhwDAY8+QFNSbCnqih5GXX62XpkmMJWFoIIDhzCCA4MwggLsoAMCAQICAQAwDQYJKoZIhvcNAQEFBQAwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMB4XDTA0MDIxMzEwMTMxNVoXDTM1MDIxMzEwMTMxNVowgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBR07d/ETMS1ycjtkpkvjXZe9k+6CieLuLsPumsJ7QC1odNz3sJiCbs2wC0nLE0uLGaEtXynIgRqIddYCHx88pb5HTXv4SZeuv0Rqq4+axW9PLAAATU8w04qqjaSXgbGLP3NmohqM6bV9kZZwZLR/klDaQGo1u9uDb9lr4Yn+rBQIDAQABo4HuMIHrMB0GA1UdDgQWBBSWn3y7xm8XvVk/UtcKG+wQ1mSUazCBuwYDVR0jBIGzMIGwgBSWn3y7xm8XvVk/UtcKG+wQ1mSUa6GBlKSBkTCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb22CAQAwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQCBXzpWmoBa5e9fo6ujionW1hUhPkOBakTr3YCDjbYfvJEiv/2P+IobhOGJr85+XHhN0v4gUkEDI8r2/rNk1m0GA8HKddvTjyGw/XqXa+LSTlDYkqI8OwR8GEYj4efEtcRpRYBxV8KxAW93YDWzFGvruKnnLbDAF6VR5w/cCMn5hzGCAZowggGWAgEBMIGUMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbQIBADAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMTUwOTA2MTYwNDAxWjAjBgkqhkiG9w0BCQQxFgQUuyx70nay4O6eJQs3x4WiAm4/7DkwDQYJKoZIhvcNAQEBBQAEgYAN7yS/34G8dBK6CfFf5g4rQk/H8s7D/aUmIzppGWOoXR7nZuXQo99wSBlQsPdeFtB+a+NNapf6lC4ibUTjgSpbu1gscGHH4Y+QtXl03bt5qgaSoFhZsCJKubwRHPHGHDGVx+tQmQ2DHk09lXjjL61FpB6iqkiFFvw4vfixsoeI6g==-----END PKCS7-----&#10;    " />
    <input type="image" src="https://www.paypalobjects.com/webstatic/en_US/btn/btn_donate_pp_142x27.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!" />
    <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1" />
    </form>
    <p><i>Thank you.</i></p>
    <p>- <a href="http://bogotobogo.com/about_us.php" target="_blank">K Hong</a></p>
    <!-- End of Paypal Donate button   -->
  </div>


  <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo_skyscraper -->
  <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-4716428189734495" data-ad-slot="5321096966" data-adsbygoogle-status="done"><ins id="aswift_3_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_3_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;"><iframe id="aswift_3" name="aswift_3" style="left:0;position:absolute;top:0;border:0;width:160px;height:600px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="160" height="600" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?guci=2.2.0.0.2.2.0.0&amp;client=ca-pub-4716428189734495&amp;output=html&amp;h=600&amp;slotname=5321096966&amp;adk=3075861136&amp;adf=1846699128&amp;pi=t.ma~as.5321096966&amp;w=160&amp;lmt=1608276999&amp;psa=1&amp;format=160x600&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;flash=0&amp;wgl=1&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hZHNlcnZpY2UuZ29vZ2xlLmNvbSIsInN0YXRlIjowfSx7Imlzc3Vlck9yaWdpbiI6Imh0dHBzOi8vYXR0ZXN0YXRpb24uYW5kcm9pZC5jb20iLCJzdGF0ZSI6MH1d&amp;dt=1608276999374&amp;bpp=9&amp;bdt=1332&amp;idt=317&amp;shv=r20201203&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=728x90%2C0x0%2C728x90&amp;nras=1&amp;correlator=3507594198107&amp;frm=20&amp;pv=1&amp;ga_vid=1038897566.1608276999&amp;ga_sid=1608276999&amp;ga_hid=1295680669&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=663&amp;ady=615&amp;biw=912&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;eid=21066700%2C21066793&amp;oid=3&amp;pvsid=568029715867916&amp;pem=78&amp;rx=0&amp;eae=0&amp;fc=896&amp;brdim=86%2C9%2C86%2C9%2C1920%2C0%2C945%2C1020%2C929%2C889&amp;vis=1&amp;rsz=%7Co%7CeE%7C&amp;abl=NS&amp;pfx=0&amp;fu=8200&amp;bc=31&amp;ifi=4&amp;uci=a!4&amp;fsb=1&amp;xpc=W4kZFUZFOm&amp;p=https%3A//www.bogotobogo.com&amp;dtd=337" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!4" data-google-query-id="CMqFgtqC1-0CFQKNvAod8XUL3A" data-load-complete="true"></iframe></ins></ins></ins>
  <script>
  (adsbygoogle = window.adsbygoogle || []).push({});
  </script>


  <br /><br />





</div></div>




<!-- Place this tag after the last widget tag. -->
<script type="text/javascript">
        (function() {
          var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
          po.src = 'https://apis.google.com/js/platform.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        })();
</script>
  	    </div>
  	    <div class="side_menu">
                
<br /><br />

<br /><br /><br />
<h1>OpenCV 3 image and video processing with Python</h1>

   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3.php" target="_blank">OpenCV 3 with Python</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php" target="_blank">Image - OpenCV BGR : Matplotlib RGB</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php" target="_blank">Basic image operations - pixel access</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php" target="_blank">iPython - Signal Processing with NumPy</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT.php" target="_blank">Signal Processing with NumPy I - FFT and DFT for sine, square waves, unitpulse, and random signal</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" target="_blank">Signal Processing with NumPy II - Image Fourier Transform : FFT &amp; DFT</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Fourier_Transform_FFT_DFT.php" target="_blank">Inverse Fourier Transform of an Image with low pass filter: cv2.idft() </a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php" target="_blank">Image Histogram</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Changing_ColorSpaces_RGB_HSV_HLS.php" target="_blank">Video Capture and Switching colorspaces - RGB / HSV</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Global_Thresholding_Adaptive_Thresholding_Otsus_Binarization_Segmentations.php" target="_blank">Adaptive Thresholding - Otsu's clustering-based image thresholding</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php" target="_blank">Edge Detection - Sobel and Laplacian Kernels</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Canny_Edge_Detection.php" target="_blank">Canny Edge Detection</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php" target="_blank">Hough Transform - Circles</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation.php" target="_blank">Watershed Algorithm : Marker-based Segmentation I</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation_2.php" target="_blank">Watershed Algorithm : Marker-based Segmentation II</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php" target="_blank">Image noise reduction : Non-local Means denoising algorithm</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php" target="_blank">Image object detection : Face detection using Haar Cascade Classifiers</a> 
   <div class="google-auto-placed ap_container" style="width: 100%; height: auto; clear: both; text-align: center;"><ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-4716428189734495" data-adsbygoogle-status="done" style="display: block; margin: auto; background-color: transparent; height: 600px;"><ins id="aswift_7_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:162px;background-color:transparent;"><ins id="aswift_7_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:162px;background-color:transparent;"></ins></ins></ins></div><br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_Segmentation_by_Foreground_Extraction_Grabcut_Algorithm_based_on_Graph_cuts.php" target="_blank">Image segmentation - Foreground extraction Grabcut algorithm based on graph cuts</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Image_reconstruction_Inpainting_Interpolation.php" target="_blank">Image Reconstruction - Inpainting (Interpolation) - Fast Marching Methods</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_mean_shift_tracking_segmentation.php" target="_blank">Video : Mean shift object tracking</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization.php" target="_blank">Machine Learning : Clustering - K-Means clustering I</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization_2.php" target="_blank">Machine Learning : Clustering - K-Means clustering II</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Classification_K-nearest_neighbors_k-NN.php" target="_blank">Machine Learning : Classification - k-nearest neighbors (k-NN) algorithm</a> 


<br />

<div class="skyscraper">
  <br />


<div class="skyscraper">

  <div class="bogo-paypal">
    <!-- Paypal Donate button -->
    <p><i>Sponsor Open Source development activities and free contents for everyone.</i></p>

    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input type="hidden" name="cmd" value="_s-xclick" />
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHRwYJKoZIhvcNAQcEoIIHODCCBzQCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYC0In+maN+zseQtRj6SJqP9kj2LLvKf0yFklTm01uHY7UwgB3YJ0MZwvi6iERXfh4x2/KVYyMzY6elATG68c3gd6gb0Pqca380dXCg2Xua8jlW0pTZ3UabUNkpYi0iIwMSUsvWKbIw9eX8cBljOrYU1CXNuk46c0Yz2J3lGG+xCZTELMAkGBSsOAwIaBQAwgcQGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQI23eIgGIDbFqAgaDMolOA+os0Y06D0j9NgHZJahDCSSl3deolhu6gz8hNd0SKwNAMBDPd5LBjJ7v6QgReCprB9L2E6CVpXZwgyLnzPC/wHbQG0Qd9sc/CqbiFy2FaJodDtPbRS8mOh+aHph0pNXgZ2kRA8uqVGIRF5gc0d6wqx7+NrPK5FehCMWoGGTmfTTMlykPVQhwDAY8+QFNSbCnqih5GXX62XpkmMJWFoIIDhzCCA4MwggLsoAMCAQICAQAwDQYJKoZIhvcNAQEFBQAwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMB4XDTA0MDIxMzEwMTMxNVoXDTM1MDIxMzEwMTMxNVowgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBR07d/ETMS1ycjtkpkvjXZe9k+6CieLuLsPumsJ7QC1odNz3sJiCbs2wC0nLE0uLGaEtXynIgRqIddYCHx88pb5HTXv4SZeuv0Rqq4+axW9PLAAATU8w04qqjaSXgbGLP3NmohqM6bV9kZZwZLR/klDaQGo1u9uDb9lr4Yn+rBQIDAQABo4HuMIHrMB0GA1UdDgQWBBSWn3y7xm8XvVk/UtcKG+wQ1mSUazCBuwYDVR0jBIGzMIGwgBSWn3y7xm8XvVk/UtcKG+wQ1mSUa6GBlKSBkTCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb22CAQAwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQCBXzpWmoBa5e9fo6ujionW1hUhPkOBakTr3YCDjbYfvJEiv/2P+IobhOGJr85+XHhN0v4gUkEDI8r2/rNk1m0GA8HKddvTjyGw/XqXa+LSTlDYkqI8OwR8GEYj4efEtcRpRYBxV8KxAW93YDWzFGvruKnnLbDAF6VR5w/cCMn5hzGCAZowggGWAgEBMIGUMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbQIBADAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMTUwOTA2MTYwNDAxWjAjBgkqhkiG9w0BCQQxFgQUuyx70nay4O6eJQs3x4WiAm4/7DkwDQYJKoZIhvcNAQEBBQAEgYAN7yS/34G8dBK6CfFf5g4rQk/H8s7D/aUmIzppGWOoXR7nZuXQo99wSBlQsPdeFtB+a+NNapf6lC4ibUTjgSpbu1gscGHH4Y+QtXl03bt5qgaSoFhZsCJKubwRHPHGHDGVx+tQmQ2DHk09lXjjL61FpB6iqkiFFvw4vfixsoeI6g==-----END PKCS7-----&#10;    " />
    <input type="image" src="https://www.paypalobjects.com/webstatic/en_US/btn/btn_donate_pp_142x27.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!" />
    <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1" />
    </form>
    <p><i>Thank you.</i></p>
    <p>- <a href="http://bogotobogo.com/about_us.php" target="_blank">K Hong</a></p>
    <!-- End of Paypal Donate button   -->
  </div>


  <script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo_skyscraper -->
  <ins class="adsbygoogle" style="display:inline-block;width:160px;height:600px" data-ad-client="ca-pub-4716428189734495" data-ad-slot="5321096966" data-adsbygoogle-status="done"><ins id="aswift_4_expand" style="display:inline-table;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;"><ins id="aswift_4_anchor" style="display:block;border:none;height:600px;margin:0;padding:0;position:relative;visibility:visible;width:160px;background-color:transparent;"></ins></ins></ins>
  <script>
  (adsbygoogle = window.adsbygoogle || []).push({});
  </script>


  <br /><br />





</div></div>

<br />
<div>
<br /><br />
<h1>Python tutorial</h1>
   <br /><br />
   <a href="/python/pytut.php">Python Home</a> 
   <br /><br />
   <a href="/python/python_introduction.php">Introduction</a> 
   <br /><br />
   <a href="/python/python_running.php">Running Python Programs (os, sys, import)</a> 
   <br /><br />
   <a href="/python/python_modules_idle.php">Modules and IDLE (Import, Reload, exec)</a> 
   <br /><br />
   <a href="/python/python_numbers_strings.php">Object Types - Numbers, Strings, and None</a> 
   <br /><br />
   <a href="/python/python_strings.php">Strings - Escape Sequence, Raw String, and Slicing</a> 
   <br /><br />
   <a href="/python/python_strings_method.php">Strings - Methods</a> 
   <br /><br />
   <a href="/python/python_string_formatting.php">Formatting Strings - expressions and method calls</a> 
   <br /><br />
   <a href="/python/python_files.php">Files and os.path</a> 
   <br /><br />
   <a href="/python/python_traversing_directory_tree_recursively_os_walk.php">Traversing directories recursively</a> 
   <br /><br />
   <a href="/python/python_subprocess_module.php">Subprocess Module</a> 
   <br /><br />
   <a href="/python/python_regularExpressions.php">Regular Expressions with Python</a> 
   <br /><br />
   <a href="/python/python_lists.php">Object Types - Lists</a> 
   <br /><br />
   <a href="/python/python_dictionaries_tuples.php">Object Types - Dictionaries and Tuples</a> 
   <br /><br />
   <a href="/python/python_functions_def.php">Functions def, *args, **kargs</a> 
   <br /><br />
   <a href="/python/python_functions_lambda.php">Functions lambda</a> 
   <br /><br />
   <a href="/python/python_functions_built_in.php">Built-in Functions</a> 
   <br /><br />
   <a href="/python/python_fncs_map_filter_reduce.php">map, filter, and reduce</a> 
   <br /><br />
   <a href="/python/python_decorators.php">Decorators</a> 
   <br /><br />
   <a href="/python/python_list_comprehension.php">List Comprehension</a> 
   <br /><br />
   <a href="/python/python_sets_union_intersection.php">Sets (union/intersection) and itertools - Jaccard coefficient and shingling to check plagiarism</a> 
   <br /><br />
   <a href="/python/python_hash_tables_hashing_dictionary_associated_arrays.php">Hashing (Hash tables and hashlib)</a> 
   <br /><br />
   <a href="/python/python_dictionary_comprehension_with_zip_from_list.php">Dictionary Comprehension with zip</a> 
   <br /><br />
   <a href="/python/python_function_with_yield_keyword_is_a_generator_iterator_next.php">The yield keyword</a> 
   <br /><br />
   <a href="/python/python_generators.php">Generator Functions and Expressions</a> 
   <br /><br />
   <a href="/python/python_function_with_generator_send_method_yield_keyword_iterator_next.php">generator.send() method</a> 
   <br /><br />
   <a href="/python/python_iterators.php">Iterators</a> 
   <br /><br />
   <a href="/python/python_classes_instances.php">Classes and Instances (__init__, __call__, etc.)</a>
   <br /><br />
   <a href="/python/python_if__name__equals__main__.php">if__name__ == '__main__'</a>
   <br /><br />
   <a href="/python/python_argparse.php">argparse</a>
   <br /><br />
   <a href="/python/python_try_except_finally_raise_syntax_error.php">Exceptions</a>
   <br /><br />
   <a href="/python/python_differences_between_static_method_and_class_method_instance_method.php">@static method vs class method</a>
   <br /><br />
   <a href="/python/python_private_attributes_methods.php">Private attributes and private methods</a>
   <br /><br />
   <a href="/python/python_bits_bytes_bitstring_constBitStream.php">bits, bytes, bitstring, and constBitStream</a>
   <br /><br />
   <a href="/python/python-json-dumps-loads-file-read-write.php">json.dump(s) and json.load(s)</a>
   <br /><br />
   <a href="/python/python_serialization_pickle_json.php">Python Object Serialization - pickle and json</a>
   <br /><br />
   <a href="/python/python_yaml_json_conversion.php">Python Object Serialization - yaml and json</a>
   <br /><br />
   <a href="/python/python_PriorityQueue_heapq_Data_Structure.php">Priority queue and heap queue data structure</a>
   <br /><br />
   <a href="/python/python_graph_data_structures.php">Graph data structure</a>
   <br /><br />
   <a href="/python/python_Dijkstras_Shortest_Path_Algorithm.php">Dijkstra's shortest path algorithm</a>
   <br /><br />
   <a href="/python/python_Prims_Spanning_Tree_Data_Structure.php">Prim's spanning tree algorithm</a>
   <br /><br />
   <a href="/python/python_closure.php">Closure</a>
   <br /><br />
   <a href="/python/python_functional_programming.php">Functional programming in Python</a>
   <br /><br />
   <a href="/python/python_ssh_remote_run.php">Remote running a local file using ssh </a>
   <br /><br />
   <a href="/python/python_sqlite_connect_create_drop_table.php">SQLite 3 - A. Connecting to DB, create/drop table, and insert data into a table</a>
   <br /><br />
   <a href="/python/python_sqlite_select_update_delete.php">SQLite 3 - B. Selecting, updating and deleting data</a>
   <br /><br />
   <a href="/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php">MongoDB with PyMongo I - Installing MongoDB ...</a>
   <br /><br />
   <a href="/python/python_http_web_services.php">Python HTTP Web Services - urllib, httplib2</a>
   <br /><br />
   <a href="/python/python_Web_scraping_with_selenium_for_domain_availability.php">Web scraping with Selenium for checking domain availability</a>
   <br /><br />
   <a href="/python/python-REST-API-Http-Requests-for-Humans-with-Flask.php">REST API : Http Requests for Humans with Flask</a>
   <br /><br />
   <a href="/python/Tornado/Python_Tornado_Blog_App.php">Blog app with Tornado</a>
   <br /><br />
   <a href="/python/Multithread/python_multithreading_creating_threads.php">Multithreading ...</a>
   <br /><br />
   <a href="/python/python_network_programming_server_client.php">Python Network Programming I - Basic Server / Client : A Basics</a>
   <br /><br />
   <a href="/python/python_network_programming_server_client_file_transfer.php">Python Network Programming I - Basic Server / Client : B File Transfer</a>
   <br /><br />
   <a href="/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php">Python Network Programming II - Chat Server / Client</a>
   <br /><br />
   <a href="/python/python_network_programming_socketserver_framework_for_network_servers.php">Python Network Programming III - Echo Server using socketserver network framework</a>
   <br /><br />
   <a href="/python/python_network_programming_socketserver_framework_for_network_servers_asynchronous_request_ThreadingMixIn_ForkingMixIn.php">Python Network Programming IV - Asynchronous Request Handling : ThreadingMixIn and ForkingMixIn</a>
   <br /><br />
   <a href="/python/python_interview_questions.php">Python Interview Questions I</a> 
   <br /><br />
   <a href="/python/python_interview_questions_2.php">Python Interview Questions II</a> 
   <br /><br />
   <a href="/python/python_interview_questions_3.php">Python Interview Questions III</a> 
   <br /><br />
   <a href="/python/python_interview_questions_4.php">Python Interview Questions IV</a> 
   <br /><br />
   <a href="/python/python_interview_questions_5.php">Python Interview Questions V</a> 
   <br /><br />
   <a href="/python/python_interview_questions_6.php">Python Interview Questions VI</a> 
   <br /><br />
   <a href="/python/python_interview_questions_7.php">Python Interview Questions VII</a> 
   <br /><br />
   <a href="/python/python_image_processing_with_Pillow_library.php">Image processing with Python image library Pillow</a> 
   <br /><br />
   <a href="/python/python_cpp_sip.php">Python and C++ with SIP</a> 
   <br /><br />
   <a href="/python/pydev_eclipse_plugin_install_python_IDE.php">PyDev with Eclipse</a> 
   <br /><br />
   <a href="/python/python_matplotlib.php">Matplotlib</a> 
   <br /><br />
   <a href="/python/python_redis_with_python.php">Redis with Python</a> 
   <br /><br />
   <a href="/python/python_numpy_array_tutorial_basic_A.php">NumPy array basics A</a> 
   <br /><br />
   <a href="/python/python_numpy_matrix_tutorial.php">NumPy Matrix and Linear Algebra</a> 
   <br /><br />
   <a href="/python/python_Pandas_NumPy_Matplotlib.php">Pandas with NumPy and Matplotlib</a> 
   <br /><br />
   <a href="/python/python_cellular_automata.php">Celluar Automata</a> 
   <br /><br />
   <a href="/python/python_numpy_batch_gradient_descent_algorithm.php">Batch gradient descent algorithm</a> 
   <br /><br />
   <a href="/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php">Longest Common Substring Algorithm</a> 
   <br /><br />
   <a href="/python/python_unit_testing.php">Python Unit Test - TDD using unittest.TestCase class</a> 
   <br /><br />
   <a href="/python/python_site_page_ranking_by_keywords.php">Simple tool - Google page ranking by keywords</a> 
   <br /><br />
   <a href="/python/GoogleApp/python_GoogleApp_HelloWorld.php">Google App Hello World</a> 
   <br /><br />
   <a href="/python/GoogleApp/python_GoogleApp_WebApp2_WSGI.php">Google App webapp2 and WSGI</a>
   <br /><br />
   <a href="/python/GoogleApp/python_GoogleApp_Uploading_HelloWorld.php">Uploading Google App Hello World</a> 
   <br /><br />
   <a href="/python/python_differences_Python2_vs_Python3_port.php">Python 2 vs Python 3</a> 
   <br /><br />
   <a href="/python/python_virtualenv_virtualenvwrapper.php">virtualenv and virtualenvwrapper</a> 
   <br /><br />
   <a href="/DevOps/AWS/aws_S3_uploading_large_file.php">Uploading a big file to AWS S3 using boto module</a> 
   <br /><br />
   <a href="/DevOps/AWS/aws_stopping_starting_instances.php">Scheduled stopping and starting an AWS instance</a> 
   <br /><br />
   <a href="/Hadoop/BigData_hadoop_CDH5_stop_start_services.php">Cloudera CDH5 - Scheduled stopping and starting services</a> 
   <br /><br />
   <a href="/python/python_Rackspace_API_curl_subprocess_Cloud_Files.php">Removing Cloud Files - Rackspace API with curl and subprocess</a> 
   <br /><br />
   <a href="/python/python-Windows-Check-if-a-Process-is-Running-Hanging-Schtasks-Run-Stop.php">Checking if a process is running/hanging and stop/run a scheduled task on Windows</a> 
   <br /><br />
   <a href="/Hadoop/BigData_hadoop_Apache_Spark_PySpark.php">Apache Spark 1.3 with PySpark (Spark Python API) Shell</a> 
   <br /><br />
   <a href="/Hadoop/BigData_hadoop_Apache_Spark_Streaming.php">Apache Spark 1.2 Streaming</a> 
   <br /><br />
   <a href="/python/Bottle/Python_Bottle_Framework.php">bottle 0.12.7 - Fast and simple WSGI-micro framework for small web-applications ...</a> 
   <br /><br />
   <a href="/python/Flask/Python_Flask_Blog_App_Production_with_MongoDB_and_Apache_WSGI.php">Flask app with Apache WSGI on Ubuntu14/CentOS7 ...</a> 
   <br /><br />
   <a href="/python/python_Selenium_WebDriver.php">Selenium WebDriver</a> 
   <br /><br />
   <a href="/python/Fabric/python_Fabric.php">Fabric - streamlining the use of SSH for application deployment</a> 
   <br /><br />
   <a href="/DevOps/Ansible/Ansible_SettingUp_Webservers_Nginx_Install_Env_Configure_Deploy_App.php" target="_blank">Ansible Quick Preview - Setting up web servers with Nginx, configure enviroments, and deploy an App</a>
   <br /><br />
   <a href="/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php">Neural Networks with backpropagation for XOR using one hidden layer</a> 
   <br /><br />
   <a href="/python/NLTK/NLTK_install.php">NLP - NLTK (Natural Language Toolkit) ...</a> 
   <br /><br />
   <a href="/python/RabbitMQ_Celery/python_Installing_RabbitMQ_Celery.php">RabbitMQ(Message broker server) and Celery(Task queue) ...</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php">OpenCV3 and Matplotlib ...</a> 
   <br /><br />
   <a href="/FFMpeg/ffmpeg_fade_in_fade_out_transitions_effects_filters_slideshow_concat.php">Simple tool - Concatenating slides using FFmpeg ...</a> 
   <br /><br />
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php">iPython - Signal Processing with NumPy</a> 
   <br /><br />
   <a href="/python/IPython/IPython_Jupyter_Install_iPython_Notebook_Matplotlib_Publishing_it_to_Github.php">iPython and Jupyter - Install Jupyter, iPython Notebook, drawing with Matplotlib, and publishing it to Github</a> 
   <br /><br />
   <a href="/python/IPython/iPython_Jupyter_Notebook_with_Embedded_D3.php">iPython and Jupyter Notebook with Embedded D3.js</a> 
   <br /><br />
   <a href="/VideoStreaming/YouTube/youtube-dl-embedding.php">Downloading YouTube videos using youtube-dl embedded with Python</a> 
   <br /><br />
   <a href="/python/scikit-learn/scikit_machine_learning_Supervised_Learning_Unsupervised_Learning.php">Machine Learning : scikit-learn ...</a> 
   <br /><br />
   <a href="/python/Django/Python_Django_tutorial_introduction.php">Django 1.6/1.8 Web Framework ...</a> 
</div>
<br />

  		
  	    </div>
          </div>
        </div>
      </div> <!-- / section -->
    </div>
  </div><iframe src="https://c.sharethis.mgr.consensu.org/portal-v2.html" id="st_gdpr_iframe" title="GDPR Consent Management" style="width: 0px; height: 0px; position: absolute; left: -5000px;"></iframe><div id="_atssh" style="visibility: hidden; height: 1px; width: 1px; position: absolute; top: -9999px; z-index: 100000;"><iframe id="_atssh282" title="AddThis utility frame" style="height: 1px; width: 1px; position: absolute; top: 0px; z-index: 100000; border: 0px; left: 0px;" src="https://s7.addthis.com/static/sh.f48a1a04fe8dbf021b4cda1d.html#rand=0.7822101962856853&amp;iit=1608276999510&amp;tmr=load%3D1608276999188%26core%3D1608276999232%26main%3D1608276999499%26ifr%3D1608276999515&amp;cb=0&amp;cdn=0&amp;md=0&amp;kw=OpenCV%203%20with%20Python%20Tutorial%3A%20Fourier%20Transform%20%3A%20FFT%20%26%20DFT%2CNumPy&amp;ab=-&amp;dh=www.bogotobogo.com&amp;dr=&amp;du=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;href=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;dt=OpenCV%203%20Signal%20Processing%20with%20NumPy%20II%20-%20Image%20Fourier%20Transform%20%3A%20FFT%20%26%20DFT%20-%202020&amp;dbg=0&amp;cap=tc%3D0%26ab%3D0&amp;inst=1&amp;jsl=33&amp;prod=undefined&amp;lng=zh&amp;ogt=&amp;pc=men&amp;pub=khhong7&amp;ssl=1&amp;sid=5fdc5c07cbe8e8ee&amp;srf=0.01&amp;ver=300&amp;xck=0&amp;xtr=0&amp;og=&amp;csi=undefined&amp;rev=v8.28.8-wp&amp;ct=1&amp;xld=1&amp;xd=1"></iframe></div><style id="service-icons-0"></style>

  <br />
<br />
<br />
<br />

<div class="custom-disqus">
<!-- Disqus -->
<!-- Disqus disabled Oct 17, 2016 
<div id="disqus_thread"></div>
<script>
    /**
     *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
     *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
     */
     
    var disqus_config = function () {
        this.page.url = window.location.href;
        this.page.identifier = document.title;
    };
    
    (function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
        var d = document, s = d.createElement('script');
        
        s.src = '//bogotobogocom.disqus.com/embed.js';  // IMPORTANT: Replace EXAMPLE with your forum shortname!
        
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
     
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
---- Disable -->
<!-- Disqus ends here -->
</div>

<br />
<br />
<br />
<br />


<!-- footer starts here -->
<footer id="footer">
  <div class="container">
    <div class="row">
      <div class="col-md-4 widget">
        <h3 class="widget-title">Contact</h3>
        <div class="widget-body">
          <p>BogoToBogo<br />
            <a href="mailto:contactus@bogotobogo.com">contactus@bogotobogo.com</a><br />
          </p>  
        </div>
      </div>

      <div class="col-md-4 widget">
        <h3 class="widget-title">Follow Bogotobogo</h3>
        <div class="widget-body">

          <!--
          <ul>
            <li><a href="https://www.facebook.com/KHongSanFrancisco" target="_unknown"><i class="fa fa-facebook"></i></a></li>
            <li><a href="https://twitter.com/KHongTwit" target="_unknown"><i class="fa fa-twitter"></i></a></li>
            <li><a href="https://plus.google.com/u/0/+KHongSanFrancisco/posts" target="_unknown"><i class="fa fa-google-plus"></i> </a></li>
          </ul>
          -->
             <h3>
             <a href="https://www.facebook.com/KHongSanFrancisco" target="_unknown"><i class="fa fa-facebook"></i></a> 
             <a href="https://twitter.com/KHongTwit" target="_unknown"><i class="fa fa-twitter"></i></a> 
             <!--<a href="https://plus.google.com/u/0/+KHongSanFrancisco/posts" target="_unknown"><i class="fa fa-google-plus"></i> </a> -->
             </h3>

        </div>
      </div>

      <div class="col-md-4 widget">
        <h3 class="widget-title"><a href="/about_us.php">About Us</a></h3>
        <div class="widget-body">
            <a href="mailto:contactus@bogotobogo.com">contactus@bogotobogo.com</a><br />
            <br />
            Golden Gate Ave, San Francisco, CA 94115
          <p></p>  
        </div>
      </div>

    </div> 
  </div>
</footer>

<footer id="underfooter">
  <div class="container">
    <div class="row">
      
      <div class="col-md-6 widget">
        <div class="widget-body">
          <p>Golden Gate Ave, San Francisco, CA 94115 </p>
        </div>
      </div>

      <div class="col-md-6 widget">
        <div class="widget-body">
          <p class="text-right">
            Copyright © 2020, bogotobogo<br /> 
            Design: <a href="http://www.bogotobogo.com" rel="designer">Web Master</a> </p>
        </div>
      </div>

    </div>
  </div>
</footer>

  <!-- JavaScript libs are placed at the end of the document so the pages load faster -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML" id="">
</script>
<!-- D3.js -->
<script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>

<!-- Google Analytics -->
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-12016988-2']);
    _gaq.push(['_trackPageview']);
    
    (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>

<!-- Google Analytics --> 
<!-- We need this for Analytics -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43017326-1', 'bogotobogo.com');
  ga('send', 'pageview');

</script>
  
<!-- Google+ -->
<script type="text/javascript" src="//apis.google.com/js/plusone.js" gapi_processed="true"></script>

  <!-- CDN MathJax -->
  <script type="text/x-mathjax-config;executed=true">
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML" id="">
  </script>




<ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;"><ins id="aswift_5_expand" style="display:inline-table;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_5_anchor" style="display:block;border:none;height:0px;margin:0;padding:0;position:relative;visibility:visible;width:0px;background-color:transparent;"><iframe id="aswift_5" name="aswift_5" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/ads?guci=2.2.0.0.2.2.0.0&amp;client=ca-pub-4716428189734495&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1608276999&amp;plat=1%3A8%2C2%3A16777224%2C9%3A32776%2C10%3A32%2C11%3A32%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1048576%2C32%3A32%2C40%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.bogotobogo.com%2Fpython%2FOpenCV_Python%2Fpython_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php&amp;ea=0&amp;flash=0&amp;pra=7&amp;wgl=1&amp;tt_state=W3siaXNzdWVyT3JpZ2luIjoiaHR0cHM6Ly9hZHNlcnZpY2UuZ29vZ2xlLmNvbSIsInN0YXRlIjowfSx7Imlzc3Vlck9yaWdpbiI6Imh0dHBzOi8vYXR0ZXN0YXRpb24uYW5kcm9pZC5jb20iLCJzdGF0ZSI6MH1d&amp;dt=1608276999530&amp;bpp=4&amp;bdt=1488&amp;idt=4&amp;shv=r20201203&amp;cbv=r20190131&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=728x90&amp;nras=1&amp;correlator=3507594198107&amp;frm=20&amp;pv=1&amp;ga_vid=1038897566.1608276999&amp;ga_sid=1608276999&amp;ga_hid=1295680669&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_java=0&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_nplug=3&amp;u_nmime=4&amp;adx=-12245933&amp;ady=-12245933&amp;biw=912&amp;bih=889&amp;scr_x=0&amp;scr_y=0&amp;eid=21066700%2C21066793&amp;oid=3&amp;pvsid=568029715867916&amp;pem=78&amp;rx=0&amp;eae=2&amp;fc=896&amp;brdim=86%2C9%2C86%2C9%2C1920%2C0%2C945%2C1020%2C929%2C889&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=8200&amp;bc=31&amp;ifi=5&amp;uci=a!5&amp;fsb=1&amp;dtd=17" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" data-google-container-id="a!5" data-load-complete="true"></iframe></ins></ins></ins><div id="stcpDiv" style="position: absolute; top: -1999px; left: -1988px;">ShareThis Copy and Paste</div><iframe id="google_osd_static_frame_3461183987912" name="google_osd_static_frame" style="display: none; width: 0px; height: 0px;"></iframe><iframe name="oauth2relay804259538" id="oauth2relay804259538" src="https://accounts.google.com/o/oauth2/postmessageRelay?parent=https%3A%2F%2Fwww.bogotobogo.com&amp;jsh=m%3B%2F_%2Fscs%2Fapps-static%2F_%2Fjs%2Fk%3Doz.gapi.zh_CN.YnQtsvjdhNk.O%2Fam%3DwQE%2Fd%3D1%2Fct%3Dzgms%2Frs%3DAGLTcCM3AUeqdmNhXMv7bPFaglkzmd4UXQ%2Fm%3D__features__#rpctoken=1704356772&amp;forcesecure=1" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-family: MathJax_Size2, sans-serif;"></div></div><div id="stwrapper" class="stwrapper stwrapper4x" style="display: none;"><iframe allowtransparency="true" id="stLframe" class="stLframe" name="stLframe" frameborder="0" scrolling="no" src="https://ws.sharethis.com/secure/index.html"></iframe></div><div id="stOverlay" onclick="javascript:stWidget.closeWidget();"></div></body><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20201203/r20190131/zrt_lookup.html#" data-ad-client="ca-pub-4716428189734495" style="display: none;"></iframe><ins class="adsbygoogle adsbygoogle-noablate" style="display: none !important; width: 100vw !important; height: 100vh !important; inset: 0px auto auto 0px !important; clear: none !important; float: none !important; margin: 0px !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; padding: 0px !important; position: fixed !important; vertical-align: baseline !important; visibility: visible !important; z-index: 2147483647 !important; background-color: white !important;" data-adsbygoogle-status="done" aria-hidden="true" data-vignette-loaded="true"><ins id="aswift_10_expand" style="display: inline-table !important; border: none !important; height: 100vh !important; margin: 0px !important; padding: 0px !important; position: relative !important; visibility: visible !important; width: 100vw !important; background-color: transparent !important; inset: auto !important; clear: none !important; float: none !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; vertical-align: baseline !important; z-index: auto !important;" tabindex="0" title="Advertisement" aria-label="Advertisement"><ins id="aswift_10_anchor" style="display: block !important; border: none !important; height: 100vh !important; margin: 0px !important; padding: 0px !important; position: relative !important; visibility: visible !important; width: 100vw !important; background-color: transparent !important; inset: auto !important; clear: none !important; float: none !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; vertical-align: baseline !important; z-index: auto !important;"><iframe id="aswift_10" name="" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="" height="" frameborder="0" src="https://googleads.g.doubleclick.net/pagead/html/r20201203/r20190131/zrt_lookup.html?fsb=1#RS-0-&amp;adk=1812271808&amp;client=ca-pub-4716428189734495&amp;fa=8&amp;ifi=10&amp;uci=a!a&amp;xpc=gcFvRdQ6bT&amp;p=https%3A//www.bogotobogo.com" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" style="width: 100vw !important; height: 100vh !important; inset: 0px auto auto 0px !important; position: absolute !important; clear: none !important; display: inline !important; float: none !important; margin: 0px !important; max-height: none !important; max-width: none !important; opacity: 1 !important; overflow: visible !important; padding: 0px !important; vertical-align: baseline !important; visibility: visible !important; z-index: auto !important;" data-google-container-id="a!a" data-google-query-id="CI259dmC1-0CFc4kvAodRncKnQ" data-load-complete="true"></iframe></ins></ins></ins></html>