import numpy as np
import cv2 as cv


src = np.array([[1, 2, 2],
                    [6, 7, 8],
                    [1, 2, 3]], dtype='float32')

kernel1 = np.array([[1, 2,3],
                    [1,2,3],
                    [1,2,3]], dtype='float32')/9

result = cv.filter2D(src, -1, kernel = kernel1)
kernel2 = np.array([[3, 2,1],
                    [3,2,1],
                    [3,2,1]], dtype='float32')/9
print(np.sum(src*kernel1))
print(np.sum(src*kernel2))
print('b:\n{}'.format(src))
print('a:\n{}'.format(result))