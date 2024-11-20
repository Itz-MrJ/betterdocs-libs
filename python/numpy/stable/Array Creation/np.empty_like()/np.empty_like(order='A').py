import numpy as np

# Create an empty_like 2x2 array
a = np.array([[10, 0], [15, 5]])
array = np.empty_like(prototype=a, order='A')
print(array)

"""
Output: (Garbage Values)
[[10 20]
 [15  5]]
"""

# Ravel with K-order
ravel_c = array.ravel(order='K')
print(ravel_c)  # Output: [10 20 15  5]