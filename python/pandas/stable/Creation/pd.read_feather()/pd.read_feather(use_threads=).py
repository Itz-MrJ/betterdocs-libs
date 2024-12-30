import pandas as pd

# Write a DataFrame to Feather
df = pd.DataFrame({'col1': range(100000), 'col2': range(100000)})
df.to_feather('data.feather')

# Read with threading (default)
df1 = pd.read_feather('data.feather', use_threads=True)
print(df1.head())
'''
Output:
   col1  col2
0     0     0
1     1     1
2     2     2
3     3     3
4     4     4
'''