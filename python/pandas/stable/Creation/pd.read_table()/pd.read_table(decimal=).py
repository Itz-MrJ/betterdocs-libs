import pandas as pd

# Example data with decimal separators (|)
data = """ID,Amount
1,1,000|9
2,2,500|70
3,3,700"""

# Write the data to a file
file_path = "example_dec.csv"
with open(file_path, "w") as f:
    f.write(data)

# Read the file
df = pd.read_table(file_path, sep=',', decimal='|')

print(df['Amount'])
'''
1      0.9
2    500.7
3    700.0
Name: Amount, dtype: float64
'''