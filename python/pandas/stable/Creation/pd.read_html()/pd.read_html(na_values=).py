import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, match="Position", na_values=["null"])

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
    Name   Age  Position
0  Alice   NaN   Manager
1    Bob  30.0  Engineer
'''