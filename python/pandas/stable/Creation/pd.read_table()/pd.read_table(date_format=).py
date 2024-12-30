import pandas as pd

# Example data with date-like strings
data = """ID,Name,BirthDate
1,Alice,2003-10-02
2,Bob,2003-04-16
3,Charlie,2023-12-29"""

# Write the data to a file
file_path = "parse_dates_example.csv"
with open(file_path, "w") as f:
    f.write(data)

# Reading the data with parse_dates=True and keep_date_col=True
df = pd.read_table(file_path, sep=',', header=0, parse_dates=["BirthDate"], date_format="%Y-%m-%d")

# Display the DataFrame
print(df['BirthDate'])
'''
Output:
0   2003-10-02
1   2003-04-16
2   2023-12-29
Name: BirthDate, dtype: datetime64[ns]
'''