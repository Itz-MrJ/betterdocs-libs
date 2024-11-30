import numpy as np

arr = np.geomspace([1,2], [4,5], num=5, axis=0)
print(arr)
'''
Output: 
[[1.         2.        ]
 [1.41421356 2.51486686]
 [2.         3.16227766]
 [2.82842712 3.97635364]
 [4.         5.        ]]
'''