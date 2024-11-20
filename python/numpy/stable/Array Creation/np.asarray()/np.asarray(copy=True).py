import numpy as np

# Original array
original_array = np.asarray([1, 2, 3])

# Creating a new array with copy=True (default behavior)
new_array = np.asarray(original_array, copy=True)

# Modify the new array
new_array[0] = 99

# Print both arrays
print("Original Array:", original_array)  # Output: [1 2 3]
print("New Array:", new_array)            # Output: [99 2 3]