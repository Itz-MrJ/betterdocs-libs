import csv
import pandas as pd

# Register a custom dialect
csv.register_dialect('my_dialect', delimiter='|', quoting=csv.QUOTE_NONE)

# Create a sample file
file_path = 'sample_dialect.csv'
with open(file_path, 'w') as f:
    f.write("ID|Name\n1|Alice\n2|Bob\n3|Charlie")

# Use the custom dialect to read the file
df = pd.read_csv(file_path, dialect='my_dialect')
print(df)
'''
Output:
   ID     Name
0   1    Alice
1   2      Bob
2   3  Charlie
'''