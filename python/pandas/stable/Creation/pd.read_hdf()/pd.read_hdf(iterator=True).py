import pandas as pd

# Create sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Chloe', 'David', 'Eva'],
    'salary': [75000, 80000, 85000, 90000, 95000],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

# Save to HDF5 in table format
df.to_hdf('bb.h5', key='data', mode='w', data_columns=True, format='table')

# Read HDF5 with chunks (iterator=True, chunksize=3)
df_filtered = pd.read_hdf('bb.h5', iterator=True, chunksize=3)
for chunk in df_filtered:
  print(chunk)
'''
Output:
   id   name  salary   department
0   1  Alice   75000           HR
1   2    Bob   80000  Engineering
2   3  Chloe   85000    Marketing
   id   name  salary   department
3   4  David   90000  Engineering
4   5    Eva   95000           HR
'''