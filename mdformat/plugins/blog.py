#encoding=utf8
"""
Jekyll blog plugin for MdFormatter.

Handles all blog / Jekyll-specific logic extracted from mdrstrip.py:
  - LINKTAGARRAY link-tag formatting in strip_line
  - Em-dash normalisation
  - codeformat:false / imgthumb frontmatter flags
  - removeRefs (pre_process) and appendRefs (post_process)
  - URL backup (backupUrlContent) and host collection (collectHost)
  - Image thumbnail management (tidyupImg)
  - Chinese symbol / code-style checks (process_line)
  - checkReviewJS / findPostMdFile (teardown)
  - G_HOSTSET statistics
"""

import re, os, sys, time, datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from codestrip import (
    THUMBNAIL, SELENIUM, isDiacritic,
    calcType, calcHost, isInvisibleDir,
    querySnapCache, removeSnapCache, touchSnapCache, clearSnapCache,
    ffmpegConvert,
)
from pythonx.funclib import (
    IS_WINDOWS, IS_MACOS, IS_LINUX,
    refindall, readfile, writefile, appendfile, readfileLast,
    readfileJson, writefileJson,
    getMd5, getFileMd5, getFileSrcMd5z,
    searchdir, openTextFile,
    bytesToString, formatTimeStamp,
    popenCmd,
    osremove, copyfile,
)
from pythonx.pelib import getLuckFileMd5

from ..plugin_base import MdPlugin

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NEWLINE_CHAR = "\r\n" if IS_WINDOWS else "\n"
PAUSE_CMD    = "pause" if IS_WINDOWS else "read -p 'Press [Enter] key to continue...'"

# 名称，域名正则。
LINKTAGARRAY = (
    ("bili",     "bilibili.com"),
    ("zhihu",    "zhihu.com"),
    ("cnblogs",  "cnblogs.com"),
    ("csdn",     "csdn.net"),
    ("github",   "github.com|github.io"),
    ("jianshu",  "jianshu.com"),
    ("wiki",     "wikipedia.org"),
    ("weixin",   "weixin.qq.com"),
    ("keqq",     "ke.qq.com"),
    ("scriptol", "scriptol.com"),
    ("khronos",  "khronos.org"),
    ("gluon",    "gluon.ai"),
)

SNAPSHOT_HTML = "<font class='ref_snapshot'>参考资料快照</font>"
REVIEW_REGEX  = (
    "^<p class='reviewtip'><script type='text/javascript' src='"
    "{% include relrefx?.html url=\".*?\" %}'></script></p>$"
)
REVIEW_FORMAT = (
    "<p class='reviewtip'><script type='text/javascript' src='"
    "{%% include relref.html url=\"/%s.js\" %%}'></script></p>"
)
REVIEW_LINE   = "<hr class='reviewline'/>"
REVIEW_JS_PATH = "%s.js"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _get_link_tag_src(name):
    return "{{% include relref_{}.html %}}".format(name)


def _is_host_ignore_stat(hostk):
    for name, host in LINKTAGARRAY:
        if refindall("^({})$".format(host), hostk):
            return True
        if refindall("\\.({})$".format(host), hostk):
            return True
    for host in ("sunocean.life", "hawkhai.com"):
        if refindall("^({})$".format(host), hostk):
            return True
        if refindall("\\.({})$".format(host), hostk):
            return True
    return False


_G_CACHE_IGLIST = {}

def _read_iglist(fpath):
    if not os.path.exists(fpath):
        return []
    hash_key = "{},{},{}".format(getMd5(fpath), os.path.getsize(fpath), os.path.getmtime(fpath))
    if hash_key in _G_CACHE_IGLIST:
        return _G_CACHE_IGLIST[hash_key]
    li = readfile(fpath, True, "utf8").split("\n")
    li = [i.strip().split(" #")[0].strip() for i in li if i.strip().split(" #")[0].strip()]
    li = [i.strip().split("# ")[0].strip() for i in li if i.strip().split("# ")[0].strip()]
    _G_CACHE_IGLIST[hash_key] = li
    return li


_G_CHECKPAGE = []

def _checkpage(fdata):
    global _G_CHECKPAGE
    if not _G_CHECKPAGE:
        tags = [
            "ERR_CONNECTION_TIMED_OUT",
            "无法访问此网站",
            '<div class="Qrcode-title">扫码登录</div>',
            '未注册手机验证后自动登录，注册即代表同意',
            "其他登录方式",
            "其他方式登录",
            'name="passport_iframe" src="https://passport.csdn.net/account/login?',
            'www.zhihu.com/api/v3/account/api/login/qrcode/',
            'pp.chuzushijian.cn',
            '动力广告',
            '<title>404 Not Found</title>',
            '<title>隐私设置错误</title>',
            '网站在更新其安全设置期间可能会经常显示警告。此问题应该很快就会得到改进。',
            '<h1>您的连接不是私密连接</h1>',
            '出现此问题的原因可能是配置有误或您的连接被拦截了。',
        ]
        _G_CHECKPAGE = [bytesToString(t.encode("utf8")) for t in tags]
    for itag in _G_CHECKPAGE:
        if fdata.find(itag) != -1:
            return itag
    return None


# ---------------------------------------------------------------------------
# File-size / directory check helpers (from mdrstrip.py)
# ---------------------------------------------------------------------------

_G_CHECKTINUE_SET = {}

def _oncheckdirectory(rootdir, basename=None):
    if rootdir in _G_CHECKTINUE_SET:
        return _G_CHECKTINUE_SET[rootdir]
    curdir = rootdir
    for _ in range(10):
        if os.path.exists(os.path.join(curdir, "imgnocheck.txt")):
            _G_CHECKTINUE_SET[rootdir] = False
            return False
        if os.path.exists(os.path.join(curdir, ".git")):
            break
        curdir = os.path.split(curdir)[0]
    _G_CHECKTINUE_SET[rootdir] = True
    return True


class BlogPlugin(MdPlugin):
    """Jekyll blog-specific MD formatting plugin."""

    def __init__(self, mycache=None, ignoreerr=False):
        self._mycache   = mycache
        self._ignoreerr = ignoreerr

        self._hostset   = {}   # {host: count}
        self._img_taged = set()

        # per-file state (reset in pre_process)
        self._reflist   = []

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def setup(self, args):
        self._args = args

    # ------------------------------------------------------------------
    # Pre-filter hook
    # ------------------------------------------------------------------

    def on_any_file(self, fpath, fname, ftype):
        """Handle .spaceback.json files before the source-type filter."""
        if fname.endswith(".spaceback.json"):
            fjson = readfileJson(fpath, "utf8")
            writefileJson(fpath, fjson, ascii=False, encoding="utf8")
            return True
        return False

    # ------------------------------------------------------------------
    # Pre-scan (file-size check) — call before formatter.run()
    # ------------------------------------------------------------------

    def run_pre_scan(self, rootdirs, ignore_list):
        """Run the file-size check pass over *rootdirs*."""
        for rootdir in rootdirs:
            if os.path.exists(rootdir):
                searchdir(rootdir, self._check_file_size,
                          ignorelist=ignore_list,
                          onDirectory=_oncheckdirectory)

    def _check_file_size(self, fpath, fname, ftype):
        if fname.endswith(THUMBNAIL):
            srcimg = fpath[:-len(THUMBNAIL)]
            if not os.path.exists(srcimg):
                osremove(fpath)
            return

        if not _oncheckdirectory(os.path.split(fpath)[0]):
            return

        invdir = isInvisibleDir(fpath)
        bigfile_cfg = os.path.join(
            "invisible" if invdir else ".", "config/mdrstrip_bigfiles.txt")
        fmd5 = getFileSrcMd5z(fpath, mycache=self._mycache, assertx=False)

        igbigfiles = _read_iglist(bigfile_cfg)
        if fmd5 not in igbigfiles and fpath not in igbigfiles:
            size = os.path.getsize(fpath) / 1024.0 / 1000.0
            if size >= 1.0:
                print(fmd5, "#", fpath, "#", "%.1f MB" % size)

                if ftype in ("gif",) and IS_WINDOWS:
                    from pythonx import pygrab
                    pygrab.gifbuildwebp(fpath)

                if (not self._ignoreerr
                        and fpath.find(os.sep + "_site" + os.sep) == -1):
                    openTextFile(bigfile_cfg)
                    assert False, "大文件最好不要入库..."

    def teardown(self):
        rebuild   = self._args.get("rebuild", False)
        openresent = self._args.get("openresent", False)
        openresentx = self._args.get("openresentx", False)
        clearimg  = self._args.get("clearimg", False)

        if rebuild or openresent:
            self._check_review_js("assets" + os.sep + "reviewjs", ".")
            self._check_review_js("invisible" + os.sep + "reviewjs", "invisible")

        if clearimg:
            self._tidy_img_collect("assets" + os.sep + "images")
            self._tidy_img_collect("invisible" + os.sep + "images")

        if rebuild:
            clearSnapCache()
            from pythonx.funclib import cleardirEmpty
            cleardirEmpty("images")
            cleardirEmpty("source")
            self._tidy_img_clear()

        # print host stats
        hostlist = sorted(self._hostset.items(), key=lambda x: x[1], reverse=True)
        print(hostlist)
        for hostx in hostlist[:10]:
            print(hostx)

    # ------------------------------------------------------------------
    # File-level hooks
    # ------------------------------------------------------------------

    def should_skip_file(self, fpath, fname, ftype, ctx):
        iglist = _read_iglist("config/mdrstrip_file_ignore.txt")
        if fname in iglist:
            return True

        if ftype != "md":
            return False

        # second pass: read frontmatter flags after lines are loaded
        # (we check codeformat:false here via ctx.mdconfig set in pre_process)
        if ctx.mdconfig.get("codeformat", "").lower() == "false":
            return True

        return False

    def pre_process(self, fpath, fname, ftype, lines, ctx):
        """Parse frontmatter, set imgthumb, remove existing ref section."""
        self._reflist = []

        if ftype != "md":
            return lines

        # parse frontmatter
        fdata = "\n".join(lines).strip()
        ctx.mdconfig = {}
        ctx.imgthumb = True
        if fdata.startswith("---"):
            kvlist = fdata.split("---")[1].strip().split("\n")
            for kv in kvlist:
                kv = kv.strip()
                if ":" not in kv:
                    continue
                key, value = kv.split(":", 1)
                key   = key.strip()
                value = value.strip()
                ctx.mdconfig[key] = value

        # check frontmatter flags
        linecount = 0
        for line in lines:
            if line.strip() == "---":
                linecount += 1
                if linecount >= 2:
                    break
            if "".join(line.strip().lower().split()) == "imgthumb:false":
                ctx.imgthumb = False
                break
            if "".join(line.strip().lower().split()) == "codeformat:false":
                # will be caught in should_skip_file after mdconfig is set
                ctx.mdconfig["codeformat"] = "false"
                return lines

        lines = _remove_refs(fpath, lines)
        return lines

    def post_process(self, fpath, fname, ftype, lines, ctx):
        """Append URL reference list / review JS block."""
        if ftype != "md":
            return lines
        lines = self._append_refs(fpath, ctx.md5src, lines, ctx.imgthumb, ctx.mdconfig)
        return lines

    def transform_page(self, page, fpath, fname, ftype, ctx):
        """Ensure REVIEW_LINE is preceded by a blank line."""
        if ftype != "md":
            return page
        page = page.replace(NEWLINE_CHAR + REVIEW_LINE, NEWLINE_CHAR * 3 + REVIEW_LINE)
        return page

    # ------------------------------------------------------------------
    # Line-level hooks
    # ------------------------------------------------------------------

    def strip_line(self, line, ctx):
        """Normalise LINKTAGARRAY tags and em-dashes."""
        if ctx.is_md_file:
            for name, host in LINKTAGARRAY:
                tak = _get_link_tag_src(name)
                line = line.replace("  " + tak + "]", tak + "]")
                line = line.replace(" "  + tak + "]", tak + "]")
                line = line.replace(tak + "]",         " " + tak + "]")
                line = line.replace(name + "]",        tak + "]")
                line = line.replace("[ " + tak + "]",  "[" + name + " " + tak + "]")
            line = line.replace(" ——", "——").replace(" ——", "——")
            line = line.replace("—— ", "——").replace("—— ", "——")
            line = line.replace("——", " —— ")
        return line

    def process_line(self, line, index, lines, ctx):
        """Collect URLs/images and run blog-specific style checks."""
        errcnt = 0

        if ctx.is_md_file:
            ireflist, line = self._collect_host(ctx.fpath, ctx.md5src, line, ctx.imgthumb)
            lines[index] = line
            self._reflist.extend(ireflist)

            # Chinese symbol / code-style checks
            errcnt += self._check_cn_symbols(line, index, ctx)
            errcnt += self._check_code_style(line, index, ctx)

        return line, errcnt

    # ------------------------------------------------------------------
    # URL backup + host collection
    # ------------------------------------------------------------------

    def _backup_url_content(self, fpath, md5src, url):
        for urlz in _read_iglist("config/mdrstrip_url_ignore_ends.txt"):
            if url.endswith(urlz):
                return None

        if not self._ignoreerr:
            assert not url.endswith(".exe"), url
            assert not url.endswith(".zip"), url

        fname = os.path.split(fpath)[-1]

        urligstarts = _read_iglist("config/mdrstrip_url_ignore_starts.txt")
        urligstarts.extend(_read_iglist("invisible/config/mdrstrip_url_ignore_starts.txt"))
        for urlz in urligstarts:
            if url.startswith(urlz):
                return None
            if "[{}]{}".format(fname, url).startswith(urlz):
                return None

        print(fpath, url)
        chrome = True
        chrome_dialog = False
        for urlz in _read_iglist("config/mdrstrip_url_chrome_dialog.txt"):
            if url.startswith(urlz):
                chrome_dialog = True

        mdname      = os.path.split(fpath)[-1]
        urlhostsrc  = calcHost(url)
        urlhostdir  = urlhostsrc.replace(":", "/")
        urlmd5      = getMd5(url)[:8]
        invdir      = isInvisibleDir(fpath)

        if mdname in ("wechatdl.md",):
            return None

        ttype = ".html"
        ttype = calcType(ttype, url.split(urlhostsrc)[1])
        if ttype.endswith(".md"):
            ttype = ".html"
        if ttype in (".action",):
            ttype = ".html"
        if ttype.endswith(".pdf"):
            chrome = False

        def _buildlocal(ftype):
            flocal = os.path.join("backup", mdname, urlhostdir, urlmd5 + ftype)
            if invdir:
                flocal = os.path.join("invisible", flocal)
            return flocal

        mdxfile = False
        flocal  = _buildlocal(ttype)

        if chrome and urlhostsrc in _read_iglist("config/mdrstrip_host_jekyll.txt"):
            mdxfile  = True
            ttype    = ".md"
            newlocal = _buildlocal(ttype)
            if os.path.exists(flocal):
                os.rename(flocal, newlocal)
            flocal = newlocal
            ttype  = ".html"
            newlocal = _buildlocal(ttype)
            if os.path.exists(flocal):
                os.rename(flocal, newlocal)
            flocal = newlocal

        shotpath = flocal + SELENIUM
        fdata = querySnapCache(urlmd5)
        if fdata:
            writefile(flocal, fdata)
            fdatalocal = True
        else:
            if self._args.get("netfake"):
                fdata = b""
            else:
                from pythonx.funclib import netgetCacheLocal
                fdata = netgetCacheLocal(
                    url, cacheTimeout=60*60*24*1000,
                    chrome=chrome, local=flocal,
                    shotpath=shotpath, chromeDialog=chrome_dialog)
            fdatalocal = False

        idata = bytesToString(fdata)
        if url not in _read_iglist("config/mdrstrip_url_ignore.txt"):
            result = _checkpage(idata)
            if result:
                print("无法访问此网站", fpath, url, result)
                if not fdatalocal:
                    os.system(PAUSE_CMD)
                removeSnapCache(urlmd5)
                osremove(flocal)
                osremove(shotpath)
                return self._backup_url_content(fpath, md5src, url)

        def _addmdhead(fdata):
            xtime = formatTimeStamp(time.time())
            return (
                "---\ntitle : %(title)s\n---\n\n"
                "* TIME: %(time)s\n* URL: <%(url)s>\n\n-----\n\n"
                % {"time": xtime, "url": url, "title": "自动快照存档"}
            ) + fdata

        def _ismdhead(fdata):
            return fdata and fdata.startswith("---")

        def _html2md(fdata):
            import html2text
            h = html2text.HTML2Text()
            h.ignore_links = False
            fdata = h.handle(fdata)
            return fdata.replace("{{", "{ {").replace("}}", "} }")

        if (len(fdata) >= 1024*1000
                and fdata.lower().find(b"<body") != -1
                and fdata.lower().find(b"<html") != -1):
            mdxfile = True

        if mdxfile:
            fdata = bytesToString(fdata, "utf8")
            if fdata.lower().find("<body") != -1 and fdata.lower().find("<html") != -1:
                fdata = _html2md(fdata)
                fdata = _addmdhead(fdata)
                if not self._args.get("netfake"):
                    writefile(flocal, fdata, "utf8")
            elif not _ismdhead(fdata):
                fdata = _addmdhead(fdata)
                if not self._args.get("netfake"):
                    writefile(flocal, fdata, "utf8")

            if urlhostsrc == "www.shadertoy.com":
                li = refindall(r"\r?\n\r?\n[0-9]+\r?\n\r?\n    \r?\n    \r?\n    ", fdata)
                for i in li:
                    fdata = fdata.replace(i, NEWLINE_CHAR + "    ")
                if not self._args.get("netfake"):
                    writefile(flocal, fdata, "utf8")

        fmd5 = getFileSrcMd5z(flocal, mycache=self._mycache, assertx=False)
        invdir2 = isInvisibleDir(flocal)
        mdrstripBigfile = os.path.join(
            "invisible" if invdir2 else ".", "config/mdrstrip_bigfiles.txt")
        igbigfiles = _read_iglist(mdrstripBigfile)
        if fmd5 not in igbigfiles and flocal not in igbigfiles:
            if len(fdata) >= 1024*1000 and not self._ignoreerr:
                print(getFileSrcMd5z(flocal, mycache=self._mycache, assertx=False),
                      "#", flocal, "#", "%.1f MB" % (len(fdata) / 1024 / 1024))
                assert False, (len(fdata) / 1024.0 / 1000.0, url, flocal)

        remote = _buildlocal(".html" if mdxfile else ttype).replace("\\", "/")
        touchSnapCache(urlmd5, flocal)

        remotename = url.split("?")[0].split("#")[0].split("/")[-1]
        if remotename in _read_iglist("config/mdrstrip_url_ignore_nametype.txt"):
            return remote

        if remote.split(".")[-1] not in (
                "pdf", "html", "git", "php", "c", "phtml", "cpp", "cxx",
                "htm", "shtm", "xml", "ipynb", "py", "asp", "shtml", "aspx",
                "xhtml", "txt", "mspx", "sh"):
            print(fpath, url)
        return remote

    def _collect_host(self, fpath, md5src, line, imgthumb):
        reflist  = []
        linesrc  = line[:]

        # ── local-path images ─────────────────────────────────────────
        regex = r"(?:\"/(.*?)\")|(?:'/(.*?)')"
        for imglocal in refindall(regex, line):
            imglocal = "".join(imglocal)
            if imglocal.endswith("/") or len(imglocal) <= 2:
                continue
            kignore = False
            for src in ("/player.bilibili.com/", "source/", "blog/",
                        "source/shader/", "assets/glslEditor-0.0.20/",
                        "images/photo.jpg"):
                if imglocal.startswith(src):
                    kignore = True
            if kignore or os.path.isdir(imglocal):
                continue
            line = self._tidy_img(imglocal, fpath, line, imgthumb=imgthumb)

        # ── external URLs ─────────────────────────────────────────────
        regex = (
            r"((https?)://"
            r"([a-z0-9\.-]+\.[a-z]{2,8})"
            r"(:[0-9]{1,4})?"
            r"(/[a-z0-9\&%_\./~=+:@\u2013-]*)??"
            r"(\?[a-z0-9\&%_\./~=+:\[\]-]*)?"
            r"(#[a-z0-9\&%_\./~=:?-]*)?"
            r")"
        )
        li = refindall(regex, line, re.IGNORECASE)
        if not li:
            return reflist, line

        iglist = _read_iglist("config/mdrstrip_url_quote.txt")
        iglist.extend(_read_iglist("invisible/config/mdrstrip_url_quote.txt"))

        for tx in li:
            url  = tx[0]
            host = tx[2]
            checkz = line.split(url)
            for iline in checkz[1:]:
                checkli = ["", ")", "]", ">", " ", "*", "$"]
                for urlz in iglist:
                    if url.startswith(urlz) and urlz:
                        checkli += [";", '"', "'", "\\", "`"]
                if iline[:2] in ("{{",):
                    continue
                if iline[:1] not in checkli:
                    print(line)
                    print(url)
                    assert False, (url, checkz)
            assert not url.endswith("."), fpath + " " + url
            remote = self._backup_url_content(fpath, md5src, url)
            if remote:
                reflist.append([url, remote])

            if _is_host_ignore_stat(host):
                continue
            self._hostset[host] = self._hostset.get(host, 0) + 1

        # ── link-tag balance check ────────────────────────────────────
        xline = line[:]
        for name, host in LINKTAGARRAY:
            tak = _get_link_tag_src(name)
            xline = xline.replace(tak + "]", name + "]")
        for tx in refindall("<.*?>", xline):
            xline = xline.replace(tx, "")
        for name, host in LINKTAGARRAY:
            li1 = refindall(host, xline, re.IGNORECASE)
            li2 = refindall(name + "\\]", xline, re.IGNORECASE)
            if len(li1) == len(li2):
                continue
            if xline.find("[") == -1 and xline.find("<") == -1 and xline.find("(") == -1:
                continue
            print(xline, li1, li2)
            openTextFile(fpath)
            assert False, linesrc

        return reflist, line

    # ------------------------------------------------------------------
    # Reference-section management
    # ------------------------------------------------------------------

    def _append_refs(self, fpath, md5src, lines, imgthumb, mdconfig):
        invdir  = isInvisibleDir(fpath)
        fpath_r = os.path.relpath(fpath, ".")
        frelgit = fpath_r
        if os.path.exists(fpath_r + ".tempd"):
            frelgit = fpath_r + ".tempd"

        def _get_date_str(frelgit):
            cmdx = 'git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'.format(frelgit)
            if invdir:
                cmdx = ('cd {} & git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'
                        .format(*frelgit.split(os.sep, 1)))
            if invdir and IS_MACOS:
                cmdx = ('cd {} && git log -n 1 --pretty=format:"%ad" --date=short -- "{}" && cd ..'
                        .format(*frelgit.split(os.sep, 1)))
            try:
                datestr = bytesToString(popenCmd(cmdx))
            except FileNotFoundError:
                datestr = None
            return datestr or datetime.datetime.now().date()

        fpath_js = fpath_r
        if fpath_js.startswith("_posts" + os.sep):
            fpath_js = os.path.join("blogs", fpath_js.split(os.sep)[-1])
        if invdir:
            fpath_js = ("invisible" + os.sep + "reviewjs" + os.sep
                        + fpath_js[len("invisible" + os.sep):])
        else:
            fpath_js = "assets" + os.sep + "reviewjs" + os.sep + fpath_js

        reviewjs = REVIEW_JS_PATH % fpath_js
        fcode    = readfile(reviewjs, True)
        fcheck   = refindall("[0-9a-f]{32}", fcode)
        if not (fcheck and md5src == fcheck[0]):
            fcode = 'document.write("%s: review"); // md5src=%s%s' % (
                _get_date_str(frelgit), md5src, NEWLINE_CHAR)
            writefile(reviewjs, fcode)

        review = REVIEW_FORMAT % fpath_js.replace("\\", "/")
        assert refindall(REVIEW_REGEX, review), review

        reflist = self._reflist
        if "sortrefs: true" in lines:
            reflist = sorted(reflist, key=lambda x: x[1])

        if reflist:
            lines.append("")
            lines.append("")
            if mdconfig:
                lines.append(REVIEW_LINE)
                lines.append(review)
            lines.append(SNAPSHOT_HTML)
            lines.append("")
            lines.append("")
            urlset = set()
            for url, remote in reflist:
                if url in urlset:
                    continue
                urlset.add(url)
                if mdconfig:
                    remote = "{{% " + ("include relrefx.html url=\"/%s\"" % remote) + " %}"
                    lines.append("- [{}]({})".format(url, remote))
                else:
                    lines.append("- [{}]({})".format(url, url))
            lines.append("")
        else:
            if mdconfig:
                lines.append("")
                lines.append("")
                lines.append(REVIEW_LINE)
                lines.append(review)
                lines.append("")
        return lines

    # ------------------------------------------------------------------
    # Image thumbnail management
    # ------------------------------------------------------------------

    def _tidy_img_collect(self, rootdir):
        def _visit(fpath, fname, ftype):
            if fname.endswith(THUMBNAIL):
                if not os.path.exists(fpath[:-len(THUMBNAIL)]):
                    osremove(fpath)
            else:
                self._img_taged.add(os.path.relpath(fpath, ".").lower())
        searchdir(rootdir, _visit)

    def _tidy_img_clear(self):
        for key in self._img_taged:
            osremove(key)

    def _tidy_img(self, imglocal, fpath, line, imgthumb=True):
        from PIL import Image, ImageFont, ImageDraw

        PIL_SAMPLE = (Image.Resampling.LANCZOS
                      if hasattr(Image, "Resampling") else Image.ANTIALIAS)

        fakeimgfiles = _read_iglist("config/mdrstrip_fake_image_files.txt")
        if imglocal in fakeimgfiles:
            return line

        imgdir, imgfname = os.path.split(imglocal)
        imgnocopy = os.path.join(imgdir, "imgnocopy.txt")
        if imgfname.find(".") == -1:
            imgfname = imgfname + ".jpg"
        imgtype = imgfname.split(".")[-1].lower()
        if imgtype == "mp4":
            ffmpegConvert(imglocal)

        if not self._args.get("copyres"):
            assert os.path.exists(imglocal), fpath + "  " + imglocal
            return line

        invdir = isInvisibleDir(fpath)
        fname  = os.path.split(fpath)[-1]
        if fname.lower().endswith(".md"):
            fname = fname[:-3]
        if refindall("^[0-9]{4}-[0-9]{2}-[0-9]{2}-", fname):
            fname = fname[:10].replace("-", "")[-6:] + "-" + fname[11:]
        if len(fname) > 32:
            fname = fname[:30] + "~" + getMd5(fname)[:2]

        tpath = os.path.join("assets", "images", fname.lower(), imgfname)
        if invdir:
            tpath = os.path.join("invisible", "images", fname.lower(), imgfname)
        if os.path.exists(imgnocopy):
            tpath = imglocal

        if not os.path.exists(imglocal) and os.path.exists(tpath):
            copyfile(tpath, imglocal)
        count = 0
        while not os.path.exists(imglocal):
            if os.path.exists(imgnocopy):
                return line
            print("文件不存在", imglocal, os.path.abspath(imglocal))
            if not imgthumb:
                return line
            count += 1
            if count >= 3:
                assert False, "重试次数过多..."
            os.system(PAUSE_CMD)
            fakeimgfiles = _read_iglist("config/mdrstrip_fake_image_files.txt")
            if imglocal in fakeimgfiles:
                return line

        iscopy = copyfile(imglocal, tpath)
        imglocalnail = imglocal + THUMBNAIL
        tpathnail    = tpath + THUMBNAIL
        isnailcopy   = False
        if os.path.exists(imglocalnail):
            isnailcopy = copyfile(imglocalnail, tpathnail)

        if os.path.abspath(imglocal) != os.path.abspath(tpath):
            self._img_taged.add(os.path.relpath(imglocal, ".").lower())
        rel_tpath = os.path.relpath(tpath, ".").lower()
        if rel_tpath in self._img_taged:
            self._img_taged.remove(rel_tpath)

        thumbPath = tpath + THUMBNAIL

        if not imgthumb:
            osremove(thumbPath)

        elif (not os.path.exists(thumbPath)
              and imgtype in ("png", "jpg", "gif", "jpeg", "webp", "bmp", "jfif")):
            try:
                img = Image.open(tpath)
            except RuntimeError as ex:
                print("Image.open RuntimeError", tpath)
                raise ex
            width, height = img.size
            widthctrl = 64
            if width > widthctrl:
                try:
                    imgtmp = img.resize(
                        (widthctrl, round(widthctrl * height / width)), PIL_SAMPLE)
                    img = imgtmp.convert("RGB")
                except OSError as ex:
                    print("Image.resize OSError", tpath)
                    raise ex
                img = img.resize((width, height), PIL_SAMPLE)
                draw = ImageDraw.Draw(img, "RGBA")
                font = ImageFont.truetype(r"assets/logos/方正楷体_GB2312.ttf", size=20)
                draw.rectangle(((0, 0), (width, 40)), fill=(0, 0, 0, 127))
                draw.text((10, 10), u"图片加载中, 请稍候....", fill="#ffffff", font=font)
            img = img.convert("RGB")
            img.save(thumbPath)
            appendfile(thumbPath, getFileMd5(tpath, mycache=self._mycache, assertx=False))

        elif not os.path.exists(thumbPath) and imgtype in ("svg",):
            osremove(thumbPath)

        elif os.path.exists(thumbPath):
            srcmd5 = readfileLast(thumbPath, True, size=32)
            if getLuckFileMd5(tpath, srcmd5) != srcmd5:
                osremove(thumbPath)
                return self._tidy_img(imglocal, fpath, line, imgthumb=imgthumb)

        if imgtype not in ("pdf", "png", "jpg", "gif", "jpeg", "webp",
                           "mp4", "zip", "bmp", "svg", "jfif", "webm", "avif"):
            print(imglocal, fpath, line)
            assert False, imglocal

        if iscopy:
            osremove(imglocal)
        if isnailcopy:
            osremove(imglocalnail)
        return line.replace(imglocal, tpath.replace("\\", "/"))

    # ------------------------------------------------------------------
    # Blog-specific line checks
    # ------------------------------------------------------------------

    def _check_cn_symbols(self, line, index, ctx):
        """Check for English punctuation used in Chinese text."""
        cnsign  = "''"""
        cnregex = "\u4e00-\u9fa5"
        for ch in line:
            ordch = ord(ch)
            regch = "\\u%04x" % ordch
            if ordch <= 0x7F or isDiacritic(ch):
                continue
            if 0x4e00 <= ordch <= 0x9fa5:
                if cnregex.find(regch) == -1:
                    cnregex += regch
            else:
                if cnsign.find(regch) == -1:
                    cnsign += regch

        cnregexc = cnregex[:]
        cnregex_full = cnregex + cnsign

        linec = line
        for itmp in refindall(r"\$\$.*?\$\$", line):
            linec = linec.replace(itmp, " ")
        for itmp in refindall("\u201c.*?\u201d", line):
            linec = linec.replace(itmp, " ")
        for itmp in refindall("`.*?`", line):
            linec = linec.replace(itmp, " ")

        lixyx = refindall(
            "[{}] [,()] [{}]".format(cnregex_full, cnregex_full), linec, re.IGNORECASE)
        lixyx.extend(refindall(
            "[{}] [,()]$".format(cnregex_full), linec, re.IGNORECASE))
        lixyx.extend(refindall(
            "[{}][,;] [{}]".format(cnregexc, cnregexc), linec, re.IGNORECASE))
        if lixyx:
            openTextFile(ctx.fpath)
            print(lixyx)
            print("中文符号问题 {}:{} \"{}\"".format(ctx.fpath, index+1, linec))
            os.system(PAUSE_CMD)
        return len(lixyx)

    def _check_code_style(self, line, index, ctx):
        """Check for if( / while( without space."""
        if (line.lower().replace("endif", "x").find("if(") != -1
                or line.lower().find("while(") != -1):
            openTextFile(ctx.fpath)
            print("'if(' & 'while(' 问题 {}:{} \"{}\"".format(ctx.fpath, index+1, line))
            os.system(PAUSE_CMD)
            return 1
        return 0

    # ------------------------------------------------------------------
    # Review JS helpers
    # ------------------------------------------------------------------

    def _find_post_md_file(self, rootdir, fnamek):
        fpathk = fnamek
        def _visit(fpath, fname, ftype):
            nonlocal fpathk
            if fname == fnamek:
                assert fpathk == fnamek
                fpathk = fpath
        searchdir(rootdir, _visit)
        return fpathk

    def _check_review_js(self, jsdir, rootdir):
        openresent  = self._args.get("openresent", False)
        openresentx = self._args.get("openresentx", False)

        def _visit(fpath, fname, ftype):
            assert fname.endswith(".md.js"), fname
            jsfile = os.path.relpath(fpath, jsdir)
            mdfile = jsfile[:-len(".js")]
            if mdfile.startswith("blogs" + os.sep):
                mdfile = self._find_post_md_file("_posts", mdfile.split(os.sep)[-1])
                mdfile = os.path.relpath(mdfile, rootdir)
            mdfile = os.path.join(rootdir, mdfile)
            if not os.path.exists(mdfile):
                osremove(fpath)
            elif openresent:
                jsdata = readfile(fpath, True).strip()
                jsy, jsm, jsd = refindall("[0-9]+", jsdata)[:3]
                today  = datetime.date.today()
                jsday  = datetime.date(int(jsy), int(jsm), int(jsd))
                xday   = today - jsday
                if xday.days <= (30 if openresentx else 15):
                    openTextFile(mdfile)

        searchdir(jsdir, _visit)


# ---------------------------------------------------------------------------
# removeRefs (module-level, used by BlogPlugin.pre_process)
# ---------------------------------------------------------------------------

def _remove_refs(fpath, lines):
    lineCount  = len(lines)
    headIndex  = -1
    for index in range(lineCount):
        i = lineCount - 1 - index
        if not lines[i] or not lines[i].strip():
            continue
        if refindall(
                r"^- \[{}\]\({}\)$".format(".*?", ".*?"), lines[i]):
            continue
        if lines[i] == SNAPSHOT_HTML:
            headIndex = i
            break
        break

    if headIndex != -1:
        assert (lines[headIndex-1] == ""
                or refindall(REVIEW_REGEX, lines[headIndex-1])), \
            "%r" % lines[headIndex-1]
        if lines[headIndex-2] in ("-----", REVIEW_LINE):
            assert lines[headIndex-3] == "", "%r" % lines[headIndex-3]
            lines = lines[:headIndex-3]
        else:
            if lines[headIndex-2] == "":
                lines = lines[:headIndex-2]
            else:
                lines = lines[:headIndex-1]
    else:
        while lines and (
                lines[-1] in ("", "-----", REVIEW_LINE)
                or refindall(REVIEW_REGEX, lines[-1])):
            lines = lines[:-1]
    return lines
