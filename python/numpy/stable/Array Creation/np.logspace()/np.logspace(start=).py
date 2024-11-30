import numpy as np
arr = np.logspace(start=0, stop=2, num=5, base=10.0)
# Both 'start' & 'stop' are included as endpoint=True
print(arr)
'''
Output:
[  1.           3.16227766  10.          31.6227766  100.        ]
'''