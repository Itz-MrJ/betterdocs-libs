import numpy as np

# Create a 2x3 array
array = np.zeros([2, 3], order='C')
print(array)

"""
Output:
[[0. 0. 0.]
 [0. 0. 0.]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [0. 0. 0. 0. 0. 0.]