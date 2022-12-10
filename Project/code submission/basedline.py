import numpy as np
import cv2
import BWBilateral as bwb
import FilterColor as fc
import MainOperation as mo
import os



root_gray_path = "original_paper_images/gray/"
root_color_path = "original_paper_images/color/"
baseline_saved_path = "output_baseline/"


if not os.path.exists(baseline_saved_path):
    os.makedirs(baseline_saved_path)

# set parameters
sigmaColor = [10, 30, 100, 300]
sigmaSpace = [1, 3, 10]
k_size = [23]

gray_image_list = os.listdir(root_gray_path)
color_image_list = os.listdir(root_color_path)


# read color image
for image_name in color_image_list:
    print(root_color_path + image_name)
    image_name = image_name.split(".")[0]
    img = mo.readColor(path=root_color_path + image_name + ".png", color_value=1)
    for ks in k_size:
        kernel_size = ks
        for ss in sigmaSpace:
            for sc in sigmaColor:
                domain_sigma = ss
                range_sigma = sc
                original_size = img.shape
                clab_img = mo.cvtLAB(img=img)
                filtered_img = np.uint8(fc.filterimage(clab_img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
                result_img = mo.cvtBGR(filtered_img)

                image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + "_ks_" + str(kernel_size) + ".png"
                img_saved_path = baseline_saved_path + image_saved_name
                print(img_saved_path, "psnr", mo.PSNR(img, result_img))
                cv2.imwrite(img_saved_path, result_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

            # 3. Gaussian blur
            gaussian_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), domain_sigma, domain_sigma)
            image_saved_name = image_name + "_gaussian_" + str(kernel_size) + "_ds_" + str(domain_sigma) + ".png"
            img_saved_path = baseline_saved_path + image_saved_name
            print(img_saved_path, "psnr: ", mo.PSNR(img, gaussian_img))
            cv2.imwrite(img_saved_path, gaussian_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        #---------------------------------------------------
        #compared with other method
        # 1. median blur
        medianblur_img = cv2.medianBlur(img, ksize=kernel_size)
        image_saved_name = image_name + "_median_" + str(kernel_size) + ".png"       
        img_saved_path = baseline_saved_path + image_saved_name
        print(img_saved_path, "psnr: ", mo.PSNR(img, medianblur_img))
        cv2.imwrite(img_saved_path, medianblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        # 2. mean blur
        meanblur_img = cv2.blur(img, ksize=(kernel_size, kernel_size), borderType=cv2.BORDER_REFLECT)
        image_saved_name = image_name + "_mean_" + str(kernel_size) + ".png"
        img_saved_path = baseline_saved_path + image_saved_name
        print(img_saved_path, "psnr: ", mo.PSNR(img, meanblur_img))
        cv2.imwrite(img_saved_path, meanblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


for image_name in gray_image_list:
    # read gray image
    print(root_gray_path + image_name)
    image_name = image_name.split(".")[0]
    img = mo.readColor(path=root_gray_path + image_name + ".png", color_value=0)
    for ks in k_size:
        kernel_size = ks
        for ss in sigmaSpace:
            for sc in sigmaColor:
                domain_sigma = ss
                range_sigma = sc
                original_size = img.shape
                filtered_img = np.uint8(bwb.filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
                image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + "_ks_" + str(kernel_size) + ".png"
                img_saved_path = baseline_saved_path + image_saved_name
                print(img_saved_path, "psnr", mo.PSNR(img, filtered_img))
                cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

            # 3. Gaussian blur
            gaussian_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), domain_sigma, domain_sigma)
            image_saved_name = image_name + "_gaussian_" + str(kernel_size) + "_ds_" + str(domain_sigma) + ".png"
            img_saved_path = baseline_saved_path + image_saved_name
            print(img_saved_path, "psnr: ", mo.PSNR(img, gaussian_img))
            cv2.imwrite(img_saved_path, gaussian_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
        #---------------------------------------------------
        #compared with other method
        # 1. median blur
        medianblur_img = cv2.medianBlur(img, ksize=kernel_size)
        image_saved_name = image_name + "_median_" + str(kernel_size) + ".png"       
        img_saved_path = baseline_saved_path + image_saved_name
        print(img_saved_path, "psnr: ", mo.PSNR(img, medianblur_img))
        cv2.imwrite(img_saved_path, medianblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

        # 2. mean blur
        meanblur_img = cv2.blur(img, ksize=(kernel_size, kernel_size), borderType=cv2.BORDER_REFLECT)
        image_saved_name = image_name + "_mean_" + str(kernel_size) + ".png"
        img_saved_path = baseline_saved_path + image_saved_name
        print(img_saved_path, "psnr: ", mo.PSNR(img, meanblur_img))
        cv2.imwrite(img_saved_path, meanblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
