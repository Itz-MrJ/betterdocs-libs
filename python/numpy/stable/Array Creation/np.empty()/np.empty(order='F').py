import numpy as np

# Create a 2x3 array
array = np.empty([2, 3], order='F')
print(array)

"""
Output: (Garbage value)
[[1. 1. 1.]
 [1. 1. 1.]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1. 1. 1. 1. 1. 1.]