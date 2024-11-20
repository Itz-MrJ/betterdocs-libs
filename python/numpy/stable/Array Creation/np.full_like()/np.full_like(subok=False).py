import numpy as np

class MyArray(np.ndarray):
    pass  # Just a subclass for demonstration

# Create an instance of MyArray
my_array = np.array([[1, 2, 3], [4, 5, 6]]).view(MyArray)
print("Original type:", type(my_array))  # Output: <class '__main__.MyArray'>

# Using np.full_like with subok=False
result_subok = np.full_like(my_array, fill_value=False, subok=False)
print("With subok=False:", type(result_subok))  # Output: <class 'numpy.ndarray'>