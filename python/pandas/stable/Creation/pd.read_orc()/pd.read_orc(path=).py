import pandas as pd

# Create a sample DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Chloe', 'David', 'Eva'],
    'age': [25, 30, 35, 40, 45],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)
df.to_orc('data.orc')

# Read the data back from the ORC file
df_read = pd.read_orc(path='data.orc')
print(df_read)
'''
Output:
   id   name  age   department
0   1  Alice   25           HR
1   2    Bob   30  Engineering
2   3  Chloe   35    Marketing
3   4  David   40  Engineering
4   5    Eva   45           HR
'''