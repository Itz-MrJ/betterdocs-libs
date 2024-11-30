import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = np.tril(m=matrix, k=-1)
print(result)
'''
Output:
[[0 0 0]
 [4 0 0]
 [7 8 0]]
'''