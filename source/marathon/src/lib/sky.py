import cv2
import numpy as np
import matplotlib.pyplot as plt

#使用色彩追踪和形态学运算得到图像中感兴趣区域

# BGR -> HSV
def BGR2HSV(_img):
    img = _img.copy() / 255.

    hsv = np.zeros_like(img, dtype=np.float32)

    # get max and min
    max_v = np.max(img, axis=2).copy()
    min_v = np.min(img, axis=2).copy()
    min_arg = np.argmin(img, axis=2)

    # H
    hsv[..., 0][np.where(max_v == min_v)]= 0
    ## if min == B
    ind = np.where(min_arg == 0)
    hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
    ## if min == R
    ind = np.where(min_arg == 2)
    hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
    ## if min == G
    ind = np.where(min_arg == 1)
    hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300

    # S
    hsv[..., 1] = max_v.copy() - min_v.copy()

    # V
    hsv[..., 2] = max_v.copy()

    return hsv

def plt_mask(data):
    data = [i for i in data]
    unique_data = np.unique(data)

    resdata = []
    for ii in unique_data:
        resdata.append(data.count(ii))

    fig = plt.figure()
    plt.plot(unique_data, resdata)
    plt.show()

# make mask
def get_mask(hsv):
    mask = np.zeros_like(hsv[..., 0])

    #temp = []
    #H, W, C = hsv.shape
    #for y in range(H):
    #    for x in range(W):
    #        if np.nan == hsv[y, x, 0]: continue
    #        try:
    #            temp.append(int(hsv[y, x, 0] / 10))
    #        except:
    #            print(hsv[y, x, 0])
    #plt_mask(temp)

    #mask[np.where((hsv > 180) & (hsv[0] < 260))] = 255
    mask[np.logical_and((hsv[..., 0] > 180), (hsv[..., 0] < 260))] = 1
    return mask

# masking
def masking(img, mask):
    out = img.copy()
    # mask [h, w] -> [h, w, channel]
    mask = np.tile(mask, [3, 1, 1]).transpose([1, 2, 0])
    out *= mask

    return out

# Erosion
def Erode(img, erodeTime=1):
    H, W = img.shape
    out = img.copy()

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each erode
    for i in range(erodeTime):
        tmp = np.pad(out, (1, 1), 'edge')
        # erode
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y - 1 : y + 2 , x - 1 : x + 2]) < 1 * 4:
                    out[y-1 , x-1] = 0

    return out

# Dilation
def Dilate(img, dilateTime=1):
    H, W = img.shape

    # kernel
    MF = np.array(((0, 1, 0),
                   (1, 0, 1),
                   (0, 1, 0)), dtype=np.int)

    # each dilate time
    out = img.copy()
    for i in range(dilateTime):
        tmp = np.pad(out, (1, 1), 'edge')
        for y in range(1, H+1):
            for x in range(1, W+1):
                if np.sum(MF * tmp[y - 1 : y + 2, x - 1 : x + 2]) >= 1:
                    out[y-1 , x-1] = 1

    return out

# Opening morphology
def Morphology_Opening(img, time=1):
    out = Erode(img, erodeTime=time)
    out = Dilate(out, dilateTime=time)
    return out

# Closing morphology
def Morphology_Closing(img, time=1):
    out = Dilate(img, dilateTime=time)
    out = Erode(out, erodeTime=time)
    return out
