# NumPy Array Creation Methods

## `np.vander`

The `np.vander` method creates a Vandermonde matrix from a given 1D array. The matrix is formed by raising the input array elements to successive powers, either in decreasing or increasing order.

### Example

```python
import numpy as np

# Create a Vandermonde matrix
arr = np.vander([1, 2, 3], increasing=True)
```

For a `detailed` usage, check out [BetterDocs - np.vander()](https://betterdocs.tech/python/libs/numpy/stable/creation/vander)