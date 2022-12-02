import numpy as np
import cv2
import BWBilateral as bwb
import MainOperation as mo
from skimage.metrics import peak_signal_noise_ratio as psnr

#run balck image

sigmaColor = [10, 30, 100, 300]
sigmaSpace = [1, 3, 10]
kernel_size = [25]

root_path = "original_paper_images/"
image_name = "cat"
py_saved_path = "output_image_python/"
im_saved_path = "output_image/"
baseline_saved_path = "output_baseline/"
# read images:
print(root_path + image_name)
img = mo.readGray(path = root_path + image_name + ".png", color_value=0)
original_size = img.shape

for ks in kernel_size:
    kernel_size = ks
    for ss in sigmaSpace:
        for sc in sigmaColor:

            # kernel_size= 21
            domain_sigma = ss
            range_sigma = sc
            

            #------------------------------------------------------------
            #use implement method
            filtered_img = np.uint8(bwb.filterimage(img, kernel_size=kernel_size, domain_sigma=domain_sigma, range_sigma=range_sigma, original_size=original_size))
            image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
            img_saved_path = im_saved_path + image_saved_name
            print(img_saved_path)
            print(psnr(img, filtered_img,data_range=255))
            # print(mo.PSNR(original_img=np.float32(img), denoised_img=np.float32(filtered_img)))
            # cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

            #--------------------------------------------------
            # directly output from opencv-python (compare)
            # py_img = cv2.imread(root_path+image_name+".png", 0)
            # filtered_img = cv2.bilateralFilter(py_img, d=kernel_size, sigmaSpace=domain_sigma, sigmaColor=range_sigma)
            # image_saved_name = image_name + "_ds" + str(domain_sigma) + "_rs" + str(range_sigma) + ".png"
            # img_saved_path = py_saved_path + image_saved_name
            # print(img_saved_path)
            # print(psnr(img, filtered_img, data_range=255))
            # # cv2.imwrite(img_saved_path, filtered_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


    #---------------------------------------------------
    #compared with other method
    # 1. median blur
    medianblur_img = cv2.medianBlur(img, ksize=kernel_size)
    image_saved_name = image_name + "_median_" + str(kernel_size) + ".png"       
    img_saved_path = baseline_saved_path + image_saved_name
    print(img_saved_path)
    # cv2.imwrite(img_saved_path, medianblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    print(psnr(img, medianblur_img, data_range=255))
    # print("median blur", psnr)

    # 2. mean blur
    meanblur_img = cv2.blur(img, ksize=(kernel_size, kernel_size), borderType=cv2.BORDER_REFLECT)
    image_saved_name = image_name + "_mean_" + str(kernel_size) + ".png"
    img_saved_path = baseline_saved_path + image_saved_name
    print(img_saved_path)
    # cv2.imwrite(img_saved_path, meanblur_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    print(psnr(img, meanblur_img, data_range=255))
    # print("mean", psnr)

    # 3. Gaussian blur
    gaussian_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 1, 1)
    image_saved_name = image_name + "_gaussian_" + str(kernel_size) + ".png"
    img_saved_path = baseline_saved_path + image_saved_name
    print(img_saved_path)
    # cv2.imwrite(img_saved_path, gaussian_img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    print(psnr(img, gaussian_img, data_range=255))
    # cv2.imshow("gaussian"+str(kernel_size), gaussian_img)
    # cv2.imshow("show blur", filtered_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows
