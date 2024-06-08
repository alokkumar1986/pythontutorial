'''for i in range(1,10):
    if i==7:
        break
    print(i)
print('out of the loop')
'''


# Write a program to find the first 10 odd numbers from 200 to 1?
count = 0
for i in range(200, 1, -1):
    if i%2!=0:
        print(i)
        count+=1
    if count==10:
        break