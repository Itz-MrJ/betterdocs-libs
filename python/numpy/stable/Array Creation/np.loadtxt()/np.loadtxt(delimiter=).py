import numpy as np

with open('data.txt', 'w') as f:
  f.write("1*2*3*4^*5")
arr_from_file = np.loadtxt(fname='data.txt',comments='^', delimiter='*')
print(arr_from_file)  # Output: [1. 2. 3. 4.]