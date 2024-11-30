# NumPy Array Creation Methods

## `np.full_like`

The `np.full_like` method creates a new array with the same shape and type as a given prototype array, but with all elements set to a specified fill value.

### Example

```python
import numpy as np

arr = np.full_like(np.array([1, 2, 3]), 7, dtype=int)
```

For a `detailed` usage, check out [BetterDocs - np.full_like()](https://betterdocs.tech/python/libs/numpy/stable/creation/full_like)