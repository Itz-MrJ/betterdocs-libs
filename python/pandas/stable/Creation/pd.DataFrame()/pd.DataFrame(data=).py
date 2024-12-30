import pandas as pd

# Creating a DataFrame
data = {'Name': ['Better', 'Docs'], 'Age': [25, 30]}
df = pd.DataFrame(data=data)
print(df)
'''
Output:
     Name  Age
0  Better   25
1    Docs   30
'''