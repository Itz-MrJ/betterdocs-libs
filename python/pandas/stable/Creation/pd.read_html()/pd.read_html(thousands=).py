import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, attrs={'class': 'numbers-class'}, thousands='|')

# Print the first matched DataFrame
print(dfs[0]['Thousands'])
'''
Output: 
0    123908213
1        78234
2         1023
Name: Thousands, dtype: int64
'''