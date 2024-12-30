import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, skiprows=1)

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
     Alice  25
0      Bob  30
1  Charlie  22
'''