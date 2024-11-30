# NumPy Array Creation Methods

## `np.fromstring`

The `np.fromstring` method interprets a string as a sequence of data values and creates a 1D array. You can specify the data type, number of elements to read, and the separator between values.

### Example

```python
import numpy as np

arr = np.fromstring("1 2 3 4", dtype=int, sep=' ')
```

For a `detailed` usage, check out [BetterDocs - np.fromstring()](https://betterdocs.tech/python/libs/numpy/stable/creation/fromstring)