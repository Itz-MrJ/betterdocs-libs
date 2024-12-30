import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["random", "random", "random"])
sheet1.append(["ID", "Name", "Salary"])
sheet1.append([1, "Alice", "2000"])
sheet1.append([2, "Bob", "10000"])
sheet1.append([2, "Charlie", "2000"])

# Save the workbook
wb.save(file_path)

# Read the sheets
df = pd.ExcelFile(path_or_buffer=file_path).parse(sheet_name='Sheet1', skiprows=1)
print(df)
'''
Output:
   ID     Name  Salary
0   1    Alice    2000
1   2      Bob   10000
2   2  Charlie    2000
'''