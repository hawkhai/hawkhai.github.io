<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1" />
<title>Base32编码解码，Base32在线转换工具 - 千千秀字</title>
<meta name="keywords" content="Base32" />
<meta name="description" content="Base32编码使用字母A-Z和数字2-7共计32个可打印ASCII字符对任意字节数据进行编码，与Base64相比，Base32编码不用区分大小写并排除了容易混淆的字符，方便人类使用及计算机处理。不过，Base32比Base64多占用大约20％的空间，因为Base32使用8个ASCII字符去编码原数据中的5个字节数据，而Base64是使用4个ASCII字符去编码原数据中的3个字节数据。" />
<link href="/css/style.css" rel="stylesheet" type="text/css" />
<style>
textarea {
	width: 100%;
	height: 150px;
	box-sizing: border-box;
	border: 1px #ccc solid;
	padding: 1%;
	line-height: 140%;
}
textarea:hover {
	border-color: #999;
}
textarea:focus {
	border-color: #59f;
}
@media screen and (max-height:640px) {
textarea {
	height: 100px;
}
}
#show {
	border: 1px #ccc solid;
	box-sizing: border-box;
	min-height: 150px;
	padding: 1%;
}
#copy {
	display: none;
}
#copytext {
	position: fixed;
	left: 9999px;
	top: 9999px;
}
</style>
<script src="https://partner.googleadservices.com/gampad/cookie.js?domain=www.qqxiuzi.cn&amp;callback=_gfp_s_&amp;client=ca-pub-2440711871479504"></script><script src="https://pagead2.googlesyndication.com/pagead/managed/js/adsense/m202112060101/show_ads_impl_fy2019.js" id="google_shimpl"></script><script src="https://hm.baidu.com/hm.js?899df2cdf7f5a83a719fb1bb96982b18"></script><script>
function ShowData(str1,str2)
{
	if (str1.length==0)
	{
		if (str2=='encode')
		document.getElementById("show").innerHTML="请在上面输入字符！";
		else
		document.getElementById("show").innerHTML="请在上面输入编码！";
		return;
	}
	document.getElementsByClassName('load-container').item(0).style.display='block';
	[].forEach.call(document.querySelectorAll('input[type="button"]'),function(b){b.disabled=true});
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 &amp;&amp; xmlhttp.status==200)
		{
			setTimeout(function(){
				document.getElementById("show").innerHTML=xmlhttp.responseText;
				document.getElementsByClassName('load-container').item(0).style.display='none';
				[].forEach.call(document.querySelectorAll('input[type="button"]'),function(b){b.disabled=false});
				if(xmlhttp.responseText!='')document.getElementById('copy').style.display='inline-block';else document.getElementById('copy').style.display='none'
			},500);
		}
	}
	xmlhttp.open("POST","baseShow.php",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send('text='+encodeURIComponent(str1)+'&amp;ende='+str2+'&amp;type=32'+'&amp;token=f7f848337dda1fdb463dfa0b1b77a916');
}
function copy(id) {
	var t = document.getElementById(id).innerHTML;
	if (t == '') return false;
	document.getElementById('copytext').innerHTML = t;
	var element = document.getElementById('copytext'), error = '浏览器不支持，请手动复制！';
	if (document.body.createTextRange) {
		var range = document.body.createTextRange();
		range.moveToElementText(element);
		range.select()
	} else if (window.getSelection) {
		var selection = window.getSelection(),
		range = document.createRange();
		range.selectNodeContents(element);
		selection.removeAllRanges();
		selection.addRange(range)
	} else return alert(error);
	try {
		if (document.execCommand('copy', false, null)) {
			document.getElementById('copytip').innerHTML = '已复制！';
		} else alert(error)
	} catch(err) {
		alert(error)
	}
}
document.addEventListener("click", function(e){
	if(e.target.id != 'copy') document.getElementById('copytip').innerHTML = ''
}, false);
</script>
<script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script src="/js/head.js"></script>
<meta http-equiv="origin-trial" content="AxujKG9INjsZ8/gUq8+dTruNvk7RjZQ1oFhhgQbcTJKDnZfbzSTE81wvC2Hzaf3TW4avA76LTZEMdiedF1vIbA4AAABueyJvcmlnaW4iOiJodHRwczovL2ltYXNkay5nb29nbGVhcGlzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2NTI3NzQ0MDAsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=" /><meta http-equiv="origin-trial" content="Azuce85ORtSnWe1MZDTv68qpaW3iHyfL9YbLRy0cwcCZwVnePnOmkUJlG8HGikmOwhZU22dElCcfrfX2HhrBPAkAAAB7eyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2NTI3NzQ0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A16nvcdeoOAqrJcmjLRpl1I6f3McDD8EfofAYTt/P/H4/AWwB99nxiPp6kA0fXoiZav908Z8etuL16laFPUdfQsAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2NTI3NzQ0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="AxBHdr0J44vFBQtZUqX9sjiqf5yWZ/OcHRcRMN3H9TH+t90V/j3ENW6C8+igBZFXMJ7G3Pr8Dd13632aLng42wgAAACBeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiVHJ1c3RUb2tlbnMiLCJleHBpcnkiOjE2NTI3NzQ0MDAsImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9" /><meta http-equiv="origin-trial" content="A88BWHFjcawUfKU3lIejLoryXoyjooBXLgWmGh+hNcqMK44cugvsI5YZbNarYvi3roc1fYbHA1AVbhAtuHZflgEAAAB2eyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IlRydXN0VG9rZW5zIiwiZXhwaXJ5IjoxNjUyNzc0NDAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ==" /><meta http-equiv="origin-trial" content="A8FHS1NmdCwGqD9DwOicnHHY+y27kdWfxKa0YHSGDfv0CSpDKRHTQdQmZVPDUdaFWUsxdgVxlwAd6o+dhJykPA0AAACWeyJvcmlnaW4iOiJodHRwczovL2RvdWJsZWNsaWNrLm5ldDo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjQzMTU1MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlLCJ1c2FnZSI6InN1YnNldCJ9" /><meta http-equiv="origin-trial" content="A8zdXi6dr1hwXEUjQrYiyYQGlU3557y5QWDnN0Lwgj9ePt66XMEvNkVWOEOWPd7TP9sBQ25X0Q15Lr1Nn4oGFQkAAACceyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXN5bmRpY2F0aW9uLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjQzMTU1MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlLCJ1c2FnZSI6InN1YnNldCJ9" /><meta http-equiv="origin-trial" content="A4/Htern2udN9w3yJK9QgWQxQFruxOXsXL7cW60DyCl0EZFGCSme/J33Q/WzF7bBkVvhEWDlcBiUyZaim5CpFQwAAACceyJvcmlnaW4iOiJodHRwczovL2dvb2dsZXRhZ3NlcnZpY2VzLmNvbTo0NDMiLCJmZWF0dXJlIjoiQ29udmVyc2lvbk1lYXN1cmVtZW50IiwiZXhwaXJ5IjoxNjQzMTU1MTk5LCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlLCJ1c2FnZSI6InN1YnNldCJ9" /><link rel="preload" href="https://adservice.google.com/adsid/integrator.js?domain=www.qqxiuzi.cn" as="script" /><script type="text/javascript" src="https://adservice.google.com/adsid/integrator.js?domain=www.qqxiuzi.cn"></script></head>
<body> 
<div class="load-container">
  <div class="loader"></div>
</div>
<div class="top"><div class="home"><a href="https://www.qqxiuzi.cn"><b><font color="#F8673D">千</font><font color="#E79C01">千</font><font color="#0EBB00">秀</font><font color="#669FFF">字</font></b></a></div><div class="nav"><a href="https://www.qqxiuzi.cn/daohang.htm">网站导航</a></div><div style="clear:both;"></div></div>
<div class="main" style="height: auto !important;">
  <div class="title"><h1>Base32编码解码</h1></div>
  <div class="ad">
<ins class="adsbygoogle" style="display: block; height: 280px;" data-ad-client="ca-pub-2440711871479504" data-ad-slot="8604148262" data-ad-format="auto" data-adsbygoogle-status="done" data-ad-status="filled"><ins id="aswift_0_expand" tabindex="0" title="Advertisement" aria-label="Advertisement" style="border: none; height: 280px; width: 892px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-table;"><ins id="aswift_0_anchor" style="border: none; height: 280px; width: 892px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: block; overflow: visible;"><iframe id="aswift_0" name="aswift_0" style="left:0;position:absolute;top:0;border:0;width:892px;height:280px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="892" height="280" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-2440711871479504&amp;output=html&amp;h=280&amp;slotname=8604148262&amp;adk=1843759609&amp;adf=1801062927&amp;pi=t.ma~as.8604148262&amp;w=892&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1639331346&amp;rafmt=1&amp;psa=0&amp;format=892x280&amp;url=https%3A%2F%2Fwww.qqxiuzi.cn%2Fbianma%2Fbase.php&amp;flash=0&amp;fwr=0&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMC4wLjAiLCJ4ODYiLCIiLCI5Ni4wLjQ2NjQuOTMiLFtdLG51bGwsbnVsbCwiNjQiXQ..&amp;dt=1639331345318&amp;bpp=6&amp;bdt=1427&amp;idt=745&amp;shv=r20211207&amp;mjsv=m202112060101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;correlator=7404671211080&amp;frm=20&amp;pv=2&amp;ga_vid=581124926.1639331346&amp;ga_sid=1639331346&amp;ga_hid=1791519054&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=1&amp;dmc=8&amp;adx=10&amp;ady=109&amp;biw=912&amp;bih=888&amp;scr_x=0&amp;scr_y=0&amp;eid=44750773%2C31063859%2C31062930&amp;oid=2&amp;pvsid=2140669617151644&amp;pem=639&amp;tmod=94&amp;eae=0&amp;fc=896&amp;brdim=-1158%2C44%2C-1158%2C44%2C1920%2C0%2C945%2C1020%2C929%2C888&amp;vis=1&amp;rsz=%7C%7CoeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=128&amp;bc=31&amp;ifi=1&amp;uci=a!1&amp;fsb=1&amp;xpc=PQ2DZBpB0M&amp;p=https%3A//www.qqxiuzi.cn&amp;dtd=774" data-google-container-id="a!1" data-google-query-id="CNCInJTp3vQCFcsH-QAd18QAOw" data-load-complete="true"></iframe></ins></ins></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div> 
  <textarea id="text"></textarea>
  <div align="center">
    <input onclick="ShowData(document.getElementById('text').value,'encode');" type="button" value="编码" />
    <input onclick="ShowData(document.getElementById('text').value,'decode');" type="button" value="解码" />
    <input type="button" onclick="document.getElementById('text').value='';document.getElementById('text').focus();document.getElementById('show').innerHTML='';document.getElementById('copy').style.display='none'" value="清空" />
  </div>
  <div id="show"></div>
  <input type="button" id="copy" onclick="copy('show')" value="复制" />
  <span id="copytip"></span>
  <div id="copytext"></div>
  <p>Base编码系列：<a href="/bianma/base64.htm" style="color:blue">Base64</a> <a href="/bianma/base.php" style="color:blue">Base32</a> <a href="/bianma/base.php?type=16" style="color:blue">Base16</a></p>
  <p>Base32编码是使用32个可打印字符（字母A-Z和数字2-7）对任意字节数据进行编码的方案，编码后的字符串不用区分大小写并排除了容易混淆的字符，可以方便地由人类使用并由计算机处理。</p>
<div style="overflow:auto">
<table width="460" border="1" cellpadding="3" cellspacing="0" bordercolor="#999999" align="center">
  <caption>
    RFC 4648 Base32 字母表
  </caption>
  <tbody>
    <tr>
      <th width="12%">值</th>
      <th width="12%">符号</th>
      <td rowspan="11"></td>
      <th width="12%">值</th>
      <th width="12%">符号</th>
      <td rowspan="11"></td>
      <th width="12%">值</th>
      <th width="12%">符号</th>
      <td rowspan="11"></td>
      <th width="12%">值</th>
      <th width="12%">符号</th>
    </tr>
    <tr>
      <td>0</td>
      <td>A</td>
      <td>8</td>
      <td>I</td>
      <td>16</td>
      <td>Q</td>
      <td>24</td>
      <td>Y</td>
    </tr>
    <tr>
      <td>1</td>
      <td>B</td>
      <td>9</td>
      <td>J</td>
      <td>17</td>
      <td>R</td>
      <td>25</td>
      <td>Z</td>
    </tr>
    <tr>
      <td>2</td>
      <td>C</td>
      <td>10</td>
      <td>K</td>
      <td>18</td>
      <td>S</td>
      <td>26</td>
      <td>2</td>
    </tr>
    <tr>
      <td>3</td>
      <td>D</td>
      <td>11</td>
      <td>L</td>
      <td>19</td>
      <td>T</td>
      <td>27</td>
      <td>3</td>
    </tr>
    <tr>
      <td>4</td>
      <td>E</td>
      <td>12</td>
      <td>M</td>
      <td>20</td>
      <td>U</td>
      <td>28</td>
      <td>4</td>
    </tr>
    <tr>
      <td>5</td>
      <td>F</td>
      <td>13</td>
      <td>N</td>
      <td>21</td>
      <td>V</td>
      <td>29</td>
      <td>5</td>
    </tr>
    <tr>
      <td>6</td>
      <td>G</td>
      <td>14</td>
      <td>O</td>
      <td>22</td>
      <td>W</td>
      <td>30</td>
      <td>6</td>
    </tr>
    <tr>
      <td>7</td>
      <td>H</td>
      <td>15</td>
      <td>P</td>
      <td>23</td>
      <td>X</td>
      <td>31</td>
      <td>7</td>
    </tr>
    <tr>
      <td><em>填充</em></td>
      <td>=</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td colspan="2"></td>
    </tr>
  </tbody>
</table>
</div>
<p>Base32将任意字符串按照字节进行切分，并将每个字节对应的二进制值（不足8比特高位补0）串联起来，按照5比特一组进行切分，并将每组二进制值转换成十进制来对应32个可打印字符中的一个。</p>
<p>由于数据的二进制传输是按照8比特一组进行（即一个字节），因此Base32按5比特切分的二进制数据必须是40比特的倍数（5和8的最小公倍数）。例如输入单字节字符“%”，它对应的二进制值是“100101”，前面补两个0变成“00100101”（二进制值不足8比特的都要在高位加0直到8比特），从左侧开始按照5比特切分成两组：“00100”和“101”，后一组不足5比特，则在末尾填充0直到5比特，变成“00100”和“10100”，这两组二进制数分别转换成十进制数，通过上述表格即可找到其对应的可打印字符“E”和“U”，但是这里只用到两组共10比特，还差30比特达到40比特，按照5比特一组还需6组，则在末尾填充6个“=”。填充“=”符号的作用是方便一些程序的标准化运行，大多数情况下不添加也无关紧要，而且，在URL中使用时必须去掉“=”符号。</p>
<p>与Base64相比，Base32具有许多优点：</p>
<ul type="circle">
<li>适合不区分大小写的文件系统，更利于人类口语交流或记忆。</li>
<li>结果可以用作文件名，因为它不包含路径分隔符 “/”等符号。</li>
<li>排除了视觉上容易混淆的字符，因此可以准确的人工录入。（例如，RFC4648符号集忽略了数字“1”、“8”和“0”，因为它们可能与字母“I”，“B”和“O”混淆）。</li>
<li>排除填充符号“=”的结果可以包含在URL中，而不编码任何字符。</li>
</ul>
<p>Base32也比Base16有优势：</p>
<ul type="circle">
<li>Base32比Base16占用的空间更小。（1000比特数据Base32需要200个字符，而Base16则为250个字符）</li>
</ul>
<p>Base32的缺点：</p>
<ul type="circle">
<li>Base32比Base64多占用大约20％的空间。因为Base32使用8个ASCII字符去编码原数据中的5个字节数据，而Base64是使用4个ASCII字符去编码原数据中的3个字节数据。</li>
</ul>
<p>本页Base32编码方案符合RFC4648文档描述。输入字符集为UTF-8编码。</p>  <div class="ad2">
<ins class="adsbygoogle" style="display: block; height: 280px;" data-ad-client="ca-pub-2440711871479504" data-ad-slot="8604148262" data-ad-format="auto" data-adsbygoogle-status="done" data-ad-status="filled"><ins id="aswift_1_expand" tabindex="0" title="Advertisement" aria-label="Advertisement" style="border: none; height: 280px; width: 892px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-table;"><ins id="aswift_1_anchor" style="border: none; height: 280px; width: 892px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: block; overflow: visible;"><iframe id="aswift_1" name="aswift_1" style="left:0;position:absolute;top:0;border:0;width:892px;height:280px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="892" height="280" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-2440711871479504&amp;output=html&amp;h=280&amp;slotname=8604148262&amp;adk=1843759609&amp;adf=3561467008&amp;pi=t.ma~as.8604148262&amp;w=892&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1639331346&amp;rafmt=1&amp;psa=0&amp;format=892x280&amp;url=https%3A%2F%2Fwww.qqxiuzi.cn%2Fbianma%2Fbase.php&amp;flash=0&amp;fwr=0&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMC4wLjAiLCJ4ODYiLCIiLCI5Ni4wLjQ2NjQuOTMiLFtdLG51bGwsbnVsbCwiNjQiXQ..&amp;dt=1639331345324&amp;bpp=2&amp;bdt=1432&amp;idt=780&amp;shv=r20211207&amp;mjsv=m202112060101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=892x280&amp;correlator=7404671211080&amp;frm=20&amp;pv=1&amp;ga_vid=581124926.1639331346&amp;ga_sid=1639331346&amp;ga_hid=1791519054&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=1&amp;dmc=8&amp;adx=10&amp;ady=2041&amp;biw=912&amp;bih=888&amp;scr_x=0&amp;scr_y=0&amp;eid=44750773%2C31063859%2C31062930&amp;oid=2&amp;pvsid=2140669617151644&amp;pem=639&amp;tmod=94&amp;eae=0&amp;fc=896&amp;brdim=-1158%2C44%2C-1158%2C44%2C1920%2C0%2C945%2C1020%2C929%2C888&amp;vis=1&amp;rsz=%7C%7CeoEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=128&amp;bc=31&amp;ifi=2&amp;uci=a!2&amp;btvi=1&amp;fsb=1&amp;xpc=MpPw2J7zc2&amp;p=https%3A//www.qqxiuzi.cn&amp;dtd=784" data-google-container-id="a!2" data-google-query-id="CJqEnJTp3vQCFd0S-QAdqTID-A" data-load-complete="true"></iframe></ins></ins></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div> 
</div>
<div class="foot">QQXIUZI.CN　<a href="https://www.qqxiuzi.cn">千千秀字</a><span id="feedback" style="margin-left:1em;cursor:pointer" onclick="feedbackPanel()">用户反馈</span></div>


<ins class="adsbygoogle adsbygoogle-noablate" data-adsbygoogle-status="done" style="display: none !important;" data-ad-status="unfilled"><ins id="aswift_2_expand" tabindex="0" title="Advertisement" aria-label="Advertisement" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: none;"><ins id="aswift_2_anchor" style="border: none; height: 0px; width: 0px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: none;"><iframe id="aswift_2" name="aswift_2" style="left:0;position:absolute;top:0;border:0;width:undefinedpx;height:undefinedpx;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allowfullscreen="true" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-2440711871479504&amp;output=html&amp;adk=1812271804&amp;adf=3025194257&amp;lmt=1639331346&amp;plat=1%3A8%2C2%3A8%2C3%3A32%2C4%3A32%2C9%3A32776%2C16%3A8388608%2C17%3A32%2C24%3A32%2C25%3A32%2C30%3A1048576%2C32%3A32&amp;format=0x0&amp;url=https%3A%2F%2Fwww.qqxiuzi.cn%2Fbianma%2Fbase.php&amp;ea=0&amp;flash=0&amp;pra=7&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMC4wLjAiLCJ4ODYiLCIiLCI5Ni4wLjQ2NjQuOTMiLFtdLG51bGwsbnVsbCwiNjQiXQ..&amp;dt=1639331345341&amp;bpp=2&amp;bdt=1449&amp;idt=773&amp;shv=r20211207&amp;mjsv=m202112060101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;prev_fmts=892x280%2C892x280&amp;nras=1&amp;correlator=7404671211080&amp;frm=20&amp;pv=1&amp;ga_vid=581124926.1639331346&amp;ga_sid=1639331346&amp;ga_hid=1791519054&amp;ga_fc=0&amp;u_tz=480&amp;u_his=2&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1040&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=1&amp;dmc=8&amp;adx=-12245933&amp;ady=-12245933&amp;biw=912&amp;bih=888&amp;scr_x=0&amp;scr_y=0&amp;eid=44750773%2C31063859%2C31062930&amp;oid=2&amp;pvsid=2140669617151644&amp;pem=639&amp;tmod=94&amp;eae=2&amp;fc=896&amp;brdim=-1158%2C44%2C-1158%2C44%2C1920%2C0%2C945%2C1020%2C929%2C888&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=32768&amp;bc=31&amp;ifi=3&amp;uci=a!3&amp;fsb=1&amp;dtd=780" data-google-container-id="a!3" data-load-complete="true"></iframe></ins></ins></ins><iframe src="https://www.google.com/recaptcha/api2/aframe" width="0" height="0" style="display: none;"></iframe></body><iframe id="google_esf" name="google_esf" src="https://googleads.g.doubleclick.net/pagead/html/r20211207/r20190131/zrt_lookup.html" style="display: none;"></iframe></html>