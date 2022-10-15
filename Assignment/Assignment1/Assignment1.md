# Assignment1

## Question 1
(a) Explain why the discrete histogram equalization technique does not, in general, yield a flat histogram.

1. From Book p127
   Histogram is an approximation to a PDF, and no new allowed intensity levels are created in the process.
2. All that histogram equalization does is remap histogram components on the in-tensity scale. To obtain a uniform (flat) histogram would require in general that pixel intensities actually be redistributed so that there are L groups of n/L pixels with the same intensity, where L is the number of allowed discrete intensity levels and n=MN is the total number of pixels in the input image. The histograme qualization method has no provisions for this type of (artificial) intensity redis-tribution process.
3. Because in global histogram equalization, all pixels with the same value are mapped to the same value. Since we cannot split pixels of the same value tobe mapped to different ones, complete flat histograms are not achievable in general. All pixels having the same value in the original image are mapped to the same value after global equalization.





