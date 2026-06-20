#encoding=utf8
"""Shared imports, command flags, constants, and cache state for mdrstrip."""
import re, os, sys
sys.path.append("../")
import datetime, time
import traceback
from urllib.parse import unquote
from codestrip import *
from pythonx.funclib import *
from pythonx.kangxi import TranslateKangXi
from pythonx.pelib import getLuckFileMd5, get_local_ipinfo

SCRIPT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "mdrstrip.py"))
CACHEFILE = os.path.join("tempdir", "mycache", os.path.split(SCRIPT_FILE)[-1], "cache.db")
MYCACHE = None

def _should_open_cache():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0].lower() == "mdrstrip"

if _should_open_cache():
    print("CACHEFILE", CACHEFILE)
    MYCACHE = LocalLimitedDict(CACHEFILE, max_size=10000)

from PIL import Image
# AttributeError: module 'PIL.Image' has no attribute 'Resampling'
PIL_IMAGE_SAMPLE = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.ANTIALIAS

# Paranoid text spacing in Python
# https://github.com/vinta/pangu.py

OPENFILE   = "openfile" in sys.argv
AUTOFORMAT = "format" in sys.argv
REBUILD    = "rebuild" in sys.argv
COPYRES    = "copyres" in sys.argv
CLEARIMG   = "clearimg" in sys.argv
IGNOREERR  = "ignoreerr" in sys.argv
OPENRESENT = "openresent" in sys.argv or "openresentx" in sys.argv
OPENRESENTx = "openresentx" in sys.argv
NETFAKE    = "netfake" in sys.argv
DEBUG = "debug" in sys.argv
LINKTAGARRAY = (("bili",     "bilibili.com"),
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

SPACEBACKFILE_TAIL = ".spaceback.json"
NEWLINE_CHAR = "\r\n" if IS_WINDOWS else "\n"
PAUSE_CMD = "pause" if IS_WINDOWS else "read -p 'Press [Enter] key to continue...'"

G_CACHE_IGLIST = {}

# copyfrom E:\kSource\blog\checkcache.py
G_CHECKPAGE = []

G_IMG_TAGED = set() # 图片资源等。

G_HOSTSET = {}

G_CNCHAR = []
G_CSCHAR = [] # 中文符号集合
G_ENCHAR = []
G_TYPESET = set()
G_MDKEYSET = set()
SNAPSHOT_HTML = "<font class='ref_snapshot'>参考资料快照</font>"
REVIEW_REGEX  = "^<p class='reviewtip'><script type='text/javascript' src='{% include relrefx?.html url=\".*?\" %}'></script></p>$"
REVIEW_FORMAT = "<p class='reviewtip'><script type='text/javascript' src='{%% include relref.html url=\"/%s.js\" %%}'></script></p>"
REVIEW_LINE   = "<hr class='reviewline'/>"
REVIEW_JS_PATH = "%s.js"
ROUGIFY_LIST = None

G_CHECKTINUE_SET = {}

def close_cache():
    global MYCACHE
    if MYCACHE:
        MYCACHE.del_impl()
    MYCACHE = None
