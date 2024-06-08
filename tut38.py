# def sumNum(a, b):
#     return a+b

# sumNum = lambda a,b : a+b

# a = int(input('Enter first number :'))
# b = int(input('Enter second number :'))
# print('Sum of a and b is : ', sumNum(a,b) )

#============================================
'''li = [1, 3, 5, 7]
# def addTwo(num) :
#     return num+2
addTwo = lambda num :num+2
nli = map(addTwo, li)
for i in nli:
    print(i)
'''
#============================================
li = [1, 4, 5, 8, 9, 20, 23, 34, 56]
# def findEven(num):
#     if num%2==0:
#       return num
findEven = lambda num : num if num%2==0 else ''
nli = filter(findEven, li)
for i in nli:
    print(i)