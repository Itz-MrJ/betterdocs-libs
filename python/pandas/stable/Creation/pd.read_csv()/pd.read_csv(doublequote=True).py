import pandas as pd
import csv

# Example data with quotes inside quoted fields
data = '''ID,Name
1,Alice
2,Bob
3,"Charlie ""The King"""
'''

# Write the data to a file
file_path = "doublequote_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file with doublequote=True (default)
df = pd.read_csv(file_path, quotechar='"', doublequote=True)
print(df)
'''
Output:
   ID                Name
0   1               Alice
1   2                 Bob
2   3  Charlie "The King"
'''