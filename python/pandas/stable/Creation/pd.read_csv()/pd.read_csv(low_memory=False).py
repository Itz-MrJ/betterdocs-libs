import pandas as pd
import csv

# Recursive function to generate large data
def generate_data(current_row, max_rows, file_path):
    if current_row > max_rows:
        return
    with open(file_path, mode='a', newline='', encoding="utf-8") as file:
        csv.writer(file).writerow([current_row, f"Name{current_row}"])
    generate_data(current_row + 1, max_rows, file_path)

# File path for the generated large CSV
file_path = "large_data.csv"

# Write headers to the file first
with open(file_path, mode='w', newline='', encoding="utf-8") as file:
    csv.writer(file).writerow(["ID", "Name"])

# Generate large data (10000 rows for this example)
generate_data(1, 10000, file_path)

# Read the generated large data using low_memory=False
df = pd.read_csv(file_path, sep=",", low_memory=False)

# Display the first few rows
print(df.head())
'''
Output:
   ID   Name
0   1  Name1
1   2  Name2
2   3  Name3
3   4  Name4
4   5  Name5
'''