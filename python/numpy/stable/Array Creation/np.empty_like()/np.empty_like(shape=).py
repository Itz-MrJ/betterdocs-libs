import numpy as np

a = np.empty_like([[1, 2], [3, 4]], shape=(2,1))
print(a)  # Values are uninitialized
'''
Output:
[[4575657222473777152]
 [4575657222473777152]]
'''