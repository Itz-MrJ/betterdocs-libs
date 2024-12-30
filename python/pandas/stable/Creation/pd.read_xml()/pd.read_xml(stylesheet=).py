import pandas as pd
from io import StringIO

# Define the XML data as a string
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<data>
    <employee>
        <id>1</id>
        <name>Alice</name>
        <department>HR</department>
    </employee>
    <employee>
        <id>2</id>
        <name>Bob</name>
        <department>IT</department>
    </employee>
</data>"""

# Define the XSLT stylesheet as a string
xslt_data = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes"/>

    <!-- Root element -->
    <xsl:template match="/">
        <transformed_data>
            <xsl:apply-templates select="data/employee"/>
        </transformed_data>
    </xsl:template>

    <!-- Template for employee -->
    <xsl:template match="employee">
        <employee>
            <id><xsl:value-of select="id"/></id>
            <name><xsl:value-of select="name"/></name>
        </employee>
    </xsl:template>
</xsl:stylesheet>"""

xml_file = StringIO(xml_data)
xslt_file = StringIO(xslt_data)

# Read the XML data and apply the XSLT transformation
df = pd.read_xml(path_or_buffer=xml_file, stylesheet=xslt_file)
print(df)
'''
Output:
   id   name
0   1  Alice
1   2    Bob
'''