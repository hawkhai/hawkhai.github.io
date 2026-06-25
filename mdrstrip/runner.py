#encoding=utf8
"""Top-level scan orchestration for the mdrstrip command."""
from .runtime import *
from .config import readFileIgnoreList
from .filesystem import checkFileSize, checkReviewJS, onCheckDirectory
from .formatter import mainfile, viewchar
from .resources import tidyupImgClear, tidyupImgCollect

def mainfilew(fpath, fname, ftype):

    #if fname not in ("layout.md", "README.md"):
    #    return

    if not REBUILD and checklog(SCRIPT_FILE, fpath):
        # print("cached", fpath)
        return 0

    if "only" in sys.argv:
        if not fname in sys.argv:
            return 0

    removelog(SCRIPT_FILE, fpath)
    errcnt = mainfile(fpath, fname, ftype)
    if errcnt == 0:
        savelog(SCRIPT_FILE, fpath)
    return errcnt

def mainw():
    print(parsePythonCmdx(SCRIPT_FILE))
    timea = time.time()
    main()
    removedirTimeout("tempdir")
    cleardirEmpty("tempdir")
    timeb = time.time()
    print("Total Time =", timeb - timea)

def main():
    buildSnapCache("backup")
    buildSnapCache("invisible"+os.sep+"backup")
    if REBUILD or OPENRESENT:
        checkReviewJS("assets"+os.sep+"reviewjs", ".")
        checkReviewJS("invisible"+os.sep+"reviewjs", "invisible")
    if CLEARIMG:
        tidyupImgCollect("assets"+os.sep+"images")
        tidyupImgCollect("invisible"+os.sep+"images")

    igdirs = readFileIgnoreList("config/ignored-dirs.txt")

    CHECK_IGNORE_LIST = [
        "backup", "tempdir", "_site",
        "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata", "imgclassify", "ksample",
        "node_modules", "pdftools", "cc-switch",
        ]
    CHECK_IGNORE_LIST.extend(igdirs)
    searchdir(".", checkFileSize, ignorelist=CHECK_IGNORE_LIST, onDirectory=onCheckDirectory)
    searchdir("backup", checkFileSize, ignorelist=CHECK_IGNORE_LIST, onDirectory=onCheckDirectory)
    searchdir("invisible"+os.sep+"backup", checkFileSize, ignorelist=CHECK_IGNORE_LIST, onDirectory=onCheckDirectory)

    MAINW_IGNORE_LIST = [
        "backup", "tempdir",
        "Debug", "Release", ".vs", "opengl-3rd", "opengles3-book", "opengles-book-samples",
        "UserDataSpider", "docs.gl", "ml-notes", "ksample", "dataset", "pdfdata", "imgclassify", "ksample",
        "openglcpp", "d2l-zh", "mathjax", "msgboard",
        "node_modules", "pdftools", "cc-switch",
        ]
    MAINW_IGNORE_LIST.extend(igdirs)
    searchdir(".", mainfilew, ignorelist=MAINW_IGNORE_LIST, reverse=True)
    if REBUILD:
        clearSnapCache()
        cleardirEmpty("images")
        cleardirEmpty("source")
        tidyupImgClear()

    global G_CSCHAR
    global G_TYPESET

    viewchar(G_CNCHAR, "cnfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(G_CSCHAR, "csfile.txt", 0x80, 0x7FFFFFFF)
    viewchar(G_ENCHAR, "enfile.txt", 0x0,  0x7F)

    print(LINE_SEP_SHORT)
    G_CSCHAR = list(set(G_CSCHAR))
    G_CSCHAR.sort()
    print("".join(G_CSCHAR))
    imgset  = ("jpeg", "jpg", "png", "gif", "bmp", "jfif")
    fontset = ("eot", "ttf", "woff", "svg", "woff2", )
    codeset = ("cc", "js", "txt", "xml", "css", "mk", "lock", "zip", "makefile", "scss",)
    G_TYPESET -= set(imgset)
    G_TYPESET -= set(fontset)
    G_TYPESET -= set(codeset)
    print(G_TYPESET)
    print(G_MDKEYSET)

    hostlist = sorted(G_HOSTSET.items(), key=lambda x: x[1], reverse=True)
    print(hostlist)
    for hostx in hostlist[:10]:
        print(hostx)
