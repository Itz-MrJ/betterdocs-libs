import numpy as np

# Create a 2x3 array
array = np.asarray([[1, 2, 3], [4, 5, 6]], order='C')
print(array)

"""
Output:
[[1 2 3]
 [4 5 6]]
"""

# Ravel with C-order (row-major)
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1, 2, 3, 4, 5, 6]