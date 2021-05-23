<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html xmlns="http://www.w3.org/1999/xhtml"><head>
	<title>Software Debugging</title>
	<meta http-equiv="Content-language" content="zh-Chinese" />
	<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
	<meta name="revisit-after" content="10 days" />
	<meta name="author" content="ADVDBG.ORG" />
	<meta name="description" content="" />
	<meta name="keywords" content="software, debugging, book, advanced debugging" />

	<link rel="stylesheet" type="text/css" href="gfx/swdbg.css" />

<script language="javascript">
&lt;!-- 

if (window != window.top) { top.location.href = location.href; }

// --&gt;
</script>

</head>

<body bgcolor="#cccccc" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0" rightmargin="0">

<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tbody><tr>
	<td width="100%" background="gfx/gray_stretch.jpg"><img src="gfx/gray_stretch.jpg" width="1" height="5" alt="" /></td>
</tr>
</tbody></table>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tbody><tr>
    <!-- <td rowspan="2" height="151"><a href="index.aspx"><img src="gfx/zhongkui_w.jpg" border="0" alt="Picture of Zhongkui"></a></td>
    -->
    <td width="100%" background="gfx/mid_stretch.jpg"><img src="gfx/mid_stretch.jpg" width="1" height="86" alt="" /></td>
	<td rowspan="2"><a href="index.aspx"><img src="gfx/stamp_w.jpg" border="0" alt="Stamp of Software Debugging" /></a></td>
</tr>
<tr>
	<td width="100%" background="gfx/wave.jpg"><img src="gfx/wave.jpg" width="1" height="65" alt="" /></td>
</tr>
</tbody></table>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tbody><tr>
	<td width="100%" colspan="3" background="gfx/gray_stretch.jpg"><img src="gfx/gray_stretch.jpg" width="1" height="5" alt="" /></td>
</tr>
<tr>
	<td background="gfx/nav_bg.jpg" width="165" valign="top">
        <table border="0" cellspacing="4" cellpadding="0">
            <tbody><tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span13"><a href="index.aspx">主  页</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span14"><a href="news.aspx">最新信息</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="op_lbl"><a href="abstract.aspx">内容简介</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span1"><a href="intro.aspx">前  言</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span2"><a href="comments.aspx">专家寄语</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span3"><a href="toc.aspx">目  录</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span4"><a href="parthead.aspx">篇  扉</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span5"><a href="sampchp.aspx">部分章节</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span6"><a href="samples.aspx">示例程序</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span7"><a href="tools.aspx">工  具</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span8"><a href="fqa.aspx">问  答</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span9"><a href="funs.aspx">写作花絮</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span10"><a href="resources.aspx">在线资源</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span11"><a href="feedback.aspx">意见反馈</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span12"><a href="errata.aspx">勘误</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
            <tr>
                <td width="12"> </td>
                <td height="50" valign="bottom" class="navtext"><span id="Span15"><a href="connect.aspx">以书会友</a></span></td>
            </tr>
            <tr>
                <td colspan="2" valign="top"><img src="gfx/menu_line.jpg" alt="" border="0" /></td>
            </tr>
		</tbody></table>
	</td>
    <td background="gfx/nav_line_stretch.jpg" width="10"><img src="gfx/nav_line_stretch.jpg" alt="navigation bar seprate line" /></td>
    <td bgcolor="#ffffff" valign="top" width="100%">

<table border="0" cellspacing="0" cellpadding="0">
    <tbody><tr><td colspan="2" height="20"></td></tr>
    <tr>
        <td width="10"></td>
        <td>
            <table width="100%" cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td><img src="gfx/cap_head.jpg" /></td>
                    <td width="100%" background="gfx/cap_stretch.jpg" class="txtCaption">符号文件观察器——SymView</td>
                    <td align="right"><img src="gfx/cap_tail.jpg" /></td>
                </tr>
            </tbody></table>
        </td>
    </tr>
    <tr>
    <td width="10"></td>
    <td class="artibody">
<table>
<tbody><tr><td height="10"></td></tr>
<tr>
    <td>
    <p>
    符号文件是调试器工作的重要依据，对很多调试功能都起着重要作用，例如栈回溯、源代码级跟踪、变量观察等等。符号文件大多是二进制的，而且不同编译器使用的文件格式有所不同。
    </p>
    <p>
    SymView工具用来显示符号文件中包含的符号表和符号数据。目前支持微软的Visual C/C++和C#编译器产生的DBG格式的符号文件和PDB格式的符号文件。
    </p>
    <p>
    SymView提供了以下多种方式来查看或者搜索符号文件的内容：
    </p>
    <ul type="square">
    <li>符号表</li>
    PDB或DBG文件中可以包含6种符号表，分别为符号表、源文件表、节贡献表、段表、注入源代码表和帧数据表。
    <li>编译素材（Compiland）</li>
    用于产生可执行文件的各种素材文件，包括OBJ、DLL、RES等。
    <li>数据流</li>
    比如描述FPO的FPO数据流。
    <li>符号类标（Tag）</li>
    根据所描述对象，符号被分为函数、常量、用户定义类型（UDT）、类型、常量等30多个类型。
    <li>搜索</li>
    可以按照符号逻辑关系或者符号名称等搜索符号。
    </ul>
    <p>
    下图是SymView的一个截图，左侧提供了上面介绍的5种观察视图。右侧上方的网格窗口用于显示左侧选中表格或者符号类的所有数据行或者符号。右侧下方用于显示上方选中行的子符号或者相关信息（属性）。
    <img src="gfx/symview.gif" />
    例如，目前使用的符号类表视图，选中的是UDT类型，右侧上方显示的是目前符号文件（ＮＴ内核的公共符号文件）中的所有ＵＤＴ类型的符号。右侧下方显示的是上方选中的_DBGKD_BREAKPOINTEX类型的所有属性。
    </p>
    <p>
    最下方的窗口用户显示SymView程序自身的调试信息，可能包含它工作过程中遇到的异常或者错误情况。
    </p>
    </td>
</tr> 

<tr>
    <td>   
    <h3>安装方法</h3>
    <p>
    目前，SymView只由一个文件组成，即SymView.exe。只要通过下面的链接下载压缩包后，将其中的文件解压缩到你喜欢的位置就可以了。
    </p>
    <p>
    值得说明的是，SymView是基于微软的DIASDK开发的，在工作时，它需要系统中已经有DIASDK的COM组件存在。如果你的系统中安装了Visual Studio 2005或者更高的版本的，那么这个组件应该已经安装好了。否则的话，你需要下载msdia80.dll并在命令行窗口执行如下命令进行注册：<br />
    regsvr32 msdia80.dll<br />
    应该在msdia80.dll所在目录中执行以上命令，或者指定完整的路径。
    </p>
    </td>
</tr>    
<tr>
    <td>   
    <h3>内部实现</h3>
    <p>
    SymView是基于微软的DIASDK开发的。DIASDK是Debug Interface Access SDK的简称。以Visual Studio 2005为例，DIASDK默认被安装在如下目录中：<br />
    c:\Program Files\Microsoft Visual Studio 8\DIA SDK<br />
    </p>
    <p>
    使用DIA组件的方法与使用其它COM组件一样，先要初始化COM支持库，然后创建接口的实例，即：
    </p><pre>	hr = CoInitialize(NULL);<br />	// Obtain Access To The Provider<br />	hr = CoCreateInstance(__uuidof(DiaSource),//CLSID_DiaSource, <br />				NULL, <br />				CLSCTX_INPROC_SERVER, <br />				__uuidof(IDiaDataSource),<br />				(void **) &amp;m_pDiaDataSource);<br />	if(hr != S_OK)<br />	{<br />		Msg(L"CoCreateInstance failed - HRESULT = %x\n",hr);<br />		return hr;<br />	}<br /></pre>
    <p></p>
    <p>
    描述符号的主要接口是IDiaSymbol，它有上百个属性，对应于不同的符号信息。MSDN中描述了DIA接口，尽管不够详尽，但是涵盖了几乎所有接口。
    </p>
    </td>
</tr>
<tr>
<td>
<h3>如何编译源代码</h3>
<p>
如果你希望自己重新编译SymView程序，那么可以通过下面的链接下载源程序包。下载后解压到一个名为SymView的目录中。
</p>
<p>
尽管包中的项目文件是VC6格式的，但是转化成更高版本的VC编译器然后编译应该不是大问题。<br />
</p>
<p>
值得注意的是，因为SymView是基于Dia SDK构建的，所以在编译时需要DIASDK的头文件和LIB文件，目前项目文件中是假定DIA SDK是位于当前项目的上一级目录的，即：<br />
</p><pre>DIASDK
--include
--lib
SymView
--*.cpp
--symview.dsw
--...
</pre>
<p>
所以一种简单的方法就是将DIASDK复制一份到与SymView平行的目录，不然的话需要调整项目设置，使其可以找到DIASDK的文件。
</p>
</td>
</tr>
<tr>
<td> 
    <h3>下载</h3>
    <p>
    包含SymView.exe的压缩包（216KB）<a href="/books/download/symview.zip">SymView.zip</a>
    </p>
    <p>
    包含msdia80.dll的压缩包（639KB）<a href="/books/download/msdia80.zip">msdia80.zip</a><br />
    </p>
    <p>
    SymView程序的完整源代码（358KB）<a href="/books/download/symv_src.zip">symv_src.zip</a><br />
    </p>
</td>
</tr>    
</tbody></table>
    </td>
</tr>
</tbody></table>
	</td>
</tr>
<!--
<tr>
	<td><img src="gfx/nav_bot_left.jpg" width="165" height="30" alt=""></td>
	<td width="100%" background="gfx/shade_bot.jpg"><img src="gfx/shade_bot.jpg" width="1" height="30" alt=""></td>
	<td></td>
</tr>
-->
<tr>
    <td width="165">
        <p align="center"></p>
    </td>
    <td background="gfx/nav_line_stretch.jpg" width="10"><img src="gfx/nav_line_stretch.jpg" alt="navigation bar seprate line" /></td>
    <td background="gfx/foot_wave.jpg"><img src="gfx/foot_wave.jpg" width="1" height="74" alt="" /></td>
</tr>    
<tr>
    <td colspan="2" bgcolor="#a5a5a5"></td>
    <td align="right" height="30" bgcolor="#a5a5a5"><font face="verdana, arial, helvetica" size="1" color="#666698">
		Copyright (C) 2008-2013 Raymond Zhang, All Rights Reserved
	    </font>
	</td>
	<!--<a class="footerLink" href="http://advdbg.org/">ADVDBG.ORG</a>-->
</tr>
</tbody></table>

</body></html>