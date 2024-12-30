import pandas as pd

# Creating a DataFrame
data = {'Name': ['Better', 'Docs'], 'Age': [25, 30]}
df = pd.DataFrame(data=data, index=("Row1", "Row2"), columns=["Name", "Age"], dtype='object')
print(df)
'''
Output:
        Name  Age
Row1  Better   25
Row2    Docs   30
'''