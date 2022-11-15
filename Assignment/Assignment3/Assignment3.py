import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
def readImg(path = None):
    # print(path)
    return cv.imread(path)[:, :,0]

def DFT2D(x, shift=True):
    '''
    Discrete space fourier transform
    x: Input matrix
    '''
    pi2 = 2 * np.pi
    N1, N2 = x.shape
    X = np.zeros((N1, N2), dtype=np.complex64)
    n1, n2 = np.mgrid[0:N1, 0:N2]

    for w1 in range(N1):
        for w2 in range(N2):
            if w1 == N1-1:
                print("finished_1")
            j2pi = np.zeros((N1, N2), dtype=np.complex64)
            j2pi.imag = pi2 * (w1 * n1 / N1 + w2 * n2 / N2)
            X[w1, w2] = np.sum(x * np.exp(-j2pi))
    print("finished")
    if shift:
        X = np.roll(X, N1 // 2, axis=0)
        X = np.roll(X, N2 // 2, axis=1)
    return X



def fftResult(input_image = None):
    ffted = np.fft.fft2(input_image)
    shifted_fft = np.fft.fftshift(ffted)
    return shifted_fft
    # return ffted
def fftMagnitude(input_data = None):
    magnitude = np.abs(input_data)
    return magnitude

def fftPhase(input_data = None):
    phase = np.angle(input_data)
    return phase

def magnitudePhaseCombine(magnitude=None, phase=None):
    combine = np.multiply(magnitude, np.exp(1j*phase))
    return combine



# def magnitudePhaseCombine(magnitude=None, phase=None):
#     # combine = np.multiply(magnitude, np.exp(1j*phase))
#     combine = np.multiply(magnitude, np.cos(phase))+np.multiply(magnitude, np.sin(phase) * 1j)
#     return combine

# def magnitudePhaseCombine(magnitude=None, phase = None, width=0, height = 0):
#     s_real = magnitude * np.cos(phase)
#     s_imag = magnitude * np.sin(phase)
#     s = np.zeros([width, height], dtype=complex)
#     s.real = np.array(s_real)
#     s.imag = np.array(s_imag)
#     return s

def reverseImg(input_data = None):
    img_reversed = np.uint8(np.abs(np.fft.ifft2(input_data)))
    # img_normed = img_reversed/np.max(img_reversed) * 255

    # return img_normed
    return img_reversed

#read image
img_house = readImg(path="house.tif")
img_jet = readImg(path="jet.tiff")
house_height, house_width = img_house.shape[0], img_house.shape[1]
jet_height, jet_width = img_jet.shape[0], img_jet.shape[1]

#FFT
house_fft = fftResult(input_image=img_house)
jet_fft = fftResult(input_image=img_jet)
# house_fft = DFT2D(img_house)
# jet_fft = DFT2D(img_jet)

# phase
house_phase = fftPhase(input_data=house_fft)
jet_phase = fftPhase(input_data=jet_fft)

# magnitude
house_mag = fftMagnitude(input_data=house_fft)
jet_mag = fftMagnitude(input_data=jet_fft)

# combine
hm_jp = magnitudePhaseCombine(magnitude=house_mag, phase=jet_phase)
jm_hp = magnitudePhaseCombine(magnitude=jet_mag, phase=house_phase)
# hm_jp = magnitudePhaseCombine(magnitude=house_mag, phase=jet_phase,width=house_width, height=house_height)
# jm_hp = magnitudePhaseCombine(magnitude=jet_mag, phase=house_phase, width = house_width, height=house_height)

print(np.shape(hm_jp))



# output image
new_image_a = reverseImg(input_data=hm_jp)
new_image_b = reverseImg(input_data=jm_hp)



plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(img_house, cmap="gray")
plt.subplot(222)
plt.imshow(img_jet, cmap="gray")
plt.subplot(223)
plt.imshow(new_image_a, cmap="gray")
plt.subplot(224)
plt.imshow(new_image_b, cmap="gray")
plt.show()


