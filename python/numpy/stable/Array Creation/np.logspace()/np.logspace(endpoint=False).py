import numpy as np
arr = np.logspace(start=0, stop=1, num=5, endpoint=False)
# Only 'start' is included & 'stop' is excluded
print(arr)
'''
Output:
[1.         1.58489319 2.51188643 3.98107171 6.30957344]
'''