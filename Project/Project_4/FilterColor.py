import numpy as np
import cv2
import MainOperation as mo


# define the domain filter
def domainFilter(kernel_size, sigma = 1):
    center_x, center_y = int((kernel_size - 1) / 2), int((kernel_size - 1) / 2)
    [x, y] = np.meshgrid(range(kernel_size), range(kernel_size))
    distance = (center_x - x) **2 + (center_y - y) **2
    kernel = np.exp(-1/2 * (distance/(sigma **2)))
    return kernel

# define the range filter:
'''
difference between np.sum() and sum() from python built.
'''
def rangefilter(img_pitch, x_intensity, kernel_size, sigma = 1):
    # kernel = np.zeros((kernel_size, kernel_size))
    # img_pitch = np.float64(img_pitch)
    # intensity_difference = np.abs(img_pitch - x_intensity)
    # kernel = np.exp(-1/2 * (intensity_difference / sigma) ** 2)
    # return kernel
    # kernel = np.zeros((kernel_size, kernel_size))
    # img_pitch = np.float64(img_pitch)
    intensity_difference =img_pitch - x_intensity
    # iidd = sum(intensity_difference **2)
    kernel = np.exp(-1/2 * (np.sum(intensity_difference **2, axis=2))/sigma **2)
    return kernel
# def rangefilter(img_pitch, x_intensity, kernel_size, sigma = 1):
#     kernel = np.zeros((kernel_size, kernel_size))
#     img_pitch = np.float64(img_pitch)
#     intensity_difference = np.abs(img_pitch - x_intensity)
#     kernel = np.exp(-1/2 * (intensity_difference / sigma) ** 2)
#     return kernel

def paddingImg(img, kernel_size):
    img_height, img_width, img_channel = img.shape
    # padding_size = (kernel_size - 1)/2
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1, img_channel))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width, :] = img
    return padded_img


def paddingReflect(img, kernel_size):
    # pre-processing:
    img_height, img_width, img_channel = img.shape
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1, img_channel))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width, :] = img

    #
    # img_height, img_width= img.shape
    # padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    # padding_size = int((kernel_size - 1) / 2)
    # padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img

    # 1. generate top, bottom, left, right padding
    # top_size: (kernel_size, width)
    # bottom_size : (kernel_size, width)
    # left_size : (height, kernel_size)
    # right_size : (height, kernel_size)
    top_value = img[:padding_size, :, :]
    reversed_top_value = np.flip(top_value, axis = 0)
    padded_img[:padding_size, padding_size:padding_size+img_width, :] = reversed_top_value

    bottom_img_value = img[-padding_size:,:, :]
    reversed_bottom_value = np.flip(bottom_img_value, axis = 0)
    padded_img[-padding_size:,padding_size:padding_size+img_width, :] = reversed_bottom_value

    left_value = img[:, :padding_size, :]
    reversed_left_value = np.flip(left_value, axis = 1)
    padded_img[padding_size:padding_size+img_height, :padding_size, :] = reversed_left_value


    right_value = img[:, -padding_size:, :]
    reversed_right_value = np.flip(right_value, axis = 1)
    padded_img[padding_size:padding_size+img_height, -padding_size:, :] = reversed_right_value

    # 2. generate four corner
    lt_corner = img[:padding_size, :padding_size, :]
    reversed_lt_corner = np.flip(np.flip(lt_corner, axis=1), axis = 0)
    padded_img[:padding_size, :padding_size, :] = reversed_lt_corner

    rt_corner = img[:padding_size, -padding_size:, :]
    reversed_rt_corner = np.flip(np.flip(rt_corner, axis = 1), axis = 0)
    padded_img[:padding_size, -padding_size:, :] = reversed_rt_corner

    lb_corner = img[-padding_size:, :padding_size, :]
    reversed_lb_corner = np.flip(np.flip(lb_corner, axis = 1), axis = 0)
    padded_img[-padding_size:, :padding_size, :] = reversed_lb_corner

    rb_corner = img[-padding_size:, -padding_size:, :]
    reversed_rb_corner = np.flip(np.flip(rb_corner, axis = 1), axis = 0)
    padded_img[-padding_size:, -padding_size:, :] = reversed_rb_corner
    return padded_img


# img=cv2.imread("img_cat.png", 1)[:7, :7, :]
# print(img.shape)
# # img = np.zeros((10, 10, 3))
# paddingReflect(img=img, kernel_size=5)




def filterimage(img, kernel_size, domain_sigma, range_sigma, original_size):
    # img_height, img_width, img_channel = img.shape
    img_height, img_width, img_channel = original_size
    img_bilateral = np.zeros(original_size)
    # padded_img = paddingImg(img=img, kernel_size=kernel_size)
    # padded_img = img
    # padded_img = cv2.copyMakeBorder(img,kernel_size,kernel_size,kernel_size,kernel_size,cv2.BORDER_REFLECT)
    padded_img = paddingReflect(img=img, kernel_size=kernel_size)
    padded_size = int((kernel_size - 1) / 2)


    # calculate the domain filter:
    domain_kernel = domainFilter(kernel_size = kernel_size, sigma = domain_sigma)

    for y in range(img_height):
        for x in range(img_width):
            # print((x, y))
            center_y = y + padded_size
            center_x = x + padded_size
            img_pitch = padded_img[center_y - padded_size : center_y + padded_size +1,
                                   center_x - padded_size : center_x + padded_size +1, :]

            # print(img_pitch.shape)
            range_kernel = rangefilter(img_pitch=img_pitch, x_intensity=img[y, x, :], kernel_size=kernel_size, sigma=range_sigma)

            img_pitch_L = img_pitch[:, :, 0]
            img_pitch_a = img_pitch[:, :, 1]
            img_pitch_b = img_pitch[:, :, 2]


            final_kernel = domain_kernel * range_kernel
            final_kernel_sum = np.sum(final_kernel)
            final_kernel = final_kernel/final_kernel_sum
            img_bilateral[y, x, 0] = np.sum(img_pitch_L * final_kernel)#/final_kernel_sum
            img_bilateral[y, x, 1] = np.sum(img_pitch_a * final_kernel)#/final_kernel_sum
            img_bilateral[y, x, 2] = np.sum(img_pitch_b * final_kernel)#/final_kernel_sum


    return img_bilateral

sigmaColor = [10, 30,50, 100, 300]
sigmaSpace = [1, 3, 10]
root_path = "original_paper_images/"
image_name = "sky"
py_saved_path = "output_color_image_python/"
im_saved_path = "output_color_image/"
# print(root_path+image_name+".png")

for ss in sigmaSpace:
    for sc in sigmaColor:

        kernel_size= 21
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
        print(root_path + image_name + ".png")
        img = mo.readColor(path=root_path + image_name + ".png", color_value=1)
        original_size = img.shape
        img = mo.cvtLAB(img=img)
        print(img.shape)
        filtered_img = np.uint8(filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
        result_img = mo.cvtBGR(filtered_img)

        image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
        img_saved_path = im_saved_path + image_saved_name
        print(img_saved_path)
        cv2.imwrite(img_saved_path, result_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        #--------------------------------------------------
        # directly output from opencv-python (compare)
        py_img = cv2.imread(root_path+image_name+".png", 1)
        py_img = cv2.cvtColor(py_img, cv2.COLOR_BGR2LAB)
        filtered_img = cv2.bilateralFilter(py_img, d=kernel_size, sigmaSpace=domain_sigma, sigmaColor=range_sigma)
        py_result_img = cv2.cvtColor(filtered_img, cv2.COLOR_LAB2BGR)
        image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
        img_saved_path = py_saved_path + image_saved_name
        print(img_saved_path)
        cv2.imwrite(img_saved_path, py_result_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])





# kernel_size = 5
# img = mo.readColor(path="rubiks_cube.png", color_value=1)
#
# original_size = img.shape
#
# img = mo.cvtLAB(img=img)
# print(img.shape)
#
# cv2.imshow("test color",img)
#
#
# domain_sigma = 10
# range_sigma = 200
# filtered_img = np.uint8(filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
#
# print((np.min(filtered_img), np.max(filtered_img)))
# result_img = mo.cvtBGR(filtered_img)
# cv2.imshow("converted result", result_img)
#
# # test on python_opencv
# py_img = cv2.imread("rubiks_cube.png", 1)
# py_img = cv2.cvtColor(py_img, cv2.COLOR_BGR2LAB)
# py_result_img = cv2.bilateralFilter(py_img, d=5, sigmaSpace=10, sigmaColor=200)
# py_result_img = cv2.cvtColor(py_result_img, cv2.COLOR_LAB2BGR)
# cv2.imshow("rest from opencv python", py_result_img)
#
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()