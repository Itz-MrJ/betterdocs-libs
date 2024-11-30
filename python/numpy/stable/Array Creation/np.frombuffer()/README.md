# NumPy Array Creation Methods

## `np.frombuffer`

The `np.frombuffer` method interprets a buffer (e.g., a byte object) as a 1D array of the specified data type. It reads a specified number of elements from the buffer, with an optional offset.

### Example

```python
import numpy as np

buffer = bytes([1, 2, 3, 4])
arr = np.frombuffer(buffer, dtype=np.int8)
```

For a `detailed` usage, check out [BetterDocs - np.frombuffer()](https://betterdocs.tech/python/libs/numpy/stable/creation/frombuffer)