import pandas as pd

# Example data
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to a GZIP-compressed file
file_path = "example_compressed.gz"
df.to_csv(file_path, index=False, compression='gzip')

# Reading the GZIP compressed file directly using pandas
df_gzip = pd.read_table(file_path, sep=',', compression='gzip')

print(df_gzip)
'''
Output:
   ID     Name  Age
0   1    Alice   30
1   2      Bob   25
2   3  Charlie   35
'''