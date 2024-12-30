import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# Create a SQLite database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, salary INTEGER, department TEXT)')

# Insert sample data into the table
cursor.executemany('INSERT INTO employee (name, salary, department) VALUES (?, ?, ?)', [('Alice', 75000, 'HR'), ('Bob', 80000, 'Engineering'), ('Chloe', 85000, 'Marketing')])
conn.commit()
conn.close()

# Create SQLAlchemy engine for pandas to use
engine = create_engine('sqlite:///example.db')

# NOTE: read_sql only works with SQLAlchemy engines, not sqlite3 directly
df = pd.read_sql(sql='employee', con=engine, columns=["id", 'name'])
print(df)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
2   3  Chloe
'''