import numpy as np
import cv2
import MainOperation as mo

img=np.random.randint(1,9,size=25).reshape((5,5))
print(img)
kernel_size= 2
# img = np.zeros((10, 10, 3))
img = cv2.copyMakeBorder(img,kernel_size,kernel_size,kernel_size,kernel_size,cv2.BORDER_REFLECT)

print(img)