#encoding=utf8
"""
mdformat.py  --  MD formatting entry point (refactored from mdrstrip.py).

Original monolithic script: mdrstrip.py  (unchanged).
Core engine:  mdformat/core.py
Blog plugin:  mdformat/plugins/blog.py

Usage (identical to mdrstrip.py):
    python mdformat.py [workdir] [format] [rebuild] [copyres] [clearimg]
                       [ignoreerr] [openfile] [openresent] [openresentx]
                       [netfake] [debug] [only <fname>]
"""

import os, sys, time
sys.path.append("../")

__file__ = os.path.abspath(__file__)

# ── cache db (same role as in mdrstrip.py) ────────────────────────────────
from pythonx.funclib import LocalLimitedDict, removedirTimeout, cleardirEmpty

CACHEFILE = os.path.join("tempdir", "mycache", os.path.split(__file__)[-1], "cache.db")
print("CACHEFILE", CACHEFILE)
MYCACHE   = LocalLimitedDict(CACHEFILE, max_size=10000)

# ── parse command-line flags ──────────────────────────────────────────────
ARGS = {
    "openfile":    "openfile"    in sys.argv,
    "format":      "format"      in sys.argv,
    "rebuild":     "rebuild"     in sys.argv,
    "copyres":     "copyres"     in sys.argv,
    "clearimg":    "clearimg"    in sys.argv,
    "ignoreerr":   "ignoreerr"   in sys.argv,
    "openresent":  "openresent"  in sys.argv or "openresentx" in sys.argv,
    "openresentx": "openresentx" in sys.argv,
    "netfake":     "netfake"     in sys.argv,
    "debug":       "debug"       in sys.argv,
    "_argv":       sys.argv[:],
}

# ── imports ───────────────────────────────────────────────────────────────
from codestrip import buildSnapCache
from pythonx.funclib import parsePythonCmdx, CWD_DIR_RUN, getPythonExe

from mdformat.core import MdFormatter
from mdformat.plugins.blog import BlogPlugin, _read_iglist

# ── ignore lists (same as mdrstrip.py main()) ────────────────────────────
CHECK_IGNORE_LIST = [
    "backup", "tempdir", "_site",
    "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
    "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata",
    "imgclassify", "node_modules", "pdftools",
]

MAINW_IGNORE_LIST = [
    "backup", "tempdir",
    "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
    "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata",
    "imgclassify", "openglcpp", "d2l-zh", "mathjax", "msgboard",
    "node_modules", "pdftools",
]

def _extend_from_config(lst):
    """Append extra dirs from mdrstrip_dir_ignore.txt."""
    igdirs = _read_iglist("config/mdrstrip_dir_ignore.txt")
    for d in igdirs:
        if d not in lst:
            lst.append(d)
    return lst

def main():
    buildSnapCache("backup")
    buildSnapCache("invisible" + os.sep + "backup")

    # ── build plugin + formatter ────────────────────────────────────────────────────
    blog_plugin = BlogPlugin(mycache=MYCACHE, ignoreerr=ARGS["ignoreerr"])
    formatter   = MdFormatter(args=ARGS, plugins=[blog_plugin], mycache=MYCACHE)

    # file-size check pass
    _extend_from_config(CHECK_IGNORE_LIST)
    blog_plugin.run_pre_scan(
        [".", "backup", "invisible" + os.sep + "backup"],
        CHECK_IGNORE_LIST,
    )

    _extend_from_config(MAINW_IGNORE_LIST)
    formatter.run(
        mainw_ignore_list=MAINW_IGNORE_LIST,
        script_file=__file__,
    )

def mainw():
    print(parsePythonCmdx(__file__))
    timea = time.time()
    main()
    removedirTimeout("tempdir")
    cleardirEmpty("tempdir")
    timeb = time.time()
    print("Total Time =", timeb - timea)

if __name__ == "__main__":
    print(sys.argv)
    import cProfile

    if len(sys.argv) >= 2 and os.path.isdir(sys.argv[1]):
        workdir = sys.argv[1]
        @CWD_DIR_RUN(workdir)
        def maingo():
            cProfile.run("mainw()") if ARGS["debug"] else mainw()
        maingo()
    else:
        cProfile.run("mainw()") if ARGS["debug"] else mainw()
        os.system(r"cd invisible & {} tempd.py encrypt".format(getPythonExe()))

    if MYCACHE:
        MYCACHE.del_impl()
    del MYCACHE
    print(parsePythonCmdx(__file__))
