import pandas as pd
import numpy as np

# Original data as a NumPy array
original_data = np.array([1, 2, 3])

# Create a Series using the NumPy array
s = pd.Series(data=original_data, copy=False)

# Modify the original data (this will affect the Series)
original_data[0] = 100

# Print the Series
print(s)
'''
Output:
0    100
1      2
2      3
dtype: int64
'''