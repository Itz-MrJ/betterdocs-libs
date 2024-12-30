import pandas as pd

# Sample data with missing 'info' field in Bob's record
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
        # Missing the entire 'info' field
    },
    {
        "id": 3,
        "name": "Chloe",
        "info": {
            "age": 22,
            # Missing 'city' but 'info' exists
        }
    }
]

# Try to normalize the JSON with errors='ignore'
df = pd.json_normalize(
    data=nested_json,
    meta=["id", "name", ["info", "age"], ["info", "city"]],
    errors="ignore"
)
print(df)
'''
Output:
   id   name  info.age info.city
0   1  Alice      25.0  New York
1   2    Bob       NaN       NaN
2   3  Chloe      22.0       NaN
'''