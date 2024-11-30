# NumPy Array Creation Methods

## `np.rec.array`

The `np.rec.array` method creates a record array, which is a structured array with fields that can be accessed like attributes. You can specify formats, names, and other attributes to customize the record array.

### Example

```python
import numpy as np

arr = np.rec.array([(1, 2.0), (3, 4.5)], dtype=[('x', 'i4'), ('y', 'f4')])
```

For a `detailed` usage, check out [BetterDocs - np.rec.array()](https://betterdocs.tech/python/libs/numpy/stable/creation/rec.array)