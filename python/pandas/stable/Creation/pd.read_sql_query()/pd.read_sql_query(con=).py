import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table
cursor.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT)')
cursor.executemany('INSERT INTO employees (name, salary, department) VALUES (?, ?, ?)', [('Alice', 75000.5, 'HR'), ('Bob', 80000.0, 'Engineering'), ('Chloe', 85000.0, 'Marketing')])
conn.commit()

# Use pandas.read_sql_query to fetch data
query = "SELECT id, name, salary FROM employees WHERE department = 'HR'"
df = pd.read_sql_query(sql=query, con=conn)
conn.close()
print(df)
'''
Output:
   id   name   salary
0   1  Alice  75000.5
'''