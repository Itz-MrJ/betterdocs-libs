import pandas as pd

# Create dataset
data = "123  Alice  25\n456  Bob    30\n789  Charlie 35"
file_path = "file1.fwf"

with open(file_path, "w") as f:
    f.write(data)

# Read the file
df = pd.read_fwf(filepath_or_buffer=file_path)
print(df)
'''
Output:
   123   Alice  25
0  456   Bob    30
1  789  Charlie 35
'''