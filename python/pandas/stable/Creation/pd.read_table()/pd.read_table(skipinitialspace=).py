import pandas as pd

# Example data with extra spaces after the comma delimiter
data = """ID,   Name     ,    Age
1,   Alice   ,   30
2,   Bob     ,   25
3,   Charlie ,  35"""

# Write the data to a file
file_path = "example_skipspace.csv"
with open(file_path, "w") as f:
    f.write(data)

# skipinitialspace=False (No space skipping)
df_false = pd.read_table(file_path, sep=',', skipinitialspace=False)

print("With skipinitialspace=False:")
print(df_false)

# skipinitialspace=True (Skipping spaces after the delimiter)
df_true = pd.read_table(file_path, sep=',', skipinitialspace=True)

print("With skipinitialspace=True:")
print(df_true)
'''
Output:
With skipinitialspace=False:
   ID    Name           Age
0   1     Alice          30
1   2     Bob            25
2   3     Charlie        35

With skipinitialspace=True:
   ID Name       Age
0   1  Alice      30
1   2  Bob        25
2   3  Charlie    35
'''