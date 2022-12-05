import numpy as np
import cv2
import matplotlib.pyplot as plt

def imgread(path):
    return cv2.imread(path, 0)


def generateHis(img, L):
    img_height, img_width = img.shape
    value_his = np.zeros(L)
    for y in range(img_height):
        for x in range(img_width):
            intensity = img[y,x]
            value_his[intensity] += 1
    value_prob = value_his * 1.0 / (img_height * img_width)
    return value_his, value_prob

def Ostu(img, value_his, value_prob, L):
    img_height, img_width = img.shape
    final_var = 0
    var_list = []
    for k in range(1, L):
        p1 = np.sum(value_prob[:k])
        p2 = 1.0 - p1
        m1 = 0.0
        m2 = 0.0
        if p1 !=0 and p2 != 0:
            for i in range(k):
                m1 += i * value_prob[i]
            m1 = m1/p1
            for j in range(k, L):
                m2 += j * value_prob[j]
            m2 = m2/p2
            var = p1 * p2 * (m1- m2) **2
            var_list.append(var)

            if var > final_var:
                final_var = var
        else:
            var_list.append(0)
    var_list = np.array(var_list)
    threshold_list = np.where(var_list == np.max(var_list))[0]
    threshold = np.average(threshold_list)
    return threshold


def paddingReflect(img, kernel_size):
    # pre-processing:
    img_height, img_width= img.shape
    padded_img = np.zeros((img_height + kernel_size - 1, img_width + kernel_size - 1))
    padding_size = int((kernel_size - 1) / 2)
    padded_img[padding_size: padding_size + img_height, padding_size: padding_size + img_width] = img
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

def averagingFilter(input_image, filter_size):
    input_filter = np.zeros((filter_size, filter_size))
    image_height, image_width = input_image.shape[0],input_image.shape[1]
    output_image = np.zeros(input_image.shape)
    padding_size = int((filter_size - 1)/2)
    padded_image = paddingReflect(img=input_image, kernel_size=filter_size)

    for y in range(padding_size, image_height + padding_size):
        for x in range(padding_size, image_width + padding_size):
            sub_image = padded_image[y - padding_size: y + (padding_size + 1), x - padding_size: x + (padding_size +1)]
            output_image[y - padding_size, x - padding_size] = np.sum(sub_image)/(filter_size * filter_size)
    return output_image  


img = imgread(path="tools_noisy.png")
value_his, value_prob = generateHis(img=img, L = 256)
th = Ostu(img=img, value_his=value_his, value_prob=value_prob, L=256)
print(th)

img[img<=th] = 0
img[img>th] = 255
cv2.imshow("test", img)
cv2.imwrite("Figures/ostu_result.png", img)

py_img = imgread(path="tools_noisy.png")
retVal_b, b_img = cv2.threshold(py_img, 0, 255, cv2.THRESH_OTSU)
print(retVal_b)
cv2.imshow('test_2', b_img)
cv2.imwrite("Figures/ostu_py.png", b_img)


img = imgread(path = "tools_noisy.png")
blur_img = np.uint8(averagingFilter(input_image=img, filter_size=7))
blur_value_his, blur_value_prob = generateHis(img=blur_img, L = 256)
blur_th = Ostu(img=blur_img, value_his=blur_value_his, value_prob=blur_value_prob, L=256)
print(blur_th)
blur_img[blur_img<=blur_th] = 0
blur_img[blur_img>blur_th] = 255
cv2.imshow("test blur", blur_img)
cv2.imwrite("Figures/ostu_average.png", blur_img)

py_img = imgread(path="tools_noisy.png")
py_blur_img = cv2.blur(img, ksize=(7, 7), borderType=cv2.BORDER_REFLECT)
retVal_b, blur_b_img = cv2.threshold(py_blur_img, 0, 255, cv2.THRESH_OTSU)
print(retVal_b)
cv2.imshow('test_blur python', blur_b_img)
cv2.imwrite("Figures/ostu_py_average.png", blur_b_img)


cv2.waitKey(0)
cv2.destroyAllWindows()




