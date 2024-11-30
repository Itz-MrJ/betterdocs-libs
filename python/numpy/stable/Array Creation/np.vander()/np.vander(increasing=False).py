import numpy as np
result = np.vander(x=[4, 2, 3], N=4, increasing=False)
print(result)
'''
Output:
[[64 16  4  1]
 [ 8  4  2  1]
 [27  9  3  1]]
'''