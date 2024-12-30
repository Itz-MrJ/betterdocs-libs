import pandas as pd
from io import StringIO

# Sample XML data
xml_data = """
<data>
    <employee id="1">
        <name>Alice</name>
        <hire_date>2003-10-02</hire_date>
        <salary>75000</salary>
    </employee>
    <employee id="2">
        <name>Bob</name>
        <hire_date>2003-04-16</hire_date>
        <salary>80000</salary>
    </employee>
    <employee id="3">
        <name>Chloe</name>
        <hire_date>2023-12-29</hire_date>
        <salary>85000</salary>
    </employee>
</data>
"""

# Use StringIO to simulate reading from a file
xml_file = StringIO(xml_data)

# Read XML data
df = pd.read_xml(xml_file, xpath=".//employee", elems_only=True)
print(df)
'''
Output:
    name   hire_date  salary
0  Alice  2003-10-02   75000
1    Bob  2003-04-16   80000
2  Chloe  2023-12-29   85000
'''