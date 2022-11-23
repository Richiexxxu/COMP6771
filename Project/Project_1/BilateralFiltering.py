import numpy as np
import cv2
import math
import matplotlib.pyplot as plt


def readimg(path, img_type = 0):
    return cv2.imread(path, img_type)


# define the domain filter
def domainFilter(kernel_size, sigma = 1):

    kernel = np.zeros((kernel_size, kernel_size))
    center_point = np.array([kernel_size/2, kernel_size/2])

    for i in range(kernel_size):
        for j in range(kernel_size):
            xi = np.array([i, j])
            distance = np.linalg.norm(xi - center_point)
            kernel[i, j] = np.exp(-1/2 * (distance / sigma) ** 2)
    # kernel = kernel / np.sum(kernel)
    return kernel


# define the range filter:
def rangefilter(img_pitch, x_intensity, kernel_size, sigma = 1):
    kernel = np.zeros((kernel_size, kernel_size))
    img_pitch = np.float64(img_pitch)
    # intensity_difference = img_pitch - img_pitch[kernel_size//2, kernel_size//1]
    # kernel = np.exp(-1/2 * (()/sigma) ^2)
    # for i in range(kernel_size):
    #     for j in range(kernel_size):
    #         intensity_difference = np.abs(img_pitch[i][j] - x_intensity)
    #         kernel[i][j] = np.exp(-1/2* (intensity_difference/sigma) ** 2)

    intensity_difference =

    # kernel = kernel/np.sum(kernel)
    return kernel

def paddingImg(img, kernel_size):
    img_height, img_width = img.shape
    padding_size = (kernel_size - 1)/2
    # padding_short = np.zeros((padding_size, img_width))
    # padding_long = np.zeros((img_height + (kernel_size - 1), padding_size))

    # padding to image:
    # 1. create zeros image:

    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img
    return padded_img

def filterimage(img, kernel_size, domain_sigma, range_sigma):
    '''
    For filtering an image
    1. input an image with img_height, and image_width
    2. padding image
    3. filter image
        3.1 calculate domain filter
        3.2 calculate range filter
        3.3 calculate filter pitch result
    4. return
    '''

    img_height, img_width = img.shape
    img_bilateral = np.zeros((img_height, img_width))
    padded_img = paddingImg(img=img,kernel_size = kernel_size)
    padded_size = int((kernel_size - 1) / 2)

    # calculate the domain flter:
    domain_kernel = domainFilter(kernel_size=kernel_size, sigma=domain_sigma)


    for y in range(img_height):
        for x in range(img_width):

            # if (y % 10 == 0) and (x % 10 == 0):
            #     print(y, x)
            # img_pitch = padded_img[0:5, 0:5]

            '''
            for point (y, x) in padded_img, center_y = y + padded_size, center_x = x + padded_size
            So, the padded from center_y - kernel_size --> center_y + kernel_size + 1
            '''
            center_y = y + padded_size
            center_x = x + padded_size
            # print((center_y, center_x))
            # print((center_y - padded_size, center_y + padded_size +1, center_x - padded_size,  center_x + padded_size +1))
            img_pitch = padded_img[center_y - padded_size : center_y + padded_size +1,
                                   center_x - padded_size : center_x + padded_size +1]

            # calculate domain kernel
            # domain_kernel = domainFilter(kernel_size=kernel_size, sigma=domain_sigma)

            # calculate range kernel
            range_kernel = rangefilter(img_pitch= img_pitch, x_intensity= img[y,x],kernel_size=kernel_size, sigma=range_sigma)

            # calculate final kernel
            final_kernel = domain_kernel * range_kernel
            final_kernel = final_kernel / np.sum(final_kernel)

            img_bilateral[y,x] = np.sum(img_pitch * final_kernel)
    return img_bilateral




# img = np.ones((9,9))
# print(img[1,1])


img = readimg(path="img_cat.png",img_type=0)
print(img.shape)
cv2.imshow("original", img)
kernel_size = 25
# pi = paddingImg(img, kernel_size=kernel_size)
# print(pi)
# print(pi[3,3])
domain_sigma = 10
range_sigma = 100
filtered_img = np.uint8(filterimage(img, kernel_size, domain_sigma, range_sigma))

cv2.imshow("filter_result", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

