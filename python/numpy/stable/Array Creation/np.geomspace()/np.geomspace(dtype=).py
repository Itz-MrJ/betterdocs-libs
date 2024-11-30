import numpy as np

# Generate 5 values logarithmically spaced between 1 and 10
result = np.geomspace(start=1, stop=10, num=5, dtype=np.int32)
print(result) 
'''
Output: 
[ 1  1  3  5 10]
'''