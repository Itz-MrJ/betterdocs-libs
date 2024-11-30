# NumPy Array Creation Methods

## `np.tri`

The `np.tri` method creates a 2D array with ones below (or above) the main diagonal and zeros elsewhere. It is typically used for generating triangular matrices.

### Example

```python
import numpy as np

# Create a lower triangular matrix of ones
arr = np.tri(3, dtype=int)
```

For a `detailed` usage, check out [BetterDocs - np.tri()](https://betterdocs.tech/python/libs/numpy/stable/creation/tri)