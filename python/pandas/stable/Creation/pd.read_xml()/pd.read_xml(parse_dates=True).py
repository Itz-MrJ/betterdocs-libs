import pandas as pd

# URL pointing to an XML file
url = "https://betterdocs.tech/global/python/pandas/read_xml.xml"

# Read the XML data from the URL into a DataFrame
df = pd.read_xml(path_or_buffer=url, parse_dates=['hire_date'])

# Display the DataFrame
print(df['hire_date'])
'''
Output:
0   2003-10-02
1   2003-04-16
2   2023-12-29
Name: hire_date, dtype: datetime64[ns]
'''