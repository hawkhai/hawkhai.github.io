#encoding=utf8
import os, re, sys
import cv2
import numpy as np
from lib.sky import *
from lib.kmorphology import *
from lib import kalgorithm
from lib import pyheal

repairfile = r"./output_images/phase3/phase3_repair.png"
repairmaskfile = r"./output_images/phase3/phase3_repair_mask.png"

skyfile = r"./input_images/phase3/phase3_sky.jpg"

outfile = r"./output_images/phase3/phase3_sky.jpg"

def findAngle(out): # 图片倾斜角度
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

# 简易边缘修复算法
def maskfill(imgsrc):
    H, W, C = imgsrc.shape
    for y in range(H):
        for x in range(W):
            if np.sum(imgsrc[y, x]): continue
            point = (y, x)
            maskfillSearch(imgsrc, point, 0)

def maskfillSearch(imgsrc, point, depth):
    if depth >= 30: return
    y, x = point
    H, W, C = imgsrc.shape
    if y < 0 or y >= H: return
    if x < 0 or x >= W: return

    # 已经有值了。
    if np.sum(imgsrc[y, x]): return

    if y < H / 2: # 尝试下面填充
        if np.sum(imgsrc[y+1, x]):
            imgsrc[y, x] = imgsrc[y+1, x]
        maskfillSearch(imgsrc, (y, x-1), depth+1) # 遍历左边
        maskfillSearch(imgsrc, (y, x+1), depth+1) # 遍历右边
    else: # 尝试用上面填充
        if np.sum(imgsrc[y-1, x]):
            imgsrc[y, x] = imgsrc[y-1, x]
        maskfillSearch(imgsrc, (y, x-1), depth+1) # 遍历左边
        maskfillSearch(imgsrc, (y, x+1), depth+1) # 遍历右边
    if x < W / 2: # 尝试用右边填充
        if np.sum(imgsrc[y, x+1]):
            imgsrc[y, x] = imgsrc[y, x+1]
        maskfillSearch(imgsrc, (y-1, x), depth+1) # 遍历上面
        maskfillSearch(imgsrc, (y+1, x), depth+1) # 遍历下面
    else: # 尝试用左边填充
        if np.sum(imgsrc[y, x-1]):
            imgsrc[y, x] = imgsrc[y, x-1]
        maskfillSearch(imgsrc, (y-1, x), depth+1) # 遍历上面
        maskfillSearch(imgsrc, (y+1, x), depth+1) # 遍历下面

# 两个算子各有特点，加起来，效果更佳。
def calculateMask(imgsrc):
    gray = kalgorithm.bgr2gray(imgsrc)
    fy, fx = kalgorithm.prewittFilter(gray, K_size=3)
    out1 = fy.astype(np.float32) + fx.astype(np.float32)
    fy, fx = kalgorithm.sobelFilter(gray, K_size=3)
    out2 = fy.astype(np.float32) + fx.astype(np.float32)
    out = out1 + out2
    out = np.clip(out, 0, 255)
    out = kalgorithm.thresholdOtsuBinarization(out)
    return out

def mainfixfile():
    srcfile = "./output_images/phase2/phase2_broken_nn.jpg.png"
    dstfile = "./output_images/phase3/phase3_repair_original.png"
    imgsrc = None
    if not os.path.exists(dstfile):
        img = kalgorithm.imgRead(srcfile)
        H, W, C = img.shape
        img = kalgorithm.nnInterpolateRound(img, int(H / 3), int(W / 3))

        # 一上来就修复图片
        # kalgorithm.imgSave(dstfile, img)
        from phase2_broken_repair import mainfix
        imgsrc = mainfix(img, dstfile, 240, onlyeasy=True)
    else:
        imgsrc = kalgorithm.imgRead(dstfile).astype(np.float32)

    if not os.path.exists(dstfile+".mask.png"):
        out = calculateMask(imgsrc)
        kalgorithm.imgSave(dstfile+".mask.png", out)

    # 分离出水平线
    if not os.path.exists(repairmaskfile):
        out = kalgorithm.imgRead(dstfile+".mask.png").astype(np.float32)
        out = kalgorithm.bgr2gray(out)
        out = morphologyErodeLine(out, 1, linelen=40)
        out = morphologyDilateLine(out, 1, linelen=40)
        kalgorithm.imgSave(dstfile+".mask.line.png", out)

        # 根据水平线，矫正原图。
        angle = findAngle(out) # 找到偏移角度。
        print("angle", angle)
        imgsrc = kalgorithm.imgRead(dstfile).astype(np.float32)

        imgsrc = kalgorithm.affineRotation(imgsrc, angle)
        # 修复边缘。
        while maskfill(imgsrc):
            pass

        kalgorithm.imgSave(repairfile, imgsrc)
        out = calculateMask(imgsrc)
        kalgorithm.imgSave(repairmaskfile, out)
        ## 计算海平面的那条线。准确分离。
        out = morphologyErodeLine(out, 1, linelen=40)
        out = morphologyDilateLine(out, 3, linelen=80)
        kalgorithm.imgSave(repairmaskfile+".mask.line.png", out)

def display(out, title="result"):
    print(out.shape, out[0, 0])
    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)

    cv2.imshow(title, out)
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
    out = masking(imgsrc, mask) # 把太黑的一起识别出来，认为是陆地。主要识别小岛。
    out = kalgorithm.bgr2gray(out)
    mask = kalgorithm.thresholdOtsuBinarization(out).astype(np.float32)/255

    # closing，移除部分毛刺
    mask = Morphology_Closing(mask, time=1) # 更多白区域，移除小黑点。

    # opening，域女再变肥一点。
    mask = Erode(mask, erodeTime=1)

    # masking
    out = masking(imgsrc, mask)

    #display(out)
    kalgorithm.imgSave(outfile+"_fisher_girl.png", out) # 把海岛准确识别出来了。
    kalgorithm.imgSave(outfile+"_fisher_girl_mask.png", mask*255)

def findvline():
    outv = kalgorithm.bgr2gray(kalgorithm.imgRead(repairmaskfile+".mask.line.png"))
    outv = kalgorithm.thresholdBinarization(outv)

    H, W = outv.shape

    yhistogram = np.sum(outv, axis=1)

    ymin = np.min(yhistogram)
    ymax = np.max(yhistogram)
    result = []
    for i in range(len(yhistogram)):
        if i > 5 and i < H-5 and yhistogram[i] > 1000:
            print(i, yhistogram[i])
            result.append(i)
    print("findvline", np.mean(result))
    return int(np.mean(result))

def main_ocean_wave():

    if os.path.exists(outfile+"_ocean_wave_mask.png"):
        return

    imgsrc = kalgorithm.imgRead(repairfile).astype(np.float32)
    sky = kalgorithm.imgRead(skyfile).astype(np.float32)

    masksrc = kalgorithm.bgr2gray(kalgorithm.imgRead(repairmaskfile))

    vline = findvline()

    fisher_girl_mask = 255-kalgorithm.bgr2gray(kalgorithm.imgRead(outfile+"_fisher_girl_mask.png"))

    # 背景减去 渔女，剩下 海平面。
    outv = masksrc - masksrc * (fisher_girl_mask/255.0)

    outv[:vline, ...] = 0
    kalgorithm.imgSave(outfile+"_ocean_wave_mask.png", outv)

    outv[:vline, ...] = 255
    outv[vline:, ...] = 0
    outv = outv.astype(np.float32)
    outv[:vline, ...] = outv[:vline, ...] * (1-(fisher_girl_mask[:vline, ...]/255.0))
    outv = np.clip(outv, 0, 255)
    kalgorithm.imgSave(outfile+"_sky_mask.png", outv)

def main_replace_sky():
    mask_fishergirl = outfile+"_fisher_girl_mask.png"
    mask_sea        = outfile+"_ocean_wave_mask.png"
    mask_sky        = outfile+"_sky_mask.png"

    imgsrc = kalgorithm.imgRead(repairfile).astype(np.float32)
    sky = kalgorithm.imgRead(skyfile).astype(np.float32)
    mask_sky = kalgorithm.imgRead(mask_sky).astype(np.float32)
    mask_sky = kalgorithm.meanFilter(mask_sky) # 均值滤波，接头处就不生硬了。

    sky = kalgorithm.blInterpolate(sky, 0.33333333334, 0.33333333334)
    print("imgsrc", imgsrc.shape, "sky", sky.shape) # (744, 1100, 3) (618, 1100, 3)
    print("mask_sky", mask_sky.shape) # (744, 1100, 3)

    newsky = np.zeros((mask_sky.shape[0], mask_sky.shape[1], sky.shape[2]), np.uint8)
    newsky[:, :] = 0
    newsky[:sky.shape[0], :sky.shape[1]] = sky
    print("newsky", newsky.shape) # 搞成一样大，才可以做乘法，合成图片。

    mask_sky = mask_sky / 255
    print(newsky.shape, mask_sky.shape, imgsrc.shape)
    finalimage = newsky * mask_sky + imgsrc * (1-mask_sky)

    kalgorithm.imgSave(outfile+"_sky_cloud.png", finalimage)

if __name__ == "__main__":

    mainfixfile()

    # 第一步，计算渔女 的 mask 掩码
    main_fisher_girl_mask()

    # 第二步，分离海水、鱼女、天空模板。
    main_ocean_wave()

    # 第三步，合成替换天空。
    main_replace_sky()
