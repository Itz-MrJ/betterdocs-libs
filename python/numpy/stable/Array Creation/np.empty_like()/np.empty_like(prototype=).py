import numpy as np

a = np.array([[1, 2], [3, 4]])
empty_arr = np.empty_like(prototype=a)
print(empty_arr)  # Values are uninitialized
'''
Output: (Garbage Values)
[[    100981028852064                   0]
 [7306090318617649184 8386106492501113458]]
'''