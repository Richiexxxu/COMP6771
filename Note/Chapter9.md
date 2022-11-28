# Chapter9 Morphological Image Processing
## Preview
- Mathematical morphology as a tool for extracting image components that are useful in the representation and description of region shape, such as boundaries, skeletons, and the convex hull. 


## 9.1 Preliminaries
- The language of mathematical morphology is set theory.
  - Sets in mathematical morphology represent objects in those images.
  - In binary images, the sets in question are members of the 2-D interger space $Z^2$. Where each element of a set is a tuple (2-D vector) whose coordinates are the coordinates of an object(typically foreground) pixel in the image.
  - Grayscale digital images can be represented as sets whose  components are in $Z^3$. 
  - Morphological operations are defined in terms of sets.
    - Objects 
        - sets of foreground pixels
    - structuring elements.(SE)
        - "don't care" elements, donated by $\times$. The value of that particular element in the SE does not matter.        
    - applications of morphology in image processing require that sets be embedded in rectangular arrays.
    - Reflection of a set(structuring element) $B$ is $\widehat{B}$. 
      - $$\widehat{B} = \{w| w = -b, for{\,}b \in B\}$$
        - In this equation, $B$ is a set of points in 2-D, then $\widehat{B}$ is the set of points in $B$ whose $(x, y)$ coordinates have been replaced by $(-x, -y)$.
    - Translationof a set $B$ by point $z = (z_1, z_1)$, denoted $(B)_Z$,is :
      - $$(B)_z = \{c | c = b+z, for{\,}b\in B\}$$ 
        - In this equation, $B$ is a st of pixels in 2-D, then $(B)_Z$ is the set of pixels in $B$ whose $(x, y)$ coordinates have been replaced by $(x+z_1, y+z_2)$.
      - This construct is used to translate a structuring element over an image, and each location perform a set operation between the structuring element and the area of the image directly under it.
## 9.2 erosion and dilation

## 9.3