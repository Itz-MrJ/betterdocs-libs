import pandas as pd

# Writing and reading a DataFrame with pickle
data = {'Name': ['Better', 'Docs'], 'Age': [25, 30]}
df = pd.DataFrame(data)
df.to_pickle('data.pkl')  # Save to pickle

# Read back from pickle
df_loaded = pd.read_pickle(filepath_or_buffer='data.pkl')
print(df_loaded)
'''
Output:
     Name  Age
0  Better   25
1    Docs   30
'''