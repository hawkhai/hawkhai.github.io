define(function(require) {
    var u = require("../lib/xhr"),
    r = require("../lib/md5"),
    e = {
        iciba: {
            translate: {
                url: "http://ifanyi.iciba.com/?c=liebao",
                method: "POST",
                input: function(t) {
                    var a = "sdaAWDdas78^DAasd890";
                    return {
                        key: a,
                        q: t,
                        sign: r((a + t).trim()).slice(0, 16)
                    }
                },
                output: require("./icibaTranslateProxy")
            },
            query: {
                url: "http://api.iciba.com/liebao/search.php",
                method: "GET",
                input: function(t) {
                    return {
                        key: "sdaAWDdas78^DAasd890",
                        word: t
                    }
                },
                output: require("./icibaQueryProxy")
            },
            poweredBy: '<a href="http://www.iciba.com/?f=lb" title="金山词霸" target="_blank">金山词霸</a>'
        }
    },
    c = "iciba";
    return function(a, r, i) {
        function n(t, i, n, e) {
            u({
                url: e.url,
                method: e.method,
                data: e.input(t)
            },
            function(t) {
                var a, r;
                try {
                    a = JSON.parse(t)
                } catch(t) {
                    return n(!1)
                }
                try {
                    r = e.output(a)
                } catch(t) {
                    return n(!1)
                }
                if (!r) return n(null);
                i(r)
            },
            function() {
                n(!1)
            })
        }
        50 <= a.length || /[\u3040-\u30FF]/.test(a) ? n(a, r, i, e[c].translate) : n(a,
        function(t) {
            t ? r(t, e[c].poweredBy) : n(a, r, i, e[c].translate)
        },
        function() {
            n(a, r, i, e[c].translate)
        },
        e[c].query)
    }
});