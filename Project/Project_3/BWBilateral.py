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
    # img_height, img_width = img.shape
    img_height, img_width = original_size
    img_bilateral = np.zeros(original_size)
    print(img_bilateral.shape)
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


sigmaColor = [10, 30, 100, 300]
sigmaSpace = [1, 3, 10]
root_path = "original_paper_images/"
image_name = "cat_part"
py_saved_path = "output_image_python/"
im_saved_path = "output_image/"
# print(root_path+image_name+".png")
for ss in sigmaSpace:
    for sc in sigmaColor:

        kernel_size= 35
        domain_sigma = ss
        range_sigma = sc


        # # cv2.imshow("first", img)

        # # print(img.shape)
        # # print(img.shape)

        #------------------------------------------------------------
        #use implement method
        # img = mo.readGray(path=root_path+image_name+".png", color_value=0)
        # original_size = img.shape
        # filtered_img = np.uint8(filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
        # # print("filter", filtered_img.shape)
        # # cv2.imshow(str(sc), filtered_img)
        # # cv2.waitKey(0)
        # image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
        # img_saved_path = im_saved_path + image_saved_name
        # print(img_saved_path)
        # cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        #--------------------------------------------------
        # directly output from opencv-python (compare)
        py_img = cv2.imread(root_path+image_name+".png", 0)
        filtered_img = cv2.bilateralFilter(py_img, d=kernel_size, sigmaSpace=domain_sigma, sigmaColor=range_sigma)
        image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
        img_saved_path = py_saved_path + image_saved_name
        print(img_saved_path)
        cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

    





#
# img = cv2.imread("original_paper_images/snack.png")
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


