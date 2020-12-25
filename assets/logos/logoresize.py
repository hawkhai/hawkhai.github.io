#encoding=utf8
import re, os, sys
from PIL import Image

def maincheck(fpath, action, xsize, test):
    img = Image.open(fpath)
    width, height = img.size
    print()
    print((fpath, action, xsize, test), img.size, img.getpixel((0, 0)))

    if action == "l" or action == "r":
        dst = Image.open("csdn-logo.png").crop((0, 0, 1, 1)).resize(
            ((width-xsize) if ("x" in sys.argv) else (width+xsize), height))
    if action == "t" or action == "b":
        dst = Image.open("csdn-logo.png").crop((0, 0, 1, 1)).resize(
            (width, (height-xsize) if ("x" in sys.argv) else (height+xsize)))

    def checkedge(img, pos, rgba):
        w, h = img.size
        x, y = pos
        if x >= 0 and x < w and y >= 0 and y < h:
            img.putpixel(pos, rgba)

    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if "x" in sys.argv:
                if action == "l":
                    checkedge(dst, (x-xsize, y), (r, g, b, a))
                if action == "t":
                    checkedge(dst, (x, y-xsize), (r, g, b, a))
                if (action == "r" or action == "b"):
                    checkedge(dst, (x, y), (r, g, b, a))
            else:
                if action == "l":
                    dst.putpixel((x+xsize, y), (r, g, b, a))
                if action == "t":
                    dst.putpixel((x, y+xsize), (r, g, b, a))
                if (action == "r" or action == "b"):
                    dst.putpixel((x, y), (r, g, b, a))
    if test:
        a, b = os.path.split(fpath)
        fpath = os.path.join(a, "test"+b+".png")
        dst.save(fpath)
    else:
        dst.save(fpath)
    print(fpath, dst.size)
    return fpath

if __name__ == "__main__":
    print(sys.argv)
    for t in sys.argv[2]:
        sys.argv[1] = maincheck(sys.argv[1], t, int(sys.argv[3]), "test" in sys.argv)
