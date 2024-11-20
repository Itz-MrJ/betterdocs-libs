import numpy as np
linspace_array = np.linspace(start=0, stop=1, num=5, retstep=True)
# Both 'start' & 'stop' are included
print(linspace_array)
'''
Output:
(array([0.  , 0.25, 0.5 , 0.75, 1.  ]), 0.25)
'''