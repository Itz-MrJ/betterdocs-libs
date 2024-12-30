import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'id': [3, 4], 'name': ['Chloe', 'David']})

# Write DataFrames to an HDF5 file under different keys
df1.to_hdf('data.h5', key='group1', mode='w')
df2.to_hdf('data.h5', key='group2', mode='a')

# Read the dataset under 'group1'
df_group1 = pd.read_hdf('data.h5', key='group1')
print(df_group1)

# Read the dataset under 'group2'
df_group2 = pd.read_hdf('data.h5', key='group2')
print(df_group2)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
   id   name
0   3  Chloe
1   4  David
'''