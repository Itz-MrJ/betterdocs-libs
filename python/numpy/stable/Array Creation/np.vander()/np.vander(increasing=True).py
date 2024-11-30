import numpy as np
result = np.vander(x=[4, 2, 3], N=4, increasing=True)
print(result)
'''
Output:
[[ 1  4 16 64]
 [ 1  2  4  8]
 [ 1  3  9 27]]
'''