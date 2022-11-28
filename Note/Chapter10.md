# Chapter 10

- Most of the segmentation algorithms in this chapter are based on one of two basic properties of image intensity values: discontinuity and and similarity.
- First approach: partition an image into region based on abrupt changes in in tensity, such as edges.
- Second approaches: partitioning an image into regions that are similar according to a set of predefined criteria.


## 10.1 Fundamentals
- $R$ represnet the entire spatial region occupied by an image, and $R_1, R_2, R_3... R_n$ are $n$ subregions of R.
  - $\stackrel{n}{\underset{i=1}{\bigcup}}R_i= R$  
    This indicates that the segmentation must be complete, in the sense that every pixel must be in a region. 
  - $R_i$ is a connected set, for i = 0, 1, 2, ..., n.  
    Points in a region be coneected in some predefined sense(e.g., the points must be 8-connected).
  - $R_i \bigcap R_j = \emptyset$ for all $i$ and $j$, $i \neq j$.  
    Region must be disjoint.  
  - $Q(R_i) = TRUE$ for $i = 1,2,3,...,n.  
    This equation deals with the properties that must be satisfied by the pixels in a segmented region, e.g., $Q(R_i) = TRUE$ if all pixels in $R_i$ have the same intensity.
  - $Q(R_i\bigcup R_j) = FALSE$ for any adjacent regions $R_i$ and $R_j$.  
    This indicates that two adjacent regions $R_i$ and $R_j$ must be different in the sense of predicate $Q$.
- Edge-based segmentation: 
  - Discontinuity
  - Assuming that boundaries of regions are sufficiently different from each other, and from the background, to allow boundary detection based on local discontinuities in intensity. 
- Region-based segmentation:
  - Similarity
  - Based on partitioning an image into regions that are similar according to a set of predefined criteria.

## 10.2 Point, Line, And edge detection
- Edge pixels are pixels at which the intensity of an image changes abruptly, and edges are sets ofconnected edge pixels. Edge detetors are local image processing tools desiged to detect edge pixels. 
- A line may be viewed as a (typically) thin edge segment in which the intensity of the background on either side of the line is either much higher or much lower than the intensity of the line pixels. 
- Isolated point : foreground (background) pixel surrounded by background(foreground) pixels.

### 10.2.1 Background
- Abrupt, local changes in intensity can be detected using derivatives.
- Finite defferences.
- First derivative requirement: 
  - must be zero in areas of constant intensity
  - mst be nonzero at the onset of an intensity step or ramp
  - must be nonzero at points along an intensity ramp
- Second derivative
  - Must be zero in areas of constant intensity
  - Must be nonzero at the onset and end of an intensity step or ramp
  - Must be zero along intensity ramps
### 10.2.2 Detection of Isolated points 
### 10.2.3 Line detection
### 10.2.4 Edge models
### 10.2.5 Basic Edge Detection
#### The Image gradient and Its properties
#### Gradient Operators
#### Combining the Gradient with Thresholding

### More Advanced Techniques for edge detection
#### The Marr-Hildreth Edge Detector
#### The Canny Edge Detector

### 10.2.6 Linking Edge Points
- Edge detection should yield sets of pixels lying only on edges.
  - But seldom due to the noise, nonuniform illumination, discontinuities in intensity values.
- Link algorithms: designed to assemble edge pixels into meaningful edges and/or region boundaries.
  - edge points in a local region ( 3 x 3 neighborhood)
  - global approach that works with an entire edge map

#### Local Processing
- Analyze the characteristics of pixels in a small neighborhood about every point $(x, y)$ that has been declared an edge point.
- similar linked points, forming an edge of pixels that share common properties according to the specified criteria.
- principle properties used for establishing similarity of edge pixels:
  - (1) the strength(magnitude).
  - (2)the direction of the gradient vector
- Process:
  - 1. compute the gradient magnitude and angle arrays, $M(x, y)$ and $\alpha (x, y)$, of the input image, $f(x, y)$.
  - 2. Form a binary image, $g(x, y)$, whose value at any point $(x, y)$ is given by:
    $$g(x,y)=
      \begin{cases}
      1, &if M(x, y) \gt T_M And \alpha(x, y) = A \pm T_A\\
      0. &otherwise
      \end{cases}$$
  - 3. Scan the rows of $g$ and fill(set to 1) all gaps (sets of 0's) in each row that do not exceed a specified length, $L$.
  - 4. To detect gaps in any other direction, $\thetha$, retate $g$ by this angle and apply the horizontal scanning procedue in step 3. Rorate the result back by $-\theta$.

#### Global Processing Using the Hough Trasform
- Hough Transform.
- 


### 10.3 Thresholding
- Image thresholding enjoys a central position in applications of image segmentation.

#### 10.3.1 Foundation
##### The basic of Internsity thresholding
- Suppose image $f(x, y)$ composed of light objects on a dark background, then object and background pixels have intensity balues grouped into two dominant modes.
  - $$ g(x, y)= \begin{cases}1 & if&f(x, y) > T\\0 &if &f(x, y) \leq T \end{cases}$$
    - The process given in this equation is refered to as gloval thresholding.
    - When the value of T changes over an image, is variable thresholding.
      - "local thresholding" and "regional threshoding" also denote variable thresholding in which the value of $T$ at any point $(x, y)$ in an image depends on properties of a neighbord of $(x, y)$.
  - $$ g(x, y) = \begin{cases}a & if&f(x, y) \gt T_2\\b &if&T_1 \lt f(x, y) \leq T_2\\ c & if&f(x,y) \leq T_1 \end{cases}$$
    - Where $a$, $b$ and $c$ are any three distinct intensity values.
  - The key factors affecting the properties of the valley(s)(the valley(s) separating the histogram modes):
    - the separation between peaks(the further apart the peaks are, the better the chances of separating the modes)
    - the noise content in the image(the modes broaden as noise increases)
    - the relative sises of objects and background
    - the uniformity of the illumination source
    - the uniformity of the reflectance properties of the image.


##### the Role of Noise in Image Thresholding
- depends the "spike" modes that the histogram model contains.
  
##### The role of illumination and Reflectance in Image Thresholding
- Three basic approaches to the problem:
  - Correct the shading pattern directly.
  - Correct the gloval shading pattern via processing using.
  - "work around" nonuniformities using variable thresholidng.

##### Basic Global Thresholding
- Algorithm of estimating the thresholding value steps:
  - 1. Select an initial estimate for the global threshold $T$.
  - 2. Segment the image using $T$ in the Equation above. Thie will produce two groups of pixels: $G_1$, consisting of pixels with intensity values $\gt T$; the $G_2$, consisting of pixels with values $\leq T$.
  - 3. Compute the average (mean) intensity values $m_1$ and $m_2$ for the pixels in $G_1$ and $G_2$, respectively.   
  - 4. Compute a new threshold value midway between $M_1$ and $m_2$:
        $$T = \frac{1}{2}(m_1 + m_2)$$
  - 5. Repeat Setps 2 through 4 until the difference between values of $T$ in successive interations is smaller than a predefined value, $\Delta T$.
   

##### Optimum Gloval Thresholding using OTSU'S Method

- A statistical-decision theory problem whose objective is to minimize the average error incurred in assigning pixels to two or more groups(classes).
- Otsu's method:
  - The method is optimum in the sense that it maximizes the between-class variance, a measure used in statistical discriminant analysis. 
    - properly thresholded classed should be distinct with respect to the intensity values of their pixels and, conversely, that a threshold giving the best reparation between classes in terms of their intensity values would be the best(optimum) threshold.
    - 
