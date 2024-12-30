import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, attrs={'id': 'finance-table'})

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
   Year  Expenditure  Profit
0  2021          200     800
1  2022          300     900
'''