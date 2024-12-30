import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE employees (id INTEGER, name TEXT, salary REAL)')
cursor.executemany('INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)', [(1, 'Alice', 75000.5), (2, 'Bob', 80000.0), (3, 'Chloe', 85000.0)])
conn.commit()

df = pd.read_sql(sql="SELECT id, name FROM employees", con=conn, dtype={"id": "float16"})
print(df)
conn.close()
'''
Output:
    id   name
0  1.0  Alice
1  2.0    Bob
2  3.0  Chloe
'''