import numpy as np

buffer = bytes([1,2,3,4]) # Output: b''
arr_from_buffer = np.frombuffer(buffer=buffer, dtype=np.int8)
print(arr_from_buffer) # Output: [1 2 3 4]