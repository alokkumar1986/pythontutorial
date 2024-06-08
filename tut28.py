'''for i in range(10):
    if i==6 or i==9:
        continue
    print(i)'''

'''flipkart_order = ['watch', 'mobile', 'laptop', 'bike']
for item in flipkart_order:
    if item =='laptop':
        continue
    print(item, ' is delivered.')
'''
#write a program to print first 10 numbers between 200 t0 1 where 2 is in unit place?

# 192
# 182
# 172
# 162
# 152
# 142
# 132
# 122
# 112
# 102
'''count = 0
for i in range(200, 1, -1):
    if i%10==2:
        print(i)
        count+=1
    if count==10:
        break'''

i = 14
if i%2==0:
    print('Number : ', 2)
    if i%3==0:
        print('Number : ', 3)
        if i%6==0:
            print('Number: ', 6)
print('Out of nested if')





       