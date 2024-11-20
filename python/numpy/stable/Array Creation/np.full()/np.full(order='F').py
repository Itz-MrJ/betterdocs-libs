import numpy as np

# Create a 3x3 array
array = np.full((3, 3),fill_value=[[1], [2], [3]], order='F')
print(array)

"""
Output:
[[1 1 1]
 [2 2 2]
 [3 3 3]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1 2 3 1 2 3 1 2 3]