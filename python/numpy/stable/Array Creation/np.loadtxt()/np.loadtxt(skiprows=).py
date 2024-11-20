import numpy as np

with open('data_skiprows.txt', 'w') as f:
    f.write("Header line\nAnother header\n1.0 2.0 3.0\n4.0 5.0 6.0")

data = np.loadtxt('data_skiprows.txt', skiprows=2)
print(data)
# Output:
# [[1. 2. 3.]
#  [4. 5. 6.]]