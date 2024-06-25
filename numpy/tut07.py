import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6] 
])
#b = a[0:, 0:2]  #view of an array
b = a[0:, 0:2].copy() #copy of an array

print(b)
print(a)

b[0,0] = 0

print(b)
print(a)