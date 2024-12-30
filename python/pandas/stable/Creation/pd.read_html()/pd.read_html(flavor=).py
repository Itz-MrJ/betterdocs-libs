import pandas as pd

# URL or HTML content
url = 'https://betterdocs.tech/global/python/pandas/tables.html'

# Using BeautifulSoup (default, if lxml isn't installed)
dfs_bs4 = pd.read_html(url, flavor='bs4')

# Using lxml
dfs_lxml = pd.read_html(url, flavor='lxml')

# Using html5lib
dfs_html5lib = pd.read_html(url, flavor='html5lib')

# Output the first DataFrame from each flavor
print(dfs_bs4[0])  # First DataFrame from BeautifulSoup
print(dfs_lxml[0])  # First DataFrame from lxml
print(dfs_html5lib[0])  # First DataFrame from html5lib
'''
Output:
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   22
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   22
      Name  Age
0    Alice   25
1      Bob   30
2  Charlie   22
'''