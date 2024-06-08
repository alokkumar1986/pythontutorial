class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age=age
        self.gender = gender

    def check(func):
        def inner_func(self):
            if(self.age<=0 and self.age<22) :
                self.age= 22
            if(self.gender!='Male' and self.gender!='Female'):
                self.gender= 'Male'
            func(self)
        return inner_func

    @check
    def show(self):
        print('Database operation')
        print('Data to be inserted :', self.name, self.age, self.gender)
        print('Data inserted')

s = Student('Ram', 55, 'Female')
s.show()