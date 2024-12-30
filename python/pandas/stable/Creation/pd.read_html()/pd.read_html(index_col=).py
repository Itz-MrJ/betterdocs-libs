import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, match="Expenditure", index_col="Year")

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
      Expenditure  Profit
Year                     
2021          200     800
2022          300     900
'''