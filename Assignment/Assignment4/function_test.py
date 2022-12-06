import numpy as np

edge_height = 10
edge_width = 10
num_thetas = 10
num_rhos = 10
d = np.sqrt(np.square(edge_height) + np.square(edge_width))
dtheta = 180 / num_thetas
drho = (2 * d) / num_rhos
#
thetas = np.arange(0, 180, step=dtheta)
rhos = np.arange(-d, d, step=drho)
#
cos_thetas = np.cos(np.deg2rad(thetas))
sin_thetas = np.sin(np.deg2rad(thetas))

result = 0