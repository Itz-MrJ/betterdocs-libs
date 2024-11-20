import numpy as np

with open('data_usecols.txt', 'w') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0")

data1, data2, data3 = np.loadtxt('data_usecols.txt', unpack=True)
print(data1)  # Output: [1. 4.]
print(data2)  # Output: [2. 5.]
print(data3)  # Output: [3. 6.]