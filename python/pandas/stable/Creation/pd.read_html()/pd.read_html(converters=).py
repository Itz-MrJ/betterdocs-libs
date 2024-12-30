import pandas as pd

# URL containing HTML tables
url = "https://betterdocs.tech/global/python/pandas/tables.html"

def half_the_age(age):
    return int(age)/2

# Read HTML tables
dfs = pd.read_html(io=url, converters={'Age': half_the_age})

# Print the first matched DataFrame
print(dfs[0])
'''
Output: 
      Name   Age
0    Alice  12.5
1      Bob  15.0
2  Charlie  11.0
'''