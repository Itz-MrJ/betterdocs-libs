import numpy as np

# Create a full_like 2x2 array
a = np.array([[1, 2], [2, 5]])
array = np.full_like(a=a, fill_value=10, order='F')
print(array)

"""
Output:
[[10 10]
 [10 10]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [10 10 10 10]