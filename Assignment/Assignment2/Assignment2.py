import numpy as np
import cv2
import math



def readimg(path):
    return cv2.imread(path, 0)

def GaussinFilter(sigma,size):
    m = (size - 1.) / 2.
    n = (size - 1.) / 2.
    y,x = np.ogrid[ -m:m+1, -n : n+1]
    h = np.exp(-(x*x + y*y) / (2.*sigma * sigma))
    h [ h < np.finfo( h.dtype ).eps * h.max()] = 0
    all_sum = h.sum()
    if all_sum != 0:
        h /= all_sum
    return h

# blur the image and get a Blur image
def weightedSum(input_subimage, input_filter, filter_size):
    new_subimage = np.zeros((filter_size, filter_size))

    for y in range(filter_size):
        for x in range(filter_size):
            new_subimage[y,x] = input_subimage[y,x] * input_filter[y,x]
    return sum(sum(new_subimage))


def averagingFilter(input_image, input_filter, filter_size):
    image_height, image_width = input_image.shape[0],input_image.shape[1]
    output_image = np.zeros(input_image.shape)
    padding_size = (filter_size - 1)/2
    padding_short = np.zeros((padding_size,image_width))
    padding_long = np.zeros((image_height + (filter_size - 1), padding_size))
    padded_image = np.r_[padding_short,input_image]
    padded_image = np.r_[padded_image,padding_short]
    padded_image = np.c_[padding_long,padded_image]
    padded_image = np.c_[padded_image,padding_long]

    for y in range(padding_size, image_height + padding_size):
        for x in range(padding_size, image_width + padding_size):
            sub_image = padded_image[y - padding_size: y + (padding_size + 1), x - padding_size: x + (padding_size +1)]
            output_image[y - padding_size, x - padding_size] = weightedSum(input_subimage=sub_image, input_filter=input_filter, filter_size=filter_size)

    return output_image      
            

# use the blur image and the original image to get t


def averageWA(input_image):
    '''
        this function will return an weight average matrix which contains the value of c.
    '''
    sum_wa = sum(sum(input_image))
    return input_image/sum_wa


def calculateThreshold(input_image,C):
    '''
        in this part, the input image is the blured image not the original input images.
        The input C is also matrix with the same size as the image.
    '''
    image_height, image_width = input_image.shape
    output_image = np.zeros(input_image.size)
    for y in range(image_height):
        for x in range(image_width):
            output_image[y,x] = input_image[y,x] - C[y,x]
    
    return output_image

# threshold the image

def threshold(input_image,max_value, threshold):
    output_image = np.zeros(input_image.shape)
    height, width = input_image.shape
    for y in range(height):
        for x in range(width):
            if input_image[y, x] >= threshold[y, x]:
                output_image[y, x] = max_value
            else:
                output_image[y, x] = 0
    return output_image

# The overall Adaptive thresholding


def adaptiveThresholding(input_image, max_value, adaptive_method, threshold_type, filter_size, C = None, Gaussian_sigma = 1.4):

    if adaptive_method == "Gaussian":
        filter = GaussinFilter(sigma=Gaussian_sigma, size=filter_size)
    
    wa_image = averagingFilter(input_image=input_image, input_filter=filter, filter_size=filter_size)

    if C == None:
        C = averageWA(input_image=wa_image)

    if threshold_type == "THRESH_BINARY":
        t_image = calculateThreshold(input_image=wa_image,C=C)

    threshold_image = threshold(input_image=input_image, max_value=max_value, threshold=t_image)

    output_image = np.array(threshold_image, dtype = 'uint8')

    return output_image 


image = readimg("Doc.tiff")

output_image = adaptiveThresholding(input_image=image,max_value=255, adaptive_method="Gaussian", threshold_type="THRESH_BINARY", filter_size=5)

cv2.imshow('1', output_image)
cv2.imwrite('output.png', output_image)


