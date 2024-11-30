import numpy as np

# Define dtype with fields
dtype = [('x', np.float32), ('y', np.int32), ('z', np.object_)]

# Create a record array
data = [(1, 2.5, 'foo'), (2, 3.5, 'bar')]
r_array = np.rec.array(data, dtype=dtype)
print(r_array)

"""
Output:
[(1., 2, 'foo') (2., 3, 'bar')]
"""
print(r_array.x)  # Output: [1. 2.]