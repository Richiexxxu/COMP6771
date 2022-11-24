import numpy as np
import cv2

'''
This file will contain function about the basic operation in this project.
'''


# read image:
def readimg(path, img_type = 0):
    return cv2.imread(path, img_type)