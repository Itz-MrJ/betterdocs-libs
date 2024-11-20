import numpy as np
import torch

# Creating a 2x2 tensor of zeros
tensor = torch.zeros((2,2))
arr = np.from_dlpack(tensor)

print(arr)
'''
Output: 
[[0. 0.]
 [0. 0.]]
'''