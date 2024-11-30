import numpy as np
result = np.diagflat(v=[[1], [2], [3]], k=0)
print(result)
'''
Output:
[[1 0 0]
 [0 2 0]
 [0 0 3]]
'''