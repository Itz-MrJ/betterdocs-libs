import pandas as pd
from io import StringIO

# Sample XML data with attributes and text content
xml_data = """
<data>
    <employee id="1" department="HR">
        <name>Alice</name>
        <hire_date>2003-10-02</hire_date>
        <salary>75000</salary>
    </employee>
    <employee id="2" department="Finance">
        <name>Bob</name>
        <hire_date>2003-04-16</hire_date>
        <salary>80000</salary>
    </employee>
    <employee id="3" department="IT">
        <name>Chloe</name>
        <hire_date>2023-12-29</hire_date>
        <salary>85000</salary>
    </employee>
</data>
"""

# Use StringIO to simulate a file-like object
xml_file = StringIO(xml_data)

# Read XML data
df = pd.read_xml(xml_file, xpath=".//employee", attrs_only=False)
print(df)
'''
Output:
   id department   name   hire_date  salary
0   1         HR  Alice  2003-10-02   75000
1   2    Finance    Bob  2003-04-16   80000
2   3         IT  Chloe  2023-12-29   85000
'''