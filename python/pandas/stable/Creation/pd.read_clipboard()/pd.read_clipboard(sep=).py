import pandas as pd
import pyperclip

# Data to be copied to clipboard
data = """ID\tName\tAge
1\tAlice\t25
2\tBob\t30
3\tCharlie\t35
"""

# Copy the data to the clipboard
pyperclip.copy(data)

# Read the data from the clipboard using pandas
df = pd.read_clipboard(sep='\t')

# Print the DataFrame
print(df)

'''
Output:
   ID     Name  Age
0   1    Alice   25
1   2      Bob   30
2   3  Charlie   35
'''