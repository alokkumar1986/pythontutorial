class Animal():
    def speak(self):
        print('The animal speak')

class Dog(Animal):
    def speak(self, bark):
        print('Dogs ', bark)

class Cat(Animal):
    def speak(self, animal, meow):
        print("The ", animal, meow)

c = Cat()
c.speak('Cat', 'meow')
d = Dog()
d.speak('bark')
# c.speak()
# d.speak()

#Method Overloading