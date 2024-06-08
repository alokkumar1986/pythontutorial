'''def greeting(name) :
    print('Hello ', name)
greeting('Aptech')
wish = greeting  #alias name
wish('Ram')
del(greeting)
# greeting('Shyam')
wish('Shyam')'''

def outer():
    print('Inside outer function')
    def inner():
        print('Inside inner function')
    print('Outside of Inner Function')
    inner()
outer()
