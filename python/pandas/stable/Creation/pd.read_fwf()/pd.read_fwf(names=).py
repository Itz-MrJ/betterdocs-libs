import pandas as pd

# Create dataset
data = "123Alice   25\n456Bob     30\n789Charlie 35"
file_path = "file8.txt"

with open(file_path, "w") as f:
    f.write(data)

# Additional arguments being passed to pd.read_table()
df = pd.read_fwf(file_path, names=["ID", "Name", "Age"])
print(df)
'''
Output:
           ID  Name  Age
0    123Alice    25  NaN
1      456Bob    30  NaN
2  789Charlie    35  NaN
'''