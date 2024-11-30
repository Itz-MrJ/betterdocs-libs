import numpy as np

# Generate 5 values logarithmically spaced between 1 and 10
result = np.geomspace(start=1, stop=10, num=5)
print(result) #Output: [ 1.          1.77827941  3.16227766  5.62341325 10.        ]