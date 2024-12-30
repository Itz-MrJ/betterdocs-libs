import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, attrs={'class': 'numbers-class'}, decimal=',')

# Print the first matched DataFrame
print(dfs[0]['Decimal'])
'''
Output: 
0    12021
1       12
2      921
Name: Decimal, dtype: int64
'''