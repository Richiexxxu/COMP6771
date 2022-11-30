import numpy as np
import cv2
import BWBilateral as bwb
import MainOperation as mo


#run balck image
img = mo.readGray(path="denoise.jpg",img_value=0)
print(img.shape)
cv2.imshow("original", img)
kernel_size = 7
domain_sigma = 10
range_sigma = 50
filtered_img = np.uint8(bwb.filterimage(img, kernel_size, domain_sigma, range_sigma))

cv2.imshow("filter_result", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # run color image
# img = mo.readColor(path="rubiks_cube.png", color_value=1)
# cv2.imshow("test original", img)
# img = mo.cvtLAB(img=img)
# print(img.shape)
# cv2.imshow("test color",img)
#
#
# kernel_size = 7
# domain_sigma = 10
# range_sigma = 50
# filtered_img = np.uint
#
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


