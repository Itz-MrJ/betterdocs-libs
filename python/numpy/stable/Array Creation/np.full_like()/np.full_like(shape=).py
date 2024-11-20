import numpy as np

a = np.full_like([[1, 2], [3, 4]], fill_value=[0, 8], shape=(3,2))
print(a)
'''
Output:
[[0 8]
 [0 8]
 [0 8]]
'''