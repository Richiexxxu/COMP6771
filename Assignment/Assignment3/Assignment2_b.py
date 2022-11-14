import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("house.tif", 0)

def zero_cross_default(input_image, threshold):
    zero_cross = np.zeros_like(input_image, dtype=np.uint8)
    image_height,  image_width = input_image.shape
    for y in range(1, image_height-1):
        for x in range(1, image_width-1):
            if input_image[y][x] == 0:
                if input_image[y][x-1] * input_image[y][x+1] < 0:
                    if np.abs(input_image[y][x-1] - input_image[y][x+1])/2 > threshold:
                        zero_cross[y][x] = 255
                    # continue
                if input_image[y-1][x] * input_image[y+1][x] <0:
                    if np.abs(input_image[y-1][x] - input_image[y+1][x])/2 > threshold:
                        zero_cross[y][x] = 255
                    # continue
                if input_image[y-1][x-1] * input_image[y+1][x+1] <0:
                    if np.abs(input_image[y-1][x-1] - input_image[y+1][x+1])/2 > threshold:
                        zero_cross[y][x] = 255
                    # continue
                if input_image[y-1][x+1] * input_image[y+1][x-1] <0:
                    if np.abs(input_image[y-1][x+1] - input_image[y+1][x-1])/2 > threshold:
                        zero_cross[y][x] = 255
            if input_image[y][x] < 0:
                if (input_image[y][x-1] > 0) or (input_image[y][x+1] > 0) or \
                        (input_image[y-1][x] > 0) or (input_image[y+1][x] > 0) or \
                        (input_image[y-1][x-1] > 0) or (input_image[y+1][x+1] > 0) or \
                        (input_image[y-1][x+1] > 0) or (input_image[y+1][x-1] > 0):
                    if np.abs(input_image[y][x-1] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y][x+1] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y-1][x] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y+1][x] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y-1][x-1] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y+1][x-1] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y-1][x+1] - input_image[y][x]) > threshold or \
                        np.abs(input_image[y+1][x+1] - input_image[y][x]) > threshold:
                        zero_cross[y][x] = 255



    return zero_cross





# log
gaussian = cv.GaussianBlur(img, (21, 21), 3.5)
cv.imshow("test_gaussian", gaussian)
dst_log = cv.Laplacian(gaussian, cv.CV_16S, ksize = 5)
# print(dst)
# print(np.max(dst_log))
# print(np.min(dst_log))
cv_log = zero_cross_default(dst_log, np.max(dst_log) * 0.15)
# cv_log = np.uint8(cv.convertScaleAbs(dst_log))
# print(cv_log[:,200])
dst_can = cv.Canny(gaussian, 100, 200)

cv.imshow("test_log", cv_log)
cv.imshow("test_ann", dst_can)
# cv.waitKey(0)
# cv.destroyAllWindows()

def edgesMarrHildreth(img, sigma):
    """w
            finds the edges using MarrHildreth edge detection method...
            :param im : input image
            :param sigma : sigma is the std-deviation and refers to the spread of gaussian
            :return:
            a binary edge image...
    """
    # size = int(2*(np.ceil(3*sigma))+1)
    #
    # x, y = np.meshgrid(np.arange(-size/2+1, size/2+1),
    #                    np.arange(-size/2+1, size/2+1))
    #
    # normal = 1 / (2.0 * np.pi * sigma**2)
    #
    # kernel = ((x**2 + y**2 - (2.0*sigma**2)) / sigma**4) * \
    #     np.exp(-(x**2+y**2) / (2.0*sigma**2)) / normal  # LoG filter
    #
    # kern_size = kernel.shape[0]
    # log = np.zeros_like(img, dtype=float)
    #
    # # applying filter
    # for i in range(img.shape[0]-(kern_size-1)):
    #     for j in range(img.shape[1]-(kern_size-1)):
    #         window = img[i:i+kern_size, j:j+kern_size] * kernel
    #         log[i, j] = np.sum(window)
    gaussian = cv.GaussianBlur(img, (15,15), 2)
    dst_log = cv.Laplacian(gaussian, cv.CV_16S, ksize = 5)
    # log = dst_log.astype(np.int64, copy=False)
    log = dst_log
    kern_size = 3
    zero_crossing = np.zeros_like(log,dtype=np.uint8)

    threshold = np.max(dst_log) * 0.2
    # computing zero crossing
    for i in range(log.shape[0]-(kern_size-1)):
        for j in range(log.shape[1]-(kern_size-1)):
            if log[i][j] == 0:
            #     print((i,j))
                if (log[i][j-1] < 0 and log[i][j+1] > 0) or \
                        (log[i][j-1] < 0 and log[i][j+1] < 0) or \
                        (log[i-1][j] < 0 and log[i+1][j] > 0) or \
                        (log[i-1][j] > 0 and log[i+1][j] < 0):
                        # (log[i-1][j-1] >0 and log[i+1][j+1] <0) or \
                        # (log[i-1][j-1] <0 and log[i+1][j+1] >0) or \
                        # (log[i-1][j+1] >0 and log[i+1][j-1] <0) or \
                        # (log[i-1][j+1] <0 and log[i+1][j-1] >0):
                    if np.abs(log[i][j-1] - log[i][j+1])/2 > threshold or \
                        np.abs(log[i-1][j] - log[i+1][j] > 0)/2 > threshold:
                        # np.abs(log[i-1][j-1] - log[i+1][j+1])/2 > threshold or \
                        # np.abs(log[i-1][j+1] - log[i+1][j-1])/2 > threshold:
                        zero_crossing[i][j] = 255
            if log[i][j] < 0:
                if (log[i][j-1] > 0) or (log[i][j+1] > 0) or \
                        (log[i-1][j] > 0) or (log[i+1][j] > 0):
                        # (log[i-1][j-1] > 0) or (log[i+1][j+1] > 0) or \
                        # (log[i-1][j+1] > 0) or (log[i+1][j-1] > 0):
                    if np.abs(log[i][j-1] - log[i][j]) > threshold or \
                        np.abs(log[i][j+1] - log[i][j]) > threshold or \
                        np.abs(log[i-1][j] - log[i][j]) > threshold or \
                        np.abs(log[i+1][j] - log[i][j]) > threshold:
                        # np.abs(log[i-1][j-1] - log[i][j]) > threshold or \
                        # np.abs(log[i+1][j-1] - log[i][j]) > threshold or \
                        # np.abs(log[i-1][j+1] - log[i][j]) > threshold or \
                        # np.abs(log[i+1][j+1] - log[i][j]) > threshold:
                        zero_crossing[i][j] = 255

    # # plotting images
    # fig = plt.figure()
    # a = fig.add_subplot(1, 2, 1)
    # imgplot = plt.imshow(log, cmap='gray')
    # a.set_title('Laplacian of Gaussian')
    # a = fig.add_subplot(1, 2, 2)
    # imgplot = plt.imshow(zero_crossing, cmap='gray')
    # string = 'Zero Crossing sigma = '
    # string += (str(sigma))
    # a.set_title(string)
    # plt.show()

    return log, zero_crossing
log, zero_crossing = edgesMarrHildreth(img, sigma=2)
cv.imshow("test", zero_crossing)
cv.waitKey(0)
cv.destroyAllWindows()