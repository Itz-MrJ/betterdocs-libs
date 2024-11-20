import numpy as np

a = np.array([[1, 2], [3, 4]])
empty_arr = np.empty_like(a, dtype=np.float32)
print(empty_arr)  # Values are uninitialized
'''
Output: (Garbage Values)
[[ 1.28442770e+07 -7.59295479e-38]
 [ 1.06929976e-04  4.41717302e-41]]
'''