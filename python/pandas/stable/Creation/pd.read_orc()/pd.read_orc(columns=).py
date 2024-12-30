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
df_read = pd.read_orc(path='data.orc', columns=["id", "name"])
print(df_read)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
2   3  Chloe
3   4  David
4   5    Eva
'''