# Bilateral Filtering for Gray and Color Images
- Bilateral filtering: smoothing images while preserving edges, by means of a nonlinear combination of nearby image values.
- Bilateral Filtering combines gray levels or colors based on both their geometric closeness and their photometric similarity, and prefers near values to distant values in both domain and range.1
- Advantages:
  - The method is noniterative, local and simple.
  - Bilateral filter can enforce the perceptual metric underlying the CIE-Lab color space, and smooth colors and preserve edges in a way that is tuned to human perception. 
  - Bilateral filtering produces no phantom colors along edges in color images, and reduce phantom colors where they appear in the original image.

## Introduction
- In this paper, we propose a nonterative scheme for edge preserving that is noniterative and simple. This scheme could be implemented by a single layer of neuron-like devices.
- This scheme allows explicit enforcement of any desired notion of photometric distance: This is important for filtering color images. If the three bands of color images are filtered separately from one another, colors are corrupted close to image edges.
- Bilateral filters can operate on the three bands at once.
- The idea: two pixels can be close to one another, occupy nearby spatial location, or they can be similar to one another, that is, have nearby values, possibly in a perceptually meaningful fashion.
  - The Bilateral filter define range filter, which averages image values with weights that decay with dissimilarity.
  - Range filters are nonlinear because their weights deped on image intensity or color.
  - Spatial locality is still an essential notion, and will not distort an image's color map.

