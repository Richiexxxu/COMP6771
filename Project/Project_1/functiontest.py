import numpy as np
import cv2


kernel_size = 5
half_kernel_size = int((kernel_size - 1) /2)

[x, y] = np.meshgrid(range(-half_kernel_size, half_kernel_size +1), range(-half_kernel_size, half_kernel_size + 1))

print((x, y))

center_x, center_y = 0, 0

distance = (center_x - x) **2 + (center_y - y) **2
print(distance)

center_x_a, center_y_a = half_kernel_size, half_kernel_size
[x_a, y_a] = np.meshgrid(range(kernel_size), range(kernel_size))
distance_a = (center_x_a - x_a) **2 + (center_y_a - y_a) ** 2
print(distance_a)