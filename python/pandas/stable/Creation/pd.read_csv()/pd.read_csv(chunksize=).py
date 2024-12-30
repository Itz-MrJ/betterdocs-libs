import pandas as pd

# Example data with dates
data = """ID,Name,BirthDate
1,Alice,2020-01-01
2,Bob,2021-02-28
3,Charlie,2023-03-15
4,David,2019-11-12
5,Eve,2022-08-09"""

# Write the data to a file
file_path = "example_ite.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the data 
df = pd.read_csv(file_path, sep=',', chunksize=3)
# Read first 2
print(df.get_chunk(2))
# # Read the *next* 2
print(df.get_chunk(2))
'''
Output:
   ID   Name   BirthDate
0   1  Alice  2020-01-01
1   2    Bob  2021-02-28

   ID     Name   BirthDate
2   3  Charlie  2023-03-15
3   4    David  2019-11-12
'''