import numpy as np

# Metadata: 1 byte, followed by record (id: 1 byte, value: 2 bytes)
binary_data = bytes([0xFF, 0x01]) + np.int16(4660).tobytes()

# Define dtype using np.dtype
dtype = np.dtype([('id', np.int8), ('value', np.int16)])

# Create record array with offset to skip 1 byte of metadata
r_array = np.rec.array(binary_data, dtype=dtype, offset=1)

print(r_array)       # Output: [(1, 4660)]
print(r_array.id)    # Output: [1]
print(r_array.value) # Output: [4660]