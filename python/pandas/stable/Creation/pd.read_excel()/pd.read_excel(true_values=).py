import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "Age", "isActive"])
sheet1.append([1, "Alice", 25, "yes"])
sheet1.append([2, "Bob", 30, "maybe"])
sheet1.append([2, "Charlie", 10, "no"])

# Save the workbook
wb.save(file_path)

# Read the sheets
df = pd.read_excel(io=file_path, true_values=["yes", "maybe"], false_values=["no"])
print(df)
'''
Output:
   ID     Name  Age  isActive
0   1    Alice   25      True
1   2      Bob   30      True
2   2  Charlie   10     False
'''