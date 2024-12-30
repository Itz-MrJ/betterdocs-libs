import pandas as pd
import json

# Create a sample JSON object
sample_json = {
    "Name": ["Alice", "Bob", "Chloe"],
    "Age": ["25", "30", "22"],
    "timestamp": ["2003-10-02", "2003-04-16", "2023-12-29"]
}

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, keep_default_dates=False)
print(df['timestamp'])
'''
Output:
0    2003-10-02
1    2003-04-16
2    2023-12-29
Name: timestamp, dtype: object
'''