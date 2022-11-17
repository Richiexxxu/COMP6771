import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("./shin.jpeg", 0)
#print(img)
#cv2.imshow("Shin",img)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
res = np.log(np.abs(fshift))
#res = res.astype(np.int8)

ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)


plt.subplot(131), plt.imshow(img,'gray'), plt.title('Original')
plt.axis('off')
plt.subplot(132), plt.imshow(res,'gray'), plt.title('Fourier Image')
plt.axis('off')
plt.subplot(133), plt.imshow(iimg,'gray'), plt.title('Inverse Fourier Image')
plt.axis('off')
plt.show()
iimg = iimg.astype(np.int8)
print(iimg)
cv2.imshow('123',iimg)
cv2.waitKey(0)