import pandas as pd

# Sample nested JSON
nested_json = [
    {
        "id": 1,
        "name": "Alice",
        "info": {
            "age": 25,
            "city": "New York",
            "address": {
                "street": "5th Ave",
                "zip": "10001"
            }
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "info": {
            "age": 30,
            "city": "Berlin",
            "address": {
                "street": "Alexanderplatz",
                "zip": "10178"
            }
        }
    }
]

# Normalize the JSON with max_level=1 (only flatten 1 level)
df = pd.json_normalize(nested_json, max_level=1)
print(df)
'''
Output:
   id   name                                               info
0   1  Alice  {'age': 25, 'city': 'New York', 'address': {'s...
1   2    Bob  {'age': 30, 'city': 'Berlin', 'address': {'str...
'''