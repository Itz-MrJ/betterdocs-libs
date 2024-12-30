import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE emp (id INTEGER, name TEXT, salary REAL)')
cursor.executemany('INSERT INTO emp (id, name, salary) VALUES (?, ?, ?)', [(1, 'Alice', 75000.5), (2, 'Bob', 80000.0), (3, 'Chloe', 85000.0)])
conn.commit()


query = "SELECT * FROM emp"
df = pd.read_sql_query(sql=query, con=conn, chunksize=2)
print(next(df))
conn.close()
'''
Output:
   id   name   salary
0   1  Alice  75000.5
1   2    Bob  80000.0
'''