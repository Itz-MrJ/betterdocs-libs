import numpy as np

# Create a ones_like 2x2 array
a = np.array([[1, 2], [2, 5]])
array = np.ones_like(a=a, order='A')
print(array)

"""
Output:
[[1 1]
 [1 1]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [1 1 1 1]