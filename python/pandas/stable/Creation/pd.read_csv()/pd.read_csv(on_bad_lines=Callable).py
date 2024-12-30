import pandas as pd

# Create a sample file with a bad line
file_path = 'sample_bad_lines.csv'
with open(file_path, 'w') as f:
    f.write("ID,Name\n1,Alice\n2,Bob\n3,Charlie,ExtraField\n4,Diana")

# Define a custom function for processing bad lines
def custom_handler(bad_line):
    print(f"Processing bad line: {bad_line}")
    # Example: return None to skip the line or modify the line
    return None

df_custom = pd.read_csv(file_path, sep=",", on_bad_lines=custom_handler, engine='python')
print("With a custom handler:")
print(df_custom)
'''
Output:
Processing bad line: ['3', 'Charlie', 'ExtraField']

With a custom handler:
   ID   Name
0   1  Alice
1   2    Bob
2   4  Diana
'''