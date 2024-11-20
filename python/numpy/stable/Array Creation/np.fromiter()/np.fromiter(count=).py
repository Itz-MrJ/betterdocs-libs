import numpy as np

arr_from_iter = np.fromiter(range(5), dtype=np.int8, count=2)
print(arr_from_iter) # Output: [0 1]