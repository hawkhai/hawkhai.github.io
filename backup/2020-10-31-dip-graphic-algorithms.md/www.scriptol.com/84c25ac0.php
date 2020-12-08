<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name=viewport content="width=device-width, initial-scale=1">
<title>Removing an object on a photo with GIMP </title>
<link type="text/css" href="/scriptol.css" rel="stylesheet">
</head>
<style>
h3
{
	color:#666666;
	font-size:140%;
}
</style>
<body>

<div id="saat">
<script type="text/javascript">
window.google_analytics_uacct = "UA-6574971-2";
</script>
</div>
 
<div id="logo"> 
<div id="topmenu">
<span class="tentry"><a href="https://www.scriptol.com/design/" target="_top">Graphics</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/html5/" target="_top">HTML 5</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/javascript/" target="_top">JavaScript</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/programming/" target="_top">Programming</a></span>  
<span class="tentry"><a href="https://www.scriptol.com/scripts/" target="_top">Scripts</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/sql/" target="_top">SQL</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/svg/" target="_top">SVG</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/webmaster/" target="_top">Webmaster</a></span>
<span class="tentry"><a href="https://www.scriptol.com/software/" target="_top">Software</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/mobile/" target="_top">Mobiles</a></span> 
<span class="tentry"><a href="https://www.scriptol.com/how-to/" target="_top">How to</a></span>  
</div>

<div id="logoback"><a href="https://www.scriptol.com/"><img src="/scriptol.png" alt="Scriptol.com, programming techniques"></a></div>
<div id="dict" onclick="location.href='https://www.scriptol.com/dictionary.php'" title="Dictionary"><img src="/images/dict.png"></div>

</div><div id="menupanel">
<div class="menuhead"><a href="https://www.scriptol.com/design/gimp/" target="_top">GIMP</a></div>

<div class="menu">     
<div class="menulist">
 <a href="https://www.scriptol.com/design/gimp/blur-edge.php" target="_top">Blur contour</a><br>
 <a href="https://www.scriptol.com/design/gimp/superimpose.php" target="_top">Superimposing</a><br>
 <a href="https://www.scriptol.com/design/gimp/fading.php" target="_top">Faded merge</a><br>
 <a href="https://www.scriptol.com/design/gimp/removing-objects.php" target="_top">Removing object </a><br />
 <a href="https://www.scriptol.com/design/gimp/clipping.php" target="_top">Clipping</a><br>
 <a href="https://www.scriptol.com/design/gimp/logo.php" target="_top">Sketch to logo</a><br>
 <a href="https://www.scriptol.com/design/gimp/tutorials.php" target="_top">Tutorials</a></div>
</div>

<div class="menu">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:inline-block;width:180px;height:90px"
     data-ad-client="ca-pub-2681794164750401"
     data-ad-slot="5844506056"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>


</div>
<div id="content">
<h1>Removing an object on a photo with GIMP </h1>
  <p>Tutorial to remove objects (or people) and restore the portion of the background they hide in a photo with the  Resynthesizer plugin. </p>
  <p>With Photoshop, it is possible to delete objects in an image automatically, without any design work. You have just to select the object and use the command &quot;fill with the background&quot;. The same can be done with The Gimp in fact and for longer (it is not impossible that the same algorithm has been reused). </p>
  <p>This plugin &quot;re-synthesizes&quot; the background&quot; and rebuilds it from  same elements on the photo. It can thus reconstruct the sky, lawn, or even more complex views, from a sample taken from the image.</p>
  <p>First, see the <a href="https://www.scriptol.com/design/gimp/resynthesizer-tutorial.php" target="_top">Resynthesizer tutorial</a> to know the purpose of controls.</p>
  <p>We will put in practice the  commands using the same pictures that the Photoshop demonstration video.</p>
  <h2>Using Resynthesizer in Script-Fu </h2>
  <h3>1. Load an image</h3>
  <p><img src="https://www.scriptol.com/design/gimp/images/banc.jpg" width="421" height="295"></p>
  <h3>2. Select an area with the lasso</h3>
  <p>We want to remove the tree on the  top left. </p>
  <p><img src="https://www.scriptol.com/design/gimp/images/banc-select.png" width="420" height="295"></p>
  <h3>3. Click on Script-Fu -&gt; Enhance -&gt; Smart remove selection</h3>
  <p>This windows is opened. Select a radius and click on OK. </p>
  <p><img src="https://www.scriptol.com/design/gimp/images/resynth-smart-remove.jpg" width="393" height="192"></p>
  <h3>4.Here is the final image </h3>
  <p><img src="https://www.scriptol.com/design/gimp/images/banc-final.jpg" width="421" height="295"></p>
  <h2>Using the   Map -&gt; Resynthesize filter</h2>
  <p>To choose the sample that reconstructs the background, this command is necessary.</p>
  <h3>1. Load an image </h3>
  <p><img src="https://www.scriptol.com/design/gimp/images/road.jpg" width="606" height="162"></p>
  <h3>2. Select a sample </h3>
  <p><img src="https://www.scriptol.com/design/gimp/images/road-sample.jpg" width="266" height="69"></p>
  <p>Use the  Selection tool to delimit a part of the picture, we choose here a part on bottom right. <br>
  Then we made a cut and paste into a new image. There is no need to save it. </p>
  <h3>3. Select an item to delete</h3>
  <p>To remove the road, it is delimited with the lasso. </p>
  <p><img src="https://www.scriptol.com/design/gimp/images/road-capture.jpg" width="607" height="163"></p>
  <h3>4. Click on : Filter -&gt; Map -&gt; Resynthesize </h3>
  <p>This window is opened: </p>
  <p><img src="https://www.scriptol.com/design/gimp/images/resynth-filter-map.jpg" width="354" height="453"></p>
  <p>For the Texture source, we  use the  sample taken from the image. <br>
    It is also used to Input map. <br>
  For Output map, we use the original photo.</p>
  <h3>5. Here is the final image </h3>
  <p><img src="https://www.scriptol.com/design/gimp/images/road-final.jpg" width="606" height="162"></p>
  
  <em>Download</em>
  <ul class="la">
    <li><a href="http://www.logarithmic.net/pfh/resynthesizer" target="_top">Download the  Resynthesizer plugin</a>. <br>
      To install, simply unzip the file keeping the directory structure (if you download resynthesizer-for-Windows-0.13b.zip). </li>
    <li><a href="https://github.com/bootchk/resynthesizer" target="_top">Source code on  GitHub</a>. </li>
  </ul>
  
<div class="pub" id="ad76890">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-2681794164750401",
          enable_page_level_ads: true
     });
</script>
</div>

  <fieldset><legend>Color channels problem</legend>
  <p>In some cases, you can get the following error message:</p>
  <pre>The input and output maps must have the same number of color channels.</pre>
  <p>This is a message from the plugin and it is raised when the photo   you want to edit has a different internal format of the  image created by The Gimp for the sample.<br>
  To remove the message you must:</p>
  <ol>
    <li>Select the entire picture (ctrl-a).</li>
    <li>Copy (ctrl-c).</li>
    <li>Paste as a new  picture (shift-ctrl-v).</li>
  </ol>
  <p>Then,   work on the two images created by The Gimp, the copy of the photo  and the sample.</p>
  </fieldset>
  
    <table class="social">
  <tr>
  <td><a href="https://twitter.com/share" class="twitter-share-button" data-count="vertical">Tweet</a><script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>
  </td>
  <td><script src="http://www.stumbleupon.com/hostedbadge.php?s=5"></script></td>
   <td>
<g:plusone></g:plusone>
<script type="text/javascript" src="http://apis.google.com/js/plusone.js"></script></td>
 
  <td>
<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.scriptol.com%2Fdesign%2Fgimp%2Fremoving-objects.php&amp;send=false&amp;layout=button_count&amp;width=450&amp;show_faces=true&amp;action=like&amp;colorscheme=light&amp;font&amp;height=21" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:100px; height:21px;" allowTransparency="true"></iframe>
  </td>
  
  <td>
<script src="http://platform.linkedin.com/in.js" type="text/javascript"></script>
<script type="IN/Share" data-counter="top"></script>  
  </td>  
  
   </tr>
  </table>

<div id="disqus_thread"></div>
<script>
(function() { 
var d = document, s = d.createElement('script');
s.src = 'https://scriptol.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
                          

<div id="footer"> &copy; 2010-2012  <a href="https://www.scriptol.com/design/" target="_top">Scriptol.com</a></div>
    
</div>

<div id="sea">
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-6574971-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-6574971-2');
</script>

</div>

<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.css" />
<script src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.js"></script>
<script>
window.addEventListener("load", function(){
window.cookieconsent.initialise({
  "palette": {
    "popup": {
      "background": "#1d8a8a"
    },
    "button": {
      "background": "#62ffaa"
    }
  },
  "type": "opt-out",
  "content": {
    "message": "Cookies are used on this site only by publishers to make ads relevants.",
    "dismiss": "Ignore",
    "deny": "Refuse"
  }  
})});
</script>
</body>
</html>
