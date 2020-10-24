import numpy as np

def RGB2BGR(img):
    r = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    b = img[:, :, 2].copy()

    # RGB > BGR
    img[:, :, 0] = b
    img[:, :, 1] = g
    img[:, :, 2] = r

    return img

def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # BGR > RGB
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img

def BGR2YUV(bgr):
    rgb = BGR2RGB(bgr)
    return RGB2YUV(rgb)

#input is a RGB numpy array with shape (height,width,3), can be uint,int, float or double, values expected in the range 0..255
#output is a double YUV numpy array with shape (height,width,3), values in the range 0..255
def RGB2YUV( rgb ):
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                 [0.58700, -0.33126, -0.41869],
                 [ 0.11400, 0.50000, -0.08131]])

    yuv = np.dot(rgb, m)
    yuv[:,:,1:] += 128.0
    return yuv

#input is an YUV numpy array with shape (height,width,3) can be uint,int, float or double, values expected in the range 0..255
#output is a double RGB numpy array with shape (height,width,3), values in the range 0..255
def YUV2RGB( yuv ):

    m = np.array([[ 1.0, 1.0, 1.0],
                 [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                 [ 1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]])

    rgb = np.dot(yuv, m)
    rgb[:,:,0] -= 179.45477266423404
    rgb[:,:,1] += 135.45870971679688
    rgb[:,:,2] -= 226.8183044444304
    return rgb

def YUV2BGR(yuv):
    rgb = YUV2RGB(yuv)
    bgr = RGB2BGR(rgb)
    return bgr
