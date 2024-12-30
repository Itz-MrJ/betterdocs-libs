import pandas as pd

# Create a sample file with a bad line
file_path = 'sample_bad_lines.csv'
with open(file_path, 'w') as f:
    f.write("ID,Name\n1,Alice\n2,Bob\n3,Charlie,ExtraField\n4,Diana")

df_err = pd.read_table(file_path, sep=",", on_bad_lines="error")
print("With on_bad_lines='error':")
print(df_err)
'''
Output (Error raised): 
ParserError                               Traceback (most recent call last)
'''