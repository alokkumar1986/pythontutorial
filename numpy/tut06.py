import numpy as np

#boolean Indexing

a = np.arange(0,10)

b = np.array([True, False,True, False, True, False,True, False,True, False])

print(a[b])

c = a>3

print(c)
print(a[c])