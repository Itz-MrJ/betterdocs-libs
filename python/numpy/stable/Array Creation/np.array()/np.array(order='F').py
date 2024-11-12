import numpy as np

# Create a 2x3 array
array = np.array([[1, 2, 3], [4, 5, 6]], order='F')
print(array)

"""
Output:
[[1 2 3]
 [4 5 6]]
"""

# Ravel with F-order (Column-major)
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1, 4, 2, 5, 3, 6]