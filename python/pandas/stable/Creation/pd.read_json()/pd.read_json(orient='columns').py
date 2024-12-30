import pandas as pd
import json

# Create a sample JSON object
sample_json = {
    "Name": ["Alice", "Bob", "Chloe"],
    "Age": [25, 30, 22],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, orient="columns")
print(df)
'''
Output:
    Name  Age         City
0  Alice   25     New York
1    Bob   30  Los Angeles
2  Chloe   22      Chicago
'''