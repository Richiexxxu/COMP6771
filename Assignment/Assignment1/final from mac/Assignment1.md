# Assignment1

## Question 1. 

- a). (5 points) Explain why the discrete histogram equalization technique does not, in general, yield a flat histogram.

    ```
    ALl that histogram equalization does is remap histogram components on the intensity scale. 
    To obtain a uniform(flat) histogram would require in general that pixel intensities actually be redistributed so that there are L groups of n/L pixels with the same intensity, where L is the number of allowed discrete intensity levels and n = MN is the total number of pixels in the input image. 
    The histogram equalization method has no provisions for this type of (artificial) intensity redistribution process.
        
    ```