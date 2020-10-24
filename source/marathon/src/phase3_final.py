#encoding=utf8
import os, re, sys
import cv2
import numpy as np
from lib.sky import *
from lib.kmorphology import *
from lib import kalgorithm

inputfile = r"./output_images/phase3/phase3_sky.jpg"
skyfile = r"./input_images/phase3/phase3_sky.jpg"

outfile = r"./output_images/phase3/phase3_sky_final.png"
repairfile = r"./output_images/phase3/phase3_repaired.png"

from phase3_sky import mainfixfile, display, findvline
from lib.kaffine import affine

# 定义函数，高斯高/低通滤波模板
def gaussianMask(src, dr):
    template = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32) # 构建滤波器
    r, c, ZZ = src.shape
    for i in np.arange(r):
        for jj in np.arange(c):
            j = int(jj - c/4 + c)
            if j >= c: j -= c
            if j < 0: j += c
            distance = np.sqrt((i - r/2)**2 + (j - c/2)**2)
            template[i, j] = (np.e ** (-1 * (distance**2 / (2 * dr ** 2)))) # Gaussian 滤波函数 ** 0.8
            template[i, j] = (template[i, j]) * 0.8 + 0.7
    return template

def maintask(xcode):
    # 在前面结果的基础上，继续工作。
    prefile = r"./output_images/phase3/phase3_sky.jpg_sky_cloud.png"
    imgsrc = kalgorithm.imgRead(prefile).astype(np.float32)

    mask_fishergirl = inputfile+"_fisher_girl_mask.png"
    mask_sea        = inputfile+"_ocean_wave_mask.png"
    mask_sky        = inputfile+"_sky_mask.png"

    sky = kalgorithm.imgRead(skyfile).astype(np.float32)
    mask_sea = (kalgorithm.imgRead(mask_sea).astype(np.float32))

    sky = kalgorithm.blInterpolate(sky, 0.33333333334, 0.33333333334)

    skydst = sky.copy()
    skyH, skyW, skyC = sky.shape
    for y in range(skyH):
        for x in range(skyW):
            skydst[y,x] = sky[skyH-1-y, skyW-1-x]
    sky = skydst

    print(imgsrc.shape, sky.shape) # (744, 1100, 3) (618, 1100, 3)
    print(mask_sea.shape) # (744, 1100, 3)

    newsky = np.zeros((mask_sea.shape[0], mask_sea.shape[1], sky.shape[2]), np.uint8)
    newsky[:, :] = 0

    peak = findvline() # 前面算出来了这个分割位置
    print("peak", peak)
    newsky[peak:, :] = sky[:newsky.shape[0]-peak, :]
    print(newsky.shape)

    # 水面 云彩 倒影
    # affine(img, a=1, b=0, c=0, d=1, tx=tx, ty=ty)
    print(newsky.shape, mask_sea.shape, imgsrc.shape)

    mask_sea[:peak, ...] = 0
    mask_sea = kalgorithm.bgr2gray(mask_sea)

    mask_sea[..., :5] = 0
    mask_sea[..., mask_sea.shape[1]-5:] = 0

    if not os.path.exists(outfile+"_mask_sea.png"):
        mask_sea = morphologyDilate(mask_sea, 2) # 膨胀3
        mask_sea = morphologyDilateLine(mask_sea, 2, linelen=3) # 膨胀3

        mask_sea = kalgorithm.meanFilter2D(mask_sea) # 滤波
        kalgorithm.imgSave(outfile+"_mask_sea.png", mask_sea)
        display(mask_sea)
    mask_sea = kalgorithm.imgRead(outfile+"_mask_sea.png").astype(np.float32) / 255

    print(imgsrc.shape, mask_sea.shape)
    outv = ((newsky * mask_sea*0.3) + # 下面部分，0.6 天空
            (imgsrc * mask_sea*0.5) + # 下面部分，0.4 原图
            (imgsrc * (1-mask_sea) * 0.5) + # 上面部分，0.6 原图
            (newsky * (1-mask_sea) * 0.3)) # 上面部分，0.4 天空-黑色
    hsv = kalgorithm.bgr2hsv(outv)
    print(outv.shape, outv[0, 0])

    H, W, C = outv.shape

    GSIZE = H
    GaussianMask = gaussianMask(outv, dr=GSIZE/4)

    maxx = 0
    minx = 100000
    for y in range(H):
        for x in range(W):
            if hsv[y, x, 0] > maxx:
                maxx = hsv[y, x, 0]
                print(hsv[y, x])
            if hsv[y, x, 0] < minx:
                minx = hsv[y, x, 0]
                print(hsv[y, x])
            hsv[y, x, 0] = xcode#(70*2+hsv[y, x, 0])/3
            hsv[y, x, 2] = hsv[y, x, 2] * (GaussianMask[y, x])
    outv = kalgorithm.hsv2bgr(hsv, outv)
    print(maxx, minx)
    #display(outv)

    # 降低画面曝光度，伽马变换
    imgsrc = imgsrc#alg.gammaCorrection(imgsrc, g=0.5)
    print(imgsrc.shape, imgsrc[0, 0])
    hsv = kalgorithm.bgr2hsv(imgsrc)
    print(imgsrc.shape, imgsrc[0, 0])
    H, W, C = imgsrc.shape
    for y in range(H):
        for x in range(W):
            hsv[y, x, 2] = hsv[y, x, 2] / 3
    imgsrc = kalgorithm.hsv2bgr(hsv, imgsrc)
    #display(imgsrc)

    #渔女剪影效果
    #背景调暗，渔女调整的更暗。
    outvgril = imgsrc#alg.gammaCorrection(outv, g=0.3)

    mask_fishergirl = 1.0 - kalgorithm.imgRead(mask_fishergirl).astype(np.float) / 255
    outv = outv * (1-mask_fishergirl) + outvgril*mask_fishergirl
    outv = np.clip(outv, 0, 255)

    #cv2.putText(outv, "{}".format(xcode), (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
    #    1, (0, 255, 255), 1, cv2.LINE_AA)

    outv = kalgorithm.meanFilter(outv)
    kalgorithm.imgSave(outfile, outv)

if __name__ == "__main__":

    mainfixfile()
    maintask(35) # 疑似最接近
