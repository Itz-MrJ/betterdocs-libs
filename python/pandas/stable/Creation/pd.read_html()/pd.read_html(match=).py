import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables, filtering tables containing "Sales"
dfs = pd.read_html(io=url, match="Sales")

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
   Year  Sales  Revenue
0  2021    500     1000
1  2022    600     1200
'''