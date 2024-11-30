import numpy as np

# Create record array with shape
data = [(1, 2.5, 'foo'), (2, 3.5, 'bar')]
r_array = np.rec.array(data, shape=(2))
print(r_array.shape)  # Output: (2,)