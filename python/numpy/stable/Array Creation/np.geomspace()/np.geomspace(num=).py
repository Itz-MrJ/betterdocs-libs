import numpy as np

# Generate 10 values logarithmically spaced between 1 and 10
result = np.geomspace(start=1, stop=10, num=10)
print(result) 
'''
Output: 
[ 1.          1.29154967  1.66810054  2.15443469  2.7825594   3.59381366
  4.64158883  5.9948425   7.74263683 10.        ]
'''