# NumPy Array Creation Methods

## `np.meshgrid`

The `np.meshgrid` method generates coordinate matrices from coordinate vectors. It creates two or more 2D arrays representing the coordinate grid based on input 1D arrays. It can be used for evaluating functions on a grid.

### Example

```python
import numpy as np

x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 5)
X, Y = np.meshgrid(x, y)
```

For a `detailed` usage, check out [BetterDocs - np.meshgrid()](https://betterdocs.tech/python/libs/numpy/stable/creation/meshgrid)