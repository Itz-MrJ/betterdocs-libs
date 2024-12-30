import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "BirthDate"])
sheet1.append([1, "Alice", "2003-10-02"])
sheet1.append([2, "Bob", "2003-04-16"])
sheet1.append([2, "Charlie", "2023-12-29"])

# Save the workbook
wb.save(file_path)

# Read the sheets
df = pd.read_excel(io=file_path, parse_dates=False)
print(df['BirthDate'])
'''
Output:
0    2003-10-02
1    2003-04-16
2    2023-12-29
Name: BirthDate, dtype: object
'''