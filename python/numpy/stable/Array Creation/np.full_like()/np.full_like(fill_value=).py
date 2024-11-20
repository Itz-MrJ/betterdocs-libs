import numpy as np

a = np.array([[1, 2], [3, 4]])
full_arr = np.full_like(a=a, fill_value=[1, 0])
print(full_arr)
'''
Output:
[[1 0]
 [1 0]]
'''