1. All images used for this experiment are stored in "original_paper_images"

2. To test the output of Bilateral filter, please run the filter.py
    (1). In this script, please check the path is correct.
    (2). Please set parameter in "sigmaColor", "sigmaSpace", and "k_size". Other wise the programing will filter an image with all pre-defined parameters. Please remember k_size should be an odd number.
3. The output of filter.py will stored in "output_image/" for gray scale images and "output_color_image" for color scale images.

4. To check the PSNR score, Please run the baseline.py
    (1), In this script, please check the path is correct.
    (2). Please set parameter in "sigmaColor", "sigmaSpace", and "k_size". Other wise the programing will filter an image with all pre-defined parameters. Please remember k_size should be an odd number.
5. The output of baseline.py will stored in "output_baseline/".
6. The PSNR will be printed directly on terninal. 