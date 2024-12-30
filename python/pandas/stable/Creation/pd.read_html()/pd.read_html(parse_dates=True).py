import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, attrs={'class': 'dates-class'}, parse_dates=['Date'])

# Print the first matched DataFrame
print(dfs[0]['Date'])
'''
Output: 
0   2003-10-02
1   2003-04-16
2   2023-12-29
Name: Date, dtype: datetime64[ns]
'''