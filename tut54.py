class X:
    x, y = 0, 0
    def printX(self, y):
        print(self.x+y)
    def __init__(self, x, y):
        print('Object Created.')
        self.x = x
        self.y = y

o = X(100, 50)
print(o.x)
# o.printX(100)
# o.printX(50)

a = X(200, 100)

print(a.x)
# o.printX(100)
# o.printX(50)