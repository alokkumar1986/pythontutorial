from abc import ABC, abstractmethod

class Demo(ABC):
    @abstractmethod
    def show1(self):
        print('Abstract method show1')
    def show2(self):
        print('Normal method show2')

class XYZ(Demo):
    def show1(self):
        print('Abstract method show1 in child class')
    

x = XYZ()
x.show1()
x.show2()


