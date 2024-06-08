# s = 'APTECH'
# print(s.lower())

# s = 'aptech'
# print(s.upper())
# print(s.capitalize())

# name = ' Hyderabad City '
# print(name)
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())
# print(len(name))


s = 'abcdbababbbabcdabb'
print(s.find('abc'))
print(s.rfind('abc'))
print(s.find('xyz'))

print(s.index('abc'))
print(s.rindex('abc'))
# print(s.index('xyz'))

print(s.count('ab'))
print(s.count('abc'))
print(s.count('xyz'))

print(s.count('ab', 2, 7))  #string.count(substring, startIndex, endIndex)

s = 'Hello Bhubaneswar'
print(s.replace('Bhubaneswar', 'Aptech')) #Hello Aptech