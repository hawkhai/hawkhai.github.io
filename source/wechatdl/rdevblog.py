#encoding=utf8
import re, os, sys
for reldirx, _lidir in (
        (os.path.dirname(os.path.abspath(__file__)), []), # 这个先，规避加载漏洞。
        (os.path.dirname(os.path.abspath(".")), [])):
    while not _lidir and len(reldirx) > 3: # 3 应该所有平台都问题不大。
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本。
        _checkfunc = lambda idir: os.path.exists(os.path.join(reldirx, idir, "pythonx", "funclib.py"))
        _lidir = [os.path.join(reldirx, idir) for idir in os.listdir(reldirx) if _checkfunc(idir)]
        assert len(_lidir) in (0, 1), _lidir
        if _lidir: reldirx = os.path.abspath(_lidir[0])
        del _checkfunc
    if _lidir: break
if not reldirx in sys.path: sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del _lidir # reldirx 可以继续使用
from pythonx.funclib import *
import urllib.parse

def analyzepage(fdata):
    articles = re.findall("<article.*?</article>", fdata, re.DOTALL | re.MULTILINE)
    mdpage = ""
    index = 0
    for article in articles:
        img = re.findall('<img width="[0-9]+" height="[0-9]+" src="(http://blog.rdev.kingsoft.net/.*?)"', article)
        if not img:
            img = re.findall('<img src="(http://blog.rdev.kingsoft.net/.*?)" />', article)

        href = re.findall('<h2 class="entry-title"><a href="(http://blog.rdev.kingsoft.net/\\?p=[0-9]+)" rel="bookmark">(.*?)</a></h2>', article)
        assert len(img) == 1, article
        assert len(href) == 1, article
        img = img[0]
        href, title = href[0]
        print(img)
        print(href)
        print(title)
        # http://blog.rdev.kingsoft.net/wp-content/uploads/2021/11/%E9%82%AE%E4%BB%B6-400x350.jpeg
        img = img.split("/")
        img[-1] = urllib.parse.quote(img[-1])
        img = "/".join(img)

        index = index + 1
        mdpage += "{}. <img width=\"400\" height=\"350\" src=\"{}\" /> [{}]({})\r\n".format(index, img, title, href)
        #print(img)
        #img = netgetCache(img)

    return mdpage

def main():
    mdpage = ""
    for i in range(1, 100):
        url = r"http://blog.rdev.kingsoft.net/?paged={}".format(i)
        print(url)
        fdata = netgetCache(url, chrome=True)
        mdpage += analyzepage(bytesToString(fdata, "utf8"))

    # http://localhost:4000/blog/source/wechatdl/rdevblog
    localfile = "rdevblog.md"
    writefile(localfile, stringToBytes(mdpage, "utf8"))
    openTextFile(localfile)

if __name__ == "__main__":
    main()
