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
    $('#postdiv h2,h3,h4,h5,h6').each(function (i) {
        if (i == 0 || $(this).position().top <= scrollDistance) {
            $('#tocdiv li.active').removeClass('active');
            var curli = $('#tocdiv li').eq(i);
            curli.addClass('active');
            curli[0].scrollIntoView();
        }
    });
}

function initToc(tocdiv) {
    if (!$.fn.toc.tocInited) {
        $.fn.toc.tocInited = true;
        tocdiv.toc({
            title: '<i class="back-to-top">目录索引</i>',
        });

        // https://codepen.io/eksch/pen/xwdOeK
        $(window).scroll(function() {
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
