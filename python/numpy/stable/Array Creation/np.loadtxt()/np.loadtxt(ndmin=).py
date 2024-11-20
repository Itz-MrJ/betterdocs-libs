import numpy as np

# Write a simple data file with a single line
with open('data_single_line.txt', 'w') as f:
    f.write("1.0 2.0 3.0")

data_ndmin2 = np.loadtxt('data_single_line.txt', ndmin=2)
print("\nndmin=2 array shape:", data_ndmin2.shape)  # Output: (1, 3)
print("ndmin=2 array:", data_ndmin2)  # Output: [[1. 2. 3.]]