import pandas as pd
import requests

# URL to the HDF5 file
url = "https://betterdocs.tech/global/python/pandas/data_large.h5"

# Download the file
response = requests.get(url)
with open("data.h5", "wb") as f:
    f.write(response.content)

# Read the HDF5 file locally
df = pd.read_hdf(path_or_buf="data.h5", start=2)
print(df.head())
'''
Output:
   id             name   birthdate  age  salary
2   3    David Goodwin  1974-09-07   50   34936
3   4  Wendy Jones DVM  1968-07-23   56   67408
4   5     Becky Butler  1995-11-30   29  134267
5   6    Heather Frank  1985-12-13   39   48576
6   7       John Hicks  1978-12-03   46   49362
'''