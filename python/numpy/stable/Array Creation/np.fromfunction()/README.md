# NumPy Array Creation Methods

## `np.fromfunction`

The `np.fromfunction` method creates an array by evaluating a function over a specified shape. The function is applied to each coordinate in the array.

### Example

```python
import numpy as np

arr = np.fromfunction(lambda i, j: i + j, (3, 3))
```

For a `detailed` usage, check out [BetterDocs - np.fromfunction()](https://betterdocs.tech/python/libs/numpy/stable/creation/fromfunction)