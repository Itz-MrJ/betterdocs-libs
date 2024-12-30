import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, displayed_only=False)

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
     Name  Age
0      We   25
1    Were   30
2  Hidden   22
'''