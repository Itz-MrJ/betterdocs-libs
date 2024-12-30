import pandas as pd

# Creating a Series
s = pd.Series(data=[10, 20, 30], index=['a', 'b', 'c'], name='Numbers')

print(s)
'''
Output:
a    10
b    20
c    30
Name: Numbers, dtype: int64
'''