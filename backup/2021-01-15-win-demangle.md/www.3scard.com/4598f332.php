<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en" class="screen-tablet device-mobile m-blog m-blog-view"><head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <title>调用约定(Calling Conventions) (__cdecl、__stdcall、__fastcall) C++函数名修饰(Name Mangling) - 通用C++ - 深圳市三艾斯科技有限公司</title>
<meta name="keywords" content="调用约定(Calling,Conventions),(,cdecl,stdcall,fastcall),C,函数名修饰(Name,Mangling)  JAVA卡 JavaCard 购买 销售 深圳市三艾斯科技有限公司" />
<meta name="description" content="调用约定(Calling Conventions) (__cdecl、__stdcall、__fastcall) C++函数名修饰(Name Mangling)" />
<link rel="stylesheet" href="/zui/css/min.css?v=3.1" type="text/css" media="screen" />
<link rel="stylesheet" href="/template/default/theme/common/style.css?v=3.1" type="text/css" media="screen" />
<link rel="stylesheet" href="/js/jquery/treeview/min.css?v=3.1" type="text/css" media="screen" />
<link rel="stylesheet" href="/data/css/default/default/style.css??v=3.1" type="text/css" media="screen" />
<script language="Javascript">var config={"webRoot":"\/","cookieLife":30,"requestType":"GET","requestFix":"-","moduleVar":"m","methodVar":"f","viewVar":"t","defaultView":"html","themeRoot":"\/theme\/","currentModule":"blog","currentMethod":"view","clientLang":"zh-cn","requiredFields":"","save":"\u4fdd\u5b58","router":"\/index.php","runMode":"front"}
</script>
<script src="/js/all.js?v=3.1" type="text/javascript"></script>
<style>.a-left{text-align: left;}
.a-right{text-align: right;}
#commentBox .page{padding: 8px 0;}
.sina-widget{display: inline-block;margin: -2px -15px 0 0;padding: 0;line-height: 1;vertical-align: top;}
</style><link rel="icon" href="/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<link href="/index.php?m=rss&amp;f=index&amp;t=xml" title="深圳市三艾斯科技有限公司" type="application/rss+xml" rel="alternate" /><script language="Javascript">if(typeof(v) != "object") v = {};v.lang = {"confirmDelete":"\u60a8\u786e\u5b9a\u8981\u6267\u884c\u5220\u9664\u64cd\u4f5c\u5417\uff1f","deleteing":"\u5220\u9664\u4e2d","doing":"\u5904\u7406\u4e2d","loading":"\u52a0\u8f7d\u4e2d","timeout":"\u7f51\u7edc\u8d85\u65f6,\u8bf7\u91cd\u8bd5"};</script>
<!--[if lt IE 9]>
<script src='/js/all.ie8.js?v=3.1' type='text/javascript'></script>
<![endif]-->
<!--[if lt IE 10]>
<script src='/js/all.ie9.js?v=3.1' type='text/javascript'></script>
<![endif]-->
<style>body{ font-family:'\5FAE\8F6F\96C5\9ED1'; }</style></head>
<body style="zoom: 1;">
<div class="page-container page-blog">
  <header id="header" class="clearfix">
    <div id="headNav" class="hide"><div class="wrapper"></div></div>
    <div id="headTitle">
      <div class="wrapper">
                        <div id="siteLogo">
          <a href="/"><img src="/data/upload/201410/f_da20874cdb596235026ac4e253c4fea2.jpg" class="logo" title="深圳市三艾斯科技有限公司" />
</a>
        </div>
              </div>
    </div>
  </header>
  <nav id="blogNav" class="navbar navbar-default" role="navigation">
    <div class="wrapper">
      <ul class="nav navbar-nav">
        <li>
           <a href="/index.php?m=blog&amp;f=index">博客首页</a>
        </li>
        <li class="nav-blog-14"><a href="/index.php?m=blog&amp;f=index&amp;id=14">随笔</a>
</li><li class="nav-blog-17"><a href="/index.php?m=blog&amp;f=index&amp;id=17">商业</a>
</li><li class="nav-blog-42"><a href="/index.php?m=blog&amp;f=index&amp;id=42">安全</a>
</li><li class="nav-blog-8 active"><a href="/index.php?m=blog&amp;f=index&amp;id=8">C++</a>
</li><li class="nav-blog-36"><a href="/index.php?m=blog&amp;f=index&amp;id=36">WEB</a>
</li><li class="nav-blog-11"><a href="/index.php?m=blog&amp;f=index&amp;id=11">JAVA</a>
</li><li class="nav-blog-10"><a href="/index.php?m=blog&amp;f=index&amp;id=10">Python</a>
</li><li class="nav-blog-12"><a href="/index.php?m=blog&amp;f=index&amp;id=12">Linux</a>
</li><li class="nav-blog-13"><a href="/index.php?m=blog&amp;f=index&amp;id=13">其他</a>
</li>      </ul>
            <ul class="nav navbar-nav navbar-right">
        <li><a href="/"><i class="icon-home icon-large"></i> 网站首页</a>
</li>
      </ul>
          </div>
  </nav>
  <div class="page-wrapper">
    <div class="page-content">
<script language="Javascript">v.path = [8,23];</script>
<script language="Javascript">v.categoryID = 23;</script>
<script language="Javascript">v.articleID = 10;</script>
<style></style><script language="Javascript">
</script>
<script language="javascript">$(function() {$(".tree").treeview({collapsed: false, unique: false}) })</script>
<ul class="breadcrumb"><li>当前位置：<a href="/index.php?m=blog&amp;f=index">博客首页</a>
</li><li><a href="/index.php?m=blog&amp;f=index&amp;moduleID=8">C++</a>
</li><li><a href="/index.php?m=blog&amp;f=index&amp;moduleID=23">通用C++</a>
</li><li>调用约定(Calling Conventions) (__cdecl、__stdcall、__fastcall) C++函数名修饰(Name Mangling)</li></ul><div class="row">
  <div class="col-md-9 col-main">
    <div class="article">
      <header>
        <h1>调用约定(Calling Conventions) (__cdecl、__stdcall、__fastcall) C++函数名修饰(Name Mangling)</h1>
        <dl class="dl-inline">
          <dd data-toggle="tooltip" data-placement="top" data-original-title="&lt;strong&gt;添加时间：&lt;/strong&gt; 2015-03-21 11:48:00   "><i class="icon-time icon-large"></i> 2015-03-21 11:48:00</dd>
          <dd data-toggle="tooltip" data-placement="top" data-original-title="&lt;strong&gt;作者：&lt;/strong&gt; admin   "><i class="icon-user icon-large"></i> admin</dd>
                    <dd class="pull-right">
                            <span class="label label-success">原创</span>            <span class="label label-warning" data-toggle="tooltip" data-placement="top" data-original-title=" &lt;strong&gt;阅读：&lt;/strong&gt;3436"><i class="icon-eye-open"></i> 3436</span>
          </dd>
        </dl>
                <section class="abstract"><strong>摘要</strong>：调用约定(Calling Conventions) (__cdecl、__stdcall、__fastcall) C++函数名修饰(Name Mangling)</section>
              </header>
      <section class="article-content">
        <p><strong><span style="font-size:16px;">一、</span></strong><span style="font-size:16px;"><strong>如何申明调用约定</strong></span></p>
<p>Windows下的调用约定可以是__<span>cdecl、<span>__</span><span>stdcall</span>、<span>__</span></span>fastcall，这些标识加在函数名前面，如：</p>
int <span>__</span><span>cdecl </span>myFunc();<br />
<br />
但在Linux下，如按照上面写法后，编译程序将导致编译错误，Linux下正确的语法如下：<br />
int __attribute__((<span>cdecl</span>)) <span>myFunc</span>();<br />
int __attribute__((<span><span>stdcall</span></span><span></span>)) <span>myFunc</span>();<br />
<p>Linux下如果函数不指定调用约定，默认的情况应该是__attribute__((<span>cdecl</span>))</p>
<p><br />
</p>
<p>IDE一般可以对项目整体进行默认调用约定设置。</p>
<p><br />
</p>
<p><strong><span style="font-size:16px;">二、如何使用调用约定</span></strong></p>
<p>函数的<span>调用约定</span>，大多数时候不需要了解，但如果需要跨语言的编程（C++调用C库需要使用extern "C"进行说明），则需要了解。</p>
<p><br />
</p>
<p>Microsoft的VC默认的是__cdecl，而Windows API则是__stdcall，如果用VC开发DLL给其他语言用，则应该指定__stdcall方式。堆栈由谁清除这个很重要，写汇编函数给C调用，一定要小心堆栈的清除工作，如果是__cdecl方式调用，汇编函数本身不需要关心保存参数的堆栈清除，如果是__stdcall方式调用，一定要在函数退出(ret)前恢复堆栈。</p>
<p><br />
</p>
<p><strong>1.__cdecl</strong><br />
        按从右至左的顺序压参数入栈，由调用者把参数弹出栈。切记：对于传送参数的内存栈是由调用者来维护的，返回值在EAX中。因此对于像printf这样可变参数的函数必须用这种约定。编译器在编译的时候对这种调用规则的函数生成修饰名的时候，在输出函数名前加上一个下划线前缀，格式为_function。<br />
<strong>2.__stdcall </strong><br />
        按从右至左的顺序压参数入栈，由被调用者把参数弹出栈。__stdcall通常用于Win32 API中，切记：函数自己在退出时清空堆栈，返回值在EAX中。__stdcall调用约定在输出函数名前加上一个下划线前缀，后面加上一个“@”符号和其参数的字节数，格式为_function@number。如函数int func(int a, double b)的修饰名是_func@12。<br />
<strong>3.__fastcall</strong><br />
       __fastcall调用的主要特点就是快，因为它是通过寄存器来传送参数的（实际上它用ECX和EDX传送前两个DWORD或更小的参数，剩下的参数仍自右向左压栈传送，被调用的函数在返回前清理传送参数的内存栈）。__fastcall调用约定在输出函数名前加上一个“@”符号，后面也是一个“@”符号和其参数的字节数，格式为@function@number。这个和__stdcall很象，唯一差别就是头两个参数通过寄存器传送。注意通过寄存器传送的两个参数是从左向右的，即第1个参数进ECX，第2个进EDX，其他参数是从右向左的入栈，返回仍然通过EAX。</p>
<p><br />
</p>
<p><strong><span style="font-size:16px;">三、C++函数名修饰（</span></strong><strong><span style="font-size:16px;">Decorated Names，</span></strong><strong><span style="font-size:16px;">Name Mangling</span></strong><strong><span style="font-size:16px;">）</span></strong></p>
<p>1.以"?"标识函数开始，后跟函数名。</p>
<p>2.函数名后面标识调用约定，然后跟参数列表。</p>
<p> __cdecl，@@YA</p>
<p> __stdcall，@@YG</p>
<p> __fastcall，@@YI</p>
<p>3.参数类型代号编码。</p>
<p> X--void<br />
 D--char<br />
 E--unsigned char<br />
 F--short<br />
 H--int<br />
 I--unsigned int<br />
 J--long<br />
 K--unsigned long<br />
 M--float<br />
 N--double</p>
<p>4.参数表第一项为该函数的返回值类型。<br />
5.参数表后以"@Z"标识整个函数名结束，如果该函数无参数，则以"Z"标识结束。</p>
<p>6.比如：“?a@@YAHD@Z”原函数为“int __cdecl a(char)”。</p>
<p><img src="/data/upload/201503/f_53837a9a2b32da06c4da07476dee9613.png" alt="" /></p>
<p><br />
</p>
<p><strong><span style="font-size:16px;">四、附件下载</span></strong></p>
<p><span style="font-size:14px;"><span style="font-size:14px;">Name Mangling解析工具</span></span><span style="font-size:14px;">，界面如上截图：</span><span style="line-height:1.57142857;"><span style="font-size:14px;"><a href="/data/download/dem.rar" target="_blank">dem.rar</a></span></span></p>
<p><span style="line-height:1.57142857;"><span>Name Mangling解析工具</span><span>，命令行版本：<a href="/data/download/undname.rar" target="_blank">undname.rar</a></span><br />
</span></p>
<p><span style="line-height:1.57142857;"><span>可执行文件(exe、dll、lib)解析工具</span><span>：<a href="/data/download/dumpbin.rar" target="_blank">dumpbin.rar</a></span>  -  dumpbin /EXPORTS /IMPORTS filename<br />
</span></p>
<p><br />
</p>
<p><strong>Linux下常用工具：</strong></p>
<p><strong>objdump</strong><strong>：</strong></p>
<p><span>  objdump -d elf-file 反汇编.text段</span></p>
<p><span><span>  objdump -S elf-file 同时显示源码和反汇编</span><br />
</span></p>
<p><span>  objdump -x elf-file 查看elf文件分段信息</span></p>
<p><span>  objdump -h elf-file 查看elf文件section的信息</span></p>
<p>  objdump -a elf-file 显示归档信息</p>
<p><span><strong>nm</strong><strong>：</strong></span></p>
<p><span>  nm <span>elf-file 显示符号表信息，常用于解决链接错误。</span></span></p>      </section>
      <section>
        <ul class="files-list clearfix"></ul>      </section>
      <footer>
                <p class="small"><strong class="text-muted">关键字</strong><span class="article-keywords">：调用约定(Calling,Conventions),(,cdecl,stdcall,fastcall),C,函数名修饰(Name,Mangling)</span></p>
                        <ul class="pager pager-justify">
                    <li class="previous"><a href="/index.php?m=blog&amp;f=view&amp;id=9"><i class="icon-arrow-left"></i> C++模板常见问题和技巧</a>
</li>
                              <li class="next"><a href="/index.php?m=blog&amp;f=view&amp;id=139">RapidJSON使用简介 <i class="icon-arrow-right"></i></a>
</li>
                  </ul>
      </footer>
    </div>
    <div id="commentBox"></div>
  </div>
  <div class="col-md-3 col-side"><side class="page-side"><div class="panel-pure panel"><a href="/index.php?m=rss&amp;f=index&amp;t=xml&amp;?type=blog" target="_blank" class="btn btn-lg btn-block"><i class="icon-rss text-warning"></i> 订阅博客</a>
</div><div id="block8" class="panel panel-block ">
  <div class="panel-heading">
    <strong><i class="icon-folder-close"></i> 博客分类</strong>
  </div>
  <div class="panel-body"><ul class="tree treeview"><li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=14" id="category14">随笔</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=48" id="category48">小知识大用处</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=47" id="category47">宏观微观局</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=18" id="category18">关于非能</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=54" id="category54">管理学</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=52" id="category52">典故</a>

</li>
</ul>
</li>
<li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=17" id="category17">商业</a>
<ul><li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=51" id="category51">金融知识</a>

</li>
</ul>
</li>
<li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=42" id="category42">安全</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=43" id="category43">加解密</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=49" id="category49">openssl</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=46" id="category46">安全专栏</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=45" id="category45">数学</a>

</li>
</ul>
</li>
<li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=8" id="category8">C++</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=23" id="category23" class="active">通用C++</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=24" id="category24">Linux下的C++</a>

</li>
</ul>
</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=36" id="category36">WEB</a>

</li>
<li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=11" id="category11">JAVA</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=38" id="category38">JAVA语言</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=39" id="category39">JAVA常用库</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=44" id="category44">JAVA的IO</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=41" id="category41">JAVA并发</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=40" id="category40">JAVA工具</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=37" id="category37">WEB服务</a>

</li>
</ul>
</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=10" id="category10">Python</a>

</li>
<li class="collapsable"><div class="hitarea collapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=12" id="category12">Linux</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=29" id="category29">批处理</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=30" id="category30">网络</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=28" id="category28">数据</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=21" id="category21">shell语言</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=22" id="category22">系统配置</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=20" id="category20">常用命令</a>

</li>
</ul>
</li>
<li class="collapsable lastCollapsable"><div class="hitarea collapsable-hitarea lastCollapsable-hitarea"></div><a href="/index.php?m=blog&amp;f=index&amp;category=13" id="category13">其他</a>
<ul><li><a href="/index.php?m=blog&amp;f=index&amp;category=25" id="category25">杂项</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=26" id="category26">工具下载</a>

</li>
<li><a href="/index.php?m=blog&amp;f=index&amp;category=53" id="category53">娱乐</a>

</li>
<li class="last"><a href="/index.php?m=blog&amp;f=index&amp;category=35" id="category35">免费虚拟主机</a>

</li>
</ul>
</li>
</ul>
</div>
</div>
<style>#block8{}#block8 .panel-heading{}</style></side></div>
</div>
  </div></div>    <footer id="footer">
    <div class="wrapper">
      <div id="footNav">
        <a href="/index.php?m=rss&amp;f=index&amp;t=xml?type=blog" target="_blank"><i class="icon icon-rss-sign icon-large"></i></a>
      </div>
      <span id="copyright">
        © 2013-2021 深圳市三艾斯科技有限公司        </span>
      <span id="icpInfo">粤ICP备13055486号</span>
    </div>
  </footer>
</div><div id="rightDocker" class="hidden-xs">
    <button id="rightDockerBtn" class="btn" data-toggle="popover" data-placement="left" data-target="$next" data-original-title="" title=""><i class="icon-qrcode"></i></button>
    <div class="popover fade">
    <div class="arrow"></div>
    <div class="popover-content docker-right">
      <table class="table table-borderless">
        <tbody><tr>
                              <td>
            <div class="heading"><i class="icon-mobile-phone"></i> 移动访问</div>
            <img src="javascript:;" width="200" height="200" data-src="/index.php?m=misc&amp;f=qrcode" />
          </td>
                  </tr>
      </tbody></table>
    </div>
  </div>
</div>
<script language="Javascript">$(document).ready(function()
{
    /* Set current active topNav. */
    if(v.path &amp;&amp; v.path.length)
    {
        $.each(v.path, function(index, category) 
        { 
            $('.nav-blog-' + category).addClass('active');
        })
    }

   if(typeof(v.categoryID) != 'undefined') $('.tree #category' + v.categoryID).addClass('active');

   $('body').tooltip(
    {
        html: true,
        selector: "[data-toggle=tooltip]",
        container: "body"
    });
});
$(document).ready(function()
{
    $('#commentBox').load( createLink('message', 'comment', 'objectType=article&amp;objectID=' + v.articleID) );  
});

</script>
<div class="hidden"><script src="http://s96.cnzz.com/z_stat.php?id=1000168455&amp;web_id=1000168455" language="JavaScript"></script><script src="http://c.cnzz.com/core.php?web_id=1000168455&amp;t=z" charset="utf-8" type="text/javascript"></script><a href="https://www.cnzz.com/stat/website.php?web_id=1000168455" target="_blank" title="站长统计">站长统计</a></div><style>#block14{}#block14 .panel-heading{}</style>

</body></html>