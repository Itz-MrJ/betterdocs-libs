import pandas as pd
import json

# Sample data
nested_json = [
    {
        "id": 1,
        "name": "Alice",
        "info": {
            "age": 25,
            "city": "New York"
        },
        "hobbies": [
            {"type": "reading", "frequency": "daily"},
            {"type": "hiking", "frequency": "weekly"}
        ]
    },
    {
        "id": 2,
        "name": "Bob",
        "info": {
            "age": 30,
            "city": "San Francisco"
        },
        "hobbies": [
            {"type": "cooking", "frequency": "monthly"}
        ]
    }
]

# Normalize the JSON with record_path
df = pd.json_normalize(data=nested_json, record_path="hobbies")
print(df)
'''
Output:
      type frequency
0  reading     daily
1   hiking    weekly
2  cooking   monthly
'''