import pandas as pd

# URL pointing to an XML file
url = "https://betterdocs.tech/global/python/pandas/read_xml.xml"

def half_sal(sal):
  return int(sal)/2

# Read the XML data from the URL into a DataFrame
df = pd.read_xml(path_or_buffer=url, converters={'salary': half_sal})

# Display the DataFrame
print(df)
'''
Output:
   id   name   hire_date   salary
0   1  Alice  2003-10-02  37500.0
1   2    Bob  2003-04-16  40000.0
2   3  Chloe  2023-12-29  42500.0
'''