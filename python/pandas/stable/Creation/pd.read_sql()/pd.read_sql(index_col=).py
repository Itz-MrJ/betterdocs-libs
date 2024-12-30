import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE emp (id INTEGER, name TEXT, salary REAL)')
cursor.executemany('INSERT INTO emp (id, name, salary) VALUES (?, ?, ?)', [(1, 'Alice', 75000.5), (2, 'Bob', 80000.0), (3, 'Chloe', 85000.0)])
conn.commit()

df = pd.read_sql(sql="SELECT * FROM emp", con=conn, index_col="id")
print(df)
conn.close()
'''
Output:
     name   salary
id                
1   Alice  75000.5
2     Bob  80000.0
3   Chloe  85000.0
'''