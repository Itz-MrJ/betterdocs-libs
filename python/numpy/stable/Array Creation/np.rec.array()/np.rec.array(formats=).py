import numpy as np

# Create a record array
r_array = np.rec.array([(1, 2.5), (3, 4.0)], formats="i4,f4")

print(r_array)