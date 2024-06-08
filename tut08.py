'''s = {10, 20, 30}
m = frozenset(s) #immutable
print(type(s))
print(type(m))
s.add(50)
# m.add(60)
s.remove(10)
# m.remove(10)
print(s)
print(m)'''

'''
d = {'age': 24}
print(type(d))
#dictionaryName[key]=value
d['name'] = 'Aptech'
print(d)'''

r = range(10, 21)
#for item in r:
#    print(item)
print(r[0])
print(r[1:5])
print(r[-1])
# r[1] = 30

for i in r[1:5]:
    print(i)




