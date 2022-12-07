import numpy as np
import cv2
import math

'''
This file will contain function about the basic operation in this project.
'''


'''
1. read image from input path
    returned an image with gray scale(1 channel)
    In python-opencv, cv2.IMREAD_GRAYSCALE
'''
def readGray(path, color_value = 0):
    return cv2.imread(path, color_value)


'''
2. read image from input path with 
    retured an image with three channe
    In python-opencv, the returned 3 channels are BGR.
'''
def readColor(path, color_value = 1):
    return cv2.imread(path, color_value)

'''
2. transfer an three channels image into LAB format
'''
def cvtLAB(img):
    # return cv2.cvtColor(img.astype(np.float32), cv2.COLOR_BGR2LAB)
    return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

'''
3. transfer the lab color space image into BGR image
'''
def cvtBGR(img):
    # return cv2.cvtColor(img.astype(np.float32), cv2.COLOR_LAB2BGR)
    return cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

'''
4. normolization to [0,1]
'''

def normolization(img):
    return img / 255.0

def renormolization(img):
    image = (np.maximum(img, 0) / img.max()) * 255.0
    return image

# def PSNR(original_img, denoised_img):
#     original_img = np.float32(original_img)
#     denoised_img = np.float32(denoised_img)
#     mse = np.mean((original_img - denoised_img) ** 2 )
#     if mse == 0:
#         return 100
#     PIXEL_MAX = 255.0
#     return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))