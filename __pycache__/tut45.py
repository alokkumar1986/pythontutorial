# pattern = [^a-zA-Z0-9]
# string = 'a7b@k9z'
import re
pattern = re.compile('\S')
matches = re.finditer(pattern, 'a7b@k9z')
for match in matches:
    print(match.start(), match.end(), match.group())
''' \s = Space character
    \S = any character except  space 
    \d = digit [0-9]
    \D = any character except digit [^0-9]
    \w = word character [a-zA-Z0-9]
    \W = any character except word character [^a-zA-Z0-9]
'''

    
