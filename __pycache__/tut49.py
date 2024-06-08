x = -1
if x<0:
  print(x)
  try :
   raise Exception('X can not be less than 0')
  except Exception:
   print('Exception handled')