import numpy as np
import cv2 as cv


def readImg(path = None):
    print(path)
    return cv.imread(path, 0)

def FFTresult(input_image = None):
    ffted = np.fft.fft2(input_image)
    shifted_fft = np.fft.fftshift(ffted)
    return shifted_fft

def FFTmagnitude(input_data = None):
    magnitude = np.abs(input_data)
    return magnitude

def FFTphase(input_data = None):
    phase = np.angle(input_data)
    return phase

def magnitude_phase_combine(magnitude, phase):





img = readImg(path="house.tif")
# print(img)
FFT_a = FFTresult(input_image=img)
print(FFT_a)






