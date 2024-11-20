import numpy as np

a = np.array([[1, 2], [3, 4]])
arr = np.zeros_like(a, dtype=np.float32)
print(arr)
'''
Output:
[[0. 0.]
 [0. 0.]]
'''