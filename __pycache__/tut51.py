# try :
#     f = open('demo.txt', 'r')
#     print(f.read(11))
# except :
#     print('File read is not allowed')


try :
    f = open('demo.txt', 'r')
    print(f.readline())
    print(f.readline())
    print(f.readline())

    print(f.read())
except :
    print('File read is not allowed')

finally:
    f.close()