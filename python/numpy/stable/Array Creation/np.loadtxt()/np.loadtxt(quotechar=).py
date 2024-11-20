import numpy as np
from io import StringIO

s = StringIO('"BetterDocs, is just ""BETTER""!"')
data = np.loadtxt(s, dtype="U", delimiter=",", quotechar='"')
print(data) # Output: BetterDocs, is just "BETTER"!