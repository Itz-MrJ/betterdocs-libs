import pandas as pd
from io import StringIO

# XML data with namespaces
xml_data = """
<library xmlns:ns="http://example.com/ns">
    <ns:book>
        <ns:title>Python Programming</ns:title>
        <ns:author>John Doe</ns:author>
        <ns:price>29.99</ns:price>
    </ns:book>
    <ns:book>
        <ns:title>Data Science with Python</ns:title>
        <ns:author>Jane Smith</ns:author>
        <ns:price>39.99</ns:price>
    </ns:book>
    <ns:magazine>
        <ns:title>Tech Trends</ns:title>
        <ns:issue>2023</ns:issue>
    </ns:magazine>
</library>
"""

# Use StringIO to simulate reading from a file
xml_file = StringIO(xml_data)

# Define the namespaces
namespaces = {
    'ns': 'http://example.com/ns'
}

# Read only 'book' elements using the defined namespace and XPath
df = pd.read_xml(xml_file, xpath=".//ns:book", namespaces=namespaces)
print(df)
'''
Output:
                      title      author  price
0        Python Programming    John Doe  29.99
1  Data Science with Python  Jane Smith  39.99
'''