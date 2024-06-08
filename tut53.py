import os

if(os.path.exists('demo1.txt')):
    os.remove('demo1.txt')
else: 
    print('file doesnot exists')

# os.rmdir('aptech')
os.mkdir('apetch')