import numpy as np

arr = np.geomspace([1,2], [4,5], num=5, axis=-1)
print(arr)
'''
Output: 
[[1.         1.41421356 2.         2.82842712 4.        ]
 [2.         2.51486686 3.16227766 3.97635364 5.        ]]
'''