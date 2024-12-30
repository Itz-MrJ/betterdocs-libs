import pandas as pd

# Example data with quoted fields
data = """ID,Name,Age
1,"Alice, Smith",30
2,"Bob, Johnson",25
3,"Charlie, Brown",35"""

# Write the data to a file
file_path = "example_quotechar.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file with quotechar as "
df = pd.read_table(file_path, sep=',', quotechar='"')

print(df)
'''
Output:
   ID            Name  Age
0   1    Alice, Smith   30
1   2    Bob, Johnson   25
2   3  Charlie, Brown   35
'''