import pandas as pd
import json

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Chloe"],
    "Age": [25, 30, 22],
    "City": ["New York", "Berlin", "Hamburg"]
}
df = pd.DataFrame(data)

# Write the DataFrame to a JSON file with Gzip compression
json_file_path = "data.json.gz"
df.to_json(json_file_path, orient='records', lines=True, compression='gzip')

# Read the compressed JSON file using pandas.read_json
df_read = pd.read_json(json_file_path, compression='gzip', lines=True)
print(df_read)
'''
Output:
    Name  Age      City
0  Alice   25  New York
1    Bob   30    Berlin
2  Chloe   22   Hamburg
'''