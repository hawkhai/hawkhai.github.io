<html xmlns="http://www.w3.org/1999/xhtml"><head><meta name="keywords" content="HDOJ ACM ICPC OJ C C++ Pascal Java" /><meta http-equiv="Content-Type" content="text/html;charset=gb2312" /><link rel="stylesheet" type="text/css" href="/images/global.css" media="all" /><link rel="stylesheet" type="text/css" href="/css/diyinhead.css" media="all" /><link rel="stylesheet" type="text/css" href="/css/webinhead.css" media="all" /><script src="/js/global.js" type="text/javascript"></script><script src="/js/register.js" type="text/javascript"></script><script src="/js/MathJax/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script><title>Problem - 2896</title><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Hover_Arrow {position: absolute; width: 15px; height: 11px; cursor: pointer}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; color: #666666}
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
.MathJax_Menu_Close {position: absolute; width: 31px; height: 31px; top: -15px; left: -15px}
</style></head><body><div id="MathJax_Message" style="display: none;"></div>
<a name="top"></a>
<table align="center" cellspacing="0" cellpadding="0" width="980" border="0" style="word-wrap:break-word">
<tbody><tr>
	<td style="border:#1A5CC8 1px solid" align="center" width="100%">
		<a href="/">
			<img src="/images/banner.jpg" width="100%" height="116" border="0" />
		</a>
	</td>
</tr>
<tr>
	<td style="border:#1A5CC8 1px solid">
	<table cellspacing="0" cellpadding="1" width="979px">
	<tbody><tr bgcolor="#1A5CC8" align="center" class="banner" height="25">
		<td>Online Judge</td>
		<td>Online Exercise</td>
		<td>Online Teaching</td>
		<td>Online Contests</td>
	<td>Exercise Author</td>
	</tr>
	<tr style="font-size:16px" align="center">
		<td width="20%" valign="top">
		<a href="/faq.php" style="text-decoration: none">F.A.Q</a><br />
		<a href="/friends" style="text-decoration: none">Hand In Hand</a><br />
		<a href="/onlineuser.php" style="text-decoration: none">Online Acmers</a>	<br />
		<!-- /onlineuser.php-->
		
		<!--<a href="" style="text-decoration: none">Forum | </a><a href="/discuss/public/list.php" style="text-decoration: none">Discuss</a><br>-->
		<!--<a href="/statistic/submit_graph.php" style="text-decoration: none">Statistical Charts</a><br>-->
		</td>
		<td width="20%" valign="top">
		<form action="/search.php" method="get">
		<a href="/listproblem.php?vol=1" style="text-decoration: none">Problem Archive</a><br />
		<!--<a href="http://feeds.feedburner.com/Hdoj-problemset"><img src="/images/rss1.jpg" alt="problemset" style="vertical-align:text-bottom;"width=20 height=20></a><br>-->
		<!--
			 <a href="/submit.php">Submit Solution</a><br>
		-->	
		<a href="/status.php" style="text-decoration: none">Realtime Judge Status</a><br />

		<a href="/ranklist.php" style="text-decoration: none">Authors Ranklist</a><br />
		<input name="field" value="author" type="hidden" /><input class="text60" name="key" /> <input class="button40" type="submit" value="Search" />
		
		<!--
			<input name=field value=problem type=hidden><input class=text60 name=key>&nbsp;<input class=button40 type=submit value=Search>
		-->
		</form>
		</td>
		<td width="20%" valign="top">
		 <form action="/search.php" method="get"> 
		     <a style="text-decoration: none" href="http://code.hdu.edu.cn/">C/C++/Java Exams     </a><br />
		<a style="text-decoration: none" href="/game">ACM Steps</a><br />
		<a href="/ITJobs/">Go to Job</a><br />	
		<a href="/livecast" style="text-decoration: none">Contest LiveCast</a><br />
		<a style="text-decoration: none" href="/region">ICPC@China</a><br />
		<!-- <a href="/register.php">Register New Author</a><br> -->
		<!-- <a href="/modifyuser.php">Update Your Information</a><br> -->
		</form>
		</td>
		<td width="20%" valign="top">
		<a href="http://bestcoder.hdu.edu.cn" style="text-decoration: none; color: red; font-weight: bold;">Best Coder <sup style="color: gray;">beta</sup></a><br /><a href="/vip/contest_list.php" style="text-decoration: none">VIP</a> | <a href="/contests/contest_list.php" style="text-decoration: none">STD Contests</a><br /><a href="http://code.hdu.edu.cn/vcontest" style="text-decoration: none">Virtual Contests </a><br />  <a href="/diy/contest_list.php" style="text-decoration: none">  DIY | </a><a href="/webcontest" style="text-decoration: none"><font color="">Web-DIY</font> <font size="1" color="gray"><sup>beta</sup></font></a><br />		</td>
		<td width="20%">
					<form method="post" action="/userloginex.php?action=login">
			  <table width="168" border="0" align="center" cellspacing="0">
			  	<tbody><tr><td align="center" colspan="2"><a href="/qqlogin/oauth/login.php"><img src="/qqlogin/images/qqlogin.png" border="0" /></a></td></tr>
				<tr><td width="68">Author ID </td><td align="right"><input name="username" type="text" class="text90" maxlength="20" /></td></tr>
				<tr><td>Password </td><td align="right"><input name="userpass" type="password" class="text90" maxlength="20" /></td></tr>
			  </tbody></table>
			  <input name="login" type="submit" class="button40" value="Sign In" /> <a href="http://bestcoder.hdu.edu.cn/register.php?url=acm.hdu.edu.cn/userloginex.php?action=login" style="text-decoration: none">Register new ID</a>
			</form>
						</td>
	</tr>
	</tbody></table>
	</td>
</tr>
<tr>
	<td>
		<div align="center" id="rollword"><marquee scrollamount="2" width="600" scrolldelay="30" onmouseover="javascript:this.stop();" onmouseout="javascript:this.start();"><b style="margin-right:20px"></b></marquee></div>	</td>
</tr>
<tr><td align="center"><h1 style="color:#1A5CC8">病毒侵袭</h1><font><b><span style="font-family:Arial;font-size:12px;font-weight:bold;color:green">Time Limit: 2000/1000 MS (Java/Others)    Memory Limit: 32768/32768 K (Java/Others)<br />Total Submission(s): 51944    Accepted Submission(s): 11086<br /></span></b></font><br /><br /><div class="panel_title" align="left">Problem Description</div> <div class="panel_content">当太阳的光辉逐渐被月亮遮蔽，世界失去了光明，大地迎来最黑暗的时刻。。。。在这样的时刻，人们却异常兴奋——我们能在有生之年看到500年一遇的世界奇观，那是多么幸福的事儿啊~~<br />但网路上总有那么些网站，开始借着民众的好奇心，打着介绍日食的旗号，大肆传播病毒。小t不幸成为受害者之一。小t如此生气，他决定要把世界上所有带病毒的网站都找出来。当然，谁都知道这是不可能的。小t却执意要完成这不能的任务，他说：“子子孙孙无穷匮也！”（愚公后继有人了）。<br />万事开头难，小t收集了好多病毒的特征码，又收集了一批诡异网站的源码，他想知道这些网站中哪些是有病毒的，又是带了怎样的病毒呢？顺便还想知道他到底收集了多少带病毒的网站。这时候他却不知道何从下手了。所以想请大家帮帮忙。小t又是个急性子哦，所以解决问题越快越好哦~~<br /></div><div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Input</div> <div class="panel_content">第一行，一个整数N（1&lt;=N&lt;=500），表示病毒特征码的个数。<br />接下来N行，每行表示一个病毒特征码，特征码字符串长度在20—200之间。<br />每个病毒都有一个编号，依此为1—N。<br />不同编号的病毒特征码不会相同。<br />在这之后一行，有一个整数M（1&lt;=M&lt;=1000），表示网站数。<br />接下来M行，每行表示一个网站源码，源码字符串长度在7000—10000之间。<br />每个网站都有一个编号，依此为1—M。<br />以上字符串中字符都是ASCII码可见字符（不包括回车）。<br /></div><div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Output</div> <div class="panel_content">依次按如下格式输出按网站编号从小到大输出，带病毒的网站编号和包含病毒编号，每行一个含毒网站信息。<br />web 网站编号: 病毒编号 病毒编号 …<br />冒号后有一个空格，病毒编号按从小到大排列，两个病毒编号之间用一个空格隔开，如果一个网站包含病毒，病毒数不会超过3个。<br />最后一行输出统计信息，如下格式<br />total: 带病毒网站数<br />冒号后有一个空格。<br /></div><div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Sample Input</div><div class="panel_content"><pre><div style="font-family:Courier New,Courier,monospace;">3
aaa
bbb
ccc
2
aaabbbccc
bbaacc</div></pre></div><div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Sample Output</div><div class="panel_content"><pre><div style="font-family:Courier New,Courier,monospace;">web 1: 1 2 3
total: 1</div></pre></div><div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Source</div> <div class="panel_content"> <a href="/search.php?field=problem&amp;key=2009+Multi-University+Training+Contest+10+-+Host+by+NIT&amp;source=1&amp;searchmode=source"> 2009 Multi-University Training Contest 10 - Host by NIT </a> </div> <div class="panel_bottom"> </div><br /><div class="panel_title" align="left">Recommend</div> <div class="panel_content">gaojie</div><div class="panel_bottom"> </div><br /><center style="font-size:15px;font-family:Arial;font-weight:bold;color:#1A5CC8"><a href="statistic.php?pid=2896">Statistic</a> | <a href="submit.php?pid=2896">Submit</a> | <a href="./discuss/problem/list.php?problemid=2896">Discuss</a> | <a href="note/note.php?pid=2896">Note</a><br /></center></td></tr><tr>
<td>
	<table style="border:#1A5CC8 1px solid; font-size:14px" cellspacing="0" cellpadding="1" width="100%">
	<tbody><tr align="center">
		<td class="footer_link" height="45"><a href="/">Home</a> | <a href="#top">Top</a></td>
		<td style="padding:6px">
			Hangzhou Dianzi University Online Judge 3.0<br />
			Copyright © 2005-2021 <a href="mailto:acm@hdu.edu.cn">HDU ACM Team</a>. All Rights Reserved.<br />
			<a href="../about_us/developer.php">Designer &amp; Developer </a>: <a>Wang Rongtao</a> <a>LinLe</a> <a href="mailto:gjavac@gmail.com">GaoJie</a> <a href="mailto:gl8997@gmail.com">GanLu</a><br />
			<span class="pagerunstatus">Total 0.000000(s) query 1, Server time : 2021-09-13 22:37:18, Gzip enabled</span>		</td>
		<td class="footer_link">
			<!-- <a href="javascript:history.go(-1);">Back</a> | <a href="javascript:history.forward();">Forward</a>-->
			<a href="/admin">Administration</a>	
		</td>
	</tr>
	</tbody></table>
</td>
</tr>
</tbody></table>

</body></html>