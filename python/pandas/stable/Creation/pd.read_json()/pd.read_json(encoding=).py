import pandas as pd
import json

# Create a sample JSON object
sample_json = {
    "Name": ["Alice", "Bob", "Chloe"],
    "Age": ["25", "30", "22"],
}

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, encoding="utf-8")
print(df)
'''
Output:
    Name  Age
0  Alice   25
1    Bob   30
2  Chloe   22
'''