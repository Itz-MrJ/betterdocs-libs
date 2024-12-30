import pandas as pd
import gzip

# Sample XML Data
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<data>
    <employee>
        <id>1</id>
        <name>Alice</name>
        <salary>75000</salary>
    </employee>
    <employee>
        <id>2</id>
        <name>Bob</name>
        <salary>80000</salary>
    </employee>
</data>"""

# Write XML data to a gzip-compressed file
with gzip.open("employees.xml.gz", "wt", encoding="utf-8") as f:
    f.write(xml_data)

# Read the compressed XML file
df = pd.read_xml("employees.xml.gz", compression="gzip")
print(df)
'''
Output:
   id   name  salary
0   1  Alice   75000
1   2    Bob   80000
'''