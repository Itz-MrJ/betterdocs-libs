import numpy as np

# 3x3 array where each entry is i + j (row + column index)
fromfunction_array = np.fromfunction(function=lambda i, j: i + j, shape=(3, 3))
print(fromfunction_array)
'''
Output:
[[0. 1. 2.]
 [1. 2. 3.]
 [2. 3. 4.]]
 '''