import pandas as pd
import requests

# URL to the HDF5 file
url = "https://betterdocs.tech/global/python/pandas/data_large.h5"

# Download the file
response = requests.get(url)
with open("data.h5", "wb") as f:
    f.write(response.content)

# Read the HDF5 file locally
df = pd.read_hdf(path_or_buf="data.h5", stop=3)
print(df)
'''
Output:
   id           name   birthdate  age  salary
0   1     Eric Arias  1979-05-22   45  102905
1   2    Billy Silva  1998-03-13   26   87949
2   3  David Goodwin  1974-09-07   50   34936
'''