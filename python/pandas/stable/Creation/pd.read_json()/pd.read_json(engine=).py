import pandas as pd
import json

# Sample data for JSON Lines format (one JSON object per line)
data = [
    {"Name": "Alice", "Age": 25},
    {"Name": "Bob", "Age": 30},
    {"Name": "Chloe", "Age": 22}
]

# Define the file path
json_file_path = "data.json"

# Write data to the file (one JSON object per line)
with open(json_file_path, "w") as json_file:
    for record in data:
        json.dump(record, json_file)
        json_file.write("\n")

# Now, read the JSON data back with lines=True
df = pd.read_json(json_file_path, lines=True, engine='ujson')
print(df)
'''
Output:
    Name  Age
0  Alice   25
1    Bob   30
2  Chloe   22
'''