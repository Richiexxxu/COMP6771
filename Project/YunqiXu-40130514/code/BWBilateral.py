import numpy as np
import matplotlib.pyplot as plt

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
    intensity_difference = (img_pitch - x_intensity) **2
    kernel = np.exp(-1/2 * (intensity_difference / sigma **2))
    return kernel

def paddingImg(img, kernel_size):
    img_height, img_width = img.shape
    padding_size = (kernel_size - 1)/2
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img
    return padded_img


def paddingReflect(img, kernel_size):
    # pre-processing:
    img_height, img_width= img.shape
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img

    # 1. generate top, bottom, left, right padding
    # top_size: (kernel_size, width)
    # bottom_size : (kernel_size, width)
    # left_size : (height, kernel_size)
    # right_size : (height, kernel_size)
    top_value = img[:padding_size, :]
    reversed_top_value = np.flip(top_value, axis = 0)
    padded_img[:padding_size, padding_size:padding_size+img_width] = reversed_top_value

    bottom_img_value = img[-padding_size:,:]
    reversed_bottom_value = np.flip(bottom_img_value, axis = 0)
    padded_img[-padding_size:,padding_size:padding_size+img_width] = reversed_bottom_value

    left_value = img[:, :padding_size]
    reversed_left_value = np.flip(left_value, axis = 1)
    padded_img[padding_size:padding_size+img_height, :padding_size] = reversed_left_value

    right_value = img[:, -padding_size:]
    reversed_right_value = np.flip(right_value, axis = 1)
    padded_img[padding_size:padding_size+img_height, -padding_size:] = reversed_right_value

    # 2. generate four corner
    lt_corner = img[:padding_size, :padding_size]
    reversed_lt_corner = np.flip(np.flip(lt_corner, axis=1), axis = 0)
    padded_img[:padding_size, :padding_size] = reversed_lt_corner

    rt_corner = img[:padding_size, -padding_size:]
    reversed_rt_corner = np.flip(np.flip(rt_corner, axis = 1), axis = 0)
    padded_img[:padding_size, -padding_size:] = reversed_rt_corner

    lb_corner = img[-padding_size:, :padding_size]
    reversed_lb_corner = np.flip(np.flip(lb_corner, axis = 1), axis = 0)
    padded_img[-padding_size:, :padding_size] = reversed_lb_corner

    rb_corner = img[-padding_size:, -padding_size:]
    reversed_rb_corner = np.flip(np.flip(rb_corner, axis = 1), axis = 0)
    padded_img[-padding_size:, -padding_size:] = reversed_rb_corner
    return padded_img

def filterimage(img, kernel_size, domain_sigma, range_sigma, original_size):
    img_height, img_width = original_size
    img_bilateral = np.zeros(original_size)
    padded_img = paddingReflect(img=img, kernel_size=kernel_size)
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
            # calculate final kernel
            final_kernel = domain_kernel * range_kernel

            img_bilateral[y,x] = np.sum(img_pitch * final_kernel)/np.sum(final_kernel)
    return img_bilateral
