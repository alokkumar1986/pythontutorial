
'''#function definition
def calSum(a, b):
    print('sum is : ', a+b)

calSum(10, 20)  #function call
print('After first summation.')
calSum(20, 30)  #function call


def calSum(a, b):
   return a+b
print('Sum is : ', calSum(10, 20));
'''
#Write a program to find factorial of a number??

def factorialNum(a):
    fact = 1
    while(a>0) :
        fact *=a
        a-=1
    return fact   

num = int(input('Enter your number to find factorial '))
print('Factorial of ', num, ' is : ', factorialNum(num))

#Write a program to print Hello World using function

def printHello() :
    print('Hello World')

printHello()


