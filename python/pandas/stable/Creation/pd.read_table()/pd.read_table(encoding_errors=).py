import pandas as pd

# Write the file with explicit UTF-8 encoding
data = "ID,Name\n1,Alice\n2,Bob\n3,Chloé"
file_path = "encoding_errors_example.csv"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(data)

# Read the file with incorrect ASCII encoding
try:
  df = pd.read_table(file_path, sep=",", encoding="ascii", encoding_errors="strict")
except UnicodeDecodeError as e:
  print(e)
df_ignore = pd.read_table(file_path, sep=",", encoding="ascii", encoding_errors="ignore")

df_replace = pd.read_table(file_path, sep=",", encoding="ascii", encoding_errors="replace")

# Print the results
print("With encoding_errors='ignore':")
print(df_ignore)

print("\nWith encoding_errors='replace':")
print(df_replace)

'''
Output:
'ascii' codec can't decode byte 0xc3 in position 28: ordinal not in range(128)
With encoding_errors='ignore':
   ID   Name
0   1  Alice
1   2    Bob
2   3   Chlo

With encoding_errors='replace':
   ID    Name
0   1   Alice
1   2     Bob
2   3  Chlo��
'''