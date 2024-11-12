import numpy as np

class MyArray(np.ndarray):
    pass  # Just a subclass for demonstration

# Create an instance of MyArray
my_array = np.array([[1, 2, 3], [4, 5, 6]]).view(MyArray)
print("Original type:", type(my_array))  # Output: <class '__main__.MyArray'>

# Using np.array with subok=False
result_subok_false = np.array(my_array, subok=False)
print("With subok=False:", type(result_subok_false))  # Output: <class 'numpy.ndarray'>