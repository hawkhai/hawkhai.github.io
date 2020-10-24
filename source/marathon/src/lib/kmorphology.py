#encoding=utf8
import cv2
import numpy as np

# Morphology Dilate 膨胀
def morphologyDil(img, Dilate_time=1):
    H, W = img.shape

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dilate_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y-1:y+2, x-1:x+2]) >= 250:
                    out[y-1, x-1] = 255

    return out

# Morphology Dilate 膨胀
def morphologyDilFull(img, Dilate_time=1):
    H, W = img.shape

    # kernel
    MF = np.array(((1, 1, 1),
                   (1, 0, 1),
                   (1, 1, 1)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dilate_time):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y-1:y+2, x-1:x+2]) >= 250:
                    out[y-1, x-1] = 255

    return out

def morphologyDil2(img, Dilate_time=1, linelen=3):
    H, W = img.shape

    li = range(linelen*2 + 1)

    # kernel
    MF = np.array((li,), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Dilate_time):
        YSIZE = 0
        XSIZE = linelen
        tmp = np.pad(out, ((YSIZE,YSIZE),(XSIZE,XSIZE)), 'edge')
        for y in range(YSIZE, H+YSIZE):
            for x in range(XSIZE, W+XSIZE):
                if np.sum(MF * tmp[y-YSIZE:y+YSIZE+1, x-XSIZE:x+XSIZE+1]) >= 250:
                    out[y-YSIZE, x-XSIZE] = 255
    return out

# Morphology Erode 腐蚀
def morphologyEro(img, Erode_time=1):
    H, W = img.shape
    out = img.copy()

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each erode
    for i in range(Erode_time):
        tmp = np.pad(out, (1, 1), 'edge')
        # erode
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y-1:y+2, x-1:x+2]) < 250*4:
                    out[y-1, x-1] = 0

    return out

def morphologyEro2(img, Erode_time=1, linelen=2):
    H, W = img.shape

    li = range(linelen*2+1)

    # kernel
    MF = np.array((li,), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(Erode_time):
        YSIZE = 0
        XSIZE = linelen
        tmp = np.pad(out, ((YSIZE,YSIZE),(XSIZE,XSIZE)), 'edge')
        for y in range(YSIZE, H+YSIZE):
            for x in range(XSIZE, W+XSIZE):
                if np.sum(MF * tmp[y-YSIZE:y+YSIZE+1, x-XSIZE:x+XSIZE+1]) < 250*np.sum(MF):
                    try:
                        out[y-YSIZE, x-XSIZE] = 0
                    except:
                        out[y-YSIZE, x-XSIZE] = 0
    return out

# Opening morphology 开运算可以用来去除仅存的小块像素。
def morphologyOpening(img, time=1):
    out = morphologyEro(img, Dilate_time=time)
    out = morphologyDil(out, Erode_time=time)
    return out

# Morphology Closing 闭运算能够将中断的像素连接起来。
def morphologyClosing(img, time=1):
    out = morphologyDil(img, Erode_time=time)
    out = morphologyEro(out, Dilate_time=time)
    return out

# 形态学梯度（Morphology Gradient）可以用于抽出物体的边缘。
# 形态学梯度为经过膨胀操作（dilate）的图像与经过腐蚀操作（erode）的图像的差，可以用于抽出物体的边缘。
def morphologyGradient(img, time=1):
    # Erode image
    eroded = morphologyDil(img, time)
    # Delate image
    dilated = morphologyEro(img, time)
    # Morphology
    out = np.abs(eroded - dilated) * 255
    return out

# 顶帽运算是原图像与开运算的结果图的差。可以提取出细线状的部分或者噪声。
def morphologyTopHat(img, time=3):
    # Opening process
    opened = morphologyOpening(img, time=time)
    # Tophat
    out = np.abs(img - opened) * 255
    return out

# 黑帽运算是原图像与闭运算的结果图的差。可以提取出细线状的部分或者噪声。
def morphologyBlackHat(img, time=3):
    # Opening process
    opened = morphologyClosing(img, time=time)
    # Blackhat
    out = np.abs(opened - img) * 255
    return out
