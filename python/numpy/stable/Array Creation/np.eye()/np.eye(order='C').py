import numpy as np

# Create a 3x3 array
array = np.eye(3, order='C')
print(array)

"""
Output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1. 0. 0. 0. 1. 0. 0. 0. 1.]