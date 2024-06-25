import numpy as np

#1-D
# a = np.arange(1, 10)
# b = np.mean(a)
# print(b)

#2-D
a = np.array([
    [1, 2, 5],
    [3, 4, 6]
])
b = np.mean(a)
print(b)
c = np.mean(a, axis=0)
print(c)
d= np.mean(a, axis=1)
print(d)
