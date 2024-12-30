import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE employees (id INTEGER, name TEXT, salary REAL)')
cursor.executemany('INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)', [(1, 'Alice', 75000.5), (2, 'Bob', 80000.0), (3, 'Chloe', 85000.0)])
conn.commit()

# Query with parameters using ?
query = "SELECT id, name, salary FROM employees WHERE salary > ?"
df = pd.read_sql_query(sql=query, con=conn, params=[78000.0])
conn.close()
print(df)
'''
Output:
   id   name   salary
0   2    Bob  80000.0
1   3  Chloe  85000.0
'''