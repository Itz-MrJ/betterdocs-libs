import numpy as np

with open('data_utf8.txt', 'w', encoding='utf-8') as f:
    f.write("1.0 2.0 3.0\n4.0 5.0 6.0")

data = np.loadtxt('data_utf8.txt', encoding='utf-8')
print(data)
# Output:
# [[1. 2. 3.]
#  [4. 5. 6.]]