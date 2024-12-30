import pandas as pd

# Example data with blank lines
data = """ID, Name, Age
1, Alice, 30

2, Bob, 25

3, Charlie, 35"""

# Write the data to a file
file_path = "skip_blank_lines_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Reading with skip_blank_lines=True (default)
df = pd.read_csv(file_path, sep=',', skip_blank_lines=True)
print(df)
'''
Output:
   ID      Name   Age
0   1     Alice    30
1   2       Bob    25
2   3   Charlie    35
'''