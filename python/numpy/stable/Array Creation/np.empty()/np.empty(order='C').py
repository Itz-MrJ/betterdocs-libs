import numpy as np

# Create a 2x3 array
array = np.empty([2, 3], order='C')
print(array)

"""
Output: (Garbage value)
[[0. 0. 0.]
 [0. 0. 0.]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [0. 0. 0. 0. 0. 0.]