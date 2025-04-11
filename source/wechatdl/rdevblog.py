#encoding=utf8
import re, os, sys
from pathlib import Path
check_pythonx_dir = lambda x: x and os.path.exists(os.path.join(x, "funclib.py"))
check_ksource_dir = lambda x: x and check_pythonx_dir(os.path.join(x, "pythonx"))
for reldirx in (os.path.dirname(os.path.abspath(__file__)), # 这个先，规避加载漏洞。
                os.path.abspath(".")):
    while len(reldirx) > 3: # 3 应该所有平台都问题不大。
        if check_ksource_dir(reldirx): break # YES!!
        reldirx = os.path.dirname(reldirx) # 只尝试 funclib.py，funclib.pyc 存在版本问题。
    if check_ksource_dir(reldirx): break # YES!!
for devdirx in [r"E:\kSource", r"D:\kSource", r"C:\kSource"]:
    if not check_ksource_dir(reldirx):
        reldirx = devdirx
if check_ksource_dir(reldirx) and not reldirx in sys.path:
    sys.path.append(reldirx) # 放到最后，避免 sys.path.insert
del devdirx # reldirx 可以继续使用
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
