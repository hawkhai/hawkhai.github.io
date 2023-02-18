<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
<title>K-means怎么选K?-SofaSofa</title>
<meta name="keywords" content="SofaSofa,数据科学,社区,统计/机器学习,无监督学习,开放问题," />
<meta name="description" content="K-means怎么选K?-SofaSofa数据科学社区" />


<script></script><script src="http://sofasofa.io/library/jquery/jquery.min.js"> </script>
<script src="http://sofasofa.io/library/bootbox.min.js"> </script>


  <script type="text/x-mathjax-config;executed=true">
  MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
      inlineMath: [ ['$','$']],
      displayMath: [ ['$$','$$']],
      processEscapes: true
    },
    "HTML-CSS": { fonts: ["TeX"] }
  });
</script>
  <script type="text/javascript" src="http://sofasofa.io/library/math/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<!-- Bootstrap -->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha/css/bootstrap.min.css" />
<link rel="icon" href="assets/images/s_ico.ico" />


<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha/js/bootstrap.min.js"></script>


<!--<link rel="stylesheet" href="../library/wenk.min.css">-->
<link rel="stylesheet" href="http://sofasfao.io/library/wenk.min.css" />
<!-- jQuery -->




<!-- Summernote -->

<link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/summernote/0.8.8/summernote-bs4.css" />
<script type="text/javascript" src="https://cdn.bootcdn.net/ajax/libs/summernote/0.8.8/summernote-bs4.js"></script>
  <link rel="stylesheet" href="http://sofasofa.io/library/font-awesome/css/font-awesome.min.css" />
  <script src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@0/summernote-ext-highlight.js"></script>
  <script src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@0/summernote-zh-CN.js"></script>


<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/animate.css" />




<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/style.css" />
<script src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@0/config.js"></script>



<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/forum_main_post.css" />
<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/forum_main.css" />
<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/public_forum_all.css" />

<!--code-->
<link rel="stylesheet" href="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/CSS_SofaSofa@1/foundation.css" />


  <style>
  .note-editor pre {
    background-color: #F8F8F8 !important;
  }

    .dropdownqr {
      position: relative;
      display: inline-block;
      z-index: 100;
  }

  .dropdownqr-content {
      display: none;
      position: absolute;
      background-color: #f9f9f9;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  }

  .dropdownqr:hover .dropdownqr-content {
      display: block;
  }

  .desc {
      padding: 15px;
      text-align: center;
      font-size: 14px;
  }
  .second_reply_div{
  border-top: 0.1px solid #e5e5e5;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  font-size: 0.8rem;
}
  </style>



<style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
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
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 1em 0em; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
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
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?rev=2.6.1') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?rev=2.6.1') format('woff'), url('http://sofasofa.io/library/math/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?rev=2.6.1') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style></head>


<body><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"><br /></div></div><div id="MathJax_Message" style="display: none;"></div>


<!-- jQuery -->
<script type="text/javascript" src="http://sofasofa.io/library/jquery/jquery.form.min.js"></script>


<style>
.navbar{
	background-color: #FFFFFF;
	color: #666666;
	border-radius: 0px !important;
	position: absolute;
	width: 100%;
	border-bottom: solid 0.5px #EAEEEF;
}
.nav-item {
  margin-left: 0px !important;
}
.nav-link{
	color: #666666 !important;
  padding: 5px 10px;
	transition: all 0.3s ease 0s;
}
.nav-link:hover{
	background-color: #F3F3F3;
}
.hd-txt:link{
	text-decoration: none !important;
	font-size: 21px;
}
.mob-txt:link{
	text-decoration: none !important;
	font-size: 18px;
}
</style>


<nav class="navbar navbar-light bg-faded">

	<div class="container p-x-0">

		<div class="navbar-brand">
			<h4 class="hidden-sm-down" style="color:#41C48E">
				<a href="http://sofasofa.io/index.php" style="color:#41C48E;text-decoration: none; font-size: 20px">  
        <img src="assets/images/green_sofa.png" class="hidden-sm-down" title="SofaSofa-数据科学社区" alt="SofaSofa-数据科学社区" style="height:42px;margin-top:-5px;" />
        </a>
           
				<a href="http://sofasofa.io/forum_main.php" class="hd-txt" style="color:#00B068"><b>问答</b></a>    
        <a href="http://sofasofa.io/interviews.php" class="hd-txt" style="color: #10a9e8"><b>面试</b><span style="font-size: 8px; color: red"><i class="fa fa-circle" aria-hidden="true"></i></span></a>    
        <a href="http://sofasofa.io/competitions.php" class="hd-txt" style="color: #F46A41"><b>竞赛</b></a>    		<a href="http://sofasofa.io/tutorials.php" class="hd-txt" style="color:#bab084"><b>教程</b></a>    <a href="http://sofasofa.io/others.php" class="hd-txt" style="color:#2b9da5"><b>板凳</b></a>    <a href="http://sofasofa.io/handbooks.php" style="color:#F37726" alt="Sofa手册" title="Sofa手册"><i class="fa fa-book" aria-hidden="true"></i></a>		<!--<a href="interviews.php" style="color:#bab084;text-decoration: none; font-size: 22px"><img src="assets/images/zongzijie.png" style="width: 2.6rem" title="吃粽子咯"></a>-->

      </h4>

      <h4 class="hidden-md-up" style="color:#01B169"><a class="btn_nav_site_mobile" href="javascript:void(0);" style="text-decoration:none;color:#01B169"><i class="fa fa-bars" aria-hidden="true"></i>  <b>So<span style="color:#0E6A44">fa</span>Sofa.<span style="color: #10a9e8;">io</span></b></a>
      </h4>
		</div>
		<div>

			<ul class="nav navbar-nav pull-right">
									<li class="nav-item">
						<a class="nav-link signup_btn" href="javascript:void(0);" role="student">
							<span class="hidden-md-up"><i class="fa fa-user-plus"></i></span>
							<span class="hidden-sm-down">注册</span>
						</a>
					</li>
					<li class="nav-item">
						<a class="nav-link login_btn" href="javascript:void(0);" role="student">
							<span class="hidden-md-up"><i class="fa fa-sign-in"></i></span>
							<span class="hidden-sm-down">登录</span>
						</a>
					</li>
							</ul>

			<!-- 搜索 -->
	    <form id="form_navbar_search" class="hidden-sm-down">
			  <div class="input-group" style="width:10rem; float:right;">
		      <input type="text" class="form-control" id="input_navbar_search" placeholder="搜索" />
		      <span class="input-group-btn">
		        <button class="btn btn-secondary" id="btn_navbar_search" type="submit">
							<i class="fa fa-search"></i>
						</button>
		      </span>
	      </div>
	    </form>
	  </div>
	</div>
</nav>

<script type="text/javascript" src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@1/mob.js" <="" script="">

&lt;script&gt;
	$(document).ready(function(){

		$('#logout').click(function(){
			$('#logoutModal').modal();
			$(document).on('click', '#confirm_logout', function(){
				$('#logoutModal').modal('hide');

				$.ajax({
					type: "get",
					url: "user_exe.php?action=user_signout",
					success: function(responseText, statusText) {
						localStorage.clear();
						location.reload(true);
					}
				});
			});
		});

		// 搜索框的变化
		$('#input_navbar_search').focusin(function() {
			$(this)
					.attr('placeholder', '搜索感兴趣的问题或内容')
				.parent()
					.animate({width: '17rem'})
				.find('.btn')
					.removeClass('btn-secondary')
					.addClass('btn-success');
		});
		$('#input_navbar_search').blur(function() {
			$(this)
					.attr('placeholder', '搜索')
				.parent()
				.animate({width: '10rem'})
				.find('.btn')
					.addClass('btn-secondary')
					.removeClass('btn-success');
		});


    // 搜索
    var options_search = {
  		url: 'public_forum_exe.php?action=main_reply',
  		type: 'get',
  		beforeSubmit: function(formData, jqForm, options) {
  			var term = encodeURIComponent($('#input_navbar_search').val());
        if (term == '') {
          bootbox.alert('请输入关键字');
          return false;
        } else {
          window.location = 'forum_main_search.php?search=' + term;
    			return true;
        }
  		},
  		success: function(responseText, statusText){
  			return true;
  		}
  	};
  	$('#form_navbar_search').ajaxForm(options_search);


	})
 </script><div class="modal fade" id="logoutModal"> <div class="modal-dialog" role="document">
		<div class="modal-content">	<div class="modal-header">		<button type="button" class="close" data-dismiss="modal" aria-label="Close">	  <span aria-hidden="true">×</span>
				  <span class="sr-only">Close</span>		</button>
			<span style="font-size:20px" class="modal-title"><i class="fa fa-question-circle-o" aria-hidden="true"></i>  确认</span>     </div>   <div class="modal-body">
				<p>您确认要退出登录么？</p>
		    </div>    <div class="modal-footer">
				<button type="button" class="btn btn-danger" id="confirm_logout">登出</button>
				<button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>    </div> 	</div>   </div> </div> <div class="modal fade" id="site_nav_Modal"> <div class="modal-dialog" role="document">	<div class="modal-content">  	<div class="modal-header">		<button type="button" class="close" data-dismiss="modal" aria-label="Close">
				  <span aria-hidden="true">×</span>
				  <span class="sr-only">Close</span>
				</button>
			<span style="font-size:20px" class="modal-title"><i class="fa fa-question-circle-o" aria-hidden="true"></i>  确认</span>
		    </div>
		    <div class="modal-body">
				<p>您确认要退出登录么？</p>
		    </div>
		    <div class="modal-footer">			<button type="button" class="btn btn-danger" id="confirm_logout">登出</button>
				<button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>    </div>	</div>  </div></div><div class="modal fade" id="nav_site_mobile"> <div class="modal-dialog" role="document">
        <div class="modal-content">	<div class="modal-body">     <div style="width: 50%; display: block; margin-left:auto; margin-right: auto;">
                	<span style="font-size: 13px">请带我飞去:</span><br /><br />
                	<a href="index.php" class="mob-txt" style="color:#00B068;"><b>问答</b></a>
       				<br /><br />
        			<a href="competitions.php" class="mob-txt" style="color:#20BEFF;"><b>数据竞赛</b></a>
        			<br /><br />
        			<a href="tutorials.php" class="mob-txt" style="color:#F46A41;"><b>教程</b></a>
        			<br /><br /> 			<a href="interviews.php" class="mob-txt" style="color:#bab084"><b>面试</b></a>			<br />   </div></div><div class="modal-footer">          <button type="button" class="btn btn-theme" data-dismiss="modal"><span style="font-size: 13px">回去啦( ͡° ͜ʖ ͡°)</span></button>
            </div></div></div></div>




<!--begin 注册-->
    <form id="form_signup" enctype="multipart/form-data" role="form">
    <div class="modal fade" id="myModal_signup" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	    <div class="modal-dialog" role="document">
			<div class="modal-content">
			    <div class="modal-header">
				    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
					    <span aria-hidden="true">×</span>
					    <span class="sr-only">Close</span>
				    </button>
				    <span style="font-size:20px" class="modal-title" id="myModalLabel"><i class="fa fa-user-plus" aria-hidden="true"></i> 欢迎注册SofaSofa！</span>
			    </div>


			    <div class="modal-body">
    <div class="form-group">
      <!--<label for="exampleInputName2">邮箱</label>-->
      <input type="email" class="form-control" name="email" id="signup_email" placeholder="请输入您的邮箱" required="" />
    </div>

		<div class="form-group">
      <!--<label for="exampleInputName2">用户名</label>-->
      <input class="form-control" name="username" id="signup_username" placeholder="请输入您的用户名" required="" />
    </div>


    <div class="form-group">
      <!--<label for="exampleInputName2">密码</label>-->
      <input type="password" class="form-control" name="password" id="password" placeholder="请输入密码" required="" />
    </div>

    <div class="form-group">
      <!--<label for="exampleInputName2">确认密码</label>-->
      <input type="password" class="form-control" id="password_check" placeholder="请再次输入您的密码" required="" />
    </div>

    <div class="form-group">
      <span>请口算并用汉字输入答案('一二三四五六七八九')</span>
      <input type="text" class="form-control" id="verify" name="verify" placeholder="向量(1, -4)的L1范数等于几？" required="" />
    </div>

    注册过啦？请直接<a class="nav-link login_btn" id="new_login_btn" href="javascript:void(0);" role="student"> 登录 </a>吧！

    <hr />

    <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
    <button type="button" class="btn btn-primary" id="confirm_sumbit_signup">
      <i class="fa fa-check-square-o"></i> 确认
    </button>
    </div>
    </div>
    </div>
    </div>
    </form>
<!--end 注册-->



<script type="text/javascript" src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@1/dlzhmm.js"> </script><!--begin 登录-->
	<form id="form_login" enctype="multipart/form-data" role="form">
	<div class="modal fade" id="myModal_login" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	    <div class="modal-dialog" role="document">
			<div class="modal-content">
			    <div class="modal-header">
				    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
					    <span aria-hidden="true">×</span>
					    <span class="sr-only">Close</span>
				    </button><span style="font-size:20px" class="modal-title" id="myModalLabel"><i class="fa fa-hand-spock-o" aria-hidden="true"></i> 欢迎回来</span>
			    </div><div class="modal-body"><div class="form-group">
						<!--<label for='exampleInputName2'>邮箱</label>-->
						<input type="email" class="form-control" name="email" placeholder="请输入您的邮箱" required="" />
				    </div><div class="form-group">			<!--<label for='exampleInputName2'>密码</label>-->
						<input type="password" class="form-control" name="password" placeholder="请输入密码" required="" />
				    </div>
						还没有注册过？点击<a href="javascript:void(0);" id="new_signup_btn">注册</a>。<br />
						忘记密码？<a href="javascript: void(0);" id="recover_password"><i class="fa fa-unlock"></i> 找回密码</a>。
			    </div>
			    <div class="modal-footer">
				    <button type="button" class="btn btn-secondary" data-dismiss="modal">取消</button>
				    <button type="submit" class="btn btn-primary">确认</button>
			    </div>
			</div>
	    </div>
	</div>
	</form>
<!--end 登录-->
<!-- 找回密码 -->
<div class="modal fade" id="myModal_recover_password" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
		<div class="modal-content">
		    <div class="modal-header">
			    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
				    <span aria-hidden="true">×</span><span class="sr-only">Close</span>
			    </button>
			    <span style="font-size:20px" class="modal-title" id="myModalLabel">找回密码</span>
		    </div>
		    <div class="modal-body">
				<div class="row m-a-0">
					<div class="col-md-8 col-md-offset-2">
						请输入注册邮箱:（重置密码的邮件可能会在您的垃圾邮箱中）<br />
						<input type="text" class="form-control" id="recover_password_email" />
					</div>			</div>    </div>    <div class="modal-footer">
			    <button type="button" class="btn btn-secondary recover_password_btn" data-dismiss="modal">取消</button>
			    <button type="button" class="btn btn-primary recover_password_btn" id="confirm_recover_password">确认</button>
				<i class="fa fa-spinner fa-spin" id="recover_password_busy_icon" hidden=""></i>
		    </div>
		</div>
  </div>
</div>




<script>
$(document).ready(function(){

  // 先检查是否在localstorage中有用户信息
  // 重新登陆
    if (localStorage["user"]) {
    $.ajax({
      type: 'POST',
      url: 'user_exe.php?action=user_signin_auto',
      data: {user: localStorage["user"]},
      success: function (response) {
        location.reload(true);
      }
    });
  }
  
	

	$(document).on('click', '.login_btn', function(){
		$('#myModal_login').modal();
	})

	$(document).on('click', '.signup_btn', function(){
		var role = $(this).attr('role');
		if(role == 'teacher'){
			$('#signup_btn_teacher').trigger('click');
		} else {
			$('#signup_btn_student').trigger('click');
		}
		$('#myModal_signup').modal();
	})

	$(document).on('click', '#new_signup_btn', function(){
		$('#myModal_login').modal('hide');
		$('#myModal_signup').modal();
	})

	$(document).on('click', '#new_login_btn', function(){
		$('#myModal_signup').modal('hide');
		$('#myModal_login').modal();
	})


	var options_login = {
		url: 'user_exe.php?action=user_signin',
		type: 'post',
			beforeSubmit: function(formData, jqForm, options) {
		    return true;
		},
		success: function(response){
			if(response == 'noexist'){
				message_alert('error', '此邮箱未注册，请注册后登陆。', 'index.php');
			} else if (response == 'wrong'){
				message_alert('error', '密码错误，请重新输入。', '');
			} else { // 成功登陆
				localStorage.setItem('user', response);
				window.location.reload();
			}
			return true;
		}
	};
	$('#form_login').ajaxForm(options_login);



	$(document).ready(function() {
  $(document).on('click', '#confirm_sumbit_signup', function(){

		if($('#password').val() != $('#password_check').val()){
			bootbox.alert('两次输入的密码不匹配，请重新输入。');
		} else if($('#verify').val() != "五") {
			bootbox.alert('您的验证码错误，请重试。');
		} else {
			$.ajax({
				method: 'POST',
				url: 'user_exe.php?action=user_signup',
				data: {name: $('#signup_name').val(), username: $('#signup_username').val(), email: $('#signup_email').val(), school: $('#signup_school').val(), password: $('#password').val()},

				success: function(responseText){

          			// alert(responseText);
					if(responseText == 'exist'){
						bootbox.alert('该邮箱已注册，请直接登录。', function(){
							$('#myModal_login').modal('show');
						});
					}
					else if (responseText.substring(0, 5) == 'Error') {
						message_alert('error', responseText, '');
					}
					else {
						bootbox.alert('您已成功注册，请登录', function(){
							$('#myModal_login').modal('show');
						});
						$('#myModal_signup').modal('hide');
					}
				}
			});
		}
	});
});

$(document).on('click', '#recover_password', function(){
	$('#myModal_recover_password').modal();
	$('#myModal_login').modal('hide');
});

$(document).on('click', '#confirm_recover_password', function(){
	var email = $('#recover_password_email').val();
	$('#recover_password_busy_icon').removeAttr('hidden');
	$('.recover_password_btn').attr('disabled', '');
	$.ajax({
		method: 'POST',
		url: 'user_exe.php?action=recover_password',
		data: {email: email},
		success: function(response){
      // alert(response);
			$('#recover_password_busy_icon').attr('hidden', '');
			$('.recover_password_btn').removeAttr('disabled');
			//alert(responseText);
			if(responseText == 'noexist'){
				message_alert('error', '您输入的账号/密码不存在，请重新输入。', '');
			} else {
				message_alert('success', '重置密码邮件已发送，请前往您的邮箱查收', 'forum_main.php');
			}
		}
	});
});


})
</script>




<!---------------------------------------------------------------------------->
<!-- Google Analytic -->
<!--<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-92762347-1', 'auto');
  ga('send', 'pageview');

</script>-->
<!---------------------------------------------------------------------------->


<!-- 第二层的顶栏 -->

<div class="container-fluid">
  <div class="row" id="navbar2">

    <div class="container p-x-0">

	
			<a href="forum_main.php" class="navbar2_btn" id="header2_all">
				<span style="color:#00B068"><i class="fa fa-list-ol"></i></span> <span class="hidden-sm-down" style="color:#5e5e5e">全部问题</span><span class="hidden-md-up" style="color:#5e5e5e">问题</span></a>
			<a href="forum_main_popular.php" class="navbar2_btn hidden-sm-down" id="header2_popular">
				<span style="color:#00B068"><i class="fa fa-fire"></i></span> <span style="color:#5e5e5e">热门</span></a>
			<a href="forum_noanswers.php" class="navbar2_btn hidden-sm-down" id="header2_noanswer">
				<span style="color:#00B068"><i class="fa fa-question-circle"></i></span> <span style="color:#5e5e5e">未解答</span></a>
			<a href="forum_main_tags.php" class="navbar2_btn" id="header2_tags">
				<span style="color:#00B068"><i class="fa fa-tags"></i></span> <span class="hidden-sm-down" style="color:#5e5e5e">所有标签</span><span class="hidden-md-up" style="color:#5e5e5e">标签</span></a>
			<a href="forum_main_favourite.php" class="navbar2_btn" id="header2_favourite" data-toggle="modal" data-target="#myModal_login">
				<span style="color:#00B068"><i class="fa fa-star"></i></span> <span class="hidden-sm-down" style="color:#5e5e5e">收藏</span><span class="hidden-md-up" style="color:#5e5e5e">收藏</span></a>
			<a href="forum_main.php#new_post_div" class="navbar2_btn hidden-sm-down" id="header2_new_post" data-toggle="modal" data-target="#myModal_login">
				<span style="color:#00B068"><i class="fa fa-plus-circle"></i></span> <span style="color:#5e5e5e">我要提问</span></a>
    </div>
  </div>
</div>


<div class="row m-x-0 m-t-lg p-t-lg" style="background-color: #f7fffb;">
  <div class="container p-y">
  <div class="col-md-9 p-l-0">
    <h1 style="font-size:24px">K-means怎么选K?</h1>

    <i class="fa fa-tags green"></i>  
            <a href="index.php?f=1000026" class="tag_link m-r" target="_blank">
              统计/机器学习
            </a>
            <a href="index.php?f=1000033" class="tag_link m-r" target="_blank">
              无监督学习
            </a>
            <a href="index.php?f=1000044" class="tag_link m-r" target="_blank">
              开放问题
            </a><span style="color:#009966; font-size: 12px">   浏览次数：32886 </span>      <span class="dropdownqr" style="color:#009966; font-size: 18px"><i class="fa fa-qrcode" aria-hidden="true"></i> <span style="font-size: 12px">分享</span>
  <div class="dropdownqr-content">
    <img src="assets/images/qrcode/qrcode_1000282.jpg" alt="二维码" />
    <div class="desc">手机扫描二维码</div>
  </div>
    </span>
    </div>
    <div class="col-md-3">
      <div>
         
        <a class="btn btn-info" href="http://sofasofa.io/data_science_case_study.php"><b>案例分析</b>面试常见题？</a>   </div>
    </div>
  </div>
</div>

<div class="container p-t" id="main_row">

  <div class="col-md-9 p-l-0">

    <div class="row m-x-0 p-x-0 m-b post_div">
			<div class="row m-x-0">

				<div class="col-md-1 col-xs-2 p-x-0 text-center">

          <div class="widget-vote">

            <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1000282" data-wenk="该问题有价值，同问！">
              <i class="fa fa-sort-asc"></i>
            </button>

            <div>16</div>

            <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1000282" data-wenk="这是个嘛问题啊！">
              <i class="fa fa-sort-desc"></i>
            </button>

          </div>


					<div style="margin-top:0.5rem; text-align:left;">
						<a href="#" class="btn_favourite btn btn-secondary btn-sm text-center wenk--right" style="width: 40px;" data-wenk="收藏" method="add" postid="1000282">
							<i class="fa fa-star-o yellow"></i><br />
              <span id="favourite_number">43</span>
						</a>
					</div>

				</div>

				<div class="col-md-11 col-xs-10"><p>我们都知道K-means的主要缺点就是在做聚类前，必须要先确定K，也就是样本里聚类的个数。一般有哪些方法呢？我知道手肘法，但是也没有明白这个手肘到底怎么用。</p><div style="max-width: 650px; float:left;"></div></div>
			</div>
		<div class="row">
			<div class="col-md-1 col-xs-2"> </div>
			<div class="col-md-5 col-xs-4">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1000282" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
			</div>
			<div class="col-md-6 col-xs-6">

			<div class="author_div">
				<div style="float:right; padding-bottom: 100px;">
					<p class="m-t-sm m-l">
						<img src="assets/images/avatars/default/1001065.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
						<a class="darkgray" href="user_profile.php?id=1001065">
							道画师
						</a>  
						<span class="gray"><i class="fa fa-clock-o"></i> 2017-03-03 11:50</span>
					</p>
				</div>
			</div>
			</div>
		</div><div align="center"><hr style="margin-top:30px;" /><br /><h5 class="m-t" style="color:#267757;"> <i class="fa fa-bicycle" aria-hidden="true" style="color:#267757;" title="老司机有答案了"></i>  7个回答 </h5></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1000299" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>49</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1000299" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p><span style="font-size: 14px;">对于K-means中K的选择，通常有四种方法。</span></p><ul><li><span style="font-size: 14px;">按需选择</span></li><li><span style="font-size: 14px;">观察法</span></li><li><span style="font-size: 14px;">手肘法</span></li><li><span style="font-size: 14px;">Gap Statistics方法</span></li></ul><p><span style="font-size: 14px; font-weight: bold;">一、按需选择</span></p><p><span style="font-size: 14px;">简单地说就是按照建模的需求和目的来选择聚类的个数。比如说，一个游戏公司想把所有玩家做聚类分析，分成顶级、高级、中级、菜鸟四类，那么K=4；如果房地产公司想把当地的商品房分成高中低三档，那么K=3。按需选择虽然合理，但是未必能保证在做K-Means时能够得到清晰的分界线。</span></p><p><span style="font-size: 14px; font-weight: bold;">二、观察法</span></p><p><span style="font-size: 14px;">就是用肉眼看，看这些点大概聚成几堆。这个方法虽然简单，但是同时也模棱两可。</span></p><p><img src="data:image/png;base64,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" data-filename="dd1.png" style="width: 338.475px; height: 230px;" /><img src="data:image/png;base64,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" data-filename="dd2.png" style="width: 336.636px; height: 228.75px;" /></p><p><img src="data:image/png;base64,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" data-filename="dd3.png" style="width: 338.475px; height: 230px;" /><img src="data:image/png;base64,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" data-filename="dd4.png" style="width: 337.004px; height: 229px;" /><span style="font-size: 1rem;"><br /></span></p><p><span style="font-size: 14px;">左上角是原始点。右上角分成了两类。左下角是三类，左下角是四类。至于K到底是选3还是选4，可能每个人都有不同的选择。</span></p><p><span style="font-size: 1rem;"><span style="font-size: 14px;">观察法的另一个缺陷就是：原始数据维数要低，一般是两维（平面散点）或者三维（立体散点），否则人类肉眼则无法观察。对于高维数据，我们通常利用PCA降维，然后再进行肉眼观察。</span><br /></span></p><p><span style="font-size: 1rem;"><span style="font-weight: bold; font-size: 14px;">三、手肘法</span></span></p><p><span style="font-size: 14px;">手肘法本质上也是一种间接的观察法。这里需要一点K-Means的背景知识。当K-Means算法完成后，我们将得到K个聚类的中心点<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;M&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" role="math" style="width: 1.61em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.313em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1001.31em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-2"><span class="msubsup" id="MathJax-Span-3"><span style="display: inline-block; position: relative; width: 1.313em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1001.07em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-4" style="font-family: MathJax_Math-italic;">M<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.955em;"><span class="mi" id="MathJax-Span-5" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>M</mi><mi>i</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-1">M_i</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-2-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x22EF;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-6" role="math" style="width: 7.682em; display: inline-block;"><span style="display: inline-block; position: relative; width: 6.372em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.372em, 1006.37em, 2.562em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-7"><span class="mi" id="MathJax-Span-8" style="font-family: MathJax_Math-italic;">i</span><span class="mo" id="MathJax-Span-9" style="font-family: MathJax_Main; padding-left: 0.301em;">=</span><span class="mn" id="MathJax-Span-10" style="font-family: MathJax_Main; padding-left: 0.301em;">1</span><span class="mo" id="MathJax-Span-11" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-12" style="font-family: MathJax_Main; padding-left: 0.182em;">2</span><span class="mo" id="MathJax-Span-13" style="font-family: MathJax_Main;">,</span><span class="mo" id="MathJax-Span-14" style="font-family: MathJax_Main; padding-left: 0.182em;">⋯</span><span class="mo" id="MathJax-Span-15" style="font-family: MathJax_Main; padding-left: 0.182em;">,</span><span class="mi" id="MathJax-Span-16" style="font-family: MathJax_Math-italic; padding-left: 0.182em;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.218em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>⋯</mo><mo>,</mo><mi>K</mi></math></span></span><script type="math/tex" id="MathJax-Element-2">i=1,2,\cdots,K</script>。以及每个原始点所对应的聚类<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-3-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;C&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-17" role="math" style="width: 1.253em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.015em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1001.01em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-18"><span class="msubsup" id="MathJax-Span-19"><span style="display: inline-block; position: relative; width: 1.015em; height: 0px;"><span style="position: absolute; clip: rect(3.098em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-20" style="font-family: MathJax_Math-italic;">C<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.717em;"><span class="mi" id="MathJax-Span-21" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>C</mi><mi>i</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-3">C_i</script>,<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-4-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mo&gt;&amp;#x22EF;&lt;/mo&gt;&lt;mo&gt;,&lt;/mo&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-22" role="math" style="width: 7.682em; display: inline-block;"><span style="display: inline-block; position: relative; width: 6.372em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.372em, 1006.37em, 2.562em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-23"><span class="mi" id="MathJax-Span-24" style="font-family: MathJax_Math-italic;">i</span><span class="mo" id="MathJax-Span-25" style="font-family: MathJax_Main; padding-left: 0.301em;">=</span><span class="mn" id="MathJax-Span-26" style="font-family: MathJax_Main; padding-left: 0.301em;">1</span><span class="mo" id="MathJax-Span-27" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-28" style="font-family: MathJax_Main; padding-left: 0.182em;">2</span><span class="mo" id="MathJax-Span-29" style="font-family: MathJax_Main;">,</span><span class="mo" id="MathJax-Span-30" style="font-family: MathJax_Main; padding-left: 0.182em;">⋯</span><span class="mo" id="MathJax-Span-31" style="font-family: MathJax_Main; padding-left: 0.182em;">,</span><span class="mi" id="MathJax-Span-32" style="font-family: MathJax_Math-italic; padding-left: 0.182em;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.218em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi><mo>=</mo><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>⋯</mo><mo>,</mo><mi>K</mi></math></span></span><script type="math/tex" id="MathJax-Element-4">i=1,2,\cdots,K</script>。我们通常采用所有样本点到它所在的聚类的中心点的距离的和作为模型的度量，记为<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-5-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-33" role="math" style="width: 1.908em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1001.55em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-34"><span class="msubsup" id="MathJax-Span-35"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-36" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-37" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-5">D_K</script>。</span></p><p><span style="font-size: 14px;"><span class="MathJax_Preview" style="color: inherit;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-6-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;munderover&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mn&gt;1&lt;/mn&gt;&lt;/mrow&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/munderover&gt;&lt;munder&gt;&lt;mo&gt;&amp;#x2211;&lt;/mo&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;X&lt;/mi&gt;&lt;mo&gt;&amp;#x2208;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;C&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;/mrow&gt;&lt;/munder&gt;&lt;mo&gt;&amp;#x2225;&lt;/mo&gt;&lt;mi&gt;X&lt;/mi&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;M&lt;/mi&gt;&lt;mi&gt;i&lt;/mi&gt;&lt;/msub&gt;&lt;mo fence=&quot;false&quot; stretchy=&quot;false&quot;&gt;&amp;#x2225;&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-38" role="math" style="width: 13.098em; display: inline-block;"><span style="display: inline-block; position: relative; width: 10.896em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(0.301em, 1010.78em, 3.693em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-39"><span class="msubsup" id="MathJax-Span-40"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-41" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-42" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-43" style="font-family: MathJax_Main; padding-left: 0.301em;">=</span><span class="munderover" id="MathJax-Span-44" style="padding-left: 0.301em;"><span style="display: inline-block; position: relative; width: 1.432em; height: 0px;"><span style="position: absolute; clip: rect(2.86em, 1001.37em, 4.646em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mo" id="MathJax-Span-45" style="font-family: MathJax_Size2; vertical-align: 0.003em;">∑</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.07em, 4.289em, -999.997em); top: -2.914em; left: 0.122em;"><span class="texatom" id="MathJax-Span-46"><span class="mrow" id="MathJax-Span-47"><span class="mi" id="MathJax-Span-48" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mo" id="MathJax-Span-49" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-50" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; clip: rect(3.217em, 1000.66em, 4.17em, -999.997em); top: -5.116em; left: 0.42em;"><span class="mi" id="MathJax-Span-51" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="munderover" id="MathJax-Span-52" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.789em; height: 0px;"><span style="position: absolute; clip: rect(2.86em, 1001.37em, 4.646em, -999.997em); top: -3.985em; left: 0.182em;"><span class="mo" id="MathJax-Span-53" style="font-family: MathJax_Size2; vertical-align: 0.003em;">∑</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.79em, 4.408em, -999.997em); top: -2.854em; left: 0.003em;"><span class="texatom" id="MathJax-Span-54"><span class="mrow" id="MathJax-Span-55"><span class="mi" id="MathJax-Span-56" style="font-size: 70.7%; font-family: MathJax_Math-italic;">X<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span class="mo" id="MathJax-Span-57" style="font-size: 70.7%; font-family: MathJax_Main;">∈</span><span class="msubsup" id="MathJax-Span-58"><span style="display: inline-block; position: relative; width: 0.717em; height: 0px;"><span style="position: absolute; clip: rect(3.336em, 1000.54em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-59" style="font-size: 70.7%; font-family: MathJax_Math-italic;">C<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.866em; left: 0.479em;"><span class="mi" id="MathJax-Span-60" style="font-size: 50%; font-family: MathJax_Math-italic;">i</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-61" style="font-family: MathJax_Main; padding-left: 0.182em;">∥</span><span class="mi" id="MathJax-Span-62" style="font-family: MathJax_Math-italic;">X<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span class="mo" id="MathJax-Span-63" style="font-family: MathJax_Main; padding-left: 0.241em;">−</span><span class="msubsup" id="MathJax-Span-64" style="padding-left: 0.241em;"><span style="display: inline-block; position: relative; width: 1.313em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1001.07em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-65" style="font-family: MathJax_Math-italic;">M<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.955em;"><span class="mi" id="MathJax-Span-66" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-67" style="font-family: MathJax_Main;">∥</span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.639em; border-left: 0px solid; width: 0px; height: 3.789em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>D</mi><mi>K</mi></msub><mo>=</mo><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mi>K</mi></munderover><munder><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>X</mi><mo>∈</mo><msub><mi>C</mi><mi>i</mi></msub></mrow></munder><mo>∥</mo><mi>X</mi><mo>−</mo><msub><mi>M</mi><mi>i</mi></msub><mo fence="false" stretchy="false">∥</mo></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-6">D_K=\sum_{i=1}^K\sum_{X\in C_i}\|X-M_i\|</script></span></p><p><span style="font-size: 14px;">这里距离可以采用欧式距离。</span></p><p><span style="font-size: 14px;">对于不同的K，最后我们会得到不同的中心点和聚类，所有会有不同的度量。</span></p><p><span style="font-size: 14px;">我们把上面的例子用不同的K去计算，会得到不同的结果。把K作为横坐标，<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-7-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-68" role="math" style="width: 1.908em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1001.55em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-69"><span class="msubsup" id="MathJax-Span-70"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-71" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-72" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-7">D_K</script>作为纵坐标，我们可以得到下面的折线。</span></p><p><img src="data:image/png;base64,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" data-filename="download%20(15) (1).png" style="width: 469.869px; height: 336.354px;" /><br /></p><p><span style="font-size: 14px;">很显然K越大，距离和越小。但是我们注意到K=3是一个拐点，就像是我们的肘部一样，K=1到3下降很快，K=3之后趋于平稳。</span><span style="font-weight: bold; font-size: 14px;">手肘法认为这个拐点就是最佳的K。</span></p><p><span style="font-size: 14px;">手肘法是一个经验方法，而且肉眼观察也因人而异，特别是遇到模棱两可的时候。相比于直接观察法，手肘法的一个优点是，适用于高维的样本数据。有时候人们也会把手肘法用于不同的度量上，如组内方差组间方差比。</span></p><p><span style="font-size: 14px; font-weight: bold;">四、Gap Statistic方法</span></p><p><span style="font-size: 14px;">这个方法是源自斯坦福几个machine learning大牛的paper </span><a href="http://www.stanford.edu/~hastie/Papers/gap.pdf" target="_blank"><span style="font-size: 14px;">Estimating the number of clusters in a data set via the gap statistic</span></a><span style="font-size: 14px;"> 。</span></p><p><span style="font-size: 14px;">这里我们要继续使用上面的<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-8-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-73" role="math" style="width: 1.908em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1001.55em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-74"><span class="msubsup" id="MathJax-Span-75"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-76" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-77" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-8">D_K</script>。Gap Statistic的定义为</span></p><p><span style="font-size: 14px;"><span class="MathJax_Preview" style="color: inherit;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-9-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;mi&gt;G&lt;/mi&gt;&lt;mi&gt;a&lt;/mi&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;mtext&gt;E&lt;/mtext&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;mo&gt;&amp;#x2212;&lt;/mo&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-78" role="math" style="width: 15.658em; display: inline-block;"><span style="display: inline-block; position: relative; width: 13.039em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1013.04em, 2.622em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-79"><span class="mi" id="MathJax-Span-80" style="font-family: MathJax_Math-italic;">G</span><span class="mi" id="MathJax-Span-81" style="font-family: MathJax_Math-italic;">a</span><span class="mi" id="MathJax-Span-82" style="font-family: MathJax_Math-italic;">p</span><span class="mo" id="MathJax-Span-83" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-84" style="font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="mo" id="MathJax-Span-85" style="font-family: MathJax_Main;">)</span><span class="mo" id="MathJax-Span-86" style="font-family: MathJax_Main; padding-left: 0.301em;">=</span><span class="mtext" id="MathJax-Span-87" style="font-family: MathJax_Main; padding-left: 0.301em;">E</span><span class="mo" id="MathJax-Span-88" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-89" style="font-family: MathJax_Main;">log</span><span class="mo" id="MathJax-Span-90"></span><span class="msubsup" id="MathJax-Span-91" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.253em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-92" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-93" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-94" style="font-family: MathJax_Main;">)</span><span class="mo" id="MathJax-Span-95" style="font-family: MathJax_Main; padding-left: 0.241em;">−</span><span class="mi" id="MathJax-Span-96" style="font-family: MathJax_Main; padding-left: 0.241em;">log</span><span class="mo" id="MathJax-Span-97"></span><span class="msubsup" id="MathJax-Span-98" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.253em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-99" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-100" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.354em; border-left: 0px solid; width: 0px; height: 1.361em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>G</mi><mi>a</mi><mi>p</mi><mo stretchy="false">(</mo><mi>K</mi><mo stretchy="false">)</mo><mo>=</mo><mtext>E</mtext><mo stretchy="false">(</mo><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>k</mi></msub><mo stretchy="false">)</mo><mo>−</mo><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>k</mi></msub></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-9">Gap(K)=\text{E}(\log D_k)-\log D_k</script></span></p><p><span style="font-size: 14px;">这里<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-10-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mtext&gt;E&lt;/mtext&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-101" role="math" style="width: 5.003em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.17em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1004.05em, 2.622em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-102"><span class="mtext" id="MathJax-Span-103" style="font-family: MathJax_Main;">E</span><span class="mo" id="MathJax-Span-104" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-105" style="font-family: MathJax_Main;">log</span><span class="mo" id="MathJax-Span-106"></span><span class="msubsup" id="MathJax-Span-107" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.253em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-108" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-109" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-110" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.354em; border-left: 0px solid; width: 0px; height: 1.361em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>E</mtext><mo stretchy="false">(</mo><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>k</mi></msub><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-10">\text{E}(\log D_k)</script>指的是<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-11-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;k&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-111" role="math" style="width: 3.336em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.741em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1002.74em, 2.562em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-112"><span class="mi" id="MathJax-Span-113" style="font-family: MathJax_Main;">log</span><span class="mo" id="MathJax-Span-114"></span><span class="msubsup" id="MathJax-Span-115" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.253em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-116" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-117" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.218em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>k</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-11">\log D_k</script>的期望。这个数值通常通过蒙特卡洛模拟产生，我们在样本里所在的矩形区域中（高维的话就是立方体区域）按照均匀分布随机地产生和原始样本数一样多的随机样本，并对这个随机样本做K-Means，从而得到一个<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-12-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-118" role="math" style="width: 1.908em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1001.55em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-119"><span class="msubsup" id="MathJax-Span-120"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-121" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-122" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>D</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-12">D_K</script>。如此往复多次，通常20次，我们可以得到20个<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-13-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-123" role="math" style="width: 3.693em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.039em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1003.04em, 2.562em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-124"><span class="mi" id="MathJax-Span-125" style="font-family: MathJax_Main;">log</span><span class="mo" id="MathJax-Span-126"></span><span class="msubsup" id="MathJax-Span-127" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-128" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-129" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.218em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-13">\log D_K</script>。对这20个数值求平均值，就得到了<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-14-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mtext&gt;E&lt;/mtext&gt;&lt;mo stretchy=&quot;false&quot;&gt;(&lt;/mo&gt;&lt;mi&gt;log&lt;/mi&gt;&lt;mo&gt;&amp;#x2061;&lt;/mo&gt;&lt;msub&gt;&lt;mi&gt;D&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;mo stretchy=&quot;false&quot;&gt;)&lt;/mo&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-130" role="math" style="width: 5.36em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.467em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1004.35em, 2.622em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-131"><span class="mtext" id="MathJax-Span-132" style="font-family: MathJax_Main;">E</span><span class="mo" id="MathJax-Span-133" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-134" style="font-family: MathJax_Main;">log</span><span class="mo" id="MathJax-Span-135"></span><span class="msubsup" id="MathJax-Span-136" style="padding-left: 0.182em;"><span style="display: inline-block; position: relative; width: 1.551em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1000.78em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-137" style="font-family: MathJax_Math-italic;">D</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.836em;"><span class="mi" id="MathJax-Span-138" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-139" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.354em; border-left: 0px solid; width: 0px; height: 1.361em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mtext>E</mtext><mo stretchy="false">(</mo><mi>log</mi><mo>⁡</mo><msub><mi>D</mi><mi>K</mi></msub><mo stretchy="false">)</mo></math></span></span><script type="math/tex" id="MathJax-Element-14">\text{E}(\log D_K)</script>的近似值。最终可以计算Gap Statisitc。而</span><span style="font-weight: bold; font-size: 14px;">Gap statistic取得最大值所对应的K就是最佳的K</span><span style="font-size: 14px;">。</span></p><p><span style="font-size: 14px;">用上图的例子，我们计算了K=1,2,..9对应的Gap Statisitc. </span></p><p><img src="data:image/png;base64,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" data-filename="download%20(16).png" style="width: 463.333px; height: 332.281px;" /><br /></p><p><span style="font-size: 14px;">Gap Statistic的优点是，我们不再需要肉眼了。我们只需要找到最大gap statistic所对应的K即可。所以这种方法也适用于“批量化作业”。如果我们要做1000次聚类分析，不需要肉眼去看1000次了。所以我个人也倾向于这种方法。</span></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1000299" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/1001041/avatar.png?1658233572" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1001041">
                高代兄
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2017-03-07 13:33</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div><div class="row m-x-0 second_reply_div">
			<div class="col-xs-1 text-center" hidden="">
				0<br />
				<a href="javascript: void(0);"><i class="fa fa-sort-asc fa-lg"></i></a>
			</div>
			<div class="col-xs-11">
				长见识了，方法一我倒是没想到，方法四我是头一次听说。谢谢分享！
				- <a class="darkgray" href="user_profile.php?id=1001053">
            <i class="fa fa-user"></i> 起个好名字
          </a> 
				<span class="dark_gray">
          <i class="fa fa-clock-o"></i>
          2017-03-07 14:04
			</span></div></div><div class="row m-x-0 second_reply_div">
			<div class="col-xs-1 text-center" hidden="">
				0<br />
				<a href="javascript: void(0);"><i class="fa fa-sort-asc fa-lg"></i></a>
			</div>
			<div class="col-xs-11">
				这个赞！
				- <a class="darkgray" href="user_profile.php?id=1001044">
            <i class="fa fa-user"></i> Alfred
          </a> 
				<span class="dark_gray">
          <i class="fa fa-clock-o"></i>
          2017-03-08 11:13
			</span></div></div><div class="row m-x-0 second_reply_div">
			<div class="col-xs-1 text-center" hidden="">
				0<br />
				<a href="javascript: void(0);"><i class="fa fa-sort-asc fa-lg"></i></a>
			</div>
			<div class="col-xs-11">
				图文并茂！
				- <a class="darkgray" href="user_profile.php?id=1001069">
            <i class="fa fa-user"></i> 擒贼先擒鱼
          </a> 
				<span class="dark_gray">
          <i class="fa fa-clock-o"></i>
          2017-03-09 13:19
			</span></div></div><div class="row m-x-0 second_reply_div">
			<div class="col-xs-1 text-center" hidden="">
				0<br />
				<a href="javascript: void(0);"><i class="fa fa-sort-asc fa-lg"></i></a>
			</div>
			<div class="col-xs-11">
				小型数据的观察法还可以，对于海量数据可能就不行了。
				- <a class="darkgray" href="user_profile.php?id=1003682">
            <i class="fa fa-user"></i> thinkingrealm
          </a> 
				<span class="dark_gray">
          <i class="fa fa-clock-o"></i>
          2019-08-10 22:26
			</span></div></div><div class="row m-x-0 second_reply_div">
			<div class="col-xs-1 text-center" hidden="">
				0<br />
				<a href="javascript: void(0);"><i class="fa fa-sort-asc fa-lg"></i></a>
			</div>
			<div class="col-xs-11">
				感谢！
				- <a class="darkgray" href="user_profile.php?id=1008513">
            <i class="fa fa-user"></i> 学数据科学的羊
          </a> 
				<span class="dark_gray">
          <i class="fa fa-clock-o"></i>
          2020-09-22 02:03
			</span></div></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1001479" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>5</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1001479" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>类似于回归里的AIC，K Means里的AIC也可以用来选K。</p><p><span class="MathJax_Preview" style="color: inherit;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-15-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;I&lt;/mi&gt;&lt;mi&gt;C&lt;/mi&gt;&lt;mo&gt;=&lt;/mo&gt;&lt;msub&gt;&lt;mtext&gt;argmin&lt;/mtext&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;mi&gt;R&lt;/mi&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;msub&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;mo&gt;+&lt;/mo&gt;&lt;mn&gt;2&lt;/mn&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-140" role="math" style="width: 15.717em; display: inline-block;"><span style="display: inline-block; position: relative; width: 13.098em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1013.1em, 2.622em, -999.997em); top: -2.199em; left: 0.003em;"><span class="mrow" id="MathJax-Span-141"><span class="mi" id="MathJax-Span-142" style="font-family: MathJax_Math-italic;">A</span><span class="mi" id="MathJax-Span-143" style="font-family: MathJax_Math-italic;">I<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="mi" id="MathJax-Span-144" style="font-family: MathJax_Math-italic;">C<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="mo" id="MathJax-Span-145" style="font-family: MathJax_Main; padding-left: 0.301em;">=</span><span class="msubsup" id="MathJax-Span-146" style="padding-left: 0.301em;"><span style="display: inline-block; position: relative; width: 3.753em; height: 0px;"><span style="position: absolute; clip: rect(3.158em, 1003.04em, 4.348em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mtext" id="MathJax-Span-147" style="font-family: MathJax_Main;">argmin</span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.747em; left: 3.039em;"><span class="mi" id="MathJax-Span-148" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mi" id="MathJax-Span-149" style="font-family: MathJax_Math-italic;">R</span><span class="mi" id="MathJax-Span-150" style="font-family: MathJax_Math-italic;">S<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="msubsup" id="MathJax-Span-151"><span style="display: inline-block; position: relative; width: 1.313em; height: 0px;"><span style="position: absolute; clip: rect(3.098em, 1000.66em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-152" style="font-family: MathJax_Math-italic;">S<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.598em;"><span class="mi" id="MathJax-Span-153" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span><span class="mo" id="MathJax-Span-154" style="font-family: MathJax_Main; padding-left: 0.241em;">+</span><span class="mn" id="MathJax-Span-155" style="font-family: MathJax_Main; padding-left: 0.241em;">2</span><span class="mi" id="MathJax-Span-156" style="font-family: MathJax_Math-italic;">p</span><span class="mi" id="MathJax-Span-157" style="font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.205em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.354em; border-left: 0px solid; width: 0px; height: 1.289em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>A</mi><mi>I</mi><mi>C</mi><mo>=</mo><msub><mtext>argmin</mtext><mi>K</mi></msub><mi>R</mi><mi>S</mi><msub><mi>S</mi><mi>K</mi></msub><mo>+</mo><mn>2</mn><mi>p</mi><mi>K</mi></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-15">AIC=\text{argmin}_K RSS_K + 2pK</script></p><p>其中<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-16-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;R&lt;/mi&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;msub&gt;&lt;mi&gt;S&lt;/mi&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/msub&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-158" role="math" style="width: 3.336em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.741em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1002.74em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-159"><span class="mi" id="MathJax-Span-160" style="font-family: MathJax_Math-italic;">R</span><span class="mi" id="MathJax-Span-161" style="font-family: MathJax_Math-italic;">S<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="msubsup" id="MathJax-Span-162"><span style="display: inline-block; position: relative; width: 1.313em; height: 0px;"><span style="position: absolute; clip: rect(3.098em, 1000.66em, 4.17em, -999.997em); top: -3.985em; left: 0.003em;"><span class="mi" id="MathJax-Span-163" style="font-family: MathJax_Math-italic;">S<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span><span style="position: absolute; top: -3.807em; left: 0.598em;"><span class="mi" id="MathJax-Span-164" style="font-size: 70.7%; font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span style="display: inline-block; width: 0px; height: 3.991em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 1.146em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi><mi>S</mi><msub><mi>S</mi><mi>K</mi></msub></math></span></span><script type="math/tex" id="MathJax-Element-16">RSS_K</script>是在聚类个数为<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-17-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-165" role="math" style="width: 1.074em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.896em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1000.9em, 2.324em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-166"><span class="mi" id="MathJax-Span-167" style="font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 0.932em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></span></span><script type="math/tex" id="MathJax-Element-17">K</script>的时候，root of sum of squares，<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-18-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;p&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-168" role="math" style="width: 0.598em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.479em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.551em, 1000.48em, 2.503em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-169"><span class="mi" id="MathJax-Span-170" style="font-family: MathJax_Math-italic;">p</span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.282em; border-left: 0px solid; width: 0px; height: 0.932em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>p</mi></math></span></span><script type="math/tex" id="MathJax-Element-18">p</script>是特征的个数。</p><p>我们选<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-19-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;mi&gt;I&lt;/mi&gt;&lt;mi&gt;C&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-171" role="math" style="width: 2.443em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.027em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1002.03em, 2.324em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-172"><span class="mi" id="MathJax-Span-173" style="font-family: MathJax_Math-italic;">A</span><span class="mi" id="MathJax-Span-174" style="font-family: MathJax_Math-italic;">I<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span><span class="mi" id="MathJax-Span-175" style="font-family: MathJax_Math-italic;">C<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 1.004em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi><mi>I</mi><mi>C</mi></math></span></span><script type="math/tex" id="MathJax-Element-19">AIC</script>最小的那个<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-20-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;K&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-176" role="math" style="width: 1.074em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.896em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.313em, 1000.9em, 2.324em, -999.997em); top: -2.14em; left: 0.003em;"><span class="mrow" id="MathJax-Span-177"><span class="mi" id="MathJax-Span-178" style="font-family: MathJax_Math-italic;">K<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.063em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.146em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 0.932em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>K</mi></math></span></span><script type="math/tex" id="MathJax-Element-20">K</script></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1001479" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1001459.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1001459">
                宽宽
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2018-01-02 00:50</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1002414" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>3</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1002414" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>可以用MeanShift，它不需要预设cluster的个数，而是自己学习cluster的个数。</p><p>相反的，可以先利用MeanShift得到cluster个数，再用K Means。</p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1002414" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1001070.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1001070">
                雷猴
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2018-05-30 12:55</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1007495" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>3</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1007495" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>定K一直是聚类算法的一个研究方向，k-means作为经典算法， 也是解决不了这个问题，如上面那位大神的讲解，之外，还可以根据adjust-R²，CCC值和伪F值判断，都是越大越好，画图来分析寻找合理的聚类个数，如图，进行了6次分群，类数为：3，4，5，6，7，8，最终选择6类，因为在这个值的时候，各项指标已经很好了，后面增加的不是很大，按照奥卡姆剃刀原理，另外，还可以看业务，假如聚类过多，每多一类，那造成的商业成本是很高的，要为每一类做营销方案，每增加一类，成本上升，综合来选，其实这个定k就是结合算法结果和业务，算法只能给我们准确的模型，但是给不出正确的模型。</p><p><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAApkAAAE6CAMAAABqEbm9AAACZ1BMVEX////Z2dn/wAClpaVbm9VZWVn/AACu3/hZcq7f/f/frnrW1tb9//////j//d6+vr7r6+vIkWfI8/3/8Nn//+5ZXZT/4a3zyJT/0XVdkcj9366ucl3z///U/P9ZYKD///q80+tgWVn81KD///Pf6fWRyO5dWXr1//9ZWV7/88iSuOByrt73+v1ZWXqRXVvf9f36+vqBW1pxWWfq/v+76fv/9d9ZbpLLy8pdWVnO3vC4uLjm5uagYFmyzOmoxeXExMSCu+Z3qtr//NTw9Pqg1PX//epqothZWXJuWVnw8PCxsbFZWW6Sbl319fXQ0NH/6sXqyJn/+/bb29uSpbXh4eHo7/jF2O3//ua7g2PH3/OGsd7/7c+rq6v/3aFZWWT/+O1dgKL96tOwkXLX5PL/6rvUoG6Artvq1LdyWnuucmD/yE2g1PH/9OOdvuNioNa8rpH/zWSggGSuyN//5bn/2ZLpu4j/1YRZXYBuka+pqajhuGFyWVnIrpH/xDX/9ddtn9DUoHVvWXNtkrtaXYf+wiuRrshuXYrfroVZgLu6oIOTYGxZWWfo/f/e9f3138ldhLtdgLHIlXKQut59oMX138GCobpZWYeuvc9ulMb13rG7kXH9yVu8yNygvND10qPYtZLHpX7U9f3U6vqgxt/SvJyugGT/wAmu3+eRsdPeyrJZbqPGuqHovmbgx6LSo4DUs3f/z22CXGPvvEaj0urm0cHUvrFdXYmdbmK73/Pq0aevr5mmfIXz//Sx08PDu6zGsYaRrrZ7hXr0yneAp86frbKchJ7MoZuTcZJubqOCXXPf89KAhLtujo6yVRSCAAAZ/UlEQVR42uya2+tMURTHz8t2axCRXAeTjISOQR48TKIzZYo3pCY0eFBETaMIkRARued+eUAehNwiojzwR1nfffY5i7MdPwaZw/fz9Fsz+5w9v/Zn1l5rnwkIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIeT/ZPq0IUOD38LSJXMGB6S4TNhtwKLz8+J44eumMdGbqaVgQDbcD/XCbFh+fHSxqe66PPNnzZwyOQ3aoQHrL9d6MnPFsiCX1WtMDPXtV6ZPMzEH7RKtbMbRuQXBAFSuNYyl+6jkhwsvmZj1N3s2Uz/botG/10y8SzP7nFiFyoPQYBsdM8oseobE+WEgMyuHF1d3rZWhexpjR3vh3jsmOiTZ88RGM35ST2ZqsPx2aE4e/91m4l3SzyQqjFuM7NEOfzSHXG20Nsc79coPo7NhZT9SMCivuvCrZuLmcwbTzP+NZPVnzT02AxG28YFBcnV5zA9xs1a9pOGvmQmNqnWa+b+hZmKp2qH4qVTuNqWLubl0CcYoTuS8EAlYtnSPijRF6JFq8RXbylt2GJQAyVQIvmMmhturwQm5VeusvbayqTq7pH09SggZtxPuxbNKiFaMZhYLrL7KJC0rOhjH8lMGdF/5ZmK4H2oG9atLvGqpXqjZvvvAqaTz0qmit4t9M633qGSNAEft3yCaUYKZZltJh5dXNey4TyHcQyuWzEozC0XaZcR14sVQ2umppcS36PTM8pamMVkzhw/Tl/xwxES44pl56qwkLrmdFI0wE9kY4tgyQKfyzSx3xHvRU74zkitn2MKze6UWLL/WOLggYyY0rh6YF2yQRCnuoeLt3pqJodV9M2lmkUhOZkQMG5/ZYWI3IRhWE4121kzYcKSWE+bUhWqxfbNtvwoQSazzplIz0e7DKglcHsZo1A7QTvbxjJnyJbl3I06rcG/C7mhrkNrtnxrhRIL0Jc5MJJak4BM3W+9q2qjLmN7N9Ok4M3EF6gf0XN5ULtCdWBR27T50g2V2gNzkKzPlfrDVZUV4CvVcHU0ziwSWE5udNtO21UCIt/LN1CXVUM2EHR4b5PmSoGbaS2GmTuWb2TqLDI4kiD5GX7d4ZlohEzP1PWTluvNRPhx38/4Hy5nd7Nym6uuidIwb74fIg9oBKeXnoTE/aqYfoEJ1uV3NxDzfMRMZtJ58JppZLNzq731q05z22uJLvpnYUI/N8ENtiCCqd9AUHxF1ejMTnNiOkjPz+o/nTHZARcKtshZkwJ64i255dSYW2qZFP/RFVdsxg29mbp2pgTJI0DoT/HCdOWcwzSwSbvWTJhag6ZUFFd2wyH5v7nrdpDJd93JBJsR2fnCB28I/1r40E/f2zcxMNYCZMhqTpXSsfe5a66L25lcb0db0P6KZRQKrn9aGlf27Rs6Tc5rr8AyLrIeMOCnXDR/jpTXRn3BkwnZoulf0Fx0ukcrd8Mo3zNSpcs3s7JJGaDnMxPfA/l5k+ZOXy+yN5SjBXYtIzzPxuVCaysdCi0cziwRWP32MIxtjTGuzO10Ei7ZjDBZZz8/14QoeGvnhmab+Ck4TMai+nZ81U6c6+GpJrpkGwMz0iRHk0xt3X4QY7p4Ptd6dsm+ubKb/EZ8BFQqsftKg1IOFI/FoO3qzNgA4TcKv2ewYV8EpZfcYfN43QuSzHfq4OnmpiUP89sO6ne4rM/EUSqbCI3rfTL1hBDPTybrvp5bctZKxb86aa4fHj+OnVjbBPTcr8nmmTqaZ/wAwBFkOteNfxppJiJope2ZPv2yjmUT5I2a2Q/npxV+HZpKMmcOH9cFeTjOJnzP7A5pJ+hOaSQj5zN69tTgNRHEAH4d4w8uDwRgvYB6qYqwIKkofuiCi+CDEEKzaEqoIorVLi62BDVRRq4IoCioIVXwRFbxSRHFFhcUP5pwx2bG1rWka20TOD3Zpdxe6y/5zJnOmzCCEEEIIIYQQQtg1QkmByUTxhMlE8YTJRPGEyUTxhMlE8YTJRPGEyUTxhMlE8YTJRAghhBBCCCEUDOw9xo6k2UI8Dw4vWervMw0b3CP0lwC9Yts8vdwloiQejOTY8Xt3Nh65cp4A2PRvIU/mxot7ssvJqR0EoYFW3Ly+g52As225iJLI1CjWnV0M+03C1pGwN+TJr+t5MrfeOk8Q9jMDWslSI6IkMhUaZHH1Kv+zeA1C1uARH5jMYZK5doOIkshUaJDsX0HcvPi3ZMKX98we4lvgov8+melU6igZyYG31xaLKL0QmfonybywZeORnZtItwWT9GGu1Zr7vCAZIJkL4m/ZE4k5+Djoz/cYdhfCDGhsyYTPUKNJjCiUe2+SJEhGzUzn73932+7s5QwJDc4/uns74mSKm4P4J7NGPQ5JgmQkU5uhXPthioQHMYz4PpMnW8yjxAyIH/55btvkt+4VmtQnkwSIbTKPppicxkzrukV/ed6+MGKMRJREpsKD9F3dsfHIjd28QIpkXvr0aNeBtx/jsEOqT6a/aaiqrSiyXCSxFX0y09oZScpnyBD2p5iMxkzpzD6pW5v6XoUM0Bd2SrbBRvP5KIkHo4HjaE6e8IbuNfwYkO2L4Yhmfqh3XBQNp0l7q6qOohhy7Opo5MlMn5G46b5zbOa0xmR1Ji8NcN/6Uam8c9tUcEkocGwSnCoyHyXx4P9XVqq0n5gWUtmhkSdTlzxZ9iQFNOClMJCH1kzlu+s2aQ9tgoZhGvUGHZ4KhbQwsUJq0OeUsg8jknYjyGlTUliXLWuWF8iBWgQFVq6ptIemXVfVoHktQSGtDSqkBVu1DRIlOdxcbb8ohFkdHJRCEiO2C4EMpE5QMAW71Bkx2w9jgXCmLBuKoqrVkQqp+Z6CVpmEZMqeguKpN577M96WAq/ImH9Oj09rYEoHUnQsGLFfv6YBVFVHpb4Y3AMlQLHm0A5OrcgyUOeN9h4ZKkMsWCGlQxdSs+VlqGn2/EVkT03xqD46vNeMWwEWGD507B7x+32py0GdubB375s3c3MtGoD3xxPOv64Ngv5GtqudMaoXTFGfin+tYDWIT4kOq6ootuop0bFxmXcVZtZiHkoDvKNcRcqyWptLMUf5JamqjWBXI9TvMumiNOGbBYIGMg2n0ZmXWpmEIwpp0jR5Wp8x3/Yyj3MpkH4qOo9w+dmqGmzErkO/wiT9xaKbEWvd3aFG3TBJFEQhHaNFDI1MSX1PhUANtDg2eRPILNS7iqUtk2iJQuqMVEgbqsdRmM+f3zz7ZnkuS5w1n0yLzZCZmQrzzmW3mU36L5X4HA9LYGSK3d0hxyiSf63Ih8TmH/9bj614ZB/pxObWU/36OjP0OU/mTF7TUmB/1+Xhz6kclWnQsMSIDVOaZLwHKzn+7A4VyPgY1KcEf0eEloUV6H706axkuTyZ0lESlAzE7D9Y7YZl2TJB0SsaDu2g1opkvOp+3QnSCc8NjGR+Wsuk0oTJsGeQzAwZhel3SXnToEXn2fFYgv1v9ewOjZ9NQd0cuECY0watTed1Ldc5YO+f2hf1urnZ9Nv3uI4YQujl8KpSJhNiFhSj2C+SGW1al/rap2c1iORY3mtU8NcEcPwOIVx3yDFMMjmns3o2Q4LPb8BB/Sd7Z/YrQxDF4ZKyJApV9u2BxL63tZmO20Qs09EjxpDYgkgIQaxhXpDgAW+WxL4+WBLCCyL+OFWmR3WP7unResypnvMlLia59+lL3Tp1Tv1qYPrMnf95PnPs8V89MBRTk+/p0PGcTodynXpcvzNU37QbpZBKHp7Zq5n2E7i/jNLVdnjP0GIqTu1MqW/m/6pvCnDbAgF1OpTEdK1e+/qm9zPtSBc40NoOn3QOyG7pyODU+gYpEtvPfTp9+vwBojixv7UdvhdMt2JDQn2zVtU3yF9lwY2aOkQyfkwzCw5kwEtz6nEbpNOhP1kzv1XJRn2D/E0W3F15UXLLghHBJXCdLwgys+1xfDtNtcPBsHNttAI/peobJHMWXGCmzhcEFaMRbUa3FDyQRrIWrvmjpTOdIP9uZjT3BRxylBDa6VCEnQOb/qzACZKZeYullL/2mQd3h7OywHE62g6HcDqUsFyu37Vw7WDFwEKigZmEAJcZV6+taIZWzx5miJn7ARU8ipkDgzUDM3+penj6muBsCM3MgoyzXDfi9+o5+QdgM/frKy0EEgt3hXo8e9YsJC2gmZl4+PnInFD68A/A+8wD138vmQQOhwdCx0MDcceVaGYmMZc+WB7eccrVEmxt/rs4Pw3nSH16B8slmvkvYj6TsVsrH71/2cyCgxQkqBn7WP0qnwBFzMMnQ8vl2sRNJZqZJbV6iOL2LHLo5moVCgc+C+4AmCulG9aGlsv5a0gyaCby/1gzv9Plsl/N9J2qsAjyX9kQ7kCePEza05dmWjaV1KsE+W8sDC+X66enL5f9aKZVog0qBBoJL6LKKmsRwJPSLB3IzpfLPjSzQpsIAouEF1FnfFg6xGAzWzqQOEOUgCXob2wCi9gXUdXHT18Ya+bM8HI5gOOWcQiHuZyGKRFQJL2Iqj4z08xoBxKXy1Z8wSrco7+AbKaeCymGmTMjHUi8MBFG1JhboolwAopCmdnSgcTlMqAsmM330RRqBBRpZsJ6q7ctT95qLU+9fTIIGcRsl3seTWKfx12XBniDOoO0A/eZCcul7kACoKenRsJhNk9WkttMlIMFtU4VHFwX6PfEkslmrokMbAC5Id4bM31RVQVOEiWX1VpakVbV5bZDwBF5EdVIM6MdSBDLZQ/MTCtwPF5hwicmEf8i6rzFQyRzQb0iHUu0AwlkueyamYJVy39b4HCXOdD6O4Wn5x3I/2um41GJV9YdnBrj7ZZJVjVsmSwGLR1ISMtld8ys0Qb1MimnFjhOmSA9YSf4DmTeZlp1mkqJsxrOWvYAdTR0amCh6kDCH9jI2Uxh0zbsM6/AKRALg2LnVPiMCORymY+ZusCpYIEDmrWBjYZ0IDObaViBE6QU6lFf0CmF3WDhYIU5AxvZzdQFTgIcUIGjUwqbo76gUwq7weFoajrk5fJfOjiMezSFOoGG6s/oUV/AKYVdYMP0UC1+CkoHUpL3JG9ygWMDnQoKzNQjGIDTYzR53jXTDJDi4KcWODURubNThyfmr5TC32NrbwAnbmnyzCPSwGmOd7PAqfxR4PjMdasAip7YlMJ+M1NnVmuOELMpO20b3cZ1cH6lFPaXmRvkibrm5J3gaB12Td7Ar7KqH1/gFK6D00gp7J99ZnRzuUc1xtccUQNFBhTlKvhiqMTqtMCxmTBqmYwJg9OjvpBTCv+dw+G++Pq1JiyTIUq0YWZJFThpk7yGd3ACMfWoL+yUwn/dXK4Pn6gDG29Lh9HATNquwAHRwckxpTAY9QWfUvgPm8s94c2liSfqXjszuY2NbgNZKK/0gJ66TEcwTrWZ0QIH4wANJbK53GTa5lJb+dvMIhQ4iIoG1pi3udRWhsysG1/g9DsLd+0xeFzDciq6mRMxkxHEZEzeXMZZyfc1T41wW2kwM83dXMZayQQhFm+YiWIai9pcwr2Ym8XKAIcxBjD4Aul0c2nK1YlOrMRSpyDI16Ogxmuglf2LvC5uzo0etLJf2DDdwM1ljJX73CqenxcHFfpiWpA6Wll8optLEy6aoZV9gLw5YUS6RpqVMPMzkX+4OQEygTUBv2Z7MVbCTXZFMt6cMGlzmWRlz5NdkXw5PAB6c2kJIaw0K3ueBYfk1t45tX5gZ2NzCfvmBKtTScVKthJESmH/EcntmvFu65DNN5aoO8RHzwwZ8v5l1lrnSMPEXbvWQ785YdMGpXgre59SCJ/gWedRU4dIxo/RTuX3Vu+0C9eGkW1br8yR/1q1dgQ5tIRkQ4rZyh6Yw20O1bRaCSM/Ezq/n3UedWzBiIhT+b3VG/zsiVL7ebf+5eeuacgI/1quL7wEKwHkZxpC8KyzNlM7ld8balOWzQq+TpQBINlRhTjszaUvqvGhQp5d8wkBkexqDCOHazMjTuX17mTwlwr2Gjd61fctQy6+zrhVAHxzoiyYVjLBSjQzm5lTh6hr5iGnumPm2TkySGlWthdRf5U9V66or2BeJq3YnHv7aBsqg5B0ks1UrHwxe1iXzVQfq2fVMiaqX9lBJfcHnyI9RzhBfksKNkGyoc1U8kz+oZ3Kf5/5j2ZuuEsb7JhOeofQYYDJqalO09l6EaJceoM285czP7RTOb3Vq4QPanP1J9jSZsGv04AK+f9YHSip4wDLJarwcHoopzVzgXYqv7d6Rw5f9U2eZ8qYzstfHyzf+PFLxjivipaASWpCQrqPJWo6CzDx2btASU3N5W4Nbzn+s5nPZItm5aP3L7VTOb7Vu/F5syK/d2bI3EuvSDZ4YgAa5y6TOEJkilPx47/NT1USY666hX7W+dDN1aqBCDoLrkQ7pdR0VUj8NC/5L72dtGPJaBjgXyqJp0ZFhtPscInddNWK3b3WCCl3ouTfLstoZuGp0hzZxyUVqaqntWv/XC2M4DU0EyDWb3Uc+T8hqUqzKlyyj3aLEpB3GNFMyJS9dodGVtNVm0vov8JdWEqimZCxWInWXdF5zS1hgaulzpWE/EoJmllMylJVh0ncGFc90EqimX2GqNMmRpxMopl9g2PW7AWa2T/UTBITzewnfMZ5xYhf5WgmgiAIgiAIgiA/2bubl6iiMI7j18XtRUahEEQTJhgmcxEyieLSjcxGcN0mepEMXIQLIRDGsShpjKJy4yJJCCqDIoIsItBNZH9V5zHHIzWCI88w58zz/SxibovpDvPrzrnnPPc5AAAwa4SIkEyEyU4ypRfcgbaC/gWCZCWZe73gfAs4/wJBspLMai843wLO94JDiKwks/q8uW/34nt0IETWkrnfIuuN72uEEJFMkhkmkkkyw2QtmYwzY2Etmb4FXPcF7s0RAknmgbaC/gXQPL4X3F4LuKB7wQEAAADwmDUKySF79UrRHXP4JFOB7l69UnRHMkmmAuW9eqXojmSSTAXKe/XK35FMkqlAd9/JDMkkmaoan8w2HJEks631JLU1P5ngmnkoxplRIJlCe69ekkkyNejv1UsySWbT1d6r1xfdAQCAFtMG2xIAwPH1zqdOTx/NCWNhZdZIqtUEzQljYS6ZNCeMhLVkdtA0JhJmkunGmVdfDCZdNNqKhJVkipXZU6dJZiwsJTPpXs6TzFiYSqarnGScGQtTyZQrJc0JI2EkmV0/3dz6insSnOaEsTCSzOz0bCorPzQnBAAAAAAARzH8vpAW3w4l2rJzo36NQbnyVdf1R6NpcUb7TMVyXn/a59p5I0/Jdiy59rCrBf2HgkuVbe1kShWXvqmdE87NRF1H+8a67udfzGdyS18sTZB3npMlflW58sLHKJLZdWahQTPtpU29/+++rFI6Btmx21tB19qv9fYokjlQOdmYZGbntD9/d3HGvaula+b4h/vaX3mpMuNrWZQrX7W/7i1Jpn9XvW4/C/3a31Nx687tz0bGme43ItW/A8qVe/q0k+krX5WT+UCSqfyjoVv+6Fv17+4aYUd2euLp40TTmqtj0U6mr3zVDpAkU85VOUXqYZ+cuDe4MjtiqqrSfT3a1+FG9QHrvRxHMrXPU+7V5PpR2jRVVinJVFa9ZoZ+qgOVvCTTjxEUW0QL3ftU+dNIMju/vxxKJqu/5kEn01e+asqVRySZY5lE1dQneUftM/2aZL/tWGlg8ORGWh1WB55MX/mqaviVJDMT+IcX468LhtaAAKBFud/di3ev1DiaKixbWrGCQoJ0x9S3+sefbaz/d5Qrb5taS4VCglTH1G4aQuY4/jmSJep3JBN1JMjTn83yR7JEbav+BGHNh8reVH4C1x+5crN+ksnz5vUmqPHJXHt4VlbC2EHguMzsiNqAZMpmVJd+1E7m782xjLFqUsE1M5xr5iHjzNX5dJf750AymzHOlKz7O6uDR9Yq8KGQIE29i8/dbJQrvZDU7x+RTNSdIF1S3/v3WQNJ5v4RyUR9CbJUEw8AAAAAAAAAAAAAAAAAAPCnvbt5bSIIwwD+srslrQZLSkjASwqhgm2kKfkwBqpeligUteJXLKj1EDVqINhaAlJEi0VQtNLSVhCloliE6qVV0Gv8u5ydzrDV7HR36cGsfX6HUN5DGdhnZ2d2YV4AAAAAAAAAAAAAAAAAAACAfyDVWzOM2tGUon256JGWe3DCX6+w9OGGrjf2ptVt4vKLGaLk6ghrO9IbtktuYlVN0yauqs7b3TrKaKSDORQiCKBUxeBq5xXdbZNv2U808vI5zTd7yKuTDZ0rOkUzcYYdzkfjT/vInLMaN95o9tglF181buaOarizpdvE7aJWpf+lu4ZQUVxqfn35sc1+FHXhmGMzXtmbNL6R3VpyF9OEmdFthotkBo/h3Z/JXMoQN369o/Tqy98nfeve2b1J7eiIkgPNM3u4nV25d4XSpwySGSSGD/Jp/iRLicnC5vrt4qVHg+ZaYUfJtE/Ml1OxLLXQfLBvpJ97Xjwzf4WQzCAxfJA7oO+iX3R+OEz7b4accqT7wGc1ucMSyZSlnSfTXNvIRiOyqQM6OQSG/6f5MmuNSJb5+uMsf+qyZLbpnMlupCsLZaLlofziINaZweI7mYlJFkaZI1UyqX3WmZy5zm4jJDPQhg2hX7E3lxMb/4PiB0LWYtP1CdmtC6cc/+3xsAgky49d8uCetuljVbE3l/bdGggjmUGW6je4SkqVzOTDzq74wgpfwdH0t6WMOee+dksXda47Ta2Ss1PvrZeXA+HpD9fKbA37I2SXaHsTLu8zLQebZTo90oc5M+COXGa5vECkuNT811y3PtWsENFYvWPqzWsPu4qzRZbLc+QouVoXH3xyn4f4NyC75GbsvqZVY6OK4cpeJmyQeGu0+0Qj2O9CO0IyoT0hmQAAAAAAAAAAAAAAAAAAAAAALX4D8ePE7jU5YesAAAAASUVORK5CYII=" data-filename="download%20(4).png" style="width: 521.573px; height: 246.333px;" /><br /></p><p><br /></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1007495" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1007365.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1007365">
                作业没写做么办
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2020-03-18 16:44</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1002606" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>1</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1002606" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>RPCL算法可以了解一下，可以认为某种程度上不需要设定K，而是自动选择合适的K。</p><p><br /></p><p>Lei Xu, Adam Krzy˙zak, and Erkki Oja. Rival penalized competitive learning for clustering analysis, rbf net, and curve detection. Neural Networks, IEEE Transactions on, 4(4):636–649, 1993.</p><p><br /></p><p>在这篇论文中有用到RPCL算法：</p><p>Automatic False Positive Canceling for Indoor Human Detection, ICIA2017</p><p><br /></p><p>以及，我比较naive的重现这篇论文的代码（部分涉及RPCL算法）：<a href="https://github.com/zchrissirhcz/dfp" target="_blank">https://github.com/zchrissirhcz/dfp</a></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1002606" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1002929.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1002929">
                ChrisZZ
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2018-07-15 23:23</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1002755" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>1</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1002755" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>补充一个方法，<a href="http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html" target="_blank">silhouette score</a></p><p>具体可以参考<a href="http://www.sthda.com/english/wiki/print.php?id=239#average-silhouette-method" target="_blank">这篇文章</a>以及<a href="http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html" target="_blank">sklearn里的例子</a></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1002755" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1001475.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1001475">
                Jiho
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2018-08-14 22:11</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div><div class="row m-x-0 p-x-0 main_reply_div">
		<div class="col-md-1 col-xs-2 p-x-0 text-center">

      <div class="widget-vote">

        <button class="vote_btn vote_btn_up wenk--right" method="up" post_id="1000659" data-wenk="我喜欢你的回答！">
          <i class="fa fa-sort-asc"></i>
        </button>

        <div>0</div>

        <button class="vote_btn vote_btn_down wenk--right" method="down" post_id="1000659" data-wenk="这回答不大给力！">
          <i class="fa fa-sort-desc"></i>
        </button>

      </div>

		</div><div class="col-md-11 col-xs-10 p-r"><p>有一种叫X-mean的方法可以从2个Cluster开始自动develop新的cluster，直到总体的BIC不能改善。<a href="https://www.cs.cmu.edu/~dpelleg/download/xmeans.pdf" target="_blank">Paper link</a></p><a href="http://sofasofa.io" style="color:#ffffff; font-size:10px; text-decoration: none">SofaSofa数据科学社区</a><a href="http://sofasofa.io/interviews.php" style="color:#ffffff; font-size:10px; text-decoration: none">DS面试题库 DS面经</a><div style="height:2rem;">
    <div class="modal fade" id="modalDeletePost">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
            <h4 class="modal-title">Warning</h4>
          </div>
          <div class="modal-body" id="modalDeletePostBody">
            <p>您确定要删除本贴么？所有相关回复也会被一并删除并且无法恢复。</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal"><i class="fa fa-ban"></i> 取消</button>
            <button type="button" rowid="1000659" id="btnConfirmDeletePost" class="btn btn-danger"><i class="fa fa-trash"></i> 确定删除</button>
          </div>
        </div>
      </div>
    </div>
        <div class="author_div">
          <div style="float:right;">
            <p class="m-l">
              <img src="assets/images/avatars/default/1001099.png" class="img-circle" style="border: 0px solid #999; width:40px;" />
              <a class="darkgray" href="user_profile.php?id=1001099">
                Jeremy
              </a>  
              <span class="gray"><i class="fa fa-clock-o"></i> 2017-05-02 05:12</span>
            </p>
          </div>
        </div></div><div style="margin-top:1rem;"></div></div></div></div>
    <form enctype="multipart/form-data" id="form_main_reply" role="form" hidden="">
          <p><a class="qa_header" style="color: #00B068 !important;text-decoration: none" href="javascript: void(0);"><i class="fa fa-plus-square fa-lg"></i><i class="fa fa-minus-square" hidden=""></i> 回答问题时需要注意什么?</a></p>
      <p class="qa_answer" style="font-size: 12px; display: none;">我们谢绝在回答前讲“生动”的故事。   我们谢绝答非所问。   我们谢绝自己不会、硬要回答。<br /><br />我们谢绝“这么简单，自己想”、“书上有，自己找”这类回答；如果你认为对方提问方式或者内容不妥，可以直接忽略，不作解答，甚至投反对票。<br /><br />我们感激每一个用户在编写答案时的努力与付出！</p>
      <hr />
      <span style="font-size: 20px" id="section_main_reply">我知道答案        </span><span style="font-size: 12px">点击下方 <i class="fa fa-file-code-o" aria-hidden="true"></i> 可插入编程代码；用美元符号<i class="fa fa-usd" aria-hidden="true"></i>插入<span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-21-Frame" tabindex="0" data-mathml="&lt;math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;&gt;&lt;mi&gt;L&lt;/mi&gt;&lt;mspace width=&quot;-.325em&quot; /&gt;&lt;mpadded height=&quot;+.21em&quot; depth=&quot;-.21em&quot; voffset=&quot;+.21em&quot;&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mstyle displaystyle=&quot;false&quot; scriptlevel=&quot;1&quot;&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;A&lt;/mi&gt;&lt;/mrow&gt;&lt;/mstyle&gt;&lt;/mrow&gt;&lt;/mpadded&gt;&lt;mspace width=&quot;-.17em&quot; /&gt;&lt;mi&gt;T&lt;/mi&gt;&lt;mspace width=&quot;-.14em&quot; /&gt;&lt;mpadded height=&quot;-.5ex&quot; depth=&quot;+.5ex&quot; voffset=&quot;-.5ex&quot;&gt;&lt;mrow class=&quot;MJX-TeXAtom-ORD&quot;&gt;&lt;mi&gt;E&lt;/mi&gt;&lt;/mrow&gt;&lt;/mpadded&gt;&lt;mspace width=&quot;-.115em&quot; /&gt;&lt;mi&gt;X&lt;/mi&gt;&lt;/math&gt;" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-179" role="math" style="width: 3.388em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.815em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.253em, 1002.82em, 2.503em, -999.997em); top: -2.133em; left: 0.003em;"><span class="mrow" id="MathJax-Span-180"><span class="mi" id="MathJax-Span-181" style="font-family: MathJax_Math-italic;">L</span><span class="mspace" id="MathJax-Span-182" style="height: 0.003em; vertical-align: 0.003em; margin-left: -0.31em;"></span><span class="mpadded" id="MathJax-Span-183"><span style="display: inline-block; position: relative; width: 0.523em; height: 0px;"><span style="position: absolute; clip: rect(3.336em, 1000.52em, 4.169em, -999.997em); top: -4.216em; left: 0.003em;"><span class="mrow" id="MathJax-Span-184"><span class="texatom" id="MathJax-Span-185"><span class="mrow" id="MathJax-Span-186"><span class="mstyle" id="MathJax-Span-187"><span class="mrow" id="MathJax-Span-188"><span class="texatom" id="MathJax-Span-189"><span class="mrow" id="MathJax-Span-190"><span class="mi" id="MathJax-Span-191" style="font-size: 70.7%; font-family: MathJax_Math-italic;">A</span></span></span></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 4.013em;"></span></span></span></span><span class="mspace" id="MathJax-Span-192" style="height: 0.003em; vertical-align: 0.003em; margin-left: -0.154em;"></span><span class="mi" id="MathJax-Span-193" style="font-family: MathJax_Math-italic;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.107em;"></span></span><span class="mspace" id="MathJax-Span-194" style="height: 0.003em; vertical-align: 0.003em; margin-left: -0.154em;"></span><span class="mpadded" id="MathJax-Span-195"><span style="display: inline-block; position: relative; width: 0.784em; height: 0px;"><span style="position: absolute; clip: rect(3.18em, 1000.78em, 4.169em, -999.997em); top: -3.799em; left: 0.003em;"><span class="mrow" id="MathJax-Span-196"><span class="texatom" id="MathJax-Span-197"><span class="mrow" id="MathJax-Span-198"><span class="mi" id="MathJax-Span-199" style="font-family: MathJax_Math-italic;">E<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 4.013em;"></span></span></span></span><span class="mspace" id="MathJax-Span-200" style="height: 0.003em; vertical-align: 0.003em; margin-left: -0.102em;"></span><span class="mi" id="MathJax-Span-201" style="font-family: MathJax_Math-italic;">X<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.138em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.309em; border-left: 0px solid; width: 0px; height: 1.253em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>L</mi><mspace width="-.325em"/><mpadded height="+.21em" depth="-.21em" voffset="+.21em"><mrow class="MJX-TeXAtom-ORD"><mstyle displaystyle="false" scriptlevel="1"><mrow class="MJX-TeXAtom-ORD"><mi>A</mi></mrow></mstyle></mrow></mpadded><mspace width="-.17em"/><mi>T</mi><mspace width="-.14em"/><mpadded height="-.5ex" depth="+.5ex" voffset="-.5ex"><mrow class="MJX-TeXAtom-ORD"><mi>E</mi></mrow></mpadded><mspace width="-.115em"/><mi>X</mi></math></span></span><script type="math/tex" id="MathJax-Element-21">\LaTeX</script>公式</span>
      <hr />
      <input name="ancestor_id" id="input_ancestor_id" value="1000282" hidden="" />
      <textarea name="content" class="form-control summernote" style="display: none;"></textarea><div class="note-editor note-frame card"><div class="note-dropzone">  <div class="note-dropzone-message"></div></div><div class="note-toolbar card-header"><div class="note-btn-group btn-group note-highlight"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="highlight"><i class="fa fa-file-code-o"></i></button></div><div class="note-btn-group btn-group note-style"><button type="button" class="note-btn btn btn-light btn-sm note-btn-bold" tabindex="-1" title="" data-original-title="粗体 (CTRL+B)"><i class="note-icon-bold"></i></button><button type="button" class="note-btn btn btn-light btn-sm note-btn-italic" tabindex="-1" title="" data-original-title="斜体 (CTRL+I)"><i class="note-icon-italic"></i></button><button type="button" class="note-btn btn btn-light btn-sm note-btn-underline" tabindex="-1" title="" data-original-title="下划线 (CTRL+U)"><i class="note-icon-underline"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="清除格式 (CTRL+\)"><i class="note-icon-eraser"></i></button></div><div class="note-btn-group btn-group note-font"><div class="note-btn-group btn-group"><button type="button" class="note-btn btn btn-light btn-sm dropdown-toggle" tabindex="-1" data-toggle="dropdown" title="" data-original-title="字体"><span class="note-current-fontname">Arial</span></button><div class="dropdown-menu note-check dropdown-fontname"><a class="dropdown-item checked" href="#" data-value="Arial"><i class="note-icon-menu-check"></i> <span style="font-family:Arial">Arial</span></a><a class="dropdown-item" href="#" data-value="Arial Black"><i class="note-icon-menu-check"></i> <span style="font-family:Arial Black">Arial Black</span></a><a class="dropdown-item" href="#" data-value="Comic Sans MS"><i class="note-icon-menu-check"></i> <span style="font-family:Comic Sans MS">Comic Sans MS</span></a><a class="dropdown-item" href="#" data-value="Courier New"><i class="note-icon-menu-check"></i> <span style="font-family:Courier New">Courier New</span></a></div></div><button type="button" class="note-btn btn btn-light btn-sm note-btn-superscript" tabindex="-1" title="" data-original-title="上标"><i class="note-icon-superscript"></i></button><button type="button" class="note-btn btn btn-light btn-sm note-btn-subscript" tabindex="-1" title="" data-original-title="下标"><i class="note-icon-subscript"></i></button></div><div class="note-btn-group btn-group note-fontsize"><div class="note-btn-group btn-group"><button type="button" class="note-btn btn btn-light btn-sm dropdown-toggle" tabindex="-1" data-toggle="dropdown" title="" data-original-title="字号"><span class="note-current-fontsize">16</span></button><div class="dropdown-menu note-check dropdown-fontsize"><a class="dropdown-item" href="#" data-value="8"><i class="note-icon-menu-check"></i> 8</a><a class="dropdown-item" href="#" data-value="9"><i class="note-icon-menu-check"></i> 9</a><a class="dropdown-item" href="#" data-value="10"><i class="note-icon-menu-check"></i> 10</a><a class="dropdown-item" href="#" data-value="11"><i class="note-icon-menu-check"></i> 11</a><a class="dropdown-item" href="#" data-value="12"><i class="note-icon-menu-check"></i> 12</a><a class="dropdown-item" href="#" data-value="14"><i class="note-icon-menu-check"></i> 14</a><a class="dropdown-item" href="#" data-value="18"><i class="note-icon-menu-check"></i> 18</a><a class="dropdown-item" href="#" data-value="24"><i class="note-icon-menu-check"></i> 24</a><a class="dropdown-item" href="#" data-value="36"><i class="note-icon-menu-check"></i> 36</a></div></div></div><div class="note-btn-group btn-group note-color"><div class="note-btn-group btn-group note-color"><button type="button" class="note-btn btn btn-light btn-sm note-current-color-button" tabindex="-1" title="" data-original-title="最近使用" data-backcolor="#FFFF00"><i class="note-icon-font note-recent-color" style="background-color: rgb(255, 255, 0);"></i></button><button type="button" class="note-btn btn btn-light btn-sm dropdown-toggle" tabindex="-1" data-toggle="dropdown" title="" data-original-title="更多"></button><div class="dropdown-menu"><div class="note-palette">  <div class="note-palette-title">背景</div>  <div>    <button type="button" class="note-color-reset btn btn-light" data-event="backColor" data-value="inherit">透明    </button>  </div>  <div class="note-holder" data-event="backColor"><div class="note-color-palette"><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#000000" data-event="backColor" data-value="#000000" title="" data-toggle="button" tabindex="-1" data-original-title="#000000"></button><button type="button" class="note-color-btn" style="background-color:#424242" data-event="backColor" data-value="#424242" title="" data-toggle="button" tabindex="-1" data-original-title="#424242"></button><button type="button" class="note-color-btn" style="background-color:#636363" data-event="backColor" data-value="#636363" title="" data-toggle="button" tabindex="-1" data-original-title="#636363"></button><button type="button" class="note-color-btn" style="background-color:#9C9C94" data-event="backColor" data-value="#9C9C94" title="" data-toggle="button" tabindex="-1" data-original-title="#9C9C94"></button><button type="button" class="note-color-btn" style="background-color:#CEC6CE" data-event="backColor" data-value="#CEC6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#CEC6CE"></button><button type="button" class="note-color-btn" style="background-color:#EFEFEF" data-event="backColor" data-value="#EFEFEF" title="" data-toggle="button" tabindex="-1" data-original-title="#EFEFEF"></button><button type="button" class="note-color-btn" style="background-color:#F7F7F7" data-event="backColor" data-value="#F7F7F7" title="" data-toggle="button" tabindex="-1" data-original-title="#F7F7F7"></button><button type="button" class="note-color-btn" style="background-color:#FFFFFF" data-event="backColor" data-value="#FFFFFF" title="" data-toggle="button" tabindex="-1" data-original-title="#FFFFFF"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#FF0000" data-event="backColor" data-value="#FF0000" title="" data-toggle="button" tabindex="-1" data-original-title="#FF0000"></button><button type="button" class="note-color-btn" style="background-color:#FF9C00" data-event="backColor" data-value="#FF9C00" title="" data-toggle="button" tabindex="-1" data-original-title="#FF9C00"></button><button type="button" class="note-color-btn" style="background-color:#FFFF00" data-event="backColor" data-value="#FFFF00" title="" data-toggle="button" tabindex="-1" data-original-title="#FFFF00"></button><button type="button" class="note-color-btn" style="background-color:#00FF00" data-event="backColor" data-value="#00FF00" title="" data-toggle="button" tabindex="-1" data-original-title="#00FF00"></button><button type="button" class="note-color-btn" style="background-color:#00FFFF" data-event="backColor" data-value="#00FFFF" title="" data-toggle="button" tabindex="-1" data-original-title="#00FFFF"></button><button type="button" class="note-color-btn" style="background-color:#0000FF" data-event="backColor" data-value="#0000FF" title="" data-toggle="button" tabindex="-1" data-original-title="#0000FF"></button><button type="button" class="note-color-btn" style="background-color:#9C00FF" data-event="backColor" data-value="#9C00FF" title="" data-toggle="button" tabindex="-1" data-original-title="#9C00FF"></button><button type="button" class="note-color-btn" style="background-color:#FF00FF" data-event="backColor" data-value="#FF00FF" title="" data-toggle="button" tabindex="-1" data-original-title="#FF00FF"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#F7C6CE" data-event="backColor" data-value="#F7C6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#F7C6CE"></button><button type="button" class="note-color-btn" style="background-color:#FFE7CE" data-event="backColor" data-value="#FFE7CE" title="" data-toggle="button" tabindex="-1" data-original-title="#FFE7CE"></button><button type="button" class="note-color-btn" style="background-color:#FFEFC6" data-event="backColor" data-value="#FFEFC6" title="" data-toggle="button" tabindex="-1" data-original-title="#FFEFC6"></button><button type="button" class="note-color-btn" style="background-color:#D6EFD6" data-event="backColor" data-value="#D6EFD6" title="" data-toggle="button" tabindex="-1" data-original-title="#D6EFD6"></button><button type="button" class="note-color-btn" style="background-color:#CEDEE7" data-event="backColor" data-value="#CEDEE7" title="" data-toggle="button" tabindex="-1" data-original-title="#CEDEE7"></button><button type="button" class="note-color-btn" style="background-color:#CEE7F7" data-event="backColor" data-value="#CEE7F7" title="" data-toggle="button" tabindex="-1" data-original-title="#CEE7F7"></button><button type="button" class="note-color-btn" style="background-color:#D6D6E7" data-event="backColor" data-value="#D6D6E7" title="" data-toggle="button" tabindex="-1" data-original-title="#D6D6E7"></button><button type="button" class="note-color-btn" style="background-color:#E7D6DE" data-event="backColor" data-value="#E7D6DE" title="" data-toggle="button" tabindex="-1" data-original-title="#E7D6DE"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#E79C9C" data-event="backColor" data-value="#E79C9C" title="" data-toggle="button" tabindex="-1" data-original-title="#E79C9C"></button><button type="button" class="note-color-btn" style="background-color:#FFC69C" data-event="backColor" data-value="#FFC69C" title="" data-toggle="button" tabindex="-1" data-original-title="#FFC69C"></button><button type="button" class="note-color-btn" style="background-color:#FFE79C" data-event="backColor" data-value="#FFE79C" title="" data-toggle="button" tabindex="-1" data-original-title="#FFE79C"></button><button type="button" class="note-color-btn" style="background-color:#B5D6A5" data-event="backColor" data-value="#B5D6A5" title="" data-toggle="button" tabindex="-1" data-original-title="#B5D6A5"></button><button type="button" class="note-color-btn" style="background-color:#A5C6CE" data-event="backColor" data-value="#A5C6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#A5C6CE"></button><button type="button" class="note-color-btn" style="background-color:#9CC6EF" data-event="backColor" data-value="#9CC6EF" title="" data-toggle="button" tabindex="-1" data-original-title="#9CC6EF"></button><button type="button" class="note-color-btn" style="background-color:#B5A5D6" data-event="backColor" data-value="#B5A5D6" title="" data-toggle="button" tabindex="-1" data-original-title="#B5A5D6"></button><button type="button" class="note-color-btn" style="background-color:#D6A5BD" data-event="backColor" data-value="#D6A5BD" title="" data-toggle="button" tabindex="-1" data-original-title="#D6A5BD"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#E76363" data-event="backColor" data-value="#E76363" title="" data-toggle="button" tabindex="-1" data-original-title="#E76363"></button><button type="button" class="note-color-btn" style="background-color:#F7AD6B" data-event="backColor" data-value="#F7AD6B" title="" data-toggle="button" tabindex="-1" data-original-title="#F7AD6B"></button><button type="button" class="note-color-btn" style="background-color:#FFD663" data-event="backColor" data-value="#FFD663" title="" data-toggle="button" tabindex="-1" data-original-title="#FFD663"></button><button type="button" class="note-color-btn" style="background-color:#94BD7B" data-event="backColor" data-value="#94BD7B" title="" data-toggle="button" tabindex="-1" data-original-title="#94BD7B"></button><button type="button" class="note-color-btn" style="background-color:#73A5AD" data-event="backColor" data-value="#73A5AD" title="" data-toggle="button" tabindex="-1" data-original-title="#73A5AD"></button><button type="button" class="note-color-btn" style="background-color:#6BADDE" data-event="backColor" data-value="#6BADDE" title="" data-toggle="button" tabindex="-1" data-original-title="#6BADDE"></button><button type="button" class="note-color-btn" style="background-color:#8C7BC6" data-event="backColor" data-value="#8C7BC6" title="" data-toggle="button" tabindex="-1" data-original-title="#8C7BC6"></button><button type="button" class="note-color-btn" style="background-color:#C67BA5" data-event="backColor" data-value="#C67BA5" title="" data-toggle="button" tabindex="-1" data-original-title="#C67BA5"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#CE0000" data-event="backColor" data-value="#CE0000" title="" data-toggle="button" tabindex="-1" data-original-title="#CE0000"></button><button type="button" class="note-color-btn" style="background-color:#E79439" data-event="backColor" data-value="#E79439" title="" data-toggle="button" tabindex="-1" data-original-title="#E79439"></button><button type="button" class="note-color-btn" style="background-color:#EFC631" data-event="backColor" data-value="#EFC631" title="" data-toggle="button" tabindex="-1" data-original-title="#EFC631"></button><button type="button" class="note-color-btn" style="background-color:#6BA54A" data-event="backColor" data-value="#6BA54A" title="" data-toggle="button" tabindex="-1" data-original-title="#6BA54A"></button><button type="button" class="note-color-btn" style="background-color:#4A7B8C" data-event="backColor" data-value="#4A7B8C" title="" data-toggle="button" tabindex="-1" data-original-title="#4A7B8C"></button><button type="button" class="note-color-btn" style="background-color:#3984C6" data-event="backColor" data-value="#3984C6" title="" data-toggle="button" tabindex="-1" data-original-title="#3984C6"></button><button type="button" class="note-color-btn" style="background-color:#634AA5" data-event="backColor" data-value="#634AA5" title="" data-toggle="button" tabindex="-1" data-original-title="#634AA5"></button><button type="button" class="note-color-btn" style="background-color:#A54A7B" data-event="backColor" data-value="#A54A7B" title="" data-toggle="button" tabindex="-1" data-original-title="#A54A7B"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#9C0000" data-event="backColor" data-value="#9C0000" title="" data-toggle="button" tabindex="-1" data-original-title="#9C0000"></button><button type="button" class="note-color-btn" style="background-color:#B56308" data-event="backColor" data-value="#B56308" title="" data-toggle="button" tabindex="-1" data-original-title="#B56308"></button><button type="button" class="note-color-btn" style="background-color:#BD9400" data-event="backColor" data-value="#BD9400" title="" data-toggle="button" tabindex="-1" data-original-title="#BD9400"></button><button type="button" class="note-color-btn" style="background-color:#397B21" data-event="backColor" data-value="#397B21" title="" data-toggle="button" tabindex="-1" data-original-title="#397B21"></button><button type="button" class="note-color-btn" style="background-color:#104A5A" data-event="backColor" data-value="#104A5A" title="" data-toggle="button" tabindex="-1" data-original-title="#104A5A"></button><button type="button" class="note-color-btn" style="background-color:#085294" data-event="backColor" data-value="#085294" title="" data-toggle="button" tabindex="-1" data-original-title="#085294"></button><button type="button" class="note-color-btn" style="background-color:#311873" data-event="backColor" data-value="#311873" title="" data-toggle="button" tabindex="-1" data-original-title="#311873"></button><button type="button" class="note-color-btn" style="background-color:#731842" data-event="backColor" data-value="#731842" title="" data-toggle="button" tabindex="-1" data-original-title="#731842"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#630000" data-event="backColor" data-value="#630000" title="" data-toggle="button" tabindex="-1" data-original-title="#630000"></button><button type="button" class="note-color-btn" style="background-color:#7B3900" data-event="backColor" data-value="#7B3900" title="" data-toggle="button" tabindex="-1" data-original-title="#7B3900"></button><button type="button" class="note-color-btn" style="background-color:#846300" data-event="backColor" data-value="#846300" title="" data-toggle="button" tabindex="-1" data-original-title="#846300"></button><button type="button" class="note-color-btn" style="background-color:#295218" data-event="backColor" data-value="#295218" title="" data-toggle="button" tabindex="-1" data-original-title="#295218"></button><button type="button" class="note-color-btn" style="background-color:#083139" data-event="backColor" data-value="#083139" title="" data-toggle="button" tabindex="-1" data-original-title="#083139"></button><button type="button" class="note-color-btn" style="background-color:#003163" data-event="backColor" data-value="#003163" title="" data-toggle="button" tabindex="-1" data-original-title="#003163"></button><button type="button" class="note-color-btn" style="background-color:#21104A" data-event="backColor" data-value="#21104A" title="" data-toggle="button" tabindex="-1" data-original-title="#21104A"></button><button type="button" class="note-color-btn" style="background-color:#4A1031" data-event="backColor" data-value="#4A1031" title="" data-toggle="button" tabindex="-1" data-original-title="#4A1031"></button></div></div></div></div><div class="note-palette">  <div class="note-palette-title">前景</div>  <div>    <button type="button" class="note-color-reset btn btn-light" data-event="removeFormat" data-value="foreColor">默认    </button>  </div>  <div class="note-holder" data-event="foreColor"><div class="note-color-palette"><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#000000" data-event="foreColor" data-value="#000000" title="" data-toggle="button" tabindex="-1" data-original-title="#000000"></button><button type="button" class="note-color-btn" style="background-color:#424242" data-event="foreColor" data-value="#424242" title="" data-toggle="button" tabindex="-1" data-original-title="#424242"></button><button type="button" class="note-color-btn" style="background-color:#636363" data-event="foreColor" data-value="#636363" title="" data-toggle="button" tabindex="-1" data-original-title="#636363"></button><button type="button" class="note-color-btn" style="background-color:#9C9C94" data-event="foreColor" data-value="#9C9C94" title="" data-toggle="button" tabindex="-1" data-original-title="#9C9C94"></button><button type="button" class="note-color-btn" style="background-color:#CEC6CE" data-event="foreColor" data-value="#CEC6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#CEC6CE"></button><button type="button" class="note-color-btn" style="background-color:#EFEFEF" data-event="foreColor" data-value="#EFEFEF" title="" data-toggle="button" tabindex="-1" data-original-title="#EFEFEF"></button><button type="button" class="note-color-btn" style="background-color:#F7F7F7" data-event="foreColor" data-value="#F7F7F7" title="" data-toggle="button" tabindex="-1" data-original-title="#F7F7F7"></button><button type="button" class="note-color-btn" style="background-color:#FFFFFF" data-event="foreColor" data-value="#FFFFFF" title="" data-toggle="button" tabindex="-1" data-original-title="#FFFFFF"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#FF0000" data-event="foreColor" data-value="#FF0000" title="" data-toggle="button" tabindex="-1" data-original-title="#FF0000"></button><button type="button" class="note-color-btn" style="background-color:#FF9C00" data-event="foreColor" data-value="#FF9C00" title="" data-toggle="button" tabindex="-1" data-original-title="#FF9C00"></button><button type="button" class="note-color-btn" style="background-color:#FFFF00" data-event="foreColor" data-value="#FFFF00" title="" data-toggle="button" tabindex="-1" data-original-title="#FFFF00"></button><button type="button" class="note-color-btn" style="background-color:#00FF00" data-event="foreColor" data-value="#00FF00" title="" data-toggle="button" tabindex="-1" data-original-title="#00FF00"></button><button type="button" class="note-color-btn" style="background-color:#00FFFF" data-event="foreColor" data-value="#00FFFF" title="" data-toggle="button" tabindex="-1" data-original-title="#00FFFF"></button><button type="button" class="note-color-btn" style="background-color:#0000FF" data-event="foreColor" data-value="#0000FF" title="" data-toggle="button" tabindex="-1" data-original-title="#0000FF"></button><button type="button" class="note-color-btn" style="background-color:#9C00FF" data-event="foreColor" data-value="#9C00FF" title="" data-toggle="button" tabindex="-1" data-original-title="#9C00FF"></button><button type="button" class="note-color-btn" style="background-color:#FF00FF" data-event="foreColor" data-value="#FF00FF" title="" data-toggle="button" tabindex="-1" data-original-title="#FF00FF"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#F7C6CE" data-event="foreColor" data-value="#F7C6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#F7C6CE"></button><button type="button" class="note-color-btn" style="background-color:#FFE7CE" data-event="foreColor" data-value="#FFE7CE" title="" data-toggle="button" tabindex="-1" data-original-title="#FFE7CE"></button><button type="button" class="note-color-btn" style="background-color:#FFEFC6" data-event="foreColor" data-value="#FFEFC6" title="" data-toggle="button" tabindex="-1" data-original-title="#FFEFC6"></button><button type="button" class="note-color-btn" style="background-color:#D6EFD6" data-event="foreColor" data-value="#D6EFD6" title="" data-toggle="button" tabindex="-1" data-original-title="#D6EFD6"></button><button type="button" class="note-color-btn" style="background-color:#CEDEE7" data-event="foreColor" data-value="#CEDEE7" title="" data-toggle="button" tabindex="-1" data-original-title="#CEDEE7"></button><button type="button" class="note-color-btn" style="background-color:#CEE7F7" data-event="foreColor" data-value="#CEE7F7" title="" data-toggle="button" tabindex="-1" data-original-title="#CEE7F7"></button><button type="button" class="note-color-btn" style="background-color:#D6D6E7" data-event="foreColor" data-value="#D6D6E7" title="" data-toggle="button" tabindex="-1" data-original-title="#D6D6E7"></button><button type="button" class="note-color-btn" style="background-color:#E7D6DE" data-event="foreColor" data-value="#E7D6DE" title="" data-toggle="button" tabindex="-1" data-original-title="#E7D6DE"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#E79C9C" data-event="foreColor" data-value="#E79C9C" title="" data-toggle="button" tabindex="-1" data-original-title="#E79C9C"></button><button type="button" class="note-color-btn" style="background-color:#FFC69C" data-event="foreColor" data-value="#FFC69C" title="" data-toggle="button" tabindex="-1" data-original-title="#FFC69C"></button><button type="button" class="note-color-btn" style="background-color:#FFE79C" data-event="foreColor" data-value="#FFE79C" title="" data-toggle="button" tabindex="-1" data-original-title="#FFE79C"></button><button type="button" class="note-color-btn" style="background-color:#B5D6A5" data-event="foreColor" data-value="#B5D6A5" title="" data-toggle="button" tabindex="-1" data-original-title="#B5D6A5"></button><button type="button" class="note-color-btn" style="background-color:#A5C6CE" data-event="foreColor" data-value="#A5C6CE" title="" data-toggle="button" tabindex="-1" data-original-title="#A5C6CE"></button><button type="button" class="note-color-btn" style="background-color:#9CC6EF" data-event="foreColor" data-value="#9CC6EF" title="" data-toggle="button" tabindex="-1" data-original-title="#9CC6EF"></button><button type="button" class="note-color-btn" style="background-color:#B5A5D6" data-event="foreColor" data-value="#B5A5D6" title="" data-toggle="button" tabindex="-1" data-original-title="#B5A5D6"></button><button type="button" class="note-color-btn" style="background-color:#D6A5BD" data-event="foreColor" data-value="#D6A5BD" title="" data-toggle="button" tabindex="-1" data-original-title="#D6A5BD"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#E76363" data-event="foreColor" data-value="#E76363" title="" data-toggle="button" tabindex="-1" data-original-title="#E76363"></button><button type="button" class="note-color-btn" style="background-color:#F7AD6B" data-event="foreColor" data-value="#F7AD6B" title="" data-toggle="button" tabindex="-1" data-original-title="#F7AD6B"></button><button type="button" class="note-color-btn" style="background-color:#FFD663" data-event="foreColor" data-value="#FFD663" title="" data-toggle="button" tabindex="-1" data-original-title="#FFD663"></button><button type="button" class="note-color-btn" style="background-color:#94BD7B" data-event="foreColor" data-value="#94BD7B" title="" data-toggle="button" tabindex="-1" data-original-title="#94BD7B"></button><button type="button" class="note-color-btn" style="background-color:#73A5AD" data-event="foreColor" data-value="#73A5AD" title="" data-toggle="button" tabindex="-1" data-original-title="#73A5AD"></button><button type="button" class="note-color-btn" style="background-color:#6BADDE" data-event="foreColor" data-value="#6BADDE" title="" data-toggle="button" tabindex="-1" data-original-title="#6BADDE"></button><button type="button" class="note-color-btn" style="background-color:#8C7BC6" data-event="foreColor" data-value="#8C7BC6" title="" data-toggle="button" tabindex="-1" data-original-title="#8C7BC6"></button><button type="button" class="note-color-btn" style="background-color:#C67BA5" data-event="foreColor" data-value="#C67BA5" title="" data-toggle="button" tabindex="-1" data-original-title="#C67BA5"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#CE0000" data-event="foreColor" data-value="#CE0000" title="" data-toggle="button" tabindex="-1" data-original-title="#CE0000"></button><button type="button" class="note-color-btn" style="background-color:#E79439" data-event="foreColor" data-value="#E79439" title="" data-toggle="button" tabindex="-1" data-original-title="#E79439"></button><button type="button" class="note-color-btn" style="background-color:#EFC631" data-event="foreColor" data-value="#EFC631" title="" data-toggle="button" tabindex="-1" data-original-title="#EFC631"></button><button type="button" class="note-color-btn" style="background-color:#6BA54A" data-event="foreColor" data-value="#6BA54A" title="" data-toggle="button" tabindex="-1" data-original-title="#6BA54A"></button><button type="button" class="note-color-btn" style="background-color:#4A7B8C" data-event="foreColor" data-value="#4A7B8C" title="" data-toggle="button" tabindex="-1" data-original-title="#4A7B8C"></button><button type="button" class="note-color-btn" style="background-color:#3984C6" data-event="foreColor" data-value="#3984C6" title="" data-toggle="button" tabindex="-1" data-original-title="#3984C6"></button><button type="button" class="note-color-btn" style="background-color:#634AA5" data-event="foreColor" data-value="#634AA5" title="" data-toggle="button" tabindex="-1" data-original-title="#634AA5"></button><button type="button" class="note-color-btn" style="background-color:#A54A7B" data-event="foreColor" data-value="#A54A7B" title="" data-toggle="button" tabindex="-1" data-original-title="#A54A7B"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#9C0000" data-event="foreColor" data-value="#9C0000" title="" data-toggle="button" tabindex="-1" data-original-title="#9C0000"></button><button type="button" class="note-color-btn" style="background-color:#B56308" data-event="foreColor" data-value="#B56308" title="" data-toggle="button" tabindex="-1" data-original-title="#B56308"></button><button type="button" class="note-color-btn" style="background-color:#BD9400" data-event="foreColor" data-value="#BD9400" title="" data-toggle="button" tabindex="-1" data-original-title="#BD9400"></button><button type="button" class="note-color-btn" style="background-color:#397B21" data-event="foreColor" data-value="#397B21" title="" data-toggle="button" tabindex="-1" data-original-title="#397B21"></button><button type="button" class="note-color-btn" style="background-color:#104A5A" data-event="foreColor" data-value="#104A5A" title="" data-toggle="button" tabindex="-1" data-original-title="#104A5A"></button><button type="button" class="note-color-btn" style="background-color:#085294" data-event="foreColor" data-value="#085294" title="" data-toggle="button" tabindex="-1" data-original-title="#085294"></button><button type="button" class="note-color-btn" style="background-color:#311873" data-event="foreColor" data-value="#311873" title="" data-toggle="button" tabindex="-1" data-original-title="#311873"></button><button type="button" class="note-color-btn" style="background-color:#731842" data-event="foreColor" data-value="#731842" title="" data-toggle="button" tabindex="-1" data-original-title="#731842"></button></div><div class="note-color-row"><button type="button" class="note-color-btn" style="background-color:#630000" data-event="foreColor" data-value="#630000" title="" data-toggle="button" tabindex="-1" data-original-title="#630000"></button><button type="button" class="note-color-btn" style="background-color:#7B3900" data-event="foreColor" data-value="#7B3900" title="" data-toggle="button" tabindex="-1" data-original-title="#7B3900"></button><button type="button" class="note-color-btn" style="background-color:#846300" data-event="foreColor" data-value="#846300" title="" data-toggle="button" tabindex="-1" data-original-title="#846300"></button><button type="button" class="note-color-btn" style="background-color:#295218" data-event="foreColor" data-value="#295218" title="" data-toggle="button" tabindex="-1" data-original-title="#295218"></button><button type="button" class="note-color-btn" style="background-color:#083139" data-event="foreColor" data-value="#083139" title="" data-toggle="button" tabindex="-1" data-original-title="#083139"></button><button type="button" class="note-color-btn" style="background-color:#003163" data-event="foreColor" data-value="#003163" title="" data-toggle="button" tabindex="-1" data-original-title="#003163"></button><button type="button" class="note-color-btn" style="background-color:#21104A" data-event="foreColor" data-value="#21104A" title="" data-toggle="button" tabindex="-1" data-original-title="#21104A"></button><button type="button" class="note-color-btn" style="background-color:#4A1031" data-event="foreColor" data-value="#4A1031" title="" data-toggle="button" tabindex="-1" data-original-title="#4A1031"></button></div></div></div></div></div></div></div><div class="note-btn-group btn-group note-para"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="无序列表 (CTRL+SHIFT+NUM7)"><i class="note-icon-unorderedlist"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="有序列表 (CTRL+SHIFT+NUM8)"><i class="note-icon-orderedlist"></i></button><div class="note-btn-group btn-group"><button type="button" class="note-btn btn btn-light btn-sm dropdown-toggle" tabindex="-1" data-toggle="dropdown" title="" data-original-title="段落"><i class="note-icon-align-left"></i></button><div class="dropdown-menu"><div class="note-btn-group btn-group note-align"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="左对齐 (CTRL+SHIFT+L)"><i class="note-icon-align-left"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="居中对齐 (CTRL+SHIFT+E)"><i class="note-icon-align-center"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="右对齐 (CTRL+SHIFT+R)"><i class="note-icon-align-right"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="两端对齐 (CTRL+SHIFT+J)"><i class="note-icon-align-justify"></i></button></div><div class="note-btn-group btn-group note-list"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="减少缩进 (CTRL+[)"><i class="note-icon-align-outdent"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="增加缩进 (CTRL+])"><i class="note-icon-align-indent"></i></button></div></div></div></div><div class="note-btn-group btn-group note-height"><div class="note-btn-group btn-group"><button type="button" class="note-btn btn btn-light btn-sm dropdown-toggle" tabindex="-1" data-toggle="dropdown" title="" data-original-title="行高"><i class="note-icon-text-height"></i></button><div class="dropdown-menu note-check dropdown-line-height"><a class="dropdown-item" href="#" data-value="1.0"><i class="note-icon-menu-check"></i> 1.0</a><a class="dropdown-item" href="#" data-value="1.2"><i class="note-icon-menu-check"></i> 1.2</a><a class="dropdown-item" href="#" data-value="1.4"><i class="note-icon-menu-check"></i> 1.4</a><a class="dropdown-item" href="#" data-value="1.5"><i class="note-icon-menu-check"></i> 1.5</a><a class="dropdown-item" href="#" data-value="1.6"><i class="note-icon-menu-check"></i> 1.6</a><a class="dropdown-item" href="#" data-value="1.8"><i class="note-icon-menu-check"></i> 1.8</a><a class="dropdown-item" href="#" data-value="2.0"><i class="note-icon-menu-check"></i> 2.0</a><a class="dropdown-item" href="#" data-value="3.0"><i class="note-icon-menu-check"></i> 3.0</a></div></div></div><div class="note-btn-group btn-group note-insert"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="链接 (CTRL+K)"><i class="note-icon-link"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="图片"><i class="note-icon-picture"></i></button></div><div class="note-btn-group btn-group note-view"><button type="button" class="note-btn btn btn-light btn-sm btn-fullscreen" tabindex="-1" title="" data-original-title="全屏"><i class="note-icon-arrows-alt"></i></button></div></div><div class="note-editing-area"><div class="note-handle"><div class="note-control-selection"><div class="note-control-selection-bg"></div><div class="note-control-holder note-control-nw"></div><div class="note-control-holder note-control-ne"></div><div class="note-control-holder note-control-sw"></div><div class="note-control-sizing note-control-se"></div><div class="note-control-selection-info"></div></div></div><textarea class="note-codable"></textarea><div class="note-editable card-block" contenteditable="true" style="height: 400px;"><p><br /></p></div></div><div class="note-statusbar">  <div class="note-resizebar">    <div class="note-icon-bar"></div>    <div class="note-icon-bar"></div>    <div class="note-icon-bar"></div>  </div></div><div class="modal link-dialog" aria-hidden="false" tabindex="-1"><div class="modal-dialog">  <div class="modal-content">    <div class="modal-header">      <h4 class="modal-title">插入链接</h4>      <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>    </div>    <div class="modal-body"><div class="form-group note-form-group"><label class="note-form-label">显示文本</label><input class="note-link-text form-control  note-form-control  note-input" type="text" /></div><div class="form-group note-form-group"><label class="note-form-label">链接地址</label><input class="note-link-url form-control note-form-control note-input" type="text" value="http://" /></div><label class="custom-control custom-checkbox" for="sn-checkbox-open-in-new-window"> <input type="checkbox" class="custom-control-input" id="sn-checkbox-open-in-new-window" checked="" /> <span class="custom-control-indicator"></span> <span class="custom-control-description">在新窗口打开</span></label></div>    <div class="modal-footer"><button href="#" class="btn btn-primary note-btn note-btn-primary note-link-btn disabled" disabled="">插入链接</button></div>  </div></div></div><div class="modal" aria-hidden="false" tabindex="-1"><div class="modal-dialog">  <div class="modal-content">    <div class="modal-header">      <h4 class="modal-title">插入图片</h4>      <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>    </div>    <div class="modal-body"><div class="form-group note-form-group note-group-select-from-files"><label class="note-form-label">从本地上传</label><input class="note-image-input form-control note-form-control note-input" type="file" name="files" accept="image/*" multiple="multiple" /></div><div class="form-group note-group-image-url" style="overflow:auto;"><label class="note-form-label">图片地址</label><input class="note-image-url form-control note-form-control note-input  col-md-12" type="text" /></div></div>    <div class="modal-footer"><button href="#" class="btn btn-primary note-btn note-btn-primary note-image-btn disabled" disabled="">插入图片</button></div>  </div></div></div><div class="modal" aria-hidden="false" tabindex="-1"><div class="modal-dialog">  <div class="modal-content">    <div class="modal-header">      <h4 class="modal-title">插入视频</h4>      <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>    </div>    <div class="modal-body"><div class="form-group note-form-group row-fluid"><label class="note-form-label">视频地址 <small class="text-muted">(优酷, 腾讯, Instagram, DailyMotion, Youtube等)</small></label><input class="note-video-url form-control  note-form-control note-input span12" type="text" /></div></div>    <div class="modal-footer"><button href="#" class="btn btn-primary note-btn note-btn-primary  note-video-btn disabled" disabled="">插入视频</button></div>  </div></div></div><div class="modal" aria-hidden="false" tabindex="-1"><div class="modal-dialog">  <div class="modal-content">    <div class="modal-header">      <h4 class="modal-title">帮助</h4>      <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>    </div>    <div class="modal-body" style="max-height: 300px; overflow: scroll;"><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>ENTER</kbd></label><span>插入段落</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+Z</kbd></label><span>撤销</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+Y</kbd></label><span>重做</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>TAB</kbd></label><span>增加缩进</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>SHIFT+TAB</kbd></label><span>减少缩进</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+B</kbd></label><span>粗体</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+I</kbd></label><span>斜体</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+U</kbd></label><span>下划线</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+S</kbd></label><span>删除线</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+BACKSLASH</kbd></label><span>清除格式</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+L</kbd></label><span>左对齐</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+E</kbd></label><span>居中对齐</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+R</kbd></label><span>右对齐</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+J</kbd></label><span>两端对齐</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+NUM7</kbd></label><span>无序列表</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+SHIFT+NUM8</kbd></label><span>有序列表</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+LEFTBRACKET</kbd></label><span>减少缩进</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+RIGHTBRACKET</kbd></label><span>增加缩进</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM0</kbd></label><span>设置选中内容样式为 普通</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM1</kbd></label><span>设置选中内容样式为 标题1</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM2</kbd></label><span>设置选中内容样式为 标题2</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM3</kbd></label><span>设置选中内容样式为 标题3</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM4</kbd></label><span>设置选中内容样式为 标题4</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM5</kbd></label><span>设置选中内容样式为 标题5</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+NUM6</kbd></label><span>设置选中内容样式为 标题6</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+ENTER</kbd></label><span>插入水平线</span><div class="help-list-item"></div><label style="width: 180px; margin-right: 10px;"><kbd>CTRL+K</kbd></label><span>显示链接对话框</span></div>    <div class="modal-footer"><p class="text-center"><a href="http://summernote.org/" target="_blank">Summernote 0.8.8</a> · <a href="https://github.com/summernote/summernote" target="_blank">Project</a> · <a href="https://github.com/summernote/summernote/issues" target="_blank">Issues</a></p></div>  </div></div></div><div class="modal ext-highlight" aria-hidden="false" tabindex="-1"><div class="modal-dialog">  <div class="modal-content">    <div class="modal-body"><div class="form-group"><label>选择语言</label><select class="form-control ext-highlight-select"><option value="python">python</option><option value="java">java</option><option value="R">R</option><option value="scala">scala</option></select></div><div class="form-group"><label>输入您的代码</label><textarea class="ext-highlight-code form-control" rows="10"></textarea></div></div>    <div class="modal-footer"><button href="#" class="btn btn-primary ext-highlight-btn disabled" disabled="">插入代码</button></div>  </div></div></div></div>
      <br />
      <!--<p>
        <i class="fa fa-picture-o green"></i> 插入图片：
        <input type="file" name="image[]" multiple><br>
      </p>-->
      <button class="btn btn-primary m-t" id="main_reply_submit_btn"><i class="fa fa-paper-plane"></i> 发表回答</button>
    </form>
  <br /><br />
  </div>

    <div class="col-md-3">
   <p><span style="color:#a36700"></span><span style="color:#666666;font-size:18px"><img src="interviews/images/thinking.png" style="width:40px" />  相关讨论</span><span style="color:#f7724a"></span></p>
    <span style="font-size: 16px"><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1000854" class="link_green">二分法K Means的算法是什么？和普通的K Means有什么区别？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1003199" class="link_green">为什么K Means算法对样本的输入顺序比较敏感？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1003353" class="link_green">关于online KMeans步骤中成员更新分类的问题？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1001749" class="link_green">k-medoids和k-means区别</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1003172" class="link_green">K-Means实现mini-batch online learning的原理是什么？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1007554" class="link_green">kmeans可以做并行化计算达到加速效果吗？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1001229" class="link_green">关于小批量K均值（mini-batch K Means）的问题</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1002081" class="link_green">Jenks和K Means在一维数据时，是不是等价的？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1022027" class="link_green">kmeans可以用在三维数据上吗？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1001391" class="link_green">特征归一化对K Means有影响吗？</a></p></span>
   <p><span style="color:#a36700"></span><span style="color:#666666;font-size:18px"><img src="interviews/images/reading.jpg" style="width:65px" />  随便看看</span><span style="color:#f7724a"></span></p>
    <span style="font-size: 16px"><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1005562" class="link_green">怎么提取pandas dataframe中某一列每个字符串的前n个字符？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1002631" class="link_green">sklearn训练classifier的时候报错Unknown label type</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1001530" class="link_green">两个凸函数相加，还是凸函数吗？</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1000254" class="link_green">Python计算两个数组的相关系数</a></p><p style="word-break: break-all;"><a href="forum_main_post.php?postid=1000702" class="link_green">修正R方(adjusted R square)是什么？</a></p></span>
  </div>
  
</div>


<script type="text/javascript" src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@1/component_footer.js"></script><style>
.footer_row{
	background-color: #F6F7F9;
	&lt;!--border-top:3px solid #606060;&gt;}
.footer_links{
        font-size:0.9rem;
        color:#004868;}
.footer_links:hover{
        color:#138F77;}
</style>
<div class="row m-a-0 footer_row"><div class="container p-t-0"><div class="row m-a-0 p-t"><div class="col-md-3"></div><div class="col-md-1"><a href="page_about.php" style="text-decoration: none"><span style="font-size:0.7rem;color:#8ECCB5;"><i class="fa fa-puzzle-piece" aria-hidden="true"></i> 关于我们</span></a></div><div class="col-md-1"><a href="page_faq.php" style="text-decoration: none"><span style="font-size:0.7rem;color:#8ECCB5;"><i class="fa fa-comments" aria-hidden="true"></i> 常见问题</span></a></div><div class="col-md-2"><a href="index.php"><img src="assets/images/green_sofa_footer.png" style="width:80%" /></a></div><div class="col-md-1"><a href="page_terms.php" style="text-decoration: none"> <span style="font-size:0.7rem;color:#8ECCB5;"><i class="fa fa-cc" aria-hidden="true"></i> 内容许可</span></a></div><div class="col-md-1"><a href="page_feedback.php" style="text-decoration: none"><span style="font-size:0.7rem;color:#8ECCB5;"><i class="fa fa-headphones" aria-hidden="true"></i> 聆听反馈</span></a></div><div class="col-md-3"></div></div><div class="row text-center m-t" style="font-size:0.7rem;color:#8ECCB5;">			© <span id="thisyear">2022</span> SofaSofa.io 版权所有. <a class="footer_links" href="http://www.miitbeian.gov.cn/" style="font-size:0.7rem;color:#8ECCB5;">苏ICP备16005786号-2</a><br /><br /></div></div></div><script>
document.getElementById('thisyear').innerHTML = (new Date()).getFullYear();
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://sofasofa.io/assets/js/httpsSubmit.js';}
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(bp, s);})();</script>

<div id="debug"></div>
<script type="text/javascript" src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@0/highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
<script type="text/javascript" src="http://sofasofa.io/assets/cdn/gh/SofaSofa-ML/JS_SofaSofa@1/main_post.js"> </script>



<div class="note-popover popover in note-link-popover bottom">  <div class="arrow"></div>  <div class="popover-content note-children-container"><span><a target="_blank"></a> </span><div class="note-btn-group btn-group note-link"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="编辑链接"><i class="note-icon-link"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="去除链接"><i class="note-icon-chain-broken"></i></button></div></div></div><div class="note-popover popover in note-image-popover bottom">  <div class="arrow"></div>  <div class="popover-content note-children-container"><div class="note-btn-group btn-group note-imagesize"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="缩放至 100%"><span class="note-fontsize-10">100%</span></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="缩放至 50%"><span class="note-fontsize-10">50%</span></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="缩放至 25%"><span class="note-fontsize-10">25%</span></button></div><div class="note-btn-group btn-group note-float"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="靠左浮动"><i class="note-icon-align-left"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="靠右浮动"><i class="note-icon-align-right"></i></button><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="取消浮动"><i class="note-icon-align-justify"></i></button></div><div class="note-btn-group btn-group note-remove"><button type="button" class="note-btn btn btn-light btn-sm" tabindex="-1" title="" data-original-title="移除图片"><i class="note-icon-trash"></i></button></div></div></div><div class="note-popover popover in note-table-popover bottom">  <div class="arrow"></div>  <div class="popover-content note-children-container"><div class="note-btn-group btn-group note-add"><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Add row below"><i class="note-icon-row-below"></i></button><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Add row above"><i class="note-icon-row-above"></i></button><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Add column left"><i class="note-icon-col-before"></i></button><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Add column right"><i class="note-icon-col-after"></i></button></div><div class="note-btn-group btn-group note-delete"><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Delete row"><i class="note-icon-row-remove"></i></button><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Delete column"><i class="note-icon-col-remove"></i></button><button type="button" class="note-btn btn btn-light btn-sm btn-md" tabindex="-1" title="" data-original-title="Delete table"><i class="note-icon-trash"></i></button></div></div></div><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-family: MathJax_Size2, sans-serif;"></div></div></body></html>