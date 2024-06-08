# s = 'This is a string'
# s1 = s.split() 
# print(s1) 
# for i in s1:
#    print(i)

# dt = '20-05-2024'
# dt1 = dt.split('-') 
# print(dt1)
# for n in dt1:
#   print(n)

# print(dt1[0])


# s = 'karthi sahasra sri nandyal india'
# l=s.split(' ', 1)  
# print(l)     
# for x in l: 
#  print(x)


# string.join(iterable)
# iterable/sequence : list, tuple, string, dict


# s = 'Aptech'
# print(s.join('Learning')) 

# t = ('John', 'Abraham', 'Bipasa')
# print('#'.join(t)) 

# d = { 
#     'name': 'ram',
#     'age' : 23
# }
# print('abc'.join(d))

# s = 'This is a string'
#This#is#a#string
#print("#".join(s))
# s1 = s.split()  #['This', 'is', 'a', 'string']
# print('#'.join(s1))

# s1 = reversed(s)
# print(s1)
# for i in s1:
#     print(i)

s = 'Aptech Learning at Bhubaneswar'
i = 0
while(i<len(s)) :
    if i==0 or i==(len(s)-1):
      print(s[i].upper(), end='')
    else:
      print(s[i].lower(), end='')
    i+=1