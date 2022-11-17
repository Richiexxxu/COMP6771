import cv2
import math
import time
import numpy as np
import time # import time to count the runtime
from bilateralFilter import *


time_start = time.time()
img = cv2.imread('./stairs.png')
B, G, R = cv2.split(img)


B=B.astype(np.float32)
G=G.astype(np.float32)
R=R.astype(np.float32)
inputIntensity = ((R*20 + G*40 + B)/61)
inputIntensity=inputIntensity.astype(np.uint8)
# no 0 allowed here
h,w = inputIntensity.shape
for i in range(0,h):
    for j in range(0,w):
        if inputIntensity[i][j] == 0:
            inputIntensity[i][j] = 1

# r, g, b here mean the rate they take in the gray scale output!
r, g, b =R/(inputIntensity), G/(inputIntensity), B/(inputIntensity)


#logBase = cv2.bilateralFilter(np.log10(inputIntensity).astype(np.float32),5,40,40)
#logBase = cv2.blur(np.log10(inputIntensity).astype(np.uint8),(15,15))
#logBase = np.log10(inputIntensity).astype(np.float32)
Kernel = GaussianKernelSpatial(3,0.6)
downF=1
Base = FastBilateral(inputIntensity, Kernel, downsam=downF)
inputIntensity = DownSample(inputIntensity,downF)
h,w = Base.shape
for i in range(0,h):
    for j in range(0,w):
        if Base[i][j] == 0:
            Base[i][j] = 1



#logBase = FastBilateral(np.log10(inputIntensity).astype(np.float32),Kernel)
#logBase = cv2.bilateralFilter(np.log10(inputIntensity).astype(np.float32),5,40,40)
#Base = np.power(10,logBase).astype(np.uint8)
logBase = np.log10(Base).astype(np.float32)
logDetail = np.log10(inputIntensity).astype(np.float32) - logBase
Detail = np.power(10, logDetail)




# compressionfactor and log_absolute_scale (These two require changes)
#targetContrast = math.log(5,10)
targetContrast = 1.15


minLB = np.min(logBase)

compressionFactor = targetContrast / ( np.max(logBase) - minLB)

log_absolute_scale = np.max(logBase) * compressionFactor
logOutputIntensity = logBase * compressionFactor + logDetail - log_absolute_scale
#logOutputIntensity = logBase + logDetail

b, g, r = DownSample(b, downF), DownSample(g, downF), DownSample(r, downF)
newB = b*np.power(10, logOutputIntensity)
newG = g*np.power(10, logOutputIntensity)
newR = r*np.power(10, logOutputIntensity)

MergeImg = cv2.merge([newB,newG,newR])
MergeImg = MergeImg.astype(np.float32)




cv2.imshow('before tone mapping', img)
#cv2.imshow('after tone mapping', 255-Detail.astype(np.uint8))
cv2.imshow('final', MergeImg)
time_end = time.time()
print('time cost : ', time_end - time_start, 's')
cv2.waitKey(0)