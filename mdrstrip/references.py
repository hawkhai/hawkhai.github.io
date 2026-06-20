#encoding=utf8
"""Markdown snapshot-reference removal and append logic."""
from .runtime import *
from .config import readFileIgnoreList
from .resources import collectHost

def removeRefs(fpath, lines):
    lineCount = len(lines)
    headIndex = -1
    for index in range(lineCount):
        i = lineCount-1 - index
        if not lines[i] or not lines[i].strip():
            continue
        if refindall("^- \\[{}\\]\\({}\\)$".format(".*?", ".*?"), lines[i]): # \\[[0-9]+\\]
            continue
        if lines[i] == SNAPSHOT_HTML:
            headIndex = i
            break
        break

    if headIndex != -1:
        assert lines[headIndex-1] == "" or refindall(REVIEW_REGEX, lines[headIndex-1]), "%r"%lines[headIndex-1]
        if lines[headIndex-2] in ("-----", REVIEW_LINE): #, "%r"%lines[headIndex-2]
            assert lines[headIndex-3] == "", "%r"%lines[headIndex-3]
            lines = lines[:headIndex-3]
        else: # 没有 REVIEW_REGEX 的情况。
            if lines[headIndex-2] == "": #, "%r"%lines[headIndex-2]
                lines = lines[:headIndex-2]
            else:
                lines = lines[:headIndex-1]
    else:
        while lines and (lines[-1] in ("", "-----", REVIEW_LINE) or
                refindall(REVIEW_REGEX, lines[-1])):
            lines = lines[:-1]
    return lines

def appendRefs(fpath, md5src, lines, imgthumb, mdconfig):
    reflist = []

    for index, line in enumerate(lines):
        ireflist, line = collectHost(fpath, md5src, line, imgthumb)
        lines[index] = line
        if ireflist:
            reflist.extend(ireflist)

    invdir = isInvisibleDir(fpath)
    fpath = os.path.relpath(fpath, ".")
    frelgit = fpath
    if os.path.exists(fpath+".tempd"): # 存在加密版本。
        frelgit = fpath+".tempd"

    def getDateStr(frelgit):
        # 获取 md 文件的最后修改时间。
        cmdx = 'git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'.format(frelgit)
        if invdir:
            cmdx = 'cd {} & git log -n 1 --pretty=format:"%ad" --date=short -- "{}"'.format(*frelgit.split(os.sep, 1))
        if invdir and IS_MACOS:
            cmdx = 'cd {} && git log -n 1 --pretty=format:"%ad" --date=short -- "{}" && cd ..'.format(*frelgit.split(os.sep, 1))

        try:
            datestr = popenCmd(cmdx)
            datestr = bytesToString(datestr)
        except FileNotFoundError: # [Errno 2] No such file or directory: 'cd invisible && git log -n 1 --pretty=format:"%ad" --date=short -- "ncnn/onnxruntime-for-win7/README_EN.md" && cd ..'
            datestr = None
        if not datestr:
            datestr = datetime.datetime.now().date()
        return datestr

    if fpath.startswith("_posts"+os.sep):
        fpath = os.path.join("blogs", fpath.split(os.sep)[-1])
    if invdir:
        fpath = "invisible"+os.sep+"reviewjs"+os.sep+ fpath[len("invisible"+os.sep):]
    else:
        fpath = "assets"+os.sep+"reviewjs"+os.sep + fpath

    reviewjs = REVIEW_JS_PATH % (fpath)
    fcode = readfile(reviewjs, True)
    fcheck = refindall("[0-9a-f]{32}", fcode)
    if fcheck and md5src == fcheck[0]:
        pass
    else:
        fcode = """document.write("%s: review"); // md5src=%s%s""" % (
                getDateStr(frelgit), md5src, NEWLINE_CHAR)
        writefile(reviewjs, fcode)
    review = REVIEW_FORMAT % (fpath.replace("\\", "/"))
    assert refindall(REVIEW_REGEX, review), review

    if "sortrefs: true" in lines:
        reflist = sorted(reflist, key=lambda x: x[1], reverse=False)

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
        count = 0
        for url, remote in reflist:
            if url in urlset: continue
            urlset.add(url)
            count = count + 1
            if mdconfig:
                remote = "{% " + ("include relrefx.html url=\"/%s\"" % (remote,)) + " %}"
                lines.append("- [{}]({})".format(url, remote)) # count
            else:
                lines.append("- [{}]({})".format(url, url)) # count
        lines.append("")
    else:
        if mdconfig:
            lines.append("")
            lines.append("")
            lines.append(REVIEW_LINE)
            lines.append(review)
            lines.append("")
    return lines
