#encoding=utf8
"""
Generic MD formatter core.

Handles:
  - File discovery and change-log caching
  - Per-file line processing pipeline
  - Code / chart block state tracking
  - Chinese-English space checks
  - Title-space and indent checks
  - Bold / backtick normalisation
  - Rouge code-language validation
  - KangXi translation
  - Spaceback-JSON post-processing
  - File write with md5 guard
  - Character-set statistics
"""

import re, os, sys, traceback

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from codestrip import (
    getLeftSpaceCount,
    checklog, savelog, removelog,
)
from pythonx.funclib import (
    IS_WINDOWS, IS_MACOS, IS_LINUX,
    refindall, readfile, readfileLines, writefile,
    readfileJson, getFileMd5,
    searchdir, openTextFile,
    LINE_SEP_SHORT,
)
from pythonx.kangxi import TranslateKangXi

from .plugin_base import MdContext

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NEWLINE_CHAR = "\r\n" if IS_WINDOWS else "\n"
PAUSE_CMD    = "pause" if IS_WINDOWS else "read -p 'Press [Enter] key to continue...'"

SPACEBACKFILE_TAIL = ".spaceback.json"

# ---------------------------------------------------------------------------
# Rougify language list (cached once)
# ---------------------------------------------------------------------------

def _load_rougify_list():
    ROUGIFY_LIST_FILE = "config/rougify_list_json.txt"
    ROUGIFY_LIST = readfileJson(ROUGIFY_LIST_FILE)
    if not ROUGIFY_LIST:
        ROUGIFY_LIST_SRC = readfile("config/rougify_list.txt", True)
        ROUGIFY_LIST = refindall("\n([^\\s:]+):", ROUGIFY_LIST_SRC, re.MULTILINE)
        ROUGIFY_LIST2 = refindall("\\[\\s*aliases\\s*:(.*?)\\]", ROUGIFY_LIST_SRC)
        for temp in ROUGIFY_LIST2:
            temp = temp.strip().split(",")
            for itemp in temp:
                itemp = itemp.strip()
                if not itemp:
                    continue
                ROUGIFY_LIST.append(itemp)
        from pythonx.funclib import writefileJson
        writefileJson(ROUGIFY_LIST_FILE, ROUGIFY_LIST)
        for i in ROUGIFY_LIST:
            assert refindall("^([0-9a-z_#+-]+)$", i, re.IGNORECASE), i
    return ROUGIFY_LIST

# ---------------------------------------------------------------------------
# Character-set statistics helpers
# ---------------------------------------------------------------------------

class CharStats:
    def __init__(self):
        self.cnchar = []
        self.cschar = []
        self.enchar = []
        self.typeset = set()

    def collect(self, line):
        from codestrip import isDiacritic
        for ch in line:
            ordch = ord(ch)
            if ordch <= 0x7F or isDiacritic(ch):
                self.enchar.append(ch)
                continue
            if 0x4e00 <= ordch <= 0x9fa5:
                if ch not in self.cnchar:
                    self.cnchar.append(ch)
            else:
                if ch not in self.cschar:
                    self.cschar.append(ch)

    def dump(self):
        from pythonx.funclib import writefile as _wf
        imgset  = ("jpeg", "jpg", "png", "gif", "bmp", "jfif")
        fontset = ("eot", "ttf", "woff", "svg", "woff2")
        codeset = ("cc", "js", "txt", "xml", "css", "mk", "lock", "zip",
                   "makefile", "scss")
        ts = self.typeset - set(imgset) - set(fontset) - set(codeset)

        print(LINE_SEP_SHORT)
        cschar = list(set(self.cschar))
        cschar.sort()
        print("".join(cschar))
        print(ts)

        def _viewchar(lichar, xfile, xmin, xmax):
            li = list(set("".join(lichar)))
            li.sort()
            page = ""
            minv, maxv = 1024, 0
            for index, tchar in enumerate(li):
                page += tchar
                if (index + 1) % 50 == 0:
                    page += NEWLINE_CHAR
                from codestrip import isDiacritic
                if isDiacritic(tchar):
                    continue
                minv = min(minv, ord(tchar))
                maxv = max(maxv, ord(tchar))
            tempfile = os.path.join("tempdir", xfile)
            _wf(tempfile, page.encode("utf8"))
            print(minv, maxv)
            print([("%04x" % ord(k), k) for k in li[:5]])
            print([("%04x" % ord(k), k) for k in li[-5:]])
            assert xmin <= minv and maxv <= xmax

        _viewchar(self.cnchar, "cnfile.txt", 0x80, 0x7FFFFFFF)
        _viewchar(self.cschar, "csfile.txt", 0x80, 0x7FFFFFFF)
        _viewchar(self.enchar, "enfile.txt", 0x0,  0x7F)

# ---------------------------------------------------------------------------
# Core formatter
# ---------------------------------------------------------------------------

class MdFormatter:
    """
    Generic Markdown formatter.

    Usage::

        fmt = MdFormatter(args, plugins=[MyPlugin()])
        fmt.run(search_roots, ignore_lists)
    """

    def __init__(self, args, plugins=None, mycache=None):
        self.args      = args          # dict of bool flags (rebuild, format, …)
        self.plugins   = plugins or []
        self._mycache  = mycache
        self._rougify_list = None
        self._char_stats   = CharStats()
        self._script_file  = None    # set by caller for checklog keying

        for plugin in self.plugins:
            plugin.setup(args)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run(self, mainw_ignore_list, script_file=None):
        """
        Scan from the current working directory and process every applicable
        file.

        *script_file* is the path of the top-level entry script, used as
        the key for the change-log cache (same role as __file__ in the
        original mdrstrip.py).
        """
        self._script_file = script_file or __file__

        searchdir(".", self._mainfilew,
                  ignorelist=mainw_ignore_list, reverse=True)

        self._char_stats.dump()
        for plugin in self.plugins:
            plugin.teardown()

    # ------------------------------------------------------------------
    # File dispatch
    # ------------------------------------------------------------------

    def _mainfilew(self, fpath, fname, ftype):
        """Cached wrapper around _mainfile."""
        if not self.args.get("rebuild") and checklog(self._script_file, fpath):
            return 0

        if "only" in self.args.get("_argv", []):
            if fname not in self.args.get("_argv", []):
                return 0

        removelog(self._script_file, fpath)
        errcnt = self._mainfile(fpath, fname, ftype)
        if errcnt == 0:
            savelog(self._script_file, fpath)
        return errcnt

    def _mainfile(self, fpath, fname, ftype, fdepth=0):
        fpathsrc, fnamesrc, ftypesrc = fpath, fname, ftype

        # ── pre-filter: let plugins handle special files (e.g. .spaceback.json)
        for plugin in self.plugins:
            if plugin.on_any_file(fpath, fname, ftype):
                return 0

        ftype_lo = ftype.lower()

        is_src_file = ftype_lo in (
            "md", "php", "html", "htm", "js", "css", "scss",
            "svg", "py", "vsh", "fsh",
        )
        is_md_file         = ftype_lo in ("md",)
        warn_cn_en_space   = ftype_lo in ("md", "php", "html", "htm", "vsh", "fsh")
        warn_title_space   = ftype_lo in ("md",)
        warn_indent_space  = ftype_lo in ("md", "php", "scss", "vsh", "fsh")

        if not is_src_file:
            return 0

        ctx = MdContext(
            fpath=fpath, fname=fname, ftype=ftype_lo, md5src="",
            is_md_file=is_md_file, is_src_file=is_src_file,
            warn_cn_en_space=warn_cn_en_space,
            warn_title_space=warn_title_space,
            warn_indent_space=warn_indent_space,
            args=self.args,
        )

        # ── allow plugins to gate the file entirely ──────────────────
        for plugin in self.plugins:
            if plugin.should_skip_file(fpath, fname, ftype_lo, ctx):
                return 0

        # ── normalise line endings on non-Windows systems ─────────────
        if IS_MACOS or IS_LINUX:
            fdata = readfile(fpath)
            fdata = (fdata.replace(b"\r\n", b"\n")
                         .replace(b"\r",   b"\n")
                         .replace(b"\n",   b"\r\n"))
            writefile(fpath, fdata)

        print(fpath)

        ctx.md5src = getFileMd5(fpath, mycache=self._mycache, assertx=False)

        try:
            lines = readfileLines(fpath, False, False, "utf8")
        except Exception as ex:
            openTextFile(fpath)
            raise ex

        # ── plugin pre-process (e.g. removeRefs) ─────────────────────
        for plugin in self.plugins:
            lines = plugin.pre_process(fpath, fname, ftype_lo, lines, ctx)

        # ── rstrip + plugin strip_line ────────────────────────────────
        lines = [self._strip_line(line, ctx) for line in lines]

        # ── blank-line normalisation ──────────────────────────────────
        lines.append("")
        lines.append("")
        while len(lines) >= 2 and not lines[-1] and not lines[-2]:
            lines = lines[:-1]
        while lines and not lines[0]:
            lines = lines[1:]

        keep_strip = (ftype_lo in ("svg",)
                      or fname in ("gitsrc.html",)
                      or refindall(r"^relref[a-z_]*\.html$", fname))
        if keep_strip:
            while lines and not lines[-1]:
                lines = lines[:-1]

        # ── allow plugins to re-check the file after pre-processing ──
        for plugin in self.plugins:
            if plugin.should_skip_file(fpath, fname, ftype_lo, ctx):
                return 0

        # ── load rougify list once ────────────────────────────────────
        if self._rougify_list is None:
            self._rougify_list = _load_rougify_list()

        # ── main line loop ────────────────────────────────────────────
        errcnt = 0
        keep_file_types = ("rar", "zip", "pdf", "doc", "mp4")

        for index, line in enumerate(lines):

            # frontmatter delimiter tracking
            if is_md_file and line.strip() == "---":
                ctx.frontmatter_count += 1
                if ctx.frontmatter_count == 1:
                    ctx.frontmatter = True
                elif ctx.frontmatter_count == 2:
                    ctx.frontmatter = False

            # strip stray file-extension spaces ("file.pdf" → "file.pdf")
            for kftype in keep_file_types:
                line = line.replace(" ." + kftype, "." + kftype)
                lines[index] = line

            # ── bold normalisation (**text** spacing) ─────────────────
            if (is_md_file
                    and line.count("**") >= 2
                    and line.count("**") % 2 == 0
                    and line.count("***") == 0
                    and not ctx.codestate):
                line = self._normalise_bold(line)
                lines[index] = line

            # ── backtick cleanup ──────────────────────────────────────
            line = line.replace("````", "```").replace("````", "```")
            linx_count = line.count("`")
            if is_md_file and linx_count >= 2 and linx_count % 2 == 0:
                line = self._normalise_backtick(line)
                lines[index] = line

            preline  = lines[index - 1] if index > 0            else ""
            nextline = lines[index + 1] if index < len(lines)-1  else ""

            # ── rouge language validation ─────────────────────────────
            li1 = refindall(r"```\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
            li2 = refindall(r"\{%\s*highlight\s*([0-9a-z_#+-]+)", line, re.IGNORECASE)
            for lang in li1 + li2:
                if lang not in self._rougify_list:
                    openTextFile(fpath)
                    print("代码语言无法识别 {}:{} \"{}\"".format(fpath, index+1, lang))
                    os.system(PAUSE_CMD)
                    return self._mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

            # ── title spacing check (pre/next line must be blank) ─────
            tag_regex = r"^\s*[#]+\s"
            preline_tag  = refindall(tag_regex, preline)
            nextline_tag = refindall(tag_regex, nextline)
            if warn_title_space and not ctx.codestate:
                tag_regex_k = r"^\s*[#]+\s{2,}"
                if refindall(tag_regex_k, preline):
                    openTextFile(fpath)
                    assert False, preline

            # ── indentation unit ──────────────────────────────────────
            idtcnt = 2 if refindall(r"^\s*[*-]+\s", line) else 4

            # ── character stats ───────────────────────────────────────
            self._char_stats.collect(line)

            # ── full-width / non-breaking space check ─────────────────
            if (line.find("\u00A0") != -1
                    and line.find("\u3000") != -1
                    and fname not in ("glslEditor.min.js",)):
                print("xspace", fpath, line)
                errcnt += 1

            # ── plugin per-line processing ────────────────────────────
            for plugin in self.plugins:
                line, delta = plugin.process_line(line, index, lines, ctx)
                errcnt += delta
            lines[index] = line

            # ── Chinese / English space check (non-code context) ──────
            if warn_cn_en_space and not ctx.codestate:
                errcnt += self._check_cn_en_space(
                    line, index, lines, ctx, keep_file_types)

            # ── chart / code state machine ────────────────────────────
            fxline = "".join(line.split())
            if fxline.startswith('<divclass="mermaid">') and not ctx.chartstate:
                ctx.chartstate = True
            if fxline.startswith("</div>") and ctx.chartstate:
                ctx.chartstate = False

            if fxline.startswith("{%highlight"):
                ctx.codestate = True
                continue
            if fxline.startswith("{%endhighlight%}"):
                ctx.codestate = False
                continue
            if fxline.startswith("```") and not ctx.codestate:
                ctx.codestate = True
                continue
            if fxline.startswith("```") and ctx.codestate:
                ctx.codestate = False
                continue

            if ctx.codestate:
                continue

            # ── title blank-line enforcement ──────────────────────────
            if warn_title_space and (preline_tag or nextline_tag):
                if line:
                    openTextFile(fpath)
                    print("标题前后空行问题 {}:{} \"{}\"".format(fpath, index+1, line))
                    os.system(PAUSE_CMD)
                    return self._mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

            # ── indentation check ─────────────────────────────────────
            count_space = getLeftSpaceCount(
                line if warn_indent_space else line.replace("\t", " "*4))
            if (count_space > 12
                    or count_space % idtcnt == 0
                    or count_space in (3,)):
                pass
            elif warn_indent_space:
                openTextFile(fpath)
                print("空格缩进问题 {}:{} \"{}\"".format(fpath, index+1, line))
                os.system(PAUSE_CMD)
                return self._mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        assert not ctx.codestate, "代码片段未闭合: " + fpath

        ctx.errcnt = errcnt

        # ── plugin post-process (e.g. appendRefs) ────────────────────
        for plugin in self.plugins:
            try:
                lines = plugin.post_process(fpath, fname, ftype_lo, lines, ctx)
            except AssertionError as ex:
                if fdepth >= 5:
                    raise ex
                openTextFile(fpath)
                traceback.print_exc()
                print("断言错误 {}".format(ex))
                os.system(PAUSE_CMD)
                return self._mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

        # ── join lines → page ─────────────────────────────────────────
        page = NEWLINE_CHAR.join(lines)
        while page.find(NEWLINE_CHAR * 3) != -1:
            page = page.replace(NEWLINE_CHAR * 3, NEWLINE_CHAR * 2)

        # ── title heading blank-line page-level fix ───────────────────
        if warn_title_space:
            # snapshot code blocks BEFORE expansion so we can restore them
            codereg  = r"\{%\s*highlight.*?\{%\s*endhighlight\s*%\}"
            coderegz = r"```.*?```"
            codeli1  = refindall(codereg,  page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            codeli1z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)

            for hdr in ("### ", "## ", "# "):
                page = page.replace(NEWLINE_CHAR*2 + hdr, NEWLINE_CHAR*3 + hdr)

            # restore code blocks that were inadvertently expanded
            codeli2  = refindall(codereg,  page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            codeli2z = refindall(coderegz, page, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            for i in range(len(codeli1)):
                page = page.replace(codeli2[i], codeli1[i])
            for i in range(len(codeli1z)):
                page = page.replace(codeli2z[i], codeli1z[i])

        # ── KangXi encoding removal ───────────────────────────────────
        if fname not in ("2021-03-14-Equivalent-Unified-Ideograph.md",):
            page = TranslateKangXi(page)

        # ── spaceback-JSON substitutions ──────────────────────────────
        spacebackfile = os.path.splitext(fpath)[0] + SPACEBACKFILE_TAIL
        spacebackjson = {}
        if not os.path.exists(spacebackfile):
            spacebackfile = os.path.join(
                os.path.split(fpath)[0],
                "k" + os.path.splitext(fname)[0] + SPACEBACKFILE_TAIL)
        if os.path.exists(spacebackfile):
            spacebackjson = readfileJson(spacebackfile, "utf8")
        page = self._apply_spaceback(page, spacebackjson)

        # ── plugin page transforms ────────────────────────────────────
        for plugin in self.plugins:
            page = plugin.transform_page(page, fpath, fname, ftype_lo, ctx)

        # ── md5 guard + write ─────────────────────────────────────────
        from pythonx.pelib import getLuckFileMd5
        md5src2 = getLuckFileMd5(fpath, ctx.md5src)
        if md5src2 == ctx.md5src:
            if not writefile(fpath, page.encode("utf8")):
                return 0
            return ctx.errcnt

        print("文本中途被改过了。{}".format(fpath))
        os.system(PAUSE_CMD)
        return self._mainfile(fpathsrc, fnamesrc, ftypesrc, fdepth+1)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _strip_line(self, line, ctx):
        """Apply rstrip then each plugin's strip_line hook."""
        for plugin in self.plugins:
            line = plugin.strip_line(line, ctx)
        return line.rstrip()

    @staticmethod
    def _normalise_bold(line):
        dotlines = line.split("**")
        newline = ""
        for idx, dot in enumerate(dotlines):
            if idx % 2 == 1:
                if not newline.strip():
                    newline = newline + "**" + dot.strip() + "** "
                else:
                    newline = newline.rstrip() + " **" + dot.strip() + "** "
            else:
                if idx >= 2:
                    newline += dot.lstrip()
                else:
                    newline += dot
        return newline.rstrip()

    @staticmethod
    def _normalise_backtick(line):
        newline = ""
        linx_count = 0
        for idx, ch in enumerate(line):
            if ch == '`':
                linx_count += 1
                if linx_count % 2 == 1:
                    if newline and not newline.endswith(" "):
                        if not newline.endswith("："):
                            newline += " "
                        newline += "`"
                    else:
                        if newline.endswith("： "):
                            newline = newline[:-1]
                        newline += "`"
                else:
                    newline += "`"
                    if idx + 1 < len(line) and line[idx + 1] != " ":
                        newline += " "
            else:
                newline += ch
        return newline

    def _check_cn_en_space(self, line, index, lines, ctx, keep_file_types):
        """Return number of Chinese/English spacing errors found."""
        from codestrip import isDiacritic

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
        for itmp in ('"WEB前端"',):
            linec = linec.replace(itmp, '""')
        linec = linec.replace('caption="',  'caption=" ')
        linec = linec.replace('caption2="', 'caption2=" ')
        linec = linec.replace('title="',    'title=" ')

        lix1 = refindall("[{}][^{} *]".format(cnregex_full, cnregex_full), linec, re.IGNORECASE)
        lix2 = refindall("[^{} *][{}]".format(cnregex_full, cnregex_full), linec, re.IGNORECASE)
        lix  = lix1 + lix2

        cnsignregex = "[{}]".format(cnsign)
        errcnt = 0
        for ix in lix:
            cx, cy = ix
            if refindall(cnsignregex, cy) or refindall(cnsignregex, cx):
                continue
            if cy in "-<]~" or cx in "->[~":
                continue
            if ctx.chartstate:
                continue
            if cx in ('"', '[') and (" " + line).count(" " + ix) == 1:
                continue
            if cy in ('"', ']', ',') and (line + " ").count(ix + " ") == 1:
                continue
            if cx in ("(",) and (" \\" + line).count(" \\" + ix) == 1:
                continue
            if cy in ("\\",) and (line + ") ").count(ix + ") ") == 1:
                continue
            if cx in ('"',) and ("[" + line).count("[" + ix) == 1:
                continue
            if cy in ('"',) and (
                    (line + "]").count(ix + "]") == 1
                    or (line + ",").count(ix + ",") == 1):
                continue

            tag_cont = False
            for kftype in keep_file_types:
                if cy in (".",) and line.count(ix + kftype) == 1:
                    tag_cont = True
            if tag_cont:
                continue

            print("[%d]" % (index+1), ix, cx, cy, "\t", line)
            errcnt += 1
            if self.args.get("format") and not ctx.frontmatter:
                line = line.replace(ix, cx + " " + cy)
                lines[index] = line

        return errcnt

    @staticmethod
    def _apply_spaceback(page, spacebackjson):
        def _spacebackreg(regkey, regmap, page):
            li = re.findall(regkey, page)
            if not li:
                return page
            for i in li:
                ix = i
                for ik in regmap.keys():
                    ix = ix.replace(ik, regmap[ik])
                page = page.replace(i, ix)
            return page

        for spacebackkey, spacebackvalue in spacebackjson.items():
            if spacebackkey == "regex":
                for regkey, regmap in spacebackvalue.items():
                    page = _spacebackreg(regkey, regmap, page)
                continue
            page = page.replace(spacebackkey, spacebackvalue)
        return page
