import pandas as pd

# Example data with Windows-style line terminators (\t)
data = "ID,Name,Age\t1,Alice,30\t2,Bob,25\t3,Charlie,35"

# Write the data to a file with \r as line terminator
file_path = "example_lineterminator.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file without specifying lineterminator
df = pd.read_csv(file_path, sep=',', lineterminator="\t")
print(df)
'''
Output:
   ID     Name  Age
0   1    Alice   30
1   2      Bob   25
2   3  Charlie   35
'''