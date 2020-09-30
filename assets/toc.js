// https://github.com/stipsan/scroll-into-view-if-needed
!function(e,t){"object"==typeof exports&&"undefined"!=typeof module?module.exports=t():"function"==typeof define&&define.amd?define(t):(e="undefined"!=typeof globalThis?globalThis:e||self).scrollIntoView=t()}(this,(function(){"use strict";function e(e){return null!=e&&"object"==typeof e&&1===e.nodeType}function t(e,t){return(!t||"hidden"!==e)&&"visible"!==e&&"clip"!==e}function n(e,n){if(e.clientHeight<e.scrollHeight||e.clientWidth<e.scrollWidth){var o=getComputedStyle(e,null);return t(o.overflowY,n)||t(o.overflowX,n)||function(e){var t=function(e){if(!e.ownerDocument||!e.ownerDocument.defaultView)return null;try{return e.ownerDocument.defaultView.frameElement}catch(e){return null}}(e);return!!t&&(t.clientHeight<e.scrollHeight||t.clientWidth<e.scrollWidth)}(e)}return!1}function o(e,t,n,o,r,i,l,c){return i<e&&l>t||i>e&&l<t?0:i<=e&&c<=n||l>=t&&c>=n?i-e-o:l>t&&c<n||i<e&&c>n?l-t+r:0}function r(t,r){var i=window,l=r.scrollMode,c=r.block,u=r.inline,f=r.boundary,d=r.skipOverflowHiddenElements,a="function"==typeof f?f:function(e){return e!==f};if(!e(t))throw new TypeError("Invalid target");for(var s=document.scrollingElement||document.documentElement,h=[],p=t;e(p)&&a(p);){if((p=p.parentNode)===s){h.push(p);break}p===document.body&&n(p)&&!n(document.documentElement)||n(p,d)&&h.push(p)}for(var m=i.visualViewport?i.visualViewport.width:innerWidth,g=i.visualViewport?i.visualViewport.height:innerHeight,v=window.scrollX||pageXOffset,w=window.scrollY||pageYOffset,b=t.getBoundingClientRect(),y=b.height,W=b.width,H=b.top,E=b.right,M=b.bottom,T=b.left,V="start"===c||"nearest"===c?H:"end"===c?M:H+y/2,k="center"===u?T+W/2:"end"===u?E:T,x=[],I=0;I<h.length;I++){var O=h[I],j=O.getBoundingClientRect(),B=j.height,C=j.width,D=j.top,L=j.right,R=j.bottom,X=j.left;if("if-needed"===l&&H>=0&&T>=0&&M<=g&&E<=m&&H>=D&&M<=R&&T>=X&&E<=L)return x;var Y=getComputedStyle(O),S=parseInt(Y.borderLeftWidth,10),N=parseInt(Y.borderTopWidth,10),q=parseInt(Y.borderRightWidth,10),z=parseInt(Y.borderBottomWidth,10),A=0,F=0,G="offsetWidth"in O?O.offsetWidth-O.clientWidth-S-q:0,J="offsetHeight"in O?O.offsetHeight-O.clientHeight-N-z:0;if(s===O)A="start"===c?V:"end"===c?V-g:"nearest"===c?o(w,w+g,g,N,z,w+V,w+V+y,y):V-g/2,F="start"===u?k:"center"===u?k-m/2:"end"===u?k-m:o(v,v+m,m,S,q,v+k,v+k+W,W),A=Math.max(0,A+w),F=Math.max(0,F+v);else{A="start"===c?V-D-N:"end"===c?V-R+z+J:"nearest"===c?o(D,R,B,N,z+J,V,V+y,y):V-(D+B/2)+J/2,F="start"===u?k-X-S:"center"===u?k-(X+C/2)+G/2:"end"===u?k-L+q+G:o(X,L,C,S,q+G,k,k+W,W);var K=O.scrollLeft,P=O.scrollTop;V+=P-(A=Math.max(0,Math.min(P+A,O.scrollHeight-B+J))),k+=K-(F=Math.max(0,Math.min(K+F,O.scrollWidth-C+G)))}x.push({el:O,top:A,left:F})}return x}function i(e){return e===Object(e)&&0!==Object.keys(e).length}return function(e,t){var n=!e.ownerDocument.documentElement.contains(e);if(i(t)&&"function"==typeof t.behavior)return t.behavior(n?[]:r(e,t));if(!n){var o=function(e){return!1===e?{block:"end",inline:"nearest"}:i(e)?e:{block:"start",inline:"nearest"}}(t);return function(e,t){void 0===t&&(t="auto");var n="scrollBehavior"in document.body.style;e.forEach((function(e){var o=e.el,r=e.top,i=e.left;o.scroll&&n?o.scroll({top:r,left:i,behavior:t}):(o.scrollTop=r,o.scrollLeft=i)}))}(r(e,o),o.behavior)}}}));

// https://github.com/ghiculescu/jekyll-table-of-contents
(function ($) {
    $.fn.toc = function (options) {
        var defaults = {
            noBackToTopLinks: false,
            title: '<i>Jump to...</i>',
            minimumHeaders: 3,
            headers: 'h1, h2, h3, h4, h5, h6',
            listType: 'ol',
            // values: [ol|ul]
            showEffect: 'show',
            // values: [show|slideDown|fadeIn|none]
            showSpeed: 'slow',
            // set to 0 to deactivate effect
            classes: {
                list: '',
                item: ''
            }
        }
        , settings = $.extend(defaults, options);
        function fixedEncodeURIComponent(str) {
            return encodeURIComponent(str).replace(/[!'()*]/g, function (c) {
                return '%' + c.charCodeAt(0).toString(16);
            });
        }

        function createLink(header) {
            var innerText = (header.textContent === undefined) ? header.innerText : header.textContent;
            return "<a href='#" + fixedEncodeURIComponent(header.id) + "'>" + innerText + "</a>";
        }

        var headers = $(settings.headers).filter(function () {
            // get all headers with an ID
            var previousSiblingName = $(this).prev().attr("name");
            if (!this.id && previousSiblingName) {
                this.id = $(this).attr("id", previousSiblingName.replace(/\./g, "-"));
            }
            return this.id;
        })
                , output = $(this);
        if (!headers.length || headers.length < settings.minimumHeaders || !output.length) {
            $(this).hide();
            return;
        }

        if (0 === settings.showSpeed) {
            settings.showEffect = 'none';
        }

        var render = {
            show: function () {
                output.hide().html(html).show(settings.showSpeed);
            },
            slideDown: function () {
                output.hide().html(html).slideDown(settings.showSpeed);
            },
            fadeIn: function () {
                output.hide().html(html).fadeIn(settings.showSpeed);
            },
            none: function () {
                output.html(html);
            }
        };
        var get_level = function (ele) {
            return parseInt(ele.nodeName.replace("H", ""), 10);
        };
        var highest_level = headers.map(function (_, ele) {
            return get_level(ele);
        }).get().sort()[0];
        var return_to_top = '<i class="icon-arrow-up back-to-top"> </i>';
        var level = get_level(headers[0]), this_level, html = settings.title + " <" + settings.listType + " class=\"" + settings.classes.list + "\">";
        headers.on('click', function () {
            if (!settings.noBackToTopLinks) {
                window.location.hash = this.id;
            }
        }).addClass('clickable-header').each(function (_, header) {
            this_level = get_level(header);
            if (!settings.noBackToTopLinks && this_level === highest_level) {
                $(header).addClass('top-level-header').after(return_to_top);
            }
            if (this_level === level)
                // same level as before; same indenting
                html += "<li class=\"" + settings.classes.item + "\">" + createLink(header);
            else if (this_level <= level) {
                // higher level than before; end parent ol
                for (var i = this_level; i < level; i++) {
                    html += "</li></" + settings.listType + ">"
                }
                html += "<li class=\"" + settings.classes.item + "\">" + createLink(header);
            } else if (this_level > level) {
                // lower level than before; expand the previous to contain a ol
                for (i = this_level; i > level; i--) {
                    html += "<" + settings.listType + " class=\"" + settings.classes.list + "\">" + "<li class=\"" + settings.classes.item + "\">"
                }
                html += createLink(header);
            }
            level = this_level;
            // update for the next one
        });
        html += "</" + settings.listType + ">";
        if (!settings.noBackToTopLinks) {
            $(document).on('click', '.back-to-top', function () {
                $(window).scrollTop(0);
                window.location.hash = '';
            });
        }

        render[settings.showEffect]();
    }
    ;
}
)(jQuery);

function getClientHeight() {
    var clientHeight = 0;
    if (document.body.clientHeight && document.documentElement.clientHeight) {
        clientHeight = (document.body.clientHeight < document.documentElement.clientHeight) ?
                document.body.clientHeight : document.documentElement.clientHeight;
    } else {
        clientHeight = (document.body.clientHeight > document.documentElement.clientHeight) ?
                document.body.clientHeight : document.documentElement.clientHeight;
    }
    return clientHeight;
}

if (typeof $.fn.toc.tocInited === 'undefined') {
    $.fn.toc.tocInited = false;
}
if (typeof $.fn.toc.tocMaxWidth === 'undefined') {
    $.fn.toc.tocMaxWidth = 0;
}

function activeCurrentScroll() {
    var scrollDistance = $(window).scrollTop();
    // Assign active class to nav links while scolling
    var targeti = -1;
    var hlist = $('#postdiv h2,h3,h4,h5,h6');
    hlist.each(function (i) {
        if (i == 0 || $(this).position().top <= scrollDistance) {
            targeti = i;
        }
    });
    if (targeti != -1) {
        var divlist = $('#tocdiv li');
        divlist.not(targeti).removeClass('active');
        divlist.eq(targeti).addClass('active');
        // http://www.nengyongma.com/fe/scrollintoviewifneeded
        // divlist[targeti].scrollIntoViewIfNeeded(false);

        // https://github.com/stipsan/scroll-into-view-if-needed
        const node = divlist[targeti];
        // similar behavior as Element.scrollIntoView({block: "nearest", inline: "nearest"})
        // only that it is a no-op if `node` is already visible
        // see: https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoView
        // same behavior as Element.scrollIntoViewIfNeeded()
        // see: https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollIntoViewIfNeeded
        scrollIntoView(node, {
            scrollMode: 'if-needed',
            block: 'nearest',
            inline: 'nearest',
        });
    }
}

function initToc(tocdiv) {
    if (!$.fn.toc.tocInited) {
        $.fn.toc.tocInited = true;
        tocdiv.toc({
            title: '<i class="back-to-top">目录索引</i>',
        });

        // https://codepen.io/eksch/pen/xwdOeK
        $(window).scroll(function () {
            checkToc();
            activeCurrentScroll();
        }).scroll();
    }
}

function checkToc() {
    var postdiv = $("#postdiv");
    var tocdiv = $("#tocdiv");
    var postLeft = postdiv.offset().left;
    var tocLeft = tocdiv.offset().left;
    var tocRight = tocLeft + tocdiv.width();

    // css 里面写的：min-width: 20em; max-width: 20em;
    var xwidth = parseInt(tocdiv.css("max-width"));
    if ($.fn.toc.tocMaxWidth == 0 && xwidth >= 100) {
        $.fn.toc.tocMaxWidth = xwidth;
    }

    if (tocRight > postLeft - 5) {

        // 尝试再挽救一下。
        if ($.fn.toc.tocMaxWidth > 0 && xwidth == $.fn.toc.tocMaxWidth) {
            tocdiv.css("max-width", "15em");
            tocdiv.css("min-width", "15em");
            setTimeout("checkToc()", 100);
            return;
        } else {
            tocdiv.fadeOut();
        }

    } else {

        // 如果可以更大，就想办法更大一些。
        if ($.fn.toc.tocMaxWidth > 0 && xwidth != $.fn.toc.tocMaxWidth) {
            var widthk = $.fn.toc.tocMaxWidth * 1 / 4;
            if (tocRight + widthk < postLeft - 10) {
                tocdiv.css("max-width", "20em");
                tocdiv.css("min-width", "20em");
                setTimeout("checkToc()", 100);
                return;
            }
        }

        initToc(tocdiv);
        tocdiv.fadeIn();

        var olroot = $("#tocdiv > ol");
        var xheight = getClientHeight() - tocdiv.position().top;
        if (olroot && olroot.length > 0) {
            var xtop = olroot.position().top;
            var theight = xheight - xtop;
            if (theight >= 100) {
                olroot.height(theight);
            }
        }
    }
}

// 文档加载完成时
$(document).ready(function () {
    checkToc();
});
// 窗口大小变化时
$(window).resize(function () {
    checkToc();
});
