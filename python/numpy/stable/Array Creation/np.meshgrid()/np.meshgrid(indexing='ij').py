import numpy as np
x = np.array([1, 2, 3])
y = np.array([4, 5])
a, b = np.meshgrid(x, y, indexing='ij')
print(a)
print(b)
'''
Output:
[[1 1]
 [2 2]
 [3 3]]
[[4 5]
 [4 5]
 [4 5]]
'''