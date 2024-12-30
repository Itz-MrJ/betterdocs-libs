import pandas as pd
import json

# Create a sample JSON object
sample_json = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Chloe", 22, "Chicago"]
]

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, orient="values")
print(df)
'''
Output:
       0   1            2
0  Alice  25     New York
1    Bob  30  Los Angeles
2  Chloe  22      Chicago
'''