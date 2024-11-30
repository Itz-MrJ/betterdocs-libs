import numpy as np

# Generate 5 values logarithmically spaced between 1 and 1000
result = np.geomspace(start=1, stop=1000, num=5)
print(result) #Output: [   1.            5.62341325   31.6227766   177.827941   1000.        ]