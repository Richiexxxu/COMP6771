import numpy as np
import cv2
import BWBilateral as bwb
import FilterColor as fc
import MainOperation as mo
# from skimage.metrics import peak_signal_noise_ratio as psnr
import os



sigmaColor = [10, 30, 100, 300]
sigmaSpace = [1, 3, 10]
k_size = [23]


root_path = "original_paper_images/color/"
image_name = "child"

baseline_saved_path = "output_baseline/"

# read color image
print(root_path + image_name + ".png")
img = mo.readColor(path=root_path + image_name + ".png", color_value=1)
for ks in k_size:
    kernel_size = ks
    for ss in sigmaSpace:
        for sc in sigmaColor:

            domain_sigma = ss
            range_sigma = sc

            # read image

            original_size = img.shape
            clab_img = mo.cvtLAB(img=img)
            # print(.shape)

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
    # print(psnr(img, medianblur_img, data_range=255))
    # print("median blur", psnr)

    # 2. mean blur
    meanblur_img = cv2.blur(img, ksize=(kernel_size, kernel_size), borderType=cv2.BORDER_REFLECT)
    image_saved_name = image_name + "_mean_" + str(kernel_size) + ".png"
    img_saved_path = baseline_saved_path + image_saved_name
    print(img_saved_path, "psnr: ", mo.PSNR(img, meanblur_img))
    cv2.imwrite(img_saved_path, meanblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    # print(psnr(img, meanblur_img, data_range=255))
    # print("mean", psnr)



    # cv2.imshow("gaussian"+str(kernel_size), gaussian_img)
    # cv2.imshow("show blur", filtered_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows

# # read gray image
# print(root_path + image_name + ".png")
# img = mo.readColor(path=root_path + image_name + ".png", color_value=0)
# for ks in k_size:
#     kernel_size = ks
#     for ss in sigmaSpace:
#         for sc in sigmaColor:

#             domain_sigma = ss
#             range_sigma = sc

#             # read image

#             original_size = img.shape
#             # clab_img = mo.cvtLAB(img=img)
#             # print(.shape)

#             filtered_img = np.uint8(bwb.filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
#             # result_img = mo.cvtBGR(filtered_img)

#             image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + "_ks_" + str(kernel_size) + ".png"
#             img_saved_path = baseline_saved_path + image_saved_name
#             # print(img_saved_path, "psnr", psnr(img, filtered_img, data_range=255))
#             print(img_saved_path, "psnr", mo.PSNR(img, filtered_img))
#             cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

#         # 3. Gaussian blur
#         gaussian_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), domain_sigma, domain_sigma)
#         image_saved_name = image_name + "_gaussian_" + str(kernel_size) + "_ds_" + str(domain_sigma) + ".png"
#         img_saved_path = baseline_saved_path + image_saved_name
#         print(img_saved_path, "psnr: ", mo.PSNR(img, gaussian_img))
#         cv2.imwrite(img_saved_path, gaussian_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#      #---------------------------------------------------
#     #compared with other method
#     # 1. median blur
#     medianblur_img = cv2.medianBlur(img, ksize=kernel_size)
#     image_saved_name = image_name + "_median_" + str(kernel_size) + ".png"       
#     img_saved_path = baseline_saved_path + image_saved_name
#     print(img_saved_path, "psnr: ", mo.PSNR(img, medianblur_img))
#     cv2.imwrite(img_saved_path, medianblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#     # print(psnr(img, medianblur_img, data_range=255))
#     # print("median blur", psnr)

#     # 2. mean blur
#     meanblur_img = cv2.blur(img, ksize=(kernel_size, kernel_size), borderType=cv2.BORDER_REFLECT)
#     image_saved_name = image_name + "_mean_" + str(kernel_size) + ".png"
#     img_saved_path = baseline_saved_path + image_saved_name
#     print(img_saved_path, "psnr: ", mo.PSNR(img, meanblur_img))
#     cv2.imwrite(img_saved_path, meanblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#     # print(psnr(img, meanblur_img, data_range=255))
#     # print("mean", psnr)



#     # cv2.imshow("gaussian"+str(kernel_size), gaussian_img)
#     # cv2.imshow("show blur", filtered_img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows



