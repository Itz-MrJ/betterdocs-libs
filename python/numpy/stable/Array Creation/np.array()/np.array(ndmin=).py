import numpy as np

# A 1D array
arr_1d = np.array([1, 2, 3])
print("Original array:", arr_1d) # Output: [1 2 3]
print("Original array dimensions:", arr_1d.ndim) # Output: 1

# Using ndmin=2 to make sure the array has at least 2 dimensions
arr_2d = np.array([1, 2, 3], ndmin=2)
print("\nArray with ndmin=2:", arr_2d) # Output: [[1 2 3]]
print("Array with ndmin=2 dimensions:", arr_2d.ndim) # Output: 2

# Using ndmin=3 to make sure the array has at least 3 dimensions
arr_3d = np.array([1, 2, 3], ndmin=3)
print("\nArray with ndmin=3:", arr_3d) # Output: [[[1 2 3]]]
print("Array with ndmin=3 dimensions:", arr_3d.ndim) # Output: 3