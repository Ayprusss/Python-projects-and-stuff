x = float(input('Enter a non-negative value: '))
n = int(input('Enter the number of terms the program should be used for: '))

import math

def sine(x):
    sine = 0
    for p in range (0, n):
        sign = (-1) ** p
        sine = sine + ( x ** ((2 * p) + 1)) / (math.factorial((2 * p) + 1)) * sign
    return sine
    
output1 = "{:.7f}".format(sine(x))

print(output1)

def cos(x):
    cos = 0
    for o in range (0, n):
        sign2 = (-1) ** o
        cos = cos + (( x ** (2 * o)) / (math.factorial(2 * o))) * sign2
    return cos

output2 = "{:.7f}".format(cos(x))

print(output2)

