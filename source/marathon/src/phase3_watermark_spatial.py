#encoding=utf8
import cv2
import numpy as np

from lib.kcolor import *
from lib.kthreshold import *
from lib.kaffine import *
from lib.kinterpolate import *
from lib import kalgorithm

def encode(srcInputFile, waterMarkFile, dstOutputFile):
    srcimg = kalgorithm.imgRead(srcInputFile)
    watermark = blInterpolate(kalgorithm.imgRead(waterMarkFile), 2, 2)
    print(watermark.shape)

    watermark = bgr2gray(watermark).astype(np.float)
    watermark = 255 - watermark
    watermark = thresholdOtsuBinarization(watermark)

    #kalgorithm.imgShow(watermark)
    #kalgorithm.imgShow(srcimg)

    WH, WW = watermark.shape
    IMGH, IMGW, IMGC = srcimg.shape

    srcimg = srcimg // 4 * 4

    for y in range(WH):
        for x in range(WW):
            #print(srcimg[y, x])
            if watermark[y, x]:
                srcimg[y, x, 0] = srcimg[y, x, 0] | 0x2
                srcimg[y, x, 1] = srcimg[y, x, 1] | 0x2
                srcimg[y, x, 2] = srcimg[y, x, 2] | 0x2

    kalgorithm.imgSave(dstOutputFile, srcimg)
    cv2.imwrite(dstOutputFile, srcimg,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
    kalgorithm.imgShow(srcimg)
    return

def decode(dstOutputFile, recoverWaterMark):

    srcimg = kalgorithm.imgRead(dstOutputFile)

    #srcimg = srcimg % 4 / 3 * 255

    IMGH, IMGW, IMGC = srcimg.shape
    for y in range(IMGH):
        for x in range(IMGW):
            a, b, c = srcimg[y, x, 0], srcimg[y, x, 1], srcimg[y, x, 2]
            if (a%4 in (2,3)) and (b%4 in (2,3)) and (c%4 in (2,3)):
                srcimg[y, x] = 255
            else:
                srcimg[y, x] = 0

    #srcimg = blInterpolate(srcimg, 0.2, 0.2)
    kalgorithm.imgShow(srcimg)
    kalgorithm.imgSave(recoverWaterMark, srcimg)
    return

def main():
    srcInputFile = r"./input_images/phase2/phase2_broken.jpg"
    waterMarkFile = r"./input_images/phase3/phase3_watermark.jpg"
    dstOutputFile = r"./output_images/phase3/phase3_broken_with_wm_spatial.png"
    recoverWaterMark = r"./output_images/phase3/phase3_watermark_recover_spatial.png"

    encode(srcInputFile, waterMarkFile, dstOutputFile)
    decode(dstOutputFile, recoverWaterMark)

if __name__ == "__main__":
    main()
