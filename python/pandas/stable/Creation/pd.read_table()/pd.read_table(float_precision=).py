import pandas as pd

# Create a file with high precision floating-point numbers
data = """ID,Value
1,3.141592653589793238462643383279502884197169399375105820974944
2,2.718281828459045235360287471352662497757247093699959574966967
3,1.618033988749894848204586834365638117900284550292151098084
"""

file_path = "high_precision_data.csv"

# Write the data to a CSV file
with open(file_path, "w") as f:
    f.write(data)

# Read the file with legacy float precision
df_legacy = pd.read_table(file_path, sep=",", float_precision="legacy")
print("With float_precision='legacy':")
print(f"Low:        {df_legacy['Value'][0]:.30f}")

# Read the file with high float precision
df_high = pd.read_table(file_path, sep=",", float_precision="high")
print("\nWith float_precision='high':")
print(f"High:       {df_high['Value'][0]:.30f}")

# Read the file with round_trip float precision
df_round = pd.read_table(file_path, sep=",", float_precision="round_trip")
print("\nWith float_precision='round_trip':")
print(f"Round Trip: {df_round['Value'][0]:.30f}")
'''
Output:
With float_precision='legacy':
Low:        3.141592653589792227819543768419

With float_precision='high':
High:       3.141592653589792671908753618482

With float_precision='round_trip':
Round Trip: 3.141592653589793115997963468544
'''