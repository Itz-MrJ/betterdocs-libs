import pandas as pd
from io import BytesIO

# XML data as a string
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<data>
    <employee>
        <id>1</id>
        <name>Alice</name>
        <department>HR</department>
        <info salary="75000" hire_date="2003-10-02"/>
    </employee>
    <employee>
        <id>2</id>
        <name>Bob</name>
        <department>IT</department>
        <info salary="80000" hire_date="2010-05-15"/>
    </employee>
    <employee>
        <id>3</id>
        <name>Charlie</name>
        <info salary="85000" hire_date="2018-08-20"/>
    </employee>
</data>"""

# Encode the string to bytes
xml_bytes = xml_data.encode('utf-8')

# Use BytesIO to wrap the bytes
xml_file = BytesIO(xml_bytes)

# Read XML with iterparse
df = pd.read_xml(xml_file, iterparse={ "employee": ["id", "name", "info@salary", "info@hire_date"]})
print(df)
'''
Output:
   id     name
0   1    Alice
1   2      Bob
2   3  Charlie
'''