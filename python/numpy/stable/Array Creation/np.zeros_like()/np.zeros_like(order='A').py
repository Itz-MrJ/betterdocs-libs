import numpy as np

# Create a zeros_like 2x2 array
a = np.array([[1, 2], [2, 5]])
array = np.zeros_like(a=a, order='A')
print(array)

"""
Output:
[[0 0]
 [0 0]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [0 0 0 0]