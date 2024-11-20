import numpy as np

# Create an empty_like 2x2 array
a = np.array([[10, 20], [15, 5]])
array = np.empty_like(prototype=a, order='F')
print(array)

"""
Output: (Garbage Values)
[[ 1 15]
 [ 2  5]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [ 1  2 15  5]