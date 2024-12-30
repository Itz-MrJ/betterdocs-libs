import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "Salary"])
sheet1.append([1, "Alice", "2000"])
sheet1.append([2, "Bob", "10050"])
sheet1.append([2, "Charlie", "232564"])
sheet1.append(["random", "random", "random"])

# Save the workbook
wb.save(file_path)

# Read the sheets
df = pd.ExcelFile(path_or_buffer=file_path).parse(sheet_name='Sheet1', skipfooter=1)
print(df)
'''
Output:
   ID     Name  Salary
0   1    Alice    2000
1   2      Bob   10050
2   2  Charlie  232564
'''