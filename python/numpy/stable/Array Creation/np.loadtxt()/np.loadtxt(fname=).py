import numpy as np

arr = np.array([1, 2, 3])
arr.tofile(file='data.txt', sep=",")  # Write as text
arr_from_file = np.loadtxt(fname='data.txt', delimiter=',')
print(arr_from_file)  # Output: [1. 2. 3.]