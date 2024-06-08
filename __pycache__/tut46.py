'''
    a = Exactly one a 
    a+ = Atleast one a
    a* = Any number of a including 0
    a? = Atmost one a
    a{m} = Excatly m number of a
    a{m,n} = minimum m number of a and maximum n number of a
'''
import re
pattern = re.compile('[6-9]{1}[0-9]{9}')
matches = re.finditer(pattern, '7873965399')
for match in matches:
    print(match.start(), match.end(), match.group())

    #abcd@gao.cok  => [a-zA-Z0-9][@]{1}[a-zA-Z0-9][.]{1}[a-zA-Z0-9]