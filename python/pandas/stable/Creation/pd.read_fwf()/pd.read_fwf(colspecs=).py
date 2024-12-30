import pandas as pd

# Create dataset
data = "123Alice   25\n456Bob     30\n789Charlie 35"
file_path = "file2.fwf"

with open(file_path, "w") as f:
    f.write(data)

# Specify column start and end positions
colspecs = [(0, 3), (3, 10), (10, 13)]
df1 = pd.read_fwf(file_path, colspecs='infer')
df2 = pd.read_fwf(file_path, colspecs=colspecs)
print(f"Infer:\n{df1}\nList of tuples:\n{df2}")
'''
Output:
Infer:
     123Alice  25
0      456Bob  30
1  789Charlie  35
List of tuples:
   123    Alice  25
0  456      Bob  30
1  789  Charlie  35
'''