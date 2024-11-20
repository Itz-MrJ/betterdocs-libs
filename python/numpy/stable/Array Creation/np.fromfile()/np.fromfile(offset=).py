import numpy as np

# Data to write
data = np.array([10, 20, 30, 40, 50], dtype=np.int32)

# Write the data to a binary file
with open('data_with_header.bin', 'wb') as f:
    f.write(b'BETTER')  # Write a header (6 bytes)
    data.tofile(f)      # Write the actual data

# Read the file, skipping the 6-byte header
arr = np.fromfile('data_with_header.bin', dtype=np.int32, offset=6)
print(arr)
# Output: [10 20 30 40 50]