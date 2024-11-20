import numpy as np

# Write to a file with a specified dtype
np.array([1, 2, 3], dtype=np.int32).tofile('data.bin')

# Read from the file with the same dtype
arr_from_file = np.fromfile(file='data.bin', dtype=np.int32)
print(arr_from_file)  # Output: [1 2 3]