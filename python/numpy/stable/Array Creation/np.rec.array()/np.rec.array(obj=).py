import numpy as np

# Create a record array from a list of tuples
data = [(1, 'A', 2.5), (2, 'B', 3.7), (3, 'C', 1.9)]
r_array = np.rec.array(obj=data, dtype=[('id', np.float32), ('name', np.object_), ('value', np.float32)])
print(r_array)

# Output
# [(1., 'A', 2.5) (2., 'B', 3.7) (3., 'C', 1.9)]

print(r_array.id)  # Access 'id' field: [1. 2. 3.]
print(r_array.name)  # Access 'name' field: ['A' 'B' 'C']
print(r_array.value)  # Access 'value' field: [2.5 3.7 1.9]