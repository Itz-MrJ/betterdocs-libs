import pandas as pd

# Example data with a comment line
data = '''# This is a comment line
ID,Name
1,Alice
2,Bob
3,Charlie
'''

# Write the data to a file
file_path = "comment_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file and skip comment lines
df = pd.read_table(file_path, sep=',', comment='#')
print(df)
'''
Output:
   ID     Name
0   1    Alice
1   2      Bob
2   3  Charlie
'''