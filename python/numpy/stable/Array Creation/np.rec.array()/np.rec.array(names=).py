import numpy as np
            
# Define names for fields
names = ('id', 'value', 'label')
# Create a record array with named fields
data = [(1, 2.5, 'A'), (2, 3.7, 'B')]
r_array = np.rec.array(data, names=names)
print(r_array)
            
"""
Output:
[(1, 2.5, 'A') (2, 3.7, 'B')]
"""
print(r_array.label)  # Output: ['A' 'B']