import pandas as pd

# Create sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Chloe', 'David', 'Eva'],
    'salary': [75000, 80000, 85000, 90000, 95000],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)
df.to_hdf('employees_table.h5', key='data', mode='w', data_columns=True, format='table')

# Use the 'where' parameter to filter data with salary > 80000
df_filtered = pd.read_hdf('employees_table.h5', key='data', where="id=2")

# Print the filtered DataFrame
print(df_filtered)
'''
Output:
   id name  salary   department
1   2  Bob   80000  Engineering
'''