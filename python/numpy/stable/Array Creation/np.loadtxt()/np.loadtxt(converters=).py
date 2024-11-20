import numpy as np

with open('data_converters.txt', 'w') as f:
    f.write("1.0, 2.0, A\n4.0, 5.0, B")

data = np.loadtxt('data_converters.txt', delimiter=',', converters={2: lambda s: ord(s.strip()) - ord('A')})
print(data)
# Output:
# [[1. 2. 0.]
#  [4. 5. 1.]]