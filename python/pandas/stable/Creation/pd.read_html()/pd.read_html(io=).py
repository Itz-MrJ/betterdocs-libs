import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read all tables from the URL
dfs = pd.read_html(io=url)

# Print the first DataFrame (the first table in the HTML)
print(dfs[0])
'''
Output: 
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   22
'''