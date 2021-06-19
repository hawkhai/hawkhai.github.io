<!-- Start: CommunityServer.Blogs.Controls.Page --><!-- Skin Path: ~/Themes/default/Skins/Views/View-Post.ascx --><!-- Start: CommunityServer.Blogs.Controls.LayoutTemplate --><!-- Skin Path: ~/Themes/default/Skins/LayoutTemplate.ascx --><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"><html xmlns="http://www.w3.org/1999/xhtml"><head>
        <!-- Start: CommunityServer.Blogs.Controls.Header -->
<!-- Skin Path: ~/Themes/default/Skins/Skins/Skin-Header.ascx -->
<title>AdvDbg System Section : 解读编码后的HEAP_ENTRY结构</title>

<link rel="stylesheet" href="/Themes/Blogs/default/style/style.css" type="text/css" media="screen" />

<meta name="GENERATOR" content="CommunityServer 1.1 (Build: 2.0.2.21480)" />
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://advdbg.org/blogs/advdbg_system/rss.aspx" />
<link rel="alternate" type="application/atom+xml" title="ATOM" href="http://advdbg.org/blogs/advdbg_system/atom.aspx" />
<!-- End: CommunityServer.Blogs.Controls.Header -->

    </head>
    <body>
        <form method="post" action="/blogs/advdbg_system/articles/5152.aspx" id="Form1">
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
		<tbody><tr><td class="CalendarNextPrev"><a href="javascript:__doPostBack('_ctl0$_ctl0$_ctl0$_ctl0$BlogSideBar1$_ctl0$Cal$_ctl0$PostCalendar','V7791')" style="color:Black" title="转到上一个月">&lt;</a></td><td nowrap="nowrap" align="center">2021年6月</td><td class="CalendarNextPrev" align="right"><a href="javascript:__doPostBack('_ctl0$_ctl0$_ctl0$_ctl0$BlogSideBar1$_ctl0$Cal$_ctl0$PostCalendar','V7852')" style="color:Black" title="转到下一个月">&gt;</a></td></tr>
	</tbody></table></td></tr><tr><th class="CalendarDays" align="center" abbr="星期日" scope="col">日</th><th class="CalendarDays" align="center" abbr="星期一" scope="col"> 一</th><th class="CalendarDays" align="center" abbr="星期二" scope="col"> 二</th><th class="CalendarDays" align="center" abbr="星期三" scope="col"> 三</th><th class="CalendarDays" align="center" abbr="星期四" scope="col"> 四</th><th class="CalendarDays" align="center" abbr="星期五" scope="col"> 五</th><th class="CalendarDays" align="center" abbr="星期六" scope="col"> 六</th></tr><tr><td class="CalendarDay" align="center">30</td><td class="CalendarDay" align="center">31</td><td class="CalendarDay" align="center">1</td><td class="CalendarDay" align="center">2</td><td class="CalendarDay" align="center">3</td><td class="CalendarDay" align="center">4</td><td class="CalendarDay" align="center">5</td></tr><tr><td class="CalendarDay" align="center">6</td><td class="CalendarDay" align="center">7</td><td class="CalendarDay" align="center">8</td><td class="CalendarDay" align="center">9</td><td class="CalendarDay" align="center">10</td><td class="CalendarDay" align="center">11</td><td class="CalendarDay" align="center">12</td></tr><tr><td class="CalendarDay" align="center">13</td><td class="CalendarDay" align="center">14</td><td class="CalendarDay" align="center">15</td><td class="CalendarDay" align="center">16</td><td class="CalendarDay" align="center">17</td><td class="CalendarDay" align="center">18</td><td class="CalendarDay" align="center">19</td></tr><tr><td class="CalendarDay" align="center">20</td><td class="CalendarDay" align="center">21</td><td class="CalendarDay" align="center">22</td><td class="CalendarDay" align="center">23</td><td class="CalendarDay" align="center">24</td><td class="CalendarDay" align="center">25</td><td class="CalendarDay" align="center">26</td></tr><tr><td class="CalendarDay" align="center">27</td><td class="CalendarDay" align="center">28</td><td class="CalendarDay" align="center">29</td><td class="CalendarDay" align="center">30</td><td class="CalendarDay" align="center">1</td><td class="CalendarDay" align="center">2</td><td class="CalendarDay" align="center">3</td></tr><tr><td class="CalendarDay" align="center">4</td><td class="CalendarDay" align="center">5</td><td class="CalendarDay" align="center">6</td><td class="CalendarDay" align="center">7</td><td class="CalendarDay" align="center">8</td><td class="CalendarDay" align="center">9</td><td class="CalendarDay" align="center">10</td></tr>
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
                    <h2>解读编码后的HEAP_ENTRY结构 </h2>
                    <p>好久没有写博客了，很是惭愧。看到<a href="http://advdbg.org/forums/5151/ShowPost.aspx">论坛上有朋友询问无法解读HEAP_ENTRY结构</a>，觉得这个问题非常好，正好也略有空闲，就聊聊这个问题吧。</p>
<p>事情还是源于“广被误解”的Vista，说起话来，已经是2006年前的事了，当年Vista团队不辞劳苦对NT做了很多大刀阔斧的改革，但因为延期，和来不及打磨的楞楞角角，遭到的批评远比好评多，功劳都被后来的Win7给占了，真是比窦娥还冤。</p>
<p>Vista引入了很多新的东西，直到今天，还有很多东西需要Windows阵营里的各色人群慢慢认识和理解消化。比如对堆的改造就是其中之一。</p>
<p>长话短说，在堆的若干新特征中， 比较易让人感觉到的便是对堆块的块头结构（HEAP_ENTRY)编码。编码的目的是引入随机性，增强堆的安全性，防止黑客轻易就可以预测堆的数据内容而实施攻击。</p>
<p>首先，在_HEAP结构中新增（相对于XP）了如下两个字段：</p>
<p>   +0x07c EncodeFlagMask   : 0x100000<br />   +0x080 Encoding         : _HEAP_ENTRY</p>
<p>其中的EncodeFlagMask用来指示是否启用编码功能；Encoding字段是用来编码的，编码的方法就是用这个Encoding结构与每个堆块的头结构做异或（XOR）。</p>
<p>不妨通过实际例子来加深理解，辛苦notepad出来作下靶子，然后请WinDBG出场。先看32位的情况：</p>
<p>0:001&gt; !heap 01670000  -A<br />Index   Address  Name      Debugging options enabled<br />  6:   01670000 <br />    Segment at 01670000 to 016b0000 (00019000 bytes committed)</p>
<p>...</p>
<p>        0167f7b0: 00048 . 00460 [101] - busy (458)<br /><strong><font color="#ff0000">        0167fc10: 00460 . 00060 [101] - busy (58)<br /></font></strong>        0167fc70: 00060 . 09370 [100]<br />        01688fe0: 09370 . 00020 [111] - busy (1d)<br />        01689000:      00027000      - uncommitted bytes.</p>
<p>不妨就以起始地址为<font face="Courier New">0167fc10</font>的这个堆块为例，先使用扩展命令观察：</p>
<p><font face="Courier New">0:001&gt; !heap -x 0167fc10<br />Entry     User      Heap      Segment       Size  PrevSize  Unused    Flags<br />-----------------------------------------------------------------------------<br />0167fc10  0167fc18  01670000  01670000        60       460         8  busy </font></p>
<p>其总长度是0x60字节，包含头结构的8个字节。</p>
<p>再观察原始的结构内容：</p>
<p>0:001&gt; dt _heap_entry  0167fc10<br />ntdll!_HEAP_ENTRY<br />   +0x000 Size             : 0x1922<br />   +0x002 Flags            : 0x37 '7'<br />   +0x003 SmallTagIndex    : 0x23 '#'<br />   +0x000 SubSegmentCode   : 0x23371922 <br />   +0x004 PreviousSize     : 0xe768<br />   +0x006 SegmentOffset    : 0 ''<br />   +0x006 LFHFlags         : 0 ''<br />   +0x007 UnusedBytes      : 0x8 ''<br />   +0x000 FunctionIndex    : 0x1922<br />   +0x002 ContextValue     : 0x2337<br />   +0x000 InterceptorValue : 0x23371922<br />   +0x004 UnusedBytesLength : 0xe768<br />   +0x006 EntryOffset      : 0 ''<br />   +0x007 ExtendedBlockSignature : 0x8 ''<br />   +0x000 Code1            : 0x23371922<br />   +0x004 Code2            : 0xe768<br />   +0x006 Code3            : 0 ''<br />   +0x007 Code4            : 0x8 ''<br />   +0x000 AgregateCode     : 0x800e768`23371922</p>
<p>Size字段是1922，这显然不对，是编码过的。</p>
<p>下面尝试用手工解码，先要读取Encoding结构的数据：</p>
<p><font face="Courier New">0:001&gt; dt _HEAP 01670000  <br />ntdll!_HEAP<br />   +0x000 Entry            : _HEAP_ENTRY<br />   +0x008 SegmentSignature : 0xffeeffee<br />   +0x00c SegmentFlags     : 0<br />   +0x010 SegmentListEntry : _LIST_ENTRY [ 0x16700a8 - 0x16700a8 ]<br />   +0x018 Heap             : 0x01670000 _HEAP<br />   +0x01c BaseAddress      : 0x01670000 <br />   +0x020 NumberOfPages    : 0x40<br />   +0x024 FirstEntry       : 0x01670588 _HEAP_ENTRY<br />   +0x028 LastValidEntry   : 0x016b0000 _HEAP_ENTRY<br />   +0x02c NumberOfUnCommittedPages : 0x27<br />   +0x030 NumberOfUnCommittedRanges : 1<br />   +0x034 SegmentAllocatorBackTraceIndex : 0<br />   +0x036 Reserved         : 0<br />   +0x038 UCRSegmentList   : _LIST_ENTRY [ 0x1688ff0 - 0x1688ff0 ]<br />   +0x040 Flags            : 0x1002<br />   +0x044 ForceFlags       : 0<br />   +0x048 CompatibilityFlags : 0<br />   +0x04c EncodeFlagMask   : 0x100000<br /><strong><font color="#ff0000">   +0x050 Encoding         : _HEAP_ENTRY<br /></font></strong>   +0x058 PointerKey       : 0x6db0dffc<br />   +0x05c Interceptor      : 0<br />   +0x060 VirtualMemoryThreshold : 0xfe00<br />   +0x064 Signature        : 0xeeffeeff<br />   +0x068 SegmentReserve   : 0x100000<br />   +0x06c SegmentCommit    : 0x2000<br />   +0x070 DeCommitFreeBlockThreshold : 0x200<br />   +0x074 DeCommitTotalFreeThreshold : 0x2000<br />   +0x078 TotalFreeSize    : 0x1a28<br />   +0x07c MaximumAllocationSize : 0x7ffdefff<br />   +0x080 ProcessHeapsListIndex : 6<br />   +0x082 HeaderValidateLength : 0x138<br />   +0x084 HeaderValidateCopy : (null) <br />   +0x088 NextAvailableTagIndex : 0<br />   +0x08a MaximumTagIndex  : 0<br />   +0x08c TagEntries       : (null) <br />   +0x090 UCRList          : _LIST_ENTRY [ 0x1688fe8 - 0x1688fe8 ]<br />   +0x098 AlignRound       : 0xf<br />   +0x09c AlignMask        : 0xfffffff8<br />   +0x0a0 VirtualAllocdBlocks : _LIST_ENTRY [ 0x16700a0 - 0x16700a0 ]<br />   +0x0a8 SegmentList      : _LIST_ENTRY [ 0x1670010 - 0x1670010 ]<br />   +0x0b0 AllocatorBackTraceIndex : 0<br />   +0x0b4 NonDedicatedListLength : 0<br />   +0x0b8 BlocksIndex      : 0x01670150 <br />   +0x0bc UCRIndex         : 0x01670590 <br />   +0x0c0 PseudoTagEntries : (null) <br />   +0x0c4 FreeLists        : _LIST_ENTRY [ 0x167f770 - 0x167fc78 ]<br />   +0x0cc LockVariable     : 0x01670138 _HEAP_LOCK<br />   +0x0d0 CommitRoutine    : 0x6db0dffc     long  +6db0dffc<br />   +0x0d4 FrontEndHeap     : (null) <br />   +0x0d8 FrontHeapLockCount : 0<br />   +0x0da FrontEndHeapType : 0 ''<br />   +0x0dc Counters         : _HEAP_COUNTERS<br />   +0x130 TuningParameters : _HEAP_TUNING_PARAMETERS<br />读取偏移为0x50的Encoding子结构：</font></p>
<p><font face="Courier New">0:001&gt; dd 01670000+50<br />01670050  2e36192e 0000e7e4 6db0dffc 00000000<br />01670060  0000fe00 eeffeeff 00100000 00002000<br />01670070  00000200 00002000 00001a28 7ffdefff<br />01670080  01380006 00000000 00000000 00000000<br />01670090  01688fe8 01688fe8 0000000f fffffff8<br />016700a0  016700a0 016700a0 01670010 01670010<br />016700b0  00000000 00000000 01670150 01670590<br />016700c0  00000000 0167f770 0167fc78 01670138</font></p>
<p><font face="Courier New">再显示堆块头结构的原始数据：<br />0:001&gt; dd 0167fc10  <br />0167fc10  23371922 0800e768 01ed3a00 01e9ca90<br />0167fc20  01c0fd08 0167edb8 00000001 00008c4e<br />0167fc30  000015f6 00000262 0000090c 00010000<br />0167fc40  01678a60 0000003c 00010001 00000000<br />0167fc50  ffffffff 00000000 00000000 ffffffff<br />0167fc60  00000000 00000000 ffffffff 00000000<br />0167fc70  52360b40 0000e7e8 016700c4 0167b5b8<br />0167fc80  0300d400 62617261 79631400 32006c72</font></p>
<p><font face="Courier New">做异或运算进行解码：<br />0:001&gt; ? 23371922^2e36192e  <br />Evaluate expression: 218169356 = 0d01000c</font></p>
<p><font face="Courier New">低地址的word是Size字段，所以Size字段是0xC，因为是以粒度8为单位的，所以字节大小是：</font></p>
<p><font face="Courier New">0:001&gt; ? c*8<br />Evaluate expression: 96 = 00000060</font></p>
<p><font face="Courier New">也就是0x60，与前面扩展命令显示出的刚好一致。</font></p>
<p><font face="Courier New">下面再看一下64位系统的情况，64位中，堆块头结构扩展为16字节，堆块的分配粒度也增大为16.</font></p>
<p>0:002&gt; !heap 02680000                -A<br />Index   Address  Name      Debugging options enabled<br />  8:   02680000 </p>
<p>...</p>
<p>        0000000002686ee0: 01010 . 010e0 [100]<br />        0000000002687fc0: 010e0 . 00040 [111] - busy (3d)<br />        0000000002688000:      00008000      - uncommitted bytes.<br /></p>
<p><font face="Courier New">0:002&gt; !heap -x 0000000002687fc0<br />Entry             User              Heap              Segment               Size  PrevSize  Unused    Flags<br />-------------------------------------------------------------------------------------------------------------<br />0000000002687fc0  0000000002687fd0  0000000002680000  0000000002680000        40      10e0         3  busy last <br /></font></p>
<p><font face="Courier New">总长度是0x40字节</font></p>
<p>0:002&gt; dt _HEAP_ENTRY 0000000002687fc0  <br />ntdll!_HEAP_ENTRY<br />   +0x000 PreviousBlockPrivateData : (null) <br />   +0x008 Size             : 0x98ce<br />   +0x00a Flags            : 0x55 'U'<br />   +0x00b SmallTagIndex    : 0x72 'r'<br />   +0x00c PreviousSize     : 0x40ec<br />   +0x00e SegmentOffset    : 0 ''<br />   +0x00e LFHFlags         : 0 ''<br />   +0x00f UnusedBytes      : 0x3 ''<br />   +0x008 CompactHeader    : 0x30040ec`725598ce<br />   +0x000 Reserved         : (null) <br />   +0x008 FunctionIndex    : 0x98ce<br />   +0x00a ContextValue     : 0x7255<br />   +0x008 InterceptorValue : 0x725598ce<br />   +0x00c UnusedBytesLength : 0x40ec<br />   +0x00e EntryOffset      : 0 ''<br />   +0x00f ExtendedBlockSignature : 0x3 ''<br />   +0x000 ReservedForAlignment : (null) <br />   +0x008 Code1            : 0x725598ce<br />   +0x00c Code2            : 0x40ec<br />   +0x00e Code3            : 0 ''<br />   +0x00f Code4            : 0x3 ''<br />   +0x008 AgregateCode     : 0x30040ec`725598ce</p>
<p>注意Size字段是从偏移8开始的两个字节，不再是从偏移0开始。</p>
<p>0:002&gt; dt _HEAP 02680000                <br />ntdll!_HEAP<br />   +0x000 Entry            : _HEAP_ENTRY<br />   +0x010 SegmentSignature : 0xffeeffee<br />   +0x014 SegmentFlags     : 0<br />   +0x018 SegmentListEntry : _LIST_ENTRY [ 0x00000000`02690018 - 0x2680128 ]<br />   +0x028 Heap             : 0x00000000`02680000 _HEAP<br />   +0x030 BaseAddress      : 0x00000000`02680000 <br />   +0x038 NumberOfPages    : 0x10<br />   +0x040 FirstEntry       : 0x00000000`02680a80 _HEAP_ENTRY<br />   +0x048 LastValidEntry   : 0x00000000`02690000 _HEAP_ENTRY<br />   +0x050 NumberOfUnCommittedPages : 8<br />   +0x054 NumberOfUnCommittedRanges : 1<br />   +0x058 SegmentAllocatorBackTraceIndex : 0<br />   +0x05a Reserved         : 0<br />   +0x060 UCRSegmentList   : _LIST_ENTRY [ 0x00000000`02687fe0 - 0x2687fe0 ]<br />   +0x070 Flags            : 0x1002<br />   +0x074 ForceFlags       : 0<br />   +0x078 CompatibilityFlags : 0<br /><strong><font color="#ff0000">   +0x07c EncodeFlagMask   : 0x100000<br />   +0x080 Encoding         : _HEAP_ENTRY<br /></font></strong>   +0x090 PointerKey       : 0x4d3b4656`7fc766cd<br />   +0x098 Interceptor      : 0<br />   +0x09c VirtualMemoryThreshold : 0xff00<br />   +0x0a0 Signature        : 0xeeffeeff<br />   +0x0a8 SegmentReserve   : 0x200000<br />   +0x0b0 SegmentCommit    : 0x2000<br />   +0x0b8 DeCommitFreeBlockThreshold : 0x400<br />   +0x0c0 DeCommitTotalFreeThreshold : 0x1000<br />   +0x0c8 TotalFreeSize    : 0x315<br />   +0x0d0 MaximumAllocationSize : 0x7ff`fffdefff<br />   +0x0d8 ProcessHeapsListIndex : 8<br />   +0x0da HeaderValidateLength : 0x208<br />   +0x0e0 HeaderValidateCopy : (null) <br />   +0x0e8 NextAvailableTagIndex : 0<br />   +0x0ea MaximumTagIndex  : 0<br />   +0x0f0 TagEntries       : (null) <br />   +0x0f8 UCRList          : _LIST_ENTRY [ 0x00000000`02687fd0 - 0x26e0fd0 ]<br />   +0x108 AlignRound       : 0x1f<br />   +0x110 AlignMask        : 0xffffffff`fffffff0<br />   +0x118 VirtualAllocdBlocks : _LIST_ENTRY [ 0x00000000`02680118 - 0x2680118 ]<br />   +0x128 SegmentList      : _LIST_ENTRY [ 0x00000000`02680018 - 0x2690018 ]<br />   +0x138 AllocatorBackTraceIndex : 0<br />   +0x13c NonDedicatedListLength : 0<br />   +0x140 BlocksIndex      : 0x00000000`02680230 <br />   +0x148 UCRIndex         : 0x00000000`02680a90 <br />   +0x150 PseudoTagEntries : (null) <br />   +0x158 FreeLists        : _LIST_ENTRY [ 0x00000000`02684e80 - 0x26dfc70 ]<br />   +0x168 LockVariable     : 0x00000000`02680208 _HEAP_LOCK<br />   +0x170 CommitRoutine    : 0x4d3b4656`7fc766cd     long  +4d3b46567fc766cd<br />   +0x178 FrontEndHeap     : 0x00000000`02690080 <br />   +0x180 FrontHeapLockCount : 0<br />   +0x182 FrontEndHeapType : 0x2 ''<br />   +0x188 Counters         : _HEAP_COUNTERS<br />   +0x1f8 TuningParameters : _HEAP_TUNING_PARAMETERS<br /><font face="Courier New">0:002&gt; dd 02680000+80                <br />00000000`02680080  00000000 00000000 <strong><font color="#ff0000">775498ca</font></strong> 000041e2<br />00000000`02680090  7fc766cd 4d3b4656 00000000 0000ff00<br />再显示堆块头结构的原始数据：</font></p>
<p><font face="Courier New">0:002&gt; dd 0000000002687fc0  <br />00000000`02687fc0  00000000 00000000 725598ce 030040ec<br />00000000`02687fd0  026e0fd0 00000000 026800f8 00000000<br />00000000`02687fe0  02680060 00000000 02680060 00000000<br />00000000`02687ff0  02688000 00000000 00008000 00000000</font></p>
<p><font face="Courier New">做异或解码：</font></p>
<p><font face="Courier New">0:002&gt; ? 775498ca^725598ce <br />Evaluate expression: 83951620 = 00000000`05010004</font></p>
<p><font face="Courier New">低地址的WORD是0x4，乘上堆的分配力度0x10，是0x40，与扩展命令显示出的也刚好相符。</font></p>
<p><font face="Courier New">就写到这吧，突然想起还有封邮件要写，下次再聊...</font></p>
                
                    <p class="postfoot">
                        posted on 2011年11月10日 22:41
						由
						<a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Entry__ctl0_AuthorLink" href="/user/Profile.aspx?UserID=2122">Raymond</a>
                    </p>                            
</div>              
	

<!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/">
<rdf:Description
rdf:about="http://advdbg.org/blogs/advdbg_system/articles/5152.aspx"
dc:identifier="http://advdbg.org/blogs/advdbg_system/articles/5152.aspx"
dc:title="解读编码后的HEAP_ENTRY结构"
trackback:ping="http://advdbg.org/blogs/trackback.aspx?PostID=5152" />
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
	
		<h4><a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Comments__ctl0_Comments_PermaLink_0" title="permalink" href="/blogs/advdbg_system/articles/5152.aspx#5155">#</a>
		    <span>re: 解读编码后的HEAP_ENTRY结构<a name="5155"></a> @ 2011年11月11日 9:32</span>
		</h4>
		
		        这篇文章不得不顶！！！！！！！！！！！！！！！！
				
				
				<p class="posteds">	
				<a id="_ctl0__ctl0__ctl0__ctl0__ctl0__ctl0_Comments__ctl0_Comments_NameLink_0" title="lee0ne" target="_blank">lee0ne</a>
				
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