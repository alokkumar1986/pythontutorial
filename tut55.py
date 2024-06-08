# Program to find sum of two numbers using class

class Numbers:
    fnum, snum= 0,0
    def __init__(self, a, b) :
         self.fnum = a
         self.snum = b
    def findSum(self):
         print('Sum is :', self.fnum+self.snum)


x = int(input('Enter first number : '))
y = int(input('Enter second number : '))

o = Numbers(x, y)
o.findSum()

# 1) Default
# 2) Parameterized
# 3) Non-Parameterized



