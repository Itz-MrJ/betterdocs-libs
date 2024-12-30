import pandas as pd
import json

# Create a sample JSON object
sample_json = {
    "schema": {
        "fields": [
            {"name": "ID", "type": "integer"},
            {"name": "Name", "type": "string"},
            {"name": "Age", "type": "integer"}
        ],
        "primaryKey": ["ID"],
        "pandas_version": "2.2"
    },
    "data": [
        {"ID": 1, "Name": "Alice", "Age": 25},
        {"ID": 2, "Name": "Bob", "Age": 30},
        {"ID": 3, "Name": "Chloe", "Age": 22}
    ]
}

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, orient="table")
print(df)
'''
Output:
     Name  Age
ID            
1   Alice   25
2     Bob   30
3   Chloe   22
'''