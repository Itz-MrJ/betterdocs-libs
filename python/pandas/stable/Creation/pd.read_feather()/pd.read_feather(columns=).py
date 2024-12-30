import pandas as pd

# Write a DataFrame to a Feather file
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})
df.to_feather('data.feather')

# Read the Feather file
df_loaded = pd.read_feather(path='data.feather', columns=['col1'])
print(df_loaded)
'''
Output:
   col1
0     1    
1     2    
2     3    
'''