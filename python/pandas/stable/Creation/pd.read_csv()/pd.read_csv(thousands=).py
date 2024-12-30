import pandas as pd

# Example data with thousands separators (dot)
data = """ID,Amount
1,1,000
2,2,500.000
3,3,700"""

# Write the data to a file
file_path = "example_thousands.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file and specify the thousands separator (dot)
df = pd.read_csv(file_path, sep=',', thousands='.')

print(df['Amount'])
'''
Output:
1         0
2    500000
3       700
Name: Amount, dtype: int64
'''