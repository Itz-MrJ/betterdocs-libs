import numpy as np

# Generate 5 values logarithmically spaced between 1 and 10
result = np.geomspace(start=1, stop=10, num=5, endpoint=False)
print(result) 
'''
Output: 
[1.         1.58489319 2.51188643 3.98107171 6.30957344]
'''