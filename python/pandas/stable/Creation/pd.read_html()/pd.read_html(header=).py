import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

# Read HTML tables
dfs = pd.read_html(io=url, header=0)

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   22
'''