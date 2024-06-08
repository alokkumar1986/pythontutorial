# x = 10
# try: 
#  print(x)
# except:
#  print('x is not defind')
# else: 
#  print('x is defined and used')
# finally:
#  print('we are in finally block which execute each time')

x = 10
try: 
  y = x/0
  print(y)
except NameError: 
  print('x is not defind at NameError')
except ZeroDivisionError:
  print('We cant divide any number with 0')
except:
  print('x is not defind')