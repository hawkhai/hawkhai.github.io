<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" lang="en"><head>
    <meta charset="UTF-8" />
    <title>YouTube视频下载 - 存图宝</title>
    <meta name="keywords" content="YouTube视频下载,怎么下载YouTube视频,存图宝" />
    <meta name="description" content="存图宝支持YouTube视频下载，在存图宝粘贴YouTube视频链接，即可一键下载多种分辨率视频：360p、720p、1080p等多种视频格式，请先确保您的浏览器能正常访问YouTube，才能下载视频" />
    <link rel="stylesheet" href="css/publicSty.css?v=1.0.1" />
    <link rel="stylesheet" href="css/top_bot.css?v=1.0.3" />
    <link rel="stylesheet" href="css/index.css?v=1.2" />
    <link rel="shortcut icon" href="images/favicon.ico" />
    <link rel="bookmark" href="images/favicon.ico" />
    <script src="https://hm.baidu.com/hm.js?e65712bbebd077bb7c0a4bf23d5f308a"></script><script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?e65712bbebd077bb7c0a4bf23d5f308a";
      var s = document.getElementsByTagName("script")[0]; 
      s.parentNode.insertBefore(hm, s);
    })();
    </script>
    <style type="text/css">
        /*.nav .logo {width: 300px;} youtube- */
        .banner_inner h3 {font-size: 30px;padding: 28px 0;}
        p.link-tip {color: #AAA;font-size: 14px; margin-bottom: 24px;}
        .banner_search {margin-bottom: 10px;}
    </style>
<link rel="stylesheet" href="https://ctb.doutui.net/js/theme/default/layer.css?v=3.1.1" id="layuicss-layer" /></head>

<body>
    <!-- nav -->
    <div class="nav">
        <div class="container flex_between">
            <div class="nav_left flex_center">
                <a href="https://cuntubao.com" class="logo_link">
                    <img src="images/logo.png" alt="存图宝" class="logo" />
                </a>
            </div>
            <div class="nav_right flex_center">
                <a class="nav_icon" id="login" href="https://cuntubao.com">登录</a>
                <div class="nav_icon vip_center"><span id="user_name_top"></span> , 会员中心 </div>
                <!-- 双11活动 -->
                <!--
                <div class='nav_icon vip_center'><span id="user_name_top"></span> , 会员中心 
                  <em>，双11活动</em>
                </div>
                 -->
                <div class="nav_icon" id="login_out">退出登录</div>
                <div class="nav_icon collect">收藏网站</div>
                <a class="nav_icon contact_txt">联系客服:</a>
                <a target="_blank" class="contact_icon" href="https://cuntubao.com/kefu.html"><img border="0" src="https://pub.idqqimg.com/qconn/wpa/button/button_111.gif" alt="点击这里给我发消息" title="点击这里给我发消息" /></a>
            </div>
        </div>
    </div>
    <div class="banner flex_mid">
        <div class="banner_inner">
            <h3><img src="images/youtube-title.png" title="YouTube视频下载" /></h3>
            <div class="banner_search flex_center">
                <input type="text" placeholder="粘贴链接，如：https://www.youtube.com/watch?v=0Cbtye7perg" id="search_input" />
                <div class="banner_search_btn" id="search_btn">下载视频</div>
            </div>
            <p class="link-tip">请先确保您的浏览器能正常访问YouTube，才能下载视频 <a style="display: inline;color: blue" target="_blank" href="https://cdn.doutui.net/ctb/web/img/youtube.png">查看演示</a></p>
            <p>存图宝还支持Instagram、Facebook、抖音、快手等去水印视频下载，请访问：<a style="display: inline;color: #275ef8" href="https://cuntubao.com">cuntubao.com</a></p>
            <p id="chrome_tip">浏览器不支持该网站，请使用最新版谷歌浏览器: <a target="_blank" href="http://www.mydown.com/soft/421/472030921.shtml">下载谷歌浏览器</a></p>
        </div>
        <div class="banner_tip"></div>
        
    </div>
    <!-- nav end-->
    <div class="footer">
        <div class="container flex_mid">
                        <div class="link">
                <a class="link_item" href="/">首页</a>
                <a class="link_item" href="http://www.doutui.net/intro.html" target="_blank">公司简介</a>
                <a class="link_item" href="http://www.doutui.net/about.html" target="_blank">关于我们</a>
                <a class="link_item link_no_border" href="http://www.doutui.net/contact.html" target="_blank">联系我们</a>
                <div class="clear"></div>
            </div>
            <div class="copy">
                <a>© 2019 重庆顺流科技有限公司 渝ICP备19003700号-4 </a>
            </div>
                    </div>
    </div>
    <!-- vip -->
    <div class="vip_modal flex_center" id="vip_modal">
      <div class="vip_modal_inner" id="vip_modal_inner">
        <img src="" alt="" class="user_img" id="user_img" />
        <div class="user_name flex_center">
          <img src="images/vip.png" alt="" id="vip_typeicon" />
          <span id="user_name">未知</span>
        </div>
        <h5 class="vip_id" id="vip_id">ID：未知</h5>
        <h4 class="vip_tip" id="vip_tip">您是VIP会员，到期时间：未知</h4>
        <div class="price_list flex_center" id="price_list">

        </div>
        <div class="pay_des flex_center">
          <img src="images/wx.png" alt="" />
          <span>微信支付</span>
        </div>
        <div id="pay_img" class="pay_img">
          <div class="pay_code_ab flex_mid" id="pay_code_ab">
            <span>每人仅可参与1次</span>
          </div>
        <canvas width="160" height="160"></canvas><img style="display: none;" /></div>
        <p class="price_des flex_center" id="price_des">支付金额
          <span></span>
          元 
          <!--<em id="spe_paytip">，获得24个月会员</em>--></p>
        <!--
        <p class="only_span_tip" id="only_span_tip">双11活动（9日-11日），每人仅可参与1次</p>
        -->
        <p class="vip_timer" id="vip_timer">开通 个月会员，到期时间：未知</p>
        <div class="pro_des">
          <em>注：</em>
          <span>存图宝会限制大批量、高频率的专业采集，若有专业采集需求请</span>
          <a href="https://pro.cuntubao.com" target="_blank">使用专业版</a>
        </div>
        <img src="images/close.png" alt="" class="close" id="close_btn" />
      </div>
    </div>
    <!-- 登录 -->
    <div class="code_modal flex_center" id="code_modal">
        <div class="code_modal_inner flex_mid" id="code_modal_inner">
            <img src="images/code_login.png" alt="" id="code_ajaximg" />
            <span>微信扫码关注，自动登录存图宝</span>
        </div>
    </div>
    <!-- 收藏 -->
    <div class="collect_modal flex_center" id="collect_modal">
        <div class="collect_modal_inner" id="collect_modal_inner">
            <div class="collect_scroll">
                <div class="collect_title">
                    <span>方法一: </span>按 <em id="btn_name">Ctrl + D</em> 将网站添加到收藏夹，下次使用时，直接从书签栏选择
                </div>
                <img src="images/sc.png" alt="" />
                <div class="collect_title">
                    <span>方法二: </span>记住我们的域名是“存图宝”全拼: <a href="cuntubao.com"> cuntubao.com </a>,直接在浏览器输入
                </div>
                <img class="ht" src="images/wz.png" alt="" />
                <div class="collect_title">
                    <span>方法三: </span> 如果忘记了网址，可以在微信里搜索 <span>“存图宝”公众号</span>, 可以在公众号找到我们的网站地址
                </div>
                <img src="images/co3.png" alt="" />
            </div>
            <img src="images/close.png" alt="" id="collect_close" />
        </div>
    </div>

<script>     
    try {
      new Function('const a = 4'); 
    } catch (e) {
      alert('当前浏览器不支持该网站，请使用最新版谷歌浏览器');
      window.location.href= 'download.html';
    }
</script>
<script type="text/javascript" src="js/jquery-1.11.3.min.js"></script>
<script type="text/javascript" src="js/qrcode.min.js"></script>
<script type="text/javascript" src="js/vip.js?v=1.2"></script>
<script type="text/javascript" src="js/layer.js"></script>
<script type="text/javascript" src="js/api.js?v=1.2"></script>
<script type="text/javascript" src="js/index.js?v=1.2"></script>
<script>
    var domain = document.domain;
    console.log(domain);
    if(domain.indexOf('yuankan.net') &gt; -1) {
        let visitorId = localStorage.visitorId;
        if (!visitorId) {
            logVisitor('register');
        } else {
            logVisitor('visit_index_page');
        }
    }

    var promotion_code = getLinkValue('code');
    if(!!promotion_code){
      localStorage.code = promotion_code;
    }   

    var browser = myBrowser();
    if(browser != "Safari" &amp;&amp; browser != "Chrome") {
      $('#chrome_tip').show();  //提示下载Chrome浏览器
    }

    setTimeout(function () {
        document.getElementById('search_input').focus();
    }, 200);

    $('#search_btn').on('click', function () {
        var inputTxt = $('#search_input').val();
        if (inputTxt == '') {
            layer.msg('请在输入框粘贴链接');
        } else {
            getData(inputTxt)
        }
    })
    $('#search_input').bind('keydown', function (res) {
        if (res.keyCode == 13) {
            var inputTxt = $('#search_input').val();
            if (inputTxt == '') {
                layer.msg('请在输入框粘贴链接');
            } else {
                getData(inputTxt)
            }
        }
    })
    //获取素材信息
    function getData(inputTxt) {
        try {
          new Function('const a = 4'); 
        } catch (e) {
          alert('当前浏览器不支持该网站，请升级浏览器或下载最新版Chrome浏览器')
          window.location.href= 'download.html'
          return;
        }   
        var token = localStorage.token;
        //如果token存在
        if (!!token) {
            localStorage.dataUrl = inputTxt;
            //请求成功
            window.location.href = 'data.html'
            //token不存在
        } else {
            //判断是否为首次请求
            let getdataNum = 1;
            //如果为第一次请求(token为临时token)
            if (!getdataNum) {
                localStorage.dataUrl = inputTxt;
                //请求成功
                window.location.href = 'data.html'
            } else {
                //如果token不存在，提示登录
                layerComment('获取素材，请先扫码登录！')
                setTimeout(() =&gt; {
                    showLoginCode('index', inputTxt)
                }, 1000)
            }
        }
    }
    var myBrowserName = myBrowser();
    if (myBrowserName == 'Safari') {
        $('.banner_tip span').html('Comand + D')
        $('#btn_name').html('Comand + D')
    } else {
        $('.banner_tip span').html('Ctrl + D')
        $('#btn_name').html('Ctrl + D')
    }
    //输入框获取焦点事件
    $("#search_input").focus(function () {

        let url = $('#search_input').val();
        //临时地址
        temporaryInputTxt = url;
        $('#search_input').val('');
    });
    $("#search_input").blur(function () {
        let url = $('#search_input').val();
        if (!url) {
            $('#search_input').val(temporaryInputTxt);
        }
    });
    var token = localStorage.token ? localStorage.token : ''
    //如果token存在
    if (!!token) {
        $('#login').hide();
        $('#phone_code').hide();
        $('.vip_center').css('display','flex');
        var newUserinfo = localStorage.userinfo;
        newUserinfo = newUserinfo ? JSON.parse(newUserinfo) : '';
        $('#user_name_top').html(newUserinfo.nickname);
        $('#user_name_top').show();
        $('#login_out').show();
        //验证token
        productList(token).then(res =&gt; {
            let code = res.code;
            //登录失效，需要重新登录
            if (code != 200) {
                layerComment(res.msg)
                setTimeout(() =&gt; {
                    showLoginCode()
                }, 1000)
                $('#login').show();
                $('.vip_center').hide();
                $('#login_out').hide();
            }
        })
    }
</script>


</body></html>