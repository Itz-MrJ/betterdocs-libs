import numpy as np

arr_from_iter = np.fromiter(iter=range(5), dtype=np.int8)
print(arr_from_iter) # Output: [0 1 2 3 4]