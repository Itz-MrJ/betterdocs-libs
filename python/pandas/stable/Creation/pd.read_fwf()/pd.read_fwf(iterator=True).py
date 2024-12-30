import pandas as pd

# Create dataset
data = "ID   Name     Age\n123  Alice    25\n456  Bob      30\n789  Charlie  35"
file_path = "file6.fwf"

with open(file_path, "w") as f:
    f.write(data)

# Use iterator to read chunks
df_iterator = pd.read_fwf(file_path, iterator=True, chunksize=1)
print(next(df_iterator))
'''
Output:
    ID     Name  Age
0  123    Alice   25
'''