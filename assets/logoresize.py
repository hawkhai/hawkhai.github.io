#encoding=utf8
import re, os, sys
from PIL import Image

def maincheck(fpath, action):
    img = Image.open(fpath)
    width, height = img.size
    #print(img.size, img.getpixel((0, 0)))
    print(fpath)

    if action == "l" or action == "r":
        dst = Image.open(fpath).resize((width-1 if "x" in sys.argv else width+1, height))
    if action == "t" or action == "b":
        dst = Image.open(fpath).resize((width, height-1 if "x" in sys.argv else height+1))

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
                    checkedge(dst, (x-1, y), (r, g, b, a))
                if action == "t":
                    checkedge(dst, (x, y-1), (r, g, b, a))
                if (action == "r" or action == "b"):
                    checkedge(dst, (x, y), (r, g, b, a))
            else:
                if (action == "l" or action == "t"):
                    dst.putpixel((x, y), (r, g, b, a))
                if action == "r":
                    dst.putpixel((x+1, y), (r, g, b, a))
                if action == "b":
                    dst.putpixel((x, y+1), (r, g, b, a))
    dst.save(fpath)

if __name__ == "__main__":
    print(sys.argv)
    maincheck(sys.argv[1], sys.argv[2])
