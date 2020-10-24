#encoding=utf8
import os, re, sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from lib import kalgorithm

RX_COLOR = (255 * 3 - 30)
RL_COLOR = (0 * 3 + 30)

def cropImage(img):
    h, w, c = img.shape
    l, t = w, h
    r, b = 0, 0
    for y in range(h):
        for x in range(w):
            sum = np.sum(img[y, x])
            if sum >= RX_COLOR or sum <= RL_COLOR: # 不是黑色或者白色
                continue
            if y < t: t = y
            if y > b: b = y
            if x < l: l = x
            if x > r: r = x
    return img[t:b+1, l:r+1]

def rotateImage(img):
    h, w, c = img.shape
    xh, xw = 0, 0
    for y in range(h):
        for x in range(w):
            sum = np.sum(img[y, x])
            if sum >= RX_COLOR or sum <= RL_COLOR: # 不是黑色或者白色
                continue
            if x < 2 and xh == 0:
                xh = y
            if y < 2 and xw == 0:
                xw = x
    print(xh, xw)
    theta = -np.arctan(xw / xh) + np.pi/2
    img = kalgorithm.affineRotation(img, theta)
    return img

# 将彩色负片转为彩色正片
def phase1(inputImgPath: str, outImgPath: str):
    img = kalgorithm.imgRead(inputImgPath)
    img = 255 - img
    kalgorithm.imgSave(outImgPath, img)

# 输入底片不正
def phase1_optional(inputImgPath: str, outImgPath: str):
    img = kalgorithm.imgRead(inputImgPath)
    img = 255 - img
    img = cropImage(img) # 剪裁
    kalgorithm.imgSave(outImgPath+".1.jpg", img)
    img = rotateImage(img) # 旋转
    kalgorithm.imgSave(outImgPath+".2.jpg", img)
    img = cropImage(img) # 再剪裁
    kalgorithm.imgSave(outImgPath, img)

if __name__ == "__main__":
    phase1_input = r"./input_images/phase1/phase1_input.jpg"
    phase1_output = r"./output_images/phase1/phase1_output.jpg"
    phase1(phase1_input, phase1_output)

    phase1_input_optional = r"./input_images/phase1/phase1_input_optional.jpg"
    phase1_output_optional = r"./output_images/phase1/phase1_output_optional.jpg"
    phase1_optional(phase1_input_optional, phase1_output_optional)
