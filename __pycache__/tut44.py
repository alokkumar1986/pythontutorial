#Write a program to find a pattern present in a given string or not

import re
count = 0
pattern = re.compile('java')
matches = re.finditer(pattern,  'Learning java is very easy java')
# print(matches)
for match in matches :
    print(match.start())  
    print(match.end())
    print(match.group())
    if match:
      count+=1   

if count>0 :
    print('The pattern is present in the given string', count )
   
else:
   print('The pattern is not present in the given string', count)
