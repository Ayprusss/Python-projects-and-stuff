# program that receive positive integer and create Collatz sequence starting with integer. if Even number is odd; next number 3n + 1. if even; next number n/ 2; sequence stops when it reaches 1.

from turtle import end_fill


n = int(input('Enter an integer: '))

is_odd = True

print(n, end =',')

while n != 1:
    if n % 2 == 0:
        is_odd: False 
        n = n // 2
        print (n, end = ',')
    elif is_odd:
        n = (3 * n) + 1
        print (n, end =',')
