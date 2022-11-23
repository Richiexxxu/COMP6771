# Bilateral Filtering for Gray and Color Images
- Bilateral filtering: smoothing images while preserving edges, by means of a nonlinear combination of nearby image values.
- Bilateral Filtering combines gray levels or colors based on both their geometric closeness and their photometric similarity, and prefers near values to distant values in both domain and range.1
- Advantages:
  - The method is noniterative, local and simple.
  - Bilateral filter can enforce the perceptual metric underlying the CIE-Lab color space, and smooth colors and preserve edges in a way that is tuned to human perception. 
  - Bilateral filtering produces no phantom colors along edges in color images, and reduce phantom colors where they appear in the original image.

## 1. Introduction
- In this paper, we propose a nonterative scheme for edge preserving that is noniterative and simple. This scheme could be implemented by a single layer of neuron-like devices.
- This scheme allows explicit enforcement of any desired notion of photometric distance: This is important for filtering color images. If the three bands of color images are filtered separately from one another, colors are corrupted close to image edges.
- Bilateral filters can operate on the three bands at once.
- The idea: two pixels can be close to one another, occupy nearby spatial location, or they can be similar to one another, that is, have nearby values, possibly in a perceptually meaningful fashion.
  - The Bilateral filter define range filter, which averages image values with weights that decay with dissimilarity.
  - Range filters are nonlinear because their weights deped on image intensity or color.
  - Spatial locality is still an essential notion, and will not distort an image's color map.

## 2. The Idea

- Define A low-pass domain filter applied to image $f(x)$:
  - $$h(x) = k_{d}^{-1}(x) \iint f(\xi)c(\xi, x) d\xi \tag{2.1}$$
    - $c(\xi, x)$ measures the geometric closeness between the neighborhood center $x$ and a nearyby point $\xi$. 
  - If low-pass filter is to preserve the dc component of low-pass signals, we obtain:
    - $$ k_{d}(x) = \iint c(\xi, x) d\xi \tag{2.2}$$
  - If the filter is shift-invariant, $c(\xi, x)$ is only a function of the vector dfference $\xi -x$ and $k_{x}$ is constant.
- Defined Range filtering:
  - $$h(x) = k_{x}^{-1}(x) \iint f(\xi)s(f(\xi), f(x)) d\xi \tag{2.3}$$
    - $s(f(\xi),f(x))$ measures the photometric similarity between the pixel at the neighborhood center $x$ and that of a nearby point $\xi$.
    -  The normalization constant $(2.2)$ is replaced by:
       -  $$ k_{r}(x) = \iint s(f(\xi), f(x))d\xi \tag{2.4}$$
          -  The normalization for the similarity function s depends on the image $f$.
          -  We say that the similarity function $s$ is unbiased if it depends only on the difference $f(\xi) - f(x)$.
 -  Bilateral filtering: Combine domain and range filtering, thereby enforcing both geometric and photometric locality.
    -  Combined filtering :
       -  $$ h(x) = k^{-1}(x) \iint f(\xi)c(\xi, x)s(f(\xi), f(x))d\xi \tag{2.5}$$
       - Normalization:
         - $$k(x) = \iint c(\xi, x) s(f(\xi), f(x))d\xi$$
       - It replaces the pixel value at $x$ with an average of similar and nearby pixel values.
       - In smooth regions, $k^{-1}  = 1$.
### 2.1 Example: the Gaussian Case
- shift-invariant Gaussian filtering: a simpel and important case of bilateral filtering, both the closeness function $c(\xi, x)$ and the similarity function $s(\phi, f)$ are Gaussian function of the Euclidean distance between their arguments.
  - Define $c$ : 
    - $$c(\xi, x) = e^{-\frac{1}{2}(\frac{d(\xi, x)}{\sigma_{d}})^2}$$
      - where, $d(\xi, x) = d(\xi - x) = ||\xi - x||$ is the Euclidean distance between $\xi$ and $x$.
    - Geometric spread $\sigma_d$ in the domainis chosen based on the desired amount of low-pass filtering. 
      - large blurs more, combines values from more distant image locations.

  - Define $s$ : 
    - $$s(\xi, x) = e^{-\frac{1}{2}(\frac{\delta(f(\xi), f(x))}{\sigma_{r}})^{2}}$$
      - where, $\delta(\phi, f) = \delta(\phi - f) = ||\phi - f||$ is a suitable measure of distance between the two intensity value $\phi$ and f.
      - In the scalar case, this may be simply the absolute difference of the pixel difference or, since noise increases with image intensity, an intensity-dependent version of it.
      - Photometric spread $\sigma_r$ in the image range is set to achieve the desired amount of combination of pixel values. 
## 3. Range versus Bilateral Filtering
- Main point: Range filtering by itself merely modifies the gray map of the image it it applied to.

## 4. Experiments with black-and-White Images.
