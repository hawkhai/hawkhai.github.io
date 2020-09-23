// https://github.com/michael-lynch/scrollgress
!function(s){s.fn.scrollgress=function(o){if(!this.length)return this;var t={height:"5px",color:"#ff0000",success:function(){}},r=this;r.settings={},r.settings=s.extend({},t,o);var e=r.settings,l=s(this),i=l.css("overflow"),c=l.css("overflow-y"),n="auto"===i||"scroll"===i||"auto"===c||"scroll"===c?!0:!1,g=s(window).outerHeight(),h=n?l[0].scrollHeight:l.height(),d=n?l:s(window),a='<div class="scrollgress"><div class="scrollgress__progress"></div></div>';s("body").prepend(a),s(".scrollgress").css({position:"fixed",top:"0px",left:"0px",background:"transparent",width:"100%",height:e.height}),s(".scrollgress__progress").css({"float":"left",background:e.color,width:"0%",height:e.height}),d.scroll(function(o){var t=n?l.scrollTop():s(document).scrollTop(),r=(t/(h-g)*100).toFixed(2);/*console.log(o.originalEvent),*/s(".scrollgress__progress").css({width:r+"%"})}),e.success.call(this)}}(jQuery);
function InstallReadingBar() { $('body').scrollgress({ height: '1.5px', color: '#b6321c' }); }
$(document).ready(function () { setTimeout("InstallReadingBar()", 1000); });
function checkVideo() {
    var postdiv = $("#postdiv");
    var iframevideo = $(".iframevideo");
    iframevideo.css("width", "" + postdiv.width() + "px");
    iframevideo.css("height", "" + (postdiv.width()*480/852) + "px");
}
// 文档加载完成时
$(document).ready(function () {
    checkVideo();
});
// 窗口大小变化时
$(window).resize(function () {
    checkVideo();
});