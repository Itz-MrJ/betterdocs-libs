import pandas as pd

# URL pointing to an XML file
url = "https://betterdocs.tech/global/python/pandas/read_xml.xml"

# Read the XML data from the URL into a DataFrame
df = pd.read_xml(path_or_buffer=url, names=["ID", "Names", "Join Date", "Salary"])

# Display the DataFrame
print(df)
'''
Output:
   ID  Names   Join Date  Salary
0   1  Alice  2003-10-02   75000
1   2    Bob  2003-04-16   80000
2   3  Chloe  2023-12-29   85000
'''