import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "Age"])
sheet1.append([1, "Alice", 20])
sheet1.append([2, "Bob", 30])
sheet1.append([2, "Charlie", 10])

# Save the workbook
wb.save(file_path)

def half_the_age(age):
    return int(age)/2

# Read the sheets
df = pd.ExcelFile(path_or_buffer=file_path).parse(sheet_name='Sheet1', converters={"Age": half_the_age})
print(df)
'''
Output:
   ID     Name   Age
0   1    Alice  10.0
1   2      Bob  15.0
2   2  Charlie   5.0
'''