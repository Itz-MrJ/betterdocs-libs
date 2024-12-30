import pandas as pd
from openpyxl import Workbook

# Create an Excel file with multiple sheets
file_path = "example.xlsx"

# Create a workbook and add data
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sheet1"
sheet1.append(["ID", "Name", "Age"])
sheet1.append([1, "Alice", 25])
sheet1.append([2, "Bob", 30])

# Save the workbook
wb.save(file_path)

# Read the default (first) sheet
df_default = pd.read_excel(io=file_path)
print(df_default)
'''
Output:
   ID   Name  Age
0   1  Alice   25
1   2    Bob   30
'''