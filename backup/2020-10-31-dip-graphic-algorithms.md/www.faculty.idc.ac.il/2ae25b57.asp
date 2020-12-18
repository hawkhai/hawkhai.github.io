<html xmlns="http://www.w3.org/1999/xhtml"><head>
<script type="text/javascript">
(function(){
window["loaderConfig"] = "/TSPD/?type=21";
})();

</script>

<script type="text/javascript" src="/TSPD/?type=18"></script>

    <link rel="stylesheet" type="text/css" href="styles/layout.css" />
    <link rel="stylesheet" type="text/css" href="styles/main.css" />
    <link rel="stylesheet" type="text/css" href="styles/misc.css" />
    <link rel="apple-touch-icon" href="apple-touch-icon.png" />
    <!--[if IE]>
    <link rel="stylesheet" type="text/css" href="styles/ie-fix.css" />
    <![endif]-->
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
    <!--[if !IE]>-->
    <link media="only screen and (max-device-width: 480px)" href="styles/iPhone.css" type="text/css" rel="stylesheet" />
    <!--<![endif]-->
    <script src="scripts/jquery.js" type="text/javascript"></script>
    <script src="scripts/jquery-color.js" type="text/javascript"></script>
    <script src="scripts/menu.js" type="text/javascript"></script>

    <script src="scripts/seam-carve.js"></script>

    <title>
	Ariel Shamir's Homepage
    </title>
</head>

<body>
<div id="main">
    <div id="header">
	<a href="index.asp">
	    <img src="images/layout/logo.jpg" alt="Ariel Shamir" id="logo" />
	</a>
	
	<table id="menu">
	    <tbody><tr>
		<td>
		    <a href="index.asp" class="menu" id="home">
			<div class="menu-fix" onclick="location.href='index.asp';">
			    <img src="images/layout/home-ovr.jpg" class="menu-ovr" style="opacity: 0;" />
			</div>
			Home
		    </a>
		</td>

		<td>
		    <a href="research.asp" class="menu" id="research">
			<div class="menu-fix" onclick="location.href='research.asp';">
			    <img src="images/layout/research-ovr.jpg" class="menu-ovr" style="opacity: 0;" />
			</div>
			Research
		    </a>
		</td>

		<td>
		    <a href="teaching.asp" class="menu" id="teaching">
			<div class="menu-fix" onclick="location.href='teaching.asp';">
			    <img src="images/layout/teaching-ovr.jpg" class="menu-ovr" style="opacity: 0;" />
			</div>
			Teaching
		    </a>
		</td>

		<td>
		    <a href="industry.asp" class="menu" id="industry">
			<div class="menu-fix" onclick="location.href='industry.asp';">
			    <img src="images/layout/industry-ovr.jpg" class="menu-ovr" style="opacity: 0;" />
			</div>
			Industry
		    </a>
		</td>

		<td>
		    <a href="others.asp" class="menu" id="others">
			<div class="menu-fix" onclick="location.href='others.asp';">
			    <img src="images/layout/others-ovr.jpg" class="menu-ovr" style="opacity: 0;" />
			</div>
			Others
		    </a>
		</td>
	    </tr>
	</tbody></table>
    </div>
    <div class="side-box"><div class="br"><div class="tl"><div class="tr">
	<h1>Categories</h1>
	<ul>
	    <li>
		<a href="subject-all.asp">All Publications</a>
	    </li>
	    <li>
		<a href="subject-shape-analysis.asp">Shape Analysis</a>
	    </li>
	    <li>
		<a href="subject-3D-modeling.asp">3D Modelling &amp; Fabrication</a>
	    </li>
	    <li>
		<a href="subject-image.asp">Image &amp; Video Processing</a>
	    </li>
	    <li>
		<a href="subject-animation.asp">Animation</a>
	    </li>
	    <li>
		<a href="subject-typography.asp">Art, Sketches &amp; Typography</a>
	    </li>
	    <li>
		<a href="subject-visual-info.asp">Information Visualization</a>
	    </li>
	    <li>
		<a href="subject-seam-carve.asp">Seam Carving</a>
	    </li>
	</ul>
    </div></div></div></div>


    <div id="content">
	<h1>Seam Carving for Content-Aware Image Resizing</h1>
	<p class="authors">
	    Presented at <img src="images/layout/sigg-07.jpg" class="text-logo" alt="Siggraph 2007" />
	    by <a href="http://www.shaiavidan.org/" target="_blank">Shai Avidan</a> and <a href="index.asp">Ariel Shamir</a>.
	</p>
	<a href="https://faculty.idc.ac.il/arik/SCWeb/imret/index.html" style="float:right">Project Page</a>
	<h2>Abstract</h2>
	<p>
	    Effective resizing of images should not only use geometric constraints, but consider the image content as well. We present a simple image operator called seam carving that supports content-aware image resizing for both reduction and expansion. A seam is an optimal 8-connected path of pixels on a single
	    image from top to bottom, or left to right, where optimality is defined by an image energy function. By repeatedly carving out or inserting seams in one direction we can change the aspect ratio of an image. By applying these operators in both directions we can retarget the image to a new size. The selection
	    and order of seams protect the content of the image, as defined by the energy function. Seam carving can also be used for image content enhancement and object removal. We support various visual saliency measures for defining the energy of an image, and can also include user input to guide the process. By
	    storing the order of seams in an image we create multi-size images, that are able to continuously change in real time to fit a given size.
	</p>
	
	<div class="video">
	    <object width="510" height="340">
		<param name="allowfullscreen" value="true" />
		<param name="allowscriptaccess" value="always" />
		<param name="movie" value="http://www.vimeo.com/moogaloop.swf?clip_id=1347424&amp;server=www.vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=3C477C&amp;fullscreen=1" />
		<embed src="http://www.vimeo.com/moogaloop.swf?clip_id=1347424&amp;server=www.vimeo.com&amp;show_title=0&amp;show_byline=0&amp;show_portrait=0&amp;color=3C477C&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="510" height="340" />
	    </object>
	</div>

	<!-- For iPhone -->
	<div id="video-replace"><div class="br"><div class="tl"><div class="tr">
	<br />
	    <a href="http://www.youtube.com/watch?v=6NcIJXTlugc" class="no-style">
		<h1>Watch video on YouTube</h1>
		<br />
		<img src="images/layout/YouTube-logo.png" alt="Watch on YouTube!" />
		<br /><br />
	    </a>
	</div></div></div></div>
	
	<!--
	<h2>Results</h2>
	<p>
	    Mouse over the method to see the result.
	    <br />
	    Aspect Ratio Change:
	</p>
	<div class="image">
	    <img src="images/research/seam-carve/christmas-original.jpg" id="christmas" class="image" />
	    <span class="controls" onmouseover="change('christmas','scale')" onmouseout="change('christmas','original')">SCALING</span>
	     &nbsp;&nbsp; 
	    <span class="controls" onmouseover="change('christmas','crop')" onmouseout="change('christmas','original')">CROPPING</span>
	     &nbsp;&nbsp; 
	    <span class="controls" onmouseover="change('christmas','seam')" onmouseout="change('christmas','original')">SEAM CARVING</span>
	</div>
	-->
	<br />

	<p>
	    <img src="images/layout/PDF.gif" class="file-icon" />
	    <a href="https://faculty.idc.ac.il/arik/SCWeb/imret/imret.pdf">The Paper (PDF)</a>
	      
	    <img src="images/layout/MOV.gif" class="file-icon" />
	    <a href="https://faculty.idc.ac.il/arik/SCWeb/imret/IMRet-All.mov">The Video (MOV)</a>
	</p>
	<br />
	<p class="small">
	* <strong>Acknowledgements:</strong> <br />
	We thank Eric Chan for the use of the waterfall image, and numerous
	flickr (http://www.flickr.com/) members for making
	their images available through creative common rights
	(http://creativecommons.org/): crazyegg95 (Buddha),
	Gustty (Couple and Surfers), JeffKubina (Capitol), mykaul (Hannuka
	and Car), o2ma (Vase), sigs66 (Long beach and Two people
	near sea).
	</p>
    </div>
    
    <div id="footer">
	<hr />
	<a href="site-map.asp">Site Map</a> | <a href="index.asp">Contact</a>
	<p class="subfooter">Designed By J.S. Best viewed at 1024 × 768 or higher.</p>
    </div>
</div>

<iframe name="TS_Injection" style="width: 0px; height: 0px; visibility: hidden; display: none;"></iframe></body></html>