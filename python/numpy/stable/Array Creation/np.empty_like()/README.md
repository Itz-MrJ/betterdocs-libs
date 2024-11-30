# NumPy Array Creation Methods

## `np.empty_like`

The `np.empty_like` method creates a new array with the same shape and type as a given prototype array, but with uninitialized values. The contents are not initialized and may contain random values.

### Example

```python
import numpy as np

arr = np.empty_like(np.array([1, 2, 3]), dtype=int)
```

For a `detailed` usage, check out [BetterDocs - np.empty_like()](https://betterdocs.tech/python/libs/numpy/stable/creation/empty_like)