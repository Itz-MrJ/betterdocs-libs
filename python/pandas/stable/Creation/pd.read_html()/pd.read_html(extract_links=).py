import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables-links.html"

# Read HTML tables
dfs = pd.read_html(io=url, extract_links="all")

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
    (Name, None)                                (Link, None)
0  (Alice, None)  (Alice's Profile, https://dikshapadi.site)
1    (Bob, None)          (Bob's Profile, https://aarya.fun)
'''