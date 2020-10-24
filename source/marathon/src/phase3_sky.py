# encoding=utf8
import os, re, sys
import cv2
import numpy as np
from lib.sky import *
from lib.toymorphology import *
from lib import kalgorithm

repairfile = r"./output_images/phase3/phase3_repaired.png"
repairmaskfile = r"./output_images/phase3/phase3_repaired_mask.png"

skyfile = r"./input_images/phase3/phase3_sky.jpg"

outfile = r"./output_images/phase3/phase3_sky.jpg"

def findAngle(out):
    H, W = out.shape
    lH = H - 1
    rH = H - 1
    for i in range(H):
        ik = H - 1 - i
        if out[ik, 0] and lH == H - 1:
            lH = ik
        if out[ik, W-1] and rH == H - 1:
            rH = ik
    return np.arctan(1.0 * (lH - rH) / W)

def maskfill(imgsrc):
    Ht, Wt, C = imgsrc.shape
    H, W, C = imgsrc.shape
    flag = False
    # 正反插值填充
    for y in range(Ht):
        for x in range(Wt):
            if np.sum(imgsrc[y, x]) == 0 and y-1>=0 and np.sum(imgsrc[y-1, x]):
                imgsrc[y, x] = imgsrc[y-1, x]
                flag = True
            if np.sum(imgsrc[y, x]) == 0 and x-1>=0 and np.sum(imgsrc[y, x-1]):
                imgsrc[y, x] = imgsrc[y, x-1]
                flag = True
    # 正反插值填充
    for iy in range(Ht):
        for ix in range(Wt):
            y = Ht - 1 - iy
            x = Wt - 1 - ix
            if np.sum(imgsrc[y, x]) == 0 and y+1<Ht and np.sum(imgsrc[y+1, x]):
                imgsrc[y, x] = imgsrc[y+1, x]
                flag = True
            if np.sum(imgsrc[y, x]) == 0 and x+1<Wt and np.sum(imgsrc[y, x+1]):
                imgsrc[y, x] = imgsrc[y, x+1]
                flag = True

    # 正反插值填充
    for y in range(Ht):
        for x in range(Wt):
            if np.sum(imgsrc[y, x]) == 0 and y-1>=0 and np.sum(imgsrc[y-1, x]):
                imgsrc[y, x] = imgsrc[y-1, x]
                flag = True
            if np.sum(imgsrc[y, x]) == 0 and x-1>=0 and np.sum(imgsrc[y, x-1]):
                imgsrc[y, x] = imgsrc[y, x-1]
                flag = True
    # 正反插值填充
    for iy in range(Ht):
        for ix in range(Wt):
            y = Ht - 1 - iy
            x = Wt - 1 - ix
            if np.sum(imgsrc[y, x]) == 0 and y+1<Ht and np.sum(imgsrc[y+1, x]):
                imgsrc[y, x] = imgsrc[y+1, x]
                flag = True
            if np.sum(imgsrc[y, x]) == 0 and x+1<Wt and np.sum(imgsrc[y, x+1]):
                imgsrc[y, x] = imgsrc[y, x+1]
                flag = True
    return flag

def calcMask(dstfile):
    imgsrc = kalgorithm.imgRead(dstfile).astype(np.float32)
    gray = kalgorithm.bgr2gray(imgsrc)
    fy, fx = kalgorithm.prewittFilter(gray, K_size=3)
    out = fy.astype(np.float32) + fx.astype(np.float32)
    fy, fx = kalgorithm.sobelFilter(gray, K_size=3)
    out = out + fy.astype(np.float32) + fx.astype(np.float32)
    out = np.clip(out, 0, 255)
    out = kalgorithm.thresholdOtsuBinarization(out)
    return out

def mainfixfile():
    srcfile = "./output_images/phase2/phase2_broken_nn.jpg.png"
    dstfile = "./output_images/phase3/phase3_repair_original.png"
    if not os.path.exists(dstfile):
        img = kalgorithm.imgRead(srcfile)
        H, W, C = img.shape
        img = kalgorithm.nnInterpolateRound(img, int(H / 3), int(W / 3))
        # 一上来就修复图片
        kalgorithm.imgSave(dstfile, img)

        from phase2_broken_repair import mainfix
        mainfix(img, dstfile, 240)

    if not os.path.exists(dstfile+".mask.png"):
        out = calcMask(dstfile)
        kalgorithm.imgSave(dstfile+".mask.png", out)

    # 分离出水平线
    if not os.path.exists(repairmaskfile):
        out = kalgorithm.imgRead(dstfile+".mask.png").astype(np.float32)
        out = kalgorithm.bgr2gray(out)
        out = morphologyEro2(out, 1, linelen=40)
        out = morphologyDil2(out, 1, linelen=40)
        kalgorithm.imgSave(dstfile+".mask.line.png", out)

        # 根据水平线，矫正原图。
        angle = findAngle(out) # 找到偏移角度。
        print(angle)
        imgsrc = kalgorithm.imgRead(dstfile).astype(np.float32)

        imgsrc = kalgorithm.affineRotation(imgsrc, angle)
        # 修复边缘。
        while maskfill(imgsrc):
            pass

        kalgorithm.imgSave(repairfile, imgsrc)
        out = calcMask(repairfile)
        kalgorithm.imgSave(repairmaskfile, out)

def display(out):
    print(out.shape, out[0,0])
    out = out.astype(np.uint8)

    cv2.imshow("result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main_fisher_girl_mask():

    if os.path.exists(outfile+"_fisher_girl_mask.png"):
        return

    imgsrc = kalgorithm.imgRead(repairfile).astype(np.float32)
    sky = kalgorithm.imgRead(skyfile).astype(np.float32)

    # 使用色彩追踪和形态学运算得到图像中感兴趣区域
    # RGB > HSV
    mask = BGR2HSV(imgsrc)

    # color tracking
    mask = get_mask(mask)
    # masking
    out = masking(imgsrc, mask) # 把太黑的一起识别出来，认为是陆地。
    out = kalgorithm.bgr2gray(out)
    mask = kalgorithm.thresholdOtsuBinarization(out).astype(np.float32)/255
    # closing
    mask = Morphology_Closing(mask, time=1) # 更多白区域，移除小黑点。
    # opening
    mask = Erode(mask, Erode_time=1)

    # masking
    out = masking(imgsrc, mask)

    #display(out)
    kalgorithm.imgSave(outfile+"_fisher_girl.png", out) # 把海岛准确识别出来了。
    kalgorithm.imgSave(outfile+"_fisher_girl_mask.png", mask*255)

def findvline():
    outv = kalgorithm.bgr2gray(kalgorithm.imgRead(repairmaskfile))
    outv = kalgorithm.thresholdBinarization(outv)
    outv = morphologyEro2(outv, 1, linelen=40)
    outv = morphologyDil2(outv, 1, linelen=40)
    H, W = outv.shape

    y_histogram = np.sum(outv, axis=1)

    y_min = np.min(y_histogram)
    y_max = np.max(y_histogram)
    for i in range(len(y_histogram)):
        if i > 0 and y_histogram[i] > 1000:
            print(i, y_histogram[i])
            return i
    return 0

def main_ocean_wave():

    if os.path.exists(outfile+"_ocean_wave_mask.png"):
        return

    imgsrc = kalgorithm.imgRead(repairfile).astype(np.float32)
    sky = kalgorithm.imgRead(skyfile).astype(np.float32)

    # 纵向寻找边缘
    outv = kalgorithm.bgr2gray(kalgorithm.imgRead(repairmaskfile))
    outvz = outv

    vline = (findvline())

    fisher_girl_mask = 255-kalgorithm.bgr2gray(kalgorithm.imgRead(outfile+"_fisher_girl_mask.png"))
    #fisher_girl_mask = morphologyDilFull(fisher_girl_mask, 2) # 渔女变得更大。

    # 背景减去 渔女，剩下 海平面。
    outv = outvz - outvz * (fisher_girl_mask/255.0)

    #outv = hilditch(outv.reshape(outv.shape[0], outv.shape[1], 1)).reshape(outv.shape[0], outv.shape[1])
    #display(outv)
    print(vline)
    outv[:vline, ...] = 0
    kalgorithm.imgSave(outfile+"_ocean_wave_mask.png", outv)

    outv[:vline, ...] = 255
    outv[vline:, ...] = 0
    outv = outv.astype(np.float32)
    outv[:vline, ...] = outv[:vline, ...] * (1-(fisher_girl_mask[:vline, ...]/255.0))
    outv = np.clip(outv, 0, 255)
    kalgorithm.imgSave(outfile+"_sky_mask.png", outv)
    return

def main_replace_sky():
    mask_fishergirl = outfile+"_fisher_girl_mask.png"
    mask_sea        = outfile+"_ocean_wave_mask.png"
    mask_sky        = outfile+"_sky_mask.png"

    imgsrc = kalgorithm.imgRead(repairfile).astype(np.float32)
    sky = kalgorithm.imgRead(skyfile).astype(np.float32)
    mask_sky = (kalgorithm.imgRead(mask_sky).astype(np.float32))
    mask_sky = kalgorithm.meanFilter(mask_sky)

    sky = kalgorithm.blInterpolate(sky, 0.33333333334, 0.33333333334)
    print(imgsrc.shape, sky.shape) # (744, 1100, 3) (618, 1100, 3)
    print(mask_sky.shape) # (744, 1100, 3)

    newsky = np.zeros((mask_sky.shape[0], mask_sky.shape[1], sky.shape[2]), np.uint8)
    newsky[:, :] = 0
    newsky[:sky.shape[0], :sky.shape[1]] = sky
    print(newsky.shape)

    mask_sky = mask_sky / 255
    print(newsky.shape, mask_sky.shape, imgsrc.shape)
    finalimage = newsky * mask_sky + imgsrc * (1-mask_sky)

    kalgorithm.imgSave(outfile+"_sky_cloud.png", finalimage)

if __name__ == "__main__":

    mainfixfile()

    # 第一步，计算渔女 的 mask 掩码
    main_fisher_girl_mask()

    # 第二步，计算 海平线。
    main_ocean_wave()

    main_replace_sky()
