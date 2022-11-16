import numpy as np
import cv2 as cv

def readImg(path):
    return cv.imread(path, 0)

def gaussianBlur(img = None, kernal_size = None, sigma = None):
    return cv.GaussianBlur(img, (kernal_size, kernal_size), sigma)

def laplacian(img = None, kernal_size = None):
    return cv.Laplacian(img, cv.CV_16S, ksize = kernal_size)

def zero_cross(input_image = None, threshold = None):
    zero_cross = np.zeros_like(input_image, dtype=np.uint8)
    image_height, image_width = input_image.shape
    for y in range(1, image_height - 1):
        for x in range(1, image_width - 1):
            if input_image[y][x] == 0:
                if input_image[y][x - 1] * input_image[y][x + 1] < 0:
                    if np.abs(input_image[y][x - 1] - input_image[y][x + 1]) / 2 > threshold:
                        zero_cross[y][x] = 255

                if input_image[y - 1][x] * input_image[y + 1][x] < 0:
                    if np.abs(input_image[y - 1][x] - input_image[y + 1][x]) / 2 > threshold:
                        zero_cross[y][x] = 255

                if input_image[y - 1][x - 1] * input_image[y + 1][x + 1] < 0:
                    if np.abs(input_image[y - 1][x - 1] - input_image[y + 1][x + 1]) / 2 > threshold:
                        zero_cross[y][x] = 255

                if input_image[y - 1][x + 1] * input_image[y + 1][x - 1] < 0:
                    if np.abs(input_image[y - 1][x + 1] - input_image[y + 1][x - 1]) / 2 > threshold:
                        zero_cross[y][x] = 255
            if input_image[y][x] < 0:
                if (input_image[y][x - 1] > 0) or (input_image[y][x + 1] > 0) or \
                        (input_image[y - 1][x] > 0) or (input_image[y + 1][x] > 0) or \
                        (input_image[y - 1][x - 1] > 0) or (input_image[y + 1][x + 1] > 0) or \
                        (input_image[y - 1][x + 1] > 0) or (input_image[y + 1][x - 1] > 0):
                    if np.abs(input_image[y][x - 1] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y][x + 1] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y - 1][x] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y + 1][x] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y - 1][x - 1] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y + 1][x - 1] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y - 1][x + 1] - input_image[y][x]) > threshold or \
                            np.abs(input_image[y + 1][x + 1] - input_image[y][x]) > threshold:
                        zero_cross[y][x] = 255
    return zero_cross

def round_up_to_odd(f):
    return int(np.ceil(f) // 2 * 2 + 1)


def marrHildreth():
    # read image
    img = readImg("house.tif")
    # Gaussian blur
    gaussian_sigma = 3.7
    gaussian_kernal_size = round_up_to_odd(gaussian_sigma * 6)
    print(gaussian_kernal_size)
    img_gaussian = gaussianBlur(img=img,kernal_size=gaussian_kernal_size, sigma=gaussian_sigma)
    cv.imshow("marr gaussian", img_gaussian)
    # laplacian
    log_size= 9
    img_log = laplacian(img = img_gaussian, kernal_size= log_size)
    # zero crossing
    threshold = np.max(img_log) * 0.25
    img_zerocross = zero_cross(input_image=img_log, threshold=threshold)

    cv.imshow("marrHildreth", img_zerocross)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # cv.imwrite("marrHildreth.png", img_zerocross)


def canny():
    # read image
    img = readImg("house.tif")

    # Gauss blur
    gaussian_sigma = 1.5
    gaussian_kernal_size = round_up_to_odd(gaussian_sigma * 6)
    print(gaussian_kernal_size)

    img_gaussian = gaussianBlur(img=img,kernal_size=gaussian_kernal_size, sigma=gaussian_sigma)
    cv.imshow("canny gaussian", img_gaussian)
    # Canny
    img_min = np.min(img_gaussian)
    img_max = np.max(img_gaussian)
    print((img_min, img_max))
    # max_threshold = img_min + img_max * 0.6
    # min_threshold = img_min + img_max * 0.2
    max_threshold = img_max * 0.6
    min_threshold = img_max * 0.2
    print((min_threshold, max_threshold))
    img_can = cv.Canny(img_gaussian, min_threshold, max_threshold)

    cv.imshow("canny", img_can)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # cv.imwrite("Canny.png", img_can)

canny()

# marrHildreth()