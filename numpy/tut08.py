import numpy as np

a = np.array([
    [1, 5, 9],
    [2, 4, 8]
    ])

b = np.sum(a, axis=0)

c = np.sum(a, axis=1)

print(b)

print(c)