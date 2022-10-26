# Chapter 4



## Section 4.1
 - computational advantages of filtering in the frequency versus the spatial doman:
   - Square images and kernals, of sizes $M \times M$ and $m \times m$, respectively. 
   - The computational advantage (as a function of kernel size) of filtering one such image with the FFT as opposed to using a non-separable kernel is :
        $$C_n(m) = \frac{M^2 m^2}{2 M^2 \log_{2}^{M^2}}
                     = \frac{m^2}{4 \log_{2}{M}}$$
        and separable,
        $$C_s(m) = \frac{2 M^2m}{2M^2\log_{2}{M^2}} = \frac{m}{2\log_{2}^{M}}$$
        In this case, when $C(m) > 1$ the advantege (in terms of computations) belongs to the FFT approach; otherwise the advantage favors spatial filtering.  
## 4.2 Preliminary concepts
 - 1. Complex Numbers
   - The complex number, C and its conjugate $C^*$ as:
        $$C = R + jI  \iff C^* = R - jI$$
        - R : Real number, real part.
        - I: real number, imaginary part.
        - $j = \sqrt{-1}$
        - Real numbers are a subset of complex numbers in which $I = 0$. 
   - Complex plane:
     - Complex numbers can be viewed geometrically as points $(R, I)$ on a plane (complex plane)
       - x-axis (abscissa) $\rightarrow$ real axis (R).
       - y-axis (ordinate) $\rightarrow$ imaginary axis(I).
   - Polar coordinates: 
     - Using polar coordinates to represent complex numbers.
     -  $C = |C|(cos\theta + jsin\theta)$, where $|c| = \sqrt{R^2 + I^2}$m, is the length of the vector extending from the origin of the complex plane to point $(R, I)$, and $\theta$ is the angle between the vector and the real axis. 
   - Complex function:
     - Euler's formula:
       $$e^{j\theta} = cos\theta + jsin\theta$$
     - So the representation of complex numbers in polar coordinates: $C = |C|e^{j\theta}$. 
     - Suppose, $F(\mu)$, of a real variable $\mu$, can be expressed as the sum $F(\mu) = R(\mu) + jI(\mu)$, where $R(\mu)$ and $I(\mu)$ are the real and imaginary component functions of $F(\mu)$, also, the complex conjugate is $F^*(\mu) = R(\mu) - jI(\mu)$, the magnitude is $|F(\mu)| = [R*\mu)^2 + I(\mu)^2]^{1/2}$. The angle is $\theta(\mu) = arctan[I(\mu)/R(\mu)]$.
 - 2. Fourier Series
   - 
  







## 4.3 Sample and Fourier Transform of Sampled Functions. 

 - A continuous function, $f(t)$, and we wish to somaple at uniform intervals ($\Delta T$) of the independent variable $t$. 
 - We assume that the function extend from $- \infty$ to $- \infty$ with respect to t. One way to model sampling is to multiply $f(t)$ by a sampling function equal to a train of impulses $\Delta T$ 
 
 