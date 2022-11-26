import numpy as np
import cv2
import MainOperation as mo

img = cv2.imread("rubiks_cube.png", 1)
img = mo.cvtLAB(img)
# img = np.float32(img/255.0)
reslt_img = cv2.bilateralFilter(img, d=15, sigmaSpace=10, sigmaColor=200)
# reslt_img_a = cv2.bilateralFilter(img, d=25, sigmaSpace=10, sigmaColor=900)
# cv2.imshow("original", img)
reslt_img = mo.cvtBGR(reslt_img)
cv2.imshow("result", reslt_img)
# cv2.imshow("resut_a", reslt_img_a)



cv2.waitKey(0)
cv2.destroyAllWindows()