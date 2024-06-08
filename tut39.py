#reduce(function, sequence)
from functools import reduce
'''
li = [10, 20, 30, 40, 50]
# def findSum(num, sum) :
#     return sum+num
findSum = lambda num,sum : sum+num
total = reduce(findSum, li)
print(total)   #150
'''
#Write a lamda function to reduce a list to find maximum value / element

li = [10, 20, 130, 40, 50]
findMax = lambda num, max : max if max>num else num
print('Maximum is : ', reduce(findMax, li))

