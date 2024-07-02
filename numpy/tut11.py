import numpy as np

a = np.array([1, 3, 2, 0, -10, -5])

print(np.all(a)) #False

b = np.array([1, 3, 2, 10, -10, -5]) #

print(np.all(b)) # True

c = np.array([0,0,0, False])

print(np.any(c)) #False

d = np.array([0,0, 1, 0, False])

print(np.any(d)) #True


e = np.array([
    [1, 2],
    [3, 4]
])
print(np.all(e, axis=0)) #[True, True]
print(np.all(e, axis=1)) #[True, True]

f = np.array([
    [1, 2],
    [3, 0]
])
print(np.all(f, axis=0)) #[True, False]
print(np.all(f, axis=1)) #[True, False]