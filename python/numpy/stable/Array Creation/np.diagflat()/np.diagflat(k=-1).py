import numpy as np
result = np.diagflat(v=[[1], [2], [3]], k=-1)
print(result)
'''
Output:
[[0 0 0 0]
 [1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]]
'''