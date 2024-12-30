import pandas as pd
import numpy as np

# Creating using np.eye
data = np.eye(3, dtype=np.int8)
# Creating a DataFrame
df = pd.DataFrame(data=data, index=("Row1", "Row2", "Row3"), copy=False)
data[1][1] = 5
print(df)
'''
Output:
      0  1  2
Row1  1  0  0
Row2  0  5  0
Row3  0  0  1
'''