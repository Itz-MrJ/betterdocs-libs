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
df_filtered = pd.read_hdf('employees_table.h5', columns=["id", "name"])

# Print the filtered DataFrame
print(df_filtered)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
2   3  Chloe
3   4  David
4   5    Eva
'''