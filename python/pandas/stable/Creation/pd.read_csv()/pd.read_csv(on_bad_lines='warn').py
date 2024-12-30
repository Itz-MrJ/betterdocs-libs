import pandas as pd

# Create a sample file with a bad line
file_path = 'sample_bad_lines.csv'
with open(file_path, 'w') as f:
    f.write("ID,Name\n1,Alice\n2,Bob\n3,Charlie,ExtraField\n4,Diana")
# Handle bad lines by logging a warning
df_warn = pd.read_csv(file_path, sep=",", on_bad_lines="warn")
print("With on_bad_lines='warn':")
print(df_warn)
'''
Output: 
With on_bad_lines='warn':
   ID   Name
0   1  Alice
1   2    Bob
2   4  Diana
<ipython-input-301-47d9fc19f966>:8: ParserWarning: Skipping line 4: expected 2 fields, saw 3
'''