class Num():
    def add(self, x, y):
        print(x+y)
    def add(self, x, y, z):
        print(x+y+z)
    
n = Num()

n.add(5,6)
n.add('Aptech ', 'Learning')

class Animal():
    def speak():
        print('Animal Speak')
class Dog(Animal):
    def speak():
        print('Dog Bark')

#=========================================
class A():
    def numtoWord(self,'234567'):
        pass

class B(A):
    def numtoword(self,'98765432'):
        pass

