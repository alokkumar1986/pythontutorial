'''
def fun1(a, c, b=10):
    print('a is :', a)
    print('b is :', b)
    print('c is :', c)

# fun1(10, 20, 30)
fun1(30, 40)
'''
def fun2(*n):
   for i in n:
     print(i)
fun2(2)
fun2(2, 7, 5, 6, 4)
