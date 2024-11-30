import numpy as np
arr = np.logspace(start=0, stop=4, num=5, dtype=np.int32)
# Both 'start' & 'stop' are included
print(arr)
'''
Output:
[    1    10   100  1000 10000]
'''