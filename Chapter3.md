## 3.4 Fundamentals of Spatial Filtering

- Define : Filter.
    "Filtering" refer to accepting(passing) or rejecting certain frequency components.  

### The Mechanics of Spatial Filtering
1. a spatial filter
   - (a). A neighborhood, (typically a small rectangle)
   - (b). A pre-defined operation taht is performed on the image pixels encompassed by the neighborhood .


## 3.5 Smoothing Spatial Filters
 - Smoothing filters are used for blurring and for noise reduction. 
 - Used in preprocessing tasks: removal of small details from an image prior to (large) object extraction, brideing of smal gaps in lines or curves. 

### 3.5.1 Smoothing Linear Filters
 - Averaging filters (lowpass filters): The output of a smoothing, linear spatial filter is simply the average of the pixels contained in the neighborhood of the filter mask.   
 - Idea of Smoothing filters: reduce sharp 
 - A major use of averaging filters is in the reduction of "irrelevant" detail in an image. 
 - Filter mask:
   - Standard average: 
        $$ R = 1/MN \sum_{i = 1}^{MN} z_i $$
     - Instead of being 1/MN, the coefficients of the filter are al 1s. The idea here is that it is computationally more efficient to have coefficients valued 1. 
     - An $m * n$ mask would have a normalizeing constant equal to $1/mn$.
     - box filter: all coefficients are equal.
   - Weighted average: terminology used to indicate that pixels are multiplied by different coefficients, thus giving more importance (weight) to some pixels at the expense of others. 
   - The general implementation for filtering an $M * N$ image with a weighted averagng filter of size $m * n$( $m$ and $n$ odd) is:
        $$ g(x, y) = \frac{\sum_{s = -a}^a \sum_{t = -b}^b w(s,t) f(x+s, y+t)}{\sum_{s = -a}^a \sum_{t = -b}^b w(s,t)}$$
   - An important application of spatial averaging is to blur an image for the purpose of getting a gross representation of objects of interest. The size of the mask established the relative size of the objects that will be blended with the background. 

### 3.5.2 Order-statistic (Nonlinear) Filters
- Order-statistic filters: 
  - nonlinear spatial filters
  - The response is based on ordering (ranking) the pixels contained in the image are encompassed by the filter, and the replacing the value of the ceter pixel with the value determined by the ranking result. 
    - best-known: median filter --> replace replaces the value of a pixel by the median of the intensity values in the neighborhood of that pixel (The original value of the pixel is included in the computation of the median).
    - Median filter can provide excellent noise-reduction capabilities, less blurring than linear smoothing filters of similar size. 
    - effective in the presence of impulse noise (salt-and pepper noise).  
    - Median filters will eliminate isolated clusters. larger clusters are affected considerable less.

## 3.6 Sharpening Spatial Filters
- The principal objective: highlight transitions in intensity. 
- spatial differentiation

### 3.6.1 Fundation