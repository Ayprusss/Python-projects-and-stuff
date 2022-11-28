# Look for Pascal's Triangle formula
import math

n = int(input('Enter a positive integer:'))

for i in range(0, n): # number of rows to be printed
    for k in range (0, i + 1): # values in each row
        value = i - k
        print(int(math.factorial(i) / ((math.factorial(k)) * (math.factorial(value)))), end = ' ')
    print('') 
    