import pandas as pd

# Create a sample DataFrame
data = {
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Chloe', 'David'],
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Write the DataFrame to a Parquet file
df.to_parquet('data.parquet', index=False)

# Read the Parquet file into a DataFrame
df_read = pd.read_parquet(path='data.parquet')
print(df_read)
'''
Output:
   id   name  age  salary
0   1  Alice   25   50000
1   2    Bob   30   60000
2   3  Chloe   35   70000
3   4  David   40   80000
'''