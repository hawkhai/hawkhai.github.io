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

repairfile = r"./output_images/phase3/phase3_repair.png"
repairmaskfile = r"./output_images/phase3/phase3_repair_mask.png"

from phase3_sky import mainfixfile, display, findvline
from lib.kaffine import affine

def findGrilCenter():
    outv = kalgorithm.bgr2gray(kalgorithm.imgRead(repairmaskfile))
    outv = kalgorithm.thresholdBinarization(outv)

    H, W = outv.shape
    xhistogram = np.sum(outv.astype(np.float32), axis=0) # 纵向投影

    xmin = np.min(xhistogram)
    xmax = np.max(xhistogram)
    result = 0
    lastvalue = 0
    assert len(xhistogram) == W
    for i in range(len(xhistogram)):
        if i > 5 and i <W-5 and xhistogram[i] > lastvalue:
            #print(i, xhistogram[i])
            result = i
            lastvalue = xhistogram[i]
    print("findGrilCenter", result)
    return result

# 自定义函数，高斯高/低通滤波模板
def gaussianMask(src, dr):
    template = np.zeros((src.shape[0], src.shape[1]), dtype=np.float32) # 构建滤波器
    r, c, ZZ = src.shape
    hcenter = c/2 # findGrilCenter()
    hshift = c/2 - hcenter # 左移的距离
    for i in np.arange(r):
        for cj in np.arange(c):
            j = int(cj + hshift - c)
            if j >= c: j -= c
            if j < 0: j += c
            if j >= c: j -= c
            if j < 0: j += c
            distance = np.sqrt((i - r/2)**2 + (j - c/2)**2)
            template[i, cj] = (np.e ** (-1 * (distance**2 / (2 * dr ** 2)))) # Gaussian 滤波函数 ** 0.8
            template[i, cj] = template[i, cj]*0.5 + 0.5
    return template

def maintask(xcode):
    # 在前面结果的基础上，继续工作。
    prefile = r"./output_images/phase3/phase3_sky.jpg_sky_cloud.png"
    imgsrc = kalgorithm.imgRead(prefile).astype(np.float32)

    mask_fishergirl = inputfile+"_fisher_girl_mask.png"
    mask_sea        = inputfile+"_ocean_wave_mask.png"
    mask_sky        = inputfile+"_sky_mask.png"

    sky = kalgorithm.imgRead(skyfile).astype(np.float32)
    mask_sea = kalgorithm.imgRead(mask_sea).astype(np.float32)

    sky = kalgorithm.blInterpolate(sky, 0.33333333334, 0.33333333334)

    # 做一个天空的镜像
    skydst = sky.copy()
    skyH, skyW, skyC = sky.shape
    for y in range(skyH):
        for x in range(skyW):
            skydst[y, x] = sky[skyH-1-y, skyW-1-x]
    sky = skydst

    print("imgsrc", imgsrc.shape, "sky", sky.shape) # (744, 1100, 3) (618, 1100, 3)
    print("mask_sea", mask_sea.shape) # (744, 1100, 3)

    # 把天空镜像搞成一样大，才可以做乘法。
    newsky = np.zeros((mask_sea.shape[0], mask_sea.shape[1], sky.shape[2]), np.uint8)
    newsky[:, :] = 0

    peak = findvline() + 1 # 前面算出来了这个分割位置
    print("peak", peak)
    newsky[peak:, :] = sky[:newsky.shape[0]-peak, :]
    print("newsky", newsky.shape)
    #display(newsky)

    # 水面 云彩 倒影
    mask_sea[:peak, ...] = 0
    mask_sea = kalgorithm.bgr2gray(mask_sea)

    # 不要边缘（前面自己写的边缘修复算法存在些许缺陷）
    mask_sea[..., :5] = 0
    mask_sea[..., mask_sea.shape[1]-5:] = 0

    # 海水搞大一点，倒影更明显一点。
    if not os.path.exists(outfile+"_mask_sea.png"):
        mask_sea = morphologyDilate(mask_sea, 1) # 膨胀
        mask_sea = morphologyDilateLine(mask_sea, 2, linelen=3) # 水平膨胀
        mask_sea = kalgorithm.meanFilter2D(mask_sea, K_size=7) # 滤波
        mask_sea[:peak+1, ...] = 0 # 膨胀后的边界清理
        mask_sea = kalgorithm.meanFilter2D(mask_sea) # 滤波
        kalgorithm.imgSave(outfile+"_mask_sea.png", mask_sea)
        #display(mask_sea)
    mask_sea = kalgorithm.imgRead(outfile+"_mask_sea.png").astype(np.float32) / 255

    print(imgsrc.shape, mask_sea.shape)
    outv = ((newsky * mask_sea*0.35) + # 下面部分，天空倒影
            (imgsrc * mask_sea*0.4) + # 下面部分，原图
            (imgsrc * (1-mask_sea) * 0.8)) # 其他部分
    
    H, W, C = outv.shape
    GSIZE = H
    GaussianMask = gaussianMask(outv, dr=GSIZE/4)
    if xcode:
        hsv = kalgorithm.bgr2hsv(outv)
        print("outv", outv.shape, outv[0, 0])

        for y in range(H):
            for x in range(W):
                hsv[y, x, 0] = xcode#(35*2+hsv[y, x, 0])/3
                hsv[y, x, 2] = hsv[y, x, 2] * GaussianMask[y, x]
        outv = kalgorithm.hsv2bgr(hsv, outv)
        #display(outv)
    else:
        print("outv", outv.shape, outv[0, 0])

        for y in range(H):
            for x in range(W):
                outv[y, x, 2] = outv[y, x, 2] * GaussianMask[y, x]
                outv[y, x, 1] = outv[y, x, 1] * GaussianMask[y, x]
                outv[y, x, 0] = outv[y, x, 0] * GaussianMask[y, x]
        #display(outv)

    # 降低画面曝光度，伽马变换
    if True: # 鱼女剪影
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

    # 渔女剪影效果
    # 背景调暗，渔女调整的更暗。
    outvgril = imgsrc#alg.gammaCorrection(outv, g=0.3)

    mask_fishergirl = 255 - kalgorithm.imgRead(mask_fishergirl)
    mask_fishergirl = kalgorithm.meanFilter(mask_fishergirl)
    mask_fishergirl = mask_fishergirl.astype(np.float) / 255.
    outv = outv * (1-mask_fishergirl) + outvgril*mask_fishergirl
    outv = np.clip(outv, 0, 255)

    # 对最终结果再微调。
    if True:
        pass # 哎，算了，就这样吧。

    #cv2.putText(outv, "{}".format(xcode), (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
    #    1, (0, 255, 255), 1, cv2.LINE_AA)
    if xcode:
        kalgorithm.imgSave(outfile+"_glod.png", outv)
    else:
        kalgorithm.imgSave(outfile, outv)

if __name__ == "__main__":

    mainfixfile()
    maintask(0)
    maintask(35)
