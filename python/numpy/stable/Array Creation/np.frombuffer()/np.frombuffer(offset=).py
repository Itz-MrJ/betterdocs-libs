import numpy as np

buffer = bytes([1,2,3,4]) # Output: b''
arr_from_buffer = np.frombuffer(buffer=buffer, dtype=np.int8, count=2, offset=2)
print(arr_from_buffer) # Output: [3 4]