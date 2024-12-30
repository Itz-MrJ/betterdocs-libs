import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, match="Position", keep_default_na=False)

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
    Name   Age  Position
0  Alice  null   Manager
1    Bob    30  Engineer
'''