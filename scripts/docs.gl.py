#encoding=utf8
import re, os, sys
sys.path.append("../../")
from pythonx.funclib import *

gmap = {}
def calcgmap():
    def mainfile(fpath, fname, ftype):
        if ftype == "xhtml":
            fname = fname[:-len(".xhtml")]
        if not fname in gmap.keys():
            gmap[fname] = []
        gmap[fname].append(fpath)
    searchdir("docs.gl", mainfile)

def getgmap(funx):
    if funx in gmap.keys():
        paths = gmap[funx]
        # <b class="fsfunc">glActiveTexture</b>
        # <strong class="fsfunc">glBindImageTexture</strong>
        # http://docs.gl/es2/glEnableVertexAttribArray
        #        docs.gl\\gl2\\glBufferSubData
        def getpage(i):
            fdata = readfile(i, True)
            li = re.findall('^<script>window.location.replace\\("(.*?)"\\);</script>$', fdata.strip())
            if li:
                if li[0] in gmap.keys():
                    redi = gmap[li[0]]
                    page = "\r\n\r\n".join([getpage(i) for i in redi])
                    return page
                else:
                    url = "http://docs.gl" + i.split("docs.gl")[-1].replace("\\", "/")
                    fdata = netgetCache(url, chrome=True)
                    fdata = bytesToString(fdata)
                    return fdata
            return fdata
        page = "\r\n\r\n".join([getpage(i) for i in paths])
        li = re.findall('<(?:b|strong) class="fsfunc">(.*?)</(?:b|strong)>', page)
        return list(set(li))
    return []

def main():
    calcgmap()
    li = readfileCfglist("docs.gl.txt")
    mdfpath = "../_posts/2021-01-22-shader-OpenGL-ex-irrlicht.md"
    mdfile = readfile(mdfpath, True)
    for line in li:
        x, y = line.split(" ", 1)
        x, y = x.strip(), y.strip()
        if x in ("glEndList",):
            continue
        if y in ("Built-In Variables",):
            continue
        count = getgmap(x)
        print(x, y, count)
        assert count
        count.append(x)
        for glname in count:
            # **glScissor** $$State Management$$
            # $$NV/AMD/ATI \leadsto EXT \leadsto ARB \leadsto GL$$
            mdfile = mdfile.replace("**{}**".format(glname), "**{}** $${}$$".format(glname, y))
            mdfile = mdfile.replace("**{}NV**".format(glname), "**{}NV** $${}$$".format(glname, y))
            mdfile = mdfile.replace("**{}AMD**".format(glname), "**{}AMD** $${}$$".format(glname, y))
            mdfile = mdfile.replace("**{}ATI**".format(glname), "**{}ATI** $${}$$".format(glname, y))
            mdfile = mdfile.replace("**{}EXT**".format(glname), "**{}EXT** $${}$$".format(glname, y))
            mdfile = mdfile.replace("**{}ARB**".format(glname), "**{}ARB** $${}$$".format(glname, y))
            for j in range(3):
                mdfile = mdfile.replace("$${}$$ $${}$$".format(y, y), "$${}$$".format(y))
            targetp = "$$\\bbox[yellow,border:1px solid red]{}$$".format("{%s}"%y)
            target = "$$\\bbox[yellow]{}$$".format("{%s}"%y)
            for j in range(3):
                mdfile = mdfile.replace(targetp, target)
            mdfile = mdfile.replace("$${}$$".format(y), target)
            for j in range(3):
                mdfile = mdfile.replace(target + " " + target, target)
    print(writefile(mdfpath, mdfile))

if __name__ == "__main__":
    main()
