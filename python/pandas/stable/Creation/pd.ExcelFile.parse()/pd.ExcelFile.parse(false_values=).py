import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "Salary", "isActive"])
sheet1.append([1, "Alice", "2000", "yes"])
sheet1.append([2, "Bob", "10000", "maybe"])
sheet1.append([2, "Charlie", "2000", "no"])

# Save the workbook
wb.save(file_path)

# Read the sheets
df = pd.ExcelFile(path_or_buffer=file_path).parse(sheet_name='Sheet1', true_values=["yes"], false_values=["no", "maybe"])
print(df)
'''
Output:
   ID     Name  Salary  isActive
0   1    Alice    2000      True
1   2      Bob   10000     False
2   2  Charlie    2000     False
'''