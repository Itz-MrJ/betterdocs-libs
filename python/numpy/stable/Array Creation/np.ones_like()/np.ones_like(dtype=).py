import numpy as np

a = np.array([[1, 2], [3, 4]])
ones_arr = np.ones_like(a, dtype=np.float32)
print(ones_arr)
'''
Output:
[[1. 1.]
 [1. 1.]]
'''