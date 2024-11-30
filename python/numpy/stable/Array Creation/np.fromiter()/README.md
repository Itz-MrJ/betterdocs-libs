# NumPy Array Creation Methods

## `np.fromiter`

The `np.fromiter` method creates a 1D array by iterating over an iterable (like a list or generator). You can specify the data type and the number of items to read from the iterable.

### Example

```python
import numpy as np

arr = np.fromiter(range(5), dtype=int)
```

For a `detailed` usage, check out [BetterDocs - np.fromiter()](https://betterdocs.tech/python/libs/numpy/stable/creation/fromiter)