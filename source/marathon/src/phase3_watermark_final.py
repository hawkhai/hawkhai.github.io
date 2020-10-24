import random

import cv2
import numpy as np

from lib import kalgorithm
from lib import watermark
from lib.kinterpolate import blInterpolate

#
# 任务:去水印
# 频域

if __name__ == "__main__":
    srcInputFile=r"./output_images/phase2/phase2_broken_bl.jpg"
    waterMarkFile=r"./input_images/phase3/phase3_watermark.jpg"
    waterMarkFile2=r"./input_images/phase3/phase3_watermark_64_64.jpg"
    dstOutputFile=r"./output_images/phase3/phase3_broken2_bl_with_wm.jpg"
    recoverWaterMark=r"./output_images/phase3/phase3_watermark_recover.jpg"

    #base 常量
    fixed_wm_shape=(64,64)
    random_seed_wm,random_seed_dct,mod,mod2=4399,2333,36,20

    wm=cv2.imread(waterMarkFile)
    H, W, C = wm.shape
    ax = 64.0 / H
    ay = 64.0 / W
    wm=blInterpolate(wm,ay,ax)
    cv2.imwrite(waterMarkFile2,wm)

    bwm1 = watermark.Watermark(random_seed_wm,random_seed_dct,mod,mod2)
    bwm1.read_ori_img(srcInputFile)
    bwm1.read_wm(waterMarkFile2)
    #写入水印
    bwm1.embed(dstOutputFile)

    #解出水印
    bwm1 = watermark.Watermark(random_seed_wm,random_seed_dct,mod,mod2,wm_shape=fixed_wm_shape)
    bwm1.extract(dstOutputFile,recoverWaterMark)
