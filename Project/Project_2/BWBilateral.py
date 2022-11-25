import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
import MainOperation as mo

# define the domain filter
def domainFilter(kernel_size, sigma = 1):
    center_x, center_y = int((kernel_size - 1) / 2), int((kernel_size - 1) / 2)
    [x, y] = np.meshgrid(range(kernel_size), range(kernel_size))
    distance = (center_x - x) **2 + (center_y - y) **2
    kernel = np.exp(-1/2 * (distance/(sigma **2)))
    return kernel

# define the range filter:
def rangefilter(img_pitch, x_intensity, kernel_size, sigma = 1):
    kernel = np.zeros((kernel_size, kernel_size))
    img_pitch = np.float64(img_pitch)
    intensity_difference = np.abs(img_pitch - x_intensity)
    kernel = np.exp(-1/2 * (intensity_difference / sigma) ** 2)
    return kernel

def paddingImg(img, kernel_size):
    img_height, img_width = img.shape
    padding_size = (kernel_size - 1)/2
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img
    return padded_img

def filterimage(img, kernel_size, domain_sigma, range_sigma):
    img_height, img_width = img.shape
    img_bilateral = np.zeros((img_height, img_width))
    padded_img = paddingImg(img=img,kernel_size = kernel_size)
    padded_size = int((kernel_size - 1) / 2)

    # calculate the domain filter:
    domain_kernel = domainFilter(kernel_size=kernel_size, sigma=domain_sigma)


    for y in range(img_height):
        for x in range(img_width):
            center_y = y + padded_size
            center_x = x + padded_size
            img_pitch = padded_img[center_y - padded_size : center_y + padded_size +1,
                                   center_x - padded_size : center_x + padded_size +1]

            range_kernel = rangefilter(img_pitch= img_pitch, x_intensity= img[y,x],kernel_size=kernel_size, sigma=range_sigma)
            # range_kernel = rangefilter(img_pitch=img_pitch, x_intensity=img[center_y, center_x], kernel_size=kernel_size, sigma=range_sigma)
            # calculate final kernel
            final_kernel = domain_kernel * range_kernel
            final_kernel = final_kernel / np.sum(final_kernel)

            img_bilateral[y,x] = np.sum(img_pitch * final_kernel)
    return img_bilateral



img = mo.readColor(path="img_cat.png", color_value=0)
cv2.imshow("test original", img)
# img = mo.cvtLAB(img=img)
print(img.shape)
# cv2.imshow("test color",img)


img = mo.normolization(img=img)
print((np.min(img), np.max(img)))

kernel_size = 25
domain_sigma = 10
range_sigma = 30
filtered_img = filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma)
cv2.imshow("filter_result", filtered_img)



cv2.waitKey(0)
cv2.destroyAllWindows()









