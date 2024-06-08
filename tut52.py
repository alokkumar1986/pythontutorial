# try :
#     f = open('demo1.txt', 'c')
# except :
#     print('File is not Created')
# # finally : 
# #     f.close()


try :
    f = open('demo1.txt', 'a')
    f.write('Aptech Learning')
except :
    print('file write is not allowed')
finally :
    f.close()