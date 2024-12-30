import pandas as pd
import json

# Create a sample JSON object with an intentional encoding issue
sample_json = {
    "Name": ["Alice", "Bob", "Chloé"],
    "City": ["München", "Berlin", "Hamburg"]
}

# Add an invalid character intentionally into the JSON for testing
# e.g., introducing a broken character in the name of the city
sample_json["City"][0] = "Münchën"  # 'ü' becomes 'ë' as an invalid byte

# Write the JSON data to a file
json_file_path = "sample_data_with_invalid_encoding.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(sample_json, json_file, ensure_ascii=False, indent=2)

# Read the JSON file with encoding_errors='strict' (default)
try:
    df_strict = pd.read_json(json_file_path, encoding='ascii', encoding_errors='strict')
    print("With encoding_errors='strict':")
    print(df_strict)
except UnicodeDecodeError as e:
    print("Error with encoding_errors='strict':", e)

# Read the JSON file with encoding_errors='ignore'
df_ignore = pd.read_json(json_file_path, encoding='ascii', encoding_errors='ignore')
print("\nWith encoding_errors='ignore':")
print(df_ignore)

# Read the JSON file with encoding_errors='replace'
df_replace = pd.read_json(json_file_path, encoding='ascii', encoding_errors='replace')
print("\nWith encoding_errors='replace':")
print(df_replace)
'''
Output:
Error with encoding_errors='strict': 'ascii' codec can't decode byte 0xc3 in position 47: ordinal not in range(128)

With encoding_errors='ignore':
    Name     City
0  Alice    Mnchn
1    Bob   Berlin
2   Chlo  Hamburg

With encoding_errors='replace':
     Name       City
0   Alice  M��nch��n
1     Bob     Berlin
2  Chlo��    Hamburg
'''