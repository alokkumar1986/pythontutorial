# b = [10, 20, 30, 40]
# print(type(b))
# m = bytes(b)
# print(type(m))
# print(m[1])
# m[0]=100
# print(m[0])

b = [10, 20, 30, 40]
print(type(b))
m = bytearray(b)
print(type(m))
print(m[0])
m[0]=100
print(m[0])

string = "Python Programming"
print(string[::-1])