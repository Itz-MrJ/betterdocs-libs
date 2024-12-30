import pandas as pd

# Create a sample file with a bad line
file_path = 'sample_bad_lines.csv'
with open(file_path, 'w') as f:
    f.write("ID,Name\n1,Alice\n2,Bob\n3,Charlie,ExtraField\n4,Diana")
    
# Handle bad lines by skipping them
df = pd.read_csv(file_path, sep=",", on_bad_lines="skip")
print("With on_bad_lines='skip':")
print(df)
'''
Output: 
With on_bad_lines='skip':
   ID   Name
0   1  Alice
1   2    Bob
2   4  Diana
'''