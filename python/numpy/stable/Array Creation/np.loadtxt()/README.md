# NumPy Array Creation Methods

## `np.loadtxt`

The `np.loadtxt` method loads data from a text file and converts it into a NumPy array. You can specify options like data type, delimiter, which columns to use, and how to handle comments and rows to skip.

### Example

```python
import numpy as np

arr = np.loadtxt('data.txt', dtype=float, delimiter=',')
```

For a `detailed` usage, check out [BetterDocs - np.loadtxt()](https://betterdocs.tech/python/libs/numpy/stable/creation/loadtxt)