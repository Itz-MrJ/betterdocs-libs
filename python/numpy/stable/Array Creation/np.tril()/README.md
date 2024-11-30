# NumPy Array Creation Methods

## `np.tril`

The `np.tril` method returns the lower triangular part of a matrix, setting elements above the main diagonal to zero. You can specify which diagonal to consider using the `k` parameter.

### Example

```python
import numpy as np

# Create a matrix with the lower triangular part retained
arr = np.tril([[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=0)
```

For a `detailed` usage, check out [BetterDocs - np.tril()](https://betterdocs.tech/python/libs/numpy/stable/creation/tril)