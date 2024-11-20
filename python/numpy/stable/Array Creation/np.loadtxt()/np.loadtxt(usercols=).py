import numpy as np

with open('data_usecols.txt', 'w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0")

data = np.loadtxt('data_usecols.txt', usecols=(0, 2))
print(data)
# Output:
# [[1. 3.]
#  [4. 6.]]