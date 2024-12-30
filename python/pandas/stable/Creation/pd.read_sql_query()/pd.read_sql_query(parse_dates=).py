import sqlite3
import pandas as pd

# Create an in-memory SQLite database and sample data
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table
cursor.execute('CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, salary REAL, date TEXT)')
cursor.executemany('INSERT INTO employees (name, salary, date) VALUES (?, ?, ?)', [('Alice', 75000.5, "2003-10-02"), ('Bob', 80000.0, '2003-04-16'), ('Chloe', 85000.0, '2023-12-29')])
conn.commit()

# Use pandas.read_sql_query to fetch data
df = pd.read_sql(sql="SELECT id, name, salary, date FROM employees", con=conn, parse_dates=["date"])
conn.close()
print(df['date'])
'''
Output:
0   2003-10-02
1   2003-04-16
2   2023-12-29
Name: date, dtype: datetime64[ns]
'''