import pandas as pd

# Sample nested JSON
nested_json = [
    {
        "id": 1,
        "name": "Alice",
        "info": {
            "age": 25,
            "city": "New York"
        }
    },
    {
        "id": 2,
        "name": "Bob",
        "info": {
            "age": 30,
            "city": "Berlin"
        }
    }
]

# Normalize the JSON with the separator
df = pd.json_normalize(data=nested_json, sep='|')
print(df)
'''
Output:
   id   name  info|age info|city
0   1  Alice        25  New York
1   2    Bob        30    Berlin
'''