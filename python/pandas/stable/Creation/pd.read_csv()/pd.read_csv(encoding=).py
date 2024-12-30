import pandas as pd

# Example data with special characters
data = "ID,Name\n1,Alice\n2,Bob\n3,Chloé"

# Write the data to a file with ISO-8859-1 encoding
file_path = "encoding_example.csv"
with open(file_path, "w", encoding="ISO-8859-1") as f:
    f.write(data)

# Read the file with the correct encoding
df = pd.read_csv(file_path, sep=",", encoding="ISO-8859-1")
print(df)
'''
Output:
   ID   Name
0   1  Alice
1   2    Bob
2   3  Chloé
'''