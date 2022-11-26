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
    kernel = np.zeros((kernel_size, kernel_size))
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
    padding_size = (kernel_size - 1)/2
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1, img_channel))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width, :] = img
    return padded_img


def filterimage(img, kernel_size, domain_sigma, range_sigma):
    img_height, img_width, img_channel = img.shape
    img_bilateral = np.zeros((img_height, img_width, img_channel))
    # padded_img = paddingImg(img=img, kernel_size=kernel_size)
    padded_img = img
    padded_size = int((kernel_size - 1) / 2)


    # calculate the domain filter:
    domain_kernel = domainFilter(kernel_size = kernel_size, sigma = domain_sigma)

    for y in range(img_height):
        for x in range(img_width):
            print((x, y))
            center_y = y + padded_size
            center_x = x + padded_size
            img_pitch = padded_img[center_y - padded_size : center_y + padded_size +1,
                                   center_x - padded_size : center_x + padded_size +1, :]

            print(img_pitch.shape)
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


kernel_size = 15
img = mo.readColor(path="rubiks_cube.png", color_value=1)

pimg = np.uint8(paddingImg(img=img, kernel_size=kernel_size))
# cv2.imshow("test original", img)
# img = mo.normolization(img=img)
img = mo.cvtLAB(img=img)
print(img.shape)
# cv2.imshow("test color",img)



domain_sigma = 10
range_sigma = 200
filtered_img = np.uint8(filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma))

# filtered_img = mo.renormolization(img=filtered_img)
print((np.min(filtered_img), np.max(filtered_img)))
# print(filtered_img.shape)
# cv2.imshow("filter_result", filtered_img)
# filtered_img = np.uint8(filtered_img)
result_img = mo.cvtBGR(filtered_img)
cv2.imshow("converted result", result_img)

# kernel_size = 15
# domain_sigma = 10
# range_sigma = 300
# filtered_img = filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma)
#
# # filtered_img = mo.renormolization(img=filtered_img)
# print((np.min(filtered_img), np.max(filtered_img)))
# # print(filtered_img.shape)
# # cv2.imshow("filter_result", filtered_img)
# # filtered_img = np.uint8(filtered_img)
# result_img = mo.cvtBGR(filtered_img)
# cv2.imshow("converted result_2", result_img)


cv2.waitKey(0)
cv2.destroyAllWindows()