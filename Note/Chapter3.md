# Intensity Transformations and Spatial Filtering

## 3.1 Background
Spatial domain

## 3.2 Some Basic Intensity Transformation Functions
 - $g(x, y) = T[f(x, y)]$
    Where $f(x, y)$ --> input image; 
    &emsp; $g(x, y)$ --> output image; 
    &emsp; $T$ --> operator on $f$ defined over a neighborhood of point $(x, y)$.

## 3.3 Histogram Processing 

### 3.3.1 Histogram Equalization
- 1. Histogram Normalized.
  The histogram of a digital image with intensity levels in the range $[0, L-1]$, is a discrete function $h(r_k) = n_k$, where $r_k$ is the $k$th intensity value and $n_k$ is the number of pixels in the image with intensity $r_k$.
  It is common practice to normalize a histogram by dividing each of its components by the total number of pixels in the image, denoted by the product $MN$, where, as usual, $M$ and $N$ are the row and column dimensions of the image. 
  Normalized histogram is given by $p(r_k) = r_k/MN$, for $k = 0, 1 , 2, ..., L-1$.  
  Intuitively, it is reasonable to conclude that an image whose pixels tend to occupy the entire range of possible intensity levels and, in addition, tend to be distributed uniformly, will have an appearance of high contrast and will exhibit a large variety of gray tones. 

### 3.3.1 Histogram Equalization
- Suppose: a moment continuous intensity values, 
  Variable $r$ denote the intensities of an image to be processed.
  $r \in  [0, L-1]$, where:
    $$
    \left\{ 
    \begin{matrix}
    r = 0, black \\
    r = L-1, white  \\
    \end{matrix}
    \right.
    $$



  For $r$ satisgying these conditions, we focus attention on transformations(intensity mappings) of the form:
  $$s = T(r), 0 \leq r \leq L-1 $$
  That produce an output intensity level s for every pixel in the input image haing intensity r. 
  Assume: 
    (a) $T(r)$ is a monotonically increasing function in the interval $0 \leq r \leq L-1$
    (b) $0 \leq T(r) \leq L-1$ for $0 \leq r \leq L-1$.
  In some formulation to be discussed later, we use the inverse:
  $$ r = T^{-1}(s), 0 \leq s \leq L-1 $$
    In this case, we change condition (a) to:
    (a') $T(r)$ is a strictly monotonically increasing function in the interval $0 \leq r \leq L-1$.
- The intensity levels in an image may by viewed as random variables in the interval $[0, L-1]$. We will use Probabilty Density Function (PDF in later). 
  Let $p_r(r)$ and $p_s(s)$ denote the PDFs of $r$ and $s$ respectively, where the subscripts on $p$ are used to indicate the $p_r$ and $p_s$ are different functions in general.  
  Probabilty theory is: if $p_r(r)$ and $T(r)$ are known, and $T(r)$ is continuous and differentiable over the range of values of interest, then the PDF of the transformed(mapped) variable $s$ can be obtained using the simple formula:
  $$ p_s(s) = p_r(r) \vert\frac{dr}{ds} \vert $$
  The transformation function is:
  $$ s = T(r)  = (L-1)\int_0^r p_r(w)dw $$
  where, w is a dumy variable of integration. The right side of this equation is recognized as the comulative distribution function(CDF) of random variable $r$.
- To find $p_s(s)$,
  First is the $\vert \frac{dr}{ds} \vert$:
  $$ \frac{ds}{dr} = \frac{dT(r)}{dr} \\\\ 
  = (L-1) \frac{d}{dr}[\int_0^r p_r(w)dw]\\
  = (L-1)p_r(r) $$
  $\therefore$ 
  $$ p_s(s) = p_r(r) \vert \frac{dr}{ds} \vert \\
   = p_r(r) \vert \frac{1}{(L-1)p_r(r)} \vert \\
   = \frac{1}{L - 1} , 0 \leq s \leq L-1 $$
  $\therefore$ $p_s(s)$ is a uniform probability density function. 
- for discrete values, we deal with probabilities(histogram valeus) and summations instead of probability density functions and integrals. So, the probability of occurrence of intensity level $r_f$ in a digital image is:
  $$ p_r(r_k) = \frac{n_k}{MN}, k = 0, 1, 2,..., L-1 $$
  Where, $MN$ is the total number of pixels in the image, $n_k$ is the number of pixels that have intensity $r_k$, and $L$ is the number of possible intensity levles in the image. 
  $\therefore$ The descrete form of the tranfformation is:
  $$ s_k = T(r_k) = (L-1) \sum_{j=0}^k n_j , k =0, 1, 2, ...,L-1 $$
  



### 3.3.2 Histogram Matching (Specificaton)
- 1. Generate a processed image that has a specified histogram is called histogram matching or histogram specification.
     continuous intensityes $r$ and $z$ (considered continous random variable), let let $p_r(r)$ and $p_z(z)$ denote their corresponding continuous probability density functions.
     $r$ is the input intensity levels images.
     $z$ is the output intensity levels images.
     We can estinate $p_r(r)$ from the given input image, while $p_z(z)$ is the specifed probability density function that we wish the output image to have. 
     Let s be a random rariable with the property:
     $$ s = T(r) = (L-1) \int_0^r p_r(w)dw $$
     where, w is a dummy variable of intergration. 
     Next, we define a random raviable $z$ with the property:
     $$ G(z) = (L-1) \int_0^z p_z(t)dt = s $$

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