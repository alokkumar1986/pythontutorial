'''def decor(func): #func is a function
    def inner_func():
        #body of inner function
    return inner_func
'''

class Demo():
    def decor(func):
        def inner_fun(self):
            print('Inner Decor Method')
            print(self.x, self.y)
            if(self.x<0):
                self.x=0
            if(self.y<0):
                self.y=0
            print(self.x, self.y)
            # func(self)
            return func(self)
        return inner_fun
    @decor
    def add(self):
        print('Inner add Method')
        print(self.x, self.y)
        return self.x+self.y
    
    def __init__(self, x, y):
        self.x=x
        self.y=y

d= Demo(-20, 50)
c = d.add()
print(c)