# from importlib.metadata import files
# f = open('demo.txt')
try :
  f = open('C:/Users/ISU_375/Desktop/files/instruction.txt', 'w')
  try :
    f.write('Lorem epsum')
  except:
    print('file is not found')
  finally :
    f.close()
    # print(f.readline())
    print('file is written and closed')
except FileNotFoundError:
  print('Something went wrong')