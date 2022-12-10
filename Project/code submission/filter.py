import numpy as np
import cv2
import FilterColor as fc
import BWBilateral as bwb
import MainOperation as mo
import os


#set parameter
root_gray_path = "original_paper_images/gray/"
root_color_path = "original_paper_images/color/"
im_saved_path = "output_image/"
# py_saved_path = "output_image_python/"
im_color_saved_path = "output_color_image/"
# py_color_saved_path = "output_color_image_python"

# check saved path
if not os.path.exists(im_saved_path):
    os.makedirs(im_saved_path)
# if not os.path.exists(py_saved_path):
#     os.makedirs(py_saved_path)
if not os.path.exists(im_color_saved_path):
    os.makedirs(im_color_saved_path)
# if not os.path.exists(py_color_saved_path):
#     os.makedirs(py_color_saved_path)



# set parameter here
sigmaColor = [10, 30, 50, 100, 300]
sigmaSpace = [1, 3, 10]
k_size = [23]

gray_image_list = os.listdir(root_gray_path)
color_image_list = os.listdir(root_color_path)


# read gray images:
for image_name in gray_image_list:
    print(root_gray_path + image_name)
    image_name = image_name.split(".")[0]
    img = mo.readGray(path = root_gray_path + image_name + ".png", color_value=0)
    original_size = img.shape
    for ks in k_size:
        kernel_size = ks
        for ss in sigmaSpace:
            for sc in sigmaColor:
                domain_sigma = ss
                range_sigma = sc
                #re-implement Bilateral filter
                filtered_img = np.uint8(bwb.filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
                image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
                img_saved_path = im_saved_path + image_saved_name
                print(img_saved_path)
                cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
                #-------------------------------------------------------------------------
                # python build-in method for comparison
                # py_img = cv2.imread(root_gray_path+image_name+".png", 0)
                # filtered_img = cv2.bilateralFilter(py_img, d=kernel_size, sigmaSpace=domain_sigma, sigmaColor=range_sigma)
                # image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
                # img_saved_path = py_saved_path + image_saved_name
                # print(img_saved_path)
                # cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

# color images
for image_name in color_image_list:
    image_name = image_name.split(".")[0]
    print(root_color_path + image_name)
    img = mo.readColor(path = root_color_path + image_name + ".png", color_value=1)
    original_size = img.shape
    for ks in k_size:
        kernel_size = ks
        for ss in sigmaSpace:
            for sc in sigmaColor:
                domain_sigma = ss
                range_sigma = sc
                original_size = img.shape
                # re-implement Bilateral filter
                clab_img = mo.cvtLAB(img=img)
                filtered_img = np.uint8(fc.filterimage(clab_img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
                result_img = mo.cvtBGR(filtered_img)
                image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
                img_saved_path = im_color_saved_path + image_saved_name
                print(img_saved_path)
                cv2.imwrite(img_saved_path, result_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
                #--------------------------------------------------
                # directly output from opencv-python (compare)
                # py_img = cv2.imread(root_color_path+image_name+".png", 1)
                # py_img = cv2.cvtColor(py_img, cv2.COLOR_BGR2LAB)
                # filtered_img = cv2.bilateralFilter(py_img, d=kernel_size, sigmaSpace=domain_sigma, sigmaColor=range_sigma)
                # py_result_img = cv2.cvtColor(filtered_img, cv2.COLOR_LAB2BGR)
                # image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
                # img_saved_path = py_saved_path + image_saved_name
                # print(img_saved_path)
                # cv2.imwrite(img_saved_path, py_result_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
