import numpy as np


sigma = 3.5
# kernal = [int(sigma * 7) if int(sigma * 7) /2 != 0 else int(sigma * 7) +1][0]
# print(np.trunc(sigma * 7) /2)
# if np.trunc(sigma * 7) /2 == 0:
#     kernal = np.trunc(sigma * 7)
# print(kernal)
#

def round_up_to_odd(f):
    return np.ceil(f) // 2 * 2 + 1

print(round_up_to_odd(3.5 * 7))

print(int(25.5))