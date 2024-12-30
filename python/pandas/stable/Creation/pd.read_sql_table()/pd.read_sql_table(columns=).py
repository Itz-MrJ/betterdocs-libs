import sqlite3
import pandas as pd
from sqlalchemy import create_engine

# Create a SQLite database connection
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('CREATE TABLE IF NOT EXISTS pcol (id INTEGER PRIMARY KEY, name TEXT, salary TEXT, date TEXT)')

# Insert sample data into the table
cursor.executemany('INSERT INTO pcol (name, salary, date) VALUES (?, ?, ?)', [('Alice', "75000.50", '2003-10-02'), ('Bob', "80000", '2003-04-16'), ('Chloe', "85000", '2023-12-29')])
conn.commit()
conn.close()

# Create SQLAlchemy engine for pandas to use
engine = create_engine('sqlite:///example.db')

# NOTE: read_sql_table only works with SQLAlchemy engines, not sqlite3 directly
df = pd.read_sql_table(table_name='pcol', con=engine, columns=["id", "name"])
print(df)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
2   3  Chloe
'''