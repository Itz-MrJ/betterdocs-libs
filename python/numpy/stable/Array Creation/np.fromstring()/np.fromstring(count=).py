import numpy as np

string = "1 2 3 4 5"
arr_from_string = np.fromstring(string=string, dtype=np.int8, count=3, sep=' ')
print(arr_from_string) # Output: [1 2 3]