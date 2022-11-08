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