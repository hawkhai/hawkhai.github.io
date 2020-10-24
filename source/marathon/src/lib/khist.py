#encoding=utf8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 直方图均衡化（Histogram Equalization）
# 直方图均衡化是使直方图变得平坦的操作。
def histEqualization(img, z_max=255):
    H, W, C = img.shape
    S = H * W * C * 1.

    out = img.copy()

    sum_h = 0.

    for i in range(1, 255):
        ind = np.where(img == i)
        sum_h += len(img[ind])
        z_prime = z_max / S * sum_h
        out[ind] = z_prime

    out = out.astype(np.uint8)

    return out

# 伽玛校正（Gamma Correction）
# gamma correction
def gammaCorrection(img, c=1, g=2.2):
    out = img.copy().astype(np.float)
    out /= 255.
    out = (1/c * out) ** (1/g)

    out *= 255
    out = out.astype(np.uint8)

    return out

# histogram normalization
# 直方图归一化（Histogram Normalization）
def histNormalization(img, a=0, b=255):
    # get max and min
    c = img.min()
    d = img.max()

    out = img.copy()

    # normalization
    out = (b-a) / (d - c) * (out - c) + a
    out[out < a] = a
    out[out > b] = b
    out = out.astype(np.uint8)

    return out

# 让直方图的平均值 m0=128，标准差 s0=52 吧！
# 这里并不是变更直方图的动态范围，而是让直方图变得平坦。
def histManipulation(img, m0=128, s0=52):
    m = np.mean(img)
    s = np.std(img)

    out = img.copy()

    # normalize
    out = s0 / s * (out - m) + m0
    out[out < 0] = 0
    out[out > 255] = 255
    out = out.astype(np.uint8)
    return out
