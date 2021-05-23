<!-- Start: CommunityServer.Blogs.Controls.Page --><!-- Skin Path: ~/Themes/default/Skins/Views/View-Post.ascx --><!-- Start: CommunityServer.Blogs.Controls.LayoutTemplate --><!-- Skin Path: ~/Themes/default/Skins/LayoutTemplate.ascx --><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><html xmlns="http://www.w3.org/1999/xhtml"><head>
        <!-- Start: CommunityServer.Blogs.Controls.Header -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-Header.ascx -->
<title>AdvDbg System Section : 使用硬件调试器调试Windows内核的启动过程</title>

<link rel="stylesheet" href="/Themes/Blogs/default/style/style.css" type="text/css" media="screen" />

<meta name="GENERATOR" content="CommunityServer 1.1 (Build: 2.0.2.21480)" />
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://advdbg.org/blogs/advdbg_system/rss.aspx" />
<link rel="alternate" type="application/atom+xml" title="ATOM" href="http://advdbg.org/blogs/advdbg_system/atom.aspx" />
<!-- End: CommunityServer.Blogs.Controls.Header -->

    </head>
    <body>
        <form method="post" action="/blogs/advdbg_system/archive/2012/10/05/5427.aspx" id="Form1">
<div class="aspNetHidden">
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTMyNjg0MDc1MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFTl9jdGwwOl9jdGwwOl9jdGwwOl9jdGwwOkJsb2dTaWRlQmFyMTpfY3RsMDpTaW5nbGV3ZWJsb2dzZWFyY2gxOl9jdGwwOlNlYXJjaEJveNhL5NQ49ZXddzqj0eUn1h2v2aJD" />
</div>

<script type="text/javascript">
&lt;!--
var theForm = document.forms['Form1'];
if (!theForm) {
    theForm = document.Form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
// --&gt;
</script>


			<div id="content">
				<div id="top">
					<!-- Start: CommunityServer.Blogs.Controls.BlogTitleHeader -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-BlogTitleHeader.ascx -->


<h1><a id="_ctl0__ctl0__ctl0__ctl0_BlogTitleHeader1__ctl0_BlogTitle" class="headermaintitle" href="/blogs/advdbg_system/default.aspx">AdvDbg System Section</a></h1>
<p id="tagline"></p>

<!-- End: CommunityServer.Blogs.Controls.BlogTitleHeader -->

				</div>        
				<div id="leftmenu">
					<!-- Start: CommunityServer.Blogs.Controls.BlogSideBar -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-BlogSideBar.ascx -->
<!-- Start: CommunityServer.Blogs.Controls.WeblogQuickLinks -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-WeblogQuickLinks.ascx -->
<!-- End: CommunityServer.Blogs.Controls.WeblogQuickLinks -->


<!-- Start: CommunityServer.Blogs.Controls.SingleWeblogSearch -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-SingleWeblogSearch.ascx -->

	
<div id="Search">
<h3>Search</h3>
<input name="_ctl0:_ctl0:_ctl0:_ctl0:BlogSideBar1:_ctl0:Singleweblogsearch1:_ctl0:SearchBox" type="text" id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Singleweblogsearch1__ctl0_SearchBox" class="searchBox" onkeydown="KeyDownHandler('_ctl0:_ctl0:_ctl0:_ctl0:BlogSideBar1:_ctl0:Singleweblogsearch1:_ctl0:SearchButton',event);" /> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Singleweblogsearch1__ctl0_SearchButton" href="javascript:__doPostBack('_ctl0$_ctl0$_ctl0$_ctl0$BlogSideBar1$_ctl0$Singleweblogsearch1$_ctl0$SearchButton','')">Go</a>

</div>
	<!-- End: CommunityServer.Blogs.Controls.SingleWeblogSearch -->
 
  
<div id="cal">
   <!-- Start: CommunityServer.Blogs.Controls.WeblogCalendar -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-WeblogCalendar.ascx -->

<div id="Cal">
	<table id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Cal__ctl0_PostCalendar" class="Calendar" cellspacing="0" cellpadding="1" title="日历">
	<tbody><tr><td valign="middle" colspan="7"><table class="CalendarTitle" cellspacing="0">
		<tbody><tr><td class="CalendarNextPrev"><a href="javascript:__doPostBack('_ctl0$_ctl0$_ctl0$_ctl0$BlogSideBar1$_ctl0$Cal$_ctl0$PostCalendar','V4627')" style="color:Black" title="转到上一个月">&lt;</a></td><td nowrap="nowrap" align="center">2012年10月</td><td class="CalendarNextPrev" align="right"><a href="javascript:__doPostBack('_ctl0$_ctl0$_ctl0$_ctl0$BlogSideBar1$_ctl0$Cal$_ctl0$PostCalendar','V4688')" style="color:Black" title="转到下一个月">&gt;</a></td></tr>
	</tbody></table></td></tr><tr><th class="CalendarDays" align="center" abbr="星期日" scope="col">日</th><th class="CalendarDays" align="center" abbr="星期一" scope="col"> 一</th><th class="CalendarDays" align="center" abbr="星期二" scope="col"> 二</th><th class="CalendarDays" align="center" abbr="星期三" scope="col"> 三</th><th class="CalendarDays" align="center" abbr="星期四" scope="col"> 四</th><th class="CalendarDays" align="center" abbr="星期五" scope="col"> 五</th><th class="CalendarDays" align="center" abbr="星期六" scope="col"> 六</th></tr><tr><td class="CalendarDay" align="center">30</td><td class="CalendarDay" align="center">1</td><td class="CalendarDay" align="center">2</td><td class="CalendarDay" align="center">3</td><td class="CalendarDay" align="center">4</td><td class="CalendarDay" align="center"><a title="1 Post" href="/blogs/advdbg_system/archive/2012/10/5.aspx">5</a></td><td class="CalendarDay" align="center">6</td></tr><tr><td class="CalendarDay" align="center">7</td><td class="CalendarDay" align="center">8</td><td class="CalendarDay" align="center">9</td><td class="CalendarDay" align="center">10</td><td class="CalendarDay" align="center">11</td><td class="CalendarDay" align="center">12</td><td class="CalendarDay" align="center">13</td></tr><tr><td class="CalendarDay" align="center">14</td><td class="CalendarDay" align="center">15</td><td class="CalendarDay" align="center">16</td><td class="CalendarDay" align="center">17</td><td class="CalendarDay" align="center">18</td><td class="CalendarDay" align="center">19</td><td class="CalendarDay" align="center">20</td></tr><tr><td class="CalendarDay" align="center">21</td><td class="CalendarDay" align="center">22</td><td class="CalendarDay" align="center">23</td><td class="CalendarDay" align="center">24</td><td class="CalendarDay" align="center">25</td><td class="CalendarDay" align="center">26</td><td class="CalendarDay" align="center">27</td></tr><tr><td class="CalendarDay" align="center">28</td><td class="CalendarDay" align="center">29</td><td class="CalendarDay" align="center">30</td><td class="CalendarDay" align="center">31</td><td class="CalendarDay" align="center">1</td><td class="CalendarDay" align="center">2</td><td class="CalendarDay" align="center">3</td></tr><tr><td class="CalendarDay" align="center">4</td><td class="CalendarDay" align="center">5</td><td class="CalendarDay" align="center">6</td><td class="CalendarDay" align="center">7</td><td class="CalendarDay" align="center">8</td><td class="CalendarDay" align="center">9</td><td class="CalendarDay" align="center">10</td></tr>
</tbody></table>
</div>
<!-- End: CommunityServer.Blogs.Controls.WeblogCalendar -->

</div>
 
  

<!-- Start: CommunityServer.Blogs.Controls.CategoryList -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-CategoryList.ascx -->

	
<h3>文章分类</h3>
<ul>

        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_0" href="/blogs/advdbg_system/articles/category/1036.aspx">Bus</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_1" href="/blogs/advdbg_system/articles/category/1048.aspx">Computer System</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_2" href="/blogs/advdbg_system/articles/category/1023.aspx">Debug Methodology</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_3" href="/blogs/advdbg_system/articles/category/1032.aspx">Driver Development</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_4" href="/blogs/advdbg_system/articles/category/1027.aspx">Embedded System</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_5" href="/blogs/advdbg_system/articles/category/1018.aspx">Kernel Debug</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_6" href="/blogs/advdbg_system/articles/category/1056.aspx">Operating System</a>
            
        </li>
    
        <li>
            <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Categorylist2__ctl0_Categories_Link_7" href="/blogs/advdbg_system/articles/category/1041.aspx">Processors</a>
            
        </li>
    
</ul>
	<!-- End: CommunityServer.Blogs.Controls.CategoryList -->
  

<!-- Start: CommunityServer.Blogs.Controls.BlogNews -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-BlogNews.ascx -->
<!-- End: CommunityServer.Blogs.Controls.BlogNews -->

 
<h3>导航</h3>
<!-- Start: CommunityServer.Controls.NavigationMenu -->
<!-- Skin Path: ~/Themes/default/Skins/Skin-NavigationMenu.ascx -->

	
<div id="headertab">
<ul>
		
				<li id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_listItem_0" class="ButtonStyle1"> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_MenuItem_0" href="/">主页</a></li>
			
				<li id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_listItem_1" class="ButtonStyle2"> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_MenuItem_1" href="/blogs/">博客</a></li>
			
				<li id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_listItem_2" class="ButtonStyle3"> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_MenuItem_2" href="/forums/">论坛</a></li>
			
				<li id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_listItem_3" class="ButtonStyle4"> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0__ctl2__ctl0_Menu_MenuItem_3" href="/photos/">相册</a></li>
			
	</ul>
</div>

	<!-- End: CommunityServer.Controls.NavigationMenu -->

 
<!-- Start: CommunityServer.Blogs.Controls.LinkCategoryList -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-LinkCategoryList.ascx -->


	<!-- End: CommunityServer.Blogs.Controls.LinkCategoryList -->


<!-- Start: CommunityServer.Blogs.Controls.Subscriptions -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-Subscriptions.ascx -->

<div id="Subscriptions">
 <h3>订阅</h3>
 <ul>
 <li> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Subscriptions1__ctl0_rsslink" href="/blogs/advdbg_system/rss.aspx">RSS 2.0</a></li>
 <li> <a id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Subscriptions1__ctl0_atomlink" href="/blogs/advdbg_system/atom.aspx">Atom 0.3</a></li>
 
 <li id="_ctl0__ctl0__ctl0__ctl0_BlogSideBar1__ctl0_Subscriptions1__ctl0_contactitem"></li>
 </ul>
 </div><!-- End: CommunityServer.Blogs.Controls.Subscriptions -->
<!-- End: CommunityServer.Blogs.Controls.BlogSideBar -->

				</div>
				<div id="main">
					
        <!-- Start: CommunityServer.Blogs.Controls.EntryViewContainer -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-EntryViewContainer.ascx -->
<!-- Start: CommunityServer.Blogs.Controls.EntryView -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-EntryView.ascx -->

	
<div class="post">
                    <h2>使用硬件调试器调试Windows内核的启动过程 </h2>
                    <p>

最近公司刚买了一台CEDT硬件仿真器,  能调试从系统复位到关机重启的所有过程。我拿来跟了一下windows的内核启动过程，看了看完全真实的Windows初始化过程:
</p><ul><li>
CEDT开机后会请求用户选择目标系统的处理器类型。选择后，机器会在BIOS自动连接目标计算机。连接成功后，亲切的Windbg界面出现了。</li><li>停止系统运行后，发现系统停在BIOS里。在Windbg的命令行敲“！runto nt”，目标机继续运行，直到Windbg停止。</li><li>EDT提供命令直接执行到nt!KiSystemStartup然后停下来。然后打开CEDT的代码追踪功能，“！trclbr on”。从BOOTLOADER会传给KiSystemStartup一个结构的地址，结构中包含了BOOT的一些基本的信息，例如，引导分区，文件系统类型等等。KiSystemStartup首先将该结构指针赋值变量KeLoaderBlock。紧接着，KiSystemStartup会将P0BootStack和KiIdleThread0的地址存入LOADER_BLOCK中。FS寄存器会被赋值0x30并将FS:[0x130]清零。</li><li>
调用KiInitializeMachineType（）。KiInitializeMachineType（）从KeLoaderBlock中读取设备类型并赋值KeI386MachineType。

</li><li>
调用GetMachineBootPointers（）获取当前的GDTR和IDTR信息。然后为中断程序和NMI等初始化TSS。</li><li>
调用KiInitializePcr（）. 初始化KiIdleThread0的ApcState，将KiIdleProcess的指针赋给KiIdleThread0-&gt;ApcState.Process.</li><li>
调用KiSwapIDT()然后用IDT中的中断处理函数表初始化中断向量表。</li><li>
调用KiProcessorStart(). 这个函数只是判断了一下KiProcessorStartControl的值，看起来它像是个简单状态机的键。在这时，什么也没做就退出了。</li><li>
调用HalInitializeProcessor（），HalInitializeProcessor（）读取CPUID获得当前系统中的实际处理核个数，并初始化HalPrivateDispatchTable中的重要服务，其中HalpSetupPciDeviceForDebugging，HalpReleasePciDeviceForDebugging，HalpGetAcpiTablePhase0，HalpCheckPowerButton，HalpMapPhysicalMemory64，HalpUnmapVirtualAddress。 初始化8259和APIC的中断处理程序。</li><li>
调用KdInitSystem（），KdInitSystem首先检查是否是DEBUG模式，如果是，他会把KdpStub赋给KiDebugRoutine，并且初始化KdpDebuggerDataListHead和KdVersionBlock。 原来我们经常用来调试的STUB是在这初始化的。
</li><li>
调用KdPollBreakIn（）来收取调试的报文，如果有BREAKIN报文收到，赋值KdpControlCPressed并返回非零。并在退出后进入DbgBreakPointWithStatus（）。
</li><li>
在接下来程序中，KiBootFeatureBits的Bit7将会设为1。
</li><li>
调用KiInitializeKernel（）。在KiInitializeKernel中，首先</li><ul><li>调用_SEH_prolog（）；</li><li>调KiSetProcessorType（）通过检查处理器STEPPING和从CPUID中读取信息获得处理器种类并设置_KPRCB. CpuType.  KiSetCR0Bits（）根据处理器类型设置CR0的BIT16。 调用KiIsNpxPresent（）判断是否支持浮点运算器。

 </li><li>初始化KPRCB.
MaximumDpcQueueDepth, KPRCB. MinimumDpcRate, KPRCB.AdjustDpcThreshold

</li><li>调用PoInitializePrcb（）初始化KPRCB.PROCESSOR_POWER_STATE， </li><li>调用KeInitializeDpc（）填充KDPC。调用KeInitializeTimerEx（）初始化一个内核同步定时器。</li><li>检查了BOOTOPTION的设置。设置EFER寄存器的LME， 启动IA-32e模式。

</li><li>中间省略了一些代码的分析，包括初始化Ki486CompatibilityLock，KiFreezeExecutionLock等。</li><li>调用KeInitializeProcess（）填充第一个进程的KPROCESS。</li><li>根据FeatureBits初始化线程的参数。调用KeInitializeThread()初始化线程KiIdleThread0， 堆栈P0BootStack，进程为前面初始化的进程。</li><li>调用KeStartThread（）设置KiIdleThread0为READY状态。</li><li>调用ExpInitializeExecutive（），初始化OBJECT管理器，初始化安全， 进程管理器以及PNP管理器。在进程管理器的初始化过程中，创建PsInitialSystemProcess以及线程Phase1Initialization（）。PNP管理器的初始化过程将读取注册表中的设备资源用于初始化。</li></ul><li>

 



调用MmCreateKernelStack（）创建内核的堆栈。


 

</li><li>进入KiIdleLoop（）。</li></ul><p>今天就写到这了, 写了以后回来看,总是觉得很粗糙, 下次我会更详细些分析. 原本画了些图来说明, 但往上贴图时却总是失败, 请指导以下该怎么做.</p><p> </p>
                
                    <p class="postfoot">
                        posted on 2012年10月5日 21:22
						由
						<a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Entry__ctl0_AuthorLink" href="/user/Profile.aspx?UserID=6761">wood2000</a>
                    </p>                            
</div>              
	

<!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/">
<rdf:Description
rdf:about="http://advdbg.org/blogs/advdbg_system/archive/2012/10/05/5427.aspx"
dc:identifier="http://advdbg.org/blogs/advdbg_system/archive/2012/10/05/5427.aspx"
dc:title="使用硬件调试器调试Windows内核的启动过程"
trackback:ping="http://advdbg.org/blogs/trackback.aspx?PostID=5427" />
</rdf:RDF>
-->

<!-- End: CommunityServer.Blogs.Controls.EntryView -->

<!-- Start: CommunityServer.Blogs.Controls.BlogPostToolBar -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-BlogPostToolBar.ascx -->

<div id="postToolbar">
	
 
	                 
  
	
 
	


<a name="commentmessage">

</a>
</div>
	
<!-- End: CommunityServer.Blogs.Controls.BlogPostToolBar -->

<!-- Start: CommunityServer.Blogs.Controls.EntryComments -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-EntryComments.ascx -->

	
<div id="comments">
	
		<h4><a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Comments__ctl0_Comments_PermaLink_0" title="permalink" href="/blogs/advdbg_system/archive/2012/10/05/5427.aspx#6462">#</a>
		    <span>re: 使用硬件调试器调试Windows内核的启动过程<a name="6462"></a> @ 2014年12月17日 22:37</span>
		</h4>
		
		        请问楼主是否有 CEDT硬件仿真器 的详细介绍？
				
				
				<p class="posteds">	
				<a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Comments__ctl0_Comments_NameLink_0" title="avimatrix" target="_blank">avimatrix</a>
				
				</p>
		
		
</div>
	<!-- End: CommunityServer.Blogs.Controls.EntryComments -->

	
<!-- End: CommunityServer.Blogs.Controls.EntryViewContainer -->
   
    
				</div>
				<div class="copyright"></div>
<p align="center" class="txt4"><a target="_blank" href="http://www.communityserver.org/"><img alt="Powered by Community Server" border="0" src="/utility/EULA.GIF" /></a> <a target="_blank" href="http://www.communityserver.cn/"><img alt="Powered by CnForums.Net" border="0" src="/utility/CnForumsLogo.GIF" /></a></p>
            </div>
        
<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="FA6862B5" />
</div>
<script language="javascript">
&lt;!--
function KeyDownHandler(btn,event)
{
	if (event.keyCode == 13)
	{
		event.returnValue = false;
		event.cancel = true;
     __doPostBack(btn)
	}
}

//--&gt;
</script>
</form>
    


<!-- End: CommunityServer.Blogs.Controls.Page -->

</body></html><!-- End: CommunityServer.Blogs.Controls.LayoutTemplate -->