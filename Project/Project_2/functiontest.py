import numpy as np
import cv2


img = cv2.imread("rubiks_cube.png", 1)
reslt_img = cv2.bilateralFilter(img, d=15, sigmaSpace=10, sigmaColor=100)

cv2.imshow("original", img)
cv2.imshow("result", reslt_img)
cv2.waitKey(0)
cv2.destroyAllWindows()