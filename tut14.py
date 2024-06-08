'''a = int(input('Enter first number : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number : '))
#firstVal if condition else secondVal

d = a if a<b<c else (b if b<c else c)
print('Smallest is : ',d)'''


x, y = 10, 30

print('x is greater than y') if x>y else print('x is less than y') if x<y else print('Both x and y are equal')