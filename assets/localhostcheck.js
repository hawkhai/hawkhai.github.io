---
title : localhostcheck
---
// https://www.cnblogs.com/keyi/p/6768284.html
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}

function islocalhost() {
    var localhost = window.location.host;
    var regex = /^[\d.]+:/;
    if (!localhost.startsWith("localhost:") && !regex.test(localhost)) {
        return false;
    }
    return true;
}

function checkhost() {
    var localhost = window.location.host;
    var href = window.location.href;
    if (!islocalhost()) {
        return;
    }

    if (localhost.startsWith("localhost:") && typeof localhost === typeof localhostip) {
        href = href.replace("localhost", localhostip);
        window.location.href = href;
    } else {
        // setCookie("invisible", "invisible", 365);
        // 内网简单保护隐私
        if (href.endsWith("/invisible/") && !getCookie("invisible")) {
            window.location.href = '{{ "/" | prepend: site.baseurl }}';
        }
    }
}

checkhost();
