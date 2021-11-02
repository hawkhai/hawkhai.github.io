#encoding=utf8
import re, os, sys
reldirx, _lidir = "", []
while not _lidir and len(reldirx) <= 100:
    reldirx += "../"
    checkfunc = lambda idir: os.path.exists(reldirx+idir+"/pythonx/funclib.py")
    _lidir = [reldirx+idir for idir in os.listdir(reldirx) if checkfunc(idir)]
    if _lidir: reldirx = _lidir[0]
sys.path.append(reldirx)
from pythonx.funclib import *

def main():
    urls = readfileLines("urls.txt")
    for url in urls:
        if not url.startswith("https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&"):
            continue
        print(url)
        try:
            fjson = netgetJsonCache(url, unssl=True)
            # {"ret":-6,"errmsg":"unknown error","home_page_list":[]}
            assert fjson["ret"] == 0, fjson
        except json.decoder.JSONDecodeError as ex: # Expecting value: line 1 column 1 (char 0)
            print(ex)
            raise ex
        time.sleep(5)

if __name__ == "__main__":
    main()
