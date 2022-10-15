import numpy as np
import cv2
from matplotlib import pyplot as plt

def read_grayscales(img):
    img = cv2.imread(img,0)
    return img
def calculate_histogram_test(img, L):
    image_flatten = img.flatten()
    print(len(image_flatten))
    bin_statistic = np.bincount(image_flatten, minlength = L)
    return bin_statistic
def calculate_histogram(img, L):
    image_flatten = img.flatten()
    new_list = np.zeros(L)
    for each_pixel in image_flatten:
        new_list[each_pixel] += 1
    return new_list 
        

def histogram_show(hist):
    print(len(hist))
    plt.bar(range(len(hist)), hist)
    plt.xlabel("rk")
    plt.ylabel("nk")
    plt.title("Histogram of imput image")
    plt.show()
def calculate_prob(hist,total_pixels):
    return [values_each_bin/total_pixels for values_each_bin in hist]
def calculate_sk(hist,L, total_number):
    new_list = np.zeros(L) 
    for index, each_value in enumerate(hist):
        calculate_sum = sum(hist[:index+1])
        new_list[index] = round((L-1)/total_number * calculate_sum)
    return new_list

def calculate_mapping(hist_sk,hist):
    new_list = np.zeros(len(hist))
    # print(hist_sk)
    for index, mapped_bin in enumerate(hist_sk):
        pixels_value = hist[index]
        # print(pixels_value)
        new_list[int(mapped_bin)] += pixels_value
    return new_list   

def new_image(img, sk):
    height, width = img.shape
    new_img = np.zeros(img.shape, dtype = 'uint8')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i, j] = sk[img[i,j]]
    return new_img
img_name = 'HawkesBay.jpeg'
img = read_grayscales(img_name)
cv2.imshow("original image", img)
print(img.shape)
cv2.waitKey(0)
# cv2.destroyAllWindows()

# calculate the histogram from the imput image
histogram_statis_test = calculate_histogram_test(img, 256)
# print(histogram_statis_test)
# print(len(histogram_statis_test))
# print(sum(histogram_statis_test))
histogram_statis = calculate_histogram(img, 256)
# print(histogram_statis)
# print((histogram_statis == histogram_statis_test).all())
histogram_show(histogram_statis)
pr = calculate_prob(histogram_statis, img.shape[0]*img.shape[1])
# print(pr)
# print(sum(pr))
sk = calculate_sk(histogram_statis, 256, img.shape[0]*img.shape[1])
# print(sk)
mapped_nk = calculate_mapping(sk, histogram_statis)
# print(mapped_nk)
new_img = new_image(img, sk)
cv2.imshow("mapped image", new_img)
cv2.waitKey(0)
cv2.destoryAllWindows()
histogram_show(mapped_nk)