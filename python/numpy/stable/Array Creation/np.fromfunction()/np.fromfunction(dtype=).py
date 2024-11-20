import numpy as np

# 1x5 array where each entry is i + j (row + column index)
fromfunction_array = np.fromfunction(function=lambda i, j: i + j, shape=(1, 5), dtype=np.int32)
print(fromfunction_array)
'''
Output:
[[0 1 2 3 4]]
'''