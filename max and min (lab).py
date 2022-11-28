# Question 1: Three digit variables and give biggest and smallest 3-digit number of the list.

from tkinter import END


a = int(input ('Enter the first 3-digit number: '))
b = int(input ('Enter the second 3-digit number: '))
c = int(input ('Enter the third 3-digit number: '))

if a < 100 or b < 100 or c < 100:
    print(' Error: all numbers must be greater than 100. ')

if a > b and a > c:
    print(' your biggest number is', a)
elif a < b and a < c:
    print('your smallest number is', a)

if b > a and a > c:
    print('your biggest number is ', b)
elif b < a and b < c:
     print('your smallest number is', b)
    
if c > a and c > b:
    print('your biggest number is', c)
elif c < a and c < b:
    print('your smallest number is', c)

if a == b and b > c:
    print ('your maximum number is', a)
elif a == b and b < c:
    print ('your minimum number is', b)

if a == c and a > b:
    print ('your maximum number is', a)
elif a == c and a < b:
    print ('your minimum number is', a)

if b == c and b > a:
    print ('your maximum number is', b)
elif a == c and b <a:
    print (' your minimum number,', b)
    