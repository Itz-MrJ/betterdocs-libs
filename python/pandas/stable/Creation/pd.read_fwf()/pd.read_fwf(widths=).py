import pandas as pd

# Create dataset
data = "123Alice  25\n456Bob    30\n789Charlie35"
file_path = "file3.fwf"

with open(file_path, "w") as f:
    f.write(data)

# Specify column widths
widths = [3, 6, 2]
df = pd.read_fwf(file_path, widths=widths)
print(df)
'''
Output:
   123   Alice   2
0  456     Bob   3
1  789  Charli  e3
'''