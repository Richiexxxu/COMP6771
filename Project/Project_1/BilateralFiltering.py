import numpy as np
import cv2
import math



def readimg(path, img_type = 0):
    return cv2.imread("path", img_type)


# define the domain filter
def domainFilter(kernel_size, sigma = 1):

    kernel = np.zeros((kernel_size, kernel_size))
    center_point = np.array([kernel_size/2, kernel_size/2])

    for i in range(kernel_size):
        for j in range(kernel_size):
            xi = np.array([i, j])
            distance = np.linalg.norm(xi - center_point)
            kernel[i, j] = np.exp(-1/2 * (distance / sigma) ^ 2)
    kernel = kernel / np.sum(kernel)
    return kernel


# define the range filter:
def rangefilter(img_pitch, x, kernel_size, sigma = 1):
    kernel = np.zeros((kernel_size, kernel_size))
    img_pitch = np.float64(img_pitch)
    # intensity_difference = img_pitch - img_pitch[kernel_size//2, kernel_size//1]
    # kernel = np.exp(-1/2 * (()/sigma) ^2)
    for i in range(kernel_size):
        for j in range(kernel_size):
            intensity_difference = np.abs(img_pitch[i][j] - x)
            kernel[i][j] = np.exp(-1/2* (intensity_difference/sigma) ^2)
    kernel = kernel/np.sum(kernel)
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

# img = np.ones((9,9))
# print(img)
# kernel_size = 5
# pi = paddingImg(img, kernel_size=kernel_size)
# print(pi)





def filterimage(img, kernel_size, domain_sigma, range_sigma):




    img_height, img_width = img.shape
    img_bilateral = np.zeros((img_height, img_width))
    padded_img = paddingImg(img=img,kernel_size = kernel_size)
    padded_size = (kernel_size - 1) / 2

    for y in range(padded_size, padded_size + img_height+1):
        for x in range(padded_size, padded_size + img_width+1):



            # # get pitch of image
            # img_pitch = img[kernel_size - kernel_size:kernel_size + kernel_size,
            #                                        kernel_size - kernel_size:kernel_size + kernel_size]
            # # calculate range kernel
            # range_kernel = rangefilter(img_pitch= img_pitch, sigma=range_sigma, )
            #
            # # calculate domain kernel
            # domain_kernel = domainFilter(kernel_size=kernel_size, sigma=domain_sigma)
            #
            # final_kernel = range_kernel * domain_kernel
            #
            # nor_final_kernel = final_kernel / np.sum(final_kernel)


#
# if __name__ == '__main__':
#
#     # setting parameters
#
#     # 1. read image
#
#     # 2. padding image
#
#
#     # filter image
#
#

