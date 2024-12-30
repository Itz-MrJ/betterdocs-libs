import pandas as pd

# Example data
data = """ID, Name, Age
1, Alice, 30
2, Bob, 25
3, Charlie, 35"""

# Write the data to a file
file_path = "verbose_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the data with verbose=True
df = pd.read_table(file_path, sep=',', verbose=False)

# Display the DataFrame
print(df)
'''
Output:
   ID      Name   Age
0   1     Alice    30
1   2       Bob    25
2   3   Charlie    35
'''