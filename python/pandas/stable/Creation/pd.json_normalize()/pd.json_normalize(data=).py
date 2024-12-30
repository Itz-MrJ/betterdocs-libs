import pandas as pd
import json

# Sample data
nested_json = [
    {
        "id": 1,
        "name": "Alice",
        "info": {"age": 25, "city": "New York"},
        "hobbies": ["reading", "hiking"],
    },
    {
        "id": 2,
        "name": "Bob",
        "info": {"age": 30, "city": "San Francisco"},
        "hobbies": ["cooking"],
    },
]

# Read the JSON data
df = pd.json_normalize(data=nested_json)
print(df)
'''
Output:
   id   name            hobbies  info.age      info.city
0   1  Alice  [reading, hiking]        25       New York
1   2    Bob          [cooking]        30  San Francisco
'''