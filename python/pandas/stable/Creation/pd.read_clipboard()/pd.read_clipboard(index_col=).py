import pandas as pd
import pyperclip

# Data to be copied to clipboard
data = """IDabcNameabcAge
1abcAliceabc25
2abcBobabc30
3abcCharlieabc35
"""

# Copy the data to the clipboard
pyperclip.copy(data)

# Read the data from the clipboard using pandas
df = pd.read_clipboard(sep='abc', index_col='ID')

# Print the DataFrame
print(df)

'''
Output:
       Name  Age
ID
1     Alice   25
2       Bob   30
3   Charlie   35
'''