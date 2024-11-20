import numpy as np

a = np.array([[1, 2], [3, 4]])
arr = np.full_like(a=a, fill_value=20)
print(arr)
'''
Output:
[[20 20]
 [20 20]]
'''