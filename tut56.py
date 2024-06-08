class Numbers:
    odd, even = [], []
    def findOddEven(self, a):
         for i in a:
              if i%2==0:
                   self.even.append(i)
              else : 
                   self.odd.append(i)
         print('Even are', self.even)
         print('Odd are', self.odd)


x = range(1, 100)
o = Numbers()
o.findOddEven(x)

# class className :
#      property
#      methods

# objName = className()

