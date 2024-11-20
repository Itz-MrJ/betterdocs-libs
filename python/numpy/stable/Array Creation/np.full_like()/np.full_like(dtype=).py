import numpy as np

a = np.array([[1, 2], [3, 4]])
full_arr = np.full_like(a=a, fill_value=0, dtype=np.float32)
print(full_arr)
'''
Output:
[[0. 0.]
 [0. 0.]]
'''