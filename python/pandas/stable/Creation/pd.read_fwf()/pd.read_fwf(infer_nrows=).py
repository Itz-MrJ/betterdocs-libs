import pandas as pd

# Create dataset
data = "123 Alice 25\n456 Bob   30\n789 Charlie 35"
file_path = "file4.fwf"

with open(file_path, "w") as f:
    f.write(data)

# Infer column widths from the first 2 rows
df = pd.read_fwf(file_path, colspecs="infer", infer_nrows=2)
print(df)
'''
Output:
   123  Alice  25
0  456    Bob  30
1  789  Charl   e
'''