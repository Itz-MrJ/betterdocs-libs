import pandas as pd

# Example data with extra rows before the actual data
data = """Header1, Header2, Header3
Some metadata line
More metadata line
ID, Name, Age
1, Alice, 30
2, Bob, 25
3, Charlie, 35"""

# Write the data to a file
file_path = "skiprows_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Reading the file while skipping the first 3 rows
df = pd.read_csv(file_path, skiprows=3, sep=",")
print(df)
'''
Output:
   ID      Name   Age
0   1     Alice    30
1   2       Bob    25
2   3   Charlie    35
'''