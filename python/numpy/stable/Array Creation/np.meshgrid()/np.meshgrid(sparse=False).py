import numpy as np
x = np.array([1, 2, 3])
y = np.array([4, 5])
a, b = np.meshgrid(x, y, sparse=False)
print(a)
print(b)
'''
Output:
[[1 2 3]
 [1 2 3]]
[[4 4 4]
 [5 5 5]]
'''