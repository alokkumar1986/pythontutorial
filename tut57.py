'''class Animal():
    def Speak(self):
        print('Animal can speak')

a = Animal()
a.Speak()'''
#===================================

'''class Animal():

    def __init__(self):
        pass
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y
    def showVal(self):
        print(self.x)
        print(self.y)

# a = Animal(10, 20)
# b = Animal(35, 45)

c = Animal()

# a.showVal()
# b.showVal()
c.showVal()
'''
#=======================================

class X():
    def __init__(self, x, y, z):
        self.p= x
        self.q= y
        self.r= z
    def __init__(self, p, q, r):
        self.p= p
        self.q= q
    
    def show(self):
        print(self.p)
        print(self.q)
        # print(self.r)

x = X(10, 20, 30)
x.show()

print(isinstance(x, X))

#====================
# class ParentClass():
#     properties


# class ChildClass(ParentClass):
#     properties
