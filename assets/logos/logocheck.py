#encoding=utf8
import re, os, sys
from PIL import Image

def getLeftZeroCount(li):
    li = li[:]
    count = 0
    while li and li[0][1] == (0, 0, 0, 0):
        count += 1
        li = li[1:]
    #print(li[0][1])
    return count

def getRightZeroCount(li):
    li = li[:]
    count = 0
    while li and li[-1][1] == (0, 0, 0, 0):
        count += 1
        li = li[:-1]
    #print(li[-1][1])
    return count

def maincheck(fpath):
    img = Image.open(fpath)
    width, height = img.size
    #print(img.size, img.getpixel((0, 0)))
    print(fpath)

    LIX = []
    for x in range(width):
        R, G, B, A = 0, 0, 0, 0
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            R += r
            G += g
            B += b
            A += a
        LIX.append([x, (R, G, B, A)])

    LIY = []
    for y in range(height):
        R, G, B, A = 0, 0, 0, 0
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            R += r
            G += g
            B += b
            A += a
        LIY.append([y, (R, G, B, A)])

    l, r = getLeftZeroCount(LIX), getRightZeroCount(LIX)
    t, b = getLeftZeroCount(LIY), getRightZeroCount(LIY)
    print(l, r)
    print(t, b)
    #print(l*1.0/width, r*1.0/width)
    #print(t*1.0/height, b*1.0/height)
    print()

if __name__ == "__main__":
    maincheck("csdn-logo.png")
    maincheck("jianshu.png")
    maincheck("wikipedia.png")
