import pandas as pd
import json

# Create a sample JSON object
sample_json = {
    "Name": ["Alice", "Bob", "Chloe"],
    "Age": ["25", "30", "22"],
    "Timestamp": [1065117600, 1050480000, 1703876400]
}

# Write the JSON to a file
json_file_path = "sample_data.json"
with open(json_file_path, "w") as json_file:
    json.dump(sample_json, json_file, indent=2)

# Read the JSON file into a DataFrame
df = pd.read_json(path_or_buf=json_file_path, date_unit='s')
print(df)
'''
Output:
    Name  Age           Timestamp
0  Alice   25 2003-10-02 18:00:00
1    Bob   30 2003-04-16 08:00:00
2  Chloe   22 2023-12-29 19:00:00
'''