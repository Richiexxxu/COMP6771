# Bilateral Filtering for Gray and Color Images
- Bilateral filtering: smoothing images while preserving edges, by means of a nonlinear combination of nearby image values.
- Bilateral Filtering combines gray levels or colors based on both their geometric closeness and their photometric similarity, and prefers near values to distant values in both domain and range.1
- Advantages:
  - The method is noniterative, local and simple.
  - Bilateral filter can enforce the perceptual metric underlying the CIE-Lab color space, and smooth colors and preserve edges in a way that is tuned to human perception. 
  - Bilateral filtering produces no phantom colors along edges in color images, and reduce phantom colors where they appear in the original image.

## Introdu