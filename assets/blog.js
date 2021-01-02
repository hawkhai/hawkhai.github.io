// https://github.com/michael-lynch/scrollgress
!function(s){s.fn.scrollgress=function(o){if(!this.length)return this;var t={height:"5px",color:"#ff0000",success:function(){}},r=this;r.settings={},r.settings=s.extend({},t,o);var e=r.settings,l=s(this),i=l.css("overflow"),c=l.css("overflow-y"),n="auto"===i||"scroll"===i||"auto"===c||"scroll"===c?!0:!1,g=s(window).outerHeight(),h=n?l[0].scrollHeight:l.height(),d=n?l:s(window),a='<div class="scrollgress"><div class="scrollgress__progress"></div></div>';s("body").prepend(a),s(".scrollgress").css({position:"fixed",top:"0px",left:"0px",background:"transparent",width:"100%",height:e.height}),s(".scrollgress__progress").css({"float":"left",background:e.color,width:"0%",height:e.height}),d.scroll(function(o){var t=n?l.scrollTop():s(document).scrollTop(),r=(t/(h-g)*100).toFixed(2);/*console.log(o.originalEvent),*/s(".scrollgress__progress").css({width:r+"%"})}),e.success.call(this)}}(jQuery);

function addBackToTop(){var o,t,e,n,i=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},r=i.backgroundColor,d=void 0===r?"#000":r,a=i.cornerOffset,c=void 0===a?20:a,s=i.diameter,l=void 0===s?56:s,u=i.ease,p=void 0===u?function(o){return.5*(1-Math.cos(Math.PI*o))}:u,m=i.id,h=void 0===m?"back-to-top":m,b=i.innerHTML,v=void 0===b?'<svg viewBox="0 0 24 24"><path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"></path></svg>':b,f=i.onClickScrollTo,x=void 0===f?0:f,w=i.scrollContainer,g=void 0===w?document.body:w,k=i.scrollDuration,y=void 0===k?100:k,T=i.showWhenScrollTopIs,M=void 0===T?1:T,z=i.size,E=void 0===z?l:z,C=i.textColor,L=void 0===C?"#fff":C,N=i.zIndex,I=void 0===N?1:N,A=g===document.body,B=A&&document.documentElement;o=Math.round(.43*E),t=Math.round(.29*E),e="#"+h+"{background:"+d+";-webkit-border-radius:50%;-moz-border-radius:50%;border-radius:50%;bottom:"+c+"px;-webkit-box-shadow:0 2px 5px 0 rgba(0,0,0,.26);-moz-box-shadow:0 2px 5px 0 rgba(0,0,0,.26);box-shadow:0 2px 5px 0 rgba(0,0,0,.26);color:"+L+";cursor:pointer;display:block;height:"+E+"px;opacity:1;outline:0;position:fixed;right:"+c+"px;-webkit-tap-highlight-color:transparent;-webkit-touch-callout:none;-webkit-transition:bottom .2s,opacity .2s;-o-transition:bottom .2s,opacity .2s;-moz-transition:bottom .2s,opacity .2s;transition:bottom .2s,opacity .2s;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;width:"+E+"px;z-index:"+I+"}#"+h+" svg{display:block;fill:currentColor;height:"+o+"px;margin:"+t+"px auto 0;width:"+o+"px}#"+h+".hidden{bottom:-"+E+"px;opacity:0}",(n=document.createElement("style")).appendChild(document.createTextNode(e)),document.head.insertAdjacentElement("afterbegin",n);var D=function(){var o=document.createElement("div");return o.id=h,o.className="hidden",o.innerHTML=v,o.addEventListener("click",function(o){o.preventDefault(),function(){var o="function"==typeof x?x():x,t=window,e=t.performance,n=t.requestAnimationFrame;if(y<=0||void 0===e||void 0===n)return q(o);var i=e.now(),r=j(),d=r-o;n(function o(t){var e=Math.min((t-i)/y,1);q(r-Math.round(p(e)*d)),e<1&&n(o)})}()}),document.body.appendChild(o),o}(),H=!0;function S(){j()>=M?function(){if(!H)return;D.className="",H=!1}():function(){if(H)return;D.className="hidden",H=!0}()}function j(){return g.scrollTop||B&&document.documentElement.scrollTop||0}function q(o){g.scrollTop=o,B&&(document.documentElement.scrollTop=o)}(A?window:g).addEventListener("scroll",S),S()}

// https://www.cnblogs.com/kikyoqiang/p/12394759.html
function changePositionk() {
    var cluster = $("#section_cluster");
    var snapshot = $("font.ref_snapshot");
    if (!cluster.length || !snapshot.length) return;
    cluster.insertBefore(snapshot);
}

function installReadingBar() {
    $('body').scrollgress({
        height: '1.5px',
        color: '#b6321c'
    });
}

function calcShortUrlx() {
    if (typeof shortSeed === 'undefined') {
        return;
    }
    var hash = md5(shortSeed).substr(0, 8);
    var urlx = shortPrex + hash;
    console.log(urlx);

    var node = $("#short_urlx");
    node.text(urlx);
    node.attr("href", urlx);
}

function setupBackToTop() {
    addBackToTop({
        diameter: 40,
        backgroundColor: '#ddd',
        textColor: 'red'
    });
}

function checkVideo() {
    var postdiv = $("#postdiv");
    var iframevideo = $(".iframevideo");
    iframevideo.css("width", "" + postdiv.width() + "px");
    iframevideo.css("height", "" + (postdiv.width()*480/852) + "px");
}

function setTableStyle(ithis, ratiostr, tablew) {

    if (tablew) {
        ithis.css('width', tablew);
    }

    var li = ratiostr.split(":"); // ["2", "3", "4", "5"]
    var total = 0;
    for (var i = 0; i < li.length; i++) {
        li[i] = parseInt(li[i]);
        total += li[i];
    }
    if (total <= 0) {
        return;
    }
    for (var i = 0; i < li.length; i++) {
        li[i] = li[i] / total * 100;
        var selector = 'th:nth-of-type(' + (i+1) + '),td:nth-of-type(' + (i+1) + ')';
        var width = li[i] + '%';
        // th:nth-of-type(n+2) -- 支持表达式 n+2 之类的
        // https://www.w3school.com.cn/cssref/css_selectors.asp
        ithis.find(selector).each(function() {
            $(this).css('width', width);
        });
    }
}

if (typeof $.fn.tsNumber === 'undefined') {
    $.fn.tsNumber = 0;
}

// 把 glslCanvas 前面一个的 glsl 脚本加载起来。
function checkGlslCanvas() {
    var nodePre = null;
    var nodeCanvas = null;
    $("div.language-glsl pre, canvas.glslCanvas").each(function() {
        var $this = $(this);
        if ($this[0].tagName.toUpperCase() == "PRE") {
            nodePre = $this;
            return;
        } else if ($this[0].tagName.toUpperCase() == "CANVAS") {
            nodeCanvas = $this;
        } else {
            return;
        }

        if (!nodePre || !nodeCanvas) {
            return;
        }

        var fragCode = nodePre.text();
        if (nodeCanvas.attr("data-fragment-url")) {
            return;
        }

        nodeCanvas.attr("data-fragment", fragCode);
        if (typeof GlslCanvas === 'undefined') {
            return;
        }

        var canvas = nodeCanvas[0];
        var sandbox = new GlslCanvas(canvas);
        // sandbox.load(fragCode);
        var vertCode = "attribute vec4 a_position; main(){\ggl_Position = a_position;\n}\n";
        // sandbox.load(fragCode, vertCode);
        // sandbox.setUniform("u_texture", "data/texture.jpg");
    });
}

// 支持语法：<table class="tablestyle" ntablew="2:3:5"></table>
function checkTableStyle() {
    // 先给所有 table 编号。
    $("table").each(function() {
        var $this = $(this);
        if (!$this.attr("tsNumbered")) {
            $this.attr("tsNumbered", 1);
            var number = $.fn.tsNumber;
            $.fn.tsNumber++;
            $this.attr("tsNumber", number);
        }
    });
    $("table.tablestyle").each(function() {
        var $this = $(this);
        var ratiostr = $this.attr("ntablew");
        var number = parseInt($this.attr("tsNumber"));
        var tablew = $this.attr("tablew");
        $this.remove(); // $this.hide();
        if (!ratiostr) {
            return;
        }

        $("table").each(function() {
            var ithis = $(this);
            var inumber = parseInt(ithis.attr("tsNumber"));
            // 紧接着的那个 table
            if (inumber == number + 1) {
                setTableStyle(ithis, ratiostr, tablew);
            }
        });
    });
}

function getQueryValue(queryName) {
    var query = decodeURI(window.location.search.substring(1));
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == queryName) { return pair[1]; }
    }
    return null;
}

function checkFlowChart() {
    if (!getQueryValue("nochart")) {
        return;
    }
    $("div.mermaid").each(function() {
        var $this = $(this);
        var imagek = $this.attr("image");
        $this.remove(); // $this.hide();
    });
}

function checkHrefTagk() {
    $(".post a[href^=http]").each(function() {
        var $this = $(this);
        var href = $this.find("> img.domaintag");
        if (!href.length) {
            $this.addClass("ahref_withimg");
        }
    });
    // https://blog.csdn.net/leewhoee/article/details/20520981
    return;
}

// 文档加载完成时
$(document).ready(function () {
    checkVideo();
    checkTableStyle();
    checkGlslCanvas();
    setupBackToTop();
    setTimeout("installReadingBar()", 1000);
    calcShortUrlx();
    checkFlowChart();
    changePositionk();
    checkHrefTagk();
    // https://github.com/jieyou/lazyload
    // $("img.lazyload").lazyload({effect: "fadeIn"});
    $("img.lazyload").lazyload({threshold: 1000, effect: "show", failurelimit: 10});
});
// 窗口大小变化时
$(window).resize(function () {
    checkVideo();
});
