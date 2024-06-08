
# def printHello(i) :
#     i+=1
#     print('Hello World')
#     if i<=10 :
#       printHello(i)

# i = 1
# printHello(i)


#Write a program to find factorial of a number??

def factorialNum(a):
    # while(a>0) :
    #     fact *=a
    #     a-=1
    if a==1:
      return 1
    else :
      return a*factorialNum(a-1) #recursive function 

num = int(input('Enter your number to find factorial '))
print('Factorial of ', num, ' is : ', factorialNum(num))


