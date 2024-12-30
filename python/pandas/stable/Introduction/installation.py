import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['NumPy', 'Pandas', 'Matplotlib'],
    'Count': [0, 1, 2],
    'Remarks': ['Better', 'Docs', '#justbetter']
}
df = pd.DataFrame(data)
print(df)
'''
Output:
|index|Name      |Count|Remarks    |
|-----|----------|-----|-----------|
|0    |NumPy     |0    |Better     |
|1    |Pandas    |1    |Docs       |
|2    |Matplotlib|2    |#justbetter|
'''