# NumPy Array Creation Methods

## `np.triu`

The `np.triu` method returns the upper triangular part of a matrix, setting elements below the main diagonal to zero. You can specify which diagonal to consider using the `k` parameter.

### Example

```python
import numpy as np

# Create a matrix with the upper triangular part retained
arr = np.triu([[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=0)
```

For a `detailed` usage, check out [BetterDocs - np.triu()](https://betterdocs.tech/python/libs/numpy/stable/creation/triu)