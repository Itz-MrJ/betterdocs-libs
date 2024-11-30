# NumPy Array Creation Methods

## `np.fromfile`

The `np.fromfile` method reads data from a binary or text file and interprets it as a 1D array of the specified data type. It also allows for specifying the number of items to read, a separator (for text files), and an offset.

### Example

```python
import numpy as np

arr = np.fromfile('data.bin', dtype=np.int32)
```

For a `detailed` usage, check out [BetterDocs - np.fromfile()](https://betterdocs.tech/python/libs/numpy/stable/creation/fromfile)