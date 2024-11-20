import numpy as np

# 3x2 array where each entry is i + j (row + column index)
fromfunction_array = np.fromfunction(function=lambda i, j: i + j, shape=(3, 2))
print(fromfunction_array)
'''
Output:
[[0. 1.]
 [1. 2.]
 [2. 3.]]
'''