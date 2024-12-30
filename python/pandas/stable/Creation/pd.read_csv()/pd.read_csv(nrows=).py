import pandas as pd

# Example data with extra rows before the actual data
data = """
ID, Name, Age
1, Alice, 30
2, Bob, 25
3, Charlie, 35
Some metadata line
More metadata line"""

# Write the data to a file
file_path = "skiprows_example.csv"
with open(file_path, "w") as f:
    f.write(data)

df = pd.read_csv(file_path, sep=",", nrows=2)
print(df)
'''
Output:
   ID      Name   Age
0   1     Alice    30
1   2       Bob    25
'''