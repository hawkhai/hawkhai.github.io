#encoding=utf8
import cv2
import numpy as np
import scipy.misc
import scipy.signal

# 定义函数，显示滤波器模板
def showTemplate(template):
    temp = np.uint8(template*255)
    cv2.imshow('Template', temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

# 定义函数，显示滤波函数
def showFunction(template):
    import matplotlib.pyplot as plt
    row, col = template.shape
    row = np.uint16(row/2)
    col = np.uint16(col/2)
    y = template[row, col:]
    x = np.arange(len(y))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.axis([0, len(x), -0.2, 1.2])
    plt.show()
    return

def ftPrint2d(src):
    print("***" * 10)
    r, c = src.shape
    for i in np.arange(r):
        for j in np.arange(c):
            print("%.2f" % src[i, j], end=" ")
        print()

# 定义函数，高斯高/低通滤波模板
def ftMaskGaussian(src, drsigma):
    template = np.zeros(src.shape, dtype=np.float32) # 构建滤波器
    r, c = src.shape
    for i in np.arange(r):
        for j in np.arange(c):
            distance = np.sqrt((i - r/2)**2 + (j - c/2)**2)
            template[i, j] = np.e ** (-1 * (distance**2 / (2 * drsigma ** 2))) # Gaussian 滤波函数

            value = (i - (r-1)/2)**2 + (j - (c-1)/2)**2
            value = -value/2/drsigma**2
            template[i, j] = 1 - np.exp(value)

    return template

if __name__ == "__main__":
    GSIZE = 100
    G = np.arange(GSIZE*GSIZE).astype(np.float32).reshape((GSIZE, GSIZE, 1))
    src = np.arange(GSIZE*GSIZE).astype(np.float32).reshape((GSIZE, GSIZE))
    maska = ftMaskGaussian(src, drsigma=10)
    maskb = ftMaskGaussian(src, drsigma=20)
    showFunction(maska)
    showTemplate(maska)
    showFunction(maskb)
    showTemplate(maskb)

def gaussianHighFrequencyFilter(im, sigma = 1., maxvalue = 1.):
    imarr = np.array(im)
    height, width = imarr.shape

    fft = np.fft.fft2(imarr)
    fft = np.fft.fftshift(fft)

    maska = np.zeros((height, width), dtype = "float")

    for i in range(height):
        for j in range(width):
            value = (i - (height-1)/2)**2 + (j - (width-1)/2)**2
            value = -value/2/sigma**2
            value = 1 - np.exp(value)
            value = value * 0.5 + 0.5
            fft[i, j] *= value
            maska[i, j] = value

    showFunction(maska)
    showTemplate(maska)

    fft = np.fft.ifftshift(fft)
    ifft = np.fft.ifft2(fft)

    ifft = np.real(ifft)
    max = np.max(ifft)
    min = np.min(ifft)

    res = np.zeros((height, width), dtype = "float")

    for i in range(height):
        for j in range(width):
            res[i, j] = maxvalue * (ifft[i, j] - min)/(max - min)

    return res

def gaussianHighFrequencyFilterImage(img, sigma = 50):
    from .kcolor import bgr2hsv, hsv2bgr
    imgsrc = img.copy()
    image = bgr2hsv(img)

    print(np.min(image[..., 2]), np.max(image[..., 2]))
    image[..., 2] = gaussianHighFrequencyFilter(image[..., 2], sigma, maxvalue=1.)

    newimg = hsv2bgr(image, imgsrc)
    return newimg

def sharpenImage(r):
    # 滤波掩模，空间滤波-锐化滤波
    window = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    # 像素值如果大于 255 则取 255, 小于 0 则取 0
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = min(max(0, s[i][j]), 255)
    s = s.astype(np.uint8)
    return s

def sharpenImage3d(r):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = sharpenImage(rr)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s

# 高斯滤波（Gaussian Filter）
# 高斯滤波器是一种可以使图像平滑的滤波器，用于去除噪声。
def gaussianFilter(img, ksize=3, sigma=1.3):
    H, W, C = img.shape
    # Zero padding
    pad = ksize // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

    # prepare Kernel
    K = np.zeros((ksize, ksize), dtype=np.float)
    for x in range(-pad, -pad + ksize):
        for y in range(-pad, -pad + ksize):
            K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    K /= (2 * np.pi * sigma * sigma)
    K /= K.sum()

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + ksize, x: x + ksize, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)
    print("GaussianFilter Kernel\r\n", K, np.sum(K))
    return out

# 中值滤波（Median Filter）
# 中值滤波器是一种可以使图像平滑的滤波器。
def medianFilter(img, ksize=3):
    H, W, C = img.shape
    # Zero padding
    pad = ksize // 2
    out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
    out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad+y, pad+x, c] = np.median(tmp[y:y+ksize, x:x+ksize, c])

    out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

    return out

# 均值滤波器使用网格内像素的平均值。
def meanFilter(img, ksize=3):
    H, W, C = img.shape

    # zero padding
    pad = ksize // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.mean(tmp[y: y + ksize, x: x + ksize, c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

def meanFilter2D(img, K_size=3):
    H, W = img.shape
    C = 1
    return meanFilter(img.reshape(H, W, C), K_size).reshape(H, W)

def gaussianFilter2D(img, K_size=3, sigma=1.3):
    H, W = img.shape
    C = 1
    return gaussianFilter(img.reshape(H, W, C), K_size, sigma).reshape(H, W)

# sobel filter
# Sobel 滤波器可以提取特定方向（纵向或横向）的边缘。
def sobelFilter(img, K_size=3):
    imgsrc = img
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = imgsrc.copy().astype(np.float)
    tmp = out.copy()

    out_v = out.copy()
    out_h = out.copy()

    ## Sobel vertical
    Kv = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]
    ## Sobel horizontal
    Kh = [[1., 0., -1.],[2., 0., -2.],[1., 0., -1.]]

    # filtering
    for y in range(H):
        for x in range(W):
            out_v[pad + y, pad + x] = np.sum(Kv * (tmp[y: y + K_size, x: x + K_size]))
            out_h[pad + y, pad + x] = np.sum(Kh * (tmp[y: y + K_size, x: x + K_size]))

    out_v = np.clip(out_v, 0, 255)
    out_h = np.clip(out_h, 0, 255)

    out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
    out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out_v, out_h

# prewitt filter
# Prewitt 滤波器是用于边缘检测的一种滤波器。
def prewittFilter(img, K_size=3):
    imgsrc = img
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # Zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = imgsrc.copy().astype(np.float)
    tmp = out.copy()

    out_v = out.copy()
    out_h = out.copy()

    ## prewitt vertical kernel
    Kv = [[-1., -1., -1.],[0., 0., 0.], [1., 1., 1.]]
    ## prewitt horizontal kernel
    Kh = [[-1., 0., 1.],[-1., 0., 1.],[-1., 0., 1.]]

    # filtering
    for y in range(H):
        for x in range(W):
            out_v[pad + y, pad + x] = np.sum(Kv * (tmp[y: y + K_size, x: x + K_size]))
            out_h[pad + y, pad + x] = np.sum(Kh * (tmp[y: y + K_size, x: x + K_size]))

    out_v = np.clip(out_v, 0, 255)
    out_h = np.clip(out_h, 0, 255)

    out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
    out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out_v, out_h
