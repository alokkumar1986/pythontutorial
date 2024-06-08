#Write a program to print 1 to 100 without a loop??
def print_numbers(n):
    if n<=100:
        print(n)
        print_numbers(n+1)
print_numbers(1)