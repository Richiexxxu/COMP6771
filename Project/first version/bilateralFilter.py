import cv2
import math
import numpy as np
import time  # import time to count the runtime

time_start = time.time()
# set pi
PI = math.pi
# Read the image.
img = cv2.imread('./light.jpg')
imgStd = img.std()
imgStd = 1
imgMax = img.max()
imgMin = img.min()
# according to the paper
NB_SEGMENT = int((imgMax - imgMin) / imgStd)



# function for padding an given image
def MyPadding(image, padding):
    # now we assume it is grayscale image! later on rgb
    h, w = image.shape
    if (padding < 0):
        print("wrong padding data!")
    newH = h + 2 * padding
    newW = w + 2 * padding
    # a new blank image
    res = np.zeros((newH, newW))
    image = image.astype(np.uint8)
    # calculating the output image
    for i in range(padding, h + padding):
        for j in range(padding, w + padding):
            res[i][j] = image[i - padding][j - padding]

    # convert the image to the grayscale range
    res = res.astype(np.uint8)
    # return the ouput image
    return res

# Manually convert rgb to grayscale images
def MyRgb2Gray(image):
    # image's shape
    h, w, c = image.shape

    # grayscale's computation equation
    grayVal = 0.2126 * img[:, :, 0] + 0.7152 * img[:, :, 1] + 0.0722 * img[:, :, 2]
    # get the result
    gray_image = grayVal.reshape(h, w).astype(np.uint8)

    # return the result
    return gray_image


# function for output a Gaussian Kernel
# here sigma is the standard difference, the scalar parameter
def GaussianKernelSpatial(size, sigma):
    if size % 2 == 0:
        print("wrong!")
        return
    kernel = np.zeros((size, size))
    coreX, coreY = int(size / 2), int(size / 2)  # 7/2 = 3 e.g.

    kernelCoreVal = 1 / (2 * PI * sigma ** 2)
    for x in range(0, size):
        for y in range(0, size):
            kernel[x][y] = math.exp(-1 * ((x - coreX) * (x - coreX) + (y - coreY) * (y - coreY)) / (2 * sigma ** 2)) / (
                        2 * PI * sigma ** 2)

    kernel[coreX][coreY] = kernelCoreVal
    kernel /= kernel.sum()
    return kernel


# the function for bilateral filtering
def GaussianKernelIntensity(size, sigma, image, ix, iy):
    if size % 2 == 0:
        print("wrong!")
        return
    kernel = np.zeros((size, size))
    coreX, coreY = int(size / 2), int(size / 2)  # 7/2 = 3 e.g.
    # start position in original image
    startX, startY = ix - coreX, iy - coreY
    kernelCoreVal = 1 / (2 * PI * sigma ** 2)
    for x in range(0, size):
        for y in range(0, size):
            kernel[x][y] = math.exp(-1 * ((image[startX + x][startY + y] - image[ix][iy]) / (2 * sigma ** 2))) / (
                        2 * PI * sigma ** 2)

    kernel[coreX][coreY] = kernelCoreVal
    kernel /= kernel.sum()
    return kernel


# my function for convulution
def MyConv2D(img, kernel):
    paddingSize = int(kernel.shape[0] / 2)  # e.g. 5/2 = 2
    # make a new conv picture
    convImg = MyPadding(img, paddingSize)
    h, w = img.shape  # original shape
    ksize = kernel.shape[0]  # kernel's size
    convH, convW = convImg.shape  # the padding image shape
    res = np.zeros((h, w))
    for i in range(0, h):
        for j in range(0, w):
            res[i][j] = int((convImg[i:i + ksize, j:j + ksize] * kernel).sum())

    res = res.astype(np.uint8)
    return res

# not using now
def Gaussian(p, s):
    x = p - s
    sigma = 1
    res = math.exp(-(x * x / sigma))

def DownSample(img, z):
    h, w = img.shape
    newH, newW = int(h/z), int(w/z)
    res = np.zeros([newH, newW])
    for i in range(0, newH):
        for j in range(0, newW):
            res[i][j]= img[i*z:i*z+z,j*z:j*z+z].mean()
    return res


def UpSample(img, z):
    h, w = img.shape
    newH, newW = int(h*z), int(w*z)
    res = np.zeros([newH,newW])
    for i in range(0, h):
        for j in range(0, w):
            res[i*z:i*z+z,j*z:j*z+z]=img[i][j]
    return res

def Bilateral(image, GaussianSpatialKer, sigma):
    paddingSize = int(GaussianSpatialKer.shape[0] / 2)  # e.g. 5/2 = 2
    # make a new conv picture
    convImg = MyPadding(img, paddingSize)
    h, w = img.shape  # original shape
    ksize = GaussianSpatialKer.shape[0]  # kernel's size
    convH, convW = convImg.shape  # the padding image shape
    res = np.zeros((h, w))
    for i in range(0, h):
        for j in range(0, w):
            GauKerInt = GaussianKernelIntensity(ksize, sigma, convImg, i, j)
            res[i][j] = int((convImg[i:i + ksize, j:j + ksize] * GaussianSpatialKer * GauKerInt).sum())
            Wp = (GaussianSpatialKer * GauKerInt).sum()
            res[i][j] /= Wp

    res = res.astype(np.uint8)
    return res

def gr(image,i_j,sigma):
    ds = (image - i_j)**2
    res = 1 / (np.sqrt(2* np.pi)*sigma) \
          * np.exp(-ds/(2*sigma**2))
    return res

def InterpolationWeight(img1, img2):
    pass

def FastBilateral(image, spatialKernel, downsam=1):
    oriimg = image
    h, w = image.shape
    #(675,1200)
    J = np.zeros((h,w))
    J1 = np.zeros((h,w))
    I_delta = (imgMax - imgMin) / NB_SEGMENT
    # new add start
    if(downsam is not 1):
        J1 = np.zeros((int(h/downsam), int(w/downsam)))
        image = DownSample(image, downsam)
    # new add stop
    for j in range(0,NB_SEGMENT):
        i_j = imgMin + j*I_delta
        G_j = gr(image,i_j,0.1)
        K_j = cv2.filter2D(G_j,-1,spatialKernel)
        H_j = G_j * image
        H_j_2 = cv2.filter2D(H_j,-1,spatialKernel)
        J_j = H_j_2/(K_j+0.1)
        I_diff = np.abs(oriimg - i_j)
        #new add start
        if(downsam is not 1):
            I_diff = np.abs(image - i_j)
            mask = I_diff < I_delta
            J1 = J1 + J_j * (mask * (1 - (I_diff / I_delta)))
        #new add stop
        else:
            mask = I_diff < I_delta
            J = J + J_j * (mask*(1-(I_diff/I_delta)))
    if(downsam is 1):
        return J.astype(np.uint8)
    else:
        return J1.astype(np.uint8)



#img = MyRgb2Gray(img)
# print(GaussianKernel(3,1))
# Apply bilateral filter with d = 15,
# sigmaColor = sigmaSpace = 75.
# avg = cv2.blur(img,(5,5))
# gau = cv2.GaussianBlur(img,(5,5),0)
# bilateral = cv2.bilateralFilter(img, 15, 75, 75)


# merge the picture
# b,g,r = cv2.split(img)
# change_image = cv2.merge([b,g,r])
# (675, 1200, 3)

# print(GaussianKernelIntensity(3, 1, img, 532,542))
#cv2.imshow('Original', img)
# img = MyPadding(img,2)
#Ker = GaussianKernelSpatial(7, 1.12)
# out = Bilateral(img, Ker,1)
# out = cv2.filter2D(img, -1, Ker)
#out = FastBilateral(img, Ker)
# cv2.imshow('MyGaussian', out)
#ds = DownSample(img,2)
#ds = UpSample(ds,2)
#ds = ds.astype(np.uint8)
#cv2.imshow('downsample',ds)
# cv2.imshow('GaussianBlur',gau)
#cv2.imshow('bilateral', out)
#time_end = time.time()
#print('time cost : ', time_end - time_start, 's')
#print(out)
#cv2.waitKey(0)


