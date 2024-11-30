import numpy as np
x = np.array([1, 2, 3])
y = np.array([4, 5])
a, b = np.meshgrid(x, y, sparse=True)
print(a)
print(b)
'''
Output:
[[1 2 3]]
[[4]
 [5]]
'''