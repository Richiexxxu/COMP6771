import numpy as np
import cv2
import MainOperation as mo

kernel_size = 5
# img = mo.readColor(path="rubiks_cube.png", color_value=1)[:10, :10, :]
img = np.zeros((5, 5, 3))
img = np.uint8(img)
print((np.max(img), np.min(img)))
# img = np.array(img)
# print(img.shape)
# oimg = np.uint8(paddingImg(img=img, kernel_size=kernel_size))
# print(oimg.shape)
img_new = mo.cvtLAB(img=img)
# img_new = np.array(img_new)
print(img_new.shape)
print((np.max(img_new), np.min(img_new)))


print((img == img_new).all())

